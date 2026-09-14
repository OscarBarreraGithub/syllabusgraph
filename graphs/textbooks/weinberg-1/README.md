# The Quantum Theory of Fields, Volume I: Foundations

**Partial, model-reviewed graph:** 483 concepts and 631 relationships. Accepted units cover printed pages 1–189, 191–595; exact topic scopes and exclusions are in [review.yaml](review.yaml).

Terra/high extracts the material; independent Sol/high review precedes each promotion. The end human audit is pending. The whole-book assessment and its resolved or pending amendments are recorded in the reconciliation report. Cross-volume correspondence and shared-graph alignment remain in progress. A listed page range records reviewed scope, not a claim that every topic on a pilot page was extracted.

This graph describes the book independently of any audience, course, or schedule. Textbooks, extracted passages, source-page renderings, and processing records remain private.

[Read the graph](knowledge/graph.yaml) · [Coverage inventory](coverage.yaml) · [Final scientific decisions](adjudications.yaml) · [Whole-book reconciliation](reconciliation.md) · [Shared QFT graph](../../subjects/qft/README.md) · [Graph bank instructions](../../README.md)

The following diagram is a small excerpt from the initial accepted batch. The linked YAML contains the current complete set of accepted records.

```mermaid
flowchart TD
  n0["Charge-conjugation and time-reversal phase constraints"]
  n1["Charge-conservation obstruction for a self-adjoint field"]
  n2["Complex causal scalar field from particle and antiparticle"]
  n3["Hermiticity and spacelike commutation for scalar interactions"]
  n4["Nonzero spacelike mixed commutator"]
  n5["Parity covariance constrains intrinsic parities"]
  n6["Complex scalar-field commutator"]
  n7["Self-adjoint causal scalar field"]
  n8["Scalar Lorentz representation and zero spin"]
  n9["Bosonic statistics and particle-antiparticle mass equality"]
  n1 -.->|pedagogical| n2
  n2 -->|prerequisite| n0
  n2 -->|prerequisite| n6
  n2 -->|prerequisite| n5
  n3 -->|prerequisite| n4
  n4 -->|prerequisite| n7
  n4 -->|prerequisite| n9
  n7 -.->|evidence| n1
  n8 -->|prerequisite| n7
  n9 -->|prerequisite| n2
```

The diagram omits mastery levels and detailed qualifications for readability; the YAML preserves the evidence, necessity, rationale, and failure mode for every relationship. Textbooks and quotation checks remain local.
