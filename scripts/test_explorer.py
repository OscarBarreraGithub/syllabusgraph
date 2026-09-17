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
from explorer_checks import check_atlas_transition, check_browser_zoom

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


def check_navigation(engine, url, pilot):
    """Use browser input, not assigned scroll offsets, to verify the workspace."""
    browser = engine.launch()
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    try:
        page.goto(url)
        expect(page.locator("#home-view")).to_be_visible()
        page.mouse.move(500, 600)
        page.mouse.wheel(0, 600)
        expect(page.locator("html")).not_to_have_js_property("scrollTop", 0)
        page.locator("#home-demo").click()
        page.locator("#overview-overlap").click()
        scroll = page.locator("#core-scroll")
        expect(scroll).to_be_visible()
        assert scroll.bounding_box()["height"] > 480
        box = scroll.bounding_box()
        page.mouse.move(box["x"] + 400, box["y"] + 200)
        page.mouse.wheel(0, 400)
        expect(scroll).not_to_have_js_property("scrollTop", 0)
        page.mouse.wheel(400, 0)
        expect(scroll).not_to_have_js_property("scrollLeft", 0)
        page.locator("#core-center").click()
        expect(scroll).to_have_js_property("scrollTop", 0)
        expect(scroll).to_have_js_property("scrollLeft", 0)

        # Dragging can begin on a card; releasing must not open that concept.
        card = page.locator(".core-card").first
        card.scroll_into_view_if_needed()
        box = card.bounding_box()
        page.mouse.move(box["x"] + 150, box["y"] + 25)
        page.mouse.down()
        page.mouse.move(box["x"] + 50, box["y"] - 35, steps=12)
        page.mouse.up()
        expect(scroll).to_be_visible()
        expect(scroll).not_to_have_js_property("scrollLeft", 0)
        expect(scroll).not_to_have_js_property("scrollTop", 0)
        for key, prop in (("ArrowDown", "scrollTop"), ("ArrowRight", "scrollLeft")):
            page.locator("#core-center").click()
            scroll.focus()
            page.keyboard.press(key)
            expect(scroll).not_to_have_js_property(prop, 0)
        for direction, prop in (("down", "scrollTop"), ("right", "scrollLeft")):
            page.locator("#core-center").click()
            page.locator("#core-pan-" + direction).click()
            expect(scroll).not_to_have_js_property(prop, 0)

        page.locator("#core-expand").click()
        expect(page.locator("#core-expand")).to_have_attribute("aria-pressed", "true")
        assert scroll.bounding_box()["height"] > 680
        assert scroll.bounding_box()["width"] == 1440
        page.keyboard.press("Escape")
        expect(page.locator("#core-expand")).to_have_attribute("aria-pressed", "false")
        page.locator("#core-center").click()
        for _ in range(4):
            page.locator("#core-zoom-out").click()
        expect(page.locator("#core-zoom-label")).to_have_text("60%")
        # At reduced zoom there must be no scrollable blank unscaled world.
        assert scroll.evaluate(
            "s => Math.abs(s.scrollWidth - document.getElementById('core-sizer').offsetWidth) <= 1"
        )
        page.locator("#core-jump").select_option("isolated")
        expect(page.locator(".core-component-title").last).to_be_in_viewport()
        page.locator("#comparison-mode").select_option("volumes")
        expect(page.locator(".core-card")).to_have_count(2)
        assert scroll.evaluate("s => s.scrollWidth <= s.clientWidth + 1")
        expect(page.locator(".core-card").first).to_be_in_viewport()
        page.locator("#overview-tab").click()
        page.reload()
        expect(page.locator("#overview-view")).to_be_visible()
        page.locator("#overview-wider").click()
        expect(page.locator(".core-card")).to_have_count(305)
        page.locator("#overview-tab").click()
        page.locator(".overview-book").first.click()
        expect(page.locator("#graph-select")).not_to_have_value("qft")
        expect(page.locator("#browse-view")).to_be_visible()

        for width, height in ((390, 844), (768, 900), (1280, 600)):
            page.set_viewport_size({"width": width, "height": height})
            page.goto(url + "?navigation=" + str(width))
            expect(page.locator("#home-view")).to_be_visible()
            assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
            page.locator("#home-demo").click()
            expect(page.locator("#overview-view")).to_be_visible()
            assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
            page.locator("#overview-overlap").click()
            page.locator("#core-pan-down").click()
            expect(scroll).not_to_have_js_property("scrollTop", 0)
            page.locator("#core-expand").click()
            assert scroll.bounding_box()["height"] > height * 0.55
            assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
            page.keyboard.press("Escape")
        # A concept layer must show exactly its reviewed records, fit the desktop,
        # and lead to the underlying evidence without losing the return route.
        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(url + "#graph=qft-path-integrals&view=map")
        points = page.locator(".concept-point")
        expect(points).to_have_count(len(pilot["nodes"]))
        assert set(points.evaluate_all("ps => ps.map(p => p.dataset.node)")) == {
            n["id"] for n in pilot["nodes"]
        }
        assert set(page.locator(".concept-link").evaluate_all(
            "ps => ps.map(p => p.dataset.edge)"
        )) == {e["id"] for e in pilot["edges"]}
        map_scroll = page.locator("#concept-map-scroll")
        assert map_scroll.evaluate(
            "s => s.scrollHeight <= s.clientHeight + 1 && s.scrollWidth <= s.clientWidth + 1"
        )
        assert points.evaluate_all("""ps => {
            const v = document.getElementById('concept-map-scroll').getBoundingClientRect();
            const boxes = ps.map(p => p.getBoundingClientRect());
            return boxes.every(b => b.top >= v.top && b.bottom <= v.bottom &&
                b.left >= v.left && b.right <= v.right) && boxes.every((a, i) =>
                boxes.slice(i + 1).every(b => a.right <= b.left || b.right <= a.left ||
                    a.bottom <= b.top || b.bottom <= a.top));
        }""")
        points.first.focus()
        page.keyboard.press("Enter")
        expect(points.first).to_have_attribute("aria-pressed", "true")
        expect(page.locator("#concept-map-detail h2")).to_have_text(
            points.first.get_attribute("aria-label")
        )
        page.locator("#concept-map-detail > button").click()
        expect(page.locator("#network-view")).to_be_visible()
        page.reload()
        page.locator("#back").click()
        expect(page.locator("#map-view")).to_be_visible()
        points.first.click()
        page.locator(".concept-treatment button").first.click()
        expect(page.locator("#graph-select")).not_to_have_value("qft-path-integrals")
        expect(page.locator("#network-view")).to_be_visible()
        page.go_back()
        expect(page.locator("#map-view")).to_be_visible()
        fitted = page.locator("#concept-map-svg").bounding_box()["width"]
        page.locator("#concept-map-in").click()
        assert page.locator("#concept-map-svg").bounding_box()["width"] > fitted
        page.locator("#concept-map-fit").click()
        assert abs(page.locator("#concept-map-svg").bounding_box()["width"] - fitted) < 1
        page.goto(url + "#graph=qft&view=core")
        expect(page.locator("#core-stats")).to_contain_text("78")
        page.locator("#core-concept-map").click()
        expect(page.locator("#atlas-view")).to_be_visible()
        page.goto(url + "#graph=qft-path-integrals&view=map")
        expect(page.locator("#map-view")).to_be_visible()
        page.set_viewport_size({"width": 390, "height": 844})
        assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
        map_scroll.focus()
        page.keyboard.press("ArrowRight")
        expect(map_scroll).not_to_have_js_property("scrollLeft", 0)
        page.keyboard.press("ArrowDown")
        expect(map_scroll).not_to_have_js_property("scrollTop", 0)

        if engine.name == "chromium":
            touch_context = browser.new_context(
                viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True
            )
            touch_page = touch_context.new_page()
            touch_page.goto(url)
            touch_page.locator("#home-demo").tap()
            touch_page.locator("#overview-overlap").tap()
            touch_scroll = touch_page.locator("#core-scroll")
            box = touch_scroll.bounding_box()
            session = touch_context.new_cdp_session(touch_page)
            # Native touch sequences, starting on a card, in each direction.
            for dx, dy, prop in ((0, 15, "scrollTop"), (12, 0, "scrollLeft")):
                x, y = 220, box["y"] + 180
                session.send("Input.dispatchTouchEvent", {
                    "type": "touchStart", "touchPoints": [{"x": x, "y": y}]
                })
                for step in range(1, 11):
                    session.send("Input.dispatchTouchEvent", {
                        "type": "touchMove",
                        "touchPoints": [{"x": x - step * dx, "y": y - step * dy}],
                    })
                    touch_page.wait_for_timeout(20)  # Pace the finger movement.
                session.send("Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
                expect(touch_scroll).not_to_have_js_property(prop, 0)
                expect(touch_page.locator("#core-view")).to_be_visible()
            touch_context.close()
        assert not errors, errors
        print(f"{engine.name}: overview scroll, graph wheel/drag/keyboard, pan buttons, zoom, expanded view, small screens passed.")
    finally:
        browser.close()


def check_atlas(engine, url, atlas):
    browser = engine.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    try:
        page.goto(url)
        page.locator("#home-demo").click()
        page.locator("#overview-explore").click()
        expect(page.locator("#atlas-view")).to_be_visible()
        points = page.locator(".atlas-point")
        actual = points.evaluate_all("ps=>ps.map(p=>p.dataset.concept)")
        by_id = {n["id"]: n for n in atlas["concepts"]}
        assert 0 < len(actual) <= 2 * len(atlas["groups"])
        assert all(len(by_id[id]["works"]) == len(atlas["works"]) for id in actual)
        assert points.evaluate_all("""ps=>{const boxes=ps.map(p=>p.getBoundingClientRect());
            return boxes.every((a,i)=>boxes.slice(i+1).every(b=>a.right<=b.left||b.right<=a.left||a.bottom<=b.top||b.bottom<=a.top));}""")
        valid = {(e["from"], e["to"]) for e in atlas["links"]}
        for edge in page.locator(".atlas-link").evaluate_all("es=>es.map(e=>[e.dataset.from,e.dataset.to])"):
            assert tuple(edge) in valid
        selected = actual[0]
        points.first.focus()
        page.keyboard.press("Enter")
        expect(points.first).to_have_attribute("aria-pressed", "true")
        expect(page.locator("#atlas-detail h2")).to_have_text(by_id[selected]["label"])
        neighbors = [e for e in atlas["links"] if selected in (e["from"], e["to"])]
        expect(page.locator(".atlas-neighbor")).to_have_count(len(neighbors))
        page.locator(".atlas-treatments summary").first.click()
        page.locator(".atlas-treatments button").first.click()
        expect(page.locator("#network-view")).to_be_visible()
        page.go_back()
        expect(page.locator("#atlas-detail h2")).to_have_text(by_id[selected]["label"])
        page.locator(".atlas-evidence-button").first.click()
        expect(page.locator("#atlas-detail h2")).to_contain_text("↔")
        expect(page.locator("#atlas-detail .atlas-treatments").first).to_be_visible()
        page.locator("#atlas-compare").click()
        expect(page.locator("#atlas-detail h2")).to_have_text("Compare the books")
        book_count = sum(len(w["projects"]) for w in atlas["works"])
        expect(page.locator("#atlas-detail .atlas-treatments")).to_have_count(book_count * (book_count - 1) // 2)
        page.locator("#atlas-detail-level").select_option("all")
        page.locator("#atlas-coverage").select_option("0")
        expect(points).to_have_count(len(atlas["concepts"]))
        assert set(points.evaluate_all("ps=>ps.map(p=>p.dataset.concept)")) == set(by_id)
        scroll = page.locator("#atlas-scroll")
        scroll.scroll_into_view_if_needed()
        box = scroll.bounding_box()
        page.mouse.move(box["x"] + 300, box["y"] + 250)
        page.mouse.wheel(0, 500)
        expect(scroll).not_to_have_js_property("scrollTop", 0)
        page.locator("#atlas-reset").click()
        expect(scroll).to_have_js_property("scrollTop", 0)
        page.locator("#atlas-zoom-in").click()
        page.locator("#atlas-zoom-in").click()
        scroll.focus()
        page.keyboard.press("ArrowRight")
        expect(scroll).not_to_have_js_property("scrollLeft", 0)
        page.locator("#atlas-reset").click()
        scroll.scroll_into_view_if_needed()
        box = scroll.bounding_box()
        page.mouse.move(box["x"] + 280, box["y"] + 250)
        page.mouse.down()
        page.mouse.move(box["x"] + 240, box["y"] + 100, steps=10)
        page.mouse.up()
        expect(scroll).not_to_have_js_property("scrollTop", 0)
        page.locator("#atlas-query").fill("no-such-concept-in-this-fixture")
        expect(page.locator("#atlas-map-caption")).to_contain_text("No matching")
        page.locator("#atlas-query").fill("")
        page.reload()
        expect(points).to_have_count(len(atlas["concepts"]))
        for width, height in [(390, 844), (768, 900), (1280, 600)]:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(url + "#graph=qft&view=atlas")
            expect(page.locator("#atlas-view")).to_be_visible()
            assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
            scroll.focus()
            page.keyboard.press("ArrowDown")
            expect(scroll).not_to_have_js_property("scrollTop", 0)
        assert not errors, errors
        print(f"{engine.name}: shared-concept overview, exact source links, coverage, search, history, wheel/drag/keyboard and narrow screens passed.")
    finally:
        browser.close()


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
                expect(page.locator("#home-view")).to_be_visible()
                expect(page.locator("#graph-select")).not_to_be_visible()
                page.locator("#home-copy").click()
                assert "SETUP.md" in page.evaluate("navigator.clipboard.readText()")
                assert "slow, checkpointed mode" in page.evaluate("navigator.clipboard.readText()")
                page.locator("#home-demo").click()
                expect(page.locator("#overview-title")).to_have_text(
                    "The ideas the books share."
                )
                expect(page.locator("#diagram-core-title")).to_have_text("Shared concepts")
                expect(page.locator("#diagram-core-count")).to_have_text(f"{payload['atlas']['counts']['all_works']} in every work")
                expect(page.locator("#overview-facts")).not_to_contain_text("78")
                expect(page.locator("#overview-intro")).to_contain_text("recognizable concepts")
                expect(page.locator("#overview-view .reading-guide h3").first).to_have_text(
                    "Start with the concept map"
                )
                expect(page.locator("#overview-books .overview-book")).to_have_count(4)
                page.locator("#overview-overlap").click()
                page.wait_for_selector("#core-cards .core-card")
                # Independently compute the intersection from exact book matches.
                grouped = {
                    n: {"weinberg" if b in {"weinberg-1", "weinberg-2"} else b for b in books}
                    for n, books in payload["direct_books"].items()
                }
                common = {id for id, books in grouped.items() if len(books) == 3}
                expected_edges = {
                    e["id"] for e in edges if e["from"] in common and e["to"] in common
                }
                assert len(common) == 78 and len(expected_edges) == 72
                assert (
                    set(page.locator(".core-card").evaluate_all("cs=>cs.map(c=>c.dataset.node)"))
                    == common
                )
                assert (
                    set(page.locator(".core-edge").evaluate_all("es=>es.map(e=>e.dataset.edge)"))
                    == expected_edges
                )
                expect(page.locator("#core-stats")).to_contain_text("25")
                expect(page.locator("#core-stats")).to_contain_text("Largest: 34 records")
                assert not page.locator("#browse-view").is_visible()
                page.locator(".core-card").first.click()
                expect(page.locator("#network-view")).to_be_visible()
                page.locator("#back").click()
                expect(page.locator("#core-view")).to_be_visible()
                page.locator("#comparison-mode").select_option("volumes")
                assert page.locator(".core-card").count() == 2
                assert page.locator(".core-edge").count() == 0
                page.reload()
                expect(page.locator("#comparison-mode")).to_have_value("volumes")
                expect(page.locator(".core-card")).to_have_count(2)
                page.locator("#comparison-mode").select_option("textbooks")
                page.locator("#core-threshold").select_option("2")
                assert page.locator(".core-card").count() == 305
                assert page.locator(".core-edge").count() == 335
                page.locator("#core-threshold").select_option("3")
                page.locator("#core-zoom-in").click()
                expect(page.locator("#core-zoom-label")).to_have_text("110%")
                page.locator("#core-center").click()
                expect(page.locator("#core-zoom-label")).to_have_text("100%")
                page.locator("#chapters-tab").click()
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
                expect(page.locator("#result-count")).to_contain_text("2,156 records")
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
                expect(page.locator("#result-count")).to_contain_text(f"{count:,} records")
                page.locator("#search").fill("zzzyyy-no-matching-concept")
                expect(page.locator("#result-count")).to_have_text("0 records")
                page.locator("#clear").click()
                expect(page.locator("#overview-view")).to_be_visible()
                page.locator("#overview-overlap").click()
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
                        f"{entry['nodes']:,} records · {entry['edges']:,} connections"
                    )
                    if entry.get("kind") == "concept-map":
                        expect(page.locator("#map-view")).to_be_visible()
                        page.locator("#overview-tab").click()
                    elif entry.get("atlas"):
                        expect(page.locator("#atlas-view")).to_be_visible()
                        page.locator("#overview-tab").click()
                    expect(page.locator("#overview-view")).to_be_visible()
                    page.locator("#overview-all").click()
                    expect(page.locator("#result-count")).to_contain_text(
                        f"{entry['nodes']:,} {'concepts' if entry['kind'] == 'concept-map' else 'records'}"
                    )

                for width in (390, 768, 1440):
                    page.set_viewport_size({"width": width, "height": 900})
                    page.goto(url + "?core-mobile=" + str(width))
                    page.locator("#home-demo").click()
                    expect(page.locator("#overview-view")).to_be_visible()
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
                    page.locator("#overview-overlap").click()
                    expect(page.locator("#core-view")).to_be_visible()
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
                    expect(page.locator("#core-stats")).to_contain_text("78")
                    if width == 390:
                        page.locator("#core-jump").select_option("isolated")
                        expect(page.locator(".core-component-title").last).to_be_in_viewport()
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
                    expect(page.locator("#home-view")).to_be_visible()
                    page.locator("#home-demo").click()
                    expect(page.locator("#overview-view")).to_be_visible()
                    expect(page.locator("#overview-facts")).to_contain_text(str(len(project.nodes)))
                    page.goto(url + "?example=" + template + "#view=browse")
                    expect(page.locator("#reading-title")).to_have_text(project.config["title"])
                    page.locator("#all-concepts").click()
                    expect(page.locator("#result-count")).to_have_text(
                        f"{len(project.nodes)} records"
                    )
                assert not errors, errors
                browser.close()
                build_catalog(ROOT / "site/catalog.json", output)
                pilot = json.loads((output / "data/qft-path-integrals.json").read_text())["knowledge"]
                for engine in (p.chromium, p.webkit):
                    check_navigation(engine, url, pilot)
                    check_atlas(engine, url, payload["atlas"])
                    check_atlas_transition(engine, url)
                check_browser_zoom(p.chromium, url)
            print(
                "Explorer passed: exact shared core, volume grouping, threshold controls, components, chapter browsing, full labels, search, expansion, exact prerequisite trace, evidence, book links/overlap, sharing, 6 graphs, generic/blank projects, mobile, CSP and private paths; compact concept map and actual wheel/drag/keyboard navigation in Chromium and WebKit."
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    main()
