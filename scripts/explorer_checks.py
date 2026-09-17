"""Browser zoom and animated-map checks shared with the explorer smoke test."""

import json
from pathlib import Path
import tempfile

from playwright.sync_api import expect


def check_browser_zoom(engine, url):
    """Real tab zoom in an isolated profile, not device scaling or CSS zoom.

    https://playwright.dev/python/docs/chrome-extensions
    https://developer.chrome.com/docs/extensions/reference/api/tabs#method-setZoom
    """
    with tempfile.TemporaryDirectory() as temp:
        extension = Path(temp) / "extension"
        extension.mkdir()
        (extension / "manifest.json").write_text(json.dumps({
            "manifest_version": 3, "name": "Local zoom verification", "version": "1.0",
            "background": {"service_worker": "worker.js"},
        }))
        (extension / "worker.js").write_text("chrome.runtime.onInstalled.addListener(() => {});")
        context = engine.launch_persistent_context(
            str(Path(temp) / "profile"), channel="chromium", headless=True, viewport=None,
            args=[f"--disable-extensions-except={extension}", f"--load-extension={extension}"],
        )
        try:
            worker = context.service_workers[0] if context.service_workers else context.wait_for_event("serviceworker")
            page = context.pages[0]
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(url)
            expect(page.locator("body")).to_have_attribute("data-view", "home")
            base_width = page.evaluate("innerWidth")
            base_density = page.evaluate("devicePixelRatio")
            routes = [
                ("home", ""), ("overview", "#graph=qft&view=overview"),
                ("atlas", "#graph=qft&view=atlas"), ("core", "#graph=qft&view=core"),
                ("browse", "#graph=qft&view=browse"),
                ("network", "#graph=qft&node=qft.abelian-curvature-from-holonomy"),
                ("overlap", "#graph=qft&view=overlap"),
                ("map", "#graph=qft-path-integrals&view=map"),
            ]
            for scale in (1, 1.25, 1.5, 2, 3, 4):
                worker.evaluate("""async scale => {
                    const [tab] = await chrome.tabs.query({active: true, currentWindow: true});
                    await chrome.tabs.setZoom(tab.id, scale);
                }""", scale)
                for view, route in routes:
                    page.goto(url + route)
                    expect(page.locator("body")).to_have_attribute("data-view", view)
                    assert abs(page.evaluate("innerWidth") - base_width / scale) < 2
                    assert abs(page.evaluate("devicePixelRatio") / base_density - scale) < 0.02
                    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), (scale, view)
                    assert page.locator("button,input,select").evaluate_all("""es => es
                        .filter(e => e.getClientRects().length && !e.closest('svg,dialog,#board,#core-world,#graph-world'))
                        .every(e => { const r=e.getBoundingClientRect(); return r.left>=-1 && r.right<=innerWidth+1; })"""), (scale, view)
                    for identity in ("board", "core-scroll", "graph-scroll", "concept-map-scroll", "atlas-scroll"):
                        target = page.locator("#" + identity)
                        if target.is_visible():
                            assert target.bounding_box()["height"] >= 120, (scale, view, identity)
                    if view == "atlas":
                        page.locator("#atlas-expand").click()
                        assert page.locator("#atlas-scroll").bounding_box()["height"] >= 70
                        page.keyboard.press("Escape")
                        expect(page.locator("#atlas-expand")).to_have_attribute("aria-pressed", "false")
                    if view == "overview":
                        page.locator("#overview-setup").click()
                        expect(page.locator("#about-dialog")).to_be_visible()
                        page.locator("#about-close").click()
                    if view == "browse":
                        page.locator("#search").fill("scalar")
                        expect(page.locator("#search-view")).to_be_visible()
                        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1")
            assert not errors, errors
            print("Chromium native browser zoom: 100–400%, every explorer screen, search, setup dialog and full-screen controls passed.")
        finally:
            context.close()


def check_atlas_transition(engine, url):
    browser = engine.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    try:
        page.goto(url + "#graph=qft&view=atlas")
        expect(page.locator("#atlas-view")).to_be_visible()
        expect(page.locator(".atlas-point")).to_have_count(27)
        assert page.locator("#atlas-scroll").evaluate("e=>e.scrollWidth<=e.clientWidth+1 && e.scrollHeight<=e.clientHeight+1")
        selected = page.locator(".atlas-point").first.get_attribute("data-concept")
        page.locator(".atlas-point").first.click()
        page.locator("#atlas-toggle-view").click()
        expect(page.locator(".atlas-point")).to_have_count(82)
        assert page.evaluate("document.getAnimations().some(a=>a.playState==='running')")
        # Reverse while motion is in flight: no stale ghosts or disabled controls.
        page.locator("#atlas-toggle-view").click()
        expect(page.locator(".atlas-point")).to_have_count(27)
        page.wait_for_function("() => !document.getAnimations().some(a=>a.playState==='running')")
        expect(page.locator(".atlas-departing")).to_have_count(0)
        expect(page.locator(f'.atlas-point[data-concept="{selected}"]')).to_have_attribute("aria-pressed", "true")
        page.emulate_media(reduced_motion="reduce")
        page.locator("#atlas-toggle-view").click()
        assert not page.evaluate("document.getAnimations().some(a=>a.playState==='running')")
        page.set_viewport_size({"width": 390, "height": 844})
        # Linux reserves scrollbar width; macOS normally overlays scrollbars.
        page.wait_for_function("""() => {
            const width = document.getElementById('atlas-scroll').clientWidth;
            return width >= 350 && width <= 390;
        }""")
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1")
        page.locator("#atlas-compare").click()
        expect(page.locator("#atlas-detail h2")).to_be_in_viewport()
        page.locator(".atlas-return").click()
        expect(page.locator("#atlas-toggle-view")).to_be_in_viewport()
        print(f"{engine.name}: reversible finite transitions, preserved selection, reduced motion and narrow-screen detail return passed.")
    finally:
        browser.close()
