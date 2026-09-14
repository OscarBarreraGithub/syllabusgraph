# The Quantum Theory of Fields, Volume II: Modern Applications

**Partial, model-reviewed graph:** 10 concepts and 10 relationships from printed pages 2–7.

Opening non-Abelian gauge-theory construction: local matter-field transformations, Lie-algebra generators and structure constants, covariant derivatives, field strength, and the first gauge-theory Lagrangian ingredients.

Terra/high extracted this batch; Sol/high independently reviewed it before promotion. The end human audit is pending. See [review.yaml](review.yaml) for exact scope, content digests, and omissions.

This graph describes the book independently of any audience, course, or schedule. Earlier supporting sections and the rest of the textbook are not yet extracted.

[Read the graph](knowledge/graph.yaml) · [Shared QFT graph](../../subjects/qft/README.md) · [Graph bank instructions](../../README.md)

```mermaid
flowchart TD
  n0["Adjoint representation from structure constants"]
  n1["Covariant derivative of matter fields"]
  n2["Finite gauge transformations"]
  n3["Gauge-field terms and mass restriction"]
  n4["Inhomogeneous gauge-field transformation"]
  n5["Gauge-covariant ingredients for a Lagrangian"]
  n6["Lie-algebra generators and structure constants"]
  n7["Local infinitesimal transformations of matter fields"]
  n8["Non-Abelian field strength from covariant-derivative commutators"]
  n9["Pure gauge and the flatness criterion"]
  n0 -->|prerequisite| n4
  n1 -->|prerequisite| n8
  n1 -->|prerequisite| n5
  n8 -->|prerequisite| n5
  n8 -->|prerequisite| n9
  n4 -->|prerequisite| n1
  n5 -->|prerequisite| n3
  n7 -->|prerequisite| n4
  n7 -.->|evidence| n6
  n6 -->|prerequisite| n0
```

The diagram omits mastery levels and detailed qualifications for readability; the YAML preserves the evidence, necessity, rationale, and failure mode for every relationship. Textbooks and quotation checks remain local.
