/* Compact, opt-in display of an explicitly authored concept layer. */
"use strict";
let conceptMapScale = 1;
let conceptMapSize = { width: 900, height: 520 };
function isConceptMap() {
  return catalog?.graphs.find((g) => g.id === data?.id)?.kind === "concept-map";
}
function mapSVG(tag, attrs = {}) {
  const element = svgEl(tag);
  for (const [key, value] of Object.entries(attrs))
    element.setAttribute(key, value);
  return element;
}
function renderConceptMap() {
  if (!isConceptMap()) return;
  show("map");
  $("concept-map-title").textContent = data.title;
  $("concept-map-count").textContent =
    `${nodes.length} concepts · ${edges.length} relationships`;
  const scene = $("concept-map-svg");
  scene.replaceChildren();
  const defs = mapSVG("defs"),
    marker = mapSVG("marker", {
      id: "concept-arrow",
      viewBox: "0 0 10 10",
      refX: 8,
      refY: 5,
      markerWidth: 6,
      markerHeight: 6,
      orient: "auto-start-reverse",
    });
  marker.append(
    mapSVG("path", { d: "M 0 1 L 9 5 L 0 9", fill: "none", stroke: "#718d9b" }),
  );
  defs.append(marker);
  scene.append(defs);
  // Components use all recorded relations; layout never adds scientific edges.
  const adjacent = new Map(nodes.map((n) => [n.id, new Set()]));
  for (const e of edges) {
    adjacent.get(e.from).add(e.to);
    adjacent.get(e.to).add(e.from);
  }
  const components = [],
    seen = new Set();
  for (const n of nodes) {
    if (seen.has(n.id)) continue;
    const ids = [n.id];
    seen.add(n.id);
    for (let i = 0; i < ids.length; i++)
      for (const next of adjacent.get(ids[i]))
        if (!seen.has(next)) {
          seen.add(next);
          ids.push(next);
        }
    components.push(ids);
  }
  components.sort((a, b) => b.length - a.length);
  const positions = new Map();
  const width = 980;
  let top = 30;
  for (const [index, ids] of components.entries()) {
    const within = edges.filter(
      (e) => ids.includes(e.from) && ids.includes(e.to),
    );
    const ranks = new Map(ids.map((id) => [id, 0]));
    // Use directed links for arrangement only. Cycles fall back to prerequisite ranks.
    const layoutRanks = (links) => {
      const degree = new Map(ids.map((id) => [id, 0]));
      const outgoing = new Map(ids.map((id) => [id, []]));
      for (const e of links) {
        degree.set(e.to, degree.get(e.to) + 1);
        outgoing.get(e.from).push(e.to);
      }
      const queue = ids.filter((id) => degree.get(id) === 0);
      for (let i = 0; i < queue.length; i++)
        for (const next of outgoing.get(queue[i])) {
          ranks.set(next, Math.max(ranks.get(next), ranks.get(queue[i]) + 1));
          degree.set(next, degree.get(next) - 1);
          if (!degree.get(next)) queue.push(next);
        }
      return queue.length === ids.length;
    };
    if (!layoutRanks(within)) {
      for (const id of ids) ranks.set(id, 0);
      layoutRanks(within.filter((e) => e.relation === "prerequisite"));
    }
    const columns = new Map();
    for (const id of ids) {
      const rank = ranks.get(id);
      if (!columns.has(rank)) columns.set(rank, []);
      columns.get(rank).push(byId.get(id));
    }
    const rows = Math.max(...[...columns.values()].map((c) => c.length));
    const height = ids.length === 1 ? 80 : rows * 125 + 20;
    const heading = mapSVG("text", {
      x: 45,
      y: top,
      class: "concept-component-label",
    });
    heading.textContent =
      ids.length === 1
        ? "NO RECORDED CONNECTION"
        : `CONNECTED SET ${index + 1}`;
    scene.append(heading);
    for (const [rank, column] of columns) {
      column.sort((a, b) => a.label.localeCompare(b.label));
      column.forEach((node, i) =>
        positions.set(node.id, {
          x: 140 + (rank * (width - 280)) / Math.max(1, columns.size - 1),
          y:
            ids.length === 1
              ? top + 30
              : top + 40 + ((i + 0.5) * (height - 40)) / column.length,
        }),
      );
    }
    top += height + 30;
  }
  conceptMapSize = { width, height: top + 35 };
  scene.setAttribute("viewBox", `0 0 ${width} ${conceptMapSize.height}`);
  $("concept-map-count").textContent =
    `${nodes.length} concepts · ${edges.length} relationships · ${components.length} separate pieces`;
  for (const edge of edges) {
    const a = positions.get(edge.from),
      b = positions.get(edge.to);
    const direction = b.x >= a.x ? 1 : -1;
    const bend = Math.max(45, Math.abs(b.x - a.x) * 0.4);
    const line = mapSVG("path", {
      d: `M ${a.x + direction * 17} ${a.y} C ${a.x + direction * bend} ${a.y}, ${b.x - direction * bend} ${b.y}, ${b.x - direction * 20} ${b.y}`,
      class:
        "concept-link" + (edge.relation === "prerequisite" ? "" : " other"),
      "marker-end": "url(#concept-arrow)",
    });
    line.dataset.edge = edge.id;
    line.dataset.from = edge.from;
    line.dataset.to = edge.to;
    const title = mapSVG("title");
    title.textContent = `${human(edge.relation)}: ${edge.rationale}`;
    line.append(title);
    scene.append(line);
  }
  for (const node of nodes) {
    const { x, y } = positions.get(node.id);
    const item = mapSVG("g", {
      class: "concept-point",
      tabindex: 0,
      role: "button",
      "aria-label": node.label,
      transform: `translate(${x},${y})`,
    });
    item.dataset.node = node.id;
    item.append(
      mapSVG("circle", { r: 23, class: "concept-halo" }),
      mapSVG("circle", { r: 10, class: "concept-dot" }),
    );
    const isolated = adjacent.get(node.id).size === 0;
    const labelX = isolated ? 40 : 0;
    const labelY = isolated ? 0 : 38;
    const label = mapSVG("text", {
      "text-anchor": isolated ? "start" : "middle",
      y: labelY,
    });
    const lines = [];
    let line = "";
    for (const word of node.label.split(/\s+/)) {
      if (line && (line + " " + word).length > 22) {
        lines.push(line);
        line = word;
      } else line += (line ? " " : "") + word;
    }
    if (line) lines.push(line);
    for (const [i, words] of lines.entries()) {
      const span = mapSVG("tspan", { x: labelX, dy: i ? 20 : 0 });
      span.textContent = words;
      label.append(span);
    }
    item.append(label);
    const count = mapSVG("text", {
      "text-anchor": isolated ? "start" : "middle",
      x: labelX,
      y: labelY + 22 + (lines.length - 1) * 20,
      class: "concept-treatments",
    });
    const bookCount = new Set((node.origins || []).map((o) => o.project)).size;
    count.textContent = `${bookCount} book ${bookCount === 1 ? "graph" : "graphs"}`;
    item.append(count);
    item.onclick = () => selectConcept(node.id);
    item.onkeydown = (e) => {
      if (["Enter", " "].includes(e.key)) {
        e.preventDefault();
        selectConcept(node.id);
      }
    };
    scene.append(item);
  }
  conceptMapScale = 1;
  resizeConceptMap();
  const detail = $("concept-map-detail");
  detail.replaceChildren();
  detail.append(
    el("span", "CONCEPTS AND TREATMENTS", "eyebrow"),
    el("h2", "An idea, then its treatments."),
    el(
      "p",
      "Select a point to see the concept and the different book treatments supporting it. Open a treatment to inspect its original record and page references.",
    ),
    el(
      "p",
      "Lines show recorded relationships. Separate pieces may reflect the graph’s scope; placement does not prescribe a course sequence.",
    ),
    el("small", $("review-status").textContent),
  );
}
function resizeConceptMap() {
  const viewport = $("concept-map-scroll");
  const fitWidth = Math.min(
    viewport.clientWidth,
    (viewport.clientHeight * conceptMapSize.width) / conceptMapSize.height,
  );
  const width =
    (innerWidth <= 760 ? Math.max(760, fitWidth) : fitWidth) * conceptMapScale;
  $("concept-map-svg").style.width = width + "px";
  $("concept-map-svg").style.height =
    (width * conceptMapSize.height) / conceptMapSize.width + "px";
}
function selectConcept(id) {
  const node = byId.get(id),
    neighbors = new Set([id]);
  for (const line of $("concept-map-svg").querySelectorAll(".concept-link")) {
    const lit = [line.dataset.from, line.dataset.to].includes(id);
    line.classList.toggle("lit", lit);
    line.classList.toggle("dim", !lit);
    if (lit) {
      neighbors.add(line.dataset.from);
      neighbors.add(line.dataset.to);
    }
  }
  for (const point of $("concept-map-svg").querySelectorAll(".concept-point")) {
    point.classList.toggle("selected", point.dataset.node === id);
    point.classList.toggle("dim", !neighbors.has(point.dataset.node));
    point.setAttribute("aria-pressed", String(point.dataset.node === id));
  }
  const detail = $("concept-map-detail");
  detail.replaceChildren();
  detail.append(
    el("span", "CONCEPT", "eyebrow"),
    el("h2", node.label),
    el("p", node.summary),
    el("h3", "Book treatments"),
  );
  for (const origin of node.origins || []) {
    const graph = catalog.graphs.find((g) => g.project_id === origin.project);
    const row = el("div", undefined, "concept-treatment");
    const button = el("button", `${bookTitle(origin.project)} ↗`);
    button.disabled = !graph;
    button.onclick = () =>
      navigateGraph(graph.id, new URLSearchParams({ node: origin.node }));
    row.append(
      button,
      el(
        "p",
        origin.note || "Supporting treatment within this concept's scope.",
      ),
    );
    detail.append(row);
  }
  const inspect = el("button", "Inspect relationships and evidence →");
  inspect.onclick = () => openNode(id);
  detail.append(inspect);
  detail.scrollTop = 0;
}
function bindConceptMapControls() {
  $("map-tab").onclick = () => {
    renderConceptMap();
    saveURL();
  };
  for (const [name, delta] of [
    ["in", 0.2],
    ["out", -0.2],
    ["fit", 0],
  ])
    $("concept-map-" + name).onclick = () => {
      conceptMapScale = delta
        ? Math.max(0.8, Math.min(2, conceptMapScale + delta))
        : 1;
      resizeConceptMap();
      if (!delta) $("concept-map-scroll").scrollTo(0, 0);
    };
  const scroll = $("concept-map-scroll");
  scroll.onkeydown = (e) => {
    if (e.target !== scroll) return;
    const offset = {
      ArrowDown: [0, 60],
      ArrowUp: [0, -60],
      ArrowRight: [60, 0],
      ArrowLeft: [-60, 0],
    }[e.key];
    if (offset) {
      e.preventDefault();
      scroll.scrollBy(...offset);
    }
  };
  let drag = null,
    moved = false;
  scroll.onpointerdown = (e) => {
    moved = false;
    if (e.pointerType === "mouse" && e.button === 0)
      drag = {
        x: e.clientX,
        y: e.clientY,
        left: scroll.scrollLeft,
        top: scroll.scrollTop,
        id: e.pointerId,
      };
  };
  scroll.onpointermove = (e) => {
    if (!drag) return;
    if (Math.abs(e.clientX - drag.x) + Math.abs(e.clientY - drag.y) > 5) {
      moved = true;
      scroll.setPointerCapture(drag.id);
    }
    if (moved) {
      scroll.scrollLeft = drag.left + drag.x - e.clientX;
      scroll.scrollTop = drag.top + drag.y - e.clientY;
    }
  };
  scroll.onpointerup = scroll.onpointercancel = () => {
    drag = null;
  };
  scroll.addEventListener(
    "click",
    (e) => {
      if (moved && e.detail) {
        e.stopPropagation();
        moved = false;
      }
    },
    true,
  );
  new ResizeObserver(() => {
    if (mode === "map") resizeConceptMap();
  }).observe(scroll);
}
