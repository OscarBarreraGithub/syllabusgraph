/* A finite, deterministic display of existing records. No inferred graph edges. */
"use strict";
let recordPoints = new Map(), recordGroups = [], recordVisible = [], recordEdges = [];
let recordSelection = null, recordFilter = "", recordScope = null, recordHover = null;
let recordCamera = { x: 0, y: 0, k: 1 }, recordFrame = 0, recordFitted = true;
let recordLayers, recordExtent, recordLayoutKey = null, recordLabelPriority = [];
let recordSize = { w: 800, h: 560, ratio: 1 }, recordPaintFrame = 0;
let recordBackgroundKey = null, recordEdgePaths = [], recordEdgeScale = 1;
let recordNear = new Set(), recordActiveEdges = [], recordHighlighted = null;
const recordColors = ["#78d6cb", "#a6b8ff", "#eaba78", "#df99ba", "#8fc9eb", "#b6cf87"];

function stopRecordAnimation() {
  cancelAnimationFrame(recordFrame);
  recordFrame = 0;
  cancelAnimationFrame(recordPaintFrame);
  recordPaintFrame = 0;
}
function prepareRecords(params) {
  stopRecordAnimation();
  recordLayoutKey = null;
  recordSelection = byId.has(params.get("record")) ? params.get("record") : null;
  recordFilter = params.get("source") || "";
  recordScope = params.get("books") ? { pair: params.get("books").split(",") } :
    params.get("chapter") ? { chapter: params.get("chapter") } : null;
  $("records-query").value = params.get("q") || "";
  const sources = data.reading_views.map(v => [v.id, v.title]);
  options($("records-filter"), [["", "All sources"], ...sources]);
  if (!sources.some(([id]) => id === recordFilter)) recordFilter = "";
  $("records-filter").value = recordFilter;
}
function saveRecordsURL(params) {
  if (recordSelection) params.set("record", recordSelection);
  if (recordFilter) params.set("source", recordFilter);
  if (recordScope?.pair) params.set("books", recordScope.pair.join(","));
  if (recordScope?.chapter) params.set("chapter", recordScope.chapter);
  if ($("records-query").value) params.set("q", $("records-query").value);
}
function openRecordGraph(scope = null) {
  recordScope = scope;
  recordFilter = "";
  recordSelection = null;
  $("records-filter").value = "";
  $("records-query").value = "";
  renderRecords();
  saveURL();
}
function recordDimensions() { return recordSize; }
function measureRecords() {
  const canvas = $("records-canvas");
  recordSize = { w: canvas.clientWidth || 800, h: canvas.clientHeight || 560,
    ratio: Math.min(devicePixelRatio || 1, 2) };
}
// Coalesce pointer events into one render per display frame. No idle loop.
function requestRecordPaint() {
  if (recordPaintFrame || recordFrame || mode !== "records") return;
  recordPaintFrame = requestAnimationFrame(() => { recordPaintFrame = 0; paintRecordCamera(); });
}
function recordAt(clientX, clientY) {
  const box = $("records-canvas").getBoundingClientRect(), { x, y, k } = recordCamera;
  const wx = x + (clientX - box.left - recordSize.w / 2) / k;
  const wy = y + (clientY - box.top - recordSize.h / 2) / k;
  let distance = (7 / k) ** 2, nearest = null;
  for (const p of recordPoints.values()) {
    const d = (p.x - wx) ** 2 + (p.y - wy) ** 2;
    if (d <= distance) { distance = d; nearest = p.id; }
  }
  return nearest;
}
function layoutRecords() {
  const source = data.reading_views.find(v => v.id === recordFilter);
  const sourceIds = source ? new Set(source.chapters.flatMap(c => c.nodes)) : null;
  const chapter = reading.chapters.find(c => c.id === recordScope?.chapter);
  const chapterIds = chapter ? new Set(chapter.nodes) : null;
  recordVisible = nodes.filter(n => (!sourceIds || sourceIds.has(n.id)) &&
    (!chapterIds || chapterIds.has(n.id)) &&
    (!recordScope?.pair || recordScope.pair.every(id => directBooks(n).includes(id))));
  const ids = new Set(recordVisible.map(n => n.id));
  recordEdges = edges.filter(e => ids.has(e.from) && ids.has(e.to));
  // Reuse reviewed topic assignments when available. Multiple origins may have
  // different homes; the first sorted home is only a deterministic display choice.
  const homes = new Map(), titles = new Map();
  if (data.atlas) {
    for (const group of data.atlas.groups) titles.set(group.id, group.title);
    for (const concept of [...data.atlas.concepts].sort((a, b) => a.id.localeCompare(b.id)))
      for (const treatment of concept.treatments) {
        const key = treatment.project + ":" + treatment.node;
        if (!homes.has(key)) homes.set(key, concept.group);
      }
  } else {
    for (const c of (source || reading).chapters) {
      titles.set(c.id, c.topics[0] || c.label);
      for (const id of c.nodes) if (!homes.has(id)) homes.set(id, c.id);
    }
  }
  const grouped = new Map();
  for (const n of recordVisible) {
    const group = data.atlas ? (n.origins || []).map(o => homes.get(o.project + ":" + o.node))
      .filter(Boolean).sort()[0] : homes.get(n.id);
    const key = group || "ungrouped";
    if (!grouped.has(key)) grouped.set(key, []);
    grouped.get(key).push(n);
  }
  const entries = [...grouped].sort(([a], [b]) => a.localeCompare(b));
  const columns = Math.max(1, Math.ceil(Math.sqrt(entries.length * 1.65)));
  const maxCount = Math.max(1, ...entries.map(([, list]) => list.length));
  const cell = Math.max(250, Math.sqrt(maxCount) * 37 + 100);
  recordPoints = new Map();
  recordGroups = entries.map(([id, list], i) => {
    const cx = (i % columns) * cell + cell / 2;
    const cy = Math.floor(i / columns) * cell * .82 + cell * .41;
    const color = recordColors[i % recordColors.length];
    list.sort((a, b) => (incident.get(b.id).length - incident.get(a.id).length) || a.id.localeCompare(b.id));
    list.forEach((n, j) => {
      const angle = j * 2.3999632297, radius = 17 * Math.sqrt(j);
      recordPoints.set(n.id, { id: n.id, x: cx + Math.cos(angle) * radius,
        y: cy + Math.sin(angle) * radius * .78, group: id, color });
    });
    return { id, title: titles.get(id) || "Other records",
      short: id === "ungrouped" ? "Other records" : data.atlas ? id.replaceAll("-", " ") : titles.get(id) || "Other records", x: cx,
      y: cy - 17 * Math.sqrt(list.length) * .78 - 35, color, count: list.length };
  });
  recordLabelPriority = [...recordVisible].sort((a, b) => incident.get(b.id).length - incident.get(a.id).length);
  const points = [...recordPoints.values()];
  recordExtent = points.length ? {
    x1: Math.min(...points.map(p => p.x)) - 70,
    y1: Math.min(...recordGroups.map(p => p.y)) - 65,
    x2: Math.max(...points.map(p => p.x)) + 70,
    y2: Math.max(...points.map(p => p.y)) + 70,
  } : { x1: 0, y1: 0, x2: 800, y2: 500 };
  // Separate paths avoid tessellating a large self-crossing polygon.
  recordEdgePaths = recordEdges.map(e => {
    const path = new Path2D(), a = recordPoints.get(e.from), b = recordPoints.get(e.to);
    path.moveTo(a.x, a.y); path.lineTo(b.x, b.y); return path;
  });
  recordBackgroundKey = null;
}
// The complete edge backdrop is static. Move its bitmap with the camera;
// redraw only the selected relationships at full screen resolution.
function rasterRecordEdges() {
  const canvas = $("records-links"), width = recordExtent.x2 - recordExtent.x1;
  const height = recordExtent.y2 - recordExtent.y1;
  recordEdgeScale = Math.min(3072 / Math.max(width, height), 2);
  canvas.width = Math.ceil(width * recordEdgeScale);
  canvas.height = Math.ceil(height * recordEdgeScale);
  canvas.style.width = canvas.width + "px"; canvas.style.height = canvas.height + "px";
  const ctx = canvas.getContext("2d");
  ctx.setTransform(recordEdgeScale, 0, 0, recordEdgeScale, -recordExtent.x1 * recordEdgeScale, -recordExtent.y1 * recordEdgeScale);
  ctx.strokeStyle = "rgba(134,170,167,.1)";
  ctx.lineWidth = .65 / recordTarget(recordExtent).k;
  for (const path of recordEdgePaths) ctx.stroke(path);
}
function renderRecords(reset = true) {
  show("records");
  const key = JSON.stringify([data.id, recordFilter, recordScope, reading.id]);
  const changed = key !== recordLayoutKey;
  if (changed) {
    layoutRecords();
    recordLayoutKey = key;
    reset = true;
  }
  if (!recordPoints.has(recordSelection)) recordSelection = null;
  recordHover = null;
  const chapter = reading.chapters.find(c => c.id === recordScope?.chapter);
  $("records-description").textContent = recordScope?.pair
    ? "Exact matches: " + recordScope.pair.map(bookTitle).join(" × ")
    : chapter ? reading.title + " · " + chapter.label
    : "Explore the original records behind the concepts. Select a point or search for an idea to see its evidence and connections.";
  $("records-count").textContent = `${fmt(recordVisible.length)} ${recordLabel()} · ${fmt(recordEdges.length)} connections`;
  $("records-all").hidden = !recordScope && !recordFilter;
  measureRecords();
  if (changed) rasterRecordEdges();
  recordLayers = { labels: $("records-labels") };
  recordHighlighted = null;
  recordBackgroundKey = null;
  highlightRecord(recordSelection);
  renderRecordDetail();
  searchRecords();
  if (reset) {
    fitRecords(false);
    if (recordSelection) focusRecordConnections(false);
  } else paintRecordCamera();
}
function recordTarget(extent) {
  const { w, h } = recordDimensions();
  const k = Math.min((w - 40) / Math.max(80, extent.x2 - extent.x1),
    (h - 65) / Math.max(80, extent.y2 - extent.y1), 2);
  return { x: (extent.x1 + extent.x2) / 2, y: (extent.y1 + extent.y2) / 2, k: Math.max(.025, k) };
}
function moveRecordCamera(target, animate = true) {
  stopRecordAnimation();
  if (!animate || matchMedia("(prefers-reduced-motion: reduce)").matches) {
    recordCamera = target; paintRecordCamera(); return;
  }
  const start = { ...recordCamera }, began = performance.now();
  function frame(now) {
    const t = Math.min(1, (now - began) / 460), ease = t * t * (3 - 2 * t);
    recordCamera = Object.fromEntries(["x", "y", "k"].map(key => [key, start[key] + (target[key] - start[key]) * ease]));
    paintRecordCamera();
    recordFrame = t < 1 ? requestAnimationFrame(frame) : 0;
  }
  recordFrame = requestAnimationFrame(frame);
}
function fitRecords(animate = true) {
  recordFitted = true;
  moveRecordCamera(recordTarget(recordExtent), animate);
}
function focusRecordConnections(animate = true) {
  if (!recordSelection) return;
  const ids = new Set([recordSelection]);
  for (const e of incident.get(recordSelection)) { ids.add(e.from); ids.add(e.to); }
  const points = [...ids].map(id => recordPoints.get(id)).filter(Boolean);
  const p = recordPoints.get(recordSelection), radius = 160;
  // Keep selected points readable even when an edge spans the entire subject.
  const nearby = points.filter(n => Math.hypot(n.x - p.x, n.y - p.y) < 600);
  const extent = { x1: Math.min(p.x - radius, ...nearby.map(n => n.x - 35)),
    x2: Math.max(p.x + radius, ...nearby.map(n => n.x + 35)),
    y1: Math.min(p.y - radius, ...nearby.map(n => n.y - 35)),
    y2: Math.max(p.y + radius, ...nearby.map(n => n.y + 35)) };
  recordFitted = false;
  moveRecordCamera(recordTarget(extent), animate);
}
function paintRecordCamera() {
  if (!recordLayers || mode !== "records") return;
  const { w, h, ratio } = recordSize, { x, y, k } = recordCamera;
  const canvas = $("records-canvas"), overlay = $("records-overlay"), ctx = overlay.getContext("2d");
  const pw = Math.round(w * ratio), ph = Math.round(h * ratio);
  if (canvas.width !== pw || canvas.height !== ph) {
    canvas.width = overlay.width = pw; canvas.height = overlay.height = ph;
  }
  const key = [x, y, k, w, h, ratio].join(":");
  if (recordBackgroundKey !== key) {
    const bg = canvas.getContext("2d");
    bg.setTransform(1, 0, 0, 1, 0, 0); bg.clearRect(0, 0, pw, ph);
    bg.setTransform(ratio * k, 0, 0, ratio * k, ratio * (w / 2 - x * k), ratio * (h / 2 - y * k));
    // Batch points by color. All records, including isolated ones, are drawn.
    const radius = Math.max(2, Math.min(4, k * 5)) / k;
    bg.globalAlpha = .9;
    for (const color of recordColors) {
      bg.beginPath(); bg.fillStyle = color;
      for (const p of recordPoints.values()) if (p.color === color) {
        bg.moveTo(p.x + radius, p.y); bg.arc(p.x, p.y, radius, 0, Math.PI * 2);
      }
      bg.fill();
    }
    recordBackgroundKey = key;
  }
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, pw, ph);
  const links = $("records-links");
  links.style.transform = `translate(${w / 2 + (recordExtent.x1 - x) * k}px, ${h / 2 + (recordExtent.y1 - y) * k}px) scale(${k / recordEdgeScale})`;
  links.style.opacity = canvas.style.opacity = recordHighlighted ? .17 : 1;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  const screen = p => ({ x: w / 2 + (p.x - x) * k, y: h / 2 + (p.y - y) * k });
  ctx.strokeStyle = "#c8e9e4"; ctx.fillStyle = "#c8e9e4"; ctx.lineWidth = 1.15;
  for (const e of recordActiveEdges) {
    const a = screen(recordPoints.get(e.from)), b = screen(recordPoints.get(e.to));
    ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
    const angle = Math.atan2(b.y - a.y, b.x - a.x), tip = { x: b.x - 7 * Math.cos(angle), y: b.y - 7 * Math.sin(angle) };
    ctx.beginPath(); ctx.moveTo(tip.x, tip.y);
    for (const d of [-.5, .5]) ctx.lineTo(tip.x - 6 * Math.cos(angle + d), tip.y - 6 * Math.sin(angle + d));
    ctx.closePath(); ctx.fill();
  }
  for (const id of new Set([...recordNear, recordSelection].filter(Boolean))) {
    const p = recordPoints.get(id); if (!p) continue;
    const s = screen(p), selected = id === recordSelection;
    ctx.beginPath(); ctx.arc(s.x, s.y, selected ? 6 : Math.max(2, Math.min(4, k * 5)), 0, Math.PI * 2);
    ctx.fillStyle = p.color; ctx.fill();
    if (selected) { ctx.strokeStyle = "#fff"; ctx.lineWidth = 1.5; ctx.stroke(); }
  }
  const percent = Math.round(k / recordTarget(recordExtent).k * 100) + "%";
  if ($("records-zoom").textContent !== percent) $("records-zoom").textContent = percent;
  labelRecords();
}
function labelRecords() {
  if (!recordLayers) return;
  const { w, h } = recordDimensions(), { x, y, k } = recordCamera;
  recordLayers.labels.replaceChildren();
  if (!recordVisible.length) {
    const text = svgEl("text"); text.setAttribute("x", w / 2); text.setAttribute("y", h / 2);
    text.setAttribute("text-anchor", "middle"); text.setAttribute("class", "record-label");
    text.textContent = "No records in this view yet."; recordLayers.labels.append(text); return;
  }
  const occupied = [], focus = recordHover || recordSelection;
  const screen = p => ({ x: w / 2 + (p.x - x) * k, y: h / 2 + (p.y - y) * k });
  const add = (p, text, cls, max = 36) => {
    const s = screen(p), short = text.length > max ? text.slice(0, max - 1) + "…" : text;
    if (s.x < 0 || s.x > w || s.y < 0 || s.y > h) return;
    const width = short.length * 6.7 + 14;
    s.x = Math.max(width / 2 + 6, Math.min(w - width / 2 - 6, s.x));
    const left = s.x - width / 2, top = s.y - 24;
    if (left < 5 || left + width > w - 5 || top < 6 || top > h - 24 ||
      occupied.some(r => left < r.x + r.w && left + width > r.x && top < r.y + 22 && top + 22 > r.y)) return;
    occupied.push({ x: left, y: top, w: width });
    const t = svgEl("text"); t.setAttribute("x", s.x); t.setAttribute("y", s.y - 9);
    t.setAttribute("text-anchor", "middle"); t.setAttribute("class", cls); t.textContent = short;
    recordLayers.labels.append(t);
  };
  if (focus && recordPoints.has(focus)) add(recordPoints.get(focus), byId.get(focus).label, "record-label selected", 56);
  if (focus) for (const e of incident.get(focus)) {
    const id = e.from === focus ? e.to : e.from, p = recordPoints.get(id);
    if (p) add(p, byId.get(id).label, "record-label");
  }
  for (const g of recordGroups) add(g, g.short, "record-group-label", 30);
  if (k > .65 && !focus) {
    let count = 0;
    for (const n of recordLabelPriority) {
      const p = recordPoints.get(n.id), s = screen(p);
      if (s.x < 0 || s.x > w || s.y < 0 || s.y > h) continue;
      add(p, n.label, "record-label");
      if (++count > 55) break;
    }
  }
}
function highlightRecord(id) {
  recordHighlighted = id;
  recordNear = new Set(id ? [id] : []);
  recordActiveEdges = id ? incident.get(id).filter(e => recordPoints.has(e.from) && recordPoints.has(e.to)) : [];
  for (const e of recordActiveEdges) { recordNear.add(e.from); recordNear.add(e.to); }
  $("records-focus").disabled = !recordSelection;
  $("records-inspect").disabled = !recordSelection;
  $("records-canvas").style.cursor = recordHover ? "pointer" : "grab";
  $("records-canvas").title = recordHover ? byId.get(recordHover).label : "";
  requestRecordPaint();
}
function selectRecord(id, animate = true) {
  if (!recordPoints.has(id)) return;
  recordSelection = id; recordHover = null;
  highlightRecord(id); renderRecordDetail(); focusRecordConnections(animate); saveURL();
}
function renderRecordDetail() {
  const panel = $("records-detail"); panel.replaceChildren();
  if (!recordSelection) {
    panel.append(el("span", "START WITH AN IDEA", "eyebrow"), el("h2", "Follow the connections."),
      el("p", "Each point is one detailed record. Search for a familiar idea, or select a point to reveal its neighbors and source evidence."),
      el("p", "The shared-concept map is the subject overview. This view keeps the underlying detail visible, including records with no connections."));
    if (data.atlas) {
      const b = el("button", "Go to shared concepts →"); b.onclick = () => { renderAtlas(); saveURL(); }; panel.append(b);
    }
    panel.append(el("h3", data.atlas ? "Topic groups" : "Source groups"));
    for (const group of recordGroups) {
      const b = el("button", undefined, "record-group-button"), dot = el("span", "●"); dot.style.color = group.color;
      b.append(dot, el("span", group.title), el("small", fmt(group.count)));
      b.onclick = () => {
        const points = [...recordPoints.values()].filter(p => p.group === group.id);
        recordFitted = false;
        moveRecordCamera(recordTarget({ x1: Math.min(...points.map(p => p.x)) - 80,
          x2: Math.max(...points.map(p => p.x)) + 80, y1: group.y - 50,
          y2: Math.max(...points.map(p => p.y)) + 80 }));
      };
      panel.append(b);
    }
    return;
  }
  const n = byId.get(recordSelection), links = incident.get(n.id);
  const close = el("button", "Clear selection ×", "quiet");
  close.onclick = () => { recordSelection = null; highlightRecord(null); renderRecordDetail(); fitRecords(); saveURL(); };
  panel.append(close, el("span", human(n.kind), "eyebrow"), el("h2", n.label), el("p", n.summary));
  const detail = el("button", "Evidence & full connections →");
  detail.onclick = () => { openNode(n.id); renderDetail(); };
  panel.append(detail, el("h3", `${fmt(links.length)} recorded connections`));
  let shown = 0;
  for (const e of links) {
    const id = e.from === n.id ? e.to : e.from;
    if (!recordPoints.has(id)) continue;
    const b = el("button", undefined, "record-neighbor");
    b.append(el("small", `${e.from === n.id ? "→" : "←"} ${human(e.relation)}`), el("span", byId.get(id).label));
    b.onclick = () => selectRecord(id); panel.append(b);
    if (++shown === 12) break;
  }
  if (links.length > shown) panel.append(el("p", "Open full connections to see every relation, including those outside this filter."));
}
function searchRecords() {
  const query = $("records-query").value.trim().toLowerCase(), results = $("records-results");
  results.replaceChildren(); results.hidden = !query;
  if (!query) return;
  const matches = recordVisible.filter(n => (n.label + " " + n.summary).toLowerCase().includes(query));
  results.append(el("p", `${fmt(matches.length)} matches${matches.length > 8 ? " · showing the first 8; refine your search" : ""}`));
  for (const n of matches.slice(0, 8)) {
    const b = el("button", n.label); b.onclick = () => {
      selectRecord(n.id); $("records-canvas").scrollIntoView({ block: "nearest" });
    }; results.append(b);
  }
}
function setRecordsExpanded(expanded) {
  $("records-view").classList.toggle("records-expanded", expanded);
  $("records-expand").textContent = expanded ? "Exit full screen ×" : "Full screen ⛶";
  $("records-expand").setAttribute("aria-pressed", String(expanded));
}
function zoomRecords(factor, anchor) {
  stopRecordAnimation(); recordFitted = false;
  const { w, h } = recordDimensions(), old = recordCamera.k;
  const k = Math.max(recordTarget(recordExtent).k * .65, Math.min(4, old * factor));
  const dx = (anchor?.x ?? w / 2) - w / 2, dy = (anchor?.y ?? h / 2) - h / 2;
  recordCamera = { x: recordCamera.x + dx / old - dx / k, y: recordCamera.y + dy / old - dy / k, k };
  paintRecordCamera();
}
function bindRecordsControls() {
  $("records-tab").onclick = () => { renderRecords(false); saveURL(); };
  $("records-all").onclick = () => openRecordGraph();
  $("records-filter").onchange = e => {
    recordFilter = e.target.value; recordScope = null; recordSelection = null; renderRecords(); saveURL();
  };
  $("records-query").oninput = () => { searchRecords(); saveURL(true); };
  $("records-fit").onclick = () => fitRecords();
  $("records-focus").onclick = () => focusRecordConnections();
  $("records-inspect").onclick = () => {
    setRecordsExpanded(false);
    $("records-detail").scrollIntoView({ block: "start", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
  };
  $("records-in").onclick = () => zoomRecords(1.35);
  $("records-out").onclick = () => zoomRecords(1 / 1.35);
  $("records-expand").onclick = () => setRecordsExpanded(!$("records-view").classList.contains("records-expanded"));
  const canvas = $("records-canvas"); let drag = null, moved = false;
  canvas.addEventListener("pointerdown", e => {
    if (e.button !== 0) return;
    stopRecordAnimation(); moved = false;
    drag = { x: e.clientX, y: e.clientY, camera: { ...recordCamera }, node: recordAt(e.clientX, e.clientY) };
    canvas.setPointerCapture(e.pointerId);
  });
  canvas.addEventListener("pointermove", e => {
    if (drag) {
      if (Math.hypot(e.clientX - drag.x, e.clientY - drag.y) < 4 && !moved) return;
      moved = true; recordFitted = false;
      recordCamera.x = drag.camera.x - (e.clientX - drag.x) / recordCamera.k;
      recordCamera.y = drag.camera.y - (e.clientY - drag.y) / recordCamera.k;
      requestRecordPaint();
    } else {
      const id = recordAt(e.clientX, e.clientY);
      if (id !== recordHover) { recordHover = id; highlightRecord(id || recordSelection); }
    }
  });
  canvas.addEventListener("pointerup", () => {
    const id = drag?.node; drag = null;
    if (!moved && id) selectRecord(id);
  });
  canvas.addEventListener("pointercancel", () => { drag = null; });
  canvas.addEventListener("pointerleave", () => {
    if (recordHover) { recordHover = null; highlightRecord(recordSelection); }
  });
  canvas.addEventListener("wheel", e => {
    // Keep native browser zoom and ordinary page scrolling. Alt-wheel zooms the map.
    if (!e.altKey || e.ctrlKey || e.metaKey) return;
    e.preventDefault(); const box = canvas.getBoundingClientRect();
    zoomRecords(Math.exp(-e.deltaY * .002), { x: e.clientX - box.left, y: e.clientY - box.top });
  }, { passive: false });
  canvas.addEventListener("keydown", e => {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    const delta = { ArrowLeft: [-70, 0], ArrowRight: [70, 0], ArrowUp: [0, -70], ArrowDown: [0, 70] }[e.key];
    if (delta) {
      e.preventDefault(); stopRecordAnimation(); recordFitted = false;
      recordCamera.x += delta[0] / recordCamera.k; recordCamera.y += delta[1] / recordCamera.k; paintRecordCamera();
    } else if (["+", "=", "-", "Home"].includes(e.key)) {
      e.preventDefault(); e.key === "Home" ? fitRecords() : zoomRecords(e.key === "-" ? 1 / 1.35 : 1.35);
    }
  });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && $("records-view").classList.contains("records-expanded")) {
      setRecordsExpanded(false); $("records-expand").focus();
    }
  });
  new ResizeObserver(() => {
    if (mode !== "records" || !recordExtent) return;
    measureRecords();
    recordBackgroundKey = null;
    if (recordFitted) fitRecords(false); else paintRecordCamera();
  }).observe(canvas);
}
