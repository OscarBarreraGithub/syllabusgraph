# QFT inventory review history

**The revised inventory is accepted; human audit is pending.** See the
[published concept map](../graphs/subjects/qft/concepts/README.md) for its current
counts, scope, decisions, and usage. The rejection below is retained as history.

The first whole-subject candidate was rejected. It proposed 120 concepts
in 15 subject groups and assigned all 2,351 book records exactly once. That
accounting passed, but the assignments were not reliable enough to publish as
conceptual coverage. No concepts from that candidate were promoted at that checkpoint. The four
book graphs and shared record graph were preserved throughout the repair.

Terra/high produced the candidate; independent Sol/high rejected it. This was
one production call and one review call, sequentially, with no correction or
review loop. The session paused at its configured two-call boundary.
[Measured usage](qft-inventory-usage.json) records a 13-minute interval from the
first ticket to the recorded review result, excluding preparation and software
work. Verified token counts were unavailable.

## What failed

The producer used ordered keyword rules on labels and summary excerpts. The
rules supplied a complete partition but made systematic semantic mistakes.
The critic supplied concrete repairs and required reassessment of every row,
rather than accepting a few example fixes.

| Source record | Candidate home | Problem |
|---|---|---|
| Peskin–Schroeder: General non-Abelian gauge construction | Abelian gauge theory | Opposite gauge-theory scope; similar errors occurred across all four books. |
| Peskin–Schroeder: Källén–Lehmann spectral representation | Lie groups and representations | A shared word does not make spectral analysis group representation theory. |
| Schwartz: Gaussian-regulator Casimir-force problem | Lie groups and representations | Casimir force was confused with the group-theory use of the name. |
| Peskin–Schroeder: Majorana canonical quantization | Scattering kinematics and cross sections | An incidental term displaced the main subject. |
| Weinberg II: Monopole flux–winding relation and Bogomol’nyi bound | Electroweak precision observables | The primary home did not match the record's physics. |

A separate 59-record “worked projects and problems” bucket grouped unrelated
material by document format. The critic identified a topical reassignment for
every record in it. Source exercises should retain their task descriptions
under the concepts they develop.

This is a failure of the candidate organization. It does not establish errors
in the underlying reviewed physics records. Nor does it show that the books
have little in common: these candidate overlap counts must not be used.

## How the checkpoint was resumed

The local immutable packet, candidate, exact critique, draft coverage table,
and runtime records remain in ignored storage. The input index is reproducible
from the public book graphs, in this order:

```bash
python scripts/concept_inventory.py index .syllabusgraph/inventory-inputs \
  graphs/textbooks/peskin-schroeder graphs/textbooks/schwartz \
  graphs/textbooks/weinberg-1 graphs/textbooks/weinberg-2
```

The next user instruction authorized work through publication. The orchestrator
resumed the same unit, retaining its original packet and three-call history.
Sol/high's final adjudication changed 988 primary homes and accepted 117 concepts
with five decisions. No reviewer was dispatched to review that adjudication.

A later source-link check exposed four residual mistakes: three atomic-emission
records were still assigned to symmetry breaking, and a BV-antifield record was
assigned to spin statistics. Full original records were added as new evidence
for a narrowly scoped amendment, linked to the same six-call recovery family.
This is a reason to inspect actual treatments when testing a map, not to treat
complete accounting or a model verdict as a guarantee. Sol/high accepted the four corrections and
recorded final replacement authority. The linked family ended at six calls;
no further reviewer followed. The published review records both decisions.

The reusable [inventory tools](concept-inventories.md) check exact record
accounting, pinned input versions, and coverage from explicit native source IDs.
Two imported prerequisites in Weinberg II remain accessible but are excluded
from independent coverage. The website projects existing book relationships;
universal conceptual prerequisites and human audit remain separate work.
