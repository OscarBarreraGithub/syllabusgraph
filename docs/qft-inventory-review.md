# QFT inventory checkpoint

**The first whole-subject candidate was rejected.** It proposed 120 concepts
in 15 subject groups and assigned all 2,351 book records exactly once. That
accounting passed, but the assignments were not reliable enough to publish as
conceptual coverage. No candidate concepts were promoted. The four book graphs,
shared record graph, and website data are unchanged.

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

## Resume from the checkpoint

The local immutable packet, candidate, exact critique, draft coverage table,
and runtime records remain in ignored storage. The input index is reproducible
from the public book graphs, in this order:

```bash
python scripts/concept_inventory.py index .syllabusgraph/inventory-inputs \
  graphs/textbooks/peskin-schroeder graphs/textbooks/schwartz \
  graphs/textbooks/weinberg-1 graphs/textbooks/weinberg-2
```

On the next authorized session, retain the existing unit and findings. A
`reject` routes to the configured final adjudicator under the normal workflow;
it does not justify a fresh unit that resets the call allowance. Reassess each
primary association by meaning, inspect competing concepts and cross-book
consistency, and resolve or defer every material finding. Applying only the
listed examples or changing keyword priority is insufficient. Do not dispatch
a new reviewer after final adjudication.

The reusable [inventory tools](concept-inventories.md) now check exact record
accounting, pinned input versions, and coverage from explicit native source
IDs. Two imported prerequisites in Weinberg II are retained but excluded from
independent coverage by that volume. Those safeguards do not replace semantic
review. Dependencies, backbone selection, and visualization remain later work.
