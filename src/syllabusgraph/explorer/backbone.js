/* A derived view of recorded overlap, independent of any course or source order. */
"use strict";
let corePerspective = "textbooks",
  coreMinimum = null,
  coreZoom = 1;
let coreWorld = { width: 0, height: 0 },
  corePositions = new Map(),
  coreJumps = new Map();
function hasCore() {
  return Boolean(data?.backbone?.available);
}
function coreScope() {
  return data.backbone.perspectives[corePerspective];
}
function coreLevel() {
  return coreScope().levels.find((l) => l.minimum === coreMinimum);
}
function prepareCore(params) {
  $("core-tab").hidden = !hasCore();
  if (!hasCore()) return;
  corePerspective =
    params.get("compare") === "volumes" ? "volumes" : "textbooks";
  if (!coreScope().levels.length) corePerspective = "volumes";
  $("comparison-mode").querySelector('[value="textbooks"]').disabled =
    !data.backbone.perspectives.textbooks.levels.length;
  $("comparison-mode").value = corePerspective;
  coreMinimum = Number(params.get("minimum")) || coreScope().units.length;
  if (!coreScope().levels.some((l) => l.minimum === coreMinimum))
    coreMinimum = coreScope().units.length;
  coreZoom = 1;
}
function renderCore(reset = true) {
  if (!hasCore()) return;
  show("core");
  const scope = coreScope(),
    level = coreLevel(),
    total = scope.units.length;
  const unitName = corePerspective === "volumes" ? "book graphs" : "textbooks";
  options(
    $("core-threshold"),
    [...scope.levels]
      .reverse()
      .map((l) => [
        String(l.minimum),
        l.minimum === total
          ? `All ${total} ${unitName}`
          : `At least ${l.minimum} ${unitName}`,
      ]),
  );
  $("core-threshold").value = String(coreMinimum);
  $("core-description").textContent = scope.units
    .map((u) => u.title)
    .join(" · ");
  const stats = $("core-stats");
  stats.replaceChildren();
  const count = level.nodes.length,
    connected = level.components.filter((c) => c.nodes.length > 1);
  for (const [value, label, note] of [
    [
      fmt(count),
      "Common concepts",
      coreMinimum === total
        ? `Independently treated in all ${total}`
        : `Independently treated in ${coreMinimum}+`,
    ],
    [
      fmt(level.edges.length),
      "Connections within the core",
      `${level.relations.prerequisite || 0} prerequisite relations`,
    ],
    [
      nodes.length ? ((count / nodes.length) * 100).toFixed(1) + "%" : "0%",
      "Of the shared graph",
      `${fmt(nodes.length)} concepts in total`,
    ],
    [
      fmt(level.components.length),
      "Separate components",
      `Largest: ${level.components[0]?.nodes.length || 0} concepts · ${level.isolated} isolated`,
    ],
  ]) {
    const stat = el("div", undefined, "core-stat");
    stat.append(el("strong", value), el("span", label), el("small", note));
    stats.append(stat);
  }
  $("core-agreement-caption").textContent =
    `Exact number of independently matched ${unitName}. Imported inputs do not count as an independent treatment.`;
  const bars = $("agreement-bars");
  bars.replaceChildren();
  for (const row of [...scope.distribution].reverse()) {
    const bar = el("div", undefined, "agreement-row"),
      text = el("div", undefined, "agreement-label");
    text.append(
      el(
        "span",
        row.count === 0
          ? "No independent match"
          : `${row.count} of ${total} ${unitName}`,
      ),
      el("strong", fmt(row.nodes)),
    );
    const track = el("div", undefined, "agreement-track"),
      fill = el("div");
    fill.style.width =
      (nodes.length ? (100 * row.nodes) / nodes.length : 0) + "%";
    if (row.count >= coreMinimum) fill.className = "included";
    track.append(fill);
    bar.append(text, track);
    bars.append(bar);
  }
  const links = $("component-links");
  links.replaceChildren();
  for (const [i, component] of connected.entries()) {
    const button = el("button", undefined, "component-jump");
    button.append(
      el("strong", `Component ${i + 1}`),
      el(
        "span",
        `${component.nodes.length} concepts · ${component.edges.length} links`,
      ),
    );
    button.onclick = () => jumpCore(String(i));
    links.append(button);
  }
  if (level.isolated) {
    const button = el("button", undefined, "component-jump");
    button.append(
      el("strong", "Isolated within this core"),
      el(
        "span",
        `${level.isolated} concepts · May connect through the wider graph`,
      ),
    );
    button.onclick = () => jumpCore("isolated");
    links.append(button);
  }
  options($("core-jump"), [
    ["top", "Jump to a component…"],
    ...connected.map((c, i) => [
      String(i),
      `Component ${i + 1} · ${c.nodes.length} concepts`,
    ]),
    ...(level.isolated
      ? [["isolated", `${level.isolated} isolated concepts`]]
      : []),
  ]);
  $("core-map-caption").textContent =
    `${count} concepts · ${level.edges.length} recorded connections · Click a concept to inspect it`;
  renderCoreGraph(level, connected);
  if (reset) {
    $("core-scroll").scrollTop = 0;
    $("core-scroll").scrollLeft = 0;
  }
}
function componentRanks(component, edgeList) {
  const incoming = new Map(component.nodes.map((id) => [id, 0])),
    outgoing = new Map(component.nodes.map((id) => [id, []]));
  const ranks = new Map(component.nodes.map((id) => [id, 0]));
  for (const e of edgeList)
    if (e.relation === "prerequisite") {
      incoming.set(e.to, incoming.get(e.to) + 1);
      outgoing.get(e.from).push(e.to);
    }
  const queue = component.nodes.filter((id) => incoming.get(id) === 0);
  for (let i = 0; i < queue.length; i++)
    for (const next of outgoing.get(queue[i])) {
      ranks.set(next, Math.max(ranks.get(next), ranks.get(queue[i]) + 1));
      incoming.set(next, incoming.get(next) - 1);
      if (incoming.get(next) === 0) queue.push(next);
    }
  return ranks;
}
function coreCard(id, x, y) {
  const n = byId.get(id),
    card = el("button", undefined, "core-card");
  card.dataset.node = id;
  const agreements = coreScope().memberships[id].length;
  card.classList.toggle("universal", agreements === coreScope().units.length);
  card.style.left = x + "px";
  card.style.top = y + "px";
  card.append(
    el("span", n.label, "card-label"),
    el(
      "span",
      `${agreements}/${coreScope().units.length} matched · ${human(n.kind)}`,
      "card-meta",
    ),
  );
  card.onclick = () => openNode(id);
  card.onpointerenter = card.onfocus = () => highlightCore(id);
  card.onpointerleave = card.onblur = () => highlightCore(null);
  $("core-cards").append(card);
  const height = card.offsetHeight;
  corePositions.set(id, { x, y, w: 222, h: height });
  return height;
}
function renderCoreGraph(level, components) {
  const cards = $("core-cards");
  cards.replaceChildren();
  corePositions = new Map();
  coreJumps = new Map();
  const edgeById = new Map(edges.map((e) => [e.id, e]));
  let top = 25,
    maxWidth = 600;
  for (const [index, c] of components.entries()) {
    coreJumps.set(String(index), top);
    const heading = el(
      "div",
      `COMPONENT ${index + 1} · ${c.nodes.length} CONCEPTS · ${c.edges.length} CONNECTIONS`,
      "core-component-title",
    );
    heading.style.top = top + "px";
    heading.style.left = "30px";
    cards.append(heading);
    const edgeList = c.edges.map((id) => edgeById.get(id)),
      ranks = componentRanks(c, edgeList);
    const lanes = new Map();
    for (const [id, rank] of ranks) {
      if (!lanes.has(rank)) lanes.set(rank, []);
      lanes.get(rank).push(id);
    }
    const order = new Map();
    let bottom = top;
    for (const [rank, ids] of [...lanes].sort((a, b) => a[0] - b[0])) {
      // One barycentric pass reduces crossings; only actual prerequisites define ranks.
      const parentOrder = (id) => {
        const parents = edgeList.filter(
          (e) =>
            e.relation === "prerequisite" && e.to === id && order.has(e.from),
        );
        return parents.length
          ? parents.reduce((s, e) => s + order.get(e.from), 0) / parents.length
          : 0;
      };
      ids.sort(
        (a, b) =>
          parentOrder(a) - parentOrder(b) ||
          byId.get(a).label.localeCompare(byId.get(b).label),
      );
      let y = top + 45;
      for (const [row, id] of ids.entries()) {
        order.set(id, row);
        y += coreCard(id, 30 + rank * 282, y) + 21;
      }
      bottom = Math.max(bottom, y);
      maxWidth = Math.max(maxWidth, 282 * rank + 290);
    }
    top = bottom + 55;
  }
  const isolated = level.components
    .filter((c) => c.nodes.length === 1)
    .flatMap((c) => c.nodes);
  if (isolated.length) {
    coreJumps.set("isolated", top);
    const heading = el(
      "div",
      `ISOLATED IN THIS CORE · ${isolated.length} CONCEPTS`,
      "core-component-title",
    );
    heading.style.top = top + "px";
    heading.style.left = "30px";
    cards.append(heading);
    top += 45;
    const columns = 3;
    isolated.sort((a, b) => byId.get(a).label.localeCompare(byId.get(b).label));
    for (let i = 0; i < isolated.length; i += columns) {
      let height = 0;
      for (let col = 0; col < columns && i + col < isolated.length; col++)
        height = Math.max(
          height,
          coreCard(isolated[i + col], 30 + col * 252, top),
        );
      top += height + 21;
    }
    maxWidth = Math.max(
      maxWidth,
      Math.min(columns, isolated.length) * 252 + 30,
    );
  }
  if (!level.nodes.length) {
    cards.append(
      el(
        "p",
        "No concepts have recorded independent treatments at this threshold. Choose a broader overlap above.",
        "core-empty",
      ),
    );
  }
  coreWorld = { width: maxWidth, height: Math.max(350, top + 35) };
  const svg = $("core-edges");
  svg.replaceChildren();
  svg.setAttribute("width", coreWorld.width);
  svg.setAttribute("height", coreWorld.height);
  const defs = svgEl("defs"),
    marker = svgEl("marker"),
    tip = svgEl("path");
  marker.id = "core-arrow";
  marker.setAttribute("viewBox", "0 0 10 10");
  marker.setAttribute("refX", "9");
  marker.setAttribute("refY", "5");
  marker.setAttribute("markerWidth", "5");
  marker.setAttribute("markerHeight", "5");
  marker.setAttribute("orient", "auto");
  tip.setAttribute("d", "M0,0 L10,5 L0,10 z");
  tip.setAttribute("fill", "#759aa9");
  marker.append(tip);
  defs.append(marker);
  svg.append(defs);
  for (const id of level.edges) {
    const e = edgeById.get(id),
      a = corePositions.get(e.from),
      b = corePositions.get(e.to);
    if (!a || !b) continue;
    const right = b.x > a.x,
      same = b.x === a.x;
    const x1 = a.x + (right || same ? a.w : 0),
      x2 = b.x + (right ? 0 : b.w),
      y1 = a.y + a.h / 2,
      y2 = b.y + b.h / 2;
    const bend = same ? 38 : Math.max(27, Math.abs(x2 - x1) / 2),
      path = svgEl("path");
    path.setAttribute(
      "d",
      `M${x1},${y1} C${x1 + (right || same ? bend : -bend)},${y1} ${x2 + (right ? -bend : bend)},${y2} ${x2},${y2}`,
    );
    path.setAttribute(
      "class",
      "core-edge " + (e.relation === "prerequisite" ? "prerequisite" : "other"),
    );
    path.setAttribute("marker-end", "url(#core-arrow)");
    path.dataset.from = e.from;
    path.dataset.to = e.to;
    path.dataset.edge = id;
    svg.append(path);
  }
  applyCoreZoom();
}
function highlightCore(id) {
  const neighbors = new Set([id]);
  for (const path of $("core-edges").querySelectorAll(".core-edge")) {
    const lit = path.dataset.from === id || path.dataset.to === id;
    path.classList.toggle("lit", Boolean(id) && lit);
    path.classList.toggle("dim", Boolean(id) && !lit);
    if (lit) {
      neighbors.add(path.dataset.from);
      neighbors.add(path.dataset.to);
    }
  }
  for (const card of $("core-cards").querySelectorAll(".core-card")) {
    card.classList.toggle(
      "dim",
      Boolean(id) && !neighbors.has(card.dataset.node),
    );
    card.classList.toggle(
      "lit",
      Boolean(id) && neighbors.has(card.dataset.node),
    );
  }
}
function applyCoreZoom() {
  $("core-world").style.width = coreWorld.width + "px";
  $("core-world").style.height = coreWorld.height + "px";
  $("core-world").style.transform = `scale(${coreZoom})`;
  $("core-sizer").style.width = coreWorld.width * coreZoom + "px";
  $("core-sizer").style.height = coreWorld.height * coreZoom + "px";
  $("core-zoom-label").textContent = Math.round(coreZoom * 100) + "%";
  $("core-zoom-out").disabled = coreZoom <= 0.6;
  $("core-zoom-in").disabled = coreZoom >= 1.4;
}
function jumpCore(id) {
  $("core-scroll").scrollTo({
    left: 0,
    top: Math.max(0, coreJumps.get(id) * coreZoom - 15),
    behavior: "smooth",
  });
}
function bindCoreControls() {
  $("core-jump").onchange = (e) =>
    e.target.value === "top"
      ? $("core-scroll").scrollTo({ top: 0, left: 0 })
      : jumpCore(e.target.value);
  $("core-tab").onclick = () => {
    renderCore(false);
    saveURL();
  };
  $("comparison-mode").onchange = (e) => {
    corePerspective = e.target.value;
    coreMinimum = coreScope().units.length;
    coreZoom = 1;
    renderCore();
    saveURL();
  };
  $("core-threshold").onchange = (e) => {
    coreMinimum = Number(e.target.value);
    coreZoom = 1;
    renderCore();
    saveURL();
  };
  const change = (delta) => {
    const scroll = $("core-scroll"),
      x = (scroll.scrollLeft + scroll.clientWidth / 2) / coreZoom,
      y = (scroll.scrollTop + scroll.clientHeight / 2) / coreZoom;
    coreZoom = Math.max(
      0.6,
      Math.min(1.4, Math.round((coreZoom + delta) * 10) / 10),
    );
    applyCoreZoom();
    scroll.scrollLeft = x * coreZoom - scroll.clientWidth / 2;
    scroll.scrollTop = y * coreZoom - scroll.clientHeight / 2;
  };
  $("core-zoom-out").onclick = () => change(-0.1);
  $("core-zoom-in").onclick = () => change(0.1);
  $("core-center").onclick = () => {
    coreZoom = 1;
    applyCoreZoom();
    $("core-scroll").scrollTo({ left: 0, top: 0 });
  };
  const scroll = $("core-scroll");
  let drag;
  scroll.onpointerdown = (e) => {
    if (
      e.pointerType !== "mouse" ||
      e.button !== 0 ||
      e.target.closest("button")
    )
      return;
    drag = {
      x: e.clientX,
      y: e.clientY,
      left: scroll.scrollLeft,
      top: scroll.scrollTop,
    };
    scroll.setPointerCapture(e.pointerId);
    scroll.classList.add("dragging");
  };
  scroll.onpointermove = (e) => {
    if (drag) {
      scroll.scrollLeft = drag.left + drag.x - e.clientX;
      scroll.scrollTop = drag.top + drag.y - e.clientY;
    }
  };
  scroll.onpointerup = scroll.onpointercancel = () => {
    drag = null;
    scroll.classList.remove("dragging");
  };
}
