# Whole-book graph reconciliation

This report records a review of the combined textbook graph after all its source scopes were accepted. Terra/high assessed semantic section coverage, cross-unit dependencies, independent routes, and proof limits. Sol/high independently reviewed that assessment and made the final recorded decision.

The audited baseline contains **483 nodes, 628 edges, and 117 inventory sections**. It is identified by the graph-content digest below. Subsequent source-backed amendments are listed separately; this snapshot is not an automatic review of arbitrary later changes.

`sha256:9485c9110acd0262126fa91d903cafcea0a83c30c885ce50678fe0fb6807f1b3`

The end human audit is **pending**. Shared-graph alignment and cross-volume follow-ups remain separate from this book's audit. See the current [review declaration](review.yaml), [coverage ledger](coverage.yaml), and [scientific decision log](adjudications.yaml).

## Findings and source-backed amendments

### weinberg-1.spin-statistics-statement-proof-and-occupancy-prerequisite

The current necessary use-level occupancy-to-stated-spin-statistics edge overstates minimum mastery: its own rationale says the stated rule explains the anticommutator occupancy algebra, while its failure mode describes lost explanatory context rather than an inability to recognize the stated rule. The later 5.7 locality/spin-sum route derives the general result but has no qualified relationship to the earlier stated-result node, hiding the independent proof route.

**Resolved by accepted unit `reconcile-001`.** Promoted final source-backed amendment; independent later proof/explanatory relation and actual one-loop joint prerequisites retained. See normal public adjudication ledger.

Source context: weinberg-1 pp. 19–20; weinberg-1 pp. 236–238.

### weinberg-1.euler-heisenberg-functional-integral-joint-inputs

The derive-level Euler–Heisenberg matching method integrates out the electron in a one-loop functional integral but is an incoming-edge root. Its construction jointly uses the QED Dirac electromagnetic coupling and the accepted external-Dirac-field determinant/trace-log construction. Omitting both inputs leaves the functional-integral method disconnected from the canonical/path-integral and perturbative routes it actually uses.

**Resolved by accepted unit `reconcile-001`.** Promoted final source-backed amendment; independent later proof/explanatory relation and actual one-loop joint prerequisites retained. See normal public adjudication ledger.

Source context: weinberg-1 pp. 355–356; weinberg-1 pp. 403–413; weinberg-1 pp. 523–524.

## Final audit decisions

**Section 12.2 includes a catalogue evidenced only in section 12.3 because “Table 12.2” was mistaken for a section designation..** Remove weinberg-1.scalar-spinor-photon-renormalizable-catalogue from section 12.2 and retain it in section 12.3.

The record has one accepted evidence citation: section “12.3, Table 12.2” on printed page 518. The coverage inventory bounds section 12.2 at pages 505–515 and section 12.3 at pages 516–524, so page 518 is not a shared boundary with 12.2. “12.2” names the table, not the source section. Removing only the 12.2 entry restores semantic section assignment while preserving the correct 12.3 record, every other corrected section row, and both pending combined-graph issues.

Alternatives considered: Keep the catalogue in both sections 12.2 and 12.3 as shared material. / Keep the catalogue only in section 12.3, following its accepted evidence.

## Cross-unit assessment

- All 483 nodes and 628 edges were read as a single graph. Every edge has existing endpoints and all required relation, level, necessity, rationale, failure-mode, and evidence fields; the necessary-prerequisite subgraph has no directed strongly connected component. This supports usable mastery routing without a mechanically inferred defect from the 39 deliberately independent records.
- The representation route is explicit: Poincare algebra and one-particle irreducible representations support asymptotic multiparticle states, whose S-matrix covariance and unitarity feed cluster/connected-scattering constructions. The Chapter 5 field-intertwiner route is distinct: it turns the same particle representations into causal fields and then supports the massless-vector and local-U(1) material. These are complementary treatments, not duplicates.
- The canonical/Fock route is preserved as a separate foundation for Wick pairing, propagators, constrained gauge theory, and phase-space path integrals. Chapter 9 provides an independent gauge-averaging proof route to the covariant QED propagator; its alternative edge correctly prevents the Chapter 8 heuristic current-conservation discussion from being treated as the sole proof.
- The perturbative route is coherent across Chapters 6, 8, 10–12: propagator/graph counting supports power counting, power counting supports local counterterms and forest subtractions, and the spinor-QED and Ward records specialize the result. The Chapter 11 one-loop calculations are applications with their own renormalization conditions and integral appendix, rather than redundant replacements for Chapter 12.
- The analytic/pole route is also preserved at useful granularity: scattering unitarity and analyticity lead to spectral/dispersion statements and pole factorization; those records feed the external-field bound-state and Lamb-shift treatment. The resonance-pole-to-bound-state-energy-shift edge expresses a shared pole method without collapsing the physically distinct resonance and Coulomb-resummed problems.
- Soft theorems, inclusive rates, KLN qualifications, heavy-source limits, and external-field bound states remain distinct. Their cross-links identify actual use (one-particle poles and heavy-target limits) while retaining the source’s separate soft, infrared, and binding approximations. Exercise records remain methods/tasks with explicit prerequisite inputs, so their independent derivation burden is not silently replaced by surrounding prose.
- The accepted full-007/full-008/full-009/full-010 reconciliations are reflected without reopening closed decisions: the Chapter 9.6 route qualifies the earlier propagator discussion, Chapter 10.4 fixes the common charge scale through photon normalization, and Chapter 12.3 explains the Pauli term as an EFT truncation rather than a symmetry prohibition.
- The correction found two pending combined-graph amendments, not resolved graph facts: the full-001 stated spin-statistics rule versus the full-005 causality derivation, and the full-007/full-008 joint inputs to the full-010 Euler–Heisenberg functional-integral method. The frozen graph remains unchanged while root sends the bounded contexts through the normal source workflow.

## Conventions and proof boundaries

The separately reviewed roman-xxv–xxvi notation source supplies the metric/index, vector, epsilon, gamma/beta and step-function rules; adjoint, complex-conjugation, Hermitian-conjugate and Dirac-bar rules; and the natural-unit, charge, numerical-uncertainty and data-reference conventions. The natural-unit rule explicitly excludes Chapter 1. These records are retained as representations/assumptions, and the spacetime convention is connected to later vector-polarization work without treating notation as a duplicate physical result.

Records: `weinberg-1.spacetime-index-vector-and-dirac-notation`, `weinberg-1.matrix-adjoint-and-dirac-bar-notation`, `weinberg-1.natural-unit-charge-and-uncertainty-conventions`.

The all-subintegration convergence criterion is reported and used to motivate forest subtractions, but the source explicitly directs its proof to outside treatments and states Euclidean asymptotic assumptions. This graph therefore records a qualified imported theorem, not an in-book proof; no recursive literature extraction is warranted here.

Records: `weinberg-1.power-counting-convergence-theorem-scope`, `weinberg-1.bphz-forest-subtractions`.

The within-volume Section 9.6 proof resolves the previously named Coulomb-propagator follow-up under its stated QED and gauge-invariance assumptions. It does not construct the alternative BRST quantization that the source defers to Volume II.

Records: `weinberg-1.qed-coulomb-gauge-constrained-path-integral`, `weinberg-1.abelian-gauge-averaging-covariant-qed-path-integral`, `weinberg-1.path-integral-qed-covariant-photon-propagator-proof`, `weinberg-1.photon-propagator-coulomb-contact-cancellation`.

The p-form result explicitly limits exactness to smoothly contractible regions and notes the multiply-connected caveat. It does not establish global de Rham/cohomological treatment, which remains an outside-volume correspondence question.

Records: `weinberg-1.p-form-exterior-derivative-and-local-exactness`, `weinberg-1.p-form-gauge-duality`.

## Section coverage assessment

These mappings follow the accepted records' section evidence and content. A shared boundary page may contribute to multiple sections; a table number does not determine its section.

<details>
<summary>Section 1 — covered</summary>

Accepted records cover the historical shift from relativistic wave mechanics to quantized fields, including the physical reasons for renormalization and S-matrix observables. The anchor records are Action-at-a-distance alternative to the electromagnetic field; Anomalous magnetic moment as a radiative correction; Bosonic occupation-number states and vacuum energy; Canonical field theory from a local action; Canonical quantization and ladder operators; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.action-at-a-distance-electrodynamics`, `weinberg-1.anomalous-magnetic-moment-radiative-correction`, `weinberg-1.bosonic-fock-space-vacuum-energy`, `weinberg-1.canonical-field-action-formalism`, `weinberg-1.canonical-oscillator-quantization`, `weinberg-1.charge-as-number-difference`, `weinberg-1.de-broglie-matter-waves`, `weinberg-1.dirac-electromagnetic-coupling-spin`, `weinberg-1.dirac-hole-theory`, `weinberg-1.dirac-linearization-clifford-algebra`, `weinberg-1.dirac-positive-probability-current`, `weinberg-1.dirac-spinor-lorentz-covariance`, `weinberg-1.dyson-renormalizability-criterion`, `weinberg-1.effective-field-theory-low-energy-form`, `weinberg-1.fermion-antiparticle-operator-reinterpretation`, `weinberg-1.fermionic-anticommutation-occupancy`, `weinberg-1.feynman-rules-covariant-perturbation`, `weinberg-1.field-commutator-lorentz-invariance`, `weinberg-1.fields-are-not-probability-amplitudes`, `weinberg-1.finite-lowest-order-qed-reactions`, `weinberg-1.fundamental-length-nonlocal-cutoff`, `weinberg-1.hole-theory-limitations`, `weinberg-1.indefinite-metric-state-cancellation`, `weinberg-1.infrared-inclusive-cancellation`, `weinberg-1.interaction-hamiltonian-perturbation-theory`, `weinberg-1.klein-gordon-indefinite-density`, `weinberg-1.klein-gordon-minimal-substitution`, `weinberg-1.lamb-shift-experimental-test`, `weinberg-1.light-by-light-effective-interaction`, `weinberg-1.many-time-formalism-limitation`, `weinberg-1.matrix-mechanics-observable-program`, `weinberg-1.matter-wave-quantization-and-diffraction`, `weinberg-1.negative-energy-instability`, `weinberg-1.nitrogen-14-statistics-and-neutron-model`, `weinberg-1.old-fashioned-perturbation-covariant-equivalence`, `weinberg-1.particle-representations-logical-start`, `weinberg-1.particle-spectrum-framework-limit`, `weinberg-1.pauli-exclusion-and-statistics`, `weinberg-1.pauli-term-symmetry-allowance`, `weinberg-1.pion-muon-resolution-yukawa-meson`, `weinberg-1.positron-antiparticle-evidence`, `weinberg-1.positron-contributions-soften-self-energy`, `weinberg-1.prewar-renormalization-confidence-barrier`, `weinberg-1.quantum-spontaneous-emission`, `weinberg-1.radiation-normal-modes`, `weinberg-1.renormalization-physical-parameters`, `weinberg-1.s-matrix-observable-formalism`, `weinberg-1.scalar-field-particle-antiparticle-operators`, `weinberg-1.spin-orbit-fine-structure`, `weinberg-1.spin-statistics-connection`, `weinberg-1.spin-zero-klein-gordon-legitimacy`, `weinberg-1.uv-self-energy-divergence`, `weinberg-1.vacuum-polarization-charge-shift`, `weinberg-1.vacuum-selects-annihilation-operators`, `weinberg-1.yukawa-massive-mediator-potential`.

</details>

<details>
<summary>Section 1.1 — covered</summary>

Accepted records cover matter waves, Klein–Gordon and Dirac equations, spin, antiparticles, and the limitations of hole theory. The anchor records are de Broglie relations and matter-wave group velocity; Dirac electromagnetic coupling predicts spin and magnetic moment; Dirac hole theory; Dirac linearization and matrix anticommutation relations; Positive probability current for the Dirac equation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.de-broglie-matter-waves`, `weinberg-1.dirac-electromagnetic-coupling-spin`, `weinberg-1.dirac-hole-theory`, `weinberg-1.dirac-linearization-clifford-algebra`, `weinberg-1.dirac-positive-probability-current`, `weinberg-1.dirac-spinor-lorentz-covariance`, `weinberg-1.hole-theory-limitations`, `weinberg-1.klein-gordon-indefinite-density`, `weinberg-1.klein-gordon-minimal-substitution`, `weinberg-1.matrix-mechanics-observable-program`, `weinberg-1.matter-wave-quantization-and-diffraction`, `weinberg-1.negative-energy-instability`, `weinberg-1.pauli-exclusion-and-statistics`, `weinberg-1.pauli-term-symmetry-allowance`, `weinberg-1.positron-antiparticle-evidence`, `weinberg-1.spin-orbit-fine-structure`, `weinberg-1.spin-zero-klein-gordon-legitimacy`.

</details>

<details>
<summary>Section 1.2 — covered</summary>

Accepted records cover normal-mode and canonical field quantization, Fock operators, charge, and the operator meaning of fields. The anchor records are Bosonic occupation-number states and vacuum energy; Canonical field theory from a local action; Canonical quantization and ladder operators; Charge as particle-minus-antiparticle number; Fermion antiparticles from negative-energy operator reinterpretation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bosonic-fock-space-vacuum-energy`, `weinberg-1.canonical-field-action-formalism`, `weinberg-1.canonical-oscillator-quantization`, `weinberg-1.charge-as-number-difference`, `weinberg-1.fermion-antiparticle-operator-reinterpretation`, `weinberg-1.fermionic-anticommutation-occupancy`, `weinberg-1.field-commutator-lorentz-invariance`, `weinberg-1.fields-are-not-probability-amplitudes`, `weinberg-1.finite-lowest-order-qed-reactions`, `weinberg-1.interaction-hamiltonian-perturbation-theory`, `weinberg-1.many-time-formalism-limitation`, `weinberg-1.nitrogen-14-statistics-and-neutron-model`, `weinberg-1.particle-spectrum-framework-limit`, `weinberg-1.pion-muon-resolution-yukawa-meson`, `weinberg-1.quantum-spontaneous-emission`, `weinberg-1.radiation-normal-modes`, `weinberg-1.scalar-field-particle-antiparticle-operators`, `weinberg-1.spin-statistics-connection`, `weinberg-1.vacuum-selects-annihilation-operators`, `weinberg-1.yukawa-massive-mediator-potential`.

</details>

<details>
<summary>Section 1.3 — covered</summary>

Accepted records cover ultraviolet and infrared problems, renormalization, covariant perturbation theory, and historical alternative programs. The anchor records are Action-at-a-distance alternative to the electromagnetic field; Anomalous magnetic moment as a radiative correction; Dyson equivalence and renormalizability criterion; Feynman rules and covariant perturbation theory; Fundamental length and nonlocal ultraviolet cutoff proposals; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.action-at-a-distance-electrodynamics`, `weinberg-1.anomalous-magnetic-moment-radiative-correction`, `weinberg-1.dyson-renormalizability-criterion`, `weinberg-1.feynman-rules-covariant-perturbation`, `weinberg-1.fundamental-length-nonlocal-cutoff`, `weinberg-1.indefinite-metric-state-cancellation`, `weinberg-1.infrared-inclusive-cancellation`, `weinberg-1.lamb-shift-experimental-test`, `weinberg-1.light-by-light-effective-interaction`, `weinberg-1.old-fashioned-perturbation-covariant-equivalence`, `weinberg-1.positron-contributions-soften-self-energy`, `weinberg-1.prewar-renormalization-confidence-barrier`, `weinberg-1.renormalization-physical-parameters`, `weinberg-1.s-matrix-observable-formalism`, `weinberg-1.uv-self-energy-divergence`, `weinberg-1.vacuum-polarization-charge-shift`.

</details>

<details>
<summary>Section 2 — covered</summary>

Accepted records cover quantum symmetries, Poincare representations, helicity, discrete symmetries, projectivity, and the mathematical appendices that prove their qualifications. The anchor records are Exponentiation of Abelian symmetry generators; Born rule for a complete orthogonal set of rays; Central charges as the local algebraic form of projectivity; Conserved momentum, angular momentum, and energy; Continuous symmetries use linear unitary operators; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.abelian-symmetry-exponentiation`, `weinberg-1.born-rule-complete-orthogonal-rays`, `weinberg-1.central-charges-from-projectivity`, `weinberg-1.conserved-poincare-generators`, `weinberg-1.continuous-symmetries-unitary`, `weinberg-1.cpt-and-unconventional-inversion-actions`, `weinberg-1.degenerate-multiplet-parity-and-joint-inversion-degeneracy`, `weinberg-1.degenerate-multiplet-time-reversal-blocks`, `weinberg-1.deprojectivization-theorem`, `weinberg-1.galilean-contraction-and-mass-central-charge`, `weinberg-1.group-operator-path-construction`, `weinberg-1.hermitian-observables-and-eigenstates`, `weinberg-1.hilbert-space-rays`, `weinberg-1.homotopy-classes-classify-global-projective-phases`, `weinberg-1.induced-representations-and-little-groups`, `weinberg-1.lie-algebra-from-local-group-law`, `weinberg-1.lorentz-invariant-one-particle-normalization`, `weinberg-1.lorentz-topology-sign-projective-representations`, `weinberg-1.massive-intrinsic-parity-and-time-reversal`, `weinberg-1.massive-spin-so3-little-group`, `weinberg-1.massive-wigner-rotation`, `weinberg-1.massless-helicity-lorentz-action`, `weinberg-1.massless-helicity-representations`, `weinberg-1.massless-iso2-little-group`, `weinberg-1.massless-parity-helicity-pairing`, `weinberg-1.massless-polarization-lorentz-rotation`, `weinberg-1.massless-time-reversal-preserves-helicity`, `weinberg-1.nonphysical-little-groups-require-infinite-unitary-multiplets`, `weinberg-1.one-particle-irreducible-poincare-states`, `weinberg-1.parity-unitary-time-reversal-antiunitary`, `weinberg-1.poincare-central-charges-removable`, `weinberg-1.poincare-generators`, `weinberg-1.poincare-group-and-lorentz-interval`, `weinberg-1.poincare-lie-algebra`, `weinberg-1.poincare-momentum-orbits-and-vacuum`, `weinberg-1.projective-cocycles`, `weinberg-1.projective-symmetry-representations`, `weinberg-1.proper-orthochronous-lorentz-component`, `weinberg-1.sl2c-double-cover-of-lorentz-group`, `weinberg-1.symmetry-as-transition-probability-invariance`, `weinberg-1.symmetry-generators-as-hermitian-observables`, `weinberg-1.time-reversal-forbids-static-dipoles`, `weinberg-1.time-reversal-square-and-kramers-degeneracy`, `weinberg-1.topological-helicity-quantization-and-covering-choice`, `weinberg-1.unconventional-time-reversal-degeneracy`, `weinberg-1.wigner-symmetry-representation-theorem`, `weinberg-1.wigner-theorem-proof-coefficient-dichotomy`, `weinberg-1.wigner-theorem-proof-operator-conclusion`, `weinberg-1.wigner-theorem-proof-orthonormal-basis`.

</details>

<details>
<summary>Section 2.1 — covered</summary>

Accepted records cover rays, observables, and the Born-rule starting point. The anchor records are Born rule for a complete orthogonal set of rays; Hermitian observables and definite values; Physical states as Hilbert-space rays; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.born-rule-complete-orthogonal-rays`, `weinberg-1.hermitian-observables-and-eigenstates`, `weinberg-1.hilbert-space-rays`.

</details>

<details>
<summary>Section 2.2 — covered</summary>

Accepted records cover transition-probability symmetries, Wigner operators, continuous generators, and projective representations. The anchor records are Exponentiation of Abelian symmetry generators; Born rule for a complete orthogonal set of rays; Continuous symmetries use linear unitary operators; Hermitian observables and definite values; Physical states as Hilbert-space rays; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.abelian-symmetry-exponentiation`, `weinberg-1.born-rule-complete-orthogonal-rays`, `weinberg-1.continuous-symmetries-unitary`, `weinberg-1.hermitian-observables-and-eigenstates`, `weinberg-1.hilbert-space-rays`, `weinberg-1.lie-algebra-from-local-group-law`, `weinberg-1.projective-symmetry-representations`, `weinberg-1.symmetry-as-transition-probability-invariance`, `weinberg-1.symmetry-generators-as-hermitian-observables`, `weinberg-1.wigner-symmetry-representation-theorem`.

</details>

<details>
<summary>Section 2.3 — covered</summary>

Accepted records cover the Poincare group, Lorentz interval, and connected component. The anchor records are Exponentiation of Abelian symmetry generators; Poincaré transformations preserve the Lorentz interval; Proper orthochronous Lorentz subgroup and discrete inversions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.abelian-symmetry-exponentiation`, `weinberg-1.poincare-group-and-lorentz-interval`, `weinberg-1.proper-orthochronous-lorentz-component`.

</details>

<details>
<summary>Section 2.4 — covered</summary>

Accepted records cover Poincare generators, their algebra, and conservation laws. The anchor records are Conserved momentum, angular momentum, and energy; Galilean contraction and mass central charge; Poincaré generators Jμν and Pμ; Poincaré Lie algebra and covariance of generators; Proper orthochronous Lorentz subgroup and discrete inversions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.conserved-poincare-generators`, `weinberg-1.galilean-contraction-and-mass-central-charge`, `weinberg-1.poincare-generators`, `weinberg-1.poincare-lie-algebra`, `weinberg-1.proper-orthochronous-lorentz-component`.

</details>

<details>
<summary>Section 2.5 — covered</summary>

Accepted records cover one-particle Poincare representations, little groups, massive spin, and massless helicity. The anchor records are Galilean contraction and mass central charge; Induced Poincaré representations from little groups; Invariant mass-shell delta and adopted momentum-state normalization; Massive spin from the SO(3) little group and SU(2) cover; Massive-particle Wigner rotations under proper orthochronous transformations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.galilean-contraction-and-mass-central-charge`, `weinberg-1.induced-representations-and-little-groups`, `weinberg-1.lorentz-invariant-one-particle-normalization`, `weinberg-1.massive-spin-so3-little-group`, `weinberg-1.massive-wigner-rotation`, `weinberg-1.massless-helicity-lorentz-action`, `weinberg-1.massless-helicity-representations`, `weinberg-1.massless-iso2-little-group`, `weinberg-1.massless-polarization-lorentz-rotation`, `weinberg-1.nonphysical-little-groups-require-infinite-unitary-multiplets`, `weinberg-1.one-particle-irreducible-poincare-states`, `weinberg-1.poincare-momentum-orbits-and-vacuum`.

</details>

<details>
<summary>Section 2.6 — covered</summary>

Accepted records cover unitary parity and antiunitary time reversal, including their massive and massless qualifications. The anchor records are Massive intrinsic parity and conventional time reversal; Proper-orthochronous Lorentz action on helicity and polarization phase; Parity pairs opposite massless helicities; Proper-orthochronous Lorentz rotation of photon and graviton polarization planes; Time reversal preserves massless helicity; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.massive-intrinsic-parity-and-time-reversal`, `weinberg-1.massless-helicity-lorentz-action`, `weinberg-1.massless-parity-helicity-pairing`, `weinberg-1.massless-polarization-lorentz-rotation`, `weinberg-1.massless-time-reversal-preserves-helicity`, `weinberg-1.parity-unitary-time-reversal-antiunitary`, `weinberg-1.time-reversal-forbids-static-dipoles`, `weinberg-1.time-reversal-square-and-kramers-degeneracy`.

</details>

<details>
<summary>Section 2.7 — covered</summary>

Accepted records cover central charges, deprojectivization, covering groups, and topological helicity quantization. The anchor records are Central charges as the local algebraic form of projectivity; Conditions for eliminating a projective phase; Proper-orthochronous Lorentz topology and representations up to a sign; Massive spin from the SO(3) little group and SU(2) cover; All Poincaré-algebra central charges are removable; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.central-charges-from-projectivity`, `weinberg-1.deprojectivization-theorem`, `weinberg-1.lorentz-topology-sign-projective-representations`, `weinberg-1.massive-spin-so3-little-group`, `weinberg-1.poincare-central-charges-removable`, `weinberg-1.projective-cocycles`, `weinberg-1.sl2c-double-cover-of-lorentz-group`, `weinberg-1.time-reversal-forbids-static-dipoles`, `weinberg-1.time-reversal-square-and-kramers-degeneracy`, `weinberg-1.topological-helicity-quantization-and-covering-choice`.

</details>

<details>
<summary>Section 2.A — covered</summary>

Accepted records cover the constructive proof of Wigner’s unitary-or-antiunitary alternative. The anchor records are Wigner representation of ray symmetries; Proof method: coefficient ratios are preserved or conjugated; Proof conclusion: linear-unitary or antilinear-antiunitary operator; Proof method: transformed orthonormal basis; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.wigner-symmetry-representation-theorem`, `weinberg-1.wigner-theorem-proof-coefficient-dichotomy`, `weinberg-1.wigner-theorem-proof-operator-conclusion`, `weinberg-1.wigner-theorem-proof-orthonormal-basis`.

</details>

<details>
<summary>Section 2.B — covered</summary>

Accepted records cover path construction, phase removal, and homotopy classification of global projective phases. The anchor records are Conditions for eliminating a projective phase; Path construction of finite group operators; Homotopy classes classify global projective phases; Proof conclusion: linear-unitary or antilinear-antiunitary operator; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.deprojectivization-theorem`, `weinberg-1.group-operator-path-construction`, `weinberg-1.homotopy-classes-classify-global-projective-phases`, `weinberg-1.wigner-theorem-proof-operator-conclusion`.

</details>

<details>
<summary>Section 2.C — covered</summary>

Accepted records cover discrete transformations on degenerate multiplets and their inversion qualifications. The anchor records are CPT, CP, and unconventional inversion multiplets; Parity diagonalization and joint parity–time-reversal degeneracy; Time reversal on degenerate multiplets has canonical blocks; Homotopy classes classify global projective phases; Unconventional time reversal can require extra degeneracy; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cpt-and-unconventional-inversion-actions`, `weinberg-1.degenerate-multiplet-parity-and-joint-inversion-degeneracy`, `weinberg-1.degenerate-multiplet-time-reversal-blocks`, `weinberg-1.homotopy-classes-classify-global-projective-phases`, `weinberg-1.unconventional-time-reversal-degeneracy`.

</details>

<details>
<summary>Section 2.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are CPT, CP, and unconventional inversion multiplets; Problem: massive spin and inversions in 2+1 dimensions; Problem: massless spin and inversions in 2+1 dimensions; Problem: derive Galilean algebra and irreducible central charges; Problem: Poincaré Casimirs from Pauli–Lubanski vector; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cpt-and-unconventional-inversion-actions`, `weinberg-1.problem-2plus1-massive-spin`, `weinberg-1.problem-2plus1-massless-spin`, `weinberg-1.problem-galilean-central-charges`, `weinberg-1.problem-poincare-casimirs`, `weinberg-1.problem-transverse-boost-massive-spin-state`, `weinberg-1.problem-transverse-boost-photon-polarization`.

</details>

<details>
<summary>Section 3 — covered</summary>

Accepted records cover asymptotic scattering, unitarity, symmetry constraints, rates, locality, reciprocity, partial waves, and resonances. The anchor records are Angular-momentum coupling and spherical-harmonic orthogonality; Antiunitary time reversal and S-matrix reciprocity; Asymptotic completeness assumption; Asymptotic multiparticle state labels and normalization; Asymptotic overlap proof of S unitarity; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.angular-momentum-coupling-orthogonality`, `weinberg-1.antiunitary-time-reversal-s-matrix-reciprocity`, `weinberg-1.asymptotic-completeness-assumption`, `weinberg-1.asymptotic-multiparticle-state-labels-and-normalization`, `weinberg-1.asymptotic-overlap-unitarity-proof`, `weinberg-1.box-normalization-and-connected-transition-element`, `weinberg-1.breit-wigner-cross-section-and-partial-widths`, `weinberg-1.charge-conjugation-cp-cpt-process-relations`, `weinberg-1.charge-conjugation-neutral-pion-decay-selection`, `weinberg-1.contour-proof-in-out-lippmann-schwinger-boundary-condition`, `weinberg-1.cpt-total-rate-equality-and-antiparticle-lifetime`, `weinberg-1.cross-section-flux-and-invariant-relative-velocity`, `weinberg-1.dalitz-plot-three-body-dynamics-diagnostic`, `weinberg-1.decay-rate-and-narrow-width-validity`, `weinberg-1.decay-rate-lorentz-time-dilation`, `weinberg-1.diagonal-partial-wave-phase-shifts`, `weinberg-1.distorted-wave-born-approximation`, `weinberg-1.dyson-time-ordered-series-result`, `weinberg-1.fourier-energy-denominator-dyson-route`, `weinberg-1.free-hamiltonian-physical-spectrum-assumption`, `weinberg-1.generalized-optical-theorem-from-s-unitarity`, `weinberg-1.generalized-partial-wave-discrete-basis`, `weinberg-1.generator-commutator-criterion-s-matrix-covariance`, `weinberg-1.h-theorem-equilibrium-stationarity-condition`, `weinberg-1.high-energy-boundary-layer-forward-amplitude`, `weinberg-1.high-energy-impact-parameter-disk-and-log-squared-growth`, `weinberg-1.in-out-states-heisenberg-asymptotic-definition`, `weinberg-1.integrated-transition-reciprocity`, `weinberg-1.interacting-boost-smoothness-lorentz-sufficiency`, `weinberg-1.interaction-picture-dyson-series`, `weinberg-1.internal-symmetry-s-matrix-selection-rules`, `weinberg-1.isospin-partial-wave-phase-shifts`, `weinberg-1.isospin-reduced-s-matrix-amplitudes`, `weinberg-1.kinetic-equation-and-probability-conservation`, `weinberg-1.lippmann-schwinger-orthonormality-and-s-unitarity-route`, `weinberg-1.lippmann-schwinger-scattering-state-equations`, `weinberg-1.local-scalar-interaction-microcausality-lorentz-s-matrix`, `weinberg-1.moller-operators-asymptotic-state-map`, `weinberg-1.neutral-kaon-cp-eigenstates-violation-and-t-inference`, `weinberg-1.old-fashioned-perturbation-theory-energy-denominators`, `weinberg-1.optical-theorem-diffraction-peak-bound`, `weinberg-1.parity-angular-momentum-inference-and-weak-violation`, `weinberg-1.parity-s-matrix-covariance-and-intrinsic-phase-freedom`, `weinberg-1.partial-wave-cross-sections-and-multiparticle-inelasticity`, `weinberg-1.partial-wave-threshold-laws-and-scattering-length`, `weinberg-1.proper-orthochronous-s-matrix-covariance-and-conservation`, `weinberg-1.pt-invariance-polarized-beta-decay-constraint`, `weinberg-1.rearrangement-collision-channel-dependent-hamiltonian-splits`, `weinberg-1.resolvent-principal-value-and-delta-decomposition`, `weinberg-1.resonance-isospin-eigenphase-and-background-interference`, `weinberg-1.resonance-long-lived-intermediate-state-mechanisms`, `weinberg-1.resonance-pole-energy-and-decay-width`, `weinberg-1.resonance-unitarity-projector-decomposition`, `weinberg-1.s-matrix-in-out-overlaps-and-unitarity`, `weinberg-1.ss-dagger-unitarity-identity`, `weinberg-1.strangeness-associated-production-and-weak-decay`, `weinberg-1.t-matrix-onshell-s-matrix-relation-and-born-approximation`, `weinberg-1.two-body-angular-momentum-coupled-partial-wave-basis`, `weinberg-1.two-body-phase-space-and-cross-section`, `weinberg-1.unitarity-reciprocity-and-boltzmann-h-theorem`, `weinberg-1.unresolved-resonance-integrated-cross-section`, `weinberg-1.watson-theorem-final-state-phase`.

</details>

<details>
<summary>Section 3.1 — covered</summary>

Accepted records cover asymptotic state assumptions, Møller/Lippmann–Schwinger constructions, and boundary prescriptions. The anchor records are Asymptotic multiparticle state labels and normalization; Contour proof of Lippmann–Schwinger in/out boundary conditions; Free Hamiltonian with physical spectrum; In and out states as asymptotic particle content; Lippmann–Schwinger scattering-state equations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.asymptotic-multiparticle-state-labels-and-normalization`, `weinberg-1.contour-proof-in-out-lippmann-schwinger-boundary-condition`, `weinberg-1.free-hamiltonian-physical-spectrum-assumption`, `weinberg-1.in-out-states-heisenberg-asymptotic-definition`, `weinberg-1.lippmann-schwinger-scattering-state-equations`, `weinberg-1.moller-operators-asymptotic-state-map`, `weinberg-1.rearrangement-collision-channel-dependent-hamiltonian-splits`, `weinberg-1.resolvent-principal-value-and-delta-decomposition`.

</details>

<details>
<summary>Section 3.2 — covered</summary>

Accepted records cover overlap and algebraic routes to S-matrix unitarity and the on-shell T matrix. The anchor records are Asymptotic completeness assumption; Asymptotic overlap proof of S unitarity; Algebraic Lippmann–Schwinger route to orthonormality; Resolvent principal-value and delta decomposition; S-matrix from in–out overlaps and completeness; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.asymptotic-completeness-assumption`, `weinberg-1.asymptotic-overlap-unitarity-proof`, `weinberg-1.lippmann-schwinger-orthonormality-and-s-unitarity-route`, `weinberg-1.resolvent-principal-value-and-delta-decomposition`, `weinberg-1.s-matrix-in-out-overlaps-and-unitarity`, `weinberg-1.t-matrix-onshell-s-matrix-relation-and-born-approximation`.

</details>

<details>
<summary>Section 3.3 — covered</summary>

Accepted records cover Lorentz and internal symmetries of scattering, discrete-symmetry process relations, and time-reversal reciprocity. The anchor records are Antiunitary time reversal and S-matrix reciprocity; C, CP, and CPT process relations; Charge-conjugation selection in neutral-pion decays; Generator commutator criterion for S-matrix covariance; Interacting boost and smoothness sufficient condition; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.antiunitary-time-reversal-s-matrix-reciprocity`, `weinberg-1.charge-conjugation-cp-cpt-process-relations`, `weinberg-1.charge-conjugation-neutral-pion-decay-selection`, `weinberg-1.generator-commutator-criterion-s-matrix-covariance`, `weinberg-1.interacting-boost-smoothness-lorentz-sufficiency`, `weinberg-1.internal-symmetry-s-matrix-selection-rules`, `weinberg-1.isospin-reduced-s-matrix-amplitudes`, `weinberg-1.lippmann-schwinger-orthonormality-and-s-unitarity-route`, `weinberg-1.neutral-kaon-cp-eigenstates-violation-and-t-inference`, `weinberg-1.parity-angular-momentum-inference-and-weak-violation`, `weinberg-1.parity-s-matrix-covariance-and-intrinsic-phase-freedom`, `weinberg-1.proper-orthochronous-s-matrix-covariance-and-conservation`, `weinberg-1.pt-invariance-polarized-beta-decay-constraint`, `weinberg-1.strangeness-associated-production-and-weak-decay`, `weinberg-1.watson-theorem-final-state-phase`.

</details>

<details>
<summary>Section 3.4 — covered</summary>

Accepted records cover connected transition elements, decay and cross-section normalization, flux, and Dalitz diagnostics. The anchor records are Box normalization and connected transition element; C, CP, and CPT process relations; Cross-section, flux, and invariant relative velocity; Dalitz plot as a three-body dynamics diagnostic; Decay rate and narrow-width validity; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.box-normalization-and-connected-transition-element`, `weinberg-1.charge-conjugation-cp-cpt-process-relations`, `weinberg-1.cross-section-flux-and-invariant-relative-velocity`, `weinberg-1.dalitz-plot-three-body-dynamics-diagnostic`, `weinberg-1.decay-rate-and-narrow-width-validity`, `weinberg-1.decay-rate-lorentz-time-dilation`, `weinberg-1.neutral-kaon-cp-eigenstates-violation-and-t-inference`, `weinberg-1.two-body-phase-space-and-cross-section`.

</details>

<details>
<summary>Section 3.5 — covered</summary>

Accepted records cover locality, microcausality, Dyson expansion, and distorted-wave/old-fashioned perturbative routes. The anchor records are Dalitz plot as a three-body dynamics diagnostic; Distorted-wave Born approximation; Dyson time-ordered series; Fourier energy-denominator route to the Dyson series; Interaction-picture route to the Dyson series; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dalitz-plot-three-body-dynamics-diagnostic`, `weinberg-1.distorted-wave-born-approximation`, `weinberg-1.dyson-time-ordered-series-result`, `weinberg-1.fourier-energy-denominator-dyson-route`, `weinberg-1.interaction-picture-dyson-series`, `weinberg-1.local-scalar-interaction-microcausality-lorentz-s-matrix`, `weinberg-1.old-fashioned-perturbation-theory-energy-denominators`.

</details>

<details>
<summary>Section 3.6 — covered</summary>

Accepted records cover optical-theorem consequences, reverse-transition reciprocity, Watson phases, and the H theorem. The anchor records are CPT equality of total rates and antiparticle lifetimes; Distorted-wave Born approximation; Generalized optical theorem from S unitarity; H-theorem equilibrium stationarity condition; Integrated transition reciprocity from the two unitarity identities; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cpt-total-rate-equality-and-antiparticle-lifetime`, `weinberg-1.distorted-wave-born-approximation`, `weinberg-1.generalized-optical-theorem-from-s-unitarity`, `weinberg-1.h-theorem-equilibrium-stationarity-condition`, `weinberg-1.integrated-transition-reciprocity`, `weinberg-1.kinetic-equation-and-probability-conservation`, `weinberg-1.optical-theorem-diffraction-peak-bound`, `weinberg-1.ss-dagger-unitarity-identity`, `weinberg-1.unitarity-reciprocity-and-boltzmann-h-theorem`.

</details>

<details>
<summary>Section 3.7 — covered</summary>

Accepted records cover coupled partial-wave bases, unitarity bounds, phase shifts, and partial-wave cross sections. The anchor records are Angular-momentum coupling and spherical-harmonic orthogonality; Diagonal partial-wave phase shifts; Generalized partial-wave discrete basis; H-theorem equilibrium stationarity condition; High-energy boundary-layer bound on the forward real amplitude; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.angular-momentum-coupling-orthogonality`, `weinberg-1.diagonal-partial-wave-phase-shifts`, `weinberg-1.generalized-partial-wave-discrete-basis`, `weinberg-1.h-theorem-equilibrium-stationarity-condition`, `weinberg-1.high-energy-boundary-layer-forward-amplitude`, `weinberg-1.high-energy-impact-parameter-disk-and-log-squared-growth`, `weinberg-1.isospin-partial-wave-phase-shifts`, `weinberg-1.partial-wave-cross-sections-and-multiparticle-inelasticity`, `weinberg-1.partial-wave-threshold-laws-and-scattering-length`, `weinberg-1.two-body-angular-momentum-coupled-partial-wave-basis`, `weinberg-1.unitarity-reciprocity-and-boltzmann-h-theorem`.

</details>

<details>
<summary>Section 3.8 — covered</summary>

Accepted records cover resonance poles, projector decomposition, Breit–Wigner rates, eigenphases, and unresolved resonance limits. The anchor records are Breit–Wigner cross-section and partial widths; High-energy boundary-layer bound on the forward real amplitude; High-energy opaque disk and log-squared growth; Resonance isospin, eigenphase jumps, and background interference; Resonances from long-lived intermediate states; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.breit-wigner-cross-section-and-partial-widths`, `weinberg-1.high-energy-boundary-layer-forward-amplitude`, `weinberg-1.high-energy-impact-parameter-disk-and-log-squared-growth`, `weinberg-1.resonance-isospin-eigenphase-and-background-interference`, `weinberg-1.resonance-long-lived-intermediate-state-mechanisms`, `weinberg-1.resonance-pole-energy-and-decay-width`, `weinberg-1.resonance-unitarity-projector-decomposition`, `weinberg-1.unresolved-resonance-integrated-cross-section`.

</details>

<details>
<summary>Section 3.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Problem: Dyson expansion from old-fashioned perturbation theory; Problem: S-matrix in terms of the K-matrix; Problem: laboratory-frame two-body cross-section; Problem: pion–proton phase-shift cross-sections; Problem: resonance branching ratio; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.problem-dyson-series-from-old-fashioned-perturbation`, `weinberg-1.problem-k-matrix-s-relation`, `weinberg-1.problem-laboratory-frame-two-body-cross-section`, `weinberg-1.problem-pion-proton-phase-shift-cross-sections`, `weinberg-1.problem-resonance-branching-ratio-and-peak-cross-section`, `weinberg-1.problem-resonance-total-peak-cross-section`, `weinberg-1.problem-separable-interaction-lippmann-schwinger`, `weinberg-1.problem-standing-wave-k-matrix`, `weinberg-1.problem-two-body-partial-wave-normalization`, `weinberg-1.resonance-isospin-eigenphase-and-background-interference`.

</details>

<details>
<summary>Section 4 — covered</summary>

Accepted records cover Fock-space construction, cluster decomposition, connected amplitudes, and multiparticle scattering constraints. The anchor records are Additive observables and the free Hamiltonian in Fock form; Bose–Fermi exchange symmetry and its cluster argument; Bosonic and fermionic Fock brackets; Cluster decomposition forces higher-particle scattering; Cluster decomposition as S-matrix factorization; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.additive-operator-and-free-hamiltonian-form`, `weinberg-1.bose-fermi-exchange-symmetry-cluster-argument`, `weinberg-1.canonical-fock-commutation-relations`, `weinberg-1.cluster-decomposition-forces-multiparticle-scattering`, `weinberg-1.cluster-decomposition-s-matrix-factorization`, `weinberg-1.connected-amplitude-separation-and-single-delta-condition`, `weinberg-1.connected-diagram-perturbative-prescription`, `weinberg-1.connected-graph-delta-counting`, `weinberg-1.connected-multibody-lippmann-schwinger-limitation`, `weinberg-1.connected-s-matrix-recursive-partition`, `weinberg-1.creation-annihilation-actions-on-fock-states`, `weinberg-1.creation-operator-symmetry-transformation-rules`, `weinberg-1.cross-species-exchange-ordering-convention`, `weinberg-1.finite-time-evolution-connected-delta-structure`, `weinberg-1.normal-ordered-creation-annihilation-expansion`, `weinberg-1.perturbative-single-delta-cluster-theorem`, `weinberg-1.single-delta-hamiltonian-coefficient-hypothesis`, `weinberg-1.stable-one-particle-scattering-assumption`.

</details>

<details>
<summary>Section 4.1 — covered</summary>

Accepted records cover exchange symmetry, cross-species ordering, and multiparticle state normalization. The anchor records are Bose–Fermi exchange symmetry and its cluster argument; Cross-species exchange ordering convention; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bose-fermi-exchange-symmetry-cluster-argument`, `weinberg-1.cross-species-exchange-ordering-convention`.

</details>

<details>
<summary>Section 4.2 — covered</summary>

Accepted records cover creation/annihilation actions, Fock brackets, additive observables, and free Hamiltonian form. The anchor records are Additive observables and the free Hamiltonian in Fock form; Bosonic and fermionic Fock brackets; Creation and annihilation actions on Fock states; Symmetry actions on creation operators; Normal-ordered expansion of an arbitrary operator; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.additive-operator-and-free-hamiltonian-form`, `weinberg-1.canonical-fock-commutation-relations`, `weinberg-1.creation-annihilation-actions-on-fock-states`, `weinberg-1.creation-operator-symmetry-transformation-rules`, `weinberg-1.normal-ordered-creation-annihilation-expansion`.

</details>

<details>
<summary>Section 4.3 — covered</summary>

Accepted records cover cluster factorization and the recursive connected S-matrix partition. The anchor records are Cluster decomposition as S-matrix factorization; Connected amplitudes, separation, and the single-delta condition; Recursive connected S-matrix elements; Symmetry actions on creation operators; Stable one-particle scattering assumption; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cluster-decomposition-s-matrix-factorization`, `weinberg-1.connected-amplitude-separation-and-single-delta-condition`, `weinberg-1.connected-s-matrix-recursive-partition`, `weinberg-1.creation-operator-symmetry-transformation-rules`, `weinberg-1.stable-one-particle-scattering-assumption`.

</details>

<details>
<summary>Section 4.4 — covered</summary>

Accepted records cover single-delta connected structures, diagram counting, finite-time limits, and the multibody Lippmann–Schwinger limitation. The anchor records are Cluster decomposition forces higher-particle scattering; Connected amplitudes, separation, and the single-delta condition; Connected-diagram prescription from time-dependent perturbation theory; Graph count proving one momentum delta for a connected contribution; Connected reformulation for multibody Lippmann–Schwinger equations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cluster-decomposition-forces-multiparticle-scattering`, `weinberg-1.connected-amplitude-separation-and-single-delta-condition`, `weinberg-1.connected-diagram-perturbative-prescription`, `weinberg-1.connected-graph-delta-counting`, `weinberg-1.connected-multibody-lippmann-schwinger-limitation`, `weinberg-1.finite-time-evolution-connected-delta-structure`, `weinberg-1.perturbative-single-delta-cluster-theorem`, `weinberg-1.single-delta-hamiltonian-coefficient-hypothesis`.

</details>

<details>
<summary>Section 4.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Problem: first-order bosonic contact scattering; Problem: construct a bosonic coherent state in the Fock basis; Problem: relate full and connected S-matrix generating functionals; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.problem-boson-contact-scattering-order-g`, `weinberg-1.problem-bosonic-coherent-state-fock-construction`, `weinberg-1.problem-connected-s-matrix-generating-functionals`.

</details>

<details>
<summary>Section 5 — covered</summary>

Accepted records cover the particle-to-field construction, causal free fields, discrete transformations, general fields, and CPT. The anchor records are Antiparticles from charge-eigenfield causality; Causal combination of creation and annihilation fields; Causal Dirac field requires fermion statistics; Causal massive vector field; Charge-conjugation and time-reversal phase constraints; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.antiparticles-from-charge-eigenfields`, `weinberg-1.causal-combination-of-creation-and-annihilation-fields`, `weinberg-1.causal-dirac-field-and-fermion-statistics`, `weinberg-1.causal-massive-vector-field`, `weinberg-1.charge-conjugation-time-reversal-phase-constraints`, `weinberg-1.charge-conservation-obstruction`, `weinberg-1.cluster-decomposition-local-field-interaction-route`, `weinberg-1.complex-causal-scalar-field`, `weinberg-1.conserved-current-for-smooth-massless-vector-limit`, `weinberg-1.cpt-proof-general-ab-scalar-route`, `weinberg-1.cpt-proof-tensor-and-dirac-bilinear-route`, `weinberg-1.cpt-theorem-local-scalar-interaction-proof`, `weinberg-1.differential-equivalence-of-field-types`, `weinberg-1.dirac-antiparticle-parity-majorana-reality`, `weinberg-1.dirac-bilinear-lorentz-and-discrete-symmetries`, `weinberg-1.dirac-equation-from-parity-completed-spinor-field`, `weinberg-1.dirac-matrix-tensor-basis-and-pseudounitarity`, `weinberg-1.dirac-rest-intertwiners-select-spin-half`, `weinberg-1.dirac-time-reversal-phase-and-transformation`, `weinberg-1.dirac-transpose-and-conjugation-identities`, `weinberg-1.field-mode-expansion-from-translation-covariance`, `weinberg-1.general-causal-field-clebsch-gordan-construction`, `weinberg-1.general-causal-fields-spin-statistics-and-phase`, `weinberg-1.general-field-charge-and-time-reversal-relations`, `weinberg-1.general-field-spin-sum-polynomial-locality-proof`, `weinberg-1.general-lorentz-scalar-couplings`, `weinberg-1.general-particle-antiparticle-parity-relation`, `weinberg-1.hermitian-local-interaction-condition`, `weinberg-1.high-spin-interaction-picture-qualification`, `weinberg-1.long-range-graviton-coupling-and-general-covariance`, `weinberg-1.lorentz-field-intertwining-conditions`, `weinberg-1.lorentz-irrep-rotation-content-and-parity-completion`, `weinberg-1.lorentz-irrep-su2-times-su2-classification`, `weinberg-1.massive-spin-one-polarization-coefficients`, `weinberg-1.massive-vector-proca-constraints`, `weinberg-1.massless-ab-helicity-selection-rule`, `weinberg-1.massless-field-little-group-coefficient-constraints`, `weinberg-1.massless-helicity-one-field-strength-and-maxwell-equations`, `weinberg-1.massless-helicity-one-no-covariant-vector-field`, `weinberg-1.massless-vector-potential-gauge-transformation`, `weinberg-1.nonzero-spacelike-mixed-commutator`, `weinberg-1.normal-ordering-preserves-locality-and-clustering`, `weinberg-1.parity-covariance-constraint`, `weinberg-1.particle-first-free-field-equations`, `weinberg-1.pauli-jordan-commutator`, `weinberg-1.positronium-charge-conjugation-selection`, `weinberg-1.real-causal-scalar-field`, `weinberg-1.rest-frame-intertwiners-determine-massive-fields`, `weinberg-1.scalar-lorentz-representation`, `weinberg-1.spin-one-inversion-phase-relations`, `weinberg-1.spinless-boson-and-mass-constraint`, `weinberg-1.vector-representation-spin-zero-or-one-content`.

</details>

<details>
<summary>Section 5.1 — covered</summary>

Accepted records cover translation-covariant field modes, causal combinations, and rest-frame intertwiner construction. The anchor records are Antiparticles from charge-eigenfield causality; Causal combination of creation and annihilation fields; Local field interactions as a route to cluster decomposition; Field mode expansion from translation covariance; Lorentz field transformation and coefficient intertwining conditions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.antiparticles-from-charge-eigenfields`, `weinberg-1.causal-combination-of-creation-and-annihilation-fields`, `weinberg-1.cluster-decomposition-local-field-interaction-route`, `weinberg-1.field-mode-expansion-from-translation-covariance`, `weinberg-1.lorentz-field-intertwining-conditions`, `weinberg-1.normal-ordering-preserves-locality-and-clustering`, `weinberg-1.particle-first-free-field-equations`, `weinberg-1.rest-frame-intertwiners-determine-massive-fields`.

</details>

<details>
<summary>Section 5.2 — covered</summary>

Accepted records cover scalar fields, charge obstruction, particle/antiparticle content, and scalar inversion phases. The anchor records are Charge-conjugation and time-reversal phase constraints; Charge-conservation obstruction for a self-adjoint field; Complex causal scalar field from particle and antiparticle; Hermiticity and spacelike commutation for scalar interactions; Nonzero spacelike mixed commutator; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.charge-conjugation-time-reversal-phase-constraints`, `weinberg-1.charge-conservation-obstruction`, `weinberg-1.complex-causal-scalar-field`, `weinberg-1.hermitian-local-interaction-condition`, `weinberg-1.nonzero-spacelike-mixed-commutator`, `weinberg-1.parity-covariance-constraint`, `weinberg-1.pauli-jordan-commutator`, `weinberg-1.real-causal-scalar-field`, `weinberg-1.scalar-lorentz-representation`, `weinberg-1.spinless-boson-and-mass-constraint`.

</details>

<details>
<summary>Section 5.3 — covered</summary>

Accepted records cover massive vectors, their causal construction, the massless-current limit, and inversion phases. The anchor records are Causal massive vector field; Conserved current for the smooth massless vector limit; Massive spin-one polarization coefficients; Massive vector Klein-Gordon and transversality constraints; Spin-one inversion phase relations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.causal-massive-vector-field`, `weinberg-1.conserved-current-for-smooth-massless-vector-limit`, `weinberg-1.massive-spin-one-polarization-coefficients`, `weinberg-1.massive-vector-proca-constraints`, `weinberg-1.spin-one-inversion-phase-relations`, `weinberg-1.vector-representation-spin-zero-or-one-content`.

</details>

<details>
<summary>Section 5.4 — covered</summary>

Accepted records cover Dirac tensor bases, pseudounitarity, and conjugation identities. The anchor records are Dirac tensor basis, parity, and pseudounitarity; Dirac transpose and complex-conjugation identities; Spin-one inversion phase relations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dirac-matrix-tensor-basis-and-pseudounitarity`, `weinberg-1.dirac-transpose-and-conjugation-identities`, `weinberg-1.spin-one-inversion-phase-relations`.

</details>

<details>
<summary>Section 5.5 — covered</summary>

Accepted records cover Dirac intertwiners, causal fermion statistics, Dirac equation, parity, Majorana, and time reversal. The anchor records are Causal Dirac field requires fermion statistics; Dirac antiparticle parity and Majorana reality; Dirac bilinear Lorentz and discrete-symmetry classification; Dirac equation from the parity-completed spinor field; Dirac rest intertwiners select spin one-half; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.causal-dirac-field-and-fermion-statistics`, `weinberg-1.dirac-antiparticle-parity-majorana-reality`, `weinberg-1.dirac-bilinear-lorentz-and-discrete-symmetries`, `weinberg-1.dirac-equation-from-parity-completed-spinor-field`, `weinberg-1.dirac-rest-intertwiners-select-spin-half`, `weinberg-1.dirac-time-reversal-phase-and-transformation`, `weinberg-1.dirac-transpose-and-conjugation-identities`, `weinberg-1.positronium-charge-conjugation-selection`.

</details>

<details>
<summary>Section 5.6 — covered</summary>

Accepted records cover Lorentz irreducible-representation constraints used to classify field content. The anchor records are Dirac bilinear Lorentz and discrete-symmetry classification; Rotation content and parity completion of Lorentz irreps; Lorentz irreducible representations from two commuting spins; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dirac-bilinear-lorentz-and-discrete-symmetries`, `weinberg-1.lorentz-irrep-rotation-content-and-parity-completion`, `weinberg-1.lorentz-irrep-su2-times-su2-classification`.

</details>

<details>
<summary>Section 5.7 — covered</summary>

Accepted records cover general causal fields, spin sums, local scalar couplings, and high-spin qualifications. The anchor records are Differential equivalence of free field types; General causal field from Clebsch-Gordan coefficients; General causal fields yield spin-statistics and common phase; General field charge-conjugation and time-reversal relations; Polynomial spin sum proof of general-field locality; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.differential-equivalence-of-field-types`, `weinberg-1.general-causal-field-clebsch-gordan-construction`, `weinberg-1.general-causal-fields-spin-statistics-and-phase`, `weinberg-1.general-field-charge-and-time-reversal-relations`, `weinberg-1.general-field-spin-sum-polynomial-locality-proof`, `weinberg-1.general-lorentz-scalar-couplings`, `weinberg-1.general-particle-antiparticle-parity-relation`, `weinberg-1.high-spin-interaction-picture-qualification`, `weinberg-1.lorentz-irrep-rotation-content-and-parity-completion`.

</details>

<details>
<summary>Section 5.8 — covered</summary>

Accepted records cover the two source-given CPT proof routes and their local-Hermitian-scalar assumptions. The anchor records are CPT proof route through general (A,B) scalar couplings; CPT proof route through scalar, vector, and Dirac tensors; CPT invariance of Hermitian local scalar interactions; Interaction-picture qualification on high-spin pathologies; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cpt-proof-general-ab-scalar-route`, `weinberg-1.cpt-proof-tensor-and-dirac-bilinear-route`, `weinberg-1.cpt-theorem-local-scalar-interaction-proof`, `weinberg-1.high-spin-interaction-picture-qualification`.

</details>

<details>
<summary>Section 5.9 — covered</summary>

Accepted records cover massless (A,B) fields, helicity, gauge-potential limits, and the gravity/gauge qualifications. The anchor records are CPT proof route through general (A,B) scalar couplings; CPT proof route through scalar, vector, and Dirac tensors; CPT invariance of Hermitian local scalar interactions; Long-range graviton coupling and general covariance; Massless (A,B) helicity selection rule; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.cpt-proof-general-ab-scalar-route`, `weinberg-1.cpt-proof-tensor-and-dirac-bilinear-route`, `weinberg-1.cpt-theorem-local-scalar-interaction-proof`, `weinberg-1.long-range-graviton-coupling-and-general-covariance`, `weinberg-1.massless-ab-helicity-selection-rule`, `weinberg-1.massless-field-little-group-coefficient-constraints`, `weinberg-1.massless-helicity-one-field-strength-and-maxwell-equations`, `weinberg-1.massless-helicity-one-no-covariant-vector-field`, `weinberg-1.massless-vector-potential-gauge-transformation`.

</details>

<details>
<summary>Section 5.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Massless (A,B) helicity selection rule; Problem: prove boost construction satisfies full covariance; Problem: classify generalized Dirac-field bilinear tensors; Problem: high-spin emission scaling from an external current; Problem: construct massive spin-two tensor field; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.massless-ab-helicity-selection-rule`, `weinberg-1.problem-boost-covariance-of-massive-coefficients`, `weinberg-1.problem-generalized-dirac-field-bilinear-tensors`, `weinberg-1.problem-high-spin-external-current-emission-scaling`, `weinberg-1.problem-massive-spin-two-field-construction`, `weinberg-1.problem-massless-higher-spin-derivative-fields`, `weinberg-1.problem-massless-spin-j-inversion-transformations`, `weinberg-1.problem-rarita-schwinger-field-construction`.

</details>

<details>
<summary>Section 6 — covered</summary>

Accepted records cover coordinate and momentum-space Feynman rules, propagators, graph counting, and off-shell source methods. The anchor records are Coordinate-space Feynman rules; Coordinate-space pairing construction of Feynman diagrams; Massive-particle covariant propagators with local contact compensation; Diagram line counting and coupling order; External-source functional derivatives as time-ordered insertions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.coordinate-space-feynman-rules`, `weinberg-1.coordinate-wick-pairing-diagram-method`, `weinberg-1.covariant-propagator-local-contact-compensation`, `weinberg-1.diagram-line-counting-and-coupling-order`, `weinberg-1.external-source-functional-derivative-method`, `weinberg-1.fermion-exchange-and-loop-signs`, `weinberg-1.feynman-diagram-symmetry-factors`, `weinberg-1.feynman-propagator-fourier-green-function`, `weinberg-1.feynman-propagator-time-ordered-correlator`, `weinberg-1.general-field-propagator-polynomial-numerator`, `weinberg-1.graph-loop-number-and-tree-integrals`, `weinberg-1.momentum-space-feynman-rules`, `weinberg-1.off-shell-diagram-continuation`.

</details>

<details>
<summary>Section 6.1 — covered</summary>

Accepted records cover Wick pairing, coordinate-space rules, fermion signs, and symmetry factors. The anchor records are Coordinate-space Feynman rules; Coordinate-space pairing construction of Feynman diagrams; Fermion exchange and closed-loop signs; Diagram symmetry and identical-field factors; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.coordinate-space-feynman-rules`, `weinberg-1.coordinate-wick-pairing-diagram-method`, `weinberg-1.fermion-exchange-and-loop-signs`, `weinberg-1.feynman-diagram-symmetry-factors`.

</details>

<details>
<summary>Section 6.2 — covered</summary>

Accepted records cover Feynman propagators, boundary conditions, and local compensation of covariant propagators. The anchor records are Massive-particle covariant propagators with local contact compensation; Feynman propagator Fourier form and boundary condition; Feynman propagator as a time-ordered vacuum correlator; General field propagator from polynomial mode sums; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.covariant-propagator-local-contact-compensation`, `weinberg-1.feynman-propagator-fourier-green-function`, `weinberg-1.feynman-propagator-time-ordered-correlator`, `weinberg-1.general-field-propagator-polynomial-numerator`.

</details>

<details>
<summary>Section 6.3 — covered</summary>

Accepted records cover momentum-space graph rules, loop counting, numerator structure, and coupling order. The anchor records are Diagram line counting and coupling order; Feynman propagator as a time-ordered vacuum correlator; Loop number and independent momentum integrals; Momentum-space Feynman rules; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.diagram-line-counting-and-coupling-order`, `weinberg-1.feynman-propagator-time-ordered-correlator`, `weinberg-1.graph-loop-number-and-tree-integrals`, `weinberg-1.momentum-space-feynman-rules`.

</details>

<details>
<summary>Section 6.4 — covered</summary>

Accepted records cover off-shell continuation and functional source insertions. The anchor records are Diagram line counting and coupling order; External-source functional derivatives as time-ordered insertions; Off-shell diagram continuation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.diagram-line-counting-and-coupling-order`, `weinberg-1.external-source-functional-derivative-method`, `weinberg-1.off-shell-diagram-continuation`.

</details>

<details>
<summary>Section 6.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are External-source functional derivatives as time-ordered insertions; Problem: cubic scalar scattering through order g²; Problem: derivative Dirac-field contraction; Problem: quartic scalar order-g² loop correction; Problem: quartic scalar tree scattering and cross-section; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.external-source-functional-derivative-method`, `weinberg-1.problem-cubic-scalar-scattering-cross-section`, `weinberg-1.problem-derivative-dirac-contraction`, `weinberg-1.problem-quartic-scalar-loop-correction`, `weinberg-1.problem-quartic-scalar-tree-cross-section`, `weinberg-1.problem-source-theorem-correlators`, `weinberg-1.problem-yukawa-diagram-amplitudes`.

</details>

<details>
<summary>Section 7 — covered</summary>

Accepted records cover canonical field theory, Noether currents, Lorentz generators, constrained systems, and Dirac brackets. The anchor records are Appendix proof: Dirac brackets for auxiliary-coordinate constraints; Appendix proof: Dirac brackets after coordinate and momentum reduction; Auxiliary-field constraints and interaction-picture route; Belinfante symmetric energy-momentum tensor; Canonical energy-momentum tensor from translations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.appendix-dirac-brackets-type-a-proof`, `weinberg-1.appendix-dirac-brackets-type-b-proof`, `weinberg-1.auxiliary-field-constraint-interaction-picture-route`, `weinberg-1.belinfante-symmetric-energy-momentum-tensor`, `weinberg-1.canonical-energy-momentum-tensor`, `weinberg-1.canonical-functional-derivatives-and-hamilton-equations`, `weinberg-1.canonical-rotation-generator-action`, `weinberg-1.canonical-symmetry-generator-method`, `weinberg-1.dirac-bracket-algebraic-properties`, `weinberg-1.dirac-bracket-commutator-prescription`, `weinberg-1.dirac-bracket-quantization-method`, `weinberg-1.dirac-canonical-lagrangian-hamiltonian-method`, `weinberg-1.first-and-second-class-constraint-classification`, `weinberg-1.free-field-canonical-variable-identification`, `weinberg-1.free-hamiltonian-to-lagrangian-legendre-method`, `weinberg-1.hamiltonian-legendre-transform-equations`, `weinberg-1.heisenberg-canonical-hamilton-equations`, `weinberg-1.internal-symmetry-current-and-lie-generators`, `weinberg-1.local-current-field-commutators`, `weinberg-1.lorentz-generators-and-s-matrix-covariance`, `weinberg-1.lorentz-scalar-lagrangian-density-hypothesis`, `weinberg-1.noether-current-and-conserved-charge`, `weinberg-1.poisson-bracket-algebra`, `weinberg-1.primary-and-secondary-constraints`, `weinberg-1.proca-interaction-picture-contact-compensation`, `weinberg-1.proca-lagrangian-spin-one-selection`, `weinberg-1.real-action-field-equation-count-hypothesis`, `weinberg-1.reduced-canonical-variables-dirac-bracket-result`, `weinberg-1.redundant-couplings-by-field-redefinition`, `weinberg-1.scalar-derivative-coupling-contact-term`, `weinberg-1.scalar-lagrangian-hamiltonian-validation`, `weinberg-1.stationary-action-euler-lagrange-method`, `weinberg-1.total-derivative-lagrangian-quantum-equivalence`.

</details>

<details>
<summary>Section 7.1 — covered</summary>

Accepted records cover canonical functional variables, Hamilton equations, and the free-field Legendre route. The anchor records are Canonical functional derivatives and Hamilton equations; Canonical variables for free scalar, vector, and Dirac fields; Free Hamiltonian to Lagrangian by Legendre transformation; Heisenberg-picture canonical Hamilton equations; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.canonical-functional-derivatives-and-hamilton-equations`, `weinberg-1.free-field-canonical-variable-identification`, `weinberg-1.free-hamiltonian-to-lagrangian-legendre-method`, `weinberg-1.heisenberg-canonical-hamilton-equations`.

</details>

<details>
<summary>Section 7.2 — covered</summary>

Accepted records cover stationary action, Legendre transforms, scalar validation, total derivatives, and auxiliary constraints. The anchor records are Auxiliary-field constraints and interaction-picture route; Hamiltonian Legendre transformation and canonical equations; Heisenberg-picture canonical Hamilton equations; Lorentz-scalar Lagrangian-density hypothesis; Real-action field-equation-count hypothesis; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.auxiliary-field-constraint-interaction-picture-route`, `weinberg-1.hamiltonian-legendre-transform-equations`, `weinberg-1.heisenberg-canonical-hamilton-equations`, `weinberg-1.lorentz-scalar-lagrangian-density-hypothesis`, `weinberg-1.real-action-field-equation-count-hypothesis`, `weinberg-1.scalar-lagrangian-hamiltonian-validation`, `weinberg-1.stationary-action-euler-lagrange-method`, `weinberg-1.total-derivative-lagrangian-quantum-equivalence`.

</details>

<details>
<summary>Section 7.3 — covered</summary>

Accepted records cover Noether currents, canonical energy-momentum, internal charges, and local current commutators. The anchor records are Canonical energy-momentum tensor from translations; Canonical charge as symmetry generator; Internal-symmetry currents and Lie-algebra charges; Local current-field commutators; Noether current and conserved charge from global action symmetry; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.canonical-energy-momentum-tensor`, `weinberg-1.canonical-symmetry-generator-method`, `weinberg-1.internal-symmetry-current-and-lie-generators`, `weinberg-1.local-current-field-commutators`, `weinberg-1.noether-current-and-conserved-charge`, `weinberg-1.total-derivative-lagrangian-quantum-equivalence`.

</details>

<details>
<summary>Section 7.4 — covered</summary>

Accepted records cover Belinfante improvement, rotation generators, and Lorentz covariance of the S matrix. The anchor records are Belinfante symmetric energy-momentum tensor; Canonical rotation-generator action on fields; Local current-field commutators; Lorentz generators and S-matrix covariance; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.belinfante-symmetric-energy-momentum-tensor`, `weinberg-1.canonical-rotation-generator-action`, `weinberg-1.local-current-field-commutators`, `weinberg-1.lorentz-generators-and-s-matrix-covariance`.

</details>

<details>
<summary>Section 7.5 — covered</summary>

Accepted records cover derivative couplings, Proca selection, and interaction-picture contact compensation. The anchor records are Canonical rotation-generator action on fields; Dirac canonical Lagrangian and Hamiltonian; Proca Hamiltonian and interaction-picture compensation; Proca Lagrangian selected to exclude scalar propagation; Canonical scalar derivative coupling contact term; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.canonical-rotation-generator-action`, `weinberg-1.dirac-canonical-lagrangian-hamiltonian-method`, `weinberg-1.proca-interaction-picture-contact-compensation`, `weinberg-1.proca-lagrangian-spin-one-selection`, `weinberg-1.scalar-derivative-coupling-contact-term`.

</details>

<details>
<summary>Section 7.6 — covered</summary>

Accepted records cover primary/secondary and first/second-class constraints, Dirac brackets, and their quantization prescription. The anchor records are Dirac-bracket algebraic properties; Dirac-bracket commutator prescription; Dirac-bracket definition for second-class constraints; Dirac canonical Lagrangian and Hamiltonian; First- and second-class constraint classification; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dirac-bracket-algebraic-properties`, `weinberg-1.dirac-bracket-commutator-prescription`, `weinberg-1.dirac-bracket-quantization-method`, `weinberg-1.dirac-canonical-lagrangian-hamiltonian-method`, `weinberg-1.first-and-second-class-constraint-classification`, `weinberg-1.poisson-bracket-algebra`, `weinberg-1.primary-and-secondary-constraints`, `weinberg-1.reduced-canonical-variables-dirac-bracket-result`.

</details>

<details>
<summary>Section 7.7 — covered</summary>

Accepted records cover field redefinitions and redundant couplings. The anchor records are Redundant couplings from field redefinitions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.redundant-couplings-by-field-redefinition`.

</details>

<details>
<summary>Section 7.A — covered</summary>

Accepted records cover the two appendical reductions that justify the Dirac-bracket construction. The anchor records are Appendix proof: Dirac brackets for auxiliary-coordinate constraints; Appendix proof: Dirac brackets after coordinate and momentum reduction; Redundant couplings from field redefinitions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.appendix-dirac-brackets-type-a-proof`, `weinberg-1.appendix-dirac-brackets-type-b-proof`, `weinberg-1.redundant-couplings-by-field-redefinition`.

</details>

<details>
<summary>Section 7.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Appendix proof: Dirac brackets after coordinate and momentum reduction; Problem: prove Dirac-bracket independence of constraint functions; Problem: prove the Dirac-bracket Jacobi identity; Problem: global-symmetry current for scalar and Dirac fields; Problem: nonlinear sigma-model canonical quantization; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.appendix-dirac-brackets-type-b-proof`, `weinberg-1.problem-dirac-bracket-constraint-redefinition`, `weinberg-1.problem-dirac-bracket-jacobi-identity`, `weinberg-1.problem-global-symmetry-current`, `weinberg-1.problem-nonlinear-sigma-canonical-quantization`, `weinberg-1.problem-scalar-vector-canonical-quantization`, `weinberg-1.problem-scalar-vector-conserved-current`, `weinberg-1.problem-scalar-vector-symmetric-energy-momentum-tensor`, `weinberg-1.problem-symmetric-energy-momentum-tensor`.

</details>

<details>
<summary>Section 8 — covered</summary>

Accepted records cover Abelian gauge theory from the Maxwell action through constrained quantization, spinor QED, Compton scattering, and p-form duality. The anchor records are Tree-level Compton amplitude and laboratory kinematics; Coulomb-gauge reduction of the auxiliary potential; First-class electromagnetic constraints and gauge fixing; Coulomb-gauge Hamiltonian with instantaneous Coulomb energy; Coulomb-gauge transverse Dirac commutators; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.compton-tree-amplitude-and-laboratory-kinematics`, `weinberg-1.coulomb-gauge-auxiliary-potential-reduction`, `weinberg-1.coulomb-gauge-constraint-structure`, `weinberg-1.coulomb-gauge-hamiltonian-and-instantaneous-energy`, `weinberg-1.coulomb-gauge-transverse-dirac-commutators`, `weinberg-1.dirac-gamma-even-trace-pairing-formula`, `weinberg-1.dirac-gamma-trace-induction-proof`, `weinberg-1.four-dimensional-p-form-field-content`, `weinberg-1.gamma-trace-cyclicity`, `weinberg-1.gauge-invariant-maxwell-action-and-equations`, `weinberg-1.local-gauge-invariance-and-minimal-coupling`, `weinberg-1.p-form-exterior-derivative-and-local-exactness`, `weinberg-1.p-form-gauge-action-and-conserved-current`, `weinberg-1.p-form-gauge-duality`, `weinberg-1.photon-polarization-density-matrix-and-spin-averaging`, `weinberg-1.polarized-klein-nishina-cross-section`, `weinberg-1.qed-loop-expansion-parameter`, `weinberg-1.spinor-qed-lagrangian-current`, `weinberg-1.spinor-qed-momentum-space-rules`, `weinberg-1.transverse-free-photon-interaction-picture`, `weinberg-1.unpolarized-klein-nishina-and-thomson-limit`.

</details>

<details>
<summary>Section 8.1 — covered</summary>

Accepted records cover Maxwell dynamics and the passage from global charge symmetry to local U(1) minimal coupling. The anchor records are Gauge-invariant Maxwell action and equations; Local U(1) gauge invariance from minimal coupling; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.gauge-invariant-maxwell-action-and-equations`, `weinberg-1.local-gauge-invariance-and-minimal-coupling`.

</details>

<details>
<summary>Section 8.2 — covered</summary>

Accepted records cover gauge constraints, gauge fixing, and Coulomb-gauge auxiliary-potential structure. The anchor records are Coulomb-gauge reduction of the auxiliary potential; First-class electromagnetic constraints and gauge fixing; Gauge-invariant Maxwell action and equations; Local U(1) gauge invariance from minimal coupling; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.coulomb-gauge-auxiliary-potential-reduction`, `weinberg-1.coulomb-gauge-constraint-structure`, `weinberg-1.gauge-invariant-maxwell-action-and-equations`, `weinberg-1.local-gauge-invariance-and-minimal-coupling`.

</details>

<details>
<summary>Section 8.3 — covered</summary>

Accepted records cover transverse commutators, Coulomb-gauge Hamiltonian, and instantaneous energy. The anchor records are Coulomb-gauge reduction of the auxiliary potential; Coulomb-gauge Hamiltonian with instantaneous Coulomb energy; Coulomb-gauge transverse Dirac commutators; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.coulomb-gauge-auxiliary-potential-reduction`, `weinberg-1.coulomb-gauge-hamiltonian-and-instantaneous-energy`, `weinberg-1.coulomb-gauge-transverse-dirac-commutators`.

</details>

<details>
<summary>Section 8.4 — covered</summary>

Accepted records cover the transverse free-photon interaction-picture field. The anchor records are Coulomb-gauge Hamiltonian with instantaneous Coulomb energy; Transverse free-photon interaction-picture field; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.coulomb-gauge-hamiltonian-and-instantaneous-energy`, `weinberg-1.transverse-free-photon-interaction-picture`.

</details>

<details>
<summary>Section 8.5 — covered</summary>

Accepted records cover the transverse propagator calculation that supplies the later covariant-rule discussion. The anchor records are Transverse free-photon interaction-picture field; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.transverse-free-photon-interaction-picture`.

</details>

<details>
<summary>Section 8.6 — covered</summary>

Accepted records cover minimal spinor QED, momentum-space rules, polarization averaging, and loop expansion scale. The anchor records are Photon polarization mixtures and unobserved-spin sums; QED loop expansion parameter; Minimal spinor QED Lagrangian and current; Momentum-space Feynman rules for spinor QED; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.photon-polarization-density-matrix-and-spin-averaging`, `weinberg-1.qed-loop-expansion-parameter`, `weinberg-1.spinor-qed-lagrangian-current`, `weinberg-1.spinor-qed-momentum-space-rules`.

</details>

<details>
<summary>Section 8.7 — covered</summary>

Accepted records cover tree Compton kinematics and polarized/unpolarized Klein–Nishina limits. The anchor records are Tree-level Compton amplitude and laboratory kinematics; Polarized Klein–Nishina Compton cross-section; Unpolarized Klein–Nishina formula and Thomson limit; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.compton-tree-amplitude-and-laboratory-kinematics`, `weinberg-1.polarized-klein-nishina-cross-section`, `weinberg-1.unpolarized-klein-nishina-and-thomson-limit`.

</details>

<details>
<summary>Section 8.8 — covered</summary>

Accepted records cover p-forms, local exactness, gauge action, and electric-magnetic duality with the stated topology caveat. The anchor records are Four-dimensional p-form gauge-field content; Exterior derivative, closed forms, and local exactness; p-form gauge action, field strength, and current conservation; Duality of p-form gauge fields; Unpolarized Klein–Nishina formula and Thomson limit; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.four-dimensional-p-form-field-content`, `weinberg-1.p-form-exterior-derivative-and-local-exactness`, `weinberg-1.p-form-gauge-action-and-conserved-current`, `weinberg-1.p-form-gauge-duality`, `weinberg-1.unpolarized-klein-nishina-and-thomson-limit`.

</details>

<details>
<summary>Section 8.A — covered</summary>

Accepted records cover gamma-trace identities and the p-form duality calculation used by the chapter. The anchor records are Even Dirac-gamma trace pairing formula; Inductive proof of the gamma-trace pairing formula; Four-dimensional p-form gauge-field content; Cyclicity and commutator invariance of Dirac traces; Duality of p-form gauge fields; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dirac-gamma-even-trace-pairing-formula`, `weinberg-1.dirac-gamma-trace-induction-proof`, `weinberg-1.four-dimensional-p-form-field-content`, `weinberg-1.gamma-trace-cyclicity`, `weinberg-1.p-form-gauge-duality`.

</details>

<details>
<summary>Section 8.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Inductive proof of the gamma-trace pairing formula; Gamma-five trace identities; Problem: gauge-invariant charged massive-vector Lagrangian; Problem: charged-scalar electrodynamics in Coulomb gauge; Problem: electron–electron scattering cross-section; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.dirac-gamma-trace-induction-proof`, `weinberg-1.gamma5-trace-identities`, `weinberg-1.problem-charged-massive-vector-gauge-lagrangian`, `weinberg-1.problem-charged-scalar-coulomb-quantization`, `weinberg-1.problem-electron-electron-scattering-cross-section`, `weinberg-1.problem-electron-muon-annihilation-cross-sections`, `weinberg-1.problem-scalar-compton-cross-sections`.

</details>

<details>
<summary>Section 9 — covered</summary>

Accepted records cover bosonic and fermionic phase-space path integrals, Gaussian rules, measure qualifications, and covariant QED gauge fixing. The anchor records are Abelian gauge averaging for the covariant QED path integral; Auxiliary-field restoration of a covariant vector action; Berezin integration, completeness, and inverse Jacobian; Bosonic phase-space path integral from canonical slices; External-Dirac-field determinant and fermion-loop expansion; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.abelian-gauge-averaging-covariant-qed-path-integral`, `weinberg-1.auxiliary-field-restoration-of-covariant-action`, `weinberg-1.berezin-integration-completeness-and-inverse-jacobian`, `weinberg-1.bosonic-phase-space-path-integral`, `weinberg-1.external-dirac-field-determinant-loop-expansion`, `weinberg-1.fermionic-gaussian-pairing-and-dirac-propagator`, `weinberg-1.fermionic-grassmann-eigenstate-basis`, `weinberg-1.fermionic-phase-space-path-integral`, `weinberg-1.field-dependent-path-integral-determinant-correction`, `weinberg-1.gaussian-pairing-wick-formula-proof`, `weinberg-1.gaussian-stationary-point-determinant-proof`, `weinberg-1.path-integral-bosonic-gaussian-pairing-route`, `weinberg-1.path-integral-covariant-propagator-and-derivative-rule`, `weinberg-1.path-integral-measure-ordering-and-euclidean-qualification`, `weinberg-1.path-integral-qed-covariant-photon-propagator-proof`, `weinberg-1.path-integral-time-ordering-and-contact-terms`, `weinberg-1.path-integral-topological-bose-fermi-statistics-proof`, `weinberg-1.phase-space-s-matrix-with-asymptotic-wave-functionals`, `weinberg-1.photon-propagator-coulomb-contact-cancellation`, `weinberg-1.qed-auxiliary-a0-covariant-action-route`, `weinberg-1.qed-coulomb-gauge-constrained-path-integral`, `weinberg-1.quadratic-momentum-lagrangian-path-integral-reduction`, `weinberg-1.scalar-vacuum-wave-functional-ie-prescription`.

</details>

<details>
<summary>Section 9.1 — covered</summary>

Accepted records cover time-sliced bosonic phase-space integrals, ordering/contact terms, and their qualifications. The anchor records are Bosonic phase-space path integral from canonical slices; Measure-dependent ordering and Euclidean path-integral qualification; Time ordering and contact terms in phase-space path integrals; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bosonic-phase-space-path-integral`, `weinberg-1.path-integral-measure-ordering-and-euclidean-qualification`, `weinberg-1.path-integral-time-ordering-and-contact-terms`.

</details>

<details>
<summary>Section 9.2 — covered</summary>

Accepted records cover asymptotic wave functionals, the S matrix, and the scalar i-epsilon prescription. The anchor records are Phase-space path integral for S-matrix matrix elements; Scalar vacuum wave functional and the iε prescription; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.phase-space-s-matrix-with-asymptotic-wave-functionals`, `weinberg-1.scalar-vacuum-wave-functional-ie-prescription`.

</details>

<details>
<summary>Section 9.3 — covered</summary>

Accepted records cover quadratic-momentum reduction, auxiliary-field restoration, and field-dependent determinants. The anchor records are Auxiliary-field restoration of a covariant vector action; Field-dependent determinant correction in a path integral; Quadratic-momentum reduction to a Lagrangian path integral; Scalar vacuum wave functional and the iε prescription; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.auxiliary-field-restoration-of-covariant-action`, `weinberg-1.field-dependent-path-integral-determinant-correction`, `weinberg-1.quadratic-momentum-lagrangian-path-integral-reduction`, `weinberg-1.scalar-vacuum-wave-functional-ie-prescription`.

</details>

<details>
<summary>Section 9.4 — covered</summary>

Accepted records cover Gaussian pairing and propagator/derivative rules. The anchor records are Gaussian pairing route to bosonic Feynman rules; Path-integral covariant propagators and derivative couplings; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.path-integral-bosonic-gaussian-pairing-route`, `weinberg-1.path-integral-covariant-propagator-and-derivative-rule`.

</details>

<details>
<summary>Section 9.5 — covered</summary>

Accepted records cover Grassmann bases, Berezin Jacobians, fermionic Gaussian signs, and the determinant loop expansion. The anchor records are Berezin integration, completeness, and inverse Jacobian; External-Dirac-field determinant and fermion-loop expansion; Fermionic Gaussian pairing signs and the Dirac propagator; Grassmann eigenstates for fermionic canonical variables; Fermionic phase-space path integral with graded time ordering; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.berezin-integration-completeness-and-inverse-jacobian`, `weinberg-1.external-dirac-field-determinant-loop-expansion`, `weinberg-1.fermionic-gaussian-pairing-and-dirac-propagator`, `weinberg-1.fermionic-grassmann-eigenstate-basis`, `weinberg-1.fermionic-phase-space-path-integral`.

</details>

<details>
<summary>Section 9.6 — covered</summary>

Accepted records cover constrained QED, the auxiliary A0 route, Abelian gauge averaging, and the rigorous covariant-propagator alternative. The anchor records are Abelian gauge averaging for the covariant QED path integral; External-Dirac-field determinant and fermion-loop expansion; Path-integral proof of covariant QED photon propagators; Covariant photon propagator after Coulomb-contact cancellation; Auxiliary A0 route from Coulomb energy to the covariant QED action; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.abelian-gauge-averaging-covariant-qed-path-integral`, `weinberg-1.external-dirac-field-determinant-loop-expansion`, `weinberg-1.path-integral-qed-covariant-photon-propagator-proof`, `weinberg-1.photon-propagator-coulomb-contact-cancellation`, `weinberg-1.qed-auxiliary-a0-covariant-action-route`, `weinberg-1.qed-coulomb-gauge-constrained-path-integral`.

</details>

<details>
<summary>Section 9.7 — covered</summary>

Accepted records cover the topological path-integral route to Bose–Fermi statistics. The anchor records are Path-integral proof of covariant QED photon propagators; Topological path-integral proof of Bose–Fermi alternatives; Covariant photon propagator after Coulomb-contact cancellation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.path-integral-qed-covariant-photon-propagator-proof`, `weinberg-1.path-integral-topological-bose-fermi-statistics-proof`, `weinberg-1.photon-propagator-coulomb-contact-cancellation`.

</details>

<details>
<summary>Section 9.A — covered</summary>

Accepted records cover the Gaussian proofs that underwrite the pairing and stationary-determinant formulas. The anchor records are Gaussian pairing formula proof; Gaussian stationary-point and determinant proof; Topological path-integral proof of Bose–Fermi alternatives; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.gaussian-pairing-wick-formula-proof`, `weinberg-1.gaussian-stationary-point-determinant-proof`, `weinberg-1.path-integral-topological-bose-fermi-statistics-proof`.

</details>

<details>
<summary>Section 9.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Gaussian pairing formula proof; Problem: neutral-vector vacuum wave functional and iε terms; Problem: one-particle field-space wave function and emission rule; Problem: harmonic-oscillator transition probability by path integrals; Problem: Rarita–Schwinger path-integral propagator; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.gaussian-pairing-wick-formula-proof`, `weinberg-1.problem-neutral-vector-vacuum-wave-functional-ie`, `weinberg-1.problem-one-particle-field-space-wave-function-and-emission`, `weinberg-1.problem-path-integral-harmonic-oscillator-transition-probability`, `weinberg-1.problem-rarita-schwinger-path-integral-propagator`.

</details>

<details>
<summary>Section 10 — covered</summary>

Accepted records cover nonperturbative symmetry, poles, renormalized fields, currents, form factors, spectral representations, and dispersion relations. The anchor records are Physical charge scale from photon-field normalization; Conserved-current charge eigenvalues; Electromagnetic form factors for spin zero and one half; Fermion 1PI self-energy and on-shell conditions; Furry’s theorem for odd-photon graph sums; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.charge-scale-photon-field-renormalization`, `weinberg-1.conserved-charge-eigenvalues-from-current`, `weinberg-1.electromagnetic-form-factors-spin-zero-spin-half`, `weinberg-1.fermion-onshell-renormalization-conditions`, `weinberg-1.furrys-theorem-odd-photon-sums`, `weinberg-1.generalized-pomeranchuk-and-photon-kramers-kronig`, `weinberg-1.generalized-ward-takahashi-identity`, `weinberg-1.heisenberg-off-shell-symmetry-constraints`, `weinberg-1.kallen-lehmann-spectral-propagator`, `weinberg-1.lsz-reduction-renormalized-field-normalization`, `weinberg-1.magnetic-moment-from-spin-half-form-factors`, `weinberg-1.microcausality-forward-amplitude-analyticity`, `weinberg-1.multiphonon-transversality-and-gauge-replacement`, `weinberg-1.one-particle-pole-factorization-bound-states`, `weinberg-1.particle-poles-exchange-range-and-analytic-continuation`, `weinberg-1.photon-1pi-transversality-masslessness-z3`, `weinberg-1.scalar-onshell-renormalization-1pi-resummation`, `weinberg-1.spectral-positivity-asymptotic-and-z-bound`, `weinberg-1.subtracted-forward-dispersion-relation`, `weinberg-1.zero-transfer-charge-vertex-cancellation`.

</details>

<details>
<summary>Section 10.1 — covered</summary>

Accepted records cover Heisenberg-picture off-shell symmetry constraints. The anchor records are Furry’s theorem for odd-photon graph sums; Heisenberg correlator symmetry constraints off shell; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.furrys-theorem-odd-photon-sums`, `weinberg-1.heisenberg-off-shell-symmetry-constraints`.

</details>

<details>
<summary>Section 10.2 — covered</summary>

Accepted records cover one-particle poles, bound-state factorization, Furry’s theorem, and exchange-range analyticity. The anchor records are Furry’s theorem for odd-photon graph sums; One-particle pole factorization, including bound states; Particle exchange poles, analytic continuation, and range; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.furrys-theorem-odd-photon-sums`, `weinberg-1.one-particle-pole-factorization-bound-states`, `weinberg-1.particle-poles-exchange-range-and-analytic-continuation`.

</details>

<details>
<summary>Section 10.3 — covered</summary>

Accepted records cover scalar/fermion 1PI resummation, on-shell conditions, and LSZ field normalization. The anchor records are Fermion 1PI self-energy and on-shell conditions; LSZ reduction and renormalized field normalization; Particle exchange poles, analytic continuation, and range; Scalar 1PI resummation and on-shell renormalization; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.fermion-onshell-renormalization-conditions`, `weinberg-1.lsz-reduction-renormalized-field-normalization`, `weinberg-1.particle-poles-exchange-range-and-analytic-continuation`, `weinberg-1.scalar-onshell-renormalization-1pi-resummation`.

</details>

<details>
<summary>Section 10.4 — covered</summary>

Accepted records cover conserved charge eigenvalues, the common photon-field charge scale, Ward identities, and zero-transfer cancellation. The anchor records are Physical charge scale from photon-field normalization; Conserved-current charge eigenvalues; Fermion 1PI self-energy and on-shell conditions; Generalized Ward–Takahashi identity; Zero-transfer charge vertex cancellation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.charge-scale-photon-field-renormalization`, `weinberg-1.conserved-charge-eigenvalues-from-current`, `weinberg-1.fermion-onshell-renormalization-conditions`, `weinberg-1.generalized-ward-takahashi-identity`, `weinberg-1.zero-transfer-charge-vertex-cancellation`.

</details>

<details>
<summary>Section 10.5 — covered</summary>

Accepted records cover photon 1PI transversality, masslessness/Z3, and gauge replacement. The anchor records are Multi-photon transversality and gauge replacements; Photon 1PI transversality, masslessness, and Z3; Zero-transfer charge vertex cancellation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.multiphonon-transversality-and-gauge-replacement`, `weinberg-1.photon-1pi-transversality-masslessness-z3`, `weinberg-1.zero-transfer-charge-vertex-cancellation`.

</details>

<details>
<summary>Section 10.6 — covered</summary>

Accepted records cover spin-zero/spin-half electromagnetic form factors and their magnetic-moment content. The anchor records are Electromagnetic form factors for spin zero and one half; Magnetic moment from spin-half form factors; Photon 1PI transversality, masslessness, and Z3; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.electromagnetic-form-factors-spin-zero-spin-half`, `weinberg-1.magnetic-moment-from-spin-half-form-factors`, `weinberg-1.photon-1pi-transversality-masslessness-z3`.

</details>

<details>
<summary>Section 10.7 — covered</summary>

Accepted records cover Kallen–Lehmann representation, positivity, asymptotics, and the Z bound. The anchor records are Källén–Lehmann spectral propagator; Magnetic moment from spin-half form factors; Spectral positivity, propagator asymptotics, and Z bound; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.kallen-lehmann-spectral-propagator`, `weinberg-1.magnetic-moment-from-spin-half-form-factors`, `weinberg-1.spectral-positivity-asymptotic-and-z-bound`.

</details>

<details>
<summary>Section 10.8 — covered</summary>

Accepted records cover microcausal forward analyticity, subtracted dispersion relations, and Pomeranchuk/Kramers–Kronig qualifications. The anchor records are Generalized Pomeranchuk ratio and photon Kramers–Kronig relation; Microcausal derivation of forward-amplitude analyticity; Spectral positivity, propagator asymptotics, and Z bound; Subtracted forward dispersion relation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.generalized-pomeranchuk-and-photon-kramers-kronig`, `weinberg-1.microcausality-forward-amplitude-analyticity`, `weinberg-1.spectral-positivity-asymptotic-and-z-bound`, `weinberg-1.subtracted-forward-dispersion-relation`.

</details>

<details>
<summary>Section 10.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Generalized Pomeranchuk ratio and photon Kramers–Kronig relation; Problem: conserved-current Källén–Lehmann representation; Problem: Dirac-field Källén–Lehmann representation; Problem: dispersion-theory complex-scalar spectral representation; Problem: forward photon-electron scattering through order e4; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.generalized-pomeranchuk-and-photon-kramers-kronig`, `weinberg-1.problem-current-kallen-lehmann`, `weinberg-1.problem-dirac-kallen-lehmann`, `weinberg-1.problem-dispersion-derived-complex-scalar-spectrum`, `weinberg-1.problem-forward-photon-electron-order-e4`, `weinberg-1.problem-no-unsubtracted-photon-dispersion`, `weinberg-1.problem-scalar-ward-identity`, `weinberg-1.problem-spin-half-transition-current`, `weinberg-1.problem-vector-1pi-renormalization`.

</details>

<details>
<summary>Section 11 — covered</summary>

Accepted records cover renormalized QED counterterms and the explicit one-loop vacuum-polarization, vertex, and self-energy calculations. The anchor records are Appendix: Feynman parameters and dimensional loop integrals; Lepton charge radius and infrared qualification; Electron-loop logarithm in the muon magnetic moment; One-loop electron self-energy with Pauli–Villars regulation; One-loop vacuum polarization with dimensional regularization; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.appendix-feynman-parameters-dimensional-integrals`, `weinberg-1.lepton-charge-radius-infrared-qualification`, `weinberg-1.muon-anomalous-moment-electron-loop-log`, `weinberg-1.one-loop-electron-self-energy-pauli-villars`, `weinberg-1.one-loop-vacuum-polarization-dimensional-regularization`, `weinberg-1.one-loop-vertex-form-factor-evaluation`, `weinberg-1.qed-renormalized-lagrangian-counterterms`, `weinberg-1.schwinger-one-loop-anomalous-magnetic-moment`, `weinberg-1.vacuum-polarization-screening-and-uehling-shift`.

</details>

<details>
<summary>Section 11.1 — covered</summary>

Accepted records cover the renormalized QED Lagrangian and counterterm organization. The anchor records are Renormalized QED Lagrangian and counterterms; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.qed-renormalized-lagrangian-counterterms`.

</details>

<details>
<summary>Section 11.2 — covered</summary>

Accepted records cover vacuum polarization, Z3, screening, and the Uehling shift. The anchor records are One-loop vacuum polarization with dimensional regularization; Renormalized QED Lagrangian and counterterms; Vacuum-polarization screening and Uehling energy shift; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.one-loop-vacuum-polarization-dimensional-regularization`, `weinberg-1.qed-renormalized-lagrangian-counterterms`, `weinberg-1.vacuum-polarization-screening-and-uehling-shift`.

</details>

<details>
<summary>Section 11.3 — covered</summary>

Accepted records cover vertex form factors, anomalous moments, electron-loop logs, and the infrared charge-radius qualification. The anchor records are Lepton charge radius and infrared qualification; Electron-loop logarithm in the muon magnetic moment; One-loop vertex form-factor evaluation; Schwinger one-loop anomalous magnetic moment; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.lepton-charge-radius-infrared-qualification`, `weinberg-1.muon-anomalous-moment-electron-loop-log`, `weinberg-1.one-loop-vertex-form-factor-evaluation`, `weinberg-1.schwinger-one-loop-anomalous-magnetic-moment`.

</details>

<details>
<summary>Section 11.4 — covered</summary>

Accepted records cover Pauli–Villars electron self energy and its infrared qualification. The anchor records are Lepton charge radius and infrared qualification; One-loop electron self-energy with Pauli–Villars regulation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.lepton-charge-radius-infrared-qualification`, `weinberg-1.one-loop-electron-self-energy-pauli-villars`.

</details>

<details>
<summary>Section 11.A — covered</summary>

Accepted records cover Feynman-parameter and dimensional-integral machinery used in the loop calculations. The anchor records are Appendix: Feynman parameters and dimensional loop integrals; One-loop electron self-energy with Pauli–Villars regulation; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.appendix-feynman-parameters-dimensional-integrals`, `weinberg-1.one-loop-electron-self-energy-pauli-villars`.

</details>

<details>
<summary>Section 11.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Problem: cubic neutral-scalar one-loop scattering; Problem: neutral-scalar electron mass shift; Problem: neutral-scalar effects on magnetic moment and Z2; Problem: charged-scalar vacuum polarization, Z3, and 2s shift; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.problem-cubic-neutral-scalar-scattering`, `weinberg-1.problem-neutral-scalar-electron-mass-shift`, `weinberg-1.problem-neutral-scalar-magnetic-moment-z2`, `weinberg-1.problem-scalar-vacuum-polarization-z3-uehling`.

</details>

<details>
<summary>Section 12 — covered</summary>

Accepted records cover power counting, subtractions, renormalizable interactions, EFT suppression, Wilsonian flow, and accidental flavor symmetry. The anchor records are Accidental lepton flavor conservation of renormalizable electrodynamics; BPHZ forest subtraction with non-overlapping boxes; EFT predictivity boundary near M; Integrating out electrons and matching low-energy light-by-light EFT; Renormalization with finite or infinite symmetry-allowed couplings; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.accidental-lepton-flavor-symmetry`, `weinberg-1.bphz-forest-subtractions`, `weinberg-1.eft-predictivity-boundary-near-m`, `weinberg-1.euler-heisenberg-matching-and-light-by-light-eft`, `weinberg-1.general-renormalization-equal-status`, `weinberg-1.high-spin-renormalizability-and-gauge-exceptions`, `weinberg-1.higher-derivative-poles-and-eft-cutoff`, `weinberg-1.local-divergent-polynomial-counterterms`, `weinberg-1.nonrenormalizable-eft-suppression`, `weinberg-1.overlap-counterterm-cancellation-example`, `weinberg-1.pauli-term-why-absent-from-minimal-qed`, `weinberg-1.phi4-renormalization-point-dependence`, `weinberg-1.power-counting-convergence-theorem-scope`, `weinberg-1.power-counting-spin-and-gauge-qualification`, `weinberg-1.qed-1pi-divergences-and-ward-reduction`, `weinberg-1.qed-counterterm-onshell-subtraction`, `weinberg-1.renormalizable-critical-surface`, `weinberg-1.scalar-eft-power-counting-example`, `weinberg-1.scalar-spinor-photon-renormalizable-catalogue`, `weinberg-1.shift-symmetric-scalar-derivative-eft`, `weinberg-1.superficial-degree-of-divergence`, `weinberg-1.symmetry-complete-renormalizable-lagrangian`, `weinberg-1.wilson-conventional-equivalence-and-tradeoffs`, `weinberg-1.wilsonian-floating-cutoff-flow`.

</details>

<details>
<summary>Section 12.1 — covered</summary>

Accepted records cover superficial divergence, spin/gauge qualifications, and the explicitly imported all-subintegration convergence criterion. The anchor records are Renormalization with finite or infinite symmetry-allowed couplings; High-spin power counting and gauge-field exceptions; All-subintegration power-counting criterion and external proof limit; Power-counting spin values and gauge-current qualification; Superficial degree of divergence from graph counting; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.general-renormalization-equal-status`, `weinberg-1.high-spin-renormalizability-and-gauge-exceptions`, `weinberg-1.power-counting-convergence-theorem-scope`, `weinberg-1.power-counting-spin-and-gauge-qualification`, `weinberg-1.superficial-degree-of-divergence`.

</details>

<details>
<summary>Section 12.2 — covered</summary>

Accepted records cover local counterterms, forests and overlap cancellation, QED Ward reduction, and on-shell subtraction. The anchor records are BPHZ forest subtraction with non-overlapping boxes; Divergent local polynomial and counterterm matching; Overlapping QED photon-self-energy counterterm cancellation; Scalar phi^4 coupling defined at an off-shell symmetric point; All-subintegration power-counting criterion and external proof limit; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bphz-forest-subtractions`, `weinberg-1.local-divergent-polynomial-counterterms`, `weinberg-1.overlap-counterterm-cancellation-example`, `weinberg-1.phi4-renormalization-point-dependence`, `weinberg-1.power-counting-convergence-theorem-scope`, `weinberg-1.qed-1pi-divergences-and-ward-reduction`, `weinberg-1.qed-counterterm-onshell-subtraction`, `weinberg-1.symmetry-complete-renormalizable-lagrangian`.

</details>

<details>
<summary>Section 12.3 — covered</summary>

Accepted records cover the EFT account of nonrenormalizable suppression, Pauli terms, derivative scalars, matching, and cutoff limits. The anchor records are EFT predictivity boundary near M; Integrating out electrons and matching low-energy light-by-light EFT; High-spin power counting and gauge-field exceptions; Higher-derivative poles lie at the EFT cutoff; Effective-theory suppression of higher-dimensional interactions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.eft-predictivity-boundary-near-m`, `weinberg-1.euler-heisenberg-matching-and-light-by-light-eft`, `weinberg-1.high-spin-renormalizability-and-gauge-exceptions`, `weinberg-1.higher-derivative-poles-and-eft-cutoff`, `weinberg-1.nonrenormalizable-eft-suppression`, `weinberg-1.pauli-term-why-absent-from-minimal-qed`, `weinberg-1.phi4-renormalization-point-dependence`, `weinberg-1.scalar-eft-power-counting-example`, `weinberg-1.scalar-spinor-photon-renormalizable-catalogue`, `weinberg-1.shift-symmetric-scalar-derivative-eft`.

</details>

<details>
<summary>Section 12.4 — covered</summary>

Accepted records cover floating-cutoff flow, critical surfaces, and Wilson/conventional tradeoffs. The anchor records are Renormalizable critical surface as a stable manifold; Wilson and conventional renormalization: equivalence and tradeoffs; Floating-cutoff Wilsonian coupling flow; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.renormalizable-critical-surface`, `weinberg-1.wilson-conventional-equivalence-and-tradeoffs`, `weinberg-1.wilsonian-floating-cutoff-flow`.

</details>

<details>
<summary>Section 12.5 — covered</summary>

Accepted records cover accidental lepton-flavor conservation and its higher-dimensional limitation. The anchor records are Accidental lepton flavor conservation of renormalizable electrodynamics; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.accidental-lepton-flavor-symmetry`.

</details>

<details>
<summary>Section 12.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Accidental lepton flavor conservation of renormalizable electrodynamics; Dimension-five Pauli term and why minimal QED omits it; Problem: leading and next-to-leading QED EFT operators without C/P/T; Problem: cancel the overlapping electron self-energy divergence; Problem: scalar renormalizable terms in 2, 3, and 6 dimensions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.accidental-lepton-flavor-symmetry`, `weinberg-1.pauli-term-why-absent-from-minimal-qed`, `weinberg-1.problem-qed-eft-cpt-relaxed-operators`, `weinberg-1.problem-qed-electron-self-energy-overlap`, `weinberg-1.problem-scalar-renormalizable-terms-by-dimension`, `weinberg-1.problem-yukawa-scalar-self-energy-subtraction`.

</details>

<details>
<summary>Section 13 — covered</summary>

Accepted records cover soft emission, infrared inclusivity, KLN sums, low-energy Compton behavior, and external-field limits. The anchor records are Collinear divergences and KLN sums over dangerous states; External-field diagram content and ladder limitation; Heavy-line eikonal permutation identity; Heavy-target external-field approximation; Low-energy photon scattering universality; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.collinear-and-kln-dangerous-states`, `weinberg-1.external-field-ladder-limitations`, `weinberg-1.heavy-line-eikonal-permutation-identity`, `weinberg-1.heavy-target-external-field-limit`, `weinberg-1.low-energy-compton-universality`, `weinberg-1.massive-qed-final-state-inclusivity`, `weinberg-1.multi-soft-photon-factorization`, `weinberg-1.real-soft-inclusive-rate`, `weinberg-1.soft-graviton-inclusive-energy-law`, `weinberg-1.soft-massless-spin-consistency`, `weinberg-1.soft-photon-single-emission-theorem`, `weinberg-1.soft-virtual-z-factor-accounting`, `weinberg-1.virtual-soft-photon-exponentiation`.

</details>

<details>
<summary>Section 13.1 — covered</summary>

Accepted records cover single- and multi-soft photon factors and the massless-spin consistency constraint. The anchor records are Arbitrary multi-soft-photon factorization; Lorentz-consistency constraints from soft massless emission; Universal leading soft-photon emission factor; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.multi-soft-photon-factorization`, `weinberg-1.soft-massless-spin-consistency`, `weinberg-1.soft-photon-single-emission-theorem`.

</details>

<details>
<summary>Section 13.2 — covered</summary>

Accepted records cover virtual-soft exponentiation and external-line Z-factor accounting. The anchor records are Arbitrary multi-soft-photon factorization; External-line omission reconciled by infrared-divergent Z factors; Virtual soft-photon exponentiation and infrared rate suppression; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.multi-soft-photon-factorization`, `weinberg-1.soft-virtual-z-factor-accounting`, `weinberg-1.virtual-soft-photon-exponentiation`.

</details>

<details>
<summary>Section 13.3 — covered</summary>

Accepted records cover real-soft inclusivity and its cancellation role. The anchor records are Real soft photons make the observable rate infrared finite; Soft-graviton inclusive energy law; External-line omission reconciled by infrared-divergent Z factors; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.real-soft-inclusive-rate`, `weinberg-1.soft-graviton-inclusive-energy-law`, `weinberg-1.soft-virtual-z-factor-accounting`.

</details>

<details>
<summary>Section 13.4 — covered</summary>

Accepted records cover collinear/KLN dangerous states, massive-QED final-state inclusivity, and the soft-graviton energy law. The anchor records are Collinear divergences and KLN sums over dangerous states; Why massive QED needs only final-state soft sums; Real soft photons make the observable rate infrared finite; Soft-graviton inclusive energy law; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.collinear-and-kln-dangerous-states`, `weinberg-1.massive-qed-final-state-inclusivity`, `weinberg-1.real-soft-inclusive-rate`, `weinberg-1.soft-graviton-inclusive-energy-law`.

</details>

<details>
<summary>Section 13.5 — covered</summary>

Accepted records cover low-energy Compton universality with the massive-QED qualification. The anchor records are Low-energy photon scattering universality; Why massive QED needs only final-state soft sums; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.low-energy-compton-universality`, `weinberg-1.massive-qed-final-state-inclusivity`.

</details>

<details>
<summary>Section 13.6 — covered</summary>

Accepted records cover heavy-target external fields, eikonal permutations, and omitted ladder/correction content. The anchor records are External-field diagram content and ladder limitation; Heavy-line eikonal permutation identity; Heavy-target external-field approximation; Low-energy photon scattering universality; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.external-field-ladder-limitations`, `weinberg-1.heavy-line-eikonal-permutation-identity`, `weinberg-1.heavy-target-external-field-limit`, `weinberg-1.low-energy-compton-universality`.

</details>

<details>
<summary>Section 13.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are External-field diagram content and ladder limitation; Problem: prove the heavy-line eikonal permutation identity; Problem: soft emission of a light massive vector in heavy-fermion decay; Problem: next low-energy photon-scattering term; Problem: pion-pair soft-photon energy dependence; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.external-field-ladder-limitations`, `weinberg-1.problem-eikonal-permutation-identity`, `weinberg-1.problem-light-vector-soft-decay`, `weinberg-1.problem-next-low-energy-compton-term`, `weinberg-1.problem-soft-pion-inclusive-rate`, `weinberg-1.problem-soft-scalar-inclusive-rate`.

</details>

<details>
<summary>Section 14 — covered</summary>

Accepted records cover external-field Dirac bound states and the scale-separated Lamb-shift calculation. The anchor records are Coulomb bound states require all-order resummation at atomic momentum; Bound-state energy shift from the external-field self-energy pole; Central electrostatic Dirac spinors and coupled radial equations; Coulomb Dirac spectrum, admissibility, and fine-structure degeneracy; External-field Dirac modes, charge sectors, and canonical normalization; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bound-state-coulomb-resummation-scale`, `weinberg-1.bound-state-energy-shift-from-propagator-pole`, `weinberg-1.central-electrostatic-dirac-radial-decomposition`, `weinberg-1.coulomb-dirac-spectrum-and-degeneracy`, `weinberg-1.external-field-dirac-mode-completeness`, `weinberg-1.external-field-feynman-propagator`, `weinberg-1.external-field-self-energy-diagrams-and-weak-field-master-formula`, `weinberg-1.high-energy-lamb-shift-form-factors`, `weinberg-1.hydrogen-lamb-shift-numerics-and-higher-correction-limit`, `weinberg-1.lamb-shift-cancellation-and-hydrogenic-formulas`, `weinberg-1.lamb-shift-photon-mass-scale-separation`, `weinberg-1.low-energy-lamb-shift-spectral-sum-and-width`, `weinberg-1.nonrelativistic-external-dirac-reduction-and-bilinears`.

</details>

<details>
<summary>Section 14.1 — covered</summary>

Accepted records cover Coulomb resummation, external Dirac modes, radial equations, spectrum, and nonrelativistic reduction. The anchor records are Coulomb bound states require all-order resummation at atomic momentum; Central electrostatic Dirac spinors and coupled radial equations; Coulomb Dirac spectrum, admissibility, and fine-structure degeneracy; External-field Dirac modes, charge sectors, and canonical normalization; Nonrelativistic external-Dirac reduction and bilinear matrix elements; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bound-state-coulomb-resummation-scale`, `weinberg-1.central-electrostatic-dirac-radial-decomposition`, `weinberg-1.coulomb-dirac-spectrum-and-degeneracy`, `weinberg-1.external-field-dirac-mode-completeness`, `weinberg-1.nonrelativistic-external-dirac-reduction-and-bilinears`.

</details>

<details>
<summary>Section 14.2 — covered</summary>

Accepted records cover external-field propagators, self-energy diagrams, and pole-based energy shifts. The anchor records are Bound-state energy shift from the external-field self-energy pole; Feynman propagator in a static external Dirac field; External-field self-energy diagrams and momentum-space energy-shift formula; Nonrelativistic external-Dirac reduction and bilinear matrix elements; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.bound-state-energy-shift-from-propagator-pole`, `weinberg-1.external-field-feynman-propagator`, `weinberg-1.external-field-self-energy-diagrams-and-weak-field-master-formula`, `weinberg-1.nonrelativistic-external-dirac-reduction-and-bilinears`.

</details>

<details>
<summary>Section 14.3 — covered</summary>

Accepted records cover high/low-energy separation, cancellation, spectral sums, Lamb-shift formulas, and stated higher-correction limits. The anchor records are External-field self-energy diagrams and momentum-space energy-shift formula; High-energy Lamb-shift contribution from on-shell form factors; Hydrogen Lamb-shift numerical result and omitted-correction limit; Regulator-independent Lamb shift and hydrogenic mean-excitation formulas; Photon-mass separation of high- and low-energy Lamb-shift contributions; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.external-field-self-energy-diagrams-and-weak-field-master-formula`, `weinberg-1.high-energy-lamb-shift-form-factors`, `weinberg-1.hydrogen-lamb-shift-numerics-and-higher-correction-limit`, `weinberg-1.lamb-shift-cancellation-and-hydrogenic-formulas`, `weinberg-1.lamb-shift-photon-mass-scale-separation`, `weinberg-1.low-energy-lamb-shift-spectral-sum-and-width`.

</details>

<details>
<summary>Section 14.problems — covered</summary>

Accepted records cover the independently stated exercises that apply the chapter’s accepted methods and retain their task status rather than being recast as text-proved results. The anchor records are Hydrogen Lamb-shift numerical result and omitted-correction limit; Problem: external-field charged-scalar mode completeness and expansion; Problem: scalar bound-state energy shift from the radiative kernel; Problem: hydrogen 2p radiative decay rate from the Lamb-shift calculation; Problem: 1s shift from a light scalar with intermediate mass; the complete list includes records whose accepted source section identifies this material even when it falls on a shared inventory boundary page, together with genuinely shared page content. Thus the assessment follows record semantics and evidence roles rather than a nonoverlapping page-interval assignment.

Records: `weinberg-1.hydrogen-lamb-shift-numerics-and-higher-correction-limit`, `weinberg-1.problem-external-scalar-mode-completeness`, `weinberg-1.problem-external-scalar-radiative-energy-shift`, `weinberg-1.problem-hydrogen-2p-radiative-decay-rate`, `weinberg-1.problem-massive-light-scalar-hydrogenic-1s-shift`, `weinberg-1.problem-massless-scalar-hydrogenic-1s-shift`.

</details>
