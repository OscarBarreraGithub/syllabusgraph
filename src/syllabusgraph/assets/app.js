"use strict";

const $ = (id) => document.getElementById(id);
const esc = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
const clone = (value) => structuredClone(value);
const token = document.querySelector(
  'meta[name="syllabusgraph-token"]',
).content;
const state = {
  project: null,
  draft: null,
  result: null,
  selected: null,
  view: "course",
  dirty: false,
  filter: "all",
  request: 0,
  editVersion: 0,
  uploadSource: null,
};
let previewTimer, toastTimer;

async function api(path, data, options = {}) {
  const response = await fetch(
    path,
    data === undefined
      ? undefined
      : {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-SyllabusGraph-Token": token,
            ...options.headers,
          },
          body: options.raw ? data : JSON.stringify(data),
        },
  );
  if (!response.ok) {
    let message = "The request did not complete.";
    try {
      message = (await response.json()).error || message;
    } catch {}
    throw new Error(message);
  }
  return options.text ? response.text() : response.json();
}

function fail(error) {
  $("global-error").textContent = error.message || String(error);
  $("global-error").hidden = false;
}
function clearError() {
  $("global-error").hidden = true;
}
function toast(message) {
  $("toast").textContent = message;
  $("toast").hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => ($("toast").hidden = true), 4000);
}
function nodes() {
  return Object.fromEntries(
    state.project.knowledge.nodes.map((n) => [n.id, n]),
  );
}
function targets() {
  return new Set([
    ...state.draft.outcomes.map((o) => o.node),
    ...Object.keys(state.draft.include || {}),
  ]);
}
function levelFor(id) {
  return (
    state.draft.outcomes.find((o) => o.node === id)?.level ||
    state.draft.include?.[id] ||
    state.result?.levels[id] ||
    state.project.config.mastery_levels[
      Math.min(1, state.project.config.mastery_levels.length - 1)
    ]
  );
}
function dirty() {
  state.request++;
  state.editVersion++;
  state.dirty = true;
  $("save-state").textContent = "Unsaved changes";
  $("save").disabled = false;
  clearTimeout(previewTimer);
  previewTimer = setTimeout(() => preview().catch(fail), 160);
}

async function load(keepDraft = false) {
  const data = await api("/api/project");
  const selected = state.draft?.id;
  state.project = data;
  document.title = `${data.config.title} · SyllabusGraph`;
  $("project-title").textContent = data.config.title;
  $("project-description").textContent = data.config.description;
  $("source-count").textContent = data.sources.length;
  $("concept-count").textContent = data.knowledge.nodes.length;
  $("content-version").textContent = `Content ${data.digest.slice(7, 15)}`;
  $("plan-select").innerHTML = Object.values(data.plans)
    .map((p) => `<option value="${esc(p.id)}">${esc(p.title)}</option>`)
    .join("");
  renderSources();
  renderWorkflow();
  if (!Object.keys(data.plans).length) {
    throw new Error(
      "Create a course plan in the project's plans directory to begin.",
    );
  }
  if (!keepDraft || !state.draft) {
    state.draft = clone(data.plans[selected] || Object.values(data.plans)[0]);
    state.dirty = false;
    state.selected = state.draft.outcomes[0]?.node || null;
  }
  $("plan-select").value = state.draft.id;
  $("save-state").textContent = state.dirty
    ? "Unsaved changes"
    : "All changes saved";
  $("save").disabled = !state.dirty;
  $("sessions").value = state.draft.sessions;
  $("minutes").value = state.draft.minutes_per_session;
  await preview();
}

async function preview() {
  clearError();
  const request = ++state.request;
  const result = await api("/api/preview", { plan: state.draft });
  if (request !== state.request) return;
  state.result = result;
  $("course-title").textContent = state.draft.title;
  $("export").disabled = false;
  renderConcepts();
  renderCourse();
  renderDetail();
  renderGraph();
}

function renderConcepts() {
  const picked = targets();
  const query = $("search").value.toLocaleLowerCase().trim();
  const available = state.project.knowledge.nodes.filter(
    (n) =>
      (state.filter !== "picked" || picked.has(n.id)) &&
      (!query ||
        `${n.label} ${n.summary} ${n.id}`.toLocaleLowerCase().includes(query)),
  );
  if (!state.project.knowledge.nodes.length) {
    $("concept-list").innerHTML =
      '<div class="empty"><h3>Start with your sources.</h3><p>Your reviewed concepts will appear here after extraction and review.</p><button class="button" data-go="sources">Open references</button></div>';
    return;
  }
  if (!available.length) {
    $("concept-list").innerHTML =
      '<p class="muted small">No concepts match this view.</p>';
    return;
  }
  const groups = [
    ...state.project.knowledge.groups,
    { id: "", title: "Other concepts" },
  ];
  $("concept-list").innerHTML = groups
    .map((g) => {
      const members = available.filter((n) => (n.group || "") === g.id);
      if (!members.length) return "";
      return (
        `<p class="group-label">${esc(g.title)}</p>` +
        members
          .map(
            (n) =>
              `<div class="concept-row"><button class="pick ${picked.has(n.id) ? "selected" : ""}" data-pick="${esc(n.id)}" aria-label="${picked.has(n.id) ? "Remove" : "Add"} ${esc(n.label)} ${picked.has(n.id) ? "from" : "to"} learning goals" aria-pressed="${picked.has(n.id)}">${picked.has(n.id) ? "✓" : ""}</button><button class="concept-name" data-detail="${esc(n.id)}">${esc(n.label)}</button>${state.result.roles[n.id] === "supporting" ? '<span class="support-mark" title="Supporting concept"></span>' : ""}</div>`,
          )
          .join("")
      );
    })
    .join("");
}

function renderCourse() {
  const result = state.result,
    data = nodes(),
    s = result.stats;
  const stats = [
    [s.targets, "Learning goals"],
    [s.supporting, "Supporting concepts"],
    [s.assumed, "Background used"],
    [
      s.unestimated ? "—" : `${Math.round(s.estimated_min)}`,
      s.unestimated
        ? `${s.unestimated} treatments unestimated`
        : `to ${Math.round(s.estimated_max)} min · estimated`,
    ],
  ];
  $("stats").innerHTML = stats
    .map(
      ([value, label]) =>
        `<div class="stat"><strong>${esc(value)}</strong><span>${esc(label)}</span></div>`,
    )
    .join("");
  $("sessions-list").innerHTML = result.sessions.length
    ? result.sessions
        .map((session) => {
          const m = session.minutes;
          const time = m.unestimated.length
            ? "Timing incomplete"
            : `${Math.round(m.min)}–${Math.round(m.max)} min`;
          return `<article class="session-card"><div class="session-number">${String(session.number).padStart(2, "0")}</div><div><div class="session-top"><h3>${esc(session.title)}</h3><span class="time ${session.timing}">${time}</span></div><div class="session-concepts">${session.nodes.map((id) => `<button class="topic-pill ${result.roles[id]}" data-detail="${esc(id)}">${esc(data[id].label)}<span>${esc(result.levels[id])}</span></button>`).join("")}</div></div></article>`;
        })
        .join("")
    : `<div class="empty"><h3>${state.project.knowledge.nodes.length ? "What should students be able to do?" : "Your course starts with a reference."}</h3><p>${state.project.knowledge.nodes.length ? "Select a goal from the concept library. Its prerequisites and a suggested session sequence will appear here." : "Attach the source material, define a manageable extraction scope, and review the resulting concepts before building a course."}</p>${state.project.knowledge.nodes.length ? "" : '<button class="button primary" data-go="sources">Attach your references</button>'}</div>`;
  $("issues").innerHTML =
    result.issues
      .filter((i) => i.code !== "empty")
      .map((i) => `<div class="issue ${i.severity}">${esc(i.message)}</div>`)
      .join("") +
    (s.unused_sessions && result.sessions.length
      ? `<p class="muted small">${s.unused_sessions} session slots remain available for practice, assessment, or further topics.</p>`
      : "");
}

function renderDetail() {
  if (!state.selected) return;
  const data = nodes(),
    node = data[state.selected];
  if (!node) return;
  const picked = targets().has(node.id),
    level = levelFor(node.id),
    result = state.result;
  const sourceLookup = Object.fromEntries(
    state.project.sources.map((s) => [s.id, s]),
  );
  const estimate = node.estimates?.[level];
  const incoming = state.project.knowledge.edges.filter(
    (e) => e.to === node.id,
  );
  const motivations = state.project.knowledge.motivations.filter((m) =>
    m.nodes.includes(node.id),
  );
  const outcome = state.draft.outcomes.find((o) => o.node === node.id);
  const omitted = state.draft.omit?.includes(node.id);
  $("detail").innerHTML =
    `<p class="eyebrow">03 / UNDERSTAND</p><h2>${esc(node.label)}</h2><p class="panel-copy">${esc(node.summary)}</p><div class="detail-actions"><button class="button ${picked ? "" : "primary"}" data-pick="${esc(node.id)}">${picked ? "Remove goal" : "Add as a goal"}</button>${result.roles[node.id] === "supporting" || omitted ? `<button class="button" data-omit="${esc(node.id)}">${omitted ? "Restore topic" : "Exclude topic"}</button>` : ""}</div><div class="detail-section"><h3>Treatment depth</h3><select id="detail-level" aria-label="Treatment depth">${state.project.config.mastery_levels.map((l) => `<option value="${esc(l)}" ${l === level ? "selected" : ""}>${esc(l)}</option>`).join("")}</select><p>${estimate ? `${estimate.min}–${estimate.max} min · ${esc(estimate.basis)}` : "No time estimate at this depth. Add one to the concept record when you have a teaching plan."}</p></div>${picked ? `<div class="detail-section"><h3>Evidence of learning</h3><textarea id="assessment" aria-label="Assessment for this learning outcome" placeholder="How will students demonstrate this?">${esc(outcome?.assessment || "")}</textarea></div>` : ""}${motivations.length ? `<div class="detail-section"><h3>Why teach it?</h3>${motivations.map((m) => `<p>${esc(m.summary)}</p>`).join("")}</div>` : ""}<div class="detail-section"><h3>Source evidence</h3>${node.evidence.map((ref) => `<div class="evidence-card"><strong>${esc(sourceLookup[ref.source]?.title || ref.source)}</strong><span>${esc(ref.section)} · p. ${ref.pages.join(", ")}</span>${ref.note ? `<p>${esc(ref.note)}</p>` : ""}</div>`).join("")}</div><div class="detail-section"><h3>Dependencies and other relationships</h3>${incoming.length ? incoming.map((e) => `<p><button class="concept-name" data-detail="${esc(e.from)}">${esc(data[e.from].label)}</button><br><span class="muted">${esc(e.relation)} · ${esc(e.source_level)} → ${esc(e.target_level)}</span><br>${esc(e.failure_mode)}</p>`).join("") : '<p class="muted">No incoming relationships recorded.</p>'}</div>`;
  $("detail-level").addEventListener("change", (event) => {
    const newLevel = event.target.value;
    if (outcome) outcome.level = newLevel;
    else if (picked) {
      state.draft.include ||= {};
      state.draft.include[node.id] = newLevel;
    } else {
      state.draft.treatments ||= {};
      state.draft.treatments[node.id] = newLevel;
    }
    dirty();
  });
  $("assessment")?.addEventListener("change", (event) => {
    const text = event.target.value.trim();
    state.draft.outcomes = state.draft.outcomes.filter(
      (o) => o.node !== node.id,
    );
    state.draft.include ||= {};
    if (text) {
      state.draft.outcomes.push({
        node: node.id,
        level: levelFor(node.id),
        assessment: text,
      });
      delete state.draft.include[node.id];
    } else state.draft.include[node.id] = levelFor(node.id);
    dirty();
  });
}

function renderGraph() {
  if (!state.result) return;
  const svg = $("graph"),
    graph = state.result.layout,
    data = nodes();
  svg.setAttribute("width", Math.max(graph.width, 650));
  svg.setAttribute("height", Math.max(graph.height, 330));
  const positions = Object.fromEntries(graph.nodes.map((n) => [n.id, n]));
  const edges = graph.edges
    .map(([from, to]) => {
      const a = positions[from],
        b = positions[to],
        x1 = a.x + 200,
        y1 = a.y + 24,
        x2 = b.x,
        y2 = b.y + 24;
      return `<path class="graph-edge" d="M${x1},${y1} C${x1 + 35},${y1} ${x2 - 35},${y2} ${x2},${y2}" marker-end="url(#arrow)"/>`;
    })
    .join("");
  const rows = graph.nodes
    .map((n) => {
      const label = data[n.id].label;
      const words = label.split(" ");
      let lines = [""];
      for (const word of words) {
        if ((lines.at(-1) + " " + word).trim().length > 25 && lines.at(-1))
          lines.push(word);
        else lines[lines.length - 1] = (lines.at(-1) + " " + word).trim();
      }
      if (lines.length > 2)
        lines = [lines[0], lines.slice(1).join(" ").slice(0, 24) + "…"];
      return `<g class="graph-node ${state.result.roles[n.id]}" transform="translate(${n.x},${n.y})" data-graph-detail="${esc(n.id)}" tabindex="0" role="button" aria-label="Inspect ${esc(label)}"><title>${esc(label)}</title><rect width="200" height="50" rx="8"/>${lines.map((line, i) => `<text x="12" y="${lines.length === 1 ? 29 : 21 + i * 16}">${esc(line)}</text>`).join("")}</g>`;
    })
    .join("");
  svg.innerHTML =
    '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#b0c1a5"/></marker></defs>' +
    edges +
    rows;
  $("graph-caption").textContent = graph.nodes.length
    ? `${graph.nodes.length} taught concepts. Implied edges are hidden; alternate derivations and evidential links are available in concept details.`
    : "Choose learning goals to build a prerequisite map.";
}

function renderSources() {
  $("source-list").innerHTML = state.project.sources.length
    ? state.project.sources
        .map(
          (source, i) =>
            `<article class="source-card"><div class="reference-no">${String(i + 1).padStart(2, "0")}</div><h3>${esc(source.title)}${source.volume ? ` · ${esc(source.volume)}` : ""}</h3><p>${esc(source.authors.join(", "))}</p><p class="small">${esc(source.edition || "")}</p><div class="source-bottom"><span class="status-pill ${source.local_status}">${source.local_status === "registered" ? `${source.page_count} pages attached` : source.local_status === "included" ? "Included source" : "Awaiting material"}</span>${source.local_status === "awaiting_upload" ? `<button class="button" data-upload="${esc(source.id)}">Attach file</button>` : ""}</div></article>`,
        )
        .join("")
    : '<div class="empty"><h3>What will your course draw from?</h3><p>Add a textbook, a set of notes, or another reference. You can attach its material locally after creating its entry.</p></div>';
  $("prepare-source").innerHTML = state.project.sources
    .map(
      (s) =>
        `<option value="${esc(s.id)}">${esc(s.title)}${s.volume ? ` · ${esc(s.volume)}` : ""}</option>`,
    )
    .join("");
}

function renderWorkflow() {
  $("unit-list").innerHTML = state.project.workflow.units.length
    ? state.project.workflow.units
        .map(
          (u) =>
            `<div class="unit"><strong>${esc(u.unit)}</strong><span class="status-pill ${esc(u.status)}">${esc(u.status)}${u.retryable_failure ? " · last attempt needs attention" : ""}</span></div>`,
        )
        .join("")
    : '<div class="empty"><h3>A small page range is a good beginning.</h3><p>Attach a reference, then prepare a source unit. Your progress will be recorded here as you extract and review it.</p></div>';
}

function view(name) {
  state.view = name;
  document
    .querySelectorAll(".view")
    .forEach((el) => (el.hidden = el.id !== `view-${name}`));
  document.querySelectorAll(".tab").forEach((el) => {
    el.classList.toggle("active", el.dataset.view === name);
    el.setAttribute("aria-selected", el.dataset.view === name);
  });
}

function pick(id) {
  if (targets().has(id)) {
    state.draft.outcomes = state.draft.outcomes.filter((o) => o.node !== id);
    delete state.draft.include?.[id];
  } else {
    state.draft.include ||= {};
    state.draft.include[id] = levelFor(id);
    state.draft.omit = (state.draft.omit || []).filter((n) => n !== id);
  }
  state.selected = id;
  dirty();
}

document.addEventListener("click", (event) => {
  const button = event.target.closest(
    "[data-pick],[data-detail],[data-go],[data-view],[data-close],[data-upload],[data-omit],[data-graph-detail]",
  );
  if (!button) return;
  if (button.dataset.pick) pick(button.dataset.pick);
  if (button.dataset.detail) {
    state.selected = button.dataset.detail;
    renderDetail();
  }
  if (button.dataset.go || button.dataset.view)
    view(button.dataset.go || button.dataset.view);
  if (button.dataset.close) $(button.dataset.close).close();
  if (button.dataset.graphDetail) {
    state.selected = button.dataset.graphDetail;
    view("course");
    renderDetail();
    $("detail").scrollIntoView({ block: "nearest" });
  }
  if (button.dataset.omit) {
    const id = button.dataset.omit;
    state.draft.omit ||= [];
    state.draft.omit = state.draft.omit.includes(id)
      ? state.draft.omit.filter((n) => n !== id)
      : [...state.draft.omit, id];
    dirty();
  }
  if (button.dataset.upload) {
    state.uploadSource = button.dataset.upload;
    $("upload-source-title").textContent = state.project.sources.find(
      (s) => s.id === state.uploadSource,
    ).title;
    $("upload-dialog").showModal();
  }
});
document.addEventListener("keydown", (event) => {
  if (
    (event.key === "Enter" || event.key === " ") &&
    event.target.dataset.graphDetail
  ) {
    event.preventDefault();
    event.target.dispatchEvent(new MouseEvent("click", { bubbles: true }));
  }
});
$("search").addEventListener("input", renderConcepts);
for (const filter of ["all", "picked"])
  $("filter-" + filter).addEventListener("click", () => {
    state.filter = filter;
    $("filter-all").classList.toggle("active", filter === "all");
    $("filter-picked").classList.toggle("active", filter === "picked");
    renderConcepts();
  });
$("plan-select").addEventListener("change", async (event) => {
  if (
    state.dirty &&
    !window.confirm("Switch courses and discard unsaved changes?")
  ) {
    event.target.value = state.draft.id;
    return;
  }
  state.draft = clone(state.project.plans[event.target.value]);
  state.selected = state.draft.outcomes[0]?.node || null;
  state.dirty = false;
  $("save").disabled = true;
  $("save-state").textContent = "All changes saved";
  $("sessions").value = state.draft.sessions;
  $("minutes").value = state.draft.minutes_per_session;
  try {
    await preview();
  } catch (error) {
    fail(error);
  }
});
for (const [id, field] of [
  ["sessions", "sessions"],
  ["minutes", "minutes_per_session"],
])
  $(id).addEventListener("change", (event) => {
    if (!event.target.checkValidity()) {
      event.target.reportValidity();
      return;
    }
    state.draft[field] = Number(event.target.value);
    dirty();
  });
$("save").addEventListener("click", async () => {
  try {
    clearTimeout(previewTimer);
    clearError();
    const snapshot = clone(state.draft),
      version = state.editVersion;
    $("save").disabled = true;
    const saved = await api("/api/save", {
      plan: snapshot,
      expected_digest: state.project.digest,
    });
    state.project.digest = saved.digest;
    state.project.plans[snapshot.id] = snapshot;
    state.dirty = state.editVersion !== version;
    $("save").disabled = !state.dirty;
    $("save-state").textContent = state.dirty
      ? "Unsaved changes"
      : "All changes saved";
    toast(
      state.dirty
        ? "Earlier revision saved; your latest edits are still unsaved."
        : "Course saved in your project.",
    );
    await preview();
  } catch (error) {
    $("save").disabled = false;
    fail(error);
  }
});
$("export").addEventListener("click", async () => {
  try {
    const format = $("export-format").value;
    const text = await api(
      "/api/export",
      { plan: state.draft, format },
      { text: true },
    );
    const link = document.createElement("a");
    link.href = URL.createObjectURL(
      new Blob([text], { type: "text/plain;charset=utf-8" }),
    );
    link.download = `${state.draft.id}-${format}.${format === "json" ? "json" : format === "mermaid" ? "mmd" : "md"}`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(link.href), 1000);
    toast("Exported the course currently on screen.");
  } catch (error) {
    fail(error);
  }
});
$("background-open").addEventListener("click", () => {
  const inherited = {},
    levels = state.project.config.mastery_levels;
  for (const prior of state.draft.prior_plans || [])
    for (const outcome of state.project.plans[prior]?.outcomes || []) {
      if (
        !inherited[outcome.node] ||
        levels.indexOf(outcome.level) > levels.indexOf(inherited[outcome.node])
      )
        inherited[outcome.node] = outcome.level;
    }
  $("background-list").innerHTML =
    state.project.knowledge.nodes
      .map((n) => {
        const fromPrior = inherited[n.id],
          explicit = state.draft.background[n.id],
          unknown = state.draft.unknown?.includes(n.id);
        return `<div class="background-row"><span>${esc(n.label)}</span><select data-background="${esc(n.id)}" data-inherited="${fromPrior ? "yes" : ""}" aria-label="Background level for ${esc(n.label)}"><option value="" ${unknown || (!fromPrior && !explicit) ? "selected" : ""}>Not assumed</option>${fromPrior ? `<option value="@inherit" ${!explicit && !unknown ? "selected" : ""}>Prior course: ${esc(fromPrior)}</option>` : ""}${state.project.config.mastery_levels.map((l) => `<option value="${esc(l)}" ${explicit === l && !unknown ? "selected" : ""}>${esc(l)}</option>`).join("")}</select></div>`;
      })
      .join("") ||
    '<p class="muted">Background choices become available when the knowledge base has concepts.</p>';
  $("background-dialog").showModal();
});
$("background-form").addEventListener("submit", (event) => {
  event.preventDefault();
  state.draft.background = {};
  state.draft.unknown = [];
  document.querySelectorAll("[data-background]").forEach((el) => {
    if (el.value && el.value !== "@inherit")
      state.draft.background[el.dataset.background] = el.value;
    else if (!el.value && el.dataset.inherited)
      state.draft.unknown.push(el.dataset.background);
  });
  $("background-dialog").close();
  dirty();
});
$("add-reference").addEventListener("click", () =>
  $("source-dialog").showModal(),
);
$("source-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = new FormData(event.target);
  const source = {
    id: data.get("id"),
    title: data.get("title"),
    authors: data
      .get("authors")
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean),
    status: "expected",
  };
  if (data.get("edition")) source.edition = data.get("edition");
  try {
    await api("/api/source", { source });
    $("source-dialog").close();
    event.target.reset();
    await load(true);
    toast("Reference added. Attach its material when ready.");
  } catch (error) {
    $("source-dialog").close();
    fail(error);
  }
});
$("upload-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = new FormData(event.target),
    file = data.get("file");
  $("upload-submit").disabled = true;
  $("upload-submit").textContent = "Reading pages…";
  try {
    await api(`/api/upload/${state.uploadSource}`, await file.arrayBuffer(), {
      raw: true,
      headers: {
        "Content-Type": "application/octet-stream",
        "X-Filename": encodeURIComponent(file.name),
        "X-Page-Offset": data.get("offset"),
      },
    });
    $("upload-dialog").close();
    event.target.reset();
    await load(true);
    toast("Source attached locally. Ready to prepare a page range.");
  } catch (error) {
    $("upload-dialog").close();
    fail(error);
  } finally {
    $("upload-submit").disabled = false;
    $("upload-submit").textContent = "Attach locally";
  }
});
$("prepare-open").addEventListener("click", () => {
  if (!state.project.sources.length) {
    view("sources");
    toast("Add a reference first.");
    return;
  }
  $("prepare-dialog").showModal();
});
$("prepare-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = new FormData(event.target);
  try {
    await api("/api/prepare", {
      unit: data.get("unit"),
      source: data.get("source"),
      first: Number(data.get("first")),
      last: Number(data.get("last")),
      scope: data.get("scope"),
    });
    $("prepare-dialog").close();
    await load(true);
    toast("Source packet prepared. Continue with the extraction workflow.");
  } catch (error) {
    $("prepare-dialog").close();
    fail(error);
  }
});
window.addEventListener("beforeunload", (event) => {
  if (state.dirty) {
    event.preventDefault();
    event.returnValue = "";
  }
});
load().catch(fail);
