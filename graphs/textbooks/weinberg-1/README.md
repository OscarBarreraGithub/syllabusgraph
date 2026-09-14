# The Quantum Theory of Fields, Volume I: Foundations

**Partial, model-reviewed graph:** 10 concepts and 10 relationships from printed pages 201–206.

Causal scalar fields: scalar Lorentz transformation behavior, the relation between annihilation and creation pieces, spacelike commutation, the real and charged scalar cases, and the resulting particle-antiparticle constraints.

Terra/high extracted this batch; Sol/high independently reviewed it before promotion. The end human audit is pending. See [review.yaml](review.yaml) for exact scope, content digests, and omissions.

This graph describes the book independently of any audience, course, or schedule. Earlier supporting sections and the rest of the textbook are not yet extracted.

[Read the graph](knowledge/graph.yaml) · [Shared QFT graph](../../subjects/qft/README.md) · [Graph bank instructions](../../README.md)

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
