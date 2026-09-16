/* Shared knowledge, source browsing, and readable connections. No model calls. */
"use strict";
const $ = (id) => document.getElementById(id);
const fmt = (n) => n.toLocaleString();
const el = (tag, text, cls) => {
  const e = document.createElement(tag);
  if (text !== undefined) e.textContent = text;
  if (cls) e.className = cls;
  return e;
};
const svgEl = (tag) =>
  document.createElementNS("http://www.w3.org/2000/svg", tag);
const human = (s) => String(s || "concept").replaceAll("_", " ");
let catalog,
  data,
  nodes = [],
  edges = [],
  byId,
  incident,
  incoming;
let reading,
  mode = "browse",
  selected = null,
  returnView = "browse";
let searchScope = null,
  resultLimit = 60,
  expanded = new Set(),
  traced = false;
let laneLimits = new Map(),
  geometry = new Map(),
  zoom = 1,
  world = { width: 0, height: 0 };
let loadSequence = 0,
  noticeTimer;
let nodeTrail = [];
function say(message) {
  $("notice").textContent = message;
  $("notice").hidden = false;
  clearTimeout(noticeTimer);
  noticeTimer = setTimeout(() => ($("notice").hidden = true), 4500);
}
function bookTitle(id) {
  return (
    catalog.graphs.find((g) => g.project_id === id)?.title ||
    data.sources.find((s) => s.id === id)?.title ||
    id
  );
}
function directBooks(node) {
  return data.direct_books[node.id] || [];
}
function options(select, entries) {
  select.replaceChildren(
    ...entries.map(([id, label]) => {
      const o = el("option", label);
      o.value = id;
      return o;
    }),
  );
}
function show(view) {
  mode = view;
  for (const name of ["core", "browse", "search", "network", "overlap"])
    $(name + "-view").hidden = name !== view;
  for (const [id, name] of [
    ["core", "core"],
    ["chapters", "browse"],
    ["graph", "network"],
    ["overlap", "overlap"],
  ]) {
    const active = view === name;
    $(id + "-tab").classList.toggle("active", active);
    $(id + "-tab").setAttribute("aria-pressed", String(active));
  }
  document.querySelector(".lens").hidden = view !== "browse";
}
function saveURL(replace = false) {
  const params = new URLSearchParams({ graph: data.id });
  if (reading) params.set("reader", reading.id);
  if (mode === "network" && selected) params.set("node", selected);
  if (mode === "overlap") params.set("view", "overlap");
  if (mode === "browse") params.set("view", "browse");
  if (hasCore()) {
    params.set("compare", corePerspective);
    params.set("minimum", String(coreMinimum));
  }
  if (mode === "search") {
    params.set("view", "search");
    if ($("search").value) params.set("q", $("search").value);
    if ($("kind-select").value) params.set("kind", $("kind-select").value);
    if (searchScope?.pair) params.set("books", searchScope.pair.join(","));
    if (searchScope?.chapter) params.set("chapter", searchScope.chapter);
  }
  const url = "#" + params.toString();
  if (location.hash !== url)
    history[replace ? "replaceState" : "pushState"]({}, "", url);
}
async function loadGraph(id, params = new URLSearchParams()) {
  const seq = ++loadSequence;
  const graph = catalog.graphs.find((g) => g.id === id) || catalog.graphs[0];
  const response = await fetch(graph.file);
  if (!response.ok) throw new Error("This graph could not be loaded.");
  const payload = await response.json();
  if (seq !== loadSequence) return;
  data = payload;
  nodes = data.knowledge.nodes;
  edges = data.knowledge.edges;
  byId = new Map(nodes.map((n) => [n.id, n]));
  incident = new Map(nodes.map((n) => [n.id, []]));
  incoming = new Map(nodes.map((n) => [n.id, []]));
  for (const e of edges) {
    incident.get(e.from)?.push(e);
    if (e.from !== e.to) incident.get(e.to)?.push(e);
    if (e.relation === "prerequisite") incoming.get(e.to)?.push(e);
  }
  selected = null;
  nodeTrail = [];
  returnView = "browse";
  $("graph-tab").disabled = true;
  $("graph-tab").title = "Choose a concept first";
  $("graph-select").value = data.id;
  $("graph-count").textContent =
    `${fmt(nodes.length)} concepts · ${fmt(edges.length)} connections`;
  $("download").href = graph.file;
  $("download").download = graph.id + "-graph.json";
  const review = data.review || {};
  $("review-status").textContent = review.status
    ? `${human(review.status).replace(/^./, (c) => c.toUpperCase())}${review.human_audit ? " · Human audit " + human(review.human_audit) : ""}`
    : "Public graph · Review status unrecorded";
  options(
    $("reading-select"),
    data.reading_views.map((v) => [v.id, v.title]),
  );
  reading =
    data.reading_views.find((v) => v.id === params.get("reader")) ||
    data.reading_views[0];
  $("reading-select").value = reading.id;
  options($("kind-select"), [
    ["", "All types"],
    ...[...new Set(nodes.map((n) => n.kind))].sort().map((k) => [k, human(k)]),
  ]);
  $("kind-select").value = params.get("kind") || "";
  $("search").value = params.get("q") || "";
  searchScope = null;
  resultLimit = 60;
  renderBoard();
  renderOverlap();
  prepareCore(params);
  returnView = hasCore() ? "core" : "browse";
  if (params.get("node") && byId.has(params.get("node"))) {
    openNode(params.get("node"), false);
  } else if (params.get("view") === "overlap") show("overlap");
  else if (params.get("view") === "search") {
    if (params.get("books"))
      searchScope = { pair: params.get("books").split(",") };
    const chapter = reading.chapters.find(
      (c) => c.id === params.get("chapter"),
    );
    if (chapter)
      searchScope = {
        ids: new Set(chapter.nodes),
        title: chapter.label,
        chapter: chapter.id,
      };
    renderSearch();
  } else if (hasCore() && params.get("view") !== "browse") renderCore();
  else show("browse");
  saveURL(true);
}
function conceptCard(node, summary = false) {
  const card = el("button", undefined, "concept-card");
  card.dataset.node = node.id;
  card.append(el("span", node.label, "card-label"));
  if (summary) card.append(el("p", node.summary, "result-summary"));
  const meta = el("span", undefined, "card-meta");
  const books = directBooks(node).length;
  meta.append(
    el("span", human(node.kind)),
    el(
      "span",
      books > 1
        ? `${books} book graphs · ${incident.get(node.id).length} links`
        : `${incident.get(node.id).length} links →`,
    ),
  );
  card.append(meta);
  card.onclick = () => openNode(node.id);
  return card;
}
function renderBoard() {
  $("reading-title").textContent = reading.title;
  const hasChapters = reading.chapters.some((c) => c.first !== undefined);
  $("reading-caption").textContent = hasChapters
    ? "THE READING MAP"
    : "THE CONCEPT MAP";
  $("reading-description").textContent =
    `${fmt(reading.node_count)} concepts in this reading view. ${hasChapters ? "Chapter topics summarize the graph’s groups. " : ""}Choose an idea to follow its connections.`;
  options(
    $("chapter-jump"),
    reading.chapters.map((c) => [c.id, c.label]),
  );
  const board = $("board");
  board.replaceChildren();
  for (const chapter of reading.chapters) {
    const col = el("section", undefined, "chapter");
    col.dataset.chapter = chapter.id;
    const head = el("div", undefined, "chapter-head");
    const meta = el("div", undefined, "chapter-meta");
    meta.append(
      el("span", chapter.label, "chapter-number"),
      el("span", `${chapter.nodes.length} concepts`),
    );
    head.append(meta);
    head.append(
      el(
        "h2",
        chapter.topics[0] ||
          (hasChapters ? "Explore the concepts" : chapter.label),
      ),
    );
    head.append(
      el(
        "p",
        chapter.topics.slice(1).join(" · ") ||
          (chapter.first !== undefined
            ? `Source pages ${chapter.first}–${chapter.last}`
            : "Every concept remains searchable"),
      ),
    );
    const cards = el("div", undefined, "chapter-nodes");
    for (const id of chapter.nodes)
      if (byId.has(id)) cards.append(conceptCard(byId.get(id)));
    const browse = el(
      "button",
      `Browse all ${chapter.nodes.length} concepts ↗`,
      "chapter-link",
    );
    browse.onclick = () => {
      searchScope = {
        ids: new Set(chapter.nodes),
        title: chapter.label,
        chapter: chapter.id,
      };
      $("search").value = "";
      $("kind-select").value = "";
      resultLimit = 60;
      renderSearch();
      saveURL();
    };
    col.append(head, cards, browse);
    board.append(col);
  }
  if (!reading.chapters.length)
    board.append(
      el(
        "p",
        "This graph has no concepts yet. Open the guide to begin with your own materials.",
        "empty",
      ),
    );
  board.scrollLeft = 0;
}
function renderSearch() {
  show("search");
  const q = $("search").value.trim().toLocaleLowerCase();
  const kind = $("kind-select").value;
  const matches = nodes.filter(
    (n) =>
      (!kind || n.kind === kind) &&
      (!searchScope?.ids || searchScope.ids.has(n.id)) &&
      (!searchScope?.pair ||
        searchScope.pair.every((b) => directBooks(n).includes(b))) &&
      (!q || `${n.label} ${n.summary} ${n.id}`.toLocaleLowerCase().includes(q)),
  );
  matches.sort((a, b) => {
    if (q) {
      const rank = (n) =>
        n.label.toLocaleLowerCase().startsWith(q)
          ? 0
          : n.label.toLocaleLowerCase().includes(q)
            ? 1
            : 2;
      const d = rank(a) - rank(b);
      if (d) return d;
    }
    return a.label.localeCompare(b.label);
  });
  $("search-title").textContent = searchScope?.pair
    ? searchScope.pair.map(bookTitle).join(" × ")
    : searchScope?.title ||
      (q
        ? `Results for “${$("search").value.trim()}”`
        : "Every concept, in one place.");
  $("result-count").textContent =
    `${fmt(matches.length)} concepts${matches.length > resultLimit ? ` · Showing ${fmt(resultLimit)}` : ""}${searchScope ? " · Type to search across the whole graph" : ""}`;
  $("results").replaceChildren(
    ...matches.slice(0, resultLimit).map((n) => conceptCard(n, true)),
  );
  if (!matches.length)
    $("results").append(
      el(
        "p",
        "No concepts match. Try another term or clear the type filter.",
        "empty",
      ),
    );
  $("more").hidden = matches.length <= resultLimit;
}
function openNode(id, updateURL = true, remember = true) {
  if (!byId.has(id)) return;
  if (mode !== "network") {
    returnView = updateURL ? mode : hasCore() ? "core" : "browse";
    nodeTrail = [];
  } else if (remember && selected && selected !== id) nodeTrail.push(selected);
  selected = id;
  expanded = new Set([id]);
  traced = false;
  laneLimits = new Map();
  zoom = 1;
  $("network-title").textContent = byId.get(id).label;
  $("detail").hidden = true;
  $("graph-tab").disabled = false;
  $("graph-tab").title = "Return to the selected concept";
  show("network");
  renderNetwork(true);
  $("graph-cards")
    .querySelector(".selected .graph-node")
    ?.focus({ preventScroll: true });
  if (updateURL) saveURL();
}
function neighborhood() {
  const positions = new Map([[selected, 0]]);
  if (traced) {
    const queue = [selected];
    for (let i = 0; i < queue.length; i++) {
      const id = queue[i];
      for (const edge of incoming.get(id))
        if (!positions.has(edge.from)) {
          positions.set(edge.from, positions.get(id) - 1);
          queue.push(edge.from);
        }
    }
    return positions;
  }
  const included = new Set([selected]);
  for (const id of expanded)
    for (const edge of incident.get(id)) {
      included.add(edge.from);
      included.add(edge.to);
    }
  const visibleEdges = edges.filter(
    (e) =>
      e.relation === "prerequisite" &&
      (expanded.has(e.from) || expanded.has(e.to)),
  );
  // Classify by an actual directed path to/from the selection. A prerequisite
  // of a dependent is not necessarily a prerequisite of the selected concept.
  for (const upstream of [true, false]) {
    const queue = [[selected, 0]],
      visited = new Set([selected]);
    for (let i = 0; i < queue.length; i++) {
      const [id, depth] = queue[i];
      for (const e of visibleEdges) {
        if ((upstream ? e.to : e.from) !== id) continue;
        const next = upstream ? e.from : e.to;
        if (visited.has(next)) continue;
        visited.add(next);
        queue.push([next, depth + 1]);
        const lane = upstream ? -depth - 1 : depth === 0 ? 1 : depth + 2;
        if (!positions.has(next)) positions.set(next, lane);
      }
    }
  }
  for (const id of included) if (!positions.has(id)) positions.set(id, 2);
  return positions;
}
function laneTitle(lane) {
  if (lane === 0) return "SELECTED CONCEPT";
  if (traced)
    return Math.abs(lane) === 1
      ? "DIRECT PREREQUISITES"
      : `${Math.abs(lane)} LINKS UPSTREAM`;
  if (lane === -1) return "PREREQUISITES";
  if (lane === 1) return "DEPENDS ON THIS";
  if (lane === 2) return "OTHER CONNECTIONS";
  return lane < 0 ? `${-lane} LINKS UPSTREAM` : `${lane - 1} LINKS DOWNSTREAM`;
}
function renderNetwork(center = false) {
  if (!selected) return;
  const positions = neighborhood(),
    lanes = new Map();
  for (const [id, lane] of positions) {
    if (!lanes.has(lane)) lanes.set(lane, []);
    lanes.get(lane).push(id);
  }
  const cards = $("graph-cards");
  cards.replaceChildren();
  geometry = new Map();
  let maxBottom = 400;
  const ordered = [...lanes.keys()].sort((a, b) => a - b);
  for (const [column, lane] of ordered.entries()) {
    const ids = lanes
      .get(lane)
      .sort((a, b) => byId.get(a).label.localeCompare(byId.get(b).label));
    const limit = laneLimits.get(lane) || 8;
    const left = 38 + column * 334;
    const heading = el(
      "div",
      `${laneTitle(lane)} · ${ids.length}`,
      "lane-title",
    );
    heading.style.left = left + "px";
    heading.style.top = "22px";
    cards.append(heading);
    let top = 76;
    for (const id of ids.slice(0, limit)) {
      const node = byId.get(id);
      const cls =
        id === selected
          ? "selected"
          : lane < 0
            ? "prereq"
            : lane === 2 && !traced
              ? "other"
              : "dependent";
      const card = el("article", undefined, "graph-card " + cls);
      card.dataset.node = id;
      card.style.left = left + "px";
      card.style.top = top + "px";
      const open = el("button", undefined, "graph-node");
      open.append(
        el("span", node.label, "card-label"),
        el("span", human(node.kind), "card-meta"),
      );
      open.title =
        id === selected
          ? "Read this concept’s evidence"
          : "Make this the selected concept";
      open.onclick = () => (id === selected ? renderDetail() : openNode(id));
      card.append(open);
      if (!traced && id !== selected) {
        const undisplayed = incident
          .get(id)
          .filter((e) => !positions.has(e.from) || !positions.has(e.to));
        if (undisplayed.length) {
          const expand = el(
            "button",
            `+ Reveal ${new Set(undisplayed.map((e) => (e.from === id ? e.to : e.from))).size} nearby concepts`,
            "expand-node",
          );
          expand.onclick = () => {
            expanded.add(id);
            renderNetwork();
          };
          card.append(expand);
        } else
          card.append(
            el("span", "All adjacent concepts are in this view", "card-meta"),
          );
      } else if (id === selected) {
        const inspect = el(
          "button",
          "Read summary & evidence ↗",
          "expand-node",
        );
        inspect.onclick = () => renderDetail();
        card.append(inspect);
      }
      card.onpointerenter = () => highlight(id);
      card.onpointerleave = () => highlight(null);
      card.onfocusin = () => highlight(id);
      card.onfocusout = () => highlight(null);
      cards.append(card);
      const height = card.offsetHeight;
      geometry.set(id, { x: left, y: top, w: 244, h: height });
      top += height + 26;
    }
    if (ids.length > limit) {
      const more = el(
        "button",
        `Show ${Math.min(12, ids.length - limit)} more (${ids.length - limit} remaining)`,
        "lane-more",
      );
      more.style.left = left + "px";
      more.style.top = top + "px";
      more.onclick = () => {
        laneLimits.set(lane, limit + 12);
        renderNetwork();
      };
      cards.append(more);
      top += 65;
    }
    maxBottom = Math.max(maxBottom, top + 60);
  }
  world = {
    width: Math.max(480, ordered.length * 334 + 20),
    height: maxBottom,
  };
  drawEdges();
  applyZoom();
  $("map-count").textContent =
    `${geometry.size} of ${positions.size} concepts in ${traced ? "the prerequisite trace" : "this neighborhood"} · Arrows follow recorded relations`;
  $("trace").classList.toggle("active", traced);
  $("trace").setAttribute("aria-pressed", String(traced));
  if (center) centerSelected();
}
function drawEdges() {
  const svg = $("edges");
  svg.replaceChildren();
  svg.setAttribute("width", world.width);
  svg.setAttribute("height", world.height);
  const defs = svgEl("defs"),
    marker = svgEl("marker"),
    tip = svgEl("path");
  marker.id = "arrow";
  marker.setAttribute("viewBox", "0 0 10 10");
  marker.setAttribute("refX", "9");
  marker.setAttribute("refY", "5");
  marker.setAttribute("markerWidth", "6");
  marker.setAttribute("markerHeight", "6");
  marker.setAttribute("orient", "auto");
  tip.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
  tip.setAttribute("fill", "#83a4b5");
  marker.append(tip);
  defs.append(marker);
  svg.append(defs);
  for (const edge of edges) {
    if (traced && edge.relation !== "prerequisite") continue;
    if (!traced && !expanded.has(edge.from) && !expanded.has(edge.to)) continue;
    const a = geometry.get(edge.from),
      b = geometry.get(edge.to);
    if (!a || !b) continue;
    const path = svgEl("path");
    const right = b.x > a.x,
      same = a.x === b.x;
    const x1 = a.x + (right || same ? a.w : 0),
      y1 = a.y + a.h / 2;
    const x2 = b.x + (right ? 0 : b.w),
      y2 = b.y + b.h / 2;
    const bend = same ? 70 : Math.max(40, Math.abs(x2 - x1) * 0.45);
    const d = same
      ? `M${x1},${y1} C${x1 + bend},${y1} ${x2 + bend},${y2} ${x2},${y2}`
      : `M${x1},${y1} C${x1 + (right ? bend : -bend)},${y1} ${x2 + (right ? -bend : bend)},${y2} ${x2},${y2}`;
    path.setAttribute("d", d);
    path.setAttribute(
      "class",
      "graph-edge " +
        (edge.relation === "prerequisite" ? "prerequisite" : "other"),
    );
    path.setAttribute("marker-end", "url(#arrow)");
    path.dataset.from = edge.from;
    path.dataset.to = edge.to;
    const title = svgEl("title");
    title.textContent = `${byId.get(edge.from).label} → ${byId.get(edge.to).label}: ${human(edge.relation)}`;
    path.append(title);
    svg.append(path);
  }
}
function highlight(id) {
  const neighbors = new Set([id]);
  for (const path of $("edges").querySelectorAll(".graph-edge")) {
    const lit = path.dataset.from === id || path.dataset.to === id;
    path.classList.toggle("lit", Boolean(id) && lit);
    path.classList.toggle("dim", Boolean(id) && !lit);
    if (lit) {
      neighbors.add(path.dataset.from);
      neighbors.add(path.dataset.to);
    }
  }
  for (const card of $("graph-cards").querySelectorAll(".graph-card")) {
    card.classList.toggle(
      "lit",
      Boolean(id) && neighbors.has(card.dataset.node),
    );
    card.classList.toggle(
      "dim",
      Boolean(id) && !neighbors.has(card.dataset.node),
    );
  }
}
function applyZoom() {
  $("graph-world").style.width = world.width + "px";
  $("graph-world").style.height = world.height + "px";
  $("graph-world").style.transform = `scale(${zoom})`;
  const viewportWidth = $("graph-scroll").clientWidth;
  $("graph-world").style.marginLeft =
    Math.max(0, (viewportWidth - world.width * zoom) / 2) + "px";
  $("graph-sizer").style.width =
    Math.max(viewportWidth, world.width * zoom) + "px";
  $("graph-sizer").style.height = world.height * zoom + "px";
  $("zoom-label").textContent = Math.round(zoom * 100) + "%";
  $("zoom-out").disabled = zoom <= 0.6;
  $("zoom-in").disabled = zoom >= 1.6;
}
function changeZoom(delta) {
  const scroll = $("graph-scroll"),
    old = zoom;
  zoom = Math.max(0.6, Math.min(1.6, Math.round((zoom + delta) * 10) / 10));
  const x = (scroll.scrollLeft + scroll.clientWidth / 2) / old;
  const y = (scroll.scrollTop + scroll.clientHeight / 2) / old;
  applyZoom();
  scroll.scrollLeft = x * zoom - scroll.clientWidth / 2;
  scroll.scrollTop = y * zoom - scroll.clientHeight / 2;
}
function centerSelected() {
  const root = geometry.get(selected),
    scroll = $("graph-scroll");
  if (!root) return;
  scroll.scrollLeft = Math.max(
    0,
    (root.x + root.w / 2) * zoom - scroll.clientWidth / 2,
  );
  scroll.scrollTop = Math.max(0, root.y * zoom - 85);
}
function evidence(refs) {
  const frag = document.createDocumentFragment();
  for (const ref of refs || []) {
    const e = el("div", undefined, "evidence");
    e.append(
      el("strong", bookTitle(ref.source)),
      el(
        "span",
        [ref.section, ref.pages?.length ? `pages ${ref.pages.join(", ")}` : ""]
          .filter(Boolean)
          .join(" · "),
      ),
    );
    frag.append(e);
  }
  return frag;
}
function renderDetail() {
  const node = byId.get(selected),
    panel = $("detail");
  panel.replaceChildren();
  panel.hidden = false;
  const top = el("div", undefined, "detail-top"),
    close = el("button", "×");
  close.setAttribute("aria-label", "Close evidence");
  close.onclick = () => {
    panel.hidden = true;
    $("detail-open").focus();
  };
  top.append(el("span", human(node.kind), "badge"), close);
  panel.append(top, el("h2", node.label), el("p", node.summary));
  const link = el("button", "Copy link to this concept", "text-button");
  link.onclick = () => copy(location.href);
  panel.append(link);
  if (node.evidence?.length)
    panel.append(el("h4", "SOURCE EVIDENCE"), evidence(node.evidence));
  if (node.notation?.length) {
    panel.append(el("h4", "NOTATION & QUALIFICATIONS"));
    for (const item of node.notation)
      panel.append(el("p", `${bookTitle(item.source)}: ${item.note}`));
  }
  if (node.origins?.length) {
    panel.append(el("h4", "BOOK TREATMENTS"));
    for (const origin of node.origins) {
      const row = el("div", undefined, "origin");
      const graph = catalog.graphs.find((g) => g.project_id === origin.project);
      const button = el(
        graph ? "button" : "span",
        bookTitle(origin.project) + (graph ? " ↗" : ""),
      );
      if (graph)
        button.onclick = () => {
          const params = new URLSearchParams({ node: origin.node });
          navigateGraph(graph.id, params);
        };
      row.append(button);
      if (origin.note) row.append(el("p", origin.note));
      panel.append(row);
    }
  }
  panel.append(el("h4", `CONNECTIONS · ${incident.get(node.id).length}`));
  if (!incident.get(node.id).length)
    panel.append(el("p", "No connections are recorded for this concept."));
  for (const edge of incident.get(node.id)) {
    const other = edge.from === node.id ? edge.to : edge.from;
    const row = el("div", undefined, "connection"),
      button = el("button", byId.get(other).label);
    button.onclick = () => openNode(other);
    let relationship = human(edge.relation);
    if (edge.relation === "prerequisite")
      relationship =
        edge.to === node.id
          ? "Needed before this concept"
          : "Depends on this concept";
    else relationship += edge.from === node.id ? " · outgoing" : " · incoming";
    if (edge.necessity) relationship += " · " + human(edge.necessity);
    row.append(button, el("small", relationship));
    const detail = el("details"),
      summary = el("summary", "Why this connection?");
    detail.append(summary);
    if (edge.rationale) detail.append(el("p", edge.rationale));
    if (edge.failure_mode)
      detail.append(el("p", "Without it: " + edge.failure_mode));
    if (edge.source_level || edge.target_level)
      detail.append(
        el(
          "p",
          `Mastery: ${edge.source_level || "—"} → ${edge.target_level || "—"}`,
        ),
      );
    detail.append(evidence(edge.evidence));
    row.append(detail);
    panel.append(row);
  }
  panel.append(el("div", node.id, "detail-id"));
  panel.scrollTop = 0;
  close.focus();
}
function renderOverlap() {
  const ids = [...new Set(nodes.flatMap(directBooks))].sort();
  const grid = $("overlap-grid");
  grid.replaceChildren();
  $("overlap-tab").disabled = ids.length < 2;
  $("overlap-tab").title =
    ids.length < 2
      ? "Available in a shared graph with book correspondences"
      : "Browse shared concepts";
  for (let i = 0; i < ids.length; i++)
    for (let j = i + 1; j < ids.length; j++) {
      const pair = [ids[i], ids[j]],
        count = nodes.filter((n) =>
          pair.every((id) => directBooks(n).includes(id)),
        ).length;
      const b = el("button", undefined, "pair");
      b.dataset.books = pair.join(",");
      b.append(
        el("strong", fmt(count)),
        el("span", pair.map(bookTitle).join(" × ")),
        el("small", "shared concepts · Open the comparison →"),
      );
      b.onclick = () => {
        searchScope = { pair };
        $("search").value = "";
        $("kind-select").value = "";
        resultLimit = 60;
        renderSearch();
        saveURL();
      };
      grid.append(b);
    }
  if (ids.length < 2)
    grid.append(
      el(
        "p",
        "Book comparison needs a shared graph with recorded book correspondences.",
        "empty",
      ),
    );
}
async function copy(value) {
  try {
    await navigator.clipboard.writeText(value);
    say("Copied.");
  } catch {
    say("Clipboard access is unavailable. Select the text and copy it.");
  }
}
function navigateGraph(id, params = new URLSearchParams()) {
  params.set("graph", id);
  history.pushState({}, "", "#" + params.toString());
  loadGraph(id, params).catch((error) => say(error.message));
}
$("graph-select").onchange = (e) => navigateGraph(e.target.value);
$("reading-select").onchange = (e) => {
  reading = data.reading_views.find((v) => v.id === e.target.value);
  renderBoard();
  show("browse");
  saveURL();
};
$("chapter-jump").onchange = (e) => {
  const column = [...$("board").children].find(
    (c) => c.dataset.chapter === e.target.value,
  );
  if (column)
    $("board").scrollTo({ left: column.offsetLeft - 30, behavior: "smooth" });
};
$("scroll-left").onclick = () =>
  $("board").scrollBy({ left: -608, behavior: "smooth" });
$("scroll-right").onclick = () =>
  $("board").scrollBy({ left: 608, behavior: "smooth" });
$("all-concepts").onclick = () => {
  searchScope = null;
  $("search").value = "";
  $("kind-select").value = "";
  resultLimit = 60;
  renderSearch();
  saveURL();
};
$("search").oninput = () => {
  searchScope = null;
  resultLimit = 60;
  renderSearch();
  saveURL(true);
};
$("kind-select").onchange = () => {
  resultLimit = 60;
  renderSearch();
  saveURL(true);
};
$("more").onclick = () => {
  resultLimit += 60;
  renderSearch();
};
$("clear").onclick = () => {
  $("search").value = "";
  if (hasCore()) renderCore(false);
  else show("browse");
  saveURL();
};
$("chapters-tab").onclick = () => {
  $("search").value = "";
  show("browse");
  saveURL();
};
$("graph-tab").onclick = () => {
  if (selected) {
    show("network");
    renderNetwork(true);
    saveURL();
  }
};
$("overlap-tab").onclick = () => {
  show("overlap");
  saveURL();
};
$("back").onclick = () => {
  if (nodeTrail.length) {
    openNode(nodeTrail.pop(), true, false);
    return;
  }
  if (returnView === "core") renderCore(false);
  else show(returnView === "network" ? "browse" : returnView);
  saveURL();
};
$("trace").onclick = () => {
  traced = true;
  laneLimits = new Map();
  renderNetwork(true);
};
$("reset-network").onclick = () => {
  traced = false;
  expanded = new Set([selected]);
  laneLimits = new Map();
  renderNetwork(true);
};
$("detail-open").onclick = () => {
  if ($("detail").hidden) renderDetail();
  else $("detail").hidden = true;
};
$("zoom-out").onclick = () => changeZoom(-0.1);
$("zoom-in").onclick = () => changeZoom(0.1);
$("fit").onclick = () => {
  zoom = 1;
  applyZoom();
  centerSelected();
};
const scroll = $("graph-scroll");
let drag;
scroll.onpointerdown = (e) => {
  if (
    e.pointerType !== "mouse" ||
    e.button !== 0 ||
    e.target.closest("button, article")
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
  if (!drag) return;
  scroll.scrollLeft = drag.left + drag.x - e.clientX;
  scroll.scrollTop = drag.top + drag.y - e.clientY;
};
scroll.onpointerup = scroll.onpointercancel = () => {
  drag = null;
  scroll.classList.remove("dragging");
};
new ResizeObserver(() => {
  if (selected && mode === "network") applyZoom();
}).observe(scroll);
for (const id of ["about-open", "setup-open"])
  $(id).onclick = () => $("about-dialog").showModal();
$("about-close").onclick = () => $("about-dialog").close();
$("copy-prompt").onclick = () => copy($("setup-prompt").textContent);
document.addEventListener("keydown", (e) => {
  if (
    e.key === "/" &&
    !e.target.closest("input, select, textarea") &&
    !$("about-dialog").open
  ) {
    e.preventDefault();
    $("search").focus();
  }
  if (e.key === "Escape" && !$("detail").hidden) {
    $("detail").hidden = true;
    $("detail-open").focus();
  }
});
window.addEventListener("popstate", () => {
  const params = new URLSearchParams(location.hash.slice(1));
  loadGraph(params.get("graph"), params).catch((error) => say(error.message));
});
async function boot() {
  const response = await fetch("catalog.json");
  if (!response.ok) throw new Error("The graph catalog could not be loaded.");
  catalog = await response.json();
  if (!catalog.graphs.length)
    throw new Error("No graphs have been published yet.");
  options(
    $("graph-select"),
    catalog.graphs.map((g) => [g.id, g.title]),
  );
  const params = new URLSearchParams(location.hash.slice(1));
  await loadGraph(params.get("graph"), params);
}
bindCoreControls();
boot().catch((error) => {
  $("reading-title").textContent = "Unable to open this graph";
  $("reading-description").textContent = error.message;
  say(error.message);
});
