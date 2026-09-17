"""Browser zoom and animated-map checks shared with the explorer smoke test."""

import json
from pathlib import Path
import tempfile

from playwright.sync_api import expect


def check_record_map(engine, url, payload):
    """Verify the useful journeys, the displayed graph, and finite camera motion."""
    browser = engine.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    try:
        page.goto(url + "#graph=qft&view=atlas")
        for name in ("core", "overlap", "overview", "atlas", "records"):
            page.locator(f"#{name}-tab").click()
            expect(page.locator("body")).to_have_attribute("data-view", name)
        # An accessibility anchor must not be interpreted as a different graph URL.
        route = page.url
        page.locator(".skip").focus()
        page.keyboard.press("Enter")
        expect(page.locator("#workspace")).to_be_focused()
        assert page.url == route
        points = page.locator(".record-point")
        expect(points).to_have_count(len(payload["knowledge"]["nodes"]))
        assert set(points.evaluate_all("ps=>ps.map(p=>p.dataset.node)")) == {
            n["id"] for n in payload["knowledge"]["nodes"]
        }
        assert set(page.locator("#records-svg line").evaluate_all("es=>es.map(e=>e.dataset.edge)")) == {
            e["id"] for e in payload["knowledge"]["edges"]
        }
        # All points start inside the drawing, including isolated records.
        assert points.evaluate_all("""ps=>{
            const r=document.getElementById('records-svg').getBoundingClientRect();
            return ps.every(p=>{const b=p.getBoundingClientRect();
                return b.left>=r.left && b.right<=r.right && b.top>=r.top && b.bottom<=r.bottom;});
        }""")
        page.locator("#records-query").fill("Abelian curvature")
        match = page.locator("#records-results button").first
        label = match.inner_text()
        match.focus()
        page.keyboard.press("Enter")
        expect(page.locator("#records-detail h2")).to_have_text(label)
        page.wait_for_function("() => recordFrame === 0")
        assert page.locator("#records-svg line.active").count() > 0
        selection = page.locator(".record-point.selected").get_attribute("data-node")
        assert all(selection in (edge["from"], edge["to"]) for edge in page.locator(
            "#records-svg line.active").evaluate_all("es=>es.map(e=>({from:e.dataset.from,to:e.dataset.to}))"))
        page.locator("#records-fit").click()
        page.wait_for_function("() => recordFrame === 0")
        expect(page.locator("#records-zoom")).to_have_text("100%")
        page.locator("#records-focus").click()
        page.locator("#records-fit").click()
        page.wait_for_function("() => recordFrame === 0")
        expect(page.locator("#records-zoom")).to_have_text("100%")
        page.locator("#records-in").click()
        expect(page.locator("#records-zoom")).to_have_text("135%")
        svg = page.locator("#records-svg")
        svg.scroll_into_view_if_needed()
        svg.focus()
        before = page.evaluate("recordCamera.x")
        page.keyboard.press("ArrowRight")
        assert page.evaluate("recordCamera.x") > before
        box = svg.bounding_box()
        before = page.evaluate("recordCamera.x")
        page.mouse.move(box["x"] + 100, box["y"] + 100)
        page.mouse.down()
        page.mouse.move(box["x"] + 180, box["y"] + 130, steps=8)
        page.mouse.up()
        assert page.evaluate("recordCamera.x") < before
        page.locator("#records-expand").click()
        page.locator("#records-inspect").click()
        expect(page.locator("#records-expand")).to_have_attribute("aria-pressed", "false")
        expect(page.locator("#records-detail h2")).to_be_in_viewport()
        page.locator("#records-detail button").filter(has_text="Evidence").click()
        expect(page.locator("#detail .evidence").first).to_be_visible()
        page.reload()
        page.locator("#back").click()
        expect(page.locator("#records-detail h2")).to_have_text(label)
        page.reload()
        expect(page.locator("#records-detail h2")).to_have_text(label)
        page.locator("#records-filter").select_option("schwartz")
        expected = {n for v in payload["reading_views"] if v["id"] == "schwartz" for c in v["chapters"] for n in c["nodes"]}
        assert set(points.evaluate_all("ps=>ps.map(p=>p.dataset.node)")) == expected
        page.reload()
        expect(points).to_have_count(len(expected))
        page.locator("#records-all").click()
        expect(points).to_have_count(len(payload["knowledge"]["nodes"]))
        # Old list links remain useful and retain their exact record scope.
        pair = ["peskin-schroeder", "schwartz"]
        page.goto(url + "#graph=qft&view=search&books=" + ",".join(pair))
        expect(page.locator("body")).to_have_attribute("data-view", "records")
        expect(points).to_have_count(sum(set(pair) <= set(v) for v in payload["direct_books"].values()))
        page.locator("#chapters-tab").click()
        page.locator(".chapter-link").first.click()
        expect(points).to_have_count(len(payload["reading_views"][0]["chapters"][0]["nodes"]))
        page.reload()
        expect(points).to_have_count(len(payload["reading_views"][0]["chapters"][0]["nodes"]))
        page.emulate_media(reduced_motion="reduce")
        page.locator("#records-query").fill("amplitude")
        page.locator("#records-results button").first.click()
        assert page.evaluate("recordFrame === 0")
        for width in (320, 390, 768, 1100, 1440):
            page.set_viewport_size({"width": width, "height": 720})
            page.locator("#records-fit").click()
            # WebKit can acknowledge the new viewport before its reflow and
            # ResizeObserver camera update. Require the actual layout invariant.
            try:
                page.wait_for_function("() => document.documentElement.scrollWidth <= innerWidth + 1", timeout=5000)
            except Exception:
                screenshots = Path(".syllabusgraph/browser-qa")
                screenshots.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(screenshots / f"records-{engine.name}-{width}.png"), full_page=True)
                print("Record map overflow:", engine.name, width, page.evaluate("""() => ({
                    width: innerWidth, scroll: document.documentElement.scrollWidth,
                    header: [...document.querySelector('.topbar').children].map(e => ({
                        tag:e.tagName,id:e.id,cls:e.className,rect:e.getBoundingClientRect().toJSON(),
                        display:getComputedStyle(e).display,margin:getComputedStyle(e).margin
                    })),
                    text: [...document.querySelectorAll('body *')].filter(e =>
                        !e.closest('svg,[hidden]') && e.scrollWidth > e.clientWidth + 1
                    ).slice(0, 20).map(e => ({tag:e.tagName,id:e.id,cls:e.className,client:e.clientWidth,scroll:e.scrollWidth})),
                    elements: [...document.querySelectorAll('body *')].filter(e =>
                        !e.closest('svg,[hidden]') && e.getBoundingClientRect().right > innerWidth + 1
                    ).map(e => ({tag:e.tagName,id:e.id,cls:e.className,right:e.getBoundingClientRect().right}))
                })"""))
                print("Header isolation:", page.evaluate("""() => [...document.querySelector('.topbar').children].map(e => {
                    const original=e.getAttribute('style');
                    e.style.setProperty('display','none','important');
                    const width=document.documentElement.scrollWidth;
                    original === null ? e.removeAttribute('style') : e.setAttribute('style',original);
                    return {id:e.id,cls:e.className,width};
                })"""))
                raise
            assert svg.bounding_box()["height"] >= 480
            expect(page.locator("#core-tab")).to_be_visible()
            expect(page.locator("#overlap-tab")).to_be_visible()
        assert not errors, errors
        print(f"{engine.name}: full record graph, exact scopes, search, evidence, saved links, camera, narrow screens and reduced motion passed.")
    finally:
        browser.close()


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
                ("records", "#graph=qft&view=records"),
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
                    for identity in ("board", "core-scroll", "graph-scroll", "concept-map-scroll", "atlas-scroll", "records-svg"):
                        target = page.locator("#" + identity)
                        if target.is_visible():
                            assert target.bounding_box()["height"] >= 120, (scale, view, identity)
                    if view not in ("home", "map"):
                        for identity in ("overview", "atlas", "records", "core", "chapters", "overlap"):
                            expect(page.locator("#" + identity + "-tab")).to_be_visible()
                    if view == "core":
                        expect(page.locator(".core-aside")).to_be_visible()
                        page.locator("#core-expand").click()
                        assert page.locator("#core-scroll").bounding_box()["height"] >= 140
                        page.keyboard.press("Escape")
                        expect(page.locator("#core-expand")).to_have_attribute("aria-pressed", "false")
                    if view == "records":
                        expect(page.locator(".record-point")).to_have_count(2156)
                        page.locator("#records-expand").click()
                        assert page.locator("#records-svg").bounding_box()["height"] >= 140
                        page.keyboard.press("Escape")
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
