# Troubleshooting a graph that is complete but not useful

Read this before expanding a pilot, reconciling a collection, or redesigning a
graph viewer. It records failures from the first large example and the actions
an orchestrator should take while the work is still small.

## Warning signs and responses

| Symptom | Check | Response |
|---|---|---|
| Thousands of nodes, but familiar ideas are hard to find | Are nodes broad concepts, results, methods, exercises, qualifications, or a mixture? Is that level explicit? | Keep detailed records as treatments. Build a small, reviewed concept layer that points to them before expanding it. Do not delete detail to make a smaller picture. |
| Surprisingly little overlap between similar references | Does the number count exact matched records, topic coverage, or identical derivations? Are complementary volumes counted as separate works? | Label the measure precisely. Inspect a recognizable topic across the sources. Separate missed mappings from valid differences in scope or method. Do not infer absence from a missing match. |
| A supposed backbone falls into isolated pieces | Does filtering discard connecting nodes? Was a spine actually defined, or was intersection/centrality/chapter order used as a substitute? | Keep context visible and distinguish conceptual dependencies from display placement. Define and review any claimed spine. Never invent shortcut prerequisites to make a line. |
| Many records lack a group, or groups refer to work batches | Can someone navigate the subject without understanding extraction history? | Establish a consistent subject-level organization. Missing groups are a diagnostic, not automatic scientific invalidity; choose the appropriate hierarchy case by case. |
| The graph looks like a page of paragraphs | Are full labels, explanations, and evidence competing with structure? | Show compact nodes and a few meaningful labels first. Reveal treatments, qualifications, and evidence on selection. Inspect an actual browser image. |
| Scroll and zoom controls pass tests but visitors remain lost | Can a new visitor identify what the page shows, find a familiar idea, follow a connection, and return? | Test these tasks, including real wheel/drag/touch input. Mechanical correctness is necessary but does not establish visual usefulness. |
| The example has become the whole product | Does the homepage explain how to use the tool with new material? | Lead with the reusable workflow, setup prompt, usage limits, and guide. Place subject-specific content in an explicitly separate demo. |
| A new view exists, but users still see the old result | Follow the primary buttons from the homepage and reload a previously shared URL. Do the overview's diagram, statistics, and labels describe the new starting point? | Update the default journey along with the view. Keep old diagnostics clearly labeled and provide a route to the new map. Test both paths; a working direct link alone is insufficient. |
| Review and repair work keep expanding | Is the same issue returning without a changed evidence contract or concrete progress? | Preserve the checkpoint, follow the finite review policy, and stop at the session limit. A new unit ID or monitoring agent does not solve the issue. |

## A checkpoint before scaling

First define what a shared concept means across the sources. Use stable,
source-neutral identities and inspect existing labels and synonyms before
adding another concept. Decide explicitly whether an incoming record supports
an existing idea, specializes it, supplies a different derivation, or is a new
idea. Preserve assumptions, notation, proof depth, and exercises in the linked
treatments. Differences in a derivation need not imply different parent ideas;
common terminology alone is not enough to identify them either. A node budget
can expose granularity drift, but no universal count is appropriate for every
subject or chapter.

Define the overview's selection rule separately. A union of source coverage,
an exact record intersection, a set of widely covered concepts, and a path
ranked by external course evidence answer different questions. State the
population, denominator, and supporting evidence. A highlighted presentation
rail is not automatically a chain of prerequisite edges. A course-consensus
path requires course evidence; it cannot be inferred from textbook overlap.

Select one representative topic with more than one treatment. Prefer a topic
that exercises the real distinctions in the material, rather than the easiest
possible match. Agree on the output level in the immutable packet: detailed
source records, a concept layer, or a course plan are different outputs.

Use the configured producer and independent critic. At the checkpoint, record:

1. The bounded inputs and their versions; which records contribute to each
   concept and which remain outside scope.
2. What each source covers, including differences and uncertainty. Topic
   membership must not silently become equivalence of derivations.
3. The meaning and support of each relationship. An arrow needs a scientific
   or explicitly editorial meaning, not just a convenient display direction.
4. A working visual that shows the structure before the details, and concrete
   inspection tasks. Preserve disconnected pieces when the evidence requires it.
5. Calls, elapsed time, available usage counters, review outcome, and what would
   change before scaling. Unknown token usage stays unknown.

Inspect relationships crossing the selected topic's boundary before preparing
its packet. A bundle containing only internal edges can produce disconnected
pieces even when the original graph has relevant connections. Record omitted
context and include the reviewed boundary material needed for the pilot's
question; do not invent replacement arrows. A small topical pilot cannot
establish whole-subject coverage or replace the subject overview.

Compare recognizable ideas across sources at the chosen level. Finding every
input record in the output checks preservation; it does not check whether
related treatments are organized under a useful common concept. Check both.

This is a small deliverable checkpoint, not a plan-approval loop or a request
for a person to supervise every unit. Stop according to the authorized session
budget. Do not renew it automatically just because a review requested changes.

## Reuse the evidence already collected

When the issue is conceptual organization, first reuse reviewed records and
their references. Reopen original material only for an actual unresolved claim.
If the source is a derived record bundle, say so: its numbered entries are not
textbook pages, and reviewing it is not a fresh verification of the textbooks.

The pilot uses an isolated graph with ordinary nodes, evidence, and origins,
plus an explicit input manifest. No change to an original book graph is needed.
`scripts/build_record_bundle.py` can produce a deterministic local text bundle
from selected record IDs; it checks the input project's content digest. This is one
available preparation method, not a universal reader or extraction requirement.

## Report completion precisely

Every comparison screen must name the selected graph and scope. Counts from a
nine-concept sample describe that sample, not overlap between entire books.
Distinguish concept coverage from equivalent-record matches and keep source
volume grouping consistent across views. Missing mappings mean unknown coverage
unless an absence has actually been established.

Track source coverage, record-level scientific review, cross-source mappings,
conceptual organization, visual usability, and human audit separately. Passing
one does not finish the others. Report the remaining work plainly rather than
calling the collection "almost done" from node counts or successful validation.

The [abstraction audit](graph-abstraction.md) gives the measured example behind
these lessons. The [run retrospective](qft-run-retrospective.md) covers context
growth, evidence omissions, bookkeeping repairs, and reviewer-loop costs.
