# Organize the subject before drawing its backbone

A detailed extraction can contain sound results, proofs, and exercises without
providing a useful overview. A concept inventory gives those records recognizable
homes while retaining their original assumptions and evidence.

Start with the existing records. Do not reread entire books merely to change
their organization. One available preparation tool is:

```bash
python scripts/concept_inventory.py index .syllabusgraph/inventory-inputs \
  path/to/book-one path/to/book-two
```

It writes a manifest with exact project/record identities and knowledge digests,
plus a derived text source with 40 records per index page. Each row contains its
ordinal, book identifier, label, and the first sentence of its existing summary.
These are **summary excerpts, not complete evidence**. They support an initial
organizational pass; they cannot settle qualified equivalence or prerequisites.
Other suitable preparation methods are welcome. Preserve identity and the
limits of the material supplied to workers.

The orchestrator prepares an ordinary immutable packet in an isolated local
project, registers the derived text as `record-index`, and states the intended
output explicitly. Use source-neutral concept IDs, short labels, meaningful
subject groups, and one primary home per indexed record. This primary assignment
is a navigation convention: a treatment can concern other concepts too. Keep
all original records accessible. Record ambiguity instead of forcing a match.

For this compact representation, each proposed node has one evidence entry:

```json
{"source": "record-index", "section": "{\"records\":[1,7]}", "pages": [1]}
```

The `section` lists record ordinals in the manifest. `pages` lists the exact
index pages containing those records, not pages in the books. The proposal uses
the normal schema and quote-witness requirements. It has no dependency edges or
motivations: those need a later, appropriately supported review.

```bash
python scripts/concept_inventory.py check \
  .syllabusgraph/inventory-inputs/index.json path/to/proposal.json
```

This checks the exact partition and pagination. It does **not** judge whether
the concepts are sensible. The configured independent critic must assess the
memberships, recognizable coverage, and granularity. A technically complete
partition can still have bad bins or miss cross-book correspondences.
Keyword rules or other automatic clustering may help prepare candidates, but
the worker must check their meaning. In particular, an incidental term can win
an ordered rule before the actual topic does. A fallback category of unrelated
"problems" is not a shared physics concept. Do not let a suggested node count
become a quota or use complete record accounting as the acceptance criterion.

Use the existing bounded dispatch workflow, including its session limit. Choose
the concept ceiling for the material; keep space in the request allowance for
the critic's copy of the proposal. A large ceiling does not grant more calls,
workers, or request bytes. If review finds a material problem at the boundary,
save the draft and findings; do not silently renew the session.

## Coverage needs its own definition

The package's `inventory()` resolves compact memberships to exact project/node
IDs. `resolve_coverage()` checks the pinned graphs and an explicit per-project
list of native source IDs. Imported prerequisites stay in the inventory but
do not count as independent treatment by the importing book. This choice is
explicit; the software does not guess a source's identity from its name.

Report counts of associated treatments, keeping individual volumes visible.
If volumes are also grouped into a work, state that grouping. A zero means no
primary assignment under the current inventory, not verified absence from a
book. Positive coverage does not assert equivalent results or methods.

Publish the inventory, input identities/digests, coverage rule, review outcome,
and measured usage. Keep requests, witnesses, runtime records, and sources in
ignored storage. Distinguish a reviewed inventory from a reviewed dependency
graph, a visual backbone, and a human audit.

A clone can recheck published memberships and coverage without the private
proposal, original books, or any model calls:

```bash
python scripts/concept_inventory.py verify path/to/inputs.json \
  path/to/inventory.json path/to/book-one path/to/book-two
```

This verifies identities, input versions, full record accounting, and derived
counts. Substantive concept review remains a separate recorded assessment.

## Publish a browsable map

The preparation functions live in `syllabusgraph.inventory`; the script is a
CLI wrapper. After promotion, resolve the accepted proposal with `inventory()`
and `resolve_coverage()`, then publish these files in a directory of your choice:

| File | Contents |
|---|---|
| `inventory.json` | Concepts, groups, exact treatment identities, native-source coverage rules and derived counts |
| `inputs.json` | The pinned record-index manifest |
| `review.yaml` | `status: model-reviewed`, `human_audit`, and `inventory_digest` calculated by `syllabusgraph.io.digest`; record the review scope and model decisions too |
| `README.md` | Meaning of membership, coverage, connections, and remaining limitations |
| Review and usage records | Public decisions and aggregate measurements, with unavailable token counts left unknown |

Add `inventory: "relative/path/to/directory"` to a collection entry in your site
catalog. Include all its book graphs as `kind: textbook`. Optional
`comparison_group: {"id": "work-id", "title": "Work title"}` explicitly combines
volumes for headline coverage. The builder verifies identities, digests, exact
record accounting, and coverage before attaching the concept atlas. A status
declaration is not cryptographic proof of scientific review; preserve its audit.

The atlas deterministically projects original book relationships through the
accepted primary homes. It retains exact source witnesses and displays those
links without universal prerequisite arrows. It shows a reduced landmark view
first; all concepts and every selected concept's neighbors remain accessible.
See the [worked example](../graphs/subjects/qft/concepts/README.md) and
[website guide](website.md). Building and browsing use no models.

To infer universal conceptual dependencies instead, use full supporting records
and relevant boundary relationships in a separate scientific review. Define a
backbone's selection rule separately from its layout. Neither an inventory nor
a coverage threshold establishes a scientific chain or a course sequence.

## Check the meaning at the source

Test actual treatment paths, including easily confused terms. The QFT repair
still had atomic spontaneous emission under spontaneous symmetry breaking and
BV antifields under spin statistics after its index-only adjudication. Full
records supported a narrow amendment. Record the new evidence, link the recovery
to the original call budget, and review the changed memberships only. Do not
restart the entire inventory or silently edit accepted scientific assignments.
