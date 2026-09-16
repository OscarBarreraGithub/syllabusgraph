/* A scrollable introduction. Every count comes from the selected public graph. */
"use strict";
function overviewCore() {
  if (!hasCore()) return null;
  const perspectives = data.backbone.perspectives;
  const scope = perspectives.textbooks.levels.length
    ? perspectives.textbooks
    : perspectives.volumes;
  return { scope, level: scope.levels.at(-1) };
}
function renderOverview() {
  show("overview");
  const core = overviewCore();
  const bookIDs = core
    ? new Set(core.scope.units.flatMap((u) => u.projects))
    : new Set([data.project_id]);
  const books = catalog.graphs.filter((g) => bookIDs.has(g.project_id));
  $("overview-eyebrow").textContent = data.title.toLocaleUpperCase();
  $("overview-title").textContent = core
    ? "What do these books have in common?"
    : nodes.length
      ? "Get to know this graph."
      : "Your map of ideas starts here.";
  $("overview-intro").textContent = core
    ? `${books.length} textbook graphs, connected in one shared map. Explore the ideas they share, follow their prerequisites, and look at the evidence behind each connection.`
    : nodes.length
      ? `Explore ${fmt(nodes.length)} concepts and ${fmt(edges.length)} recorded relationships. Start with the concept index or search for an idea, then follow its connections back to the sources.`
      : "Bring your material and work with your coding agent to build a source-backed knowledge graph. The guide walks you through setup, scope, extraction, and independent review.";
  $("overview-explore").textContent = core
    ? "Explore the shared backbone →"
    : nodes.length
      ? "Explore the concepts →"
      : "Get set up →";
  $("overview-explore").onclick = () => {
    if (core) {
      prepareCore(new URLSearchParams());
      renderCore();
      saveURL();
    } else if (nodes.length) {
      show("browse");
      saveURL();
    } else $("about-dialog").showModal();
  };
  $("overview-all").hidden = !nodes.length;
  $("overview-all").textContent = `Browse all ${fmt(nodes.length)} concepts`;
  $("overview-caption").textContent = core
    ? `The starting view compares ${core.scope.units.map((u) => u.title).join(", ")}. Course design comes later.`
    : "This is a knowledge map. Course design is a separate step.";
  const bookList = $("diagram-books");
  bookList.replaceChildren();
  for (const book of books) {
    const row = el("div", undefined, "diagram-book");
    row.append(
      el("span", book.title),
      el("small", `${fmt(book.nodes)} concepts`),
    );
    bookList.append(row);
  }
  $("diagram-label").textContent = core
    ? `${books.length} BOOK GRAPHS → ONE SHARED MAP`
    : "YOUR KNOWLEDGE GRAPH";
  $("diagram-shared-title").textContent = core
    ? "Shared knowledge graph"
    : "Knowledge graph";
  $("diagram-shared-count").textContent = `${fmt(nodes.length)} concepts`;
  $("diagram-shared-note").textContent =
    `${fmt(edges.length)} recorded relationships`;
  $("diagram-core-wrap").hidden = !core;
  if (core) {
    $("diagram-core-count").textContent =
      `${fmt(core.level.nodes.length)} concepts in common`;
    $("diagram-core-note").textContent =
      `Independently treated in all ${core.scope.units.length} compared textbooks`;
  }
  const facts = $("overview-facts");
  facts.replaceChildren();
  const values = core
    ? [
        [
          fmt(core.level.nodes.length),
          "Concepts in the common backbone",
          `Matched across all ${core.scope.units.length} textbooks`,
        ],
        [
          fmt(core.level.edges.length),
          "Connections between those concepts",
          `${core.level.relations.prerequisite || 0} prerequisite relations`,
        ],
        [
          fmt(core.level.components.length),
          "Separate connected pieces",
          `The largest contains ${core.level.components[0]?.nodes.length || 0} concepts`,
        ],
        [
          fmt(nodes.length),
          "Concepts in the full shared graph",
          "The whole collection remains searchable",
        ],
      ]
    : [
        [fmt(nodes.length), "Concepts", "Each retains its source evidence"],
        [fmt(edges.length), "Connections", "Follow the recorded relationships"],
      ];
  for (const [value, title, caption] of values) {
    const stat = el("div", undefined, "overview-fact");
    stat.append(el("strong", value), el("span", title), el("small", caption));
    facts.append(stat);
  }
  $("overview-structure").textContent = core
    ? `The common backbone is a subset of the shared graph. It has ${core.level.components.length} separate connected pieces, rather than one continuous chain. Some paths run through ideas outside this overlap. Connections keep their source-specific evidence; their presence does not mean every book asserts the same relationship.`
    : "Concepts and relationships retain their evidence. The index helps you find an idea; its neighborhood shows where that idea fits.";
  $("overview-wider").hidden = !core || core.scope.units.length <= 2;
  if (core && core.scope.units.length > 2) {
    $("overview-wider").textContent =
      `See the wider overlap (${core.scope.levels[0].nodes.length} concepts) →`;
    $("overview-wider").onclick = () => {
      prepareCore(new URLSearchParams());
      coreMinimum = 2;
      renderCore();
      saveURL();
    };
  }
  document.querySelector(".reading-guide article:first-child h3").textContent =
    core ? "Start with the overlap" : "Find a concept";
  document.querySelector(".reading-guide article:first-child p").textContent =
    core
      ? "Each card is a concept. The common backbone keeps ideas independently treated in every compared textbook. Widen the overlap to include ideas shared by fewer books."
      : "Open the index to browse concepts, or use search to find an idea by name. You can explore a knowledge graph before deciding how to teach it.";
  $("overview-books-heading").textContent = core
    ? "The individual book graphs."
    : "Explore this graph.";
  $("overview-books-caption").textContent = core
    ? "Each book keeps its own concepts, qualifications, and source references. The shared graph records how those treatments connect."
    : "The concept index and source references remain available alongside the graph.";
  const library = $("overview-books");
  library.replaceChildren();
  for (const book of books) {
    const card = el("button", undefined, "overview-book");
    card.append(
      el(
        "span",
        book.kind === "textbook" ? "BOOK GRAPH" : "KNOWLEDGE GRAPH",
        "eyebrow",
      ),
      el("strong", book.title),
      el(
        "span",
        `${fmt(book.nodes)} concepts · ${fmt(book.edges)} connections`,
      ),
      el("small", "Open the concept index →"),
    );
    card.onclick = () =>
      navigateGraph(book.id, new URLSearchParams({ view: "browse" }));
    library.append(card);
  }
  $("overview-review").textContent = $("review-status").textContent;
}
function bindOverviewControls() {
  $("overview-tab").onclick = () => {
    renderOverview();
    saveURL();
  };
  $("overview-all").onclick = () => $("all-concepts").click();
  $("overview-setup").onclick = () => $("about-dialog").showModal();
}
