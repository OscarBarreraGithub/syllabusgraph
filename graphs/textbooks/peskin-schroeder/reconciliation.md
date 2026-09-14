# Whole-book graph reconciliation

This report records a review of the combined textbook graph after all its source scopes were accepted. Terra/high assessed semantic section coverage, cross-unit dependencies, independent routes, and proof limits. Sol/high independently reviewed that assessment and made the final recorded decision.

The audited baseline contains **634 nodes, 844 edges, and 146 inventory sections**. It is identified by the graph-content digest below. Subsequent source-backed amendments are listed separately; this snapshot is not an automatic review of arbitrary later changes.

`sha256:08a1eb5357568887c3c37eba00d8d4706ee61ca09eaa0e92756b7b3ffd9c722d`

The end human audit is **pending**. Shared-graph alignment and cross-volume follow-ups remain separate from this book's audit. See the current [review declaration](review.yaml), [coverage ledger](coverage.yaml), and [scientific decision log](adjudications.yaml).

## Findings and source-backed amendments

No graph amendment remains from this accepted whole-book audit.

## Audit decisions

**The audit treats necessity=necessary on an alternative edge as planner-enforced, falsely making the optional Chapter 9 Wick route compulsory..** Remove the issue and dependent audit language; retain the alternative edge because it is noncompulsory and necessary only within its optional route.

The first alternative matches both the graph semantics and the source. src/syllabusgraph/planner.py lines 134-138 selects only relation=prerequisite before filtering necessity, while docs/project-format.md lines 103-108 says alternative edges record available routes that the planner does not automatically choose or enforce. Peskin-Schroeder pp. 88-89 establish the operator Wick theorem. Page 288 independently reproduces its pairing result through direct Gaussian integration, and pp. 289-292 introduce the generating-functional method as a further route whose repeated differentiation uses the free Z[J]. The edge peskin-schroeder.free-z-to-gaussian-wick therefore records an input required within that optional route; it cannot force Chapter 9 into prerequisite closure. Removing the report issue preserves all 634 nodes, 844 edges, 146 section mappings, convention records, and qualified proof boundaries. The independently verified printed-page 471 and 779 divider classifications also remain supported without graph nodes or denominator changes.

Alternatives considered: Remove the mistaken audit issue and retain the accepted alternative edge unchanged. / Keep the issue and dispatch a source amendment to lower necessity or remodel the route.

## Cross-unit assessment

- All 634 node IDs and 844 edge IDs were inspected in the frozen graph. The repeated-label mechanical index is empty; its 602 unmapped-node pointers were treated as review pointers, not defects.
- The Chapter 2 scalar-field, Chapter 3 spinor, Chapter 4 interaction/LSZ, Chapter 5 scattering, Chapter 7 Ward/LSZ, Chapter 10 renormalization, Chapter 15 gauge-geometry, Chapters 17–18 QCD/OPE, Chapters 19–21 anomaly/Higgs/gauge-quantization, and Appendix reference dependencies are represented by explicit source-backed prerequisites where the later derivation actually uses them. Textbook order alone was not treated as necessity.
- Substantial problems and projects are retained as branch records with their own inputs. The inspection found no exercise answer used as a necessary premise in those branches; accepted final-unit decisions already removed the formerly circular and duplicate cases.
- Independent routes are explicit for Mott scattering, helicity calculations, the ABJ anomaly, Goldstone equivalence, elementary versus composite Higgs outcomes, and the other listed alternative edges. All 26 alternative edges remain noncompulsory because alternative relations do not drive planner closure; each route retains its own actual inputs.
- The Chapter 19 ABJ point-split, triangle, and measure routes and the Chapter 21 Ward and cut routes each retain their own actual inputs. No route is inferred merely from shared chronology or labels.
- No redundant concept was identified merely because two records cite the same page or because a chapter roll-up overlaps subsection evidence. The review distinguished source-specific derivations, results, and representations when their instructional use differs.

## Conventions and proof boundaries

The retained xix–xxi frontmatter records preserve metric/index/orientation, Dirac normalization, operators and distributions, Fourier factors, and electromagnetic-unit conventions. They are source-specific evidence and are not treated as new physics nodes.

Records: `peskin-schroeder.minkowski-index-and-orientation-conventions`, `peskin-schroeder.chiral-dirac-basis-and-relativistic-normalization-declaration`, `peskin-schroeder.one-particle-operator-pauli-and-distribution-conventions`, `peskin-schroeder.fourier-transform-normalization-conventions`, `peskin-schroeder.heaviside-lorentz-electrodynamics-conventions`.

Appendix records retain diagram signs and arrows, external-state conventions, dimensional-regularization branches, ghost/Yang–Mills rules, and numerator/group identities. These are kept distinct from derivational concepts to avoid silently harmonizing conventions.

Records: `peskin-schroeder.appendix-diagrammatic-conventions`, `peskin-schroeder.appendix-external-particle-and-polarization-conventions`, `peskin-schroeder.appendix-dimensional-regularization-branch-prescription`, `peskin-schroeder.appendix-nonabelian-and-ghost-rule-table`, `peskin-schroeder.appendix-numerator-algebra-and-group-identities`.

The general spin-statistics theorem is retained as a source-stated result under its listed assumptions; this corpus does not claim its full proof.

Records: `peskin-schroeder.spin-statistics-theorem-stated-assumptions`.

The early physical-polarization argument remains qualified and points to the later Ward treatment; it is not credited with a proof beyond its stated scope.

Records: `peskin-schroeder.ward-identity-external-photon-polarization-sum`, `peskin-schroeder.qed-feynman-rules-and-physical-polarizations`.

The graph preserves the source's use of infrared cancellation/exponentiation and QCD on-shell RG while retaining the stated technical proof boundaries.

Records: `peskin-schroeder.soft-virtual-photon-exponentiation`, `peskin-schroeder.qcd-on-shell-rg-infrared-proof-boundary`.

These records state the bounded effective-action and R-xi claims with their assumptions; no external proof is invented.

Records: `peskin-schroeder.effective-action-varying-background-proof-boundary`, `peskin-schroeder.rxi-gauge-limits-and-proof-boundary`.

Reported strong-coupling, exact-model, and original-source results retain attribution and scope rather than being presented as derivations completed by this book graph.

Records: `peskin-schroeder.qcd-strong-coupling-color-confinement`, `peskin-schroeder.schwinger-model-photon-mass`, `peskin-schroeder.two-dimensional-conformal-fixed-points-and-wzw-example`.

Source-era phenomenological routes remain qualified descriptions of the text's alternatives, not current empirical claims or external proofs.

Records: `peskin-schroeder.broken-supersymmetry-source-era-hierarchy-route`, `peskin-schroeder.composite-higgs-source-era-route`.

## Section coverage assessment

These mappings follow the accepted records' section evidence and content. A shared boundary page may contribute to multiple sections; a table number does not determine its section.

<details>
<summary>Section 1 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: High-energy center-of-mass muon-pair setup; Coherent addition of allowed diagram amplitudes; Helicity and angular-momentum selection in pair annihilation; Infrared-inclusive final-state requirement.

Records: `peskin-schroeder.cm-high-energy-muon-pair-setup`, `peskin-schroeder.coherent-sum-of-diagram-amplitudes`, `peskin-schroeder.helicity-angular-momentum-selection`, `peskin-schroeder.infrared-inclusive-final-states`, `peskin-schroeder.loop-momentum-integration-and-divergence`, `peskin-schroeder.photon-mediated-second-order-amplitude`, `peskin-schroeder.qed-diagrammatic-calculation`, `peskin-schroeder.qed-tree-amplitude-rule`, `peskin-schroeder.tree-level-muon-pair-cross-section`, `peskin-schroeder.unpolarized-trace-technology`.

</details>

<details>
<summary>Section 2 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Antiparticles in the complex-scalar causality cancellation; Canonical momentum and Hamiltonian for a field; Canonical quantization of the real field; Particle creation by a finite-time classical source.

Records: `peskin-schroeder.antiparticle-causality-cancellation`, `peskin-schroeder.canonical-field-momentum-hamiltonian`, `peskin-schroeder.canonical-quantization-real-field`, `peskin-schroeder.classical-source-on-shell-particle-creation`, `peskin-schroeder.complex-scalar-u1-current`, `peskin-schroeder.feynman-scalar-propagator`, `peskin-schroeder.field-euler-lagrange-equation`, `peskin-schroeder.free-field-perturbative-foundation`, `peskin-schroeder.heisenberg-klein-gordon-field`, `peskin-schroeder.kg-ladder-mode-expansion`, `peskin-schroeder.klein-gordon-canonical-hamiltonian`, `peskin-schroeder.klein-gordon-classical-equation`, `peskin-schroeder.klein-gordon-fourier-oscillator-modes`, `peskin-schroeder.local-field-action`, `peskin-schroeder.local-field-particle-creation`, `peskin-schroeder.lorentz-invariant-one-particle-normalization`, `peskin-schroeder.microcausality-field-commutator`, `peskin-schroeder.noether-current-and-charge`, `peskin-schroeder.real-klein-gordon-lagrangian`, `peskin-schroeder.relativistic-field-viewpoint`, `peskin-schroeder.retarded-klein-gordon-green-function`, `peskin-schroeder.scalar-bose-einstein-statistics`, `peskin-schroeder.scalar-fock-spectrum`, `peskin-schroeder.spacelike-wightman-amplitude`, `peskin-schroeder.translation-stress-energy-tensor`.

</details>

<details>
<summary>Section 2.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Relativistic field viewpoint.

Records: `peskin-schroeder.relativistic-field-viewpoint`.

</details>

<details>
<summary>Section 2.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Canonical momentum and Hamiltonian for a field; Complex scalar U(1) current; Field Euler-Lagrange equation; Klein-Gordon canonical Hamiltonian.

Records: `peskin-schroeder.canonical-field-momentum-hamiltonian`, `peskin-schroeder.complex-scalar-u1-current`, `peskin-schroeder.field-euler-lagrange-equation`, `peskin-schroeder.klein-gordon-canonical-hamiltonian`, `peskin-schroeder.klein-gordon-classical-equation`, `peskin-schroeder.local-field-action`, `peskin-schroeder.noether-current-and-charge`, `peskin-schroeder.real-klein-gordon-lagrangian`, `peskin-schroeder.translation-stress-energy-tensor`.

</details>

<details>
<summary>Section 2.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Canonical quantization of the real field; Klein-Gordon ladder-operator mode expansion; Klein-Gordon Fourier modes as harmonic oscillators; Field operator creates a localized one-particle superposition.

Records: `peskin-schroeder.canonical-quantization-real-field`, `peskin-schroeder.kg-ladder-mode-expansion`, `peskin-schroeder.klein-gordon-fourier-oscillator-modes`, `peskin-schroeder.local-field-particle-creation`, `peskin-schroeder.lorentz-invariant-one-particle-normalization`, `peskin-schroeder.scalar-bose-einstein-statistics`, `peskin-schroeder.scalar-fock-spectrum`, `peskin-schroeder.translation-stress-energy-tensor`.

</details>

<details>
<summary>Section 2.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Antiparticles in the complex-scalar causality cancellation; Particle creation by a finite-time classical source; Feynman scalar propagator and time ordering; Free field as the basis of perturbation theory.

Records: `peskin-schroeder.antiparticle-causality-cancellation`, `peskin-schroeder.classical-source-on-shell-particle-creation`, `peskin-schroeder.feynman-scalar-propagator`, `peskin-schroeder.free-field-perturbative-foundation`, `peskin-schroeder.heisenberg-klein-gordon-field`, `peskin-schroeder.microcausality-field-commutator`, `peskin-schroeder.retarded-klein-gordon-green-function`, `peskin-schroeder.spacelike-wightman-amplitude`.

</details>

<details>
<summary>Section 2.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Particle creation by a finite-time classical source; Complex scalar quantization: two charged particle species; Internal symmetry of identical complex scalar fields; Improved electromagnetic stress-energy tensor.

Records: `peskin-schroeder.classical-source-on-shell-particle-creation`, `peskin-schroeder.complex-scalar-canonical-particles-and-charge`, `peskin-schroeder.identical-complex-scalars-internal-symmetry`, `peskin-schroeder.improved-electromagnetic-stress-energy`, `peskin-schroeder.maxwell-variational-field-equations`, `peskin-schroeder.spacelike-wightman-amplitude`.

</details>

<details>
<summary>Section 3 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Canonical Dirac momentum and Hamiltonian; Charge conjugation, bilinear signs, and CPT; Chiral U(1) symmetry and handed currents; Dirac adjoint and free Dirac Lagrangian.

Records: `peskin-schroeder.canonical-dirac-momentum-and-hamiltonian`, `peskin-schroeder.charge-conjugation-bilinears-and-cpt`, `peskin-schroeder.chiral-u1-symmetry-and-handed-currents`, `peskin-schroeder.dirac-adjoint-and-free-lagrangian`, `peskin-schroeder.dirac-bilinear-lorentz-basis`, `peskin-schroeder.dirac-clifford-algebra-generators`, `peskin-schroeder.dirac-local-field-particle-creation`, `peskin-schroeder.dirac-momentum-space-and-feynman-propagator`, `peskin-schroeder.dirac-noether-angular-momentum-spin`, `peskin-schroeder.dirac-positive-frequency-spinors`, `peskin-schroeder.dirac-retarded-propagator-from-anticommutator`, `peskin-schroeder.dirac-spin-sum-completeness`, `peskin-schroeder.dirac-spinor-and-covariant-equation`, `peskin-schroeder.dirac-u-v-normalization`, `peskin-schroeder.dirac-u1-charge`, `peskin-schroeder.dirac-vector-and-axial-currents`, `peskin-schroeder.discrete-lorentz-components-and-cpt-status`, `peskin-schroeder.fermionic-anticommutator-causality`, `peskin-schroeder.fermionic-ladder-operators-and-statistics`, `peskin-schroeder.helicity-and-massless-weyl-solutions`, `peskin-schroeder.lorentz-action-on-quantized-dirac-field`, `peskin-schroeder.lorentz-covariance-field-law`, `peskin-schroeder.lorentz-representations-and-generators`, `peskin-schroeder.naive-dirac-commutator-instability`, `peskin-schroeder.parity-dirac-field-bilinears-and-bound-states`, `peskin-schroeder.quantized-dirac-field-expansion`, `peskin-schroeder.rapidity-boosted-dirac-spinors`, `peskin-schroeder.spin-statistics-theorem-stated-assumptions`, `peskin-schroeder.time-reversal-antiunitary-dirac-symmetry`, `peskin-schroeder.weyl-fierz-rearrangement`, `peskin-schroeder.weyl-spinors-and-chiral-mass-mixing`.

</details>

<details>
<summary>Section 3.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Lorentz covariance from field transformation laws; Finite-dimensional Lorentz representations and generators.

Records: `peskin-schroeder.lorentz-covariance-field-law`, `peskin-schroeder.lorentz-representations-and-generators`.

</details>

<details>
<summary>Section 3.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Dirac adjoint and free Dirac Lagrangian; Dirac Clifford algebra and spinor Lorentz generators; Dirac spinor and covariant first-order equation; Finite-dimensional Lorentz representations and generators.

Records: `peskin-schroeder.dirac-adjoint-and-free-lagrangian`, `peskin-schroeder.dirac-clifford-algebra-generators`, `peskin-schroeder.dirac-spinor-and-covariant-equation`, `peskin-schroeder.lorentz-representations-and-generators`, `peskin-schroeder.weyl-spinors-and-chiral-mass-mixing`.

</details>

<details>
<summary>Section 3.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Positive-frequency free Dirac spinors; Dirac spin-sum completeness relations; u and v solution normalization; Helicity and the massless Weyl limit.

Records: `peskin-schroeder.dirac-positive-frequency-spinors`, `peskin-schroeder.dirac-spin-sum-completeness`, `peskin-schroeder.dirac-u-v-normalization`, `peskin-schroeder.helicity-and-massless-weyl-solutions`, `peskin-schroeder.rapidity-boosted-dirac-spinors`.

</details>

<details>
<summary>Section 3.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Chiral U(1) symmetry and handed currents; Lorentz classification of Dirac bilinears; Dirac spin-sum completeness relations; Vector and axial Dirac currents.

Records: `peskin-schroeder.chiral-u1-symmetry-and-handed-currents`, `peskin-schroeder.dirac-bilinear-lorentz-basis`, `peskin-schroeder.dirac-spin-sum-completeness`, `peskin-schroeder.dirac-vector-and-axial-currents`, `peskin-schroeder.weyl-fierz-rearrangement`.

</details>

<details>
<summary>Section 3.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Canonical Dirac momentum and Hamiltonian; Local Dirac fields create particle states; Momentum-space and Feynman Dirac propagator; Noether angular momentum and spin one-half.

Records: `peskin-schroeder.canonical-dirac-momentum-and-hamiltonian`, `peskin-schroeder.dirac-local-field-particle-creation`, `peskin-schroeder.dirac-momentum-space-and-feynman-propagator`, `peskin-schroeder.dirac-noether-angular-momentum-spin`, `peskin-schroeder.dirac-retarded-propagator-from-anticommutator`, `peskin-schroeder.dirac-u1-charge`, `peskin-schroeder.fermionic-anticommutator-causality`, `peskin-schroeder.fermionic-ladder-operators-and-statistics`, `peskin-schroeder.lorentz-action-on-quantized-dirac-field`, `peskin-schroeder.naive-dirac-commutator-instability`, `peskin-schroeder.quantized-dirac-field-expansion`, `peskin-schroeder.spin-statistics-theorem-stated-assumptions`, `peskin-schroeder.weyl-fierz-rearrangement`.

</details>

<details>
<summary>Section 3.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Charge conjugation, bilinear signs, and CPT; P, T, C, and disconnected Lorentz components; Parity of Dirac fields, bilinears, and fermion-antifermion bound states; Antiunitary time reversal for Dirac fermions.

Records: `peskin-schroeder.charge-conjugation-bilinears-and-cpt`, `peskin-schroeder.discrete-lorentz-components-and-cpt-status`, `peskin-schroeder.parity-dirac-field-bilinears-and-bound-states`, `peskin-schroeder.time-reversal-antiunitary-dirac-symmetry`.

</details>

<details>
<summary>Section 3.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Charge conjugation, bilinear signs, and CPT; Problem: complex-scalar P, C, T, and CPT exercise; Problem: tensor-bilinear P, C, and T transformations; Problem: rewrite a Dirac field as two Weyl fields.

Records: `peskin-schroeder.charge-conjugation-bilinears-and-cpt`, `peskin-schroeder.problem-complex-scalar-discrete-symmetries`, `peskin-schroeder.problem-dirac-tensor-discrete-symmetries`, `peskin-schroeder.problem-dirac-two-weyl-rewrite`, `peskin-schroeder.problem-free-supersymmetric-multiplet`, `peskin-schroeder.problem-general-dirac-fierz-coefficients`, `peskin-schroeder.problem-gordon-identity`, `peskin-schroeder.problem-grassmann-majorana-action`, `peskin-schroeder.problem-lorentz-su2-times-su2`, `peskin-schroeder.problem-majorana-current-comparison`, `peskin-schroeder.problem-majorana-quantization`, `peskin-schroeder.problem-majorana-two-component-equation`, `peskin-schroeder.problem-massless-spinor-helicity-products`, `peskin-schroeder.problem-positronium-cp-selection-rules`, `peskin-schroeder.problem-superpotential-interactions`.

</details>

<details>
<summary>Section 4 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Adiabatic projection onto the interacting vacuum; Breit-Wigner width, rest-frame decay rate, and time dilation; Connected, amputated S-matrix prescription; Coulomb potential and exchanged-spin force pattern.

Records: `peskin-schroeder.adiabatic-interacting-vacuum-projection`, `peskin-schroeder.breit-wigner-resonance-width-and-time-dilation`, `peskin-schroeder.connected-amputated-s-matrix-prescription`, `peskin-schroeder.coulomb-potential-and-exchange-spin-pattern`, `peskin-schroeder.cross-section-and-decay-observables`, `peskin-schroeder.fermion-line-flow-and-closed-loop-sign`, `peskin-schroeder.fermionic-wick-sign-convention`, `peskin-schroeder.feynman-diagram-representation`, `peskin-schroeder.gauge-field-quantization-obstruction-and-gauge-tradeoff`, `peskin-schroeder.in-out-states-s-t-and-invariant-matrix-element`, `peskin-schroeder.interacting-correlation-function-quotient`, `peskin-schroeder.interaction-picture-dyson-series`, `peskin-schroeder.local-interaction-hamiltonian`, `peskin-schroeder.lorentz-invariant-phase-space-cross-section`, `peskin-schroeder.perturbative-interaction-expansion`, `peskin-schroeder.phi4-momentum-space-feynman-rules`, `peskin-schroeder.phi4-odd-correlation-vanishing`, `peskin-schroeder.phi4-position-space-feynman-rules`, `peskin-schroeder.phi4-symmetry-factors`, `peskin-schroeder.phi4-tree-level-2to2-scattering`, `peskin-schroeder.power-counting-renormalizable-interactions`, `peskin-schroeder.qed-feynman-rules-and-physical-polarizations`, `peskin-schroeder.qed-from-yukawa-analogy`, `peskin-schroeder.qed-minimal-coupling-and-local-gauge-symmetry`, `peskin-schroeder.scalar-wick-theorem`, `peskin-schroeder.vacuum-bubble-exponentiation-and-cancellation`, `peskin-schroeder.yukawa-feynman-rules`, `peskin-schroeder.yukawa-potential-from-nonrelativistic-exchange`.

</details>

<details>
<summary>Section 4.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Gauge-field canonical obstruction and gauge-choice tradeoff; Local interaction Hamiltonian and phi-four model; Power counting for renormalizable interactions; QED minimal coupling and local gauge symmetry.

Records: `peskin-schroeder.gauge-field-quantization-obstruction-and-gauge-tradeoff`, `peskin-schroeder.local-interaction-hamiltonian`, `peskin-schroeder.power-counting-renormalizable-interactions`, `peskin-schroeder.qed-minimal-coupling-and-local-gauge-symmetry`.

</details>

<details>
<summary>Section 4.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Adiabatic projection onto the interacting vacuum; Interacting correlation functions as normalized free-vacuum expressions; Interaction-picture evolution and Dyson series; Interaction as a perturbative expansion.

Records: `peskin-schroeder.adiabatic-interacting-vacuum-projection`, `peskin-schroeder.interacting-correlation-function-quotient`, `peskin-schroeder.interaction-picture-dyson-series`, `peskin-schroeder.perturbative-interaction-expansion`.

</details>

<details>
<summary>Section 4.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Scalar Wick theorem and contractions.

Records: `peskin-schroeder.scalar-wick-theorem`.

</details>

<details>
<summary>Section 4.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Feynman diagrams as contraction representations; Momentum-space phi-four Feynman rules; Position-space phi-four Feynman rules; Phi-four diagram symmetry factors.

Records: `peskin-schroeder.feynman-diagram-representation`, `peskin-schroeder.phi4-momentum-space-feynman-rules`, `peskin-schroeder.phi4-position-space-feynman-rules`, `peskin-schroeder.phi4-symmetry-factors`, `peskin-schroeder.vacuum-bubble-exponentiation-and-cancellation`.

</details>

<details>
<summary>Section 4.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Breit-Wigner width, rest-frame decay rate, and time dilation; Cross sections, differential cross sections, and decay rates; In/out states, S and T matrices, and invariant matrix element; Invariant phase space and cross-section formula.

Records: `peskin-schroeder.breit-wigner-resonance-width-and-time-dilation`, `peskin-schroeder.cross-section-and-decay-observables`, `peskin-schroeder.in-out-states-s-t-and-invariant-matrix-element`, `peskin-schroeder.lorentz-invariant-phase-space-cross-section`, `peskin-schroeder.phi4-odd-correlation-vanishing`.

</details>

<details>
<summary>Section 4.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Connected, amputated S-matrix prescription; Invariant phase space and cross-section formula; Tree-level phi-four two-to-two scattering.

Records: `peskin-schroeder.connected-amputated-s-matrix-prescription`, `peskin-schroeder.lorentz-invariant-phase-space-cross-section`, `peskin-schroeder.phi4-tree-level-2to2-scattering`.

</details>

<details>
<summary>Section 4.7 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Connected, amputated S-matrix prescription; Fermion-line particle-number flow and closed-loop sign; Fermionic time ordering, normal ordering, and Wick signs; Yukawa Feynman rules and external spinors.

Records: `peskin-schroeder.connected-amputated-s-matrix-prescription`, `peskin-schroeder.fermion-line-flow-and-closed-loop-sign`, `peskin-schroeder.fermionic-wick-sign-convention`, `peskin-schroeder.yukawa-feynman-rules`, `peskin-schroeder.yukawa-potential-from-nonrelativistic-exchange`.

</details>

<details>
<summary>Section 4.8 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Coulomb potential and exchanged-spin force pattern; Photon polarizations and provisional Lorenz-gauge propagator qualification; Yukawa-to-QED Feynman-rule analogy; Attractive Yukawa potential from scalar exchange.

Records: `peskin-schroeder.coulomb-potential-and-exchange-spin-pattern`, `peskin-schroeder.qed-feynman-rules-and-physical-polarizations`, `peskin-schroeder.qed-from-yukawa-analogy`, `peskin-schroeder.yukawa-potential-from-nonrelativistic-exchange`.

</details>

<details>
<summary>Section 4.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Coulomb potential and exchanged-spin force pattern; Problem: source-created-particle Poisson statistics; Problem: explicit breaking in the linear sigma model; Problem: soft-pion cancellation in the broken linear sigma model.

Records: `peskin-schroeder.coulomb-potential-and-exchange-spin-pattern`, `peskin-schroeder.problem-classical-source-poisson-statistics`, `peskin-schroeder.problem-linear-sigma-explicit-breaking`, `peskin-schroeder.problem-linear-sigma-soft-pion-cancellation`, `peskin-schroeder.problem-linear-sigma-spontaneous-breaking`, `peskin-schroeder.problem-linear-sigma-unbroken-rules`, `peskin-schroeder.problem-rutherford-classical-potential-amplitude`, `peskin-schroeder.problem-rutherford-nonrelativistic-formula`, `peskin-schroeder.problem-scalar-decay-lifetime`.

</details>

<details>
<summary>Section 5 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Bound-state production-decay resonance relation; Compton amplitude from the two fermion-line orderings; Coulomb-ladder resummation produces threshold resonances; Crossing symmetry and crossed-fermion sign.

Records: `peskin-schroeder.bound-state-production-decay-detailed-balance`, `peskin-schroeder.compton-two-diagram-amplitude`, `peskin-schroeder.coulomb-ladder-bound-state-resummation`, `peskin-schroeder.crossing-symmetry-s-matrix`, `peskin-schroeder.dirac-trace-identities-gamma5`, `peskin-schroeder.electron-muon-scattering-cross-section-and-coulomb-pole`, `peskin-schroeder.explicit-helicity-spinor-amplitude-method`, `peskin-schroeder.helicity-projection-trace-method`, `peskin-schroeder.high-energy-compton-helicity-endpoint`, `peskin-schroeder.klein-nishina-and-thomson-limits`, `peskin-schroeder.mandelstam-variables-and-identity`, `peskin-schroeder.massive-muon-pair-cross-section`, `peskin-schroeder.nr-fermion-antifermion-bound-state-vector`, `peskin-schroeder.pointlike-bound-state-wavefunction-at-origin`, `peskin-schroeder.quark-pair-r-ratio`, `peskin-schroeder.s-t-u-channel-classification`, `peskin-schroeder.threshold-muon-pair-spin-triplet-swave`, `peskin-schroeder.two-photon-pair-annihilation-cross-section`, `peskin-schroeder.ward-identity-external-photon-polarization-sum`.

</details>

<details>
<summary>Section 5.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Dirac trace identities, gamma5 traces, and contractions; Massive muon-pair production and threshold behavior; High-energy quark-pair R ratio and color multiplicity.

Records: `peskin-schroeder.dirac-trace-identities-gamma5`, `peskin-schroeder.massive-muon-pair-cross-section`, `peskin-schroeder.quark-pair-r-ratio`.

</details>

<details>
<summary>Section 5.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Explicit ultrarelativistic spinor-amplitude calculation; Helicity-projection trace calculation.

Records: `peskin-schroeder.explicit-helicity-spinor-amplitude-method`, `peskin-schroeder.helicity-projection-trace-method`.

</details>

<details>
<summary>Section 5.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bound-state production-decay resonance relation; Coulomb-ladder resummation produces threshold resonances; Explicit ultrarelativistic spinor-amplitude calculation; Nonrelativistic fermion-antifermion bound-state vector.

Records: `peskin-schroeder.bound-state-production-decay-detailed-balance`, `peskin-schroeder.coulomb-ladder-bound-state-resummation`, `peskin-schroeder.explicit-helicity-spinor-amplitude-method`, `peskin-schroeder.nr-fermion-antifermion-bound-state-vector`, `peskin-schroeder.pointlike-bound-state-wavefunction-at-origin`, `peskin-schroeder.threshold-muon-pair-spin-triplet-swave`.

</details>

<details>
<summary>Section 5.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Coulomb-ladder resummation produces threshold resonances; Crossing symmetry and crossed-fermion sign; Electron-muon scattering cross section and forward Coulomb pole; Mandelstam variables and the four-mass identity.

Records: `peskin-schroeder.coulomb-ladder-bound-state-resummation`, `peskin-schroeder.crossing-symmetry-s-matrix`, `peskin-schroeder.electron-muon-scattering-cross-section-and-coulomb-pole`, `peskin-schroeder.mandelstam-variables-and-identity`, `peskin-schroeder.s-t-u-channel-classification`.

</details>

<details>
<summary>Section 5.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Compton amplitude from the two fermion-line orderings; High-energy Compton backward enhancement and helicity endpoint; Klein-Nishina Compton formula and Thomson limit; Mandelstam variables and the four-mass identity.

Records: `peskin-schroeder.compton-two-diagram-amplitude`, `peskin-schroeder.high-energy-compton-helicity-endpoint`, `peskin-schroeder.klein-nishina-and-thomson-limits`, `peskin-schroeder.mandelstam-variables-and-identity`, `peskin-schroeder.s-t-u-channel-classification`, `peskin-schroeder.two-photon-pair-annihilation-cross-section`, `peskin-schroeder.ward-identity-external-photon-polarization-sum`.

</details>

<details>
<summary>Section 5.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: Bhabha scattering and channel interference; Problem: massive-vector polarization sum from a conserved current; Problem: relativistic Mott Coulomb scattering; Problem: spin-triplet P-wave positronium two-photon decays.

Records: `peskin-schroeder.problem-bhabha-scattering-interference`, `peskin-schroeder.problem-massive-vector-polarization-sum`, `peskin-schroeder.problem-mott-coulomb-scattering`, `peskin-schroeder.problem-positronium-p-wave-two-photon-decays`, `peskin-schroeder.problem-positronium-s-wave-two-photon-lifetime`, `peskin-schroeder.problem-spinor-helicity-photon-polarizations`, `peskin-schroeder.problem-spinor-product-helicity-amplitudes`, `peskin-schroeder.problem-weizsacker-williams-collinear-distribution`, `peskin-schroeder.two-photon-pair-annihilation-cross-section`.

</details>

<details>
<summary>Section 6 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Classical soft-bremsstrahlung spectrum; On-shell electron vertex form factors; Feynman-parameter combination of loop denominators; Charge and magnetic moment from vertex form factors.

Records: `peskin-schroeder.classical-soft-bremsstrahlung-spectrum`, `peskin-schroeder.electron-vertex-form-factor-decomposition`, `peskin-schroeder.feynman-parameter-denominator-combination`, `peskin-schroeder.form-factors-charge-and-magnetic-moment`, `peskin-schroeder.infrared-inclusive-vertex-and-soft-cross-section`, `peskin-schroeder.infrared-singular-dirac-form-factor`, `peskin-schroeder.leading-log-inclusive-soft-exponentiation`, `peskin-schroeder.leading-log-soft-photon-line-factorization`, `peskin-schroeder.one-loop-vertex-form-factors-and-charge-subtraction`, `peskin-schroeder.one-loop-vertex-reduction-to-form-factors`, `peskin-schroeder.pauli-villars-photon-regularization`, `peskin-schroeder.precision-qed-alpha-comparisons`, `peskin-schroeder.radiative-correction-heavy-target-scope`, `peskin-schroeder.schwinger-one-loop-electron-anomalous-moment`, `peskin-schroeder.single-soft-photon-infrared-divergence`, `peskin-schroeder.soft-photon-emission-factorization`, `peskin-schroeder.soft-real-photon-exponentiation`, `peskin-schroeder.soft-virtual-photon-exponentiation`, `peskin-schroeder.sudden-kick-worldline-current`, `peskin-schroeder.wick-rotation-for-convergent-loop-integrals`.

</details>

<details>
<summary>Section 6.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Classical soft-bremsstrahlung spectrum; Heavy-target radiative-correction setup; Single-soft-photon infrared divergence; Soft-photon emission factorization.

Records: `peskin-schroeder.classical-soft-bremsstrahlung-spectrum`, `peskin-schroeder.radiative-correction-heavy-target-scope`, `peskin-schroeder.single-soft-photon-infrared-divergence`, `peskin-schroeder.soft-photon-emission-factorization`, `peskin-schroeder.sudden-kick-worldline-current`.

</details>

<details>
<summary>Section 6.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: On-shell electron vertex form factors; Charge and magnetic moment from vertex form factors; Single-soft-photon infrared divergence.

Records: `peskin-schroeder.electron-vertex-form-factor-decomposition`, `peskin-schroeder.form-factors-charge-and-magnetic-moment`, `peskin-schroeder.single-soft-photon-infrared-divergence`.

</details>

<details>
<summary>Section 6.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Feynman-parameter combination of loop denominators; Regularized one-loop form factors and charge subtraction; One-loop vertex reduction to form factors; Pauli-Villars regularization of the vertex loop.

Records: `peskin-schroeder.feynman-parameter-denominator-combination`, `peskin-schroeder.one-loop-vertex-form-factors-and-charge-subtraction`, `peskin-schroeder.one-loop-vertex-reduction-to-form-factors`, `peskin-schroeder.pauli-villars-photon-regularization`, `peskin-schroeder.precision-qed-alpha-comparisons`, `peskin-schroeder.schwinger-one-loop-electron-anomalous-moment`, `peskin-schroeder.wick-rotation-for-convergent-loop-integrals`.

</details>

<details>
<summary>Section 6.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Infrared-safe inclusive electron-scattering cross section; Infrared-singular Dirac form factor.

Records: `peskin-schroeder.infrared-inclusive-vertex-and-soft-cross-section`, `peskin-schroeder.infrared-singular-dirac-form-factor`.

</details>

<details>
<summary>Section 6.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Infrared-safe inclusive electron-scattering cross section; Leading-log inclusive soft-photon exponentiation; Leading-log soft-photon factorization on external lines; Soft real-photon exponentiation and detector threshold.

Records: `peskin-schroeder.infrared-inclusive-vertex-and-soft-cross-section`, `peskin-schroeder.leading-log-inclusive-soft-exponentiation`, `peskin-schroeder.leading-log-soft-photon-line-factorization`, `peskin-schroeder.soft-real-photon-exponentiation`, `peskin-schroeder.soft-virtual-photon-exponentiation`.

</details>

<details>
<summary>Section 6.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Stated pseudoscalar axion-electron coupling; Polarization-independence assumption in the equivalent-photon approximation; Stated scalar Higgs-electron coupling; Problem: pseudoscalar axion contribution and constraint for electron g minus 2.

Records: `peskin-schroeder.axion-electron-pseudoscalar-coupling-assumption`, `peskin-schroeder.equivalent-photon-polarization-independence-assumption`, `peskin-schroeder.higgs-electron-scalar-coupling-assumption`, `peskin-schroeder.problem-axion-pseudoscalar-gminus2-constraint`, `peskin-schroeder.problem-equivalent-photon-approximation`, `peskin-schroeder.problem-higgs-scalar-gminus2-constraint`, `peskin-schroeder.problem-rosenbluth-elastic-form-factor-cross-section`, `peskin-schroeder.soft-photon-poisson-multiplicity`, `peskin-schroeder.sudakov-form-factor`.

</details>

<details>
<summary>Section 7 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Charge renormalization and momentum-dependent effective coupling; Cutkosky cutting rules for diagram discontinuities; Dimensional regularization for symmetry-preserving loop integrals; Dirac propagator pole residue and physical mass.

Records: `peskin-schroeder.charge-renormalization-and-running-coupling`, `peskin-schroeder.cutkosky-cutting-rules`, `peskin-schroeder.dim-reg-loop-integral-method`, `peskin-schroeder.dirac-pole-residue-and-physical-mass`, `peskin-schroeder.gauge-current-and-ward-identity-distinction`, `peskin-schroeder.kallen-lehmann-spectral-representation`, `peskin-schroeder.lsz-asymptotic-wavepacket-pole-analysis`, `peskin-schroeder.lsz-field-strength-correction-to-form-factor`, `peskin-schroeder.lsz-reduction-from-correlation-functions`, `peskin-schroeder.one-loop-vacuum-polarization-and-pair-threshold`, `peskin-schroeder.optical-theorem-unitarity-relation`, `peskin-schroeder.regulator-must-preserve-ward-identity`, `peskin-schroeder.self-energy-imaginary-part-and-decay-width`, `peskin-schroeder.self-energy-resummation-and-pole-conditions`, `peskin-schroeder.transverse-photon-vacuum-polarization`, `peskin-schroeder.two-point-poles-cuts-and-bound-states`, `peskin-schroeder.uehling-potential-and-vacuum-screening`, `peskin-schroeder.ward-takahashi-correlation-identity`, `peskin-schroeder.ward-vertex-identity-and-z1-z2`.

</details>

<details>
<summary>Section 7.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Dirac propagator pole residue and physical mass; Kallen-Lehmann spectral representation; Self-energy resummation, mass shift, and field-strength residue; Particle poles, multiparticle cuts, and bound-state poles.

Records: `peskin-schroeder.dirac-pole-residue-and-physical-mass`, `peskin-schroeder.kallen-lehmann-spectral-representation`, `peskin-schroeder.self-energy-resummation-and-pole-conditions`, `peskin-schroeder.two-point-poles-cuts-and-bound-states`.

</details>

<details>
<summary>Section 7.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Asymptotic wavepackets and multiparticle pole extraction; LSZ field-strength correction justifies charge subtraction; LSZ reduction from correlation functions; Self-energy resummation, mass shift, and field-strength residue.

Records: `peskin-schroeder.lsz-asymptotic-wavepacket-pole-analysis`, `peskin-schroeder.lsz-field-strength-correction-to-form-factor`, `peskin-schroeder.lsz-reduction-from-correlation-functions`, `peskin-schroeder.self-energy-resummation-and-pole-conditions`.

</details>

<details>
<summary>Section 7.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Cutkosky cutting rules for diagram discontinuities; LSZ field-strength correction justifies charge subtraction; Optical theorem from S-matrix unitarity; Self-energy imaginary part and narrow-resonance width.

Records: `peskin-schroeder.cutkosky-cutting-rules`, `peskin-schroeder.lsz-field-strength-correction-to-form-factor`, `peskin-schroeder.optical-theorem-unitarity-relation`, `peskin-schroeder.self-energy-imaginary-part-and-decay-width`.

</details>

<details>
<summary>Section 7.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Ward-Takahashi identity for QED correlation functions; Ward vertex identity and Z1 equals Z2.

Records: `peskin-schroeder.ward-takahashi-correlation-identity`, `peskin-schroeder.ward-vertex-identity-and-z1-z2`.

</details>

<details>
<summary>Section 7.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Charge renormalization and momentum-dependent effective coupling; Dimensional regularization for symmetry-preserving loop integrals; Gauge symmetry, current conservation, and Ward identity; One-loop vacuum polarization, pair threshold, and unitarity check.

Records: `peskin-schroeder.charge-renormalization-and-running-coupling`, `peskin-schroeder.dim-reg-loop-integral-method`, `peskin-schroeder.gauge-current-and-ward-identity-distinction`, `peskin-schroeder.one-loop-vacuum-polarization-and-pair-threshold`, `peskin-schroeder.regulator-must-preserve-ward-identity`, `peskin-schroeder.transverse-photon-vacuum-polarization`, `peskin-schroeder.uehling-potential-and-vacuum-screening`, `peskin-schroeder.ward-vertex-identity-and-z1-z2`.

</details>

<details>
<summary>Section 7.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: direct phi-four one-loop calculation and optical theorem; Problem: regulator dependence of Z1 equals Z2; Problem: QED plus Yukawa vertex renormalization.

Records: `peskin-schroeder.problem-phi4-one-loop-optical-theorem`, `peskin-schroeder.problem-qed-regulator-comparison`, `peskin-schroeder.problem-yukawa-qed-vertex-renormalization`.

</details>

<details>
<summary>Section 7.project — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Project: inclusive quark-pair plus gluon cross section; Gluon-jet project model and infrared regulator; Project: real-gluon emission and three-jet distribution; Project: three-body energy fractions and phase space.

Records: `peskin-schroeder.gluon-jet-project-inclusive-ir-cancellation`, `peskin-schroeder.gluon-jet-project-model-and-regulator`, `peskin-schroeder.gluon-jet-project-real-emission-three-jet-distribution`, `peskin-schroeder.gluon-jet-project-three-body-kinematics`, `peskin-schroeder.gluon-jet-project-virtual-form-factor-route`.

</details>

<details>
<summary>Section 8 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Correlation length and critical divergence; Critical fluctuations and quantum field theory; Critical two-point scaling, field normalization, and QFT mass; Effective-theory parameters and long-distance degrees of freedom.

Records: `peskin-schroeder.correlation-length-critical-divergence`, `peskin-schroeder.critical-fluctuation-qft-correspondence`, `peskin-schroeder.critical-two-point-scaling-and-qft-mass`, `peskin-schroeder.effective-theory-relevant-parameters-and-degrees-of-freedom`, `peskin-schroeder.landau-correlation-green-function`, `peskin-schroeder.landau-gibbs-free-energy-expansion`, `peskin-schroeder.landau-mean-field-magnetization-scaling`, `peskin-schroeder.landau-universality-from-symmetry`, `peskin-schroeder.local-landau-free-energy-functional`, `peskin-schroeder.natural-light-particles-and-cutoff-hierarchy`, `peskin-schroeder.nontrivial-critical-exponents`, `peskin-schroeder.order-parameter-and-critical-point`, `peskin-schroeder.renormalizable-qft-fixed-physical-parameters`, `peskin-schroeder.ultraviolet-cutoff-as-short-distance-dependence`.

</details>

<details>
<summary>Section 9 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Bosonic functional determinant; Complex-scalar current contact identity; Configuration-space path integral; Covariant photon propagator and gauge parameter.

Records: `peskin-schroeder.bosonic-functional-determinant`, `peskin-schroeder.complex-scalar-current-contact-identity`, `peskin-schroeder.configuration-space-path-integral`, `peskin-schroeder.covariant-photon-propagator-and-gauge-parameter`, `peskin-schroeder.dirac-generating-functional-grassmann-sources`, `peskin-schroeder.dirac-grassmann-functional-propagator`, `peskin-schroeder.euclidean-correlation-length-compton-wavelength`, `peskin-schroeder.euclidean-qft-statistical-mechanics-correspondence`, `peskin-schroeder.faddeev-popov-gauge-fixing-abelian`, `peskin-schroeder.fermion-determinant-as-closed-loop-series`, `peskin-schroeder.free-scalar-generating-functional`, `peskin-schroeder.functional-derivative-and-scalar-source`, `peskin-schroeder.functional-phi4-vertices-and-vacuum-cancellation`, `peskin-schroeder.functional-qed-ward-takahashi-identity`, `peskin-schroeder.gauge-invariant-correlator-xi-independence`, `peskin-schroeder.gauge-redundancy-obstructs-photon-gaussian`, `peskin-schroeder.gaussian-functional-wick-contractions`, `peskin-schroeder.general-noether-schwinger-dyson-identity`, `peskin-schroeder.grassmann-algebra-and-shift-invariant-integration`, `peskin-schroeder.grassmann-gaussian-determinants-and-pairings`, `peskin-schroeder.lagrangian-functional-definition-and-manifest-symmetries`, `peskin-schroeder.phase-space-path-integral-and-weyl-ordering`, `peskin-schroeder.physical-qed-s-matrix-projection`, `peskin-schroeder.qed-functional-feynman-rules`, `peskin-schroeder.real-scalar-field-path-integral`, `peskin-schroeder.scalar-functional-integral-lattice-and-ie`, `peskin-schroeder.schwinger-dyson-equations-from-field-shifts`, `peskin-schroeder.time-sliced-path-integral-normalization`, `peskin-schroeder.translation-schwinger-dyson-stress-tensor`, `peskin-schroeder.vacuum-correlators-from-scalar-path-integral`.

</details>

<details>
<summary>Section 9.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Configuration-space path integral; Phase-space path integral and Weyl ordering; Time-sliced path-integral normalization.

Records: `peskin-schroeder.configuration-space-path-integral`, `peskin-schroeder.phase-space-path-integral-and-weyl-ordering`, `peskin-schroeder.time-sliced-path-integral-normalization`.

</details>

<details>
<summary>Section 9.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bosonic functional determinant; Free scalar generating functional; Functional derivative and scalar source; Functional phi-four vertices and vacuum-bubble cancellation.

Records: `peskin-schroeder.bosonic-functional-determinant`, `peskin-schroeder.free-scalar-generating-functional`, `peskin-schroeder.functional-derivative-and-scalar-source`, `peskin-schroeder.functional-phi4-vertices-and-vacuum-cancellation`, `peskin-schroeder.gaussian-functional-wick-contractions`, `peskin-schroeder.lagrangian-functional-definition-and-manifest-symmetries`, `peskin-schroeder.real-scalar-field-path-integral`, `peskin-schroeder.scalar-functional-integral-lattice-and-ie`, `peskin-schroeder.vacuum-correlators-from-scalar-path-integral`.

</details>

<details>
<summary>Section 9.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Euclidean QFT–statistical-mechanics correspondence.

Records: `peskin-schroeder.euclidean-qft-statistical-mechanics-correspondence`.

</details>

<details>
<summary>Section 9.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Covariant photon propagator and gauge parameter; Euclidean correlation length and Compton wavelength; Faddeev–Popov gauge fixing in Abelian theory; Gauge-invariant correlators are gauge-parameter independent.

Records: `peskin-schroeder.covariant-photon-propagator-and-gauge-parameter`, `peskin-schroeder.euclidean-correlation-length-compton-wavelength`, `peskin-schroeder.faddeev-popov-gauge-fixing-abelian`, `peskin-schroeder.gauge-invariant-correlator-xi-independence`, `peskin-schroeder.gauge-redundancy-obstructs-photon-gaussian`.

</details>

<details>
<summary>Section 9.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Dirac generating functional with Grassmann sources; Dirac Grassmann functional propagator; Fermion determinant as a closed-loop series; Grassmann algebra and shift-invariant integration.

Records: `peskin-schroeder.dirac-generating-functional-grassmann-sources`, `peskin-schroeder.dirac-grassmann-functional-propagator`, `peskin-schroeder.fermion-determinant-as-closed-loop-series`, `peskin-schroeder.grassmann-algebra-and-shift-invariant-integration`, `peskin-schroeder.grassmann-gaussian-determinants-and-pairings`, `peskin-schroeder.physical-qed-s-matrix-projection`, `peskin-schroeder.qed-functional-feynman-rules`.

</details>

<details>
<summary>Section 9.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Complex-scalar current contact identity; Functional derivation of the QED Ward–Takahashi identity; General Noether Schwinger–Dyson identity; Schwinger–Dyson equations from field shifts.

Records: `peskin-schroeder.complex-scalar-current-contact-identity`, `peskin-schroeder.functional-qed-ward-takahashi-identity`, `peskin-schroeder.general-noether-schwinger-dyson-identity`, `peskin-schroeder.schwinger-dyson-equations-from-field-shifts`, `peskin-schroeder.translation-schwinger-dyson-stress-tensor`.

</details>

<details>
<summary>Section 9.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 9.2(a): thermal trace as periodic Euclidean path integral; Problem: scalar-QED pair-production cross section; Problem: scalar-QED propagator and photon vertices; Problem: scalar-QED vacuum polarization.

Records: `peskin-schroeder.problem-bosonic-thermal-path-integral`, `peskin-schroeder.problem-scalar-qed-pair-production-cross-section`, `peskin-schroeder.problem-scalar-qed-propagator-and-vertices`, `peskin-schroeder.problem-scalar-qed-vacuum-polarization`, `peskin-schroeder.problem-thermal-fermion-antiperiodic-boundary`, `peskin-schroeder.problem-thermal-free-scalar-determinant`, `peskin-schroeder.problem-thermal-harmonic-oscillator-determinant`, `peskin-schroeder.problem-thermal-photon-gauge-fixed-partition`.

</details>

<details>
<summary>Section 10 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Bare perturbation theory and renormalization; BPHZ finiteness and the two-loop phi-four cancellation; Endpoint subtraction isolates the two-loop nonlocal pole; External-momentum differentiation lowers superficial divergence.

Records: `peskin-schroeder.bare-to-renormalized-parameter-elimination`, `peskin-schroeder.bphz-and-two-loop-phi4-nonlocal-cancellation`, `peskin-schroeder.endpoint-subtraction-isolates-two-loop-nonlocal-pole`, `peskin-schroeder.external-momentum-derivative-power-counting`, `peskin-schroeder.furry-theorem-photon-odd-point-vanishing`, `peskin-schroeder.general-feynman-denominator-identity-proof`, `peskin-schroeder.phi4-field-rescaling-counterterm-split`, `peskin-schroeder.phi4-primitive-divergences-and-z2-symmetry`, `peskin-schroeder.phi4-two-loop-crossing-groups-and-factorized-subtraction`, `peskin-schroeder.phi4-two-loop-field-strength-subdivergence-structure`, `peskin-schroeder.phi4-two-point-onshell-counterterms`, `peskin-schroeder.qed-graph-topology-and-primitive-amplitudes`, `peskin-schroeder.qed-oneloop-dimreg-selfenergy-and-vacuum-polarization-counterterms`, `peskin-schroeder.qed-oneloop-vertex-counterterm-and-allorders-ward-recursion`, `peskin-schroeder.qed-primitive-divergences-and-symmetry-constraints`, `peskin-schroeder.qed-uv-ir-regulator-separation`, `peskin-schroeder.renormalizability-classification-by-dimension`, `peskin-schroeder.renormalization-conditions-and-phi4-one-loop-vertex`, `peskin-schroeder.renormalized-qed-counterterms-and-conditions`, `peskin-schroeder.subdivergences-locality-and-counterterm-insertion`, `peskin-schroeder.superficial-degree-qualifications`, `peskin-schroeder.superficial-divergence-power-counting`, `peskin-schroeder.two-loop-counterterm-pole-log-cancellation`, `peskin-schroeder.ward-identity-z1-z2-and-universal-charge`, `peskin-schroeder.yukawa-scalar-field-strength-renormalization`.

</details>

<details>
<summary>Section 10.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: External-momentum differentiation lowers superficial divergence; Furry theorem for odd photon-current amplitudes; QED topology reduction to primitively divergent amplitudes; QED primitive divergences constrained by chiral and Ward identities.

Records: `peskin-schroeder.external-momentum-derivative-power-counting`, `peskin-schroeder.furry-theorem-photon-odd-point-vanishing`, `peskin-schroeder.qed-graph-topology-and-primitive-amplitudes`, `peskin-schroeder.qed-primitive-divergences-and-symmetry-constraints`, `peskin-schroeder.renormalizability-classification-by-dimension`, `peskin-schroeder.superficial-degree-qualifications`, `peskin-schroeder.superficial-divergence-power-counting`.

</details>

<details>
<summary>Section 10.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bare perturbation theory and renormalization; Renormalized phi-four Lagrangian and counterterm split; Phi-four primitive divergences and odd-amplitude exclusion; Phi-four two-loop field-strength and subdivergence structures.

Records: `peskin-schroeder.bare-to-renormalized-parameter-elimination`, `peskin-schroeder.phi4-field-rescaling-counterterm-split`, `peskin-schroeder.phi4-primitive-divergences-and-z2-symmetry`, `peskin-schroeder.phi4-two-loop-field-strength-subdivergence-structure`, `peskin-schroeder.phi4-two-point-onshell-counterterms`, `peskin-schroeder.renormalization-conditions-and-phi4-one-loop-vertex`, `peskin-schroeder.yukawa-scalar-field-strength-renormalization`.

</details>

<details>
<summary>Section 10.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: One-loop QED delta-m, delta-2, and delta-3 in dimensional regularization; One-loop QED delta-1 and all-orders Ward recursion; Source-specific UV and IR regulator choice in QED; Renormalized QED counterterms and on-shell conditions.

Records: `peskin-schroeder.qed-oneloop-dimreg-selfenergy-and-vacuum-polarization-counterterms`, `peskin-schroeder.qed-oneloop-vertex-counterterm-and-allorders-ward-recursion`, `peskin-schroeder.qed-uv-ir-regulator-separation`, `peskin-schroeder.renormalized-qed-counterterms-and-conditions`, `peskin-schroeder.ward-identity-z1-z2-and-universal-charge`, `peskin-schroeder.yukawa-scalar-field-strength-renormalization`.

</details>

<details>
<summary>Section 10.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Subdivergences, locality, and counterterm insertion; Ward identity, Z1 equals Z2, and universal charge.

Records: `peskin-schroeder.subdivergences-locality-and-counterterm-insertion`, `peskin-schroeder.ward-identity-z1-z2-and-universal-charge`.

</details>

<details>
<summary>Section 10.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: BPHZ finiteness and the two-loop phi-four cancellation; Endpoint subtraction isolates the two-loop nonlocal pole; General denominator-combination identity and proof; Two-loop phi-four crossing groups and factorized Group I subtraction.

Records: `peskin-schroeder.bphz-and-two-loop-phi4-nonlocal-cancellation`, `peskin-schroeder.endpoint-subtraction-isolates-two-loop-nonlocal-pole`, `peskin-schroeder.general-feynman-denominator-identity-proof`, `peskin-schroeder.phi4-two-loop-crossing-groups-and-factorized-subtraction`, `peskin-schroeder.two-loop-counterterm-pole-log-cancellation`.

</details>

<details>
<summary>Section 10.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: BPHZ finiteness and the two-loop phi-four cancellation; Problem: phi-four fixed-t high-energy leading logarithms; Problem: phi-four two-loop field-strength renormalization; Problem: one-loop QED odd- and four-photon amplitudes.

Records: `peskin-schroeder.bphz-and-two-loop-phi4-nonlocal-cancellation`, `peskin-schroeder.problem-ch10-phi4-fixedt-leading-logs`, `peskin-schroeder.problem-ch10-phi4-two-loop-field-strength`, `peskin-schroeder.problem-ch10-qed-odd-even-photon-divergences`, `peskin-schroeder.problem-ch10-yukawa-renormalization`, `peskin-schroeder.two-loop-counterterm-pole-log-cancellation`.

</details>

<details>
<summary>Section 11 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Symmetry-linked counterterms in the broken O(N) model; Classical Goldstone theorem from symmetry of the potential; Discrete scalar symmetry breaking by shifting about a vacuum; Effective action generates one-particle-irreducible amplitudes.

Records: `peskin-schroeder.broken-on-sigma-counterterms`, `peskin-schroeder.classical-goldstone-theorem`, `peskin-schroeder.discrete-symmetry-breaking-scalar-shift`, `peskin-schroeder.effective-action-1pi-generating-functional`, `peskin-schroeder.effective-action-background-field-expansion`, `peskin-schroeder.effective-action-legendre-transform`, `peskin-schroeder.effective-action-varying-background-proof-boundary`, `peskin-schroeder.effective-potential-vacua-and-convexity`, `peskin-schroeder.msbar-scale-and-large-log-qualification`, `peskin-schroeder.on-linear-sigma-model-broken-vacuum`, `peskin-schroeder.on-sigma-effective-potential-determinant`, `peskin-schroeder.on-sigma-one-loop-four-point-cancellations`, `peskin-schroeder.on-sigma-renormalization-conditions`, `peskin-schroeder.on-sigma-tadpole-and-goldstone-one-loop`, `peskin-schroeder.quantum-goldstone-theorem`, `peskin-schroeder.spontaneous-symmetry-breaking-question`, `peskin-schroeder.symmetric-counterterms-general-effective-action`, `peskin-schroeder.zeroth-order-natural-relations`.

</details>

<details>
<summary>Section 11.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Classical Goldstone theorem from symmetry of the potential; Discrete scalar symmetry breaking by shifting about a vacuum; O(N) linear sigma model and broken vacuum.

Records: `peskin-schroeder.classical-goldstone-theorem`, `peskin-schroeder.discrete-symmetry-breaking-scalar-shift`, `peskin-schroeder.on-linear-sigma-model-broken-vacuum`.

</details>

<details>
<summary>Section 11.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Symmetry-linked counterterms in the broken O(N) model; Classical Goldstone theorem from symmetry of the potential; One-loop O(N) four- and three-point cancellation; Linear sigma renormalization conditions with a tadpole convention.

Records: `peskin-schroeder.broken-on-sigma-counterterms`, `peskin-schroeder.classical-goldstone-theorem`, `peskin-schroeder.on-sigma-one-loop-four-point-cancellations`, `peskin-schroeder.on-sigma-renormalization-conditions`, `peskin-schroeder.on-sigma-tadpole-and-goldstone-one-loop`.

</details>

<details>
<summary>Section 11.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Effective action as a functional Legendre transform; Effective potential, vacuum selection, and convexity.

Records: `peskin-schroeder.effective-action-legendre-transform`, `peskin-schroeder.effective-potential-vacua-and-convexity`.

</details>

<details>
<summary>Section 11.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Background-field expansion of the effective action; Modified minimal subtraction, scale dependence, and large logarithms; O(N) effective potential from fluctuation determinants.

Records: `peskin-schroeder.effective-action-background-field-expansion`, `peskin-schroeder.msbar-scale-and-large-log-qualification`, `peskin-schroeder.on-sigma-effective-potential-determinant`.

</details>

<details>
<summary>Section 11.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Effective action generates one-particle-irreducible amplitudes; Modified minimal subtraction, scale dependence, and large logarithms.

Records: `peskin-schroeder.effective-action-1pi-generating-functional`, `peskin-schroeder.msbar-scale-and-large-log-qualification`.

</details>

<details>
<summary>Section 11.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Effective action generates one-particle-irreducible amplitudes; Effective-action renormalization boundary for varying backgrounds; Goldstone theorem to all quantum orders; Symmetry-preserving counterterms for constant scalar backgrounds.

Records: `peskin-schroeder.effective-action-1pi-generating-functional`, `peskin-schroeder.effective-action-varying-background-proof-boundary`, `peskin-schroeder.quantum-goldstone-theorem`, `peskin-schroeder.symmetric-counterterms-general-effective-action`, `peskin-schroeder.zeroth-order-natural-relations`.

</details>

<details>
<summary>Section 11.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: Gross-Neveu determinant, broken minimum, and large-N suppression; Problem: Gross-Neveu discrete chiral symmetry and auxiliary field; Problem: finite natural relation in a broken fermion model; Problem: spin-wave theory and low-dimensional order.

Records: `peskin-schroeder.problem-gross-neveu-determinant-minimum-large-n`, `peskin-schroeder.problem-gross-neveu-symmetry-and-auxiliary-field`, `peskin-schroeder.problem-natural-relation-with-fermions`, `peskin-schroeder.problem-spin-wave-theory`.

</details>

<details>
<summary>Section 12 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Beta-function flow classes; Callan-Symanzik equation; Correlation-length exponent from mass flow; Counterterm logarithms determine leading RG functions.

Records: `peskin-schroeder.beta-function-flow-classes`, `peskin-schroeder.callan-symanzik-equation`, `peskin-schroeder.correlation-length-exponent-from-mass-flow`, `peskin-schroeder.counterterms-determine-leading-cs-functions`, `peskin-schroeder.cs-dimensional-scaling-of-greens-functions`, `peskin-schroeder.cs-running-coupling-characteristics`, `peskin-schroeder.epsilon-expanded-wilson-fisher-beta`, `peskin-schroeder.free-fixed-point-effective-lagrangian`, `peskin-schroeder.general-perturbation-rg-flow`, `peskin-schroeder.heavy-w-local-operator-motivation`, `peskin-schroeder.magnet-cutoff-and-critical-tuning`, `peskin-schroeder.mass-operator-anomalous-dimension`, `peskin-schroeder.massless-dim-reg-subtraction-prescription`, `peskin-schroeder.massless-phi4-one-loop-beta`, `peskin-schroeder.massless-spacelike-renormalization-conditions`, `peskin-schroeder.momentum-shell-mode-split`, `peskin-schroeder.on-critical-exponent-universality`, `peskin-schroeder.operator-dimension-ir-relevance`, `peskin-schroeder.qed-beta-from-renormalization-constants`, `peskin-schroeder.qed-running-charge-and-landau-pole`, `peskin-schroeder.renormalization-of-local-operator-insertions`, `peskin-schroeder.renormalized-theory-fixed-point-trajectory`, `peskin-schroeder.rg-flow-not-invertible-group`, `peskin-schroeder.rg-operator-relevance-classification`, `peskin-schroeder.scalar-mass-naturalness-problem`, `peskin-schroeder.shell-induced-effective-interactions`, `peskin-schroeder.wilson-euclidean-sharp-cutoff`, `peskin-schroeder.wilson-fisher-fixed-point-from-shell-flow`, `peskin-schroeder.wilson-rescaling-transformation`.

</details>

<details>
<summary>Section 12.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Free fixed point and long-distance effective Lagrangian; Magnetic cutoff analogy and critical tuning; Momentum-shell split of scalar modes; Renormalization-group flow and noninvertibility.

Records: `peskin-schroeder.free-fixed-point-effective-lagrangian`, `peskin-schroeder.magnet-cutoff-and-critical-tuning`, `peskin-schroeder.momentum-shell-mode-split`, `peskin-schroeder.rg-flow-not-invertible-group`, `peskin-schroeder.rg-operator-relevance-classification`, `peskin-schroeder.shell-induced-effective-interactions`, `peskin-schroeder.wilson-euclidean-sharp-cutoff`, `peskin-schroeder.wilson-fisher-fixed-point-from-shell-flow`, `peskin-schroeder.wilson-rescaling-transformation`.

</details>

<details>
<summary>Section 12.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Callan-Symanzik equation; Counterterm logarithms determine leading RG functions; Massless dimensional-regularization subtraction prescription; Massless phi-four one-loop beta function.

Records: `peskin-schroeder.callan-symanzik-equation`, `peskin-schroeder.counterterms-determine-leading-cs-functions`, `peskin-schroeder.massless-dim-reg-subtraction-prescription`, `peskin-schroeder.massless-phi4-one-loop-beta`, `peskin-schroeder.massless-spacelike-renormalization-conditions`, `peskin-schroeder.qed-beta-from-renormalization-constants`, `peskin-schroeder.renormalized-theory-fixed-point-trajectory`, `peskin-schroeder.scalar-mass-naturalness-problem`.

</details>

<details>
<summary>Section 12.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Beta-function flow classes; RG-improved dimensional scaling of Green functions; Running coupling from characteristic curves; QED running charge and Landau-pole limitation.

Records: `peskin-schroeder.beta-function-flow-classes`, `peskin-schroeder.cs-dimensional-scaling-of-greens-functions`, `peskin-schroeder.cs-running-coupling-characteristics`, `peskin-schroeder.qed-running-charge-and-landau-pole`.

</details>

<details>
<summary>Section 12.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Beta-function flow classes; Heavy-W exchange motivates local operators; Phi-squared mass-operator anomalous dimension; Renormalization of local-operator insertions.

Records: `peskin-schroeder.beta-function-flow-classes`, `peskin-schroeder.heavy-w-local-operator-motivation`, `peskin-schroeder.mass-operator-anomalous-dimension`, `peskin-schroeder.renormalization-of-local-operator-insertions`.

</details>

<details>
<summary>Section 12.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Correlation-length exponent from mass flow; Epsilon-expanded Wilson-Fisher beta function; General perturbation RG flow; Phi-squared mass-operator anomalous dimension.

Records: `peskin-schroeder.correlation-length-exponent-from-mass-flow`, `peskin-schroeder.epsilon-expanded-wilson-fisher-beta`, `peskin-schroeder.general-perturbation-rg-flow`, `peskin-schroeder.mass-operator-anomalous-dimension`, `peskin-schroeder.on-critical-exponent-universality`, `peskin-schroeder.operator-dimension-ir-relevance`.

</details>

<details>
<summary>Section 12.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: asymptotic O(2) beta functions; Problem: asymptotic O(2) epsilon fixed points; Problem: asymptotic O(2) infrared restoration; Problem: Gross-Neveu beta function and asymptotic freedom.

Records: `peskin-schroeder.problem-asymptotic-on2-beta-functions`, `peskin-schroeder.problem-asymptotic-on2-epsilon-fixed-points`, `peskin-schroeder.problem-asymptotic-on2-infrared-restoration`, `peskin-schroeder.problem-gross-neveu-asymptotic-freedom`, `peskin-schroeder.problem-yukawa-beta-flow`.

</details>

<details>
<summary>Section 13 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Critical correlation exponents; Critical-exponent scaling relations; Critical two-point scaling and eta; Experimental and lattice tests of critical universality.

Records: `peskin-schroeder.critical-correlation-exponents-definition`, `peskin-schroeder.critical-exponent-scaling-relations`, `peskin-schroeder.critical-two-point-scaling-anomalous-dimension`, `peskin-schroeder.experimental-universality-critical-exponents`, `peskin-schroeder.fixed-point-eigenoperator-scaling`, `peskin-schroeder.four-dimensional-marginal-logarithms`, `peskin-schroeder.gibbs-free-energy-scaling-equation`, `peskin-schroeder.large-n-sigma-phase-transition-above-two`, `peskin-schroeder.mermin-wagner-spin-wave-obstruction`, `peskin-schroeder.nonlinear-sigma-asymptotic-freedom-and-n2-exception`, `peskin-schroeder.nonlinear-sigma-large-n-saddle`, `peskin-schroeder.nonlinear-sigma-model-constraint-and-goldstone-coordinates`, `peskin-schroeder.nonlinear-sigma-near-two-eta`, `peskin-schroeder.nonlinear-sigma-near-two-nu`, `peskin-schroeder.nonlinear-sigma-one-loop-cs-functions`, `peskin-schroeder.nonlinear-sigma-renormalizability-and-symmetry-counterterms`, `peskin-schroeder.nonlinear-sigma-temperature-fixed-point`, `peskin-schroeder.nonlinear-sigma-wilson-shell-derivation`, `peskin-schroeder.on-epsilon-expansion-critical-exponents`, `peskin-schroeder.rg-improved-effective-potential`, `peskin-schroeder.two-dimensional-nonlinear-sigma-mass-gap`.

</details>

<details>
<summary>Section 13.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Critical correlation exponents; Critical-exponent scaling relations; Critical two-point scaling and eta; Experimental and lattice tests of critical universality.

Records: `peskin-schroeder.critical-correlation-exponents-definition`, `peskin-schroeder.critical-exponent-scaling-relations`, `peskin-schroeder.critical-two-point-scaling-anomalous-dimension`, `peskin-schroeder.experimental-universality-critical-exponents`, `peskin-schroeder.fixed-point-eigenoperator-scaling`, `peskin-schroeder.gibbs-free-energy-scaling-equation`, `peskin-schroeder.on-epsilon-expansion-critical-exponents`.

</details>

<details>
<summary>Section 13.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Experimental and lattice tests of critical universality; Four-dimensional marginal logarithms; Renormalization-group-improved effective potential.

Records: `peskin-schroeder.experimental-universality-critical-exponents`, `peskin-schroeder.four-dimensional-marginal-logarithms`, `peskin-schroeder.rg-improved-effective-potential`.

</details>

<details>
<summary>Section 13.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Large-N sigma-model phase transition above two dimensions; Mermin-Wagner obstruction from sigma-model fluctuations; Nonlinear sigma-model asymptotic freedom and N=2 exception; Large-N nonlinear sigma-model saddle.

Records: `peskin-schroeder.large-n-sigma-phase-transition-above-two`, `peskin-schroeder.mermin-wagner-spin-wave-obstruction`, `peskin-schroeder.nonlinear-sigma-asymptotic-freedom-and-n2-exception`, `peskin-schroeder.nonlinear-sigma-large-n-saddle`, `peskin-schroeder.nonlinear-sigma-model-constraint-and-goldstone-coordinates`, `peskin-schroeder.nonlinear-sigma-near-two-eta`, `peskin-schroeder.nonlinear-sigma-near-two-nu`, `peskin-schroeder.nonlinear-sigma-one-loop-cs-functions`, `peskin-schroeder.nonlinear-sigma-renormalizability-and-symmetry-counterterms`, `peskin-schroeder.nonlinear-sigma-temperature-fixed-point`, `peskin-schroeder.nonlinear-sigma-wilson-shell-derivation`, `peskin-schroeder.two-dimensional-nonlinear-sigma-mass-gap`.

</details>

<details>
<summary>Section 13.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Large-N sigma-model phase transition above two dimensions; Problem: correction-to-scaling exponent; Problem: CP-N emergent photon; Problem: CP-N Lagrange-multiplier representation.

Records: `peskin-schroeder.large-n-sigma-phase-transition-above-two`, `peskin-schroeder.problem-correction-to-scaling-exponent`, `peskin-schroeder.problem-cpn-emergent-photon`, `peskin-schroeder.problem-cpn-lagrange-multiplier-representation`, `peskin-schroeder.problem-cpn-large-n-saddle`, `peskin-schroeder.problem-cpn-local-symmetry-and-sigma-map`, `peskin-schroeder.problem-eta-two-loop-on-model`, `peskin-schroeder.scalar-field-dimensional-rg-regimes`.

</details>

<details>
<summary>Section 13.project — covered</summary>

The project records represent the substantive final-project branches on pp. 469–470. The exact accepted render for p. 471 is a Part III / Non-Abelian Gauge Theories divider, so it contributes no concept; p. 472 remains the separately accepted publisher-only exclusion.

Records: `peskin-schroeder.coleman-weinberg-model-assumptions`, `peskin-schroeder.problem-coleman-weinberg-beta-flow`, `peskin-schroeder.problem-coleman-weinberg-higgs-expansion`, `peskin-schroeder.problem-coleman-weinberg-mass-squared-scan`, `peskin-schroeder.problem-coleman-weinberg-nonzero-mass-endpoint`, `peskin-schroeder.problem-coleman-weinberg-one-loop-potential`, `peskin-schroeder.problem-coleman-weinberg-radiative-minimum`, `peskin-schroeder.problem-coleman-weinberg-rg-improved-potential`, `peskin-schroeder.problem-coleman-weinberg-superconductor-epsilon-flow`.

</details>

<details>
<summary>Section 14 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Asymptotic freedom predicts logarithmic scaling violations; Parton-model Bjorken scaling; Bjorken x from elastic parton kinematics; Limited transverse momentum in high-energy hadron collisions.

Records: `peskin-schroeder.asymptotic-freedom-scaling-violations-and-hard-jets`, `peskin-schroeder.bjorken-scaling-parton-cross-section`, `peskin-schroeder.dis-bjorken-x-from-elastic-parton-kinematics`, `peskin-schroeder.high-energy-hadron-transverse-momentum-pattern`, `peskin-schroeder.parton-model-deep-inelastic-assumptions`.

</details>

<details>
<summary>Section 15 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Abelian field strength as curvature; Abelian Wilson line and loop; Adjoint representation and its covariant derivative; Quadratic Casimir definitions and the index relation.

Records: `peskin-schroeder.abelian-curvature-from-holonomy-and-covariant-commutator`, `peskin-schroeder.abelian-wilson-line-and-loop`, `peskin-schroeder.adjoint-representation-covariant-derivative-and-bianchi-input`, `peskin-schroeder.casimir-definitions-and-index-relation`, `peskin-schroeder.compact-simple-lie-algebra-classification`, `peskin-schroeder.covariant-yang-mills-equation-and-bianchi-identity`, `peskin-schroeder.general-nonabelian-gauge-construction`, `peskin-schroeder.lie-algebra-jacobi-identity-and-local-global-distinction`, `peskin-schroeder.local-comparator-connection-and-covariant-derivative`, `peskin-schroeder.local-symmetry-dimension-four-maxwell-dirac-selection`, `peskin-schroeder.nonabelian-path-ordered-wilson-line`, `peskin-schroeder.real-pseudoreal-and-complex-representations`, `peskin-schroeder.su2-local-covariant-derivative-and-connection`, `peskin-schroeder.sun-casimir-normalization-and-adjoint-values`, `peskin-schroeder.sun-generators-representations-and-trace-normalization`, `peskin-schroeder.traced-nonabelian-wilson-loop-and-curvature`, `peskin-schroeder.yang-mills-field-strength-self-interactions`.

</details>

<details>
<summary>Section 15.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Abelian field strength as curvature; Local comparator, connection, and covariant derivative; Local symmetry and the dimension-four Maxwell-Dirac Lagrangian.

Records: `peskin-schroeder.abelian-curvature-from-holonomy-and-covariant-commutator`, `peskin-schroeder.local-comparator-connection-and-covariant-derivative`, `peskin-schroeder.local-symmetry-dimension-four-maxwell-dirac-selection`.

</details>

<details>
<summary>Section 15.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: General non-Abelian gauge construction; Local symmetry and the dimension-four Maxwell-Dirac Lagrangian; SU(2) local connection and covariant derivative; Yang-Mills curvature and symmetry-fixed self-interactions.

Records: `peskin-schroeder.general-nonabelian-gauge-construction`, `peskin-schroeder.local-symmetry-dimension-four-maxwell-dirac-selection`, `peskin-schroeder.su2-local-covariant-derivative-and-connection`, `peskin-schroeder.yang-mills-field-strength-self-interactions`.

</details>

<details>
<summary>Section 15.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Abelian Wilson line and loop; General non-Abelian gauge construction; Path-ordered non-Abelian Wilson line; Traced non-Abelian Wilson loop.

Records: `peskin-schroeder.abelian-wilson-line-and-loop`, `peskin-schroeder.general-nonabelian-gauge-construction`, `peskin-schroeder.nonabelian-path-ordered-wilson-line`, `peskin-schroeder.traced-nonabelian-wilson-loop-and-curvature`, `peskin-schroeder.yang-mills-field-strength-self-interactions`.

</details>

<details>
<summary>Section 15.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Adjoint representation and its covariant derivative; Quadratic Casimir definitions and the index relation; Compact simple Lie algebras and their classification; Covariant Yang-Mills equation and Bianchi identity.

Records: `peskin-schroeder.adjoint-representation-covariant-derivative-and-bianchi-input`, `peskin-schroeder.casimir-definitions-and-index-relation`, `peskin-schroeder.compact-simple-lie-algebra-classification`, `peskin-schroeder.covariant-yang-mills-equation-and-bianchi-identity`, `peskin-schroeder.lie-algebra-jacobi-identity-and-local-global-distinction`, `peskin-schroeder.real-pseudoreal-and-complex-representations`, `peskin-schroeder.sun-casimir-normalization-and-adjoint-values`, `peskin-schroeder.sun-generators-representations-and-trace-normalization`.

</details>

<details>
<summary>Section 15.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: Casimirs from SU(2) subgroup decompositions; Problem: scalar propagator as a worldline functional integral; Problem: SU(2) adjoint basis and Casimirs; Problem: SU(3) fundamental generators and invariants.

Records: `peskin-schroeder.problem-casimir-su2-decomposition`, `peskin-schroeder.problem-scalar-propagator-worldline-wilson-line`, `peskin-schroeder.problem-su2-adjoint-casimirs`, `peskin-schroeder.problem-su3-fundamental-generators-and-invariants`, `peskin-schroeder.problem-wilson-loop-coulomb-potentials`, `peskin-schroeder.sun-casimir-normalization-and-adjoint-values`.

</details>

<details>
<summary>Section 16 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Background determinants, g-factor two, and beta coefficients; Background-field route to the non-Abelian beta function; BRST auxiliary-field symmetry and nilpotence; BRST physical state space and restricted unitarity.

Records: `peskin-schroeder.background-determinants-magnetic-moment-and-beta-coefficients`, `peskin-schroeder.background-field-gauge-invariant-effective-action-route`, `peskin-schroeder.brst-auxiliary-field-symmetry-and-nilpotence`, `peskin-schroeder.brst-physical-state-space-and-restricted-unitarity`, `peskin-schroeder.faddeev-popov-ghost-lagrangian-and-rules`, `peskin-schroeder.gauge-symmetry-counterterm-relations-and-coupling-universality`, `peskin-schroeder.ghost-cancellation-of-unphysical-cut-states`, `peskin-schroeder.nonabelian-coulomb-antiscreening-explanation`, `peskin-schroeder.nonabelian-faddeev-popov-determinant-and-gauge-fixing`, `peskin-schroeder.nonabelian-ward-cancellations-and-optical-theorem-paradox`, `peskin-schroeder.one-loop-gauge-self-energy-ghost-transversality`, `peskin-schroeder.one-loop-nonabelian-beta-function`, `peskin-schroeder.yang-mills-feynman-rules-and-universal-coupling`.

</details>

<details>
<summary>Section 16.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Non-Abelian Ward cancellations and the unitarity paradox; Yang-Mills Feynman rules and universal coupling.

Records: `peskin-schroeder.nonabelian-ward-cancellations-and-optical-theorem-paradox`, `peskin-schroeder.yang-mills-feynman-rules-and-universal-coupling`.

</details>

<details>
<summary>Section 16.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Faddeev-Popov ghosts and their Feynman rules; Non-Abelian Faddeev-Popov gauge fixing; Non-Abelian Ward cancellations and the unitarity paradox.

Records: `peskin-schroeder.faddeev-popov-ghost-lagrangian-and-rules`, `peskin-schroeder.nonabelian-faddeev-popov-determinant-and-gauge-fixing`, `peskin-schroeder.nonabelian-ward-cancellations-and-optical-theorem-paradox`.

</details>

<details>
<summary>Section 16.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Faddeev-Popov ghosts and their Feynman rules; Ghost cancellation of unphysical Cutkosky states.

Records: `peskin-schroeder.faddeev-popov-ghost-lagrangian-and-rules`, `peskin-schroeder.ghost-cancellation-of-unphysical-cut-states`.

</details>

<details>
<summary>Section 16.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: BRST auxiliary-field symmetry and nilpotence; BRST physical state space and restricted unitarity; Ghost cancellation of unphysical Cutkosky states.

Records: `peskin-schroeder.brst-auxiliary-field-symmetry-and-nilpotence`, `peskin-schroeder.brst-physical-state-space-and-restricted-unitarity`, `peskin-schroeder.ghost-cancellation-of-unphysical-cut-states`.

</details>

<details>
<summary>Section 16.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: BRST physical state space and restricted unitarity; Gauge-symmetry counterterm relations and coupling universality; One-loop gauge self-energy: ghost-required transversality; One-loop non-Abelian beta function.

Records: `peskin-schroeder.brst-physical-state-space-and-restricted-unitarity`, `peskin-schroeder.gauge-symmetry-counterterm-relations-and-coupling-universality`, `peskin-schroeder.one-loop-gauge-self-energy-ghost-transversality`, `peskin-schroeder.one-loop-nonabelian-beta-function`.

</details>

<details>
<summary>Section 16.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Background determinants, g-factor two, and beta coefficients; Background-field route to the non-Abelian beta function; Gauge-symmetry counterterm relations and coupling universality.

Records: `peskin-schroeder.background-determinants-magnetic-moment-and-beta-coefficients`, `peskin-schroeder.background-field-gauge-invariant-effective-action-route`, `peskin-schroeder.gauge-symmetry-counterterm-relations-and-coupling-universality`.

</details>

<details>
<summary>Section 16.7 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Qualitative non-Abelian Coulomb antiscreening.

Records: `peskin-schroeder.nonabelian-coulomb-antiscreening-explanation`.

</details>

<details>
<summary>Section 16.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem: Arnowitt-Fickler gauge quantization; Problem: non-Abelian charged scalar and beta function; Problem: non-Abelian counterterm relations.

Records: `peskin-schroeder.problem-arnowitt-fickler-gauge-quantization`, `peskin-schroeder.problem-nonabelian-charged-scalar-beta-function`, `peskin-schroeder.problem-nonabelian-counterterm-relations`.

</details>

<details>
<summary>Section 17 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Altarelli–Parisi evolution framework; SU(3) color factor in the e+e− QCD correction; QCD color representations and color-singlet hadrons; Leading-order QCD factorization for deep-inelastic scattering.

Records: `peskin-schroeder.qcd-altarelli-parisi-evolution`, `peskin-schroeder.qcd-color-factor-transcription`, `peskin-schroeder.qcd-color-singlets-and-field-content`, `peskin-schroeder.qcd-dis-leading-parton-factorization`, `peskin-schroeder.qcd-dis-xy-scaling-and-callan-gross`, `peskin-schroeder.qcd-drell-yan-mass-rapidity-pdfs`, `peskin-schroeder.qcd-gluon-splitting-kernel-result`, `peskin-schroeder.qcd-hadron-collision-factorization`, `peskin-schroeder.qcd-inclusive-eplus-eminus-hadrons`, `peskin-schroeder.qcd-independent-alpha-s-determinations`, `peskin-schroeder.qcd-neutrino-dis-flavor-and-helicity-analysis`, `peskin-schroeder.qcd-on-shell-rg-infrared-proof-boundary`, `peskin-schroeder.qcd-parton-scattering-formulas`, `peskin-schroeder.qcd-pdf-flavor-and-momentum-sum-rules`, `peskin-schroeder.qcd-qqg-energy-fraction-distribution`, `peskin-schroeder.qcd-quark-flavors-charges-and-color-motivation`, `peskin-schroeder.qcd-running-coupling-and-lambda`, `peskin-schroeder.qcd-scaling-violation-phenomenology`, `peskin-schroeder.qcd-strong-coupling-color-confinement`, `peskin-schroeder.qcd-three-jet-energy-flow`, `peskin-schroeder.qcd-two-body-jet-rapidity-kinematics`, `peskin-schroeder.qed-collinear-factorization-and-equivalent-photon`, `peskin-schroeder.qed-collinear-virtuality-and-helicity-kernel`, `peskin-schroeder.qed-gribov-lipatov-kernels`, `peskin-schroeder.qed-normalized-electron-distribution`, `peskin-schroeder.qed-strong-ordering-and-gribov-lipatov-evolution`.

</details>

<details>
<summary>Section 17.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: QCD color representations and color-singlet hadrons; Quark flavors, charge assignments, flavor symmetry, and the color puzzle.

Records: `peskin-schroeder.qcd-color-singlets-and-field-content`, `peskin-schroeder.qcd-quark-flavors-charges-and-color-motivation`.

</details>

<details>
<summary>Section 17.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: SU(3) color factor in the e+e− QCD correction; Inclusive e+e− hadron rate through first order in alpha_s; On-shell QCD RG use and infrared-cancellation proof boundary; The leading e+e−→q qbar g energy-fraction distribution.

Records: `peskin-schroeder.qcd-color-factor-transcription`, `peskin-schroeder.qcd-inclusive-eplus-eminus-hadrons`, `peskin-schroeder.qcd-on-shell-rg-infrared-proof-boundary`, `peskin-schroeder.qcd-qqg-energy-fraction-distribution`, `peskin-schroeder.qcd-running-coupling-and-lambda`, `peskin-schroeder.qcd-strong-coupling-color-confinement`, `peskin-schroeder.qcd-three-jet-energy-flow`.

</details>

<details>
<summary>Section 17.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Leading-order QCD factorization for deep-inelastic scattering; DIS x-y kinematics, Bjorken scaling, and Callan–Gross behavior; Neutrino DIS separates flavors through chiral charged currents; PDF flavor-number and momentum sum rules.

Records: `peskin-schroeder.qcd-dis-leading-parton-factorization`, `peskin-schroeder.qcd-dis-xy-scaling-and-callan-gross`, `peskin-schroeder.qcd-neutrino-dis-flavor-and-helicity-analysis`, `peskin-schroeder.qcd-pdf-flavor-and-momentum-sum-rules`.

</details>

<details>
<summary>Section 17.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Drell–Yan lepton pairs determine incoming PDF fractions; Hard hadron-collision factorization; Leading spin- and color-averaged parton cross sections; PDF flavor-number and momentum sum rules.

Records: `peskin-schroeder.qcd-drell-yan-mass-rapidity-pdfs`, `peskin-schroeder.qcd-hadron-collision-factorization`, `peskin-schroeder.qcd-parton-scattering-formulas`, `peskin-schroeder.qcd-pdf-flavor-and-momentum-sum-rules`, `peskin-schroeder.qcd-two-body-jet-rapidity-kinematics`.

</details>

<details>
<summary>Section 17.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Altarelli–Parisi evolution framework; QCD gluon-to-gluon splitting kernel; Scaling-violation phenomenology from PDF evolution; Collinear splitting factorization and the equivalent-photon distribution.

Records: `peskin-schroeder.qcd-altarelli-parisi-evolution`, `peskin-schroeder.qcd-gluon-splitting-kernel-result`, `peskin-schroeder.qcd-scaling-violation-phenomenology`, `peskin-schroeder.qed-collinear-factorization-and-equivalent-photon`, `peskin-schroeder.qed-collinear-virtuality-and-helicity-kernel`, `peskin-schroeder.qed-gribov-lipatov-kernels`, `peskin-schroeder.qed-normalized-electron-distribution`, `peskin-schroeder.qed-strong-ordering-and-gribov-lipatov-evolution`.

</details>

<details>
<summary>Section 17.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Independent alpha_s determinations in a common convention.

Records: `peskin-schroeder.qcd-independent-alpha-s-determinations`.

</details>

<details>
<summary>Section 17.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 17.1(b): scheme independence of the first two beta coefficients; Problem 17.1(a): two-loop QCD running coupling; Problem 17.2(b): energy-ordering test of gluon spin; Problem 17.2(a): scalar-gluon qqS three-body cross section.

Records: `peskin-schroeder.problem-17-1-scheme-independent-two-loop-asymptotics`, `peskin-schroeder.problem-17-1-two-loop-rg-integration`, `peskin-schroeder.problem-17-2-gluon-spin-discrimination`, `peskin-schroeder.problem-17-2-scalar-gluon-three-body-rate`, `peskin-schroeder.problem-17-3a-qqbar-to-gg-helicity-cross-section`, `peskin-schroeder.problem-17-3b-gg-to-gg-helicity-cross-section`, `peskin-schroeder.problem-17-4-gluon-splitting-kernel`, `peskin-schroeder.problem-17-5-heavy-quark-photoproduction`, `peskin-schroeder.problem-17-6a-small-x-evolution-variable`, `peskin-schroeder.problem-17-6b-small-x-gluon-asymptotic`, `peskin-schroeder.problem-17-6c-small-x-quark-from-gluons`, `peskin-schroeder.problem-17-6d-small-x-distribution-sketch`.

</details>

<details>
<summary>Section 18 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Altarelli-Parisi moments equal twist-two anomalous dimensions; Isospin eigenoperators and hard-QCD Delta-I enhancement; DIS form factors and the parton-model Callan-Gross relation; DIS dispersion relation and moment sum rules.

Records: `peskin-schroeder.ap-moment-anomalous-dimension-equivalence`, `peskin-schroeder.delta-i-half-weak-eigenoperator-rescaling`, `peskin-schroeder.dis-current-conservation-form-factors-and-parton-callan-gross`, `peskin-schroeder.dis-dispersion-moment-sum-rules`, `peskin-schroeder.dis-forward-compton-optical-theorem`, `peskin-schroeder.dis-n2-energy-momentum-conservation-and-asymptotic-fractions`, `peskin-schroeder.dis-ope-pdf-definition-and-leading-callan-gross`, `peskin-schroeder.dis-twist-power-counting-and-flavor-separation`, `peskin-schroeder.dis-twist-two-quark-ope`, `peskin-schroeder.eplus-eminus-hadrons-optical-current-correlator`, `peskin-schroeder.eplus-eminus-ope-vacuum-power-corrections`, `peskin-schroeder.gluon-twist-two-operators-odd-n-total-derivative`, `peskin-schroeder.itep-dispersion-sum-rules-and-local-duality-limit`, `peskin-schroeder.nonleptonic-weak-operator-mixing-and-w-cutoff`, `peskin-schroeder.ope-local-expansion-and-universality`, `peskin-schroeder.ope-operator-mixing-matrix-equation`, `peskin-schroeder.ope-rg-coefficients-and-fixed-point-scaling`, `peskin-schroeder.qcd-gauge-invariant-operator-log-rescaling`, `peskin-schroeder.qcd-quark-mass-effective-running`, `peskin-schroeder.qcd-quark-mass-operator-renormalization`, `peskin-schroeder.quark-twist-two-anomalous-dimension`, `peskin-schroeder.semileptonic-weak-current-qcd-protection`, `peskin-schroeder.twist-two-quark-gluon-mixing-matrix`, `peskin-schroeder.weak-cabibbo-four-fermion-effective-vertices`.

</details>

<details>
<summary>Section 18.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Leading-log rescaling of a gauge-invariant QCD operator; Effective running quark mass; Quark mass-operator renormalization and current check.

Records: `peskin-schroeder.qcd-gauge-invariant-operator-log-rescaling`, `peskin-schroeder.qcd-quark-mass-effective-running`, `peskin-schroeder.qcd-quark-mass-operator-renormalization`.

</details>

<details>
<summary>Section 18.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Isospin eigenoperators and hard-QCD Delta-I enhancement; Nonleptonic weak-operator mixing below the W scale; QCD protection of a semileptonic weak current; Cabibbo-rotated weak effective vertices.

Records: `peskin-schroeder.delta-i-half-weak-eigenoperator-rescaling`, `peskin-schroeder.nonleptonic-weak-operator-mixing-and-w-cutoff`, `peskin-schroeder.semileptonic-weak-current-qcd-protection`, `peskin-schroeder.weak-cabibbo-four-fermion-effective-vertices`.

</details>

<details>
<summary>Section 18.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Isospin eigenoperators and hard-QCD Delta-I enhancement; Wilson operator product expansion; RG equation and scaling of OPE coefficients.

Records: `peskin-schroeder.delta-i-half-weak-eigenoperator-rescaling`, `peskin-schroeder.ope-local-expansion-and-universality`, `peskin-schroeder.ope-rg-coefficients-and-fixed-point-scaling`.

</details>

<details>
<summary>Section 18.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: e-plus-e-minus hadron rate from the current correlator; OPE power corrections to the inclusive hadronic rate; ITEP dispersion sum rules and their limitation; Matrix RG equation for mixed OPE operators.

Records: `peskin-schroeder.eplus-eminus-hadrons-optical-current-correlator`, `peskin-schroeder.eplus-eminus-ope-vacuum-power-corrections`, `peskin-schroeder.itep-dispersion-sum-rules-and-local-duality-limit`, `peskin-schroeder.ope-operator-mixing-matrix-equation`.

</details>

<details>
<summary>Section 18.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Altarelli-Parisi moments equal twist-two anomalous dimensions; DIS form factors and the parton-model Callan-Gross relation; DIS dispersion relation and moment sum rules; DIS hadronic tensor from forward Compton scattering.

Records: `peskin-schroeder.ap-moment-anomalous-dimension-equivalence`, `peskin-schroeder.dis-current-conservation-form-factors-and-parton-callan-gross`, `peskin-schroeder.dis-dispersion-moment-sum-rules`, `peskin-schroeder.dis-forward-compton-optical-theorem`, `peskin-schroeder.dis-n2-energy-momentum-conservation-and-asymptotic-fractions`, `peskin-schroeder.dis-ope-pdf-definition-and-leading-callan-gross`, `peskin-schroeder.dis-twist-power-counting-and-flavor-separation`, `peskin-schroeder.dis-twist-two-quark-ope`, `peskin-schroeder.gluon-twist-two-operators-odd-n-total-derivative`, `peskin-schroeder.itep-dispersion-sum-rules-and-local-duality-limit`, `peskin-schroeder.quark-twist-two-anomalous-dimension`, `peskin-schroeder.twist-two-quark-gluon-mixing-matrix`.

</details>

<details>
<summary>Section 18.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 18.1: proton-decay lifetime and QCD enhancement; Problem 18.2: parity-violating DIS and odd moments; Problem 18.3: gluon twist-two anomalous-dimension calculation; Problem 18.4: photon structure functions from QED and QCD evolution.

Records: `peskin-schroeder.problem-18-1-proton-decay-operator-running`, `peskin-schroeder.problem-18-2-parity-violating-dis-form-factor`, `peskin-schroeder.problem-18-3-gluon-twist-two-counterterms`, `peskin-schroeder.problem-18-4-photon-dis-structure-functions`.

</details>

<details>
<summary>Section 19 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Adler-Bell-Jackiw axial anomaly; Triangle derivation of the ABJ anomaly in dimensional regularization; Anomaly pole and soft-pion order-of-limits; Bounded gamma-five prescription for chiral gauge calculations.

Records: `peskin-schroeder.abj-anomaly-operator-equation`, `peskin-schroeder.abj-triangle-dimensional-gamma5-route`, `peskin-schroeder.anomaly-pole-order-of-limits`, `peskin-schroeder.chiral-gauge-gamma5-calculation-prescription`, `peskin-schroeder.chiral-gauge-theory-left-handed-couplings`, `peskin-schroeder.classical-scale-current-and-improved-stress-tensor`, `peskin-schroeder.fujikawa-chiral-measure-jacobian`, `peskin-schroeder.fujikawa-even-dimensional-anomaly`, `peskin-schroeder.gauge-anomaly-group-coefficient`, `peskin-schroeder.gauge-invariant-point-split-axial-current`, `peskin-schroeder.goldberger-treiman-pion-nucleon-relation`, `peskin-schroeder.pi0-two-photon-anomaly-decay`, `peskin-schroeder.pion-decay-constant-axial-current-pole`, `peskin-schroeder.pion-pseudo-goldstone-mass-and-isospin`, `peskin-schroeder.qcd-chiral-condensate-and-pions`, `peskin-schroeder.qcd-chiral-flavor-symmetry-and-currents`, `peskin-schroeder.real-representations-and-mixed-gravitational-anomaly`, `peskin-schroeder.schwinger-model-photon-mass`, `peskin-schroeder.su2-no-local-cubic-anomaly`, `peskin-schroeder.sun-anomaly-representation-tests`, `peskin-schroeder.trace-anomaly-beta-function`, `peskin-schroeder.trace-anomaly-regulator-limit`, `peskin-schroeder.two-dimensional-anomaly-spectral-flow`, `peskin-schroeder.two-dimensional-axial-anomaly-gauge-choice`, `peskin-schroeder.two-dimensional-chiral-qed-representation`.

</details>

<details>
<summary>Section 19.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Gauge-invariant point splitting of a composite axial current; Schwinger-model vacuum polarization and photon mass; Global anomaly from adiabatic spectral flow; Two-dimensional axial anomaly as a gauge-invariance tradeoff.

Records: `peskin-schroeder.gauge-invariant-point-split-axial-current`, `peskin-schroeder.schwinger-model-photon-mass`, `peskin-schroeder.two-dimensional-anomaly-spectral-flow`, `peskin-schroeder.two-dimensional-axial-anomaly-gauge-choice`, `peskin-schroeder.two-dimensional-chiral-qed-representation`.

</details>

<details>
<summary>Section 19.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Adler-Bell-Jackiw axial anomaly; Triangle derivation of the ABJ anomaly in dimensional regularization; Fujikawa Jacobian for a local chiral rotation.

Records: `peskin-schroeder.abj-anomaly-operator-equation`, `peskin-schroeder.abj-triangle-dimensional-gamma5-route`, `peskin-schroeder.fujikawa-chiral-measure-jacobian`.

</details>

<details>
<summary>Section 19.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Anomaly pole and soft-pion order-of-limits; Fujikawa Jacobian for a local chiral rotation; Even-dimensional Fujikawa anomaly form; Goldberger-Treiman relation from an axial-current pole.

Records: `peskin-schroeder.anomaly-pole-order-of-limits`, `peskin-schroeder.fujikawa-chiral-measure-jacobian`, `peskin-schroeder.fujikawa-even-dimensional-anomaly`, `peskin-schroeder.goldberger-treiman-pion-nucleon-relation`, `peskin-schroeder.pi0-two-photon-anomaly-decay`, `peskin-schroeder.pion-decay-constant-axial-current-pole`, `peskin-schroeder.pion-pseudo-goldstone-mass-and-isospin`, `peskin-schroeder.qcd-chiral-condensate-and-pions`, `peskin-schroeder.qcd-chiral-flavor-symmetry-and-currents`.

</details>

<details>
<summary>Section 19.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bounded gamma-five prescription for chiral gauge calculations; Chiral gauge theory and left-handed matter; Cubic gauge-anomaly group coefficient; Real representations and mixed gravitational U(1) constraint.

Records: `peskin-schroeder.chiral-gauge-gamma5-calculation-prescription`, `peskin-schroeder.chiral-gauge-theory-left-handed-couplings`, `peskin-schroeder.gauge-anomaly-group-coefficient`, `peskin-schroeder.real-representations-and-mixed-gravitational-anomaly`, `peskin-schroeder.su2-no-local-cubic-anomaly`, `peskin-schroeder.sun-anomaly-representation-tests`.

</details>

<details>
<summary>Section 19.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bounded gamma-five prescription for chiral gauge calculations; Scale current and stated stress-tensor qualification; Trace anomaly governed by the beta function; Regulator-dependent derivations, regulator-independent anomaly.

Records: `peskin-schroeder.chiral-gauge-gamma5-calculation-prescription`, `peskin-schroeder.classical-scale-current-and-improved-stress-tensor`, `peskin-schroeder.trace-anomaly-beta-function`, `peskin-schroeder.trace-anomaly-regulator-limit`.

</details>

<details>
<summary>Section 19.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 19.1(a): global E-parallel-B anomaly law; Problem 19.1(b): Weyl Hamiltonian in parallel fields; Problem 19.1(c): Landau-level reduction of a Weyl fermion; Problem 19.1(d): finite-box Landau degeneracy.

Records: `peskin-schroeder.problem-19-1a-global-eb-anomaly`, `peskin-schroeder.problem-19-1b-weyl-hamiltonian`, `peskin-schroeder.problem-19-1c-landau-level-spectrum`, `peskin-schroeder.problem-19-1d-landau-degeneracy`, `peskin-schroeder.problem-19-1e-spectral-flow-check`, `peskin-schroeder.problem-19-2a-pion-weak-amplitude`, `peskin-schroeder.problem-19-2b-pion-helicity-suppression`, `peskin-schroeder.problem-19-3a-product-anomaly-coefficients`, `peskin-schroeder.problem-19-3bc-sun-tensor-anomalies`, `peskin-schroeder.problem-19-4ab-heavy-mass-anomaly-limits`, `peskin-schroeder.problem-19-4cd-heavy-mass-loop-checks`, `peskin-schroeder.trace-anomaly-regulator-limit`.

</details>

<details>
<summary>Section 20 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Abelian Higgs mechanism; CKM charged-current mixing and physical CP phase; Current-algebra construction of the Higgs mass matrix; Custodial symmetry and the rho mass relation.

Records: `peskin-schroeder.abelian-higgs-mechanism`, `peskin-schroeder.ckm-matrix-and-physical-cp-phase`, `peskin-schroeder.current-algebra-higgs-mass-construction`, `peskin-schroeder.custodial-symmetry-rho-relation`, `peskin-schroeder.electroweak-charged-neutral-current-couplings`, `peskin-schroeder.electroweak-precision-observables-and-radiative-corrections`, `peskin-schroeder.electroweak-su2-u1-hypercharge-assignments`, `peskin-schroeder.electroweak-wz-photon-mixing-masses`, `peskin-schroeder.fermi-constant-from-w-exchange`, `peskin-schroeder.gim-neutral-current-flavor-conservation`, `peskin-schroeder.higgs-decay-phenomenology-and-mass-bounds`, `peskin-schroeder.higgs-mechanism-superconducting-meissner-application`, `peskin-schroeder.higgs-transverse-polarization-and-unitarity-gauge`, `peskin-schroeder.lepton-yukawa-diagonalization-and-flavor-conservation`, `peskin-schroeder.nonabelian-higgs-mass-matrix`, `peskin-schroeder.sm-discrete-symmetries-and-single-higgs-yukawas`, `peskin-schroeder.standard-model-gauge-anomaly-cancellation`, `peskin-schroeder.standard-model-higgs-potential-and-mass`, `peskin-schroeder.standard-model-yukawa-masses-and-higgs-couplings`, `peskin-schroeder.su2-adjoint-higgs-to-u1`, `peskin-schroeder.su2-doublet-higgs-complete-breaking`, `peskin-schroeder.su3-adjoint-higgs-breaking-patterns`, `peskin-schroeder.su3-adjoint-higgs-exact-mass-spectra`, `peskin-schroeder.theta-terms-chiral-rotations-and-strong-cp`, `peskin-schroeder.yukawa-singular-value-diagonalization-and-mass-basis`, `peskin-schroeder.z-polarization-asymmetry`.

</details>

<details>
<summary>Section 20.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Abelian Higgs mechanism; Current-algebra construction of the Higgs mass matrix; Higgs mechanism and the Meissner effect; Goldstone pole, transversality, and unitarity gauge.

Records: `peskin-schroeder.abelian-higgs-mechanism`, `peskin-schroeder.current-algebra-higgs-mass-construction`, `peskin-schroeder.higgs-mechanism-superconducting-meissner-application`, `peskin-schroeder.higgs-transverse-polarization-and-unitarity-gauge`, `peskin-schroeder.nonabelian-higgs-mass-matrix`, `peskin-schroeder.su2-adjoint-higgs-to-u1`, `peskin-schroeder.su2-doublet-higgs-complete-breaking`, `peskin-schroeder.su3-adjoint-higgs-breaking-patterns`, `peskin-schroeder.su3-adjoint-higgs-exact-mass-spectra`.

</details>

<details>
<summary>Section 20.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Current-algebra construction of the Higgs mass matrix; Electroweak charged and neutral currents; Electroweak precision relations and radiative corrections; Electroweak SU(2)_L x U(1)_Y representations.

Records: `peskin-schroeder.current-algebra-higgs-mass-construction`, `peskin-schroeder.electroweak-charged-neutral-current-couplings`, `peskin-schroeder.electroweak-precision-observables-and-radiative-corrections`, `peskin-schroeder.electroweak-su2-u1-hypercharge-assignments`, `peskin-schroeder.electroweak-wz-photon-mixing-masses`, `peskin-schroeder.fermi-constant-from-w-exchange`, `peskin-schroeder.higgs-decay-phenomenology-and-mass-bounds`, `peskin-schroeder.standard-model-gauge-anomaly-cancellation`, `peskin-schroeder.standard-model-higgs-potential-and-mass`, `peskin-schroeder.standard-model-yukawa-masses-and-higgs-couplings`, `peskin-schroeder.z-polarization-asymmetry`.

</details>

<details>
<summary>Section 20.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: CKM charged-current mixing and physical CP phase; Custodial symmetry and the rho mass relation; Flavor-diagonal neutral currents and loop-suppressed flavor change; General Higgs-sector requirements and custodial relation.

Records: `peskin-schroeder.ckm-matrix-and-physical-cp-phase`, `peskin-schroeder.custodial-symmetry-rho-relation`, `peskin-schroeder.gim-neutral-current-flavor-conservation`, `peskin-schroeder.higgs-decay-phenomenology-and-mass-bounds`, `peskin-schroeder.lepton-yukawa-diagonalization-and-flavor-conservation`, `peskin-schroeder.sm-discrete-symmetries-and-single-higgs-yukawas`, `peskin-schroeder.theta-terms-chiral-rotations-and-strong-cp`, `peskin-schroeder.yukawa-singular-value-diagonalization-and-mass-basis`.

</details>

<details>
<summary>Section 20.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 20.1: SU(5) adjoint breaking spectrum; Problem 20.2(a): W partial and total widths; Problem 20.2(b): Z partial widths and branching fractions; Problem 20.3(a): photon--Z interference cross section.

Records: `peskin-schroeder.problem-20-1-su5-breaking-spectrum`, `peskin-schroeder.problem-20-2a-w-decay-widths`, `peskin-schroeder.problem-20-2b-z-decay-widths`, `peskin-schroeder.problem-20-3a-z-interference-cross-section`, `peskin-schroeder.problem-20-3bc-forward-backward-asymmetry`, `peskin-schroeder.problem-20-3d-z-peak-invisible-modes`, `peskin-schroeder.problem-20-4a-neutral-current-dis`, `peskin-schroeder.problem-20-4b-isoscalar-ratios`, `peskin-schroeder.problem-20-4c-weinberg-nose`, `peskin-schroeder.problem-20-5ab-two-higgs-vacuum`, `peskin-schroeder.problem-20-5c-charged-higgs-mode`, `peskin-schroeder.problem-20-5d-charged-higgs-quark-couplings`.

</details>

<details>
<summary>Section 21 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Chiral fermion vacuum-polarization calculation; Left-handed e-plus e-minus to longitudinal W-pair cancellation; Right-handed e-plus e-minus to longitudinal W-pair limit; Scalar reference amplitudes for e-plus e-minus to phi-plus phi-minus.

Records: `peskin-schroeder.chiral-fermion-vacuum-polarization-route`, `peskin-schroeder.eeww-left-handed-unitarity-cancellation`, `peskin-schroeder.eeww-right-handed-longitudinal-cancellation`, `peskin-schroeder.eeww-scalar-reference-amplitudes`, `peskin-schroeder.electroweak-natural-relations-from-observables`, `peskin-schroeder.goldstone-equivalence-cut-cancellation-route`, `peskin-schroeder.goldstone-equivalence-theorem`, `peskin-schroeder.goldstone-equivalence-ward-route`, `peskin-schroeder.heavy-doublet-oblique-approximation`, `peskin-schroeder.longitudinal-vector-polarization-kinematics`, `peskin-schroeder.massive-vector-high-energy-consistency`, `peskin-schroeder.nonabelian-rxi-gauge-fixing-matrices`, `peskin-schroeder.nonabelian-rxi-ghosts-and-gws-specialization`, `peskin-schroeder.rxi-abelian-gauge-fixing`, `peskin-schroeder.rxi-abelian-propagators-and-ghost`, `peskin-schroeder.rxi-gauge-limits-and-proof-boundary`, `peskin-schroeder.rxi-tree-gauge-parameter-cancellation`, `peskin-schroeder.source-era-top-mass-precision-comparison`, `peskin-schroeder.top-bottom-divergence-check-and-heavy-top-effect`, `peskin-schroeder.top-to-goldstone-b-route`, `peskin-schroeder.top-to-wb-width-and-longitudinal-enhancement`, `peskin-schroeder.weak-angle-scheme-differences-and-finiteness`, `peskin-schroeder.weak-vacuum-polarization-observable-map`.

</details>

<details>
<summary>Section 21.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Non-Abelian R-xi gauge fixing from the F matrix; Non-Abelian R-xi ghosts and GWS mass eigenstates; Abelian R-xi gauge fixing after symmetry breaking; Abelian R-xi spectrum, propagators, and ghost coupling.

Records: `peskin-schroeder.nonabelian-rxi-gauge-fixing-matrices`, `peskin-schroeder.nonabelian-rxi-ghosts-and-gws-specialization`, `peskin-schroeder.rxi-abelian-gauge-fixing`, `peskin-schroeder.rxi-abelian-propagators-and-ghost`, `peskin-schroeder.rxi-gauge-limits-and-proof-boundary`, `peskin-schroeder.rxi-tree-gauge-parameter-cancellation`.

</details>

<details>
<summary>Section 21.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Left-handed e-plus e-minus to longitudinal W-pair cancellation; Right-handed e-plus e-minus to longitudinal W-pair limit; Scalar reference amplitudes for e-plus e-minus to phi-plus phi-minus; Cut-state cancellation route to equivalence.

Records: `peskin-schroeder.eeww-left-handed-unitarity-cancellation`, `peskin-schroeder.eeww-right-handed-longitudinal-cancellation`, `peskin-schroeder.eeww-scalar-reference-amplitudes`, `peskin-schroeder.goldstone-equivalence-cut-cancellation-route`, `peskin-schroeder.goldstone-equivalence-theorem`, `peskin-schroeder.goldstone-equivalence-ward-route`, `peskin-schroeder.longitudinal-vector-polarization-kinematics`, `peskin-schroeder.massive-vector-high-energy-consistency`, `peskin-schroeder.nonabelian-rxi-ghosts-and-gws-specialization`, `peskin-schroeder.top-to-goldstone-b-route`, `peskin-schroeder.top-to-wb-width-and-longitudinal-enhancement`.

</details>

<details>
<summary>Section 21.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Chiral fermion vacuum-polarization calculation; Electroweak natural relations and observable weak angles; Heavy-doublet oblique approximation; Gauge origin of good high-energy massive-vector behavior.

Records: `peskin-schroeder.chiral-fermion-vacuum-polarization-route`, `peskin-schroeder.electroweak-natural-relations-from-observables`, `peskin-schroeder.heavy-doublet-oblique-approximation`, `peskin-schroeder.massive-vector-high-energy-consistency`, `peskin-schroeder.source-era-top-mass-precision-comparison`, `peskin-schroeder.top-bottom-divergence-check-and-heavy-top-effect`, `peskin-schroeder.weak-angle-scheme-differences-and-finiteness`, `peskin-schroeder.weak-vacuum-polarization-observable-map`.

</details>

<details>
<summary>Section 21.problems — covered</summary>

The retained records include the source's substantial independent task branches and their linked inputs; semantic matching against evidence sections and summaries covers: Problem 21.1: weak contribution to the muon anomalous moment; Problem 21.2: complete W-pair helicity analysis; Problem 21.3: d anti-u to W-minus photon radiation zero; Problem 21.4: Higgs-mass dependence of radiative corrections.

Records: `peskin-schroeder.problem-21-1-weak-muon-anomalous-moment`, `peskin-schroeder.problem-21-2-ww-helicity-amplitudes`, `peskin-schroeder.problem-21-3-dubar-to-wgamma-radiation-zero`, `peskin-schroeder.problem-21-4-higgs-mass-oblique-corrections`.

</details>

<details>
<summary>Section 21.project — covered</summary>

The project records represent the substantive Higgs-decay branches on pp. 775–777. The exact inspected p. 779 render contains only the centered Epilogue heading and has no teachable claim; pp. 778 and 780 remain separately accepted publisher-only exclusions.

Records: `peskin-schroeder.gluon-fusion-higgs-production-project-task`, `peskin-schroeder.higgs-decay-branching-fraction-synthesis-task`, `peskin-schroeder.higgs-decay-form-factors-numerical-project-task`, `peskin-schroeder.higgs-decay-project-model-and-source-era-inputs`, `peskin-schroeder.higgs-to-diphoton-fermion-loop-task`, `peskin-schroeder.higgs-to-diphoton-w-loop-task`, `peskin-schroeder.higgs-to-fermion-pairs-and-leading-log-qcd-task`, `peskin-schroeder.higgs-to-gluons-loop-and-form-factor-task`, `peskin-schroeder.higgs-to-vector-pairs-goldstone-check-task`.

</details>

<details>
<summary>Section 22 — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Bethe ansatz from two-spin scattering; Broken-supersymmetry source-era route to hierarchy and unification; Composite-Higgs source-era route; Conditional RG bridge from asymptotic freedom to confinement.

Records: `peskin-schroeder.bethe-ansatz-factorized-many-spin-states`, `peskin-schroeder.broken-supersymmetry-source-era-hierarchy-route`, `peskin-schroeder.composite-higgs-source-era-route`, `peskin-schroeder.conditional-rg-bridge-to-confinement`, `peskin-schroeder.confining-string-limit-and-quantitative-limit`, `peskin-schroeder.cosmological-constant-proposed-possibilities-qualified`, `peskin-schroeder.cosmological-constant-source-era-puzzle`, `peskin-schroeder.elementary-higgs-source-era-route`, `peskin-schroeder.euclidean-instantons-as-quantum-processes`, `peskin-schroeder.flavor-and-cp-source-era-open-questions`, `peskin-schroeder.gauge-hierarchy-naturalness-problem`, `peskin-schroeder.grand-unification-running-hypothesis`, `peskin-schroeder.higgs-sector-electroweak-breaking-outcome`, `peskin-schroeder.lattice-qcd-continuum-and-monte-carlo-route`, `peskin-schroeder.planck-scale-and-unification-proximity`, `peskin-schroeder.planck-scale-quantum-gravity-limit`, `peskin-schroeder.spatial-solitons-and-monopoles-as-particle-states`, `peskin-schroeder.string-theory-source-era-proposal-and-effective-qft`, `peskin-schroeder.supersymmetric-multiplets-and-gauginos`, `peskin-schroeder.supersymmetric-vacuum-zero-energy`, `peskin-schroeder.supersymmetry-algebra-spectrum-pairing`, `peskin-schroeder.supersymmetry-scalar-radiative-cancellation`, `peskin-schroeder.two-dimensional-bosonization-and-thirring-fixed-line`, `peskin-schroeder.two-dimensional-conformal-fixed-points-and-wzw-example`, `peskin-schroeder.wilson-loop-area-law-static-potential`.

</details>

<details>
<summary>Section 22.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Conditional RG bridge from asymptotic freedom to confinement; Confining-string picture and its stated quantitative limitation; Lattice QCD continuum and Monte Carlo route; Wilson-loop area law and static confinement potential.

Records: `peskin-schroeder.conditional-rg-bridge-to-confinement`, `peskin-schroeder.confining-string-limit-and-quantitative-limit`, `peskin-schroeder.lattice-qcd-continuum-and-monte-carlo-route`, `peskin-schroeder.wilson-loop-area-law-static-potential`.

</details>

<details>
<summary>Section 22.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Composite-Higgs source-era route; Cosmological-constant source-era puzzle; Elementary-Higgs source-era route; Flavor and CP-pattern source-era open questions.

Records: `peskin-schroeder.composite-higgs-source-era-route`, `peskin-schroeder.cosmological-constant-source-era-puzzle`, `peskin-schroeder.elementary-higgs-source-era-route`, `peskin-schroeder.flavor-and-cp-source-era-open-questions`, `peskin-schroeder.gauge-hierarchy-naturalness-problem`, `peskin-schroeder.grand-unification-running-hypothesis`, `peskin-schroeder.higgs-sector-electroweak-breaking-outcome`, `peskin-schroeder.planck-scale-and-unification-proximity`.

</details>

<details>
<summary>Section 22.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Bethe ansatz from two-spin scattering; Qualified proposed possibilities for the cosmological constant; Cosmological-constant source-era puzzle; Euclidean instantons as quantum processes.

Records: `peskin-schroeder.bethe-ansatz-factorized-many-spin-states`, `peskin-schroeder.cosmological-constant-proposed-possibilities-qualified`, `peskin-schroeder.cosmological-constant-source-era-puzzle`, `peskin-schroeder.euclidean-instantons-as-quantum-processes`, `peskin-schroeder.spatial-solitons-and-monopoles-as-particle-states`, `peskin-schroeder.two-dimensional-bosonization-and-thirring-fixed-line`, `peskin-schroeder.two-dimensional-conformal-fixed-points-and-wzw-example`.

</details>

<details>
<summary>Section 22.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Broken-supersymmetry source-era route to hierarchy and unification; Supersymmetric multiplets and gauginos; Supersymmetric vacuum zero energy; Supersymmetry algebra and boson--fermion spectrum pairing.

Records: `peskin-schroeder.broken-supersymmetry-source-era-hierarchy-route`, `peskin-schroeder.supersymmetric-multiplets-and-gauginos`, `peskin-schroeder.supersymmetric-vacuum-zero-energy`, `peskin-schroeder.supersymmetry-algebra-spectrum-pairing`, `peskin-schroeder.supersymmetry-scalar-radiative-cancellation`.

</details>

<details>
<summary>Section 22.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Broken-supersymmetry source-era route to hierarchy and unification; Planck-scale quantum-gravity limit; String-theory source-era proposal and effective QFT.

Records: `peskin-schroeder.broken-supersymmetry-source-era-hierarchy-route`, `peskin-schroeder.planck-scale-quantum-gravity-limit`, `peskin-schroeder.string-theory-source-era-proposal-and-effective-qft`.

</details>

<details>
<summary>Section A — covered</summary>

This is a roll-up of section-matched source records rather than a separate heading node. Semantic matching against each record's evidence section and summary covers: Appendix cross-section, decay-rate, and two-body phase-space formulae; Appendix scalar and QED rule conventions; Appendix dimensional-regularization integral table and branch prescription; Appendix spinor and polarization conventions.

Records: `peskin-schroeder.appendix-cross-section-phase-space-reference`, `peskin-schroeder.appendix-diagrammatic-conventions`, `peskin-schroeder.appendix-dimensional-regularization-branch-prescription`, `peskin-schroeder.appendix-external-particle-and-polarization-conventions`, `peskin-schroeder.appendix-natural-unit-conversion-factors`, `peskin-schroeder.appendix-nonabelian-and-ghost-rule-table`, `peskin-schroeder.appendix-numerator-algebra-and-group-identities`, `peskin-schroeder.appendix-source-era-constants-and-estimation-values`.

</details>

<details>
<summary>Section A.1 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix scalar and QED rule conventions; Appendix non-Abelian and ghost Feynman-rule table.

Records: `peskin-schroeder.appendix-diagrammatic-conventions`, `peskin-schroeder.appendix-nonabelian-and-ghost-rule-table`.

</details>

<details>
<summary>Section A.2 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix spinor and polarization conventions; Appendix non-Abelian and ghost Feynman-rule table.

Records: `peskin-schroeder.appendix-external-particle-and-polarization-conventions`, `peskin-schroeder.appendix-nonabelian-and-ghost-rule-table`.

</details>

<details>
<summary>Section A.3 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix numerator algebra and group-identity table.

Records: `peskin-schroeder.appendix-numerator-algebra-and-group-identities`.

</details>

<details>
<summary>Section A.4 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix dimensional-regularization integral table and branch prescription; Appendix numerator algebra and group-identity table.

Records: `peskin-schroeder.appendix-dimensional-regularization-branch-prescription`, `peskin-schroeder.appendix-numerator-algebra-and-group-identities`.

</details>

<details>
<summary>Section A.5 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix cross-section, decay-rate, and two-body phase-space formulae; Appendix dimensional-regularization integral table and branch prescription.

Records: `peskin-schroeder.appendix-cross-section-phase-space-reference`, `peskin-schroeder.appendix-dimensional-regularization-branch-prescription`.

</details>

<details>
<summary>Section A.6 — covered</summary>

The source-matched records represent the subsection's distinct result, method, representation, qualification, or task content; matching used evidence sections and summaries rather than citation overlap alone. Representative coverage: Appendix cross-section, decay-rate, and two-body phase-space formulae; Appendix natural-unit conversion factors; Appendix source-era physical constants, masses, and derived combinations.

Records: `peskin-schroeder.appendix-cross-section-phase-space-reference`, `peskin-schroeder.appendix-natural-unit-conversion-factors`, `peskin-schroeder.appendix-source-era-constants-and-estimation-values`.

</details>
