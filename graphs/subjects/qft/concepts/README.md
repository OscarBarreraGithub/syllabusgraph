# The shared QFT concepts

**117 concepts, 15 subject groups, 2,351 book records.** Every record has one
primary topic home; the original book graphs retain its full treatment.
Open the local website and choose **Explore the demo → Open the concept map**.

| Coverage | Concepts |
|---|---:|
| All three works: Peskin–Schroeder, Schwartz, Weinberg I + II | 82 |
| At least two of those works | 107 |
| All four individual volumes | 33 |
| Whole inventory | 117 |

These are topic associations, not claims of identical results or derivations.
Volumes are grouped explicitly in the catalog. Coverage requires citations to
the book's native sources; two imported Weinberg I prerequisites in Weinberg II
are retained but do not count as that volume's independent treatment. A zero
means no primary assignment, not established absence from a book.

[All concepts and book counts](coverage.md) · [Inventory](inventory.json) ·
[Input identities](inputs.json) · [Review](review.yaml) ·
[Final decisions](decisions.json) · [Measured usage](usage.json)

## Reading the connections

The shared network contains 82 concepts and 618 distinct connected pairs in
one connected component. Each pair has at least one original book relationship
between records assigned to its endpoints. A line says those **specific
treatments** connect; it is not a universal prerequisite between broad ideas.
Open it to inspect the original direction, rationale, qualifications, and pages.
The connecting relationship need not occur in all three works.

Across the full inventory, 1,095 book relationships stay within a concept and
1,762 cross concept boundaries, forming 801 distinct pairs. These account for
all 2,857 original book relationships. No new scientific edges were inferred.

The opening view selects up to two well-connected shared concepts per subject
group: 27 landmarks for this collection. Connections contribute a score of
`1 + supporting works / 4`; ties use concept IDs. A spanning forest, preferring
more supporting works and then more source links, reduces visual clutter.
These are display rules, not a teaching order or scientific consensus ranking.
Select a concept to see all its connections, switch to **All concepts**, widen
coverage, or add surrounding context. Search also finds original treatment labels.

## What was reviewed

Terra/high proposed the inventory. Independent Sol/high rejected systematic
keyword collisions and an unrelated exercise bucket. On the authorized resume,
Sol/high made the final decision in the same work unit: reassess every row,
change 988 primary homes, and accept 117 concepts with five recorded decisions.
There was no reviewer-after-adjudicator loop. The
[rejection record](../../../../docs/qft-inventory-review.md) is retained.

A source drilldown then exposed four residual mistakes. A bounded amendment
added the full original records: three atomic-emission treatments moved from
symmetry breaking to free fields, and one BV-antifield treatment moved from spin
statistics to BRST/BV. Terra/high produced the correction; Sol/high reviewed it
and recorded final replacement authority. The linked family used six calls in
total, retaining the original verdict and the amendment separately.

The initial organizational review used labels and first-sentence excerpts from the
existing reviewed summaries. It did not reread the textbooks, establish exact
equivalence, review secondary topic assignments, or certify universal concept
prerequisites. All detailed records remain available to inspect those distinctions.
**Human audit is pending.** The derived connection projection is mechanically
checked against the original book relationships, not a new scientific review.

## Measured effort

The inventory and bounded amendment used **six sequential calls to two workers**
(Terra/high and Sol/high). Summed dispatch-to-completion intervals were **37.4
minutes**. The first-ticket-to-last-result span was **91.7 minutes**, including
a pause between user turns. Neither is measured active model computation time.
These figures exclude the original textbook extraction, software work, and
orchestrator usage; verified per-call tokens were unavailable. See
[usage.json](usage.json), the separate
[completion-work counter snapshot](../../../../docs/qft-share-ready-usage.json),
and the [original run history](../../../../docs/usage-estimates.md).

## Reproduce from a clone

After the agent follows [SETUP.md](../../../../SETUP.md), these checks require
neither textbooks nor model calls:

```bash
python scripts/concept_inventory.py verify \
  graphs/subjects/qft/concepts/inputs.json \
  graphs/subjects/qft/concepts/inventory.json \
  graphs/textbooks/peskin-schroeder graphs/textbooks/schwartz \
  graphs/textbooks/weinberg-1 graphs/textbooks/weinberg-2
syllabusgraph site build
syllabusgraph site serve --port 8767 --open
```

The build verifies the review declaration, inventory digest, pinned book
versions, exact record partition, and native-source counts before exporting.
It preserves the detailed shared graph separately. Private sources, quoted
witnesses, agent requests, and runtime logs are not distributed.

To make an inventory for another subject, follow the
[reusable workflow](../../../../docs/concept-inventories.md). Changing scientific
memberships requires the configured independent review; changing layout does not.
