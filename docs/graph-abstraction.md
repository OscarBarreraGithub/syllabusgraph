# From extracted records to a conceptual map

The current [subject map](../graphs/subjects/qft/concepts/README.md) organizes
2,351 book records into 117 concepts. Of those, 82 have native-source treatments
in all three works and 107 in at least two. The organizational review is complete;
human audit remains pending. Connections project existing book relationships
onto the accepted memberships, preserving the original treatments and evidence.

The earlier exact-match graph and bounded pilot answer different questions.
This page preserves the diagnosis that led to the concept layer.

## What the overlap count measures

At shared graph digest
`sha256:5f55bb4fec0de5609648bf92e19f3a9f94bcaffa1a4d1ce095aa2a315603d42a`,
the QFT collection contains 2,156 shared-graph records. Comparing
Peskin–Schroeder, Schwartz, and Weinberg I + II as three works gives:

| Explicit independent book matches | Records |
|---|---:|
| All three works | 78 |
| Exactly two works | 227 |
| One work | 1,776 |
| No independent book-origin match | 75 |

Thus 305 records have matches in at least two works. The 75 records in the
last row are not necessarily unsupported: source evidence and an independent
book-origin mapping are different fields. Imported textbook prerequisites do
not count as an independent treatment.

These are counts of explicit correspondence at the stored record granularity,
**not counts of the physics topics the books share**. The graph contains 1,005
method records and 762 result records, as well as concepts, representations,
and assumptions. Qualifications, proofs, calculations, and exercises may occupy
separate records within one broad idea.

For example, the accepted graph has a time-sliced quantum-mechanical path
integral record matched to Peskin–Schroeder and Schwartz, and a field-theory
path integral from the Hamiltonian record matched to Schwartz and Weinberg I.
Neither is an all-three match. Both belong in an investigation of the broader
path-integral topic; treating them as identical would lose their distinctions.
This example establishes a limitation of the count, not a new equivalence claim.

The all-three filter also removes every other record and any edge incident on
one of them. The resulting 78 records have 72 relationships, 25 connected
components, and 17 isolated records. It is an induced intersection, not an
established conceptual backbone. A node outside the filter may connect pieces
that appear disconnected inside it.

## What the record graph was missing

The original shared record graph had 1,143 records with no `group`. Its groups
mixed subject areas with source-specific routes and extraction batches. That
organization was insufficient for a subject-level map; the separate inventory
now supplies the reviewed topic homes.

The repair required defining a reusable concept layer above the
existing records, with explicit mappings from book treatments to concepts.
Keep conceptual coverage, equivalence of results, and alternative derivations
distinct. A book's presence in a topic must come from reviewed supporting
records; the display must not invent it from a familiar title or keyword.

Start with one bounded topic using the existing extracted records and evidence.
Establish a coherent shared concept, its book treatments, and its dependencies;
check that it remains useful without choosing an audience or teaching order.
Inspect the resulting map before extending the approach across the collection.
Use the configured extraction/review policy for any new scientific mappings.
Do not rerun whole-book extraction merely to change presentation.

## Presentation requirements

- The homepage explains the reusable tool and provides its copyable setup
  prompt. The subject collection is a separate demo.
- The map starts with structure: a small number of meaningful labeled anchors,
  surrounding context, and visible connections. Textual evidence belongs in a
  selection panel or detail view.
- Zooming and selection reveal detail. An initial screen of long record titles
  is not a successful overview, even if all controls work.
- A conceptual spine must have an explicit, reviewable definition. Book
  intersection, graph centrality, chapter order, and course order are different
  things; none automatically supplies that spine.
- Evaluation must include recognizable concepts, understandable paths,
  traceable book coverage, and useful navigation, alongside mechanical tests.

## Historical checkpoint: the bounded pilot

The [path-integral pilot](../graphs/subjects/qft-path-integrals/README.md) provided nine concepts and six relationships from 14 existing reviewed records.
Terra/high produced it and Sol/high accepted it on the first independent review.
Its compact map shows book treatments on selection. Input records, scientific
scope, review outcome, and measured usage are published with the graph.

The selection has three separate components. It does not establish every
connecting dependency or exhaust the topic, and it has not undergone human
inspection. It tests an abstraction approach; it does not finish the subject map.
It is retained as a workflow example, not the current starting point. The original
shared graph and exact-overlap diagnostic also remain available.
Future orchestrators should follow the [troubleshooting checkpoint](graph-troubleshooting.md).

## Why the pilot did not resolve the whole-subject problem

The pilot reorganized 14 of 2,156 detailed records. Its selection contains only
internal relationships; links to unselected records are outside that bundle.
The resulting nine concepts and three components test a local abstraction,
not a subject-wide skeleton. Moving this small graph to the main entry point
did not create the missing whole-subject organization.

The pilot's pairwise comparison also counts only its nine concepts: for example,
three are mapped to both Peskin–Schroeder and Weinberg I, whereas the full shared
record graph has 68 explicit matches for that pair. Neither number estimates
every topic those books have in common. The comparison interface needs explicit
scope and consistent work/volume grouping, beyond the graph selector.

The missing deliverable was a subject-wide inventory of stable concepts, mapped
to the reviewed book treatments, with supported dependencies and a stated rule
for highlighting its central structure. Preserve source-specific detail beneath
that inventory. Reuse the accepted evidence and review new mappings in bounded
units; do not rerun whole-book extraction just to impose a new display.

An external course-consensus path would be a separate analysis with its own
corpus and selection rule. The current graph-only task does not require an
audience, a semester length, or a course sequence. Source coverage and dependency
structure can organize the subject before any course is chosen.

## Current resolution

The whole-subject inventory now supplies stable primary homes, a per-book
coverage table, and a browsable shared network. It retains all original records.
The first keyword-driven candidate was rejected; the configured final adjudicator
resolved its material findings. See the [review history](qft-inventory-review.md).

The opening 27 landmarks are a display selection from the 82 shared concepts.
Every displayed line is supported by an existing book relationship; the complete
projected network remains inspectable. This projection does not promote a
qualified source prerequisite into a universal concept prerequisite. Establishing
such prerequisites or an external course-consensus path needs a separate evidence
contract. The graph is ready to explore before choosing an audience or course.
