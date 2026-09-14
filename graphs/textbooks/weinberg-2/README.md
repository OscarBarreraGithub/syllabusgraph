# The Quantum Theory of Fields, Volume II: Modern Applications

**Partial, model-reviewed graph:** 44 concepts and 39 relationships. Accepted units cover printed pages 2–40; exact topic scopes and exclusions are in [review.yaml](review.yaml).

Terra/high extracts the material; independent Sol/high review precedes each promotion. The end human audit is pending. Full-book construction and cross-unit dependency reconciliation are in progress. A listed page range records reviewed scope, not a claim that every topic on a pilot page was extracted.

This graph describes the book independently of any audience, course, or schedule. Textbooks, extracted passages, source-page renderings, and processing records remain private.

[Read the graph](knowledge/graph.yaml) · [Shared QFT graph](../../subjects/qft/README.md) · [Graph bank instructions](../../README.md)

The following diagram is a small excerpt from the initial accepted batch. The linked YAML contains the current complete set of accepted records.

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
