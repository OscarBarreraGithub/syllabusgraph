"""Measure full-record graph interactions on a served site; no model calls.

Run after `syllabusgraph site serve`. Output belongs in ignored local storage.
The report is a comparison aid, not a hardware-independent FPS guarantee.
"""

import argparse
import json
from pathlib import Path
import time

from playwright.sync_api import sync_playwright


def stats(values):
    ordered = sorted(values)
    if not ordered:
        return {"count": 0, "median_ms": 0, "p95_ms": 0, "max_ms": 0}
    return {
        "count": len(ordered),
        "median_ms": round(ordered[len(ordered) // 2], 2),
        "p95_ms": round(ordered[min(len(ordered) - 1, int(len(ordered) * .95))], 2),
        "max_ms": round(ordered[-1], 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:8767/#graph=qft&view=records")
    parser.add_argument("--cpu", type=float, default=4)
    parser.add_argument("--output", type=Path, default=Path(".syllabusgraph/performance/records.json"))
    args = parser.parse_args()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=2)
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        session = page.context.new_cdp_session(page)
        session.send("Emulation.setCPUThrottlingRate", {"rate": args.cpu})
        session.send("Performance.enable")
        page.goto(args.url)
        page.wait_for_function("() => typeof recordPoints !== 'undefined' && recordPoints.size > 0 && recordFrame === 0")
        page.evaluate("""() => {
          window.samples = {paint:[], highlight:[], frames:[], longTasks:[]};
          for (const [key, name] of [['paint','paintRecordCamera'],['highlight','highlightRecord']]) {
            const old = window[name]; window[name] = function(...args) {
              const t=performance.now(), result=old(...args);
              samples[key].push(performance.now()-t); return result;
            };
          }
          new PerformanceObserver(list=>samples.longTasks.push(...list.getEntries().map(e=>e.duration)))
            .observe({type:'longtask'});
          window.tracking=true; let last=performance.now();
          function frame(now){samples.frames.push(now-last);last=now;if(tracking)requestAnimationFrame(frame)}
          requestAnimationFrame(frame);
        }""")
        before = {m["name"]: m["value"] for m in session.send("Performance.getMetrics")["metrics"]}
        started = time.monotonic()
        positions = page.evaluate("""() => {
          const r=document.getElementById('records-canvas').getBoundingClientRect();
          const stride=Math.max(1,Math.ceil(recordPoints.size/31));
          return [...recordPoints.values()].filter((p,i)=>i%stride===0).map(p=>({
            x:r.x+r.width/2+(p.x-recordCamera.x)*recordCamera.k,
            y:r.y+r.height/2+(p.y-recordCamera.y)*recordCamera.k
          }));
        }""")
        for pos in positions:
            page.mouse.move(pos["x"], pos["y"])
        page.mouse.click(positions[0]["x"], positions[0]["y"])
        page.wait_for_timeout(700)
        page.locator("#records-fit").click()
        page.wait_for_timeout(700)
        box = page.locator("#records-canvas").bounding_box()
        x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
        page.mouse.move(x, y)
        page.mouse.down()
        page.mouse.move(x + 180, y + 90, steps=30)
        page.mouse.up()
        for _ in range(3):
            page.locator("#records-in").click()
        page.wait_for_timeout(150)
        page.evaluate("tracking=false")
        after = {m["name"]: m["value"] for m in session.send("Performance.getMetrics")["metrics"]}
        report = {
            "url": args.url, "browser": browser.version, "cpu_slowdown": args.cpu,
            "viewport": {"width": 1440, "height": 1000, "pixel_ratio": 2},
            "scenario": "Hover up to 31 points, select/focus, overview, pan 30 steps, zoom 3 steps",
            "records": page.evaluate("recordPoints.size"), "edges": page.evaluate("recordEdges.length"),
            "wall_seconds": round(time.monotonic() - started, 2),
            "samples": {k: stats(v) for k, v in page.evaluate("samples").items()},
            "metrics_seconds": {k: round(after[k] - before[k], 3) for k in [
                "TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration",
            ]},
            "map_dom_elements": page.locator(".records-viewport *").count(),
            "errors": errors,
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps(report, indent=2))
        browser.close()
        assert not errors, errors


if __name__ == "__main__":
    main()
