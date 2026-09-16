# Path integrals: concept-layer pilot

**Nine concepts, six relationships, 14 supporting records.** This bounded
pilot reorganizes previously reviewed QFT records into recognizable ideas,
with distinct book treatments beneath them. It does not replace or modify the
four book graphs or the full shared graph.

Terra/high produced the proposal; a separate Sol/high critic accepted it on the
first review. Mechanical checks passed and the proposal was promoted. Human
inspection is pending. The review used the derived graph records, not a fresh
reading of textbook pages. It makes no claim of complete path-integral coverage.

[Graph](knowledge/graph.yaml) · [Inputs](inputs.json) · [Review](review.yaml) ·
[Measured usage](usage.json) · [Orchestrator troubleshooting](../../../docs/graph-troubleshooting.md)

## What to inspect

Open the website, choose **Explore the demo**, then **Explore the concept
pilot**. The compact map shows short labels and the recorded relationships.
Select an idea to see its meaning and the book treatments contributing to it.
Follow a treatment to the original book node and its textbook page references.

- **Path-integral constructions** collects the time-sliced, phase-space, and
  field-theory constructions. Its book-origin notes preserve their different
  prescriptions and assumptions. This is broader topic coverage, not a claim
  that the derivations are interchangeable.
- **Free-field contractions** brings together the functional pairings, operator
  Wick theorem, and scalar-propagator treatments while retaining their scope.
- The connected-functional and effective-action branch keeps source-specific
  conventions. The critic accepted its scoped prerequisite claims.

The map has three connected components, including one isolated concept.
Those gaps are visible. The small selection does not establish all connecting
dependencies, and no artificial spine was added to make the diagram connected.
This remains a pilot for inspecting the abstraction and visual approach, not a
finished backbone of the full subject. No audience or course order was chosen.

## Reproduce the inputs

`inputs.json` lists the 14 shared-graph record IDs in stable bundle-page order
and pins the input project's content digest (configuration, knowledge, and
plans). From the repository root:

```bash
python scripts/build_record_bundle.py graphs/subjects/qft \
  graphs/subjects/qft-path-integrals/inputs.json \
  .syllabusgraph/path-integral-records.txt
syllabusgraph validate -p graphs/subjects/qft-path-integrals
syllabusgraph site serve --port 8767
```

The bundle is a deterministic export of public derived records and their
relationships within this selection. No original textbooks are copied.
Evidence source `reviewed-qft-records` uses the manifest's numbered entries;
these are **not textbook page numbers**. Evidence sections name original
shared-graph records. Book-origin links retain access to the original treatments.

The normal bounded producer/critic workflow produced this ordinary graph.
Local packets, quote witnesses, runtime records, and policy stay ignored.
Reusing the accepted graph makes no model calls. Extending it requires a new
authorized scope and the normal review policy, not an automatic renewal.

## Checkpoint

Two calls, one worker at a time, no correction loop. The measured interval from
first dispatch to accepted promotion was about seven minutes. That excludes
preparation, website implementation, and the orchestrator's earlier work.
Verified token counters were unavailable; serialized request sizes in
`usage.json` are not token or billing estimates. A full-collection forecast must
also account for input selection, boundary connections, and integration work.

Before expanding, inspect whether these concepts and their book-treatment
distinctions are useful. Remaining subject work includes choosing representative
topics, reviewing missing conceptual connections, and establishing a coherent
whole-subject map. The previous record inventory remains available throughout.
