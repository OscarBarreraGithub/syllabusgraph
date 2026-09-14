# Quantum field theory graph collection

**Construction in progress:** four independent textbook graphs currently contain 1580 reviewed concepts. The shared graph contains 97 concepts and 70 relationships, mapping 104 distinct book concepts through explicit origins.

Terra/high performs extraction and alignment; independent Sol/high review precedes promotion. These are **partial graphs**, with an end human audit pending. Shared alignment covers the bounded book inputs recorded in review.yaml; other accepted book additions remain to be aligned. Full-book coverage, global reconciliation, and that alignment must finish before calling this collection complete.

| Book graph | Printed pages in accepted units | Concepts | Relationships |
|---|---|---:|---:|
| [Peskin–Schroeder](../../textbooks/peskin-schroeder/README.md) | 3–263, 265–345, 347–391, 393–471, 473–544 | 425 | 619 |
| [Schwartz](../../textbooks/schwartz/README.md) | 3–105, 109–284, 287–477 | 457 | 575 |
| [Weinberg I](../../textbooks/weinberg-1/README.md) | 1–189, 191–498 | 419 | 555 |
| [Weinberg II](../../textbooks/weinberg-2/README.md) | 1–59, 63–247, 252–358 | 279 | 327 |

The reviewed inventories account for 2,646 substantive numbered pages and 605 section entries. Accepted full extraction scopes currently cover 1828 of those pages; narrow pilots are excluded from that measure. Each book README links its complete inventory and remaining ranges. These counts track progress; the final conceptual-coverage and dependency audit is still pending. [Read the final inventory decision](review-decisions.yaml).

[Read the shared graph](knowledge/graph.yaml) · [Coverage and review record](review.yaml) · [Final scientific decisions](adjudications.yaml) · [Graph bank instructions](../../README.md)

## Correspondences in reviewed portions

A shared node's `origins` identify the book concepts it represents and explain the scope of the match. Related treatments can remain distinct: these counts measure explicit shared-node correspondences, not every conceptual similarity. Imported textbook inputs remain traceable in origins but do not count as independent treatments by the importing book.

| Book pair | Shared concepts in extracted portions |
|---|---:|
| Peskin–Schroeder / Schwartz | 12 |
| Peskin–Schroeder / Weinberg I | 0 |
| Peskin–Schroeder / Weinberg II | 0 |
| Schwartz / Weinberg I | 0 |
| Schwartz / Weinberg II | 0 |
| Weinberg I / Weinberg II | 0 |

**These numbers are not whole-book overlap estimates.** The reviewed inputs cover different portions of the subject. A zero means no shared-node mapping in the aligned inputs; it does not mean either book omits the topic.

Examples of the mapped concepts (the YAML contains every correspondence):

| Shared concept | Book origins |
|---|---|
| Canonical momentum and Hamiltonian for a field (`qft.canonical-field-momentum-hamiltonian`) | Peskin–Schroeder: `peskin-schroeder.canonical-field-momentum-hamiltonian`; Schwartz: `schwartz.classical-field-hamiltonian-lagrangian-legendre-transform`; Schwartz: `schwartz.canonical-scalar-field-energy-density` |
| Complex scalar U(1) current (`qft.complex-scalar-u1-current`) | Peskin–Schroeder: `peskin-schroeder.complex-scalar-u1-current`; Schwartz: `schwartz.noether-current-and-conserved-charge`; Schwartz: `schwartz.complex-scalar-global-u1-symmetry` |
| Equal-time canonical commutators of a scalar field (`qft.equal-time-scalar-field-commutators`) | Peskin–Schroeder: `peskin-schroeder.canonical-quantization-real-field`; Schwartz: `schwartz.equal-time-scalar-field-commutation-relations` |
| Field Euler-Lagrange equation (`qft.field-euler-lagrange-equation`) | Peskin–Schroeder: `peskin-schroeder.field-euler-lagrange-equation`; Schwartz: `schwartz.euler-lagrange-and-klein-gordon-equations` |
| Klein-Gordon canonical Hamiltonian (`qft.klein-gordon-canonical-hamiltonian`) | Peskin–Schroeder: `peskin-schroeder.klein-gordon-canonical-hamiltonian`; Schwartz: `schwartz.canonical-scalar-field-energy-density` |
| Classical Klein-Gordon equation (`qft.klein-gordon-classical-equation`) | Peskin–Schroeder: `peskin-schroeder.klein-gordon-classical-equation`; Schwartz: `schwartz.euler-lagrange-and-klein-gordon-equations` |
| Klein-Gordon Fourier modes as harmonic oscillators (`qft.klein-gordon-fourier-oscillator-modes`) | Peskin–Schroeder: `peskin-schroeder.klein-gordon-fourier-oscillator-modes`; Schwartz: `schwartz.massless-field-plane-wave-oscillator-modes` |
| Local field action (`qft.local-field-action`) | Peskin–Schroeder: `peskin-schroeder.local-field-action`; Schwartz: `schwartz.action-variation-and-boundary-assumption` |
| Noether current and conserved charge (`qft.noether-current-and-conserved-charge`) | Peskin–Schroeder: `peskin-schroeder.noether-current-and-charge`; Schwartz: `schwartz.noether-current-and-conserved-charge` |
| Real Klein-Gordon Lagrangian (`qft.real-klein-gordon-lagrangian`) | Peskin–Schroeder: `peskin-schroeder.real-klein-gordon-lagrangian`; Schwartz: `schwartz.euler-lagrange-and-klein-gordon-equations` |
| Relativistic field viewpoint (`qft.relativistic-field-viewpoint`) | Peskin–Schroeder: `peskin-schroeder.relativistic-field-viewpoint`; Schwartz: `schwartz.relativistic-energy-allows-particle-production` |
| Translation symmetry and energy-momentum tensor (`qft.translation-symmetry-and-energy-momentum-tensor`) | Peskin–Schroeder: `peskin-schroeder.translation-stress-energy-tensor`; Schwartz: `schwartz.translation-symmetry-and-canonical-energy-momentum-tensor` |

Each book README includes a diagram. The YAML retains equations/notation, evidence, mastery requirements, necessity, and source-specific route qualifications. The shared graph is a synthesis; book graphs retain their own organizing groups and motivations.

## One shared result, distinct routes

The shared graph separates a physical result from source-specific methods for reaching it. This view is generated from the reviewed graph; dashed edges mark alternative routes, while solid edges retain prerequisites within a route.

```mermaid
flowchart LR
  r0["Peskin–Schroeder: Canonical momentum and Hamiltonian for a field"]
  r1["Shared result: Equal-time canonical commutators of a scalar field"]
  r2["Schwartz: Free scalar field as a momentum-mode expansion"]
  r3["Schwartz: Momentum-mode creation and annihilation algebra"]
  r4["Peskin–Schroeder: Canonical quantization prescription"]
  r5["Schwartz: Derive commutators from modes"]
  r4 -.->|alternative| r1
  r0 -->|prerequisite| r4
  r5 -.->|alternative| r1
  r2 -->|prerequisite| r5
  r3 -->|prerequisite| r5
  r3 -->|prerequisite| r2
```

The illustrated result uses two explicit method nodes because the book records combine a route with its result. Shared nodes can merge equivalent book concepts or separate distinct derivation routes, so shared and input counts need not match. The current course planner does not choose an alternative route automatically; that choice belongs to the later course-design work.

## Reuse and continuation

```bash
syllabusgraph validate -p graphs/subjects/qft
python scripts/check_graph_bank.py
```

These commands work from a clone without textbooks, private caches, or a model account. Extending the graphs requires access to the cited material and the usual independent review. Put references in a project's ignored `materials/` directory; extraction records and quote witnesses stay in `.syllabusgraph/`. See the [PDF reading guide](../../../docs/pdf-reading.md) for adaptable setup.

Continue by extracting further bounded textbook sections, retaining each book's treatment and reviewing new correspondences. Coleman and Weinberg III are outside this initial scope. QFT I/II course design follows graph construction; the [roadmap](../../../docs/roadmap.md) records the task of identifying the right questions about goals, background, depth, time, and assessment.
