# Architecture

SyllabusGraph has three boundaries:

| Layer | Owns |
|---|---|
| Engine | Validation, graph algorithms, planning, source workflow, API, UI, export |
| Subject knowledge | Concepts, evidence, relationships, notation, topic groups, motivation |
| Course plan | Audience, outcomes, assumed mastery, narrative order, teaching time, exclusions |

The core package does not enumerate textbooks, subject namespaces, instructors,
or semesters. `Project` resolves explicit project paths. A knowledge base can
have zero concepts, and a course can start without outcomes or a comparison
corpus. The blank project and bundled sampling example use the same APIs.

## Planning

Mastery levels are an ordered project configuration; the supplied templates
use `recognize`, `use`, and `derive`. A prerequisite specifies both the source
mastery required and the target mastery at which the dependency becomes active.
Closure propagates the strongest required level until reaching a sufficient
background assumption. Explicit course targets are still taught even if also
listed as background.

Only `prerequisite` relationships constrain closure and order. Alternative
derivations, evidential support, and editorial preferences remain visible data.
The concept-level prerequisite graph must be acyclic. When sources use reverse
derivation routes, represent the alternatives explicitly rather than placing
both directions in the compulsory prerequisite graph.

Topological sorting uses configured topic-group order to choose between ready
concepts. The graph layout uses prerequisite depth and hides transitively
implied edges. Layout coordinates do not claim teaching chronology.

The session planner partitions the ordered concepts into contiguous sessions.
Its exact dynamic program balances estimated time while preferring coherent
group boundaries. Estimates apply to the requested treatment depth. Missing
estimates use a neutral weight for partitioning and remain visibly unestimated;
the output never claims such a session fits. Estimates currently describe a
whole treatment, not an empirically calibrated adjustment for partial entry
knowledge. The algorithm is intended for course-sized graphs, not millions of
concepts; partitioning is quadratic in selected concepts per session count.
A plan can select up to 1,000 concepts; larger selections need a narrower scope
or more explicitly supplied entry background.

Prior course assumptions use the prior course's explicit outcomes, not every
topic mentioned in it. The prior plan must be marked ready and have no blocking
planning errors. This is an instructor-declared entry contract, not evidence
that any particular student has mastered the material. Explicit audience
answers can lower inherited assumptions. The `unknown` list removes an
assumption completely, including one inherited from an earlier course.

## Reproducibility

Canonical JSON serialization determines content hashes. Project configuration,
knowledge, and course plans determine a project digest; source file checksums
identify the locally supplied editions. Run times and local file paths are
absent from compiled course identity. There is no cache prerequisite for
loading a project.

An extraction packet records source checksum, page mapping, exact scope,
instructions/schema, and the knowledge base seen by the extractor. Reusing the
same work-unit ID with different inputs is rejected. A changed proposal
invalidates prior acceptance. A changed knowledge base requires review again,
apart from recovery after the same atomic graph write already completed.

## Agent review contract

`agents.py` records accepted local role policy and immutable orchestrator
requests. The native host launches the configured runtime; model identity is a
trusted runtime report, not cryptographic attestation. Extractors and adjudicators
produce proposals. An independent critic reviews extraction; the configured
critic model gives the final adjudication when disputes persist. Acceptance binds
the exact revision, base, and policy before promotion. There is no critic after
adjudication. A fixed per-unit dispatch budget also bounds failed retries;
unresolved or invalid final results are deferred, not endlessly resubmitted.

Decision ledgers authorize exact record replacements and retain source citations,
alternatives, and rationale. They do not waive graph or evidence checks. Audit
history includes dispatches, failures, decisions, and snapshot-bound human checks.
Default end-audit mode allows work to proceed while human review is pending;
trust mode makes that final review optional. Original sources, quotes, requests,
and audit logs stay in ignored storage.

## Storage and local serving

The canonical graph is one file, replaced atomically during promotion.
Receipts and work-unit status permit recovery if the process stopped after
that replacement. A project-level exclusive lock prevents simultaneous writers;
an interrupted lock requires explicit operator inspection before removal.

The server binds to loopback, checks Host, validates write origins and a
per-session token, and serves an explicit UI asset allowlist. It does not serve
arbitrary project paths, source binaries, extraction text, or run logs. Public
exports are assembled from reviewed project data. It is a local application,
not an authenticated multi-user hosting service.

## Extension points

The command runner accepts JSON on stdin and returns JSON on stdout. It can
wrap a model API, a local model, an existing agent tool, or a manual workflow.
No runner is selected or executed automatically. Add integrations outside the
planner so model availability never prevents using a reviewed course.

Cross-course overlap/depth comparison is implemented. External syllabus
alignment, institutional corpus collection, automatic OCR, timed teaching
studies, collaborative hosted accounts, and generation of complete lecture
prose are separate extensions. They do not gate the basic course workflow.

## Read-only graph website

`site.py` exports explicitly selected projects into static assets. It never
copies project directories. `explorer/` contains dependency-free HTML, CSS, and
canvas/DOM JavaScript shared by local browsing and Cloudflare hosting. The
payload preserves graph records and selected bibliography fields; derived
`direct_books` comparison metadata excludes imported textbook nodes. Public
exports have no endpoints for uploading or editing private sources.

## Session pacing

`pacing.py` gates native ticket creation under the existing project write lock.
Work-session identity is bound into the immutable dispatch. Counts come from
tickets, including failures, rather than a counter reset by model configuration.
Admission time, request size, and worker concurrency are independently bounded.
Recovery families flatten to an immutable root and count historical tickets.
Completion and promotion remain possible after a session pauses or expires.
`work status` reads metadata only; it never launches a worker or infers quota.
Manual command adapters are outside these gates and must not be used to bypass
the user's limits. See [usage boundaries](usage-estimates.md).
