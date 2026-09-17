/* A scrollable introduction. Every count comes from the selected public graph. */
"use strict";
function renderHome() {
  show("home");
  $("home-demo-title").textContent = `${data.title}: a worked example.`;
  $("home-demo-caption").textContent =
    `${fmt(nodes.length)} graph records with source references. Explore the included collection, then build your own from your subject and references. The demo is separate from your workspace.`;
}
function overviewCore() {
  if (!hasCore()) return null;
  const perspectives = data.backbone.perspectives;
  const scope = perspectives.textbooks.levels.length
    ? perspectives.textbooks
    : perspectives.volumes;
  return { scope, level: scope.levels.at(-1) };
}
function linkedConceptMap() {
  if (data.atlas)
    return {
      ...catalog.graphs.find((g) => g.id === data.id),
      title: "Shared concept map",
      nodes: data.atlas.counts.concepts,
      edges: data.atlas.links.length,
    };
  const target = catalog.graphs.find((g) => g.id === data.id)?.concept_map;
  return catalog.graphs.find((g) => g.id === target);
}
function renderLegacyOverview() {
  const guides = document.querySelectorAll("#overview-view .reading-guide article");
  guides[1].querySelector("p").textContent =
    "Arrows lead from prerequisites to the ideas that use them. Dashed lines show other relationships. Scroll or drag the graph to move; use + and − to zoom.";
  guides[1].querySelector(".mini-connection").hidden = false;
  guides[2].querySelector("p").textContent =
    "Select a concept to explore its neighborhood. Open Evidence to read the summary, book treatments, page references, and the reasoning behind each connection.";
  show("overview");
  const pilot = linkedConceptMap();
  $("overview-overlap").hidden = !pilot || !hasCore();
  $("overview-overlap").onclick = () => {
    prepareCore(new URLSearchParams());
    renderCore();
    saveURL();
  };
  const core = overviewCore();
  const bookIDs = core
    ? new Set(core.scope.units.flatMap((u) => u.projects))
    : new Set([data.project_id]);
  const books = catalog.graphs.filter((g) => bookIDs.has(g.project_id));
  $("overview-eyebrow").textContent = data.title.toLocaleUpperCase();
  $("overview-title").textContent = pilot
    ? "Start with a concept map."
    : core
      ? "Explore the example collection."
      : nodes.length
        ? "Get to know this graph."
        : "Your map of ideas starts here.";
  $("overview-intro").textContent = pilot
    ? `${pilot.title} organizes selected records into ${fmt(pilot.nodes)} concepts, with distinct book treatments behind each one. It is a bounded starting point; the full subject concept map is still unfinished.`
    : core
      ? `${books.length} textbook graphs, connected in one shared map. Explore the ideas they share, follow their prerequisites, and look at the evidence behind each connection.`
      : nodes.length
        ? `Explore ${fmt(nodes.length)} concepts and ${fmt(edges.length)} recorded relationships. Start with the concept index or search for an idea, then follow its connections back to the sources.`
        : "Bring your material and work with your coding agent to build a source-backed knowledge graph. The guide walks you through setup, scope, extraction, and independent review.";
  $("overview-explore").textContent = pilot
    ? "Open the concept map →"
    : core
      ? "Inspect exact record overlap →"
      : nodes.length
        ? "Explore the concepts →"
        : "Get set up →";
  $("overview-explore").onclick = () => {
    if (pilot) navigateGraph(pilot.id);
    else if (core) {
      prepareCore(new URLSearchParams());
      renderCore();
      saveURL();
    } else if (nodes.length) {
      if (isConceptMap()) renderConceptMap();
      else show("browse");
      saveURL();
    } else $("about-dialog").showModal();
  };
  $("overview-all").hidden = !nodes.length;
  $("overview-all").textContent =
    `Browse all ${fmt(nodes.length)} ${core ? "records" : "concepts"}`;
  $("overview-caption").textContent = pilot
    ? "The concept map and the detailed record inventory are different layers. No course has been chosen."
    : core
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
    ? "Shared record inventory"
    : "Knowledge graph";
  $("diagram-shared-count").textContent =
    `${fmt(nodes.length)} ${core ? "records" : "concepts"}`;
  $("diagram-shared-note").textContent =
    `${fmt(edges.length)} recorded relationships`;
  $("diagram-core-wrap").hidden = !core && !pilot;
  $("diagram-core-title").textContent = pilot
    ? pilot.title
    : "Exact record overlap";
  if (pilot) {
    $("diagram-core-count").textContent = `${fmt(pilot.nodes)} concepts`;
    $("diagram-core-note").textContent =
      `${fmt(pilot.edges)} relationships · A bounded concept layer, not the complete subject map`;
  } else if (core) {
    $("diagram-core-count").textContent =
      `${fmt(core.level.nodes.length)} records matched`;
    $("diagram-core-note").textContent =
      `Explicit matches across all ${core.scope.units.length} works; not a count of shared topics`;
  }
  const facts = $("overview-facts");
  facts.replaceChildren();
  const values = pilot
    ? [
        [fmt(pilot.nodes), "Concepts in the pilot", pilot.title],
        [
          fmt(pilot.edges),
          "Relationships in the pilot",
          "Only reviewed connections are drawn",
        ],
        [
          fmt(books.length),
          "Textbook graphs",
          "Original treatments remain available",
        ],
        [
          fmt(nodes.length),
          "Detailed shared records",
          "The full inventory remains searchable",
        ],
      ]
    : core
      ? [
          [
            fmt(core.level.nodes.length),
            "Records matched across every work",
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
          [
            fmt(edges.length),
            "Connections",
            "Follow the recorded relationships",
          ],
        ];
  for (const [value, title, caption] of values) {
    const stat = el("div", undefined, "overview-fact");
    stat.append(el("strong", value), el("span", title), el("small", caption));
    facts.append(stat);
  }
  $("overview-structure").textContent = pilot
    ? "Start with the concept map and select an idea to reveal its book treatments. The full shared graph retains the detailed records underneath. Exact overlap is a separate diagnostic of record matching; its count does not measure how many topics the books share."
    : core
      ? `This count measures explicit matches between detailed records: concepts, results, methods, and assumptions. It does not measure all topics the books share. Different treatments of one topic can remain separate. Filtering to these records leaves ${core.level.components.length} connected pieces and removes paths through other records. This intersection is not yet a conceptual backbone.`
      : "Concepts and relationships retain their evidence. The index helps you find an idea; its neighborhood shows where that idea fits.";
  $("overview-wider").hidden = !core || core.scope.units.length <= 2;
  if (core && core.scope.units.length > 2) {
    $("overview-wider").textContent =
      `Diagnostic: wider record overlap (${core.scope.levels[0].nodes.length}) →`;
    $("overview-wider").onclick = () => {
      prepareCore(new URLSearchParams());
      coreMinimum = 2;
      renderCore();
      saveURL();
    };
  }
  document.querySelector(
    "#overview-view .reading-guide article:first-child h3",
  ).textContent = pilot
    ? "Start with the concept map"
    : core
      ? "Inspect exact matches"
      : "Find a concept";
  document.querySelector(
    "#overview-view .reading-guide article:first-child p",
  ).textContent = pilot
    ? "Each point is a concept with supporting book treatments. The pilot covers a selected topic; it does not replace the complete record inventory or establish every connection in the subject."
    : core
      ? "Each card is an extracted record. This filter keeps records explicitly matched to independent treatments in every compared work. A topic can appear in all the books through distinct records and therefore be absent here."
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
  $("home-prompt").textContent = $("setup-prompt").textContent.trim();
  for (const id of ["home-copy", "home-copy-secondary"])
    $(id).onclick = () => copy($("home-prompt").textContent);
  for (const id of ["home-demo", "home-demo-nav", "home-demo-bottom"])
    $(id).onclick = () => {
      if (!data)
        return say("The demo is still loading. Please try again shortly.");
      renderOverview();
      saveURL();
    };
  $("overview-tab").onclick = () => {
    renderOverview();
    saveURL();
  };
  $("overview-all").onclick = () => $("all-concepts").click();
  $("overview-setup").onclick = () => $("about-dialog").showModal();
}

function renderOverview() {
  renderLegacyOverview();
  if (!data.atlas) return;
  const atlas = data.atlas;
  $("overview-title").textContent = "The ideas the books share.";
  $("overview-intro").textContent =
    `${fmt(atlas.counts.concepts)} recognizable concepts organize ${fmt(atlas.counts.records)} source records. ${fmt(atlas.counts.all_works)} have treatments across all ${atlas.works.length} works. Explore the common structure, then compare the different ways each book develops it.`;
  $("overview-explore").textContent = "Open the concept map →";
  $("overview-explore").onclick = () => {
    renderAtlas();
    saveURL();
  };
  $("overview-caption").textContent =
    `${atlas.works.map((w) => w.title).join(" · ")}. No course or audience has been selected.`;
  $("diagram-core-title").textContent = "Shared concepts";
  $("diagram-shared-title").textContent = "Whole-subject concept inventory";
  $("diagram-shared-count").textContent = `${fmt(atlas.counts.concepts)} concepts`;
  $("diagram-shared-note").textContent =
    `${fmt(atlas.counts.records)} book records retain their original treatments`;
  for (const label of $("diagram-books").querySelectorAll("small"))
    label.textContent = label.textContent.replace(" concepts", " records");
  $("diagram-core-count").textContent =
    `${fmt(atlas.counts.all_works)} in every work`;
  $("diagram-core-note").textContent =
    `${fmt(atlas.counts.concepts)} concepts in the complete inventory · Source-specific treatments preserved`;
  const facts = $("overview-facts");
  facts.replaceChildren();
  for (const [value, title, caption] of [
    [
      atlas.counts.all_works,
      "Shared across all works",
      "Explicitly grouped volumes",
    ],
    [
      atlas.counts.two_or_more,
      "Covered by two or more",
      "Primary concept assignments",
    ],
    [
      atlas.counts.concepts,
      "Concepts in the inventory",
      "A whole-subject organization",
    ],
    [
      atlas.counts.records,
      "Underlying source records",
      "Original evidence and qualifications",
    ],
  ]) {
    const fact = el("div", undefined, "overview-fact");
    fact.append(
      el("strong", fmt(value)),
      el("span", title),
      el("small", caption),
    );
    facts.append(fact);
  }
  $("overview-structure").textContent =
    "The map organizes detailed treatments under recognizable concepts. Select an idea for its book coverage and source connections. Coverage is an association, not a claim of identical derivations; a missing assignment is not proven absence. Map lines retain the specific relationships in the underlying book graphs.";
  $("overview-review").textContent =
    "Concept inventory: model-reviewed · Human audit pending";
  document.querySelector(
    "#overview-view .reading-guide article:first-child p",
  ).textContent =
    "Start with a few shared landmarks, then show all concepts or search for an idea. Select a point to compare its book treatments and follow a source connection. The complete record inventory stays accessible underneath.";
  const guides = document.querySelectorAll("#overview-view .reading-guide article");
  guides[1].querySelector("p").textContent =
    "Lines connect ideas through specific book treatments. Select a point to see all its neighbors; open a source link for its direction and qualifications. Scroll or drag to move, and use + or − to zoom.";
  guides[1].querySelector(".mini-connection").hidden = true;
  guides[2].querySelector("p").textContent =
    "Compare the treatments under each book, then open an original record for its full summary and page references. Browser Back returns to the concept map.";
  for (const card of $("overview-books").querySelectorAll(".overview-book")) {
    for (const span of card.querySelectorAll("span"))
      span.textContent = span.textContent.replace(" concepts ·", " records ·");
  }
}
