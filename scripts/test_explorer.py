"""Exercise reading, following, expanding, and sharing real public graphs."""

from collections import Counter
from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
from threading import Thread
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen

from playwright.sync_api import sync_playwright, expect

from syllabusgraph.cli import initialize
from syllabusgraph.site import SiteHandler, build_catalog, build_site

ROOT = Path(__file__).resolve().parents[1]


def displayed(page):
    return set(page.locator(".graph-card").evaluate_all("cards => cards.map(c => c.dataset.node)"))


def reveal_lanes(page):
    # Every collapsed lane must be reachable; this is not a retry loop.
    for _ in range(200):
        if not page.locator(".lane-more").count():
            return
        page.locator(".lane-more").first.click()
    raise AssertionError("Lane expansion did not terminate")


def main():
    with tempfile.TemporaryDirectory() as temp:
        output = Path(temp) / "web"
        catalog = build_catalog(ROOT / "site/catalog.json", output)
        payload = json.loads((output / "data/qft.json").read_text(encoding="utf-8"))
        nodes = {n["id"]: n for n in payload["knowledge"]["nodes"]}
        edges = payload["knowledge"]["edges"]
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SiteHandler, directory=output))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}"
        try:
            with urlopen(url + "/catalog.json") as response:
                assert response.headers["Cache-Control"] == "no-store"
            for path in (
                "/.syllabusgraph/agent-policy.json",
                "/materials/book.pdf",
                "/data/",
                "/../SETUP.md",
            ):
                try:
                    urlopen(url + path)
                    raise AssertionError("Private or directory path was served")
                except HTTPError as exc:
                    assert exc.code == 404
            with sync_playwright() as p:
                browser = p.chromium.launch()
                context = browser.new_context(
                    viewport={"width": 1440, "height": 1000},
                    permissions=["clipboard-read", "clipboard-write"],
                )
                page = context.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                page.goto(url)
                page.wait_for_selector("#board .concept-card")
                assert (
                    page.locator("#review-status").inner_text()
                    == "Model-reviewed · Human audit pending"
                )
                assert page.locator("#reading-select option").count() == 4
                view = payload["reading_views"][0]
                assert page.locator(".chapter").count() == len(view["chapters"])
                assert set(
                    page.locator("#board .concept-card").evaluate_all(
                        "cs=>cs.map(c=>c.dataset.node)"
                    )
                ) == {n for c in view["chapters"] for n in c["nodes"]}
                page.locator("#chapter-jump").select_option(view["chapters"][8]["id"])
                # Scroll movement is asynchronous, but the chosen column must enter view.
                expect(page.locator(".chapter").nth(8)).to_be_in_viewport()
                page.locator("#reading-select").select_option(payload["reading_views"][1]["id"])
                expect(page.locator("#reading-title")).to_have_text("Schwartz")
                page.locator("#all-concepts").click()
                expect(page.locator("#result-count")).to_contain_text("2,156 concepts")
                assert page.locator("#results .concept-card").count() == 60
                page.locator("#more").click()
                assert page.locator("#results .concept-card").count() == 120

                page.locator("#search").fill("Abelian curvature")
                page.locator("#results .concept-card").first.click()
                root = page.locator(".graph-card.selected").get_attribute("data-node")
                label = nodes[root]["label"]
                expect(page.locator("#network-title")).to_have_text(label)
                assert page.locator(".selected .card-label").inner_text() == label
                node_url = page.url
                before = displayed(page)
                page.locator(".graph-card .expand-node").filter(has_text="+ Reveal").first.click()
                assert before < displayed(page)
                page.locator("#reset-network").click()
                assert displayed(page) == before
                neighbor = page.locator(".graph-card:not(.selected) .graph-node").first
                neighbor_label = neighbor.locator(".card-label").inner_text()
                neighbor.click()
                expect(page.locator("#network-title")).to_have_text(neighbor_label)
                page.locator("#back").click()
                expect(page.locator("#network-title")).to_have_text(label)
                page.locator("#zoom-in").click()
                expect(page.locator("#zoom-label")).to_have_text("110%")
                page.locator("#fit").click()
                expect(page.locator("#zoom-label")).to_have_text("100%")
                page.reload()
                expect(page.locator("#network-title")).to_have_text(label)
                page.locator("#detail-open").click()
                assert page.locator("#detail .evidence").count() > 0
                assert page.locator("#detail .connection").count() > 0
                page.locator("#detail .origin button").first.click()
                expect(page.locator("#graph-select")).not_to_have_value("qft")
                expect(page.locator(".graph-card.selected")).to_be_visible()
                page.locator("#detail-open").click()
                assert page.locator("#detail .evidence").count() > 0
                page.go_back()
                expect(page.locator("#network-title")).to_have_text(label)

                # Independently calculate every direct neighbor of the busiest concept.
                degree = Counter(endpoint for e in edges for endpoint in (e["from"], e["to"]))
                dense = degree.most_common(1)[0][0]
                page.goto(url + "#" + urlencode({"graph": "qft", "node": dense}))
                expect(page.locator("#network-title")).to_have_text(nodes[dense]["label"])
                all_neighbors = {dense} | {
                    e["to"] if e["from"] == dense else e["from"]
                    for e in edges
                    if dense in (e["from"], e["to"])
                }
                assert len(displayed(page)) < len(all_neighbors)
                reveal_lanes(page)
                assert displayed(page) == all_neighbors
                # Full prerequisite trace must have exactly the recorded transitive closure.
                ancestors, queue = {dense}, [dense]
                while queue:
                    id = queue.pop()
                    for e in edges:
                        if (
                            e["relation"] == "prerequisite"
                            and e["to"] == id
                            and e["from"] not in ancestors
                        ):
                            ancestors.add(e["from"])
                            queue.append(e["from"])
                page.locator("#trace").click()
                reveal_lanes(page)
                assert displayed(page) == ancestors
                assert not page.locator(".graph-edge.other").count()
                assert not page.locator(".graph-card .card-label").evaluate_all(
                    "cs => cs.some(c => c.scrollHeight > c.clientHeight + 1 || c.scrollWidth > c.clientWidth + 1)"
                )

                page.locator("#overlap-tab").click()
                assert page.locator(".pair").count() == 6
                pair = page.locator(".pair").first.get_attribute("data-books").split(",")
                count = sum(set(pair) <= set(books) for books in payload["direct_books"].values())
                expect(page.locator(".pair strong").first).to_have_text(f"{count:,}")
                page.locator(".pair").first.click()
                expect(page.locator("#result-count")).to_contain_text(f"{count:,} concepts")
                page.locator("#search").fill("zzzyyy-no-matching-concept")
                expect(page.locator("#result-count")).to_have_text("0 concepts")
                page.locator("#clear").click()
                with page.expect_download() as dl:
                    page.locator("#download").click()
                downloaded = json.loads(Path(dl.value.path()).read_text(encoding="utf-8"))
                assert downloaded["knowledge"] == payload["knowledge"]
                page.locator("#about-open").click()
                page.locator("#copy-prompt").click()
                assert "SETUP.md" in page.evaluate("navigator.clipboard.readText()")
                page.keyboard.press("Escape")
                for entry in catalog["graphs"]:
                    page.locator("#graph-select").select_option(entry["id"])
                    expect(page.locator("#graph-count")).to_have_text(
                        f"{entry['nodes']:,} concepts · {entry['edges']:,} connections"
                    )
                    page.locator("#all-concepts").click()
                    expect(page.locator("#result-count")).to_contain_text(
                        f"{entry['nodes']:,} concepts"
                    )

                for width in (390, 768, 1440):
                    page.set_viewport_size({"width": width, "height": 900})
                    page.goto(node_url)
                    expect(page.locator("#network-title")).to_have_text(label)
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
                    expect(page.locator(".graph-card.selected")).to_be_in_viewport()
                    page.locator("#detail-open").click()
                    expect(page.locator("#detail h2")).to_be_visible()
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
                    page.locator("#detail .detail-top button").click()
                    page.locator("#chapters-tab").click()
                    expect(page.locator(".chapter").first).to_be_in_viewport()
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")

                # No inventory or subject-specific settings are required in new projects.
                for template in ("sampling", "blank"):
                    project = initialize(Path(temp) / template, template)
                    build_site([{"path": project.root}], output)
                    page.goto(url + "?example=" + template)
                    expect(page.locator("#reading-title")).to_have_text(project.config["title"])
                    page.locator("#all-concepts").click()
                    expect(page.locator("#result-count")).to_have_text(
                        f"{len(project.nodes)} concepts"
                    )
                assert not errors, errors
                browser.close()
            print(
                "Explorer passed: chapter browsing, full labels, search, expansion, exact prerequisite trace, evidence, book links/overlap, sharing, 5 graphs, generic/blank projects, mobile, CSP and private paths."
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    main()
