"""Real-size graph browsing, mobile, source privacy, and static hosting checks."""

from functools import partial
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen

from playwright.sync_api import sync_playwright, expect

from syllabusgraph.site import SiteHandler, build_catalog

ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory() as temp:
        output = Path(temp) / "web"
        catalog = build_catalog(ROOT / "site/catalog.json", output)
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SiteHandler, directory=output))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{server.server_port}"
        try:
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
                page.goto(url)
                page.wait_for_selector(".result")
                assert page.locator("#result-count").inner_text() == "2,156 concepts"
                assert (
                    page.locator("#review-status").inner_text()
                    == "Model-reviewed · Human audit pending"
                )
                page.locator("#search").fill("Abelian curvature")
                page.locator(".result").first.click()
                assert page.locator("#detail .evidence").count() > 0
                assert page.locator("#detail .connection").count() > 0
                node_url = page.url
                label = page.locator("#detail h2").inner_text()
                page.reload()
                page.wait_for_selector("#detail .badge")
                assert page.locator("#detail h2").inner_text() == label
                page.locator("#detail .origin button").first.click()
                expect(page.locator("#graph-select")).not_to_have_value("qft")
                page.wait_for_selector("#detail .badge")
                assert page.locator("#detail .evidence").count() > 0
                page.goto(url)
                page.wait_for_selector(".result")
                page.locator("#overlap-tab").click()
                assert page.locator(".pair").count() == 6
                count = int(page.locator(".pair strong").first.inner_text().replace(",", ""))
                page.locator(".pair").first.click()
                assert page.locator("#result-count").inner_text() == f"{count:,} concepts · overlap"
                page.locator("#clear").click()
                page.locator("#search").fill("zzzyyy-no-matching-concept")
                assert page.locator("#result-count").inner_text() == "0 concepts"
                page.locator("#clear").click()
                page.locator("#zoom-in").click()
                page.locator("#fit").click()
                with page.expect_download() as dl:
                    page.locator("#download").click()
                data = json.loads(Path(dl.value.path()).read_text())
                assert len(data["knowledge"]["nodes"]) == 2156
                assert len(data["knowledge"]["edges"]) == 3319
                page.locator("#copy-prompt").click()
                assert "SETUP.md" in page.evaluate("navigator.clipboard.readText()")
                for entry in catalog["graphs"]:
                    page.locator("#graph-select").select_option(entry["id"])
                    expect(page.locator("#result-count")).to_have_text(f"{entry['nodes']:,} concepts")
                page.goto(node_url)
                page.wait_for_selector("#detail .badge")
                for width in (390, 768, 1440):
                    page.set_viewport_size({"width": width, "height": 900})
                    assert not page.evaluate("document.documentElement.scrollWidth > innerWidth")
                    assert page.locator("#detail h2").is_visible()
                assert not errors, errors
                browser.close()
            print(
                "Explorer: 5 full-size graphs, evidence, origins, overlap, deep links, download, clipboard, mobile, and private-path checks passed."
            )
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    main()
