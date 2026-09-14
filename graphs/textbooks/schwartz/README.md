# Quantum Field Theory and the Standard Model

**Partial, model-reviewed graph:** 7 concepts and 7 relationships from printed pages 21–26.

Free scalar-field quantization through the Fock-space description, creation and annihilation operators, field expansion, time evolution, and equal-time commutation relations, with the short closing application kept only as context for the quantum-field description.

Terra/high extracted this batch; Sol/high independently reviewed it before promotion. The end human audit is pending. See [review.yaml](review.yaml) for exact scope, content digests, and omissions.

This graph describes the book independently of any audience, course, or schedule. Earlier supporting sections and the rest of the textbook are not yet extracted.

[Read the graph](knowledge/graph.yaml) · [Shared QFT graph](../../subjects/qft/README.md) · [Graph bank instructions](../../README.md)

```mermaid
flowchart TD
  n0["Equal-time scalar-field commutation relations"]
  n1["Fock space and physical particle sectors"]
  n2["Free scalar field as a momentum-mode expansion"]
  n3["Heisenberg evolution of a free scalar field"]
  n4["Momentum-mode creation and annihilation algebra"]
  n5["One-particle wavefunction and nonrelativistic limit"]
  n6["One-particle position state from a field operator"]
  n2 -->|prerequisite| n0
  n2 -->|prerequisite| n6
  n3 -->|prerequisite| n5
  n4 -->|prerequisite| n0
  n4 -->|prerequisite| n3
  n4 -->|prerequisite| n2
  n4 -->|prerequisite| n6
```

The diagram omits mastery levels and detailed qualifications for readability; the YAML preserves the evidence, necessity, rationale, and failure mode for every relationship. Textbooks and quotation checks remain local.
