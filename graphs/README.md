# Graph bank

Reusable knowledge graphs belong here, independently of any course. Each
textbook has its own project; a subject project combines reviewed concepts
while preserving links back to their book-specific treatments. Contributions
can cover a small section: completeness is never implied by a book's presence.

The first collection is [quantum field theory](subjects/qft/README.md), with
[Peskin–Schroeder](textbooks/peskin-schroeder/README.md),
[Schwartz](textbooks/schwartz/README.md), and Weinberg
[volume I](textbooks/weinberg-1/README.md) and
[volume II](textbooks/weinberg-2/README.md).

```text
graphs/
  textbooks/<book-id>/
    project.yaml          Bibliography and graph settings
    knowledge/graph.yaml  Reviewed concepts, dependencies, and citations
    review.yaml           Bounded coverage, review status, and omissions
    coverage.yaml         Optional whole-book inventory and remaining page scopes
    adjudications.yaml    Optional final scientific decisions and their reasons
    reconciliation.md     Optional whole-book semantic audit and amendment report
    README.md             Scope and reading guide
  subjects/<subject-id>/  Shared graph with the same project format
```

These are ordinary SyllabusGraph projects with zero course plans. Read their
YAML directly or validate a project using the installed CLI:

```bash
syllabusgraph validate -p graphs/textbooks/peskin-schroeder
python scripts/check_graph_bank.py
```

The second command checks all projects and resolves nodes' reviewed `origins`.
It rejects stale public review digests, course plans, `public_file` attachments, and
origins that do not resolve to exact nodes in a reviewed textbook graph.
Textbook nodes may use origins to identify inputs imported from another book;
their summaries, evidence, and correspondence notes must distinguish using an
external result from deriving it in the current book. Self-imports are rejected.
The report lists these references under `imports`, separately from shared overlap.
Review summaries are contributor declarations tied to graph content; the check
cannot establish that scientific review actually occurred.
When `coverage.yaml` is present, the check also verifies its project identity
and graph digest. It does not authenticate the inventory or prove completeness.
It does not scan arbitrary files for textbook content; inspect files before
committing and run the separate [publication audit](../docs/releasing.md).
Its overlap table counts shared concepts with reviewed origins in each pair of
book graphs. Origins pointing to imported textbook nodes remain valid links,
but do not count as an independent treatment by the importing book in that table.
It describes only the extracted portions, not total textbook
overlap; zero can simply mean the relevant section has not been extracted.
The correspondence notes explain narrower scopes and alternative treatments.
Browse the collection with `syllabusgraph site serve`, or one project with
`syllabusgraph explore -p graphs/subjects/qft`. The read-only explorer includes
book comparison, concept search, source evidence, and neighborhood views without
creating a course plan. See [the website guide](../docs/website.md). Existing
`compare` continues to compare course plans, not textbooks.

To contribute, use a new book directory or extend an existing one through a
focused pull request. State the exact source edition, section scope, node
granularity, scientific review performed, and remaining omissions. Follow the
[source workflow](../docs/source-workflow.md) and
[native review policy](../workflows/orchestrate.md). Public review summaries
must accurately distinguish model review from a human audit.

Use `review.yaml` with `status: partial-model-reviewed` (or `model-reviewed` /
`human-reviewed` when justified) and `graph_digest` equal to
`syllabusgraph.io.digest(project.knowledge)`. Record bounded units and omissions
alongside it. Source-file checksums, packet/proposal fingerprints, and full
processing records stay local. A populated bank graph needs a current review
summary; changing both graph and digest is a contributor attestation, not a
substitute for the required review.

For whole-book work, inventory sections, appendices, projects, and substantive
problems before claiming completeness. Record page coordinates, justified
nonconceptual exclusions, retained notation conventions, accepted unit scopes,
and remaining ranges in `coverage.yaml`. Pages shared by problems and references
retain their substantive material. A reviewed page range alone does not prove
that all its concepts were captured, especially for a narrow pilot.
The [QFT collection](subjects/qft/README.md) includes a reviewed inventory with
conservative progress records and a public final-decision log. These are source
coordinates and review conclusions; textbook text stays private.

A whole-book reconciliation report can map sections to their actual records,
assess dependencies across extraction units, and explain remaining proof limits.
Identify the audited graph snapshot and list subsequent accepted amendments.
Acceptance of a report that identifies a gap does not resolve that gap: retain
its pending status until a source-backed amendment is reviewed and applied.

When a scientific disagreement reaches final adjudication, a project may publish
`adjudications.yaml` with the deciding model, alternatives considered, selected
resolution, affected record IDs, source citations, and promotion or deferral
outcome. Preserve the decision as history when later evidence extends the graph.
Full proposals, quotation witnesses, source fingerprints, and runtime records
remain private. A model decision does not imply that the end human audit occurred.

Put your own PDFs in the project's ignored `materials/` directory, or register
them from another local location. `.syllabusgraph/` holds private source copies,
page text, proposals, quotation checks, and dispatch records. Never commit these
files. Publish original graph summaries and citations only. No textbooks are
needed to reuse or validate the reviewed graphs.

Course design follows graph construction. Audience, objectives, prior knowledge,
and time will shape a course plan, not erase concepts from a textbook graph.
The [roadmap](../docs/roadmap.md) records the task of identifying the right
questions for that later step.
