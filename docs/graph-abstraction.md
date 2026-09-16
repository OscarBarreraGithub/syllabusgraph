# From extracted records to a conceptual map

The example's extraction and correspondence reviews are complete, with a human
audit pending. A whole-subject conceptual overview is a separate, unfinished task.
Source coverage and valid records do not establish that a graph communicates
the subject well or captures every cross-book correspondence.

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

## What is missing

The current shared graph has 1,143 records with no `group`. Existing groups
mix subject areas with source-specific routes and extraction-batch groupings.
They do not yet provide a consistent hierarchy for a subject-level map.

The next scientific task is to define a reusable concept layer above the
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

## First bounded pilot

The [path-integral pilot](../graphs/subjects/qft-path-integrals/README.md) now
provides nine concepts and six relationships from 14 existing reviewed records.
Terra/high produced it and Sol/high accepted it on the first independent review.
Its compact map shows book treatments on selection. Input records, scientific
scope, review outcome, and measured usage are published with the graph.

The selection has three separate components. It does not establish every
connecting dependency or exhaust the topic, and it has not undergone human
inspection. It tests an abstraction approach; it does not finish the subject map.
Inspect the concept boundaries and visual navigation before choosing further
topics. The original shared graph and exact-overlap view remain available.
Future orchestrators should follow the [troubleshooting checkpoint](graph-troubleshooting.md).
