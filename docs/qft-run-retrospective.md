# What the QFT run taught us

The first large run produced four reviewed textbook graphs and a shared graph,
but cost too much to be a sensible default onboarding experience. The reusable
workflow now starts with small, explicitly resumed sessions. The lesson is to
bound work and prepare evidence better, while keeping substantive review.

The later concept-map repair exposed a different bottleneck: repeated display
changes could not supply missing subject organization. A tiny pilot and exact
record intersections were both mistaken for whole-subject coverage. The
[abstraction history](graph-abstraction.md) and
[inventory review](qft-inventory-review.md) record the correction. The reusable
response is to define the unit of comparison, preserve book treatments, review
the full membership inventory, and test real source drilldowns before publishing
counts. A model acceptance still needs an honest scope; shortened summaries can
miss distinctions. Repair observed errors with bounded new evidence, not an
open-ended review of reviews.

This audit covers the public creation history from the initial bank commit
[`4def5cf`](https://github.com/OscarBarreraGithub/syllabusgraph/commit/4def5cf)
through completion at
[`681e56c`](https://github.com/OscarBarreraGithub/syllabusgraph/commit/681e56c),
plus the local dispatch, failure, deferral, promotion, and recovery records.
Only aggregate measurements and operational findings are published here. The
private source packets and worker transcripts remain private.

## What was measured

| Measurement | Observation | Meaning / limit |
|---|---|---|
| Recorded construction interval | About 42 hours, September 14–15, 2026 | Wall time includes pauses and idle time; not active worker hours. |
| Recorded dispatches in that interval | 652 | 625 source-workflow requests plus 27 supplemental requests. Includes retries and issued requests; not necessarily a successful model call. |
| Confirmed worker sessions | 222 | A session can handle multiple calls. This is not simultaneous concurrency. |
| Recorded native results / dispatches with failures | 635 / 17 | These categories can overlap. |
| Work units in the report interval | 179 | Recovery units can belong to the same logical family. Counting unit IDs alone hides retries. |
| Last independently verified usage snapshot | 68,832,437 comparable tokens through September 15, 16:29 UTC | Input excluding reported cache plus output; **not a complete run total or billing measure**. See the [usage record](../graphs/subjects/qft/usage.md). |
| Source requests across the full local creation history, including pilots | 643 requests across 184 unit directories | A different scope from the 652-request report; do not add the two counts. |
| Saved source-request size in the full local history | Median 2.54 MB; maximum 12.49 MB; 2.30 GB summed | Serialized JSON bytes, including repeated graph/evidence context. Not tokens, unique data, or necessarily provider input. |
| Public commit intervals after the initial graph bank | 93 intervals; median 19.47 minutes; longest 196.48 minutes | A commit gap is a publication gap, not proof that agents were idle or looping. |

The original goal counter froze at 59,502,458 tokens. A later local reconstruction
was held when counter continuity could no longer be verified. We do not add
snapshots, count cached tokens twice, infer prices, or present a final total.
Some older results lack completion timestamps, so exact active worker durations
cannot be reconstructed from them. New completion receipts record timestamps.

## Where time and usage went

**Whole-book extraction finished before shared-graph reconciliation.** By
`391bcd1` / `ac3a5ff` on September 14, all four book scopes and audits were
published. Shared correspondence work continued until the next evening. At
`f04edd7` on September 15, every book concept had an origin mapping, but the
combined relationship assessment still left **230 cases** to resolve. Reporting
this as “almost done” understated the remaining scientific work.

Improvement: keep separate counts for source coverage, reviewed book concepts,
reviewed book relationships, mapped origins, reconciled shared relationships,
mechanical validation, and publication. Completion in one column must not close
another. Estimate remaining time from comparable full units, including initial
extraction and review, rather than review-only timings or node counts.

**Evidence packets repeatedly omitted retained citations needed by amendments.**
The full local history contains 51 deferred unit records. Many explicitly
continue in an evidence-extended unit: a proposed shared-node amendment kept
old citations, but the original immutable packet did not contain those pages.
These are historical closed attempts, not 51 outstanding graph defects.
Examples include `full-align-029`, `035`, `037`, `043`, and `055`.

Improvement: before dispatch, enumerate the existing records likely to be
amended, their retained citations, new evidence, and incident relationships.
Prepare the union of those pages once. Mechanical preflight must include
proposed replacement records even when they are still described as unresolved
amendments. A source-scope error should be caught before another scientific
critic is asked to read the whole packet. This remains an orchestrator
responsibility for custom amendment formats; the engine cannot parse arbitrary
free-form amendment instructions.

**The final Peskin repair repeated this evidence problem.** The scientific
review accepted the resolution, then final validation found ten retained page
citations absent from its 206-page packet. The evidence recovery expanded the
packet to 216 pages and cost three additional calls. The logical family took
about 48 minutes and eight issued dispatches, despite a six-call per-unit limit.
The next two repair batches took about 18 and 10 minutes, with four and two
calls respectively. The two-call case shows that no extra review loop is needed
when extraction and the first critic agree.

Improvement: recovery IDs share a family budget. Register a recovery with
`work link CHILD --parent PARENT` **before** its first dispatch. A renamed unit
must not manufacture a fresh allowance. Six calls across the family is the new
ceiling; if new evidence cannot be handled within it, defer and record why.
There is no automatic exception or reviewer of a final decision.

**Some expensive review work repaired bookkeeping and weak generic labels.**
The combined relationship assessment initially treated graph reachability and
generic boundary labels as sufficient explanations. The first critic identified
93 alleged gaps already represented by accepted residual edges. Later, 139
cases still lacked individual source support, and 238 receipt references across
157 rows needed correction. Final adjudication converted unresolved questions
into explicit pending source work rather than approving vague explanations.

Improvement: build an exact index of accepted edges, routes, origin owners, and
receipt membership before asking a model what is missing. Validate IDs
mechanically. A path in a graph is not evidence that a prerequisite or derivation
is scientifically adequate. Write a concrete disposition for each source
relationship, with its supporting records, instead of repeating boilerplate.

**Runtime and schema failures consumed recovery calls.** Alignment `026`
needed a format-only replay after an unsupported `affected_records.kind`;
alignment `047` suffered two correction calls with no result and a bounded
recovery. Scientific decisions were not meant to restart because serialization
failed. These exceptions also crossed the nominal per-unit accounting boundary.

Improvement: supply the actual output contract, validate JSON before importing,
preserve returned files, and record failures explicitly. Recover a saved result
before launching another worker. Do not rerun accepted science to repair a file
path or enum. Family accounting includes failed and superseded tickets.

**Growing shared context made every later call heavier.** Requests serialized
the current graph along with evidence and previous results. The 2.54 MB median
and 12.49 MB maximum make repeated full-context reading a concrete concern,
although byte size alone cannot establish its share of token cost.

Improvement implemented now: a session request-size guard rejects oversized
requests before ticket issuance. Default: 750 KB of compact request content.
It includes current graph context. For an already large graph, even a small
page scope can exceed this limit; explicitly select an appropriate larger
allowance or work on a separate, coherent book/section project and reconcile
later. Do not silently drop dependencies or evidence to fit a budget. Automatic
scientifically safe graph-context selection is not implemented.

**Concurrency and monitoring added coordination work.** Shared graph updates
could invalidate stale reviews. `fc5b3a7` separated a draft's source identity
from the graph revision, allowing a draft to finish while still requiring a
fresh review against the current graph. The user later required serial work.
Frequent status queries and a growing orchestration conversation also consumed
usage that worker-only counts do not capture.

Improvement: default to one worker. Increase concurrency only for genuinely
independent scopes under an explicit session budget. Read metadata rather than
whole transcripts. Wait on completion events. No monitoring agent, endless
polling, or recurring plan review. Accepted source claims get one bounded
review path; stylistic preferences do not block completion.

## What the next orchestrator should do

The later visualization work exposed a separate failure: complete source
coverage and record-level review had been treated as sufficient for a usable
conceptual map. Detailed methods, qualifications, and results appeared as large
text cards, while a strict all-book intersection was mislabeled a backbone.
It removed connecting context and understated broader topic coverage. The
homepage also centered the example instead of explaining the reusable tool.

Improvement: use the [graph troubleshooting guide](graph-troubleshooting.md)
before scaling or redesigning. First inspect one bounded concept layer with
explicit book treatments and a working visual. Keep conceptual readiness and
visual usability separate from extraction and review completion. Reuse existing
evidence; a presentation failure does not justify another whole-book extraction.

1. At session start, inspect saved state and select one bounded next action.
   Recover returned results before issuing anything new. Start with a small
   pilot; report its calls, elapsed time, and available usage counter before
   extrapolating to a book.
2. Preflight evidence scope, page mapping, candidate amendments, exact record
   IDs, and request size. Reuse private reader caches. Do not re-OCR the book on
   every call or reread every transcript after each checkpoint.
3. Dispatch within the session allowance. Persist every result immediately.
   Correct once, recheck once, then use the configured final adjudicator.
   Never ask another critic to review that final decision.
4. If a worker has been outstanding for ten minutes, inspect progress **once**.
   Age alone is not a stall: look for new results, source checks, or a concrete
   current operation. If there is no progress, stop dependent dispatches,
   recover the host result or record failure, and defer if the bounded recovery
   cannot solve it. Check on an event or a reasonable interval, not a busy loop.
5. Stop launching when calls, admission time, or context allowance runs out.
   Save results, promote already accepted work if mechanical checks pass,
   pause, and report what is next. A new session requires a new user request.
6. Report progress with the separate completion columns above. Flag missing
   usage coverage. Don't forecast “almost done” from a successful intermediate
   checkpoint or a quiet review queue.

The software enforces dispatch/session/context/concurrency limits and linked
family budgets. It flags outstanding calls older than ten minutes in
`work status`; it does not infer whether a remote model is making progress,
terminate native workers, or detect unlinked semantic duplicates. Those parts
remain the orchestrator's job. The [usage guide](usage-estimates.md) describes
the exact boundary between enforced limits and human/agent policy.
