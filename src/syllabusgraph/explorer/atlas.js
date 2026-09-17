/* Reviewed concepts, exact source connections, and explicit book coverage. */
"use strict";
let atlasMinimum = 3,
  atlasSelected = null,
  atlasScale = 1;
let atlasPositions = new Map(),
  atlasSize = { width: 1000, height: 800 };
const atlasBooks = new Map();
const atlasColors = [
  "#74d8cb",
  "#92bafa",
  "#e6ba76",
  "#c1a3ef",
  "#e99eac",
  "#93c78f",
  "#eba88b",
  "#b6b8f2",
  "#73c8e3",
  "#c4cd80",
  "#d59cd3",
  "#84c4b1",
  "#dcb996",
  "#a8b1d1",
  "#acc796",
];
function prepareAtlas(params) {
  atlasSelected = params.get("concept");
  atlasMinimum = Number(
    params.get("coverage") ?? data.atlas?.works.length ?? 0,
  );
  if (!data.atlas) return;
  atlasMinimum = Math.max(0, Math.min(data.atlas.works.length, atlasMinimum));
  options($("atlas-coverage"), [
    [String(data.atlas.works.length), `All ${data.atlas.works.length} works`],
    ...(data.atlas.works.length > 2 ? [["2", "Two or more works"]] : []),
    ["0", "Every concept"],
  ]);
  $("atlas-coverage").value = String(atlasMinimum);
  $("atlas-context").checked = params.get("context") === "on";
  $("atlas-detail-level").value =
    params.get("detail") === "all" ? "all" : "landmarks";
  $("atlas-query").value = params.get("find") || "";
}
function saveAtlasURL(params) {
  params.set("coverage", String(atlasMinimum));
  if (atlasSelected) params.set("concept", atlasSelected);
  if ($("atlas-context").checked) params.set("context", "on");
  if ($("atlas-detail-level").value === "all") params.set("detail", "all");
  if ($("atlas-query").value) params.set("find", $("atlas-query").value);
}
function atlasForest(links, identities) {
  // A display reduction only: every retained line still has exact source witnesses.
  const parents = new Map([...identities].map((id) => [id, id]));
  const root = (id) => {
    while (parents.get(id) !== id) id = parents.get(id);
    return id;
  };
  return [...links]
    .filter((e) => identities.has(e.from) && identities.has(e.to))
    .sort(
      (a, b) =>
        b.works.length - a.works.length ||
        b.records.length - a.records.length ||
        a.from.localeCompare(b.from) ||
        a.to.localeCompare(b.to),
    )
    .filter((e) => {
      const a = root(e.from),
        b = root(e.to);
      if (a === b) return false;
      parents.set(a, b);
      return true;
    });
}
function atlasText(parent, value, x, y, limit = 23, cls = "") {
  const text = mapSVG("text", { x, y, class: cls });
  const lines = [];
  let line = "";
  for (const word of value.split(/\s+/)) {
    if (line && (line + " " + word).length > limit) {
      lines.push(line);
      line = word;
    } else line += (line ? " " : "") + word;
  }
  if (line) lines.push(line);
  if (cls === "atlas-label" && lines.length > 3) {
    lines.splice(3);
    lines[2] += "…";
  }
  lines.forEach((value, i) => {
    const span = mapSVG("tspan", { x, dy: i ? 16 : 0 });
    span.textContent = value;
    text.append(span);
  });
  parent.append(text);
  return lines.length;
}
function renderAtlas() {
  if (!data.atlas) return;
  show("atlas");
  const atlas = data.atlas;
  $("atlas-title").textContent = data.title;
  $("atlas-intro").textContent =
    `${atlas.works.map((w) => w.title).join(" · ")}. Select a concept to compare treatments.`;
  const stats = $("atlas-stats");
  stats.replaceChildren();
  for (const [value, label] of [
    [atlas.counts.all_works, "in every work"],
    [atlas.counts.two_or_more, "in two or more"],
    [atlas.counts.concepts, "concepts in total"],
    [atlas.counts.records, "source records"],
  ]) {
    const item = el("div");
    item.append(el("strong", fmt(value)), el("span", label));
    stats.append(item);
  }
  drawAtlas();
  if (atlasSelected && atlas.concepts.some((n) => n.id === atlasSelected)) {
    selectAtlasConcept(atlasSelected, false);
    focusAtlasPoint(atlasSelected);
  } else atlasWelcome();
}
function drawAtlas() {
  const atlas = data.atlas,
    query = $("atlas-query").value.trim().toLowerCase();
  const emphasized = new Set(
    atlas.concepts
      .filter(
        (n) =>
          n.works.length >= atlasMinimum &&
          (!query ||
            [n.label, n.summary, ...n.treatments.map((t) => t.label)].some(
              (s) => s.toLowerCase().includes(query),
            )),
      )
      .map((n) => n.id),
  );
  const landmarks = $("atlas-detail-level").value === "landmarks";
  let visible = atlas.concepts.filter(
    (n) => emphasized.has(n.id) || $("atlas-context").checked,
  );
  if (landmarks && !query) {
    const degree = new Map(atlas.concepts.map((n) => [n.id, 0]));
    for (const e of atlas.links)
      for (const id of [e.from, e.to])
        degree.set(id, degree.get(id) + 1 + e.works.length / 4);
    visible = atlas.groups.flatMap((group) =>
      atlas.concepts
        .filter((n) => n.group === group.id && emphasized.has(n.id))
        .sort(
          (a, b) =>
            degree.get(b.id) - degree.get(a.id) || a.id.localeCompare(b.id),
        )
        .slice(0, 2),
    );
    if ($("atlas-context").checked)
      visible.push(
        ...atlas.concepts
          .filter((n) => !emphasized.has(n.id))
          .sort(
            (a, b) =>
              degree.get(b.id) - degree.get(a.id) || a.id.localeCompare(b.id),
          )
          .slice(0, 6),
      );
  }
  if (atlasSelected && !visible.some((n) => n.id === atlasSelected)) {
    const selected = atlas.concepts.find((n) => n.id === atlasSelected);
    if (selected) visible.push(selected);
  }
  const identities = new Set(visible.map((n) => n.id));
  const svg = $("atlas-svg");
  svg.replaceChildren();
  const width = Math.max(990, $("atlas-scroll").clientWidth),
    column = width / 3;
  const bottoms = [25, 25, 25];
  atlasPositions = new Map();
  const regions = mapSVG("g"),
    lines = mapSVG("g"),
    points = mapSVG("g");
  svg.append(regions, lines, points);
  if (landmarks) {
    const columns = 5;
    visible.forEach((node, i) =>
      atlasPositions.set(node.id, {
        x: (((i % columns) + 0.5) * width) / columns,
        y: 50 + Math.floor(i / columns) * 124,
        color:
          atlasColors[
            atlas.groups.findIndex((g) => g.id === node.group) %
              atlasColors.length
          ],
      }),
    );
    bottoms[0] = Math.ceil(visible.length / columns) * 124 + 50;
  } else
    for (const [index, group] of atlas.groups.entries()) {
      const members = visible
        .filter((n) => n.group === group.id)
        .sort((a, b) => a.label.localeCompare(b.label));
      if (!members.length) continue;
      const col = bottoms.indexOf(Math.min(...bottoms)),
        x = col * column + 18,
        y = bottoms[col];
      const height = 78 + Math.ceil(members.length / 2) * 83,
        color = atlasColors[index % atlasColors.length];
      regions.append(
        mapSVG("rect", {
          x,
          y,
          width: column - 28,
          height,
          rx: 15,
          class: "atlas-region",
        }),
      );
      const groupLabel = mapSVG("g", {
        class: "atlas-group-label",
        fill: color,
      });
      atlasText(groupLabel, group.title, x + 16, y + 24, 38);
      regions.append(groupLabel);
      members.forEach((node, i) => {
        const px = x + 22 + ((i % 2) * (column - 42)) / 2,
          py = y + 76 + Math.floor(i / 2) * 83;
        atlasPositions.set(node.id, { x: px, y: py, color });
      });
      bottoms[col] += height + 22;
    }
  const forest = atlasForest(atlas.links, identities);
  for (const edge of forest) {
    const a = atlasPositions.get(edge.from),
      b = atlasPositions.get(edge.to);
    const path = mapSVG("path", {
      d: `M ${a.x} ${a.y} Q ${(a.x + b.x) / 2 + 35} ${(a.y + b.y) / 2 - 25} ${b.x} ${b.y}`,
      class: "atlas-link",
    });
    path.dataset.from = edge.from;
    path.dataset.to = edge.to;
    lines.append(path);
  }
  for (const node of visible) {
    const p = atlasPositions.get(node.id),
      active = emphasized.has(node.id);
    const point = mapSVG("g", {
      class: "atlas-point" + (active ? "" : " context"),
      role: "button",
      tabindex: 0,
      transform: `translate(${p.x},${p.y})`,
      "aria-label": `${node.label}; ${node.works.length} works`,
      "aria-pressed": "false",
    });
    point.dataset.concept = node.id;
    const title = mapSVG("title");
    title.textContent = `${node.label} · ${node.works.length} works`;
    point.append(
      title,
      mapSVG("circle", { r: landmarks ? 20 : 12, class: "atlas-halo" }),
      mapSVG("circle", { r: active ? (landmarks ? 9 : 6) : 4, fill: p.color }),
    );
    atlasText(
      point,
      node.label,
      landmarks ? 0 : 15,
      landmarks ? 35 : 4,
      landmarks ? 25 : Math.floor((column - 75) / 13),
      "atlas-label",
    );
    if (landmarks) point.lastChild.setAttribute("text-anchor", "middle");
    point.onclick = () => selectAtlasConcept(node.id);
    point.onkeydown = (e) => {
      if (["Enter", " "].includes(e.key)) {
        e.preventDefault();
        selectAtlasConcept(node.id);
      }
    };
    points.append(point);
  }
  atlasSize = { width, height: Math.max(500, ...bottoms) };
  svg.setAttribute("viewBox", `0 0 ${width} ${atlasSize.height}`);
  resizeAtlas();
  $("atlas-map-caption").textContent =
    `${emphasized.size} concepts match · ${visible.length} ${landmarks ? "overview points" : "shown"} · Scroll or drag. Select a point to explore its source connections.`;
  if (query && !emphasized.size)
    $("atlas-map-caption").textContent =
      "No matching concepts at this coverage level. Try Every concept or a different term.";
}
function resizeAtlas() {
  $("atlas-svg").style.width = atlasSize.width * atlasScale + "px";
  $("atlas-svg").style.height = atlasSize.height * atlasScale + "px";
}
function atlasWelcome() {
  const detail = $("atlas-detail");
  detail.replaceChildren();
  detail.append(
    el("span", "HOW TO READ THE MAP", "eyebrow"),
    el("h2", "One idea. Several treatments."),
    el(
      "p",
      "Start with a few landmarks, then switch to All concepts or search for an idea. Bright points match your coverage filter; colors identify subject areas.",
    ),
    el(
      "p",
      "Select a concept to see its scope, the records supporting each book’s coverage, and all its source connections.",
    ),
    el(
      "small",
      "Overview landmarks: up to two well-connected shared concepts per subject area. This is a display selection, not a ranking of scientific importance.",
    ),
    el("h3", "What the lines mean"),
    el(
      "p",
      "Lines trace relationships between specific records in the books. The overview shows a reduced set for readability; selection reveals every neighboring connection. They do not prescribe a course sequence.",
    ),
    el("h3", "What coverage means"),
    el(
      "p",
      "A source treatment has a primary home in this inventory. Different derivations remain separate underneath. An empty book column means no primary assignment, not proven absence.",
    ),
    el("small", "Model-reviewed organization · Human audit pending"),
  );
}
async function atlasBook(project) {
  if (!atlasBooks.has(project)) {
    const entry = catalog.graphs.find((g) => g.project_id === project);
    if (!entry) throw new Error("The source graph is unavailable.");
    atlasBooks.set(
      project,
      fetch(entry.file).then((r) => {
        if (!r.ok) throw new Error("Could not load the source graph.");
        return r.json();
      }),
    );
  }
  return atlasBooks.get(project);
}
function atlasOpenRecord(project, node) {
  const graph = catalog.graphs.find((g) => g.project_id === project);
  navigateGraph(graph.id, new URLSearchParams({ node }));
}
function selectAtlasConcept(id, save = true) {
  const atlas = data.atlas,
    node = atlas.concepts.find((n) => n.id === id);
  if (!node) return;
  atlasSelected = id;
  if (!atlasPositions.has(id)) drawAtlas();
  $("atlas-svg").querySelector(".atlas-selected-links")?.remove();
  const layer = mapSVG("g", { class: "atlas-selected-links" }),
    nearby = new Set([id]);
  const links = atlas.links.filter((e) => e.from === id || e.to === id);
  for (const edge of links) {
    const a = atlasPositions.get(edge.from),
      b = atlasPositions.get(edge.to);
    nearby.add(edge.from);
    nearby.add(edge.to);
    if (!a || !b) continue;
    const path = mapSVG("path", {
      d: `M ${a.x} ${a.y} Q ${(a.x + b.x) / 2 + 25} ${(a.y + b.y) / 2 - 20} ${b.x} ${b.y}`,
      class: "atlas-link selected",
    });
    path.dataset.from = edge.from;
    path.dataset.to = edge.to;
    layer.append(path);
  }
  $("atlas-svg").insertBefore(layer, $("atlas-svg").lastChild);
  for (const point of $("atlas-svg").querySelectorAll(".atlas-point")) {
    point.classList.toggle("selected", point.dataset.concept === id);
    point.classList.toggle("unrelated", !nearby.has(point.dataset.concept));
    point.setAttribute("aria-pressed", String(point.dataset.concept === id));
  }
  const detail = $("atlas-detail");
  detail.replaceChildren();
  detail.append(
    el(
      "span",
      `${node.works.length} OF ${atlas.works.length} WORKS`,
      "eyebrow",
    ),
    el("h2", node.label),
    el("p", node.summary),
  );
  const clear = el("button", "Clear selection");
  clear.onclick = () => {
    atlasSelected = null;
    drawAtlas();
    atlasWelcome();
    saveURL();
  };
  detail.append(clear);
  detail.append(el("h3", "Book treatments"));
  for (const project of data.atlas.works.flatMap((w) => w.projects)) {
    const treatments = node.treatments.filter((t) => t.project === project);
    const count = node.independent_book_counts[project] || 0;
    const section = el("details", undefined, "atlas-treatments");
    section.append(
      el(
        "summary",
        `${bookTitle(project)} · ${count || "no"} primary ${count === 1 ? "record" : "records"}`,
      ),
    );
    for (const treatment of treatments) {
      const button = el(
        "button",
        treatment.label +
          (treatment.independent_coverage
            ? " ↗"
            : " · imported prerequisite ↗"),
      );
      button.onclick = () => atlasOpenRecord(project, treatment.node);
      section.append(button);
    }
    if (!treatments.length)
      section.append(
        el(
          "p",
          "No primary assignment in this inventory; this is not a claim of absence from the book.",
        ),
      );
    detail.append(section);
  }
  detail.append(
    el("h3", `${links.length} connected concepts`),
    el(
      "p",
      "Each connection below opens the specific recorded relationship. Its direction and qualifications belong to that source treatment.",
    ),
  );
  for (const edge of [...links].sort(
    (a, b) =>
      b.works.length - a.works.length || b.records.length - a.records.length,
  )) {
    const other = atlas.concepts.find(
      (n) => n.id === (edge.from === id ? edge.to : edge.from),
    );
    const row = el("div", undefined, "atlas-neighbor"),
      button = el("button", other.label);
    button.onclick = () => {
      selectAtlasConcept(other.id);
      focusAtlasPoint(other.id);
    };
    const evidence = el(
      "button",
      `${edge.records.length} source links · ${edge.works.length} works ↗`,
      "atlas-evidence-button",
    );
    evidence.onclick = () =>
      showAtlasConnection(edge, node, other).catch((e) => say(e.message));
    row.append(button, evidence);
    detail.append(row);
  }
  detail.append(
    el(
      "small",
      `${node.internal_relationships} additional source relationships stay within this concept’s treatments.`,
    ),
  );
  detail.scrollTop = 0;
  if (save) saveURL();
}
function focusAtlasPoint(id) {
  const p = atlasPositions.get(id);
  if (!p) return;
  $("atlas-scroll").scrollTo({
    left: Math.max(0, p.x * atlasScale - $("atlas-scroll").clientWidth / 2),
    top: Math.max(0, p.y * atlasScale - 180),
    behavior: "smooth",
  });
}
async function showAtlasConnection(link, from, to) {
  const sourceData = await Promise.all(
    [...new Set(link.records.map((r) => r.project))].map(async (p) => [
      p,
      await atlasBook(p),
    ]),
  );
  if (mode !== "atlas" || !data.atlas) return;
  const sources = new Map(sourceData),
    detail = $("atlas-detail");
  detail.replaceChildren();
  const back = el("button", "← " + from.label);
  back.onclick = () => selectAtlasConcept(from.id);
  detail.append(
    back,
    el("h2", from.label + " ↔ " + to.label),
    el("p", data.atlas.connection_meaning),
  );
  for (const record of link.records) {
    const book = sources.get(record.project),
      edge = book.knowledge.edges.find((e) => e.id === record.edge),
      get = (id) => book.knowledge.nodes.find((n) => n.id === id);
    const section = el("details", undefined, "atlas-treatments");
    section.append(
      el(
        "summary",
        `${bookTitle(record.project)} · ${human(edge.relation)} · ${edge.necessity}`,
      ),
      el("p", get(edge.from).label + " → " + get(edge.to).label),
      el("p", edge.rationale),
    );
    if (edge.failure_mode) section.append(el("p", edge.failure_mode));
    for (const ev of edge.evidence)
      section.append(
        el("small", `${ev.source}, ${ev.section}, pp. ${ev.pages.join(", ")}`),
      );
    const inspect = el("button", "Open the target record and its inputs ↗");
    inspect.onclick = () => atlasOpenRecord(record.project, edge.to);
    section.append(inspect);
    detail.append(section);
  }
  detail.scrollTop = 0;
}
function atlasComparison() {
  const atlas = data.atlas,
    detail = $("atlas-detail");
  detail.replaceChildren();
  detail.append(
    el("span", "CONCEPT COVERAGE", "eyebrow"),
    el("h2", "Compare the books"),
    el("p", atlas.coverage_meaning),
  );
  const units = atlas.works.flatMap((w) =>
    w.projects.map((p) => ({ id: p, title: bookTitle(p) })),
  );
  for (let i = 0; i < units.length; i++)
    for (let j = i + 1; j < units.length; j++) {
      const pair = [units[i], units[j]],
        matches = atlas.concepts.filter((n) =>
          pair.every((b) => n.independent_book_counts[b.id]),
        );
      const block = el("details", undefined, "atlas-treatments");
      block.append(
        el(
          "summary",
          `${pair.map((b) => b.title).join(" × ")}: ${matches.length} concepts`,
        ),
      );
      for (const n of matches) {
        const b = el("button", n.label);
        b.onclick = () => {
          selectAtlasConcept(n.id);
          focusAtlasPoint(n.id);
        };
        block.append(b);
      }
      detail.append(block);
    }
  detail.append(
    el(
      "p",
      "The headline combines explicitly grouped volumes into works. This comparison keeps every volume separate.",
    ),
  );
}
function bindAtlasControls() {
  $("atlas-tab").onclick = () => {
    renderAtlas();
    saveURL();
  };
  for (const id of [
    "atlas-detail-level",
    "atlas-coverage",
    "atlas-context",
    "atlas-query",
  ])
    $(id).oninput = () => {
      atlasMinimum = Number($("atlas-coverage").value);
      atlasSelected = null;
      drawAtlas();
      atlasWelcome();
      saveURL(true);
      if ($("atlas-query").value) {
        const first = $("atlas-svg").querySelector(
          ".atlas-point:not(.context)",
        );
        if (first) focusAtlasPoint(first.dataset.concept);
      }
    };
  $("atlas-compare").onclick = atlasComparison;
  for (const [id, delta] of [
    ["in", 0.15],
    ["out", -0.15],
    ["reset", 0],
  ])
    $(id === "reset" ? "atlas-reset" : "atlas-zoom-" + id).onclick = () => {
      atlasScale = delta ? Math.max(0.65, Math.min(2, atlasScale + delta)) : 1;
      resizeAtlas();
      if (!delta) $("atlas-scroll").scrollTo(0, 0);
    };
  const scroll = $("atlas-scroll");
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
  scroll.onkeydown = (e) => {
    if (e.target !== scroll) return;
    const offset = {
      ArrowDown: [0, 70],
      ArrowUp: [0, -70],
      ArrowRight: [70, 0],
      ArrowLeft: [-70, 0],
    }[e.key];
    if (offset) {
      e.preventDefault();
      scroll.scrollBy(...offset);
    }
  };
}
