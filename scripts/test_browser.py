"""Real-browser checks on disposable projects. Optional: install the browser extra."""

from contextlib import contextmanager
from pathlib import Path
import tempfile
import threading

from playwright.sync_api import expect, sync_playwright

from syllabusgraph.cli import initialize
from syllabusgraph.server import CourseServer


@contextmanager
def server_for(path):
    server = CourseServer(path, 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def main():
    screenshots = Path(".syllabusgraph/browser-check")
    screenshots.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary, sync_playwright() as playwright:
        root = Path(temporary)
        initialize(root / "sample", "sampling")
        initialize(root / "qft", "qft")
        browser = playwright.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1440, "height": 1000}, reduced_motion="reduce"
        )
        page = context.new_page()
        errors, external = [], []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on(
            "request",
            lambda req: (
                external.append(req.url) if not req.url.startswith("http://127.0.0.1:") else None
            ),
        )
        with server_for(root / "sample") as base:
            page.goto(base)
            expect(page.locator(".session-card")).to_have_count(4)
            expect(page.locator("#global-error")).to_be_hidden()
            page.screenshot(path=str(screenshots / "desktop.png"), full_page=True)
            page.get_by_role(
                "button", name="Add Simulation checks to learning goals", exact=True
            ).click()
            expect(page.locator(".stat").nth(0).locator("strong")).to_have_text("3")
            page.get_by_label("Treatment depth", exact=True).select_option("derive")
            page.get_by_label("Assessment for this learning outcome").fill(
                "Implement and explain a coverage experiment."
            )
            page.get_by_label("Assessment for this learning outcome").press("Tab")
            page.get_by_role("button", name="Save course", exact=True).click()
            expect(page.locator("#save-state")).to_have_text("All changes saved")
            page.reload()
            expect(page.locator(".stat").nth(0).locator("strong")).to_have_text("3")
            with page.expect_download() as download:
                page.get_by_role("button", name="Export ↗", exact=True).click()
            text = Path(download.value.path()).read_text()
            assert "Implement and explain a coverage experiment." in text
            assert "Simulation checks** (derive)" in text
            page.get_by_label("Course plan", exact=True).select_option("simulation-lab")
            page.get_by_role("button", name="Set student background", exact=True).click()
            page.get_by_label(
                "Background level for Confidence intervals", exact=True
            ).select_option("")
            page.get_by_role("button", name="Apply background", exact=True).click()
            expect(
                page.locator('.topic-pill[data-detail="sampling.confidence_interval"]')
            ).to_be_visible()
            page.get_by_role("button", name="Save course", exact=True).click()
            expect(page.locator("#save-state")).to_have_text("All changes saved")
            page.get_by_role("button", name="Set student background", exact=True).click()
            expect(
                page.get_by_label("Background level for Confidence intervals", exact=True)
            ).to_have_value("")
            page.get_by_role("button", name="Close background settings", exact=True).click()
            page.get_by_label("Course plan", exact=True).select_option("foundations")
            page.get_by_role("tab", name="Concept map", exact=True).click()
            expect(page.locator(".graph-node").first).to_be_visible()
            page.screenshot(path=str(screenshots / "graph.png"), full_page=True)
            page.get_by_role("tab", name="References", exact=False).click()
            page.get_by_role("button", name="Add reference", exact=True).click()
            page.get_by_label("Short identifier").fill("local-note")
            page.get_by_label("Title", exact=True).fill("Local teaching note")
            page.get_by_role("dialog").get_by_role(
                "button", name="Add reference", exact=True
            ).click()
            expect(page.locator(".source-card")).to_have_count(2)
            page.get_by_role("button", name="Attach file", exact=True).click()
            text_file = root / "note.txt"
            text_file.write_text("An original note supports this local source import exercise.")
            page.get_by_label("Local file").set_input_files(text_file)
            page.get_by_role("button", name="Attach locally", exact=True).click()
            expect(page.get_by_text("1 pages attached", exact=True)).to_be_visible()
            page.get_by_role("tab", name="Source workflow", exact=True).click()
            page.get_by_role("button", name="Prepare a page range", exact=True).click()
            page.locator("#prepare-source").select_option("local-note")
            page.get_by_label("Unit identifier").fill("local-unit")
            page.get_by_label("Last printed page").fill("1")
            page.get_by_label("What should this unit cover?").fill(
                "Read and review the original local note."
            )
            page.get_by_role("button", name="Prepare packet", exact=True).click()
            expect(page.locator(".unit")).to_contain_text("local-unit")
            expect(page.locator(".unit")).to_contain_text("prepared")
            page.get_by_role("tab", name="Course design", exact=True).click()
            page.set_viewport_size({"width": 390, "height": 844})
            expect(page.locator(".session-card").first).to_be_visible()
            assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1")
            page.screenshot(path=str(screenshots / "mobile.png"), full_page=True)
            assert not errors, errors
            assert not external, external
        with server_for(root / "qft") as base:
            page.set_viewport_size({"width": 1440, "height": 1000})
            page.goto(base)
            expect(
                page.get_by_role("heading", name="Quantum field theory", exact=True)
            ).to_be_visible()
            expect(
                page.get_by_role("button", name="Attach your references", exact=True)
            ).to_be_visible()
            page.get_by_label("Course plan", exact=True).select_option("qft-ii")
            expect(page.locator(".issue.error")).to_contain_text("Prior course")
            page.get_by_role("tab", name="References", exact=False).click()
            expect(page.locator(".source-card")).to_have_count(4)
            expect(page.get_by_role("button", name="Attach file", exact=True)).to_have_count(4)
            page.screenshot(path=str(screenshots / "qft.png"), full_page=True)
            assert not errors, errors
        browser.close()
    print(
        "Browser checks passed: editing, persistence, draft export, graph, uploads, preparation, mobile, and QFT scaffold."
    )
    print(f"Screenshots: {screenshots}")


if __name__ == "__main__":
    main()
