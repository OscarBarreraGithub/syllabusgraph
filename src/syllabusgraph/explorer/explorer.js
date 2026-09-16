"use strict";
const $ = (id) => document.getElementById(id);
const colors = {
  selected: "#285747",
  before: "#b87842",
  after: "#627f98",
  other: "#929b8c",
};
let catalog,
  graph,
  nodes,
  edges,
  byId,
  neighbors,
  selected = null,
  pair = null,
  visible = [],
  limit = 60;
let points = [],
  lines = [],
  zoom = 1,
  offset = { x: 0, y: 0 },
  drag = null,
  moved = false,
  version = 0;
const cache = new Map();
const canvas = $("map"),
  ctx = canvas.getContext("2d");
const fmt = (n) => n.toLocaleString();
function el(tag, text, cls) {
  const e = document.createElement(tag);
  if (text !== undefined) e.textContent = text;
  if (cls) e.className = cls;
  return e;
}
function say(text) {
  $("notice").textContent = text;
  $("notice").style.display = "block";
  setTimeout(() => ($("notice").style.display = "none"), 3500);
}
function books(n) {
  return graph.direct_books?.[n.id] || [];
}
function originBooks(n) {
  return [...new Set((n.origins || []).map((o) => o.project))];
}
function bookTitle(id) {
  return (
    catalog.graphs.find((g) => g.project_id === id)?.title ||
    graph.sources.find((s) => s.id === id)?.title ||
    id
  );
}
function showEvidence(parent, evidence) {
  for (const e of evidence || []) {
    const box = el("div", undefined, "evidence");
    box.append(
      el("strong", bookTitle(e.source)),
      el(
        "span",
        `${e.section || "Source"} · pp. ${(e.pages || []).join(", ")}`,
      ),
    );
    parent.append(box);
  }
}
function hash(s) {
  let h = 2166136261;
  for (const c of s) h = Math.imul(h ^ c.charCodeAt(0), 16777619);
  return (h >>> 0) / 4294967296;
}
function setURL() {
  const p = new URLSearchParams({ graph: graph.id });
  if (selected) p.set("node", selected);
  history.replaceState(null, "", "#" + p);
}
async function loadGraph(id, node = null) {
  const v = ++version;
  const entry = catalog.graphs.find((g) => g.id === id) || catalog.graphs[0];
  try {
    if (!cache.has(entry.id)) {
      const r = await fetch(entry.file);
      if (!r.ok) throw Error("Graph download failed");
      cache.set(entry.id, await r.json());
    }
    if (v !== version) return;
    graph = cache.get(entry.id);
    nodes = graph.knowledge.nodes;
    edges = graph.knowledge.edges;
    byId = new Map(nodes.map((n) => [n.id, n]));
    neighbors = new Map(nodes.map((n) => [n.id, []]));
    for (const e of edges) {
      neighbors.get(e.from)?.push(e);
      neighbors.get(e.to)?.push(e);
    }
    selected = null;
    pair = null;
    limit = 60;
    $("search").value = "";
    $("graph-select").value = entry.id;
    $("collection-title").textContent = entry.title;
    $("stats").replaceChildren(
      ...[
        [nodes.length, "concepts"],
        [edges.length, "relationships"],
        [
          new Set(
            graph.sources
              .filter((s) => !s.id.endsWith("-notation"))
              .map((s) => s.id),
          ).size,
          "sources",
        ],
      ].map(([n, label]) => {
        const d = el("div", undefined, "stat");
        d.append(el("strong", fmt(n)), el("span", label));
        return d;
      }),
    );
    $("review-status").textContent =
      graph.review.status === "model-reviewed"
        ? `Model-reviewed · Human audit ${graph.review.human_audit || "not recorded"}`
        : "Review status is recorded with the source project.";
    $("download").href = entry.file;
    $("download").setAttribute("download", `${entry.id}-graph.json`);
    const b = [...new Set(nodes.flatMap(originBooks))];
    $("source-select").replaceChildren(
      new Option(b.length ? "All books" : "All sources", ""),
      ...b.map((id) => new Option(bookTitle(id), id)),
    );
    $("source-select").disabled = !b.length;
    $("kind-select").replaceChildren(
      new Option("All types", ""),
      ...[...new Set(nodes.map((n) => n.kind))]
        .sort()
        .map((k) => new Option(k.replaceAll("_", " "), k)),
    );
    $("overlap-tab").disabled = entry.kind !== "shared" || b.length < 2;
    switchView(false);
    filter();
    if (node && byId.has(node)) selectNode(node);
    else {
      emptyDetail();
      setURL();
    }
  } catch (err) {
    say(err.message);
    $("review-status").textContent =
      "Could not load this graph. Refresh to try again.";
  }
}
function emptyDetail() {
  const d = $("detail");
  d.replaceChildren(
    el("div", "A PLACE TO BEGIN", "tiny"),
    el("h2", "Pick an idea. See what it rests on."),
    el("p", "Each point is a concept. Each line is a recorded relationship."),
    el("div", undefined, "detail-rule"),
    el(
      "p",
      "Search on the left or select a point on the map. You’ll find the explanation, connected ideas, and section and page references here.",
    ),
    el(
      "div",
      "The layout is a browsing aid, not a proposed teaching order.",
      "detail-note",
    ),
  );
}
function filter() {
  const q = $("search").value.toLowerCase().trim(),
    b = $("source-select").value,
    k = $("kind-select").value;
  visible = nodes.filter(
    (n) =>
      (!q || `${n.label} ${n.summary} ${n.id}`.toLowerCase().includes(q)) &&
      (!b || originBooks(n).includes(b)) &&
      (!k || n.kind === k) &&
      (!pair || pair.every((id) => books(n).includes(id))),
  );
  if (q)
    visible.sort(
      (a, b) =>
        Number(b.label.toLowerCase().includes(q)) -
        Number(a.label.toLowerCase().includes(q)),
    );
  renderList();
  if (!selected) layout();
}
function renderList() {
  $("result-count").textContent =
    `${fmt(visible.length)} concepts${pair ? " · overlap" : ""}`;
  $("results").replaceChildren();
  for (const n of visible.slice(0, limit)) {
    const b = el(
      "button",
      undefined,
      "result" + (selected === n.id ? " active" : ""),
    );
    b.append(
      el("span", n.label),
      el("small", `${n.kind} · ${neighbors.get(n.id).length} connections`),
    );
    b.onclick = () => selectNode(n.id);
    b.setAttribute("aria-pressed", selected === n.id ? "true" : "false");
    $("results").append(b);
  }
  if (!visible.length)
    $("results").append(
      el("p", "No matches. Try another term or reset the filters.", "empty"),
    );
  $("more").hidden = visible.length <= limit;
}
function selectNode(id) {
  if (!byId.has(id)) return;
  selected = id;
  switchView(false);
  renderList();
  layout();
  setURL();
  const n = byId.get(id),
    d = $("detail");
  d.replaceChildren(
    el("span", n.kind, "badge"),
    el("h2", n.label),
    el("p", n.summary),
  );
  const share = el("button", "Copy link", "text-button");
  share.onclick = () => copy(location.href);
  d.append(share);
  const origins = n.origins || [];
  if (origins.length) {
    d.append(el("h4", "BOOK TREATMENTS"));
    for (const o of origins) {
      const block = el("div", undefined, "origin");
      const target = catalog.graphs.find((g) => g.project_id === o.project);
      if (target) {
        const b = el("button", `${bookTitle(o.project)} ↗`);
        b.onclick = () => loadGraph(target.id, o.node);
        block.append(b);
      } else block.append(el("strong", bookTitle(o.project)));
      if (o.note) block.append(el("p", o.note));
      d.append(block);
    }
  }
  d.append(el("h4", "SOURCE EVIDENCE"));
  showEvidence(d, n.evidence);
  if (!n.evidence?.length)
    d.append(el("p", "No page evidence recorded on this concept."));
  if (n.notation?.length) {
    d.append(el("h4", "NOTATION & QUALIFICATIONS"));
    for (const item of n.notation)
      d.append(el("p", `${bookTitle(item.source)}: ${item.note}`));
  }
  const adjacent = neighbors.get(id);
  d.append(el("h4", `CONNECTED IDEAS · ${adjacent.length}`));
  for (const e of adjacent) {
    const other = byId.get(e.from === id ? e.to : e.from);
    if (!other) continue;
    const row = el("div", undefined, "connection");
    const b = el("button", other.label);
    b.onclick = () => selectNode(other.id);
    const direction = e.to === id ? "Into this concept" : "From this concept";
    row.append(
      b,
      el(
        "small",
        `${direction} · ${e.relation}${e.necessity ? " · " + e.necessity : ""}`,
      ),
    );
    const details = el("details");
    details.append(el("summary", "Relationship evidence"));
    if (e.rationale) details.append(el("p", e.rationale));
    if (e.failure_mode)
      details.append(el("p", `Without it: ${e.failure_mode}`));
    if (e.source_level || e.target_level)
      details.append(
        el("p", `Mastery: ${e.source_level || "—"} → ${e.target_level || "—"}`),
      );
    showEvidence(details, e.evidence);
    row.append(details);
    d.append(row);
  }
  d.append(el("div", n.id, "detail-note"));
  d.scrollTop = 0;
}
function layout() {
  if (!graph) return;
  zoom = 1;
  offset = { x: 0, y: 0 };
  points = [];
  lines = [];
  if (selected) {
    const incident = neighbors.get(selected);
    const ids = [
      ...new Set(incident.map((e) => (e.from === selected ? e.to : e.from))),
    ];
    const before = new Set(
        incident
          .filter((e) => e.to === selected && e.relation === "prerequisite")
          .map((e) => e.from),
      ),
      after = new Set(
        incident
          .filter((e) => e.from === selected && e.relation === "prerequisite")
          .map((e) => e.to),
      );
    const groups = [
      ids.filter((id) => before.has(id)),
      ids.filter((id) => !before.has(id) && after.has(id)),
      ids.filter((id) => !before.has(id) && !after.has(id)),
    ];
    points.push({ id: selected, x: 0, y: 0, r: 8, color: colors.selected });
    groups.forEach((list, g) =>
      list.slice(0, 60).forEach((id, i) => {
        const angle =
          (g === 0 ? Math.PI : g === 1 ? 0 : Math.PI / 2) +
          (i - (Math.min(list.length, 60) - 1) / 2) *
            Math.min(0.22, 2.0 / Math.max(1, list.length));
        const radius = 165 + Math.floor(i / 12) * 38;
        points.push({
          id,
          x: Math.cos(angle) * radius,
          y: Math.sin(angle) * radius,
          r: 5,
          color: [colors.before, colors.after, colors.other][g],
        });
      }),
    );
    const present = new Set(points.map((p) => p.id));
    lines = incident.filter((e) => present.has(e.from) && present.has(e.to));
    $("map-mode").textContent = "ONE CONCEPT, ITS CONNECTIONS";
    $("map-heading").textContent = byId.get(selected).label;
    $("map-count").textContent =
      `${points.length - 1} of ${ids.length} neighbors shown`;
  } else {
    const buckets = new Map();
    for (const n of visible) {
      const key = n.group || `other-${books(n)[0] || "concepts"}-${n.kind}`;
      if (!buckets.has(key)) buckets.set(key, []);
      buckets.get(key).push(n);
    }
    const sets = [...buckets.values()].sort((a, b) => b.length - a.length);
    sets.forEach((list, g) => {
      const angle = g * 2.399963,
        rad = 48 * Math.sqrt(g),
        cx = Math.cos(angle) * rad,
        cy = Math.sin(angle) * rad;
      list.forEach((n, i) => {
        const a = i * 2.399963 + hash(n.id) * 0.3,
          r = 5.2 * Math.sqrt(i);
        points.push({
          id: n.id,
          x: cx + Math.cos(a) * r,
          y: cy + Math.sin(a) * r,
          r: 2.3,
          color: ["#527768", "#8b9980", "#a89473", "#6e8790"][g % 4],
        });
      });
    });
    const present = new Set(points.map((p) => p.id));
    lines = edges.filter((e) => present.has(e.from) && present.has(e.to));
    $("map-mode").textContent = "THE WHOLE PICTURE";
    $("map-heading").textContent = pair
      ? "Concepts with origins in both selected books."
      : "Choose a concept to explore its neighborhood.";
    $("map-count").textContent =
      `${fmt(points.length)} concepts · ${fmt(lines.length)} links`;
  }
  const legend = document.querySelector(".legend");
  legend.replaceChildren();
  if (selected) {
    for (const [key, label] of [
      ["selected", "Selected"],
      ["before", "Prerequisite"],
      ["after", "Depends on this"],
      ["other", "Other relation"],
    ]) {
      const span = el("span");
      const dot = el("i", undefined, "dot");
      dot.style.background = colors[key];
      span.append(dot, document.createTextNode(label));
      legend.append(span);
    }
  } else
    legend.append(
      el(
        "span",
        "Colors separate visual groups · Drag to pan · Select a point to explore",
      ),
    );
  draw();
}
function geometry() {
  const box = canvas.getBoundingClientRect();
  const xs = points.map((p) => Math.abs(p.x)),
    ys = points.map((p) => Math.abs(p.y));
  const scale =
    Math.min(
      (box.width - 80) / (2 * Math.max(120, ...xs)),
      (box.height - 165) / (2 * Math.max(110, ...ys)),
    ) * zoom;
  return {
    w: box.width,
    h: box.height,
    scale,
    cx: box.width / 2 + offset.x,
    cy: box.height / 2 + 35 + offset.y,
  };
}
function draw() {
  if (!ctx || canvas.getBoundingClientRect().width === 0) return;
  const geo = geometry(),
    dpr = Math.min(devicePixelRatio || 1, 2);
  canvas.width = geo.w * dpr;
  canvas.height = geo.h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, geo.w, geo.h);
  const at = new Map();
  for (const p of points) {
    p.sx = geo.cx + p.x * geo.scale;
    p.sy = geo.cy + p.y * geo.scale;
    at.set(p.id, p);
  }
  ctx.lineWidth = selected ? 1 : 0.6;
  for (const e of lines) {
    const a = at.get(e.from),
      b = at.get(e.to);
    if (!a || !b) continue;
    ctx.strokeStyle = selected
      ? e.relation === "prerequisite"
        ? "#9cab98aa"
        : "#a9b1a777"
      : "#85978026";
    ctx.setLineDash(selected && e.relation !== "prerequisite" ? [3, 4] : []);
    ctx.beginPath();
    ctx.moveTo(a.sx, a.sy);
    ctx.lineTo(b.sx, b.sy);
    ctx.stroke();
    if (selected) {
      const angle = Math.atan2(b.sy - a.sy, b.sx - a.sx),
        x = b.sx - Math.cos(angle) * 9,
        y = b.sy - Math.sin(angle) * 9;
      ctx.setLineDash([]);
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x - Math.cos(angle - 0.5) * 5, y - Math.sin(angle - 0.5) * 5);
      ctx.moveTo(x, y);
      ctx.lineTo(x - Math.cos(angle + 0.5) * 5, y - Math.sin(angle + 0.5) * 5);
      ctx.stroke();
    }
  }
  ctx.setLineDash([]);
  for (const p of points) {
    ctx.fillStyle = p.color;
    ctx.beginPath();
    ctx.arc(
      p.sx,
      p.sy,
      p.r * (selected ? 1 : Math.min(1.8, zoom)),
      0,
      Math.PI * 2,
    );
    ctx.fill();
    if (p.id === selected) {
      ctx.strokeStyle = "#28574730";
      ctx.lineWidth = 7;
      ctx.stroke();
    }
  }
  if (selected) {
    ctx.font = "11px system-ui";
    for (const p of points) {
      if ((points.length > 20 || geo.w < 440) && p.id !== selected) continue;
      const label = byId.get(p.id).label;
      const maxWidth = Math.min(180, (geo.w - 48) / (geo.w < 440 ? 1.5 : 3));
      let text = label;
      while (ctx.measureText(text).width > maxWidth && text.length > 4) text = text.slice(0, -1);
      if (text !== label) text = text.slice(0, -1) + "…";
      const width = ctx.measureText(text).width;
      const x = Math.max(width / 2 + 12, Math.min(geo.w - width / 2 - 12, p.sx));
      ctx.textAlign = "center";
      ctx.fillStyle = "#f5f7f1ee";
      ctx.fillRect(x - width / 2 - 3, p.sy + p.r + 6, width + 6, 16);
      ctx.fillStyle = "#37493e";
      ctx.fillText(text, x, p.sy + p.r + 18);
    }
  }
}
function hit(event) {
  const r = canvas.getBoundingClientRect(),
    x = event.clientX - r.left,
    y = event.clientY - r.top;
  let nearest = null,
    dist = 144;
  for (const p of points) {
    const d = (p.sx - x) ** 2 + (p.sy - y) ** 2;
    if (d < dist) {
      dist = d;
      nearest = p;
    }
  }
  return nearest;
}
canvas.addEventListener("pointerdown", (e) => {
  drag = { x: e.clientX, y: e.clientY, ox: offset.x, oy: offset.y };
  moved = false;
  canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener("pointermove", (e) => {
  if (drag) {
    const dx = e.clientX - drag.x,
      dy = e.clientY - drag.y;
    if (Math.abs(dx) + Math.abs(dy) > 4) moved = true;
    offset = { x: drag.ox + dx, y: drag.oy + dy };
    draw();
    return;
  }
  const p = hit(e),
    tip = $("tooltip");
  tip.hidden = !p;
  if (p) {
    tip.textContent = byId.get(p.id).label;
    const r = canvas.getBoundingClientRect();
    tip.style.left = Math.min(e.clientX - r.left + 12, r.width - 240) + "px";
    tip.style.top = Math.max(80, e.clientY - r.top - 40) + "px";
  }
});
canvas.addEventListener("pointerup", (e) => {
  if (!moved) {
    const p = hit(e);
    if (p) selectNode(p.id);
  }
  drag = null;
  $("tooltip").hidden = true;
});
canvas.addEventListener("pointercancel", () => {
  drag = null;
});
canvas.addEventListener("pointerleave", () => {
  $("tooltip").hidden = true;
});
canvas.addEventListener(
  "wheel",
  (e) => {
    if (e.ctrlKey || e.metaKey) {
      e.preventDefault();
      zoom = Math.max(0.35, Math.min(8, zoom * (e.deltaY < 0 ? 1.12 : 0.89)));
      draw();
    }
  },
  { passive: false },
);
new ResizeObserver(() => draw()).observe(canvas);
function switchView(overlap) {
  $("map-view").hidden = overlap;
  $("overlap-view").hidden = !overlap;
  $("map-tab").classList.toggle("active", !overlap);
  $("overlap-tab").classList.toggle("active", overlap);
  $("map-tab").setAttribute("aria-pressed", String(!overlap));
  $("overlap-tab").setAttribute("aria-pressed", String(overlap));
  if (overlap) renderOverlap();
  else requestAnimationFrame(draw);
}
function renderOverlap() {
  const ids = [...new Set(nodes.flatMap(books))].sort();
  const grid = $("overlap-grid");
  grid.replaceChildren();
  for (let i = 0; i < ids.length; i++)
    for (let j = i + 1; j < ids.length; j++) {
      const count = nodes.filter(
        (n) => books(n).includes(ids[i]) && books(n).includes(ids[j]),
      ).length;
      const b = el("button", undefined, "pair");
      b.append(
        el("strong", fmt(count)),
        el("span", `${bookTitle(ids[i])} × ${bookTitle(ids[j])}`),
      );
      b.onclick = () => {
        pair = [ids[i], ids[j]];
        selected = null;
        $("search").value = "";
        $("source-select").value = "";
        $("kind-select").value = "";
        limit = 60;
        switchView(false);
        filter();
        emptyDetail();
        setURL();
      };
      grid.append(b);
    }
  if (ids.length < 2)
    grid.append(
      el(
        "p",
        "Book comparison becomes available in a shared graph with recorded origins.",
      ),
    );
}
async function copy(value) {
  try {
    await navigator.clipboard.writeText(value);
    say("Copied.");
  } catch {
    say("Select and copy the prompt below. Clipboard access is unavailable.");
  }
}
$("graph-select").onchange = (e) => loadGraph(e.target.value);
$("search").oninput = () => {
  limit = 60;
  selected = null;
  filter();
  emptyDetail();
  setURL();
};
$("source-select").onchange = $("kind-select").onchange = () => {
  selected = null;
  limit = 60;
  filter();
  emptyDetail();
  setURL();
};
$("clear").onclick = () => {
  pair = null;
  selected = null;
  $("search").value = "";
  $("source-select").value = "";
  $("kind-select").value = "";
  limit = 60;
  filter();
  emptyDetail();
  setURL();
};
$("more").onclick = () => {
  limit += 60;
  renderList();
};
$("map-tab").onclick = () => switchView(false);
$("overlap-tab").onclick = () => switchView(true);
$("overview").onclick = () => {
  selected = null;
  layout();
  renderList();
  emptyDetail();
  setURL();
};
$("zoom-in").onclick = () => {
  zoom = Math.min(8, zoom * 1.3);
  draw();
};
$("zoom-out").onclick = () => {
  zoom = Math.max(0.35, zoom / 1.3);
  draw();
};
$("fit").onclick = () => {
  zoom = 1;
  offset = { x: 0, y: 0 };
  draw();
};
$("copy-prompt").onclick = () => copy($("setup-prompt").textContent);
(async () => {
  try {
    const r = await fetch("catalog.json");
    if (!r.ok) throw Error("Catalog unavailable");
    catalog = await r.json();
    $("graph-select").replaceChildren(
      ...catalog.graphs.map(
        (g) =>
          new Option(
            `${g.title}${g.kind === "shared" ? " · shared" : ""}`,
            g.id,
          ),
      ),
    );
    const p = new URLSearchParams(location.hash.slice(1));
    await loadGraph(p.get("graph"), p.get("node"));
  } catch (e) {
    $("collection-title").textContent = "The atlas could not be loaded.";
    $("review-status").textContent =
      "Serve the built website over localhost; opening the HTML file directly is not supported.";
    say(e.message);
  }
})();

window.addEventListener("hashchange", () => {
  const p = new URLSearchParams(location.hash.slice(1));
  if (catalog && p.get("graph")) loadGraph(p.get("graph"), p.get("node"));
});
