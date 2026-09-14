# Whole-book graph reconciliation

This report records a review of the combined textbook graph after all its source scopes were accepted. Terra/high assessed semantic section coverage, cross-unit dependencies, independent routes, and proof limits. Sol/high independently reviewed that assessment and accepted the assessment without requiring adjudication.

The audited baseline contains **875 nodes, 972 edges, and 254 inventory sections**. It is identified by the graph-content digest below. Subsequent source-backed amendments are listed separately; this snapshot is not an automatic review of arbitrary later changes.

`sha256:4a90511ca4ec0c164e9ed0f93f44bd422ad1332cba07b25d9f67b80966b93863`

The end human audit is **pending**. Shared-graph alignment and cross-volume follow-ups remain separate from this book's audit. See the current [review declaration](review.yaml), [coverage ledger](coverage.yaml), and [scientific decision log](adjudications.yaml).

## Findings and source-backed amendments

### schwartz-inventory-p813-appendices-divider

Printed p. 813 is an APPENDICES divider, outside the 254 substantive section records and not yet listed in coverage.excluded_whole_pages. The accepted final run confirms it has no scientific content; leaving it only implicit risks later inventory ambiguity.

**Resolved by an explicit inventory annotation.** The coverage ledger explicitly classifies printed page 813 as a nonconceptual divider. The historical 818-page reviewed-scope denominator is preserved; no scientific record is added or amended.

Source context: schwartz pp. 813–813.

## Audit decisions

The independent critic accepted the assessment. No disputed finding required final adjudication.

## Cross-unit assessment

- Inspected all 903 prerequisite, 34 alternative, 19 evidence, and 16 pedagogical edges with their relation, necessity, source level, target level, rationale, and failure mode. The frozen graph distinguishes the minimum actual use/derive inputs from mere chronology and contains no new combined dependency that warrants reopening a closed final decision.
- Alternative edges are noncompulsory routes. In particular, the three spin-statistics derivations, the equilibrium and field-theory Einstein-coefficient routes, the regulator-comparison routes, and the 1PI/effective-action routes preserve route-local inputs without making every alternative input part of global planner closure; the 'necessary' strength on an alternative describes its own completed route only.
- Substantial problem branches are retained as source tasks with task-specific inputs, including the split spin, Compton, anomaly, amplitude, EFT, DIS, and SCET exercises. Their summaries and edge rationales do not use a requested answer as its own premise or merge independent branches merely because they occur on one page.
- The exact repeated normalized label 'Chiral Lagrangian derivative expansion' is not a duplicate defect. schwartz.chiral-lagrangian-derivative-expansion (22.3, pp. 401--403) represents the pion EFT, derivative/counterterm expansion, loop logarithms, cutoff, and QCD matching limit; schwartz.chiral-lagrangian-derivative-operators (28.2.2, p. 569) gives the SU(2)L x SU(2)R invariant operator construction and the symmetry-limit mass consequence. These are distinct treatments at useful granularity.
- The full-015 original appendix history is superseded by accepted full-015-extended context: its final accepted 20 new nodes, two authorized replacements, and 14 edges are in the frozen graph. This reconciliation does not treat the original deferred history as a current content gap.
- The only new whole-book inventory concern is the already confirmed nonconceptual classification of p. 813. It is an inventory disposition, not scientific missing coverage, and has no graph-node, edge, or denominator consequence.

## Conventions and proof boundaries

Appendix A conventions are represented as reusable calculation inputs: natural units and dimensions, Fourier/operator normalizations, metric/sign/covariant-derivative/propagator choices, mode and diagram conventions, and Dirac/chiral identities. They remain evidence-bearing conventions rather than decorative front matter.

Records: `schwartz.appendix-natural-units-and-mass-dimensions`, `schwartz.fourier-transform-derivative-operator-correspondence`, `schwartz.appendix-sign-propagator-and-covariant-derivative-conventions`, `schwartz.appendix-free-mode-and-diagram-conventions`, `schwartz.appendix-dirac-algebra-and-field-strength-identities`.

Appendix B retains denominator, proper-time, contour, dimensional-continuation, gamma-five, scalar-integral, pole, tensor-reduction, derivative, and Pauli--Villars conventions and limits. The dimensional logarithm is represented as a completed route with joint inputs; its three regulator routes remain alternatives.

Records: `schwartz.appendix-feynman-parameter-identities-and-shift`, `schwartz.appendix-schwinger-parameter-identities`, `schwartz.appendix-wick-rotation-method`, `schwartz.appendix-dimensional-continuation-conventions`, `schwartz.appendix-dimreg-gamma5-assumption`, `schwartz.appendix-dimensional-scalar-integral-formula`, `schwartz.appendix-dimensional-poles-and-scaleless-integrals`, `schwartz.appendix-lorentz-tensor-loop-reduction`, `schwartz.appendix-derivative-regularization-method`, `schwartz.appendix-pauli-villars-regularization-method`.

Publication matter, contents, prefaces, reviewed blanks, and part dividers require no concept node. The p. 813 APPENDICES divider is separately reported below for an explicit inventory supplement; it does not alter the accepted substantive denominator or create filler science.

These records explicitly retain the source's external/topological proof limits: one-loop exactness is reported with its topological proof outside the displayed calculation; the DIS analyticity proof is attributed externally; and the weak-EFT OPE proof is deferred to Chapter 32. They are qualified imports, not recursively supplied proofs.

Records: `schwartz.abelian-chiral-anomaly-and-one-loop-exactness`, `schwartz.dis-analytic-contour-moment-route`, `schwartz.weak-effective-lagrangian-locality-and-power-suppression`.

The theorem/bound/evidence records preserve their stated scope: the rigorous CPT proof and Froissart hypotheses are not supplied, strong-coupling area-law continuation remains open, and the Weinberg--Witten statement carries its fixed-spacetime qualification.

Records: `schwartz.cpt-theorem-scope`, `schwartz.froissart-total-cross-section-growth-bound`, `schwartz.wilson-area-law-confinement-evidence-qualification`, `schwartz.weinberg-witten-spin-two-and-fixed-spacetime-qualification`.

These records retain route-local limits: light-cone scaling is not elevated to a general proof, the half-integer causality route is sufficient rather than necessary, the printed proper-time anomaly sign discrepancy is recorded, and the dimensional gamma-five prescription remains an assumption with anomaly subtlety.

Records: `schwartz.lightcone-factorization-scaling-route-and-limit`, `schwartz.higher-spin-causality-statistics-and-limitation`, `schwartz.proper-time-background-axial-anomaly-route`, `schwartz.appendix-dimreg-gamma5-assumption`.

## Section coverage assessment

These mappings follow the accepted records' section evidence and content. A shared boundary page may contribute to multiple sections; a table number does not determine its section.

<details>
<summary>Section 1 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Blackbody cavity modes and the classical spectrum; Bosonic spontaneous and stimulated emission factor; Einstein emission and absorption coefficient relations; Equilibration requires particle creation and destruction; Fermi golden rule for a field-creating interaction; Field-theoretic derivation of Einstein coefficients; Radiation intensity and mode occupation; Planck thermal radiation spectrum; Quantized massless photon modes; Single-mode oscillator number algebra; Two-level equilibrium detailed balance; Ultraviolet catastrophe. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.blackbody-cavity-modes-and-classical-spectrum`, `schwartz.bosonic-spontaneous-and-stimulated-emission-factor`, `schwartz.einstein-emission-and-absorption-coefficients`, `schwartz.equilibration-requires-particle-creation-and-destruction`, `schwartz.fermi-golden-rule-field-interaction`, `schwartz.field-theoretic-einstein-coefficient-derivation`, `schwartz.intensity-mode-occupation-relation`, `schwartz.planck-thermal-radiation-spectrum`, `schwartz.quantized-massless-photon-modes`, `schwartz.single-mode-oscillator-number-algebra`, `schwartz.two-level-equilibrium-detailed-balance`, `schwartz.ultraviolet-catastrophe`.

</details>

<details>
<summary>Section 1.1 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Blackbody cavity modes and the classical spectrum; Quantized massless photon modes; Ultraviolet catastrophe. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.blackbody-cavity-modes-and-classical-spectrum`, `schwartz.quantized-massless-photon-modes`, `schwartz.ultraviolet-catastrophe`.

</details>

<details>
<summary>Section 1.2 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Einstein emission and absorption coefficient relations; Equilibration requires particle creation and destruction; Planck thermal radiation spectrum; Two-level equilibrium detailed balance. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.einstein-emission-and-absorption-coefficients`, `schwartz.equilibration-requires-particle-creation-and-destruction`, `schwartz.planck-thermal-radiation-spectrum`, `schwartz.two-level-equilibrium-detailed-balance`.

</details>

<details>
<summary>Section 1.3 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Bosonic spontaneous and stimulated emission factor; Einstein emission and absorption coefficient relations; Fermi golden rule for a field-creating interaction; Field-theoretic derivation of Einstein coefficients; Radiation intensity and mode occupation; Single-mode oscillator number algebra. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bosonic-spontaneous-and-stimulated-emission-factor`, `schwartz.einstein-emission-and-absorption-coefficients`, `schwartz.fermi-golden-rule-field-interaction`, `schwartz.field-theoretic-einstein-coefficient-derivation`, `schwartz.intensity-mode-occupation-relation`, `schwartz.single-mode-oscillator-number-algebra`.

</details>

<details>
<summary>Section 2 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Atom-photon interaction Hamiltonian; Canonical and path-integral quantization routes; Canonical quantum harmonic oscillator; Discrete Lorentz transformations and causal type; Equal-time scalar-field commutation relations; Fock space and physical particle sectors; Free scalar field as a momentum-mode expansion; Heisenberg evolution of a free scalar field; Lorentz contractions and the d'Alembertian; Lorentz-invariant kinematics method; Lorentz metric and transformations; Lorentz transformation laws for scalar, vector, and tensor fields; Massless field plane waves as oscillator modes; Maxwell theory in Lorenz gauge; Momentum-mode creation and annihilation algebra; One-particle wavefunction and nonrelativistic limit; One-particle position state from a field operator; Rapidity parameterization of boosts; Relativistic energy allows particle production; Rotations and invariant inner products; Second quantization as many mode oscillators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.atom-photon-interaction-hamiltonian`, `schwartz.canonical-and-path-integral-quantization-routes`, `schwartz.canonical-quantum-harmonic-oscillator`, `schwartz.discrete-lorentz-transformations-and-causal-type`, `schwartz.equal-time-scalar-field-commutation-relations`, `schwartz.fock-space-particle-sectors`, `schwartz.free-scalar-field-mode-expansion`, `schwartz.heisenberg-free-field-time-evolution`, `schwartz.lorentz-covariant-index-contractions-and-dalembertian`, `schwartz.lorentz-invariant-kinematics-method`, `schwartz.lorentz-metric-and-transformations`, `schwartz.lorentz-transformation-laws-for-fields`, `schwartz.massless-field-plane-wave-oscillator-modes`, `schwartz.maxwell-lorenz-gauge-wave-equation`, `schwartz.momentum-mode-creation-annihilation-algebra`, `schwartz.one-particle-nonrelativistic-wavefunction-limit`, `schwartz.one-particle-position-state-from-field`, `schwartz.rapidity-parameterization-of-boosts`, `schwartz.relativistic-energy-allows-particle-production`, `schwartz.rotations-and-invariant-inner-products`, `schwartz.second-quantization-many-mode-particle-interpretation`.

</details>

<details>
<summary>Section 2.1 — covered</summary>

The accepted concept, method, representation records substantively represent this section's distinct content: Canonical and path-integral quantization routes; Discrete Lorentz transformations and causal type; Lorentz contractions and the d'Alembertian; Lorentz metric and transformations; Lorentz transformation laws for scalar, vector, and tensor fields; Rapidity parameterization of boosts; Relativistic energy allows particle production; Rotations and invariant inner products. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.canonical-and-path-integral-quantization-routes`, `schwartz.discrete-lorentz-transformations-and-causal-type`, `schwartz.lorentz-covariant-index-contractions-and-dalembertian`, `schwartz.lorentz-metric-and-transformations`, `schwartz.lorentz-transformation-laws-for-fields`, `schwartz.rapidity-parameterization-of-boosts`, `schwartz.relativistic-energy-allows-particle-production`, `schwartz.rotations-and-invariant-inner-products`.

</details>

<details>
<summary>Section 2.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Canonical quantum harmonic oscillator; Lorentz-invariant kinematics method; Massless field plane waves as oscillator modes; Maxwell theory in Lorenz gauge. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.canonical-quantum-harmonic-oscillator`, `schwartz.lorentz-invariant-kinematics-method`, `schwartz.massless-field-plane-wave-oscillator-modes`, `schwartz.maxwell-lorenz-gauge-wave-equation`.

</details>

<details>
<summary>Section 2.3 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Atom-photon interaction Hamiltonian; Equal-time scalar-field commutation relations; Fock space and physical particle sectors; Free scalar field as a momentum-mode expansion; Heisenberg evolution of a free scalar field; Momentum-mode creation and annihilation algebra; One-particle wavefunction and nonrelativistic limit; One-particle position state from a field operator; Second quantization as many mode oscillators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.atom-photon-interaction-hamiltonian`, `schwartz.equal-time-scalar-field-commutation-relations`, `schwartz.fock-space-particle-sectors`, `schwartz.free-scalar-field-mode-expansion`, `schwartz.heisenberg-free-field-time-evolution`, `schwartz.momentum-mode-creation-annihilation-algebra`, `schwartz.one-particle-nonrelativistic-wavefunction-limit`, `schwartz.one-particle-position-state-from-field`, `schwartz.second-quantization-many-mode-particle-interpretation`.

</details>

<details>
<summary>Section 2.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Coherent states of the harmonic oscillator; Compton scattering as photon momentum application; Discrete Lorentz transformations and causal type; GZK threshold as an invariant-collision application; Lorentz-invariant kinematics method; Lorentz-invariant on-shell phase-space measure; Rapidity parameterization of boosts. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.coherent-states-of-the-oscillator`, `schwartz.compton-scattering-as-photon-momentum-application`, `schwartz.discrete-lorentz-transformations-and-causal-type`, `schwartz.gzk-threshold-as-invariant-collision-application`, `schwartz.lorentz-invariant-kinematics-method`, `schwartz.lorentz-invariant-onshell-phase-space-measure`, `schwartz.rapidity-parameterization-of-boosts`.

</details>

<details>
<summary>Section 3 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Action variation and the asymptotic-boundary assumption; Canonical scalar-field energy density; Field Hamiltonians, Lagrangians, and Legendre transforms; Complex scalar global U(1) symmetry; Coulomb potential from field propagation; Roles of currents and nondynamical sources; Euler–Lagrange and Klein–Gordon equations; Fourier correspondence and Appendix A normalization; Green-function propagator kernel; Higher-derivative terms, effective interactions, and instability; Kinetic terms, interactions, and dynamical fields; Noether current and conserved charge; Scope of Noether's theorem; Perturbative nonlinear classical-field solution; Sourced Maxwell equations from the action; Translation symmetry and the canonical energy-momentum tensor. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.action-variation-and-boundary-assumption`, `schwartz.canonical-scalar-field-energy-density`, `schwartz.classical-field-hamiltonian-lagrangian-legendre-transform`, `schwartz.complex-scalar-global-u1-symmetry`, `schwartz.coulomb-potential-from-field-propagation`, `schwartz.current-roles-and-nondynamical-sources`, `schwartz.euler-lagrange-and-klein-gordon-equations`, `schwartz.fourier-transform-derivative-operator-correspondence`, `schwartz.green-function-propagator-kernel`, `schwartz.higher-derivative-effective-interactions-and-instability`, `schwartz.kinetic-terms-interactions-and-dynamical-fields`, `schwartz.noether-current-and-conserved-charge`, `schwartz.noether-theorem-scope`, `schwartz.perturbative-nonlinear-classical-field-solution`, `schwartz.sourced-maxwell-equations-from-action`, `schwartz.translation-symmetry-and-canonical-energy-momentum-tensor`.

</details>

<details>
<summary>Section 3.1 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Canonical scalar-field energy density; Field Hamiltonians, Lagrangians, and Legendre transforms. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.canonical-scalar-field-energy-density`, `schwartz.classical-field-hamiltonian-lagrangian-legendre-transform`.

</details>

<details>
<summary>Section 3.2 — covered</summary>

The accepted assumption, concept records substantively represent this section's distinct content: Action variation and the asymptotic-boundary assumption; Kinetic terms, interactions, and dynamical fields. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.action-variation-and-boundary-assumption`, `schwartz.kinetic-terms-interactions-and-dynamical-fields`.

</details>

<details>
<summary>Section 3.3 — covered</summary>

The accepted assumption, concept, result records substantively represent this section's distinct content: Complex scalar global U(1) symmetry; Roles of currents and nondynamical sources; Euler–Lagrange and Klein–Gordon equations; Higher-derivative terms, effective interactions, and instability; Noether current and conserved charge; Scope of Noether's theorem; Translation symmetry and the canonical energy-momentum tensor. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.complex-scalar-global-u1-symmetry`, `schwartz.current-roles-and-nondynamical-sources`, `schwartz.euler-lagrange-and-klein-gordon-equations`, `schwartz.higher-derivative-effective-interactions-and-instability`, `schwartz.noether-current-and-conserved-charge`, `schwartz.noether-theorem-scope`, `schwartz.translation-symmetry-and-canonical-energy-momentum-tensor`.

</details>

<details>
<summary>Section 3.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Fourier correspondence and Appendix A normalization; Sourced Maxwell equations from the action. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.fourier-transform-derivative-operator-correspondence`, `schwartz.sourced-maxwell-equations-from-action`.

</details>

<details>
<summary>Section 3.5 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Coulomb potential from field propagation; Green-function propagator kernel; Perturbative nonlinear classical-field solution. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.coulomb-potential-from-field-propagation`, `schwartz.green-function-propagator-kernel`, `schwartz.perturbative-nonlinear-classical-field-solution`.

</details>

<details>
<summary>Section 3.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Classical Feynman diagrams and rules; Classical spontaneous symmetry breaking; Energy-momentum tensor improvement ambiguity; Euler–Lagrange and Klein–Gordon equations; Graviton polarizations and trace coupling; Lorentz Noether currents and boost charges; Nonlinear gravity, dimensional analysis, and perihelion shift; Photon polarizations, current conservation, and causality; Classical-field and quantum-matter consistency question; Yukawa potential and massive-vector constraint. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.classical-feynman-diagrams-and-rules`, `schwartz.classical-spontaneous-symmetry-breaking`, `schwartz.energy-momentum-tensor-improvement-ambiguity`, `schwartz.euler-lagrange-and-klein-gordon-equations`, `schwartz.graviton-polarizations-and-trace-coupling`, `schwartz.lorentz-noether-currents-and-boost-charges`, `schwartz.nonlinear-gravity-dimensional-analysis-and-perihelion`, `schwartz.photon-polarizations-current-conservation-and-causality`, `schwartz.semiclassical-field-matter-consistency-question`, `schwartz.yukawa-potential-and-massive-vector-constraint`.

</details>

<details>
<summary>Section 4 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Advanced and retarded OFPT time orderings; Lamb-shift ultraviolet phase-space divergence; Lippmann–Schwinger scattering equation; Off-shell momentum from summed OFPT orderings; OFPT on-shell intermediate states; Relativistically normalized OFPT rules; Transfer matrix and Born series; Zero-point energy and observable differences. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.advanced-retarded-time-ordering-sum`, `schwartz.lamb-shift-ultraviolet-phase-space-divergence`, `schwartz.lippmann-schwinger-scattering-equation`, `schwartz.offshell-momentum-from-ofpt`, `schwartz.ofpt-on-shell-intermediate-states`, `schwartz.ofpt-relativistic-rules`, `schwartz.transfer-matrix-born-series`, `schwartz.zero-point-energy-observable-differences`.

</details>

<details>
<summary>Section 4.1 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Advanced and retarded OFPT time orderings; Lippmann–Schwinger scattering equation; Off-shell momentum from summed OFPT orderings; OFPT on-shell intermediate states; Transfer matrix and Born series. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.advanced-retarded-time-ordering-sum`, `schwartz.lippmann-schwinger-scattering-equation`, `schwartz.offshell-momentum-from-ofpt`, `schwartz.ofpt-on-shell-intermediate-states`, `schwartz.transfer-matrix-born-series`.

</details>

<details>
<summary>Section 4.2 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Lamb-shift ultraviolet phase-space divergence; OFPT on-shell intermediate states; Relativistically normalized OFPT rules; Zero-point energy and observable differences. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.lamb-shift-ultraviolet-phase-space-divergence`, `schwartz.ofpt-on-shell-intermediate-states`, `schwartz.ofpt-relativistic-rules`, `schwartz.zero-point-energy-observable-differences`.

</details>

<details>
<summary>Section 4.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Lamb-shift ultraviolet phase-space divergence; OFPT annihilation time-slicings problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.lamb-shift-ultraviolet-phase-space-divergence`, `schwartz.ofpt-annihilation-time-slicings-problem`.

</details>

<details>
<summary>Section 5 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Center-of-mass 2→2 cross section; Cross section from flux, probability, and luminosity; Decay rate from phase space and time dilation; Lorentz-invariant phase space and cross section; Nonrelativistic Born–QFT Coulomb match; Relativistic normalization and delta-function regulation; S-matrix as an asymptotic-state map; Spin projections in e⁺e⁻→μ⁺μ⁻. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cm-two-to-two-cross-section`, `schwartz.cross-section-flux-probability-luminosity`, `schwartz.decay-rate-lips-and-time-dilation`, `schwartz.lorentz-invariant-phase-space-cross-section`, `schwartz.nonrelativistic-born-qft-coulomb-match`, `schwartz.relativistic-state-normalization-and-delta-regulation`, `schwartz.s-matrix-asymptotic-state-map`, `schwartz.spin-projection-annihilation-angular-distribution`.

</details>

<details>
<summary>Section 5.1 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Center-of-mass 2→2 cross section; Cross section from flux, probability, and luminosity; Decay rate from phase space and time dilation; Lorentz-invariant phase space and cross section; Relativistic normalization and delta-function regulation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cm-two-to-two-cross-section`, `schwartz.cross-section-flux-probability-luminosity`, `schwartz.decay-rate-lips-and-time-dilation`, `schwartz.lorentz-invariant-phase-space-cross-section`, `schwartz.relativistic-state-normalization-and-delta-regulation`.

</details>

<details>
<summary>Section 5.2 — covered</summary>

The accepted result records substantively represent this section's distinct content: Center-of-mass 2→2 cross section; Nonrelativistic Born–QFT Coulomb match. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cm-two-to-two-cross-section`, `schwartz.nonrelativistic-born-qft-coulomb-match`.

</details>

<details>
<summary>Section 5.3 — covered</summary>

The accepted result records substantively represent this section's distinct content: Spin projections in e⁺e⁻→μ⁺μ⁻. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.spin-projection-annihilation-angular-distribution`.

</details>

<details>
<summary>Section 5.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Circular-polarization annihilation problem; Lab-frame 2→2 cross-section problem; LIPS Lorentz-invariance problem; Three-body muon-decay phase-space problem; Rutherford-scattering correspondence problem; Spin projections in e⁺e⁻→μ⁺μ⁻. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.circular-polarization-annihilation-problem`, `schwartz.lab-frame-two-to-two-cross-section-problem`, `schwartz.lips-lorentz-invariance-problem`, `schwartz.multibody-decay-phase-space-problem`, `schwartz.rutherford-scattering-cross-section-problem`, `schwartz.spin-projection-annihilation-angular-distribution`.

</details>

<details>
<summary>Section 6 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Asymptotic-free-state assumption for LSZ; Feynman propagator iε contour prescription; Feynman propagator from time ordering; Generalized LSZ with interpolating operators; LSZ boundary-operator derivation; LSZ reduction as one-particle pole projection. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.asymptotic-freedom-assumption-for-lsz`, `schwartz.feynman-propagator-iepsilon-contour`, `schwartz.feynman-propagator-time-ordering`, `schwartz.generalized-lsz-interpolating-operators`, `schwartz.lsz-boundary-operator-derivation`, `schwartz.lsz-reduction-pole-projection`.

</details>

<details>
<summary>Section 6.1 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Asymptotic-free-state assumption for LSZ; Generalized LSZ with interpolating operators; LSZ boundary-operator derivation; LSZ reduction as one-particle pole projection. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.asymptotic-freedom-assumption-for-lsz`, `schwartz.generalized-lsz-interpolating-operators`, `schwartz.lsz-boundary-operator-derivation`, `schwartz.lsz-reduction-pole-projection`.

</details>

<details>
<summary>Section 6.2 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Feynman propagator iε contour prescription; Feynman propagator from time ordering. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.feynman-propagator-iepsilon-contour`, `schwartz.feynman-propagator-time-ordering`.

</details>

<details>
<summary>Section 6.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Advanced/retarded propagator integral problem; Feynman propagator iε contour prescription; General-operator creation/annihilation expansion problem; Position-space propagator and massless-limit problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.advanced-retarded-propagator-integrals-problem`, `schwartz.feynman-propagator-iepsilon-contour`, `schwartz.general-operator-creation-annihilation-expansion-problem`, `schwartz.position-space-propagator-massless-limit-problem`.

</details>

<details>
<summary>Section 7 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Derivative couplings and total-derivative invariance; Disconnected amplitudes and cluster decomposition; Hamiltonian contraction route to position-space rules; Vacuum-normalized interacting correlator; Interaction normalization and graph symmetry factors; Interaction-picture Dyson-series route; Lagrangian Schwinger–Dyson route to diagrams; Mandelstam channels in φ³ scattering; Momentum-flow conventions and identical final states; Momentum-space Feynman rules; Normal ordering and Wick’s theorem; Position-space Feynman rules; Schwinger–Dyson contact equations; Wick contractions and vacuum-bubble cancellation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.derivative-couplings-and-total-derivative-invariance`, `schwartz.disconnected-amplitudes-and-cluster-decomposition`, `schwartz.hamiltonian-contraction-route-to-position-rules`, `schwartz.interacting-correlator-vacuum-normalization`, `schwartz.interaction-normalization-and-symmetry-factors`, `schwartz.interaction-picture-dyson-series-route`, `schwartz.lagrangian-schwinger-dyson-feynman-rule-route`, `schwartz.mandelstam-channels-phi3-scattering`, `schwartz.momentum-flow-and-identical-final-states`, `schwartz.momentum-space-feynman-rules`, `schwartz.normal-ordering-and-wicks-theorem`, `schwartz.position-space-feynman-rules`, `schwartz.schwinger-dyson-contact-equations`, `schwartz.wick-contractions-and-vacuum-bubble-cancellation`.

</details>

<details>
<summary>Section 7.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Interaction normalization and graph symmetry factors; Lagrangian Schwinger–Dyson route to diagrams; Schwinger–Dyson contact equations. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.interaction-normalization-and-symmetry-factors`, `schwartz.lagrangian-schwinger-dyson-feynman-rule-route`, `schwartz.schwinger-dyson-contact-equations`.

</details>

<details>
<summary>Section 7.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Hamiltonian contraction route to position-space rules; Vacuum-normalized interacting correlator; Interaction-picture Dyson-series route; Position-space Feynman rules; Wick contractions and vacuum-bubble cancellation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hamiltonian-contraction-route-to-position-rules`, `schwartz.interacting-correlator-vacuum-normalization`, `schwartz.interaction-picture-dyson-series-route`, `schwartz.position-space-feynman-rules`, `schwartz.wick-contractions-and-vacuum-bubble-cancellation`.

</details>

<details>
<summary>Section 7.3 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Disconnected amplitudes and cluster decomposition; Hamiltonian contraction route to position-space rules; Momentum-flow conventions and identical final states; Momentum-space Feynman rules; Position-space Feynman rules. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.disconnected-amplitudes-and-cluster-decomposition`, `schwartz.hamiltonian-contraction-route-to-position-rules`, `schwartz.momentum-flow-and-identical-final-states`, `schwartz.momentum-space-feynman-rules`, `schwartz.position-space-feynman-rules`.

</details>

<details>
<summary>Section 7.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Derivative couplings and total-derivative invariance; Disconnected amplitudes and cluster decomposition; Mandelstam channels in φ³ scattering. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.derivative-couplings-and-total-derivative-invariance`, `schwartz.disconnected-amplitudes-and-cluster-decomposition`, `schwartz.mandelstam-channels-phi3-scattering`.

</details>

<details>
<summary>Section 7.A — covered</summary>

The accepted result records substantively represent this section's distinct content: Derivative couplings and total-derivative invariance; Normal ordering and Wick’s theorem. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.derivative-couplings-and-total-derivative-invariance`, `schwartz.normal-ordering-and-wicks-theorem`.

</details>

<details>
<summary>Section 7.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Derivative couplings and total-derivative invariance; Disconnected amplitudes and cluster decomposition; Loop-amplitude and LSZ translation problem; Mass-insertion propagator resummation problem; Møller scattering and spin-channel problem; Normal ordering and Wick’s theorem; Tetrahedron symmetry-factor problem; Unstable-particle width problem; Weak-decay scale-estimate problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.derivative-couplings-and-total-derivative-invariance`, `schwartz.disconnected-amplitudes-and-cluster-decomposition`, `schwartz.loop-amplitude-position-momentum-lsz-problem`, `schwartz.mass-insertion-propagator-resummation-problem`, `schwartz.moller-scattering-spin-channels-problem`, `schwartz.normal-ordering-and-wicks-theorem`, `schwartz.tetrahedron-symmetry-factor-problem`, `schwartz.unstable-particle-width-problem`, `schwartz.weak-decay-scale-estimate-problem`.

</details>

<details>
<summary>Section 8 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Covariant Rξ photon propagator; Fierz–Pauli massive spin-2 Lagrangian; Gauge-current minimal coupling and scalar contact term; Gauge invariance from longitudinal decoupling; Gauge-parameter independence from transverse contractions; Gauge redundancy, locality, and global gauge data; Little-group induced vector representations; Longitudinal decomposition and ghost test; Massive vector field quantization by polarization modes; Massive-vector longitudinal high-energy perturbative breakdown; Massive vector transverse and longitudinal polarization basis; Massless little-group derivation of the Ward identity; Massless Maxwell gauge redundancy and two modes; Massless spin-2 longitudinal-decoupling route to general relativity; Particle as an irreducible unitary Poincaré representation; Proca Lagrangian and massive spin-1 constraint; Scalar-QED local U(1) Lagrangian; Stueckelberg representation of a massive vector; Conflict between vector Lorentz covariance and positive norm; Wigner mass, spin, and polarization classification. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.covariant-rxi-photon-propagator`, `schwartz.fierz-pauli-massive-spin-two`, `schwartz.gauge-current-minimal-coupling`, `schwartz.gauge-invariance-from-longitudinal-decoupling`, `schwartz.gauge-parameter-independence-from-transversality`, `schwartz.gauge-redundancy-locality-and-global-data`, `schwartz.little-group-induced-vector-representations`, `schwartz.longitudinal-stueckelberg-ghost-test`, `schwartz.massive-vector-field-quantization`, `schwartz.massive-vector-longitudinal-perturbative-breakdown`, `schwartz.massive-vector-polarization-basis`, `schwartz.massless-little-group-ward-identity`, `schwartz.massless-maxwell-gauge-redundancy-and-two-modes`, `schwartz.massless-spin-two-to-general-relativity-route`, `schwartz.particle-as-unitary-poincare-irrep`, `schwartz.proca-lagrangian-and-spin-one-constraint`, `schwartz.scalar-qed-local-u1-lagrangian`, `schwartz.stueckelberg-massive-vector-representation`, `schwartz.vector-lorentz-unitarity-conflict`, `schwartz.wigner-mass-spin-polarization-classification`.

</details>

<details>
<summary>Section 8.1 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Particle as an irreducible unitary Poincaré representation; Conflict between vector Lorentz covariance and positive norm; Wigner mass, spin, and polarization classification. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.particle-as-unitary-poincare-irrep`, `schwartz.vector-lorentz-unitarity-conflict`, `schwartz.wigner-mass-spin-polarization-classification`.

</details>

<details>
<summary>Section 8.2 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Massive-vector longitudinal high-energy perturbative breakdown; Massive vector transverse and longitudinal polarization basis; Massless Maxwell gauge redundancy and two modes; Proca Lagrangian and massive spin-1 constraint; Conflict between vector Lorentz covariance and positive norm. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.massive-vector-longitudinal-perturbative-breakdown`, `schwartz.massive-vector-polarization-basis`, `schwartz.massless-maxwell-gauge-redundancy-and-two-modes`, `schwartz.proca-lagrangian-and-spin-one-constraint`, `schwartz.vector-lorentz-unitarity-conflict`.

</details>

<details>
<summary>Section 8.3 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Gauge-current minimal coupling and scalar contact term; Little-group induced vector representations; Massless Maxwell gauge redundancy and two modes; Scalar-QED local U(1) Lagrangian. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-current-minimal-coupling`, `schwartz.little-group-induced-vector-representations`, `schwartz.massless-maxwell-gauge-redundancy-and-two-modes`, `schwartz.scalar-qed-local-u1-lagrangian`.

</details>

<details>
<summary>Section 8.4 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Gauge-current minimal coupling and scalar contact term; Little-group induced vector representations; Massive vector field quantization by polarization modes; Massless little-group derivation of the Ward identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-current-minimal-coupling`, `schwartz.little-group-induced-vector-representations`, `schwartz.massive-vector-field-quantization`, `schwartz.massless-little-group-ward-identity`.

</details>

<details>
<summary>Section 8.5 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Covariant Rξ photon propagator; Massless little-group derivation of the Ward identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.covariant-rxi-photon-propagator`, `schwartz.massless-little-group-ward-identity`.

</details>

<details>
<summary>Section 8.6 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Covariant Rξ photon propagator; Gauge-parameter independence from transverse contractions; Gauge redundancy, locality, and global gauge data; Stueckelberg representation of a massive vector. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.covariant-rxi-photon-propagator`, `schwartz.gauge-parameter-independence-from-transversality`, `schwartz.gauge-redundancy-locality-and-global-data`, `schwartz.stueckelberg-massive-vector-representation`.

</details>

<details>
<summary>Section 8.7 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Fierz–Pauli massive spin-2 Lagrangian; Gauge invariance from longitudinal decoupling; Gauge redundancy, locality, and global gauge data; Longitudinal decomposition and ghost test; Massless spin-2 longitudinal-decoupling route to general relativity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.fierz-pauli-massive-spin-two`, `schwartz.gauge-invariance-from-longitudinal-decoupling`, `schwartz.gauge-redundancy-locality-and-global-data`, `schwartz.longitudinal-stueckelberg-ghost-test`, `schwartz.massless-spin-two-to-general-relativity-route`.

</details>

<details>
<summary>Section 8.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Axial-gauge photon propagator problem; Massive spin-3 kinetic-action construction problem; Massive-vector propagator inversion problem; No interacting massless integer spin above two; Massless spin-2 cubic-interaction construction problem; Maxwell energy-positivity derivation problem; Positive-norm probability proof problem; Scalar four-derivative ghost proof problem; Tensor polarization-sum and degree-counting problem; Vector polarization-sum derivation problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.axial-photon-propagator-problem`, `schwartz.massive-spin-three-kinetic-action-problem`, `schwartz.massive-vector-propagator-problem`, `schwartz.massless-higher-spin-no-interaction-result`, `schwartz.massless-spin-two-cubic-interactions-problem`, `schwartz.maxwell-energy-positivity-problem`, `schwartz.positive-norm-probability-problem`, `schwartz.scalar-four-derivative-ghost-proof-problem`, `schwartz.tensor-polarization-sums-problem`, `schwartz.vector-polarization-sums-problem`.

</details>

<details>
<summary>Section 9 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Complex scalar quantization and antiparticles; External photon polarizations in LSZ rules; Scalar Møller scattering and ξ cancellation; Scalar-QED local U(1) Lagrangian; Scalar-QED internal-photon gauge-cancellation route; Scalar-QED propagators and derivative three-point vertices; Scalar-QED seagull contact vertex; Scalar-QED Ward identity from the complete tree diagram set; Soft form factor and charge definition; Soft-photon external-leg factorization; Soft massless spin-1 Lorentz invariance implies charge conservation; Soft massless spin-2 implies universal gravity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.complex-scalar-antiparticle-quantization`, `schwartz.external-photon-lsz-polarizations`, `schwartz.scalar-moller-scattering-and-xi-cancellation`, `schwartz.scalar-qed-local-u1-lagrangian`, `schwartz.scalar-qed-loop-gauge-cancellation-route`, `schwartz.scalar-qed-propagators-and-derivative-vertices`, `schwartz.scalar-qed-seagull-contact-vertex`, `schwartz.scalar-qed-ward-cancellation-complete-diagram-set`, `schwartz.soft-form-factor-charge-definition`, `schwartz.soft-photon-external-leg-factorization`, `schwartz.soft-spin-one-lorentz-implies-charge-conservation`, `schwartz.soft-spin-two-universal-gravity`.

</details>

<details>
<summary>Section 9.1 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Complex scalar quantization and antiparticles; Scalar-QED local U(1) Lagrangian. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.complex-scalar-antiparticle-quantization`, `schwartz.scalar-qed-local-u1-lagrangian`.

</details>

<details>
<summary>Section 9.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: External photon polarizations in LSZ rules; Scalar-QED propagators and derivative three-point vertices; Scalar-QED seagull contact vertex. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.external-photon-lsz-polarizations`, `schwartz.scalar-qed-propagators-and-derivative-vertices`, `schwartz.scalar-qed-seagull-contact-vertex`.

</details>

<details>
<summary>Section 9.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: External photon polarizations in LSZ rules; Scalar Møller scattering and ξ cancellation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.external-photon-lsz-polarizations`, `schwartz.scalar-moller-scattering-and-xi-cancellation`.

</details>

<details>
<summary>Section 9.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Scalar Møller scattering and ξ cancellation; Scalar-QED internal-photon gauge-cancellation route; Scalar-QED Ward identity from the complete tree diagram set. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scalar-moller-scattering-and-xi-cancellation`, `schwartz.scalar-qed-loop-gauge-cancellation-route`, `schwartz.scalar-qed-ward-cancellation-complete-diagram-set`.

</details>

<details>
<summary>Section 9.5 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Scalar-QED internal-photon gauge-cancellation route; Soft form factor and charge definition; Soft-photon external-leg factorization; Soft massless spin-1 Lorentz invariance implies charge conservation; Soft massless spin-2 implies universal gravity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scalar-qed-loop-gauge-cancellation-route`, `schwartz.soft-form-factor-charge-definition`, `schwartz.soft-photon-external-leg-factorization`, `schwartz.soft-spin-one-lorentz-implies-charge-conservation`, `schwartz.soft-spin-two-universal-gravity`.

</details>

<details>
<summary>Section 9.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Light-by-light gauge-invariant diagram-set problem; Non-Abelian soft-consistency derivation problem; Scalar-QED Compton scattering problem; Soft-graviton self-interaction derivation problem; Soft-limit derivation of the massless higher-spin obstruction. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.light-by-light-gauge-set-problem`, `schwartz.nonabelian-soft-consistency-problem`, `schwartz.scalar-qed-compton-scattering-problem`, `schwartz.soft-graviton-self-interaction-problem`, `schwartz.soft-spin-greater-than-two-obstruction`.

</details>

<details>
<summary>Section 10 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Dirac adjoint and covariant spinor bilinears; Dirac Clifford algebra and spinor Lorentz generators; Dirac equation factorizes the Klein–Gordon equation; Dirac magnetic-dipole prediction; Dirac number current and charge density; Minimal photon coupling and the spin Pauli term; Dirac spinor, Lagrangian, and equation; Nonunitarity of finite-dimensional Lorentz spinor representations; Groups, representations, and Lorentz components; Lorentz algebra as two commuting su(2) factors; (A,B) Lorentz irreps and their rotation content; Lorentz Lie algebra from rotation and boost generators; Majorana mass and Grassmann necessity; Massless Weyl equation and the mass-term obstruction; Pauli spinor and Schrödinger–Pauli dynamics; 2π spinor sign and projective Lorentz representation; Weyl index, epsilon, and sigma-matrix conventions; Weyl kinetic terms and Lorentz-invariant Dirac mass; Left- and right-handed Weyl representations. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-adjoint-and-covariant-bilinears`, `schwartz.dirac-clifford-algebra-and-spin-generators`, `schwartz.dirac-equation-klein-gordon-factorization`, `schwartz.dirac-magnetic-dipole-prediction`, `schwartz.dirac-noether-number-current`, `schwartz.dirac-photon-coupling-and-pauli-term`, `schwartz.dirac-spinor-lagrangian-and-equation`, `schwartz.finite-spinor-lorentz-nonunitarity`, `schwartz.groups-representations-and-lorentz-components`, `schwartz.lorentz-algebra-two-su2-factors`, `schwartz.lorentz-irrep-labels-and-rotation-content`, `schwartz.lorentz-lie-algebra-generators`, `schwartz.majorana-mass-grassmann-necessity`, `schwartz.massless-weyl-equation-and-mass-obstruction`, `schwartz.pauli-spinor-and-schrodinger-pauli-equation`, `schwartz.spinor-two-pi-rotation-and-projective-representations`, `schwartz.weyl-index-and-sigma-conventions`, `schwartz.weyl-kinetic-terms-and-dirac-mass`, `schwartz.weyl-spinor-lorentz-representations`.

</details>

<details>
<summary>Section 10.1 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Groups, representations, and Lorentz components; Lorentz algebra as two commuting su(2) factors; (A,B) Lorentz irreps and their rotation content; Lorentz Lie algebra from rotation and boost generators; Massless Weyl equation and the mass-term obstruction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.groups-representations-and-lorentz-components`, `schwartz.lorentz-algebra-two-su2-factors`, `schwartz.lorentz-irrep-labels-and-rotation-content`, `schwartz.lorentz-lie-algebra-generators`, `schwartz.massless-weyl-equation-and-mass-obstruction`.

</details>

<details>
<summary>Section 10.2 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Dirac spinor, Lagrangian, and equation; Nonunitarity of finite-dimensional Lorentz spinor representations; (A,B) Lorentz irreps and their rotation content; Weyl kinetic terms and Lorentz-invariant Dirac mass; Left- and right-handed Weyl representations. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-spinor-lagrangian-and-equation`, `schwartz.finite-spinor-lorentz-nonunitarity`, `schwartz.lorentz-irrep-labels-and-rotation-content`, `schwartz.weyl-kinetic-terms-and-dirac-mass`, `schwartz.weyl-spinor-lorentz-representations`.

</details>

<details>
<summary>Section 10.3 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Dirac adjoint and covariant spinor bilinears; Dirac Clifford algebra and spinor Lorentz generators; Dirac equation factorizes the Klein–Gordon equation; Dirac spinor, Lagrangian, and equation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-adjoint-and-covariant-bilinears`, `schwartz.dirac-clifford-algebra-and-spin-generators`, `schwartz.dirac-equation-klein-gordon-factorization`, `schwartz.dirac-spinor-lagrangian-and-equation`.

</details>

<details>
<summary>Section 10.4 — covered</summary>

The accepted result records substantively represent this section's distinct content: Minimal photon coupling and the spin Pauli term. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-photon-coupling-and-pauli-term`.

</details>

<details>
<summary>Section 10.5 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Dirac magnetic-dipole prediction; Dirac number current and charge density; 2π spinor sign and projective Lorentz representation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-magnetic-dipole-prediction`, `schwartz.dirac-noether-number-current`, `schwartz.spinor-two-pi-rotation-and-projective-representations`.

</details>

<details>
<summary>Section 10.6 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Majorana mass and Grassmann necessity; 2π spinor sign and projective Lorentz representation; Weyl index, epsilon, and sigma-matrix conventions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.majorana-mass-grassmann-necessity`, `schwartz.spinor-two-pi-rotation-and-projective-representations`, `schwartz.weyl-index-and-sigma-conventions`.

</details>

<details>
<summary>Section 10.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Majorana-representation algebra problem; Nonrelativistic Dirac magnetic and spin–orbit derivation problem; Finite-dimensional SU(2) irrep construction problem; Supersymmetry and auxiliary-field elimination problem; Weyl index, epsilon, and sigma-matrix conventions; Weyl sigma-identity derivation problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.majorana-representation-problem`, `schwartz.nonrelativistic-dirac-magnetic-and-spin-orbit-problem`, `schwartz.su2-finite-irrep-construction-problem`, `schwartz.supersymmetry-auxiliary-field-problem`, `schwartz.weyl-index-and-sigma-conventions`, `schwartz.weyl-sigma-identity-problem`.

</details>

<details>
<summary>Section 11 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Charge conjugation in QED and for bilinears; Charge-conjugation transformation of a Dirac spinor; Chirality, helicity, and spin distinction; CP T-hat transformation calculation; Dirac spinor normalization and completeness sums; Free Dirac particle and antiparticle solutions; Majorana charge conjugacy and U(1) neutrality; Parity phases and spinor chirality swap; Simple T-hat field conjugation; Vector and axial currents under parity; Wigner time reversal as an anti-linear symmetry. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.charge-conjugation-qed-and-bilinears`, `schwartz.charge-conjugation-spinor-transformation`, `schwartz.chirality-helicity-and-spin-distinction`, `schwartz.cp-simple-time-reversal-calculation`, `schwartz.dirac-spinor-normalization-and-completeness`, `schwartz.free-dirac-particle-antiparticle-solutions`, `schwartz.majorana-charge-conjugacy-and-u1-neutrality`, `schwartz.parity-intrinsic-phases-and-spinor-chirality-swap`, `schwartz.simple-time-reversal-field-conjugation`, `schwartz.vector-and-axial-currents-under-parity`, `schwartz.wigner-time-reversal-antilinearity`.

</details>

<details>
<summary>Section 11.1 — covered</summary>

The accepted concept records substantively represent this section's distinct content: Chirality, helicity, and spin distinction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chirality-helicity-and-spin-distinction`.

</details>

<details>
<summary>Section 11.2 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Chirality, helicity, and spin distinction; Dirac spinor normalization and completeness sums; Free Dirac particle and antiparticle solutions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chirality-helicity-and-spin-distinction`, `schwartz.dirac-spinor-normalization-and-completeness`, `schwartz.free-dirac-particle-antiparticle-solutions`.

</details>

<details>
<summary>Section 11.3 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Charge-conjugation transformation of a Dirac spinor; Majorana charge conjugacy and U(1) neutrality. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.charge-conjugation-spinor-transformation`, `schwartz.majorana-charge-conjugacy-and-u1-neutrality`.

</details>

<details>
<summary>Section 11.4 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Charge conjugation in QED and for bilinears; Charge-conjugation transformation of a Dirac spinor; Majorana charge conjugacy and U(1) neutrality. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.charge-conjugation-qed-and-bilinears`, `schwartz.charge-conjugation-spinor-transformation`, `schwartz.majorana-charge-conjugacy-and-u1-neutrality`.

</details>

<details>
<summary>Section 11.5 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Charge conjugation in QED and for bilinears; Parity phases and spinor chirality swap; Vector and axial currents under parity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.charge-conjugation-qed-and-bilinears`, `schwartz.parity-intrinsic-phases-and-spinor-chirality-swap`, `schwartz.vector-and-axial-currents-under-parity`.

</details>

<details>
<summary>Section 11.6 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: CP T-hat transformation calculation; Simple T-hat field conjugation; Vector and axial currents under parity; Wigner time reversal as an anti-linear symmetry. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cp-simple-time-reversal-calculation`, `schwartz.simple-time-reversal-field-conjugation`, `schwartz.vector-and-axial-currents-under-parity`, `schwartz.wigner-time-reversal-antilinearity`.

</details>

<details>
<summary>Section 11.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Beta-decay electron-polarization problem; Charge-conjugation bilinear derivation problem; Chiral-QED selection and helicity-reversal problem; CPT theorem scope; Magnetic/electric dipole discrete-symmetry problem; Dirac-algebra identity derivation problem; Fierz rearrangement derivation problem; General local Dirac/photon CPT-invariance problem; On-shell Gordon-identity problem; Massless spin-one charge-conservation proof problem; Neutrino Majorana U(1)-obstruction problem; Neutrino mass-eigenstate and see-saw problem; Neutrinoless double-beta lepton-flow problem; Nonrelativistic spin-flip and measurement problem; Rest-spinor current-selection problem; Spinor completeness and current-identity problem; Wigner-CPT transformation calculation; Wigner time reversal as an anti-linear symmetry. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.beta-decay-electron-polarization-problem`, `schwartz.charge-conjugation-bilinear-problem`, `schwartz.chiral-qed-and-helicity-problem`, `schwartz.cpt-theorem-scope`, `schwartz.dipole-operator-discrete-symmetry-problem`, `schwartz.dirac-algebra-identities-problem`, `schwartz.fierz-rearrangement-problem`, `schwartz.general-local-cpt-invariance-problem`, `schwartz.gordon-identity-problem`, `schwartz.massless-spin-one-charge-conservation-problem`, `schwartz.neutrino-majorana-u1-obstruction-problem`, `schwartz.neutrino-mass-eigenstate-and-seesaw-problem`, `schwartz.neutrinoless-double-beta-lepton-flow-problem`, `schwartz.nonrelativistic-spin-flip-and-measurement-problem`, `schwartz.rest-spinor-current-problem`, `schwartz.spinor-completeness-and-current-problem`, `schwartz.wigner-cpt-transformation-calculation`, `schwartz.wigner-time-reversal-antilinearity`.

</details>

<details>
<summary>Section 12 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Dirac propagator requires fermionic ordering; Exchange-path route to spin–statistics; Exchange-path topology in 3+1 and 2+1 dimensions; Fermionic time ordering; General-spin derivative-count route to statistics; Higher-spin causality route and its limitation; Identical-particle exchange algebra and Pauli exclusion; Quantized Dirac field mode expansion; S-matrix Lorentz-invariance route to spin–statistics; Scalar microcausality and the Pauli–Jordan distribution; Scalar Feynman propagator requires bosonic ordering; Spin–statistics theorem; Spinor microcausality from anticommutators; Stability route to all-spin statistics; Statistics from lower-bounded free-field energy. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-propagator-requires-fermionic-ordering`, `schwartz.exchange-path-spin-statistics-route`, `schwartz.exchange-path-topology-and-anyons`, `schwartz.fermionic-time-ordering`, `schwartz.general-spin-kinetic-derivative-statistics-route`, `schwartz.higher-spin-causality-statistics-and-limitation`, `schwartz.identical-particle-exchange-and-pauli-exclusion`, `schwartz.quantized-dirac-field-mode-expansion`, `schwartz.s-matrix-lorentz-spin-statistics-route`, `schwartz.scalar-microcausality-pauli-jordan-function`, `schwartz.scalar-propagator-requires-bosonic-ordering`, `schwartz.spin-statistics-theorem`, `schwartz.spinor-microcausality-anticommutator`, `schwartz.stability-general-spin-statistics-route`, `schwartz.statistics-and-energy-stability`.

</details>

<details>
<summary>Section 12.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Exchange-path route to spin–statistics; Identical-particle exchange algebra and Pauli exclusion; Spin–statistics theorem. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.exchange-path-spin-statistics-route`, `schwartz.identical-particle-exchange-and-pauli-exclusion`, `schwartz.spin-statistics-theorem`.

</details>

<details>
<summary>Section 12.2 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Exchange-path route to spin–statistics; Exchange-path topology in 3+1 and 2+1 dimensions; Identical-particle exchange algebra and Pauli exclusion. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.exchange-path-spin-statistics-route`, `schwartz.exchange-path-topology-and-anyons`, `schwartz.identical-particle-exchange-and-pauli-exclusion`.

</details>

<details>
<summary>Section 12.3 — covered</summary>

The accepted concept, representation records substantively represent this section's distinct content: Exchange-path topology in 3+1 and 2+1 dimensions; Quantized Dirac field mode expansion. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.exchange-path-topology-and-anyons`, `schwartz.quantized-dirac-field-mode-expansion`.

</details>

<details>
<summary>Section 12.4 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Dirac propagator requires fermionic ordering; Fermionic time ordering; Quantized Dirac field mode expansion; S-matrix Lorentz-invariance route to spin–statistics; Scalar Feynman propagator requires bosonic ordering. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-propagator-requires-fermionic-ordering`, `schwartz.fermionic-time-ordering`, `schwartz.quantized-dirac-field-mode-expansion`, `schwartz.s-matrix-lorentz-spin-statistics-route`, `schwartz.scalar-propagator-requires-bosonic-ordering`.

</details>

<details>
<summary>Section 12.5 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Dirac propagator requires fermionic ordering; General-spin derivative-count route to statistics; S-matrix Lorentz-invariance route to spin–statistics; Stability route to all-spin statistics; Statistics from lower-bounded free-field energy. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dirac-propagator-requires-fermionic-ordering`, `schwartz.general-spin-kinetic-derivative-statistics-route`, `schwartz.s-matrix-lorentz-spin-statistics-route`, `schwartz.stability-general-spin-statistics-route`, `schwartz.statistics-and-energy-stability`.

</details>

<details>
<summary>Section 12.6 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: General-spin derivative-count route to statistics; Higher-spin causality route and its limitation; Scalar microcausality and the Pauli–Jordan distribution; Spinor microcausality from anticommutators; Stability route to all-spin statistics. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.general-spin-kinetic-derivative-statistics-route`, `schwartz.higher-spin-causality-statistics-and-limitation`, `schwartz.scalar-microcausality-pauli-jordan-function`, `schwartz.spinor-microcausality-anticommutator`, `schwartz.stability-general-spin-statistics-route`.

</details>

<details>
<summary>Section 12.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Higher-spin causality route and its limitation; Spinor-bilinear causality problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.higher-spin-causality-statistics-and-limitation`, `schwartz.spinor-bilinear-causality-problem`.

</details>

<details>
<summary>Section 13 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Compton backscattering pole softening; Massless Compton helicity selection; QED Compton two-diagram amplitude; Unpolarized Compton squared amplitude; Tree e⁺e⁻→μ⁺μ⁻ amplitude and longitudinal cancellation; Center-of-mass e⁺e⁻→μ⁺μ⁻ cross section; Unpolarized e⁺e⁻→μ⁺μ⁻ squared amplitude; Gamma-matrix trace identities; Klein–Nishina Compton cross section; Mott formula and Rutherford limits; Physical photon polarization sum; Fermion exchange and loop signs in QED; QED fermion-line and loop evaluation; Higher-order QED divergences and renormalization motivation; QED momentum-space Feynman rules; Crossing method for QED Rutherford scattering. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.compton-backscattering-pole`, `schwartz.compton-helicity-selection`, `schwartz.compton-qed-two-diagram-amplitude`, `schwartz.compton-unpolarized-squared-amplitude`, `schwartz.electron-positron-to-muon-amplitude`, `schwartz.electron-positron-to-muon-cm-cross-section`, `schwartz.electron-positron-to-muon-unpolarized-rate`, `schwartz.gamma-trace-identities`, `schwartz.klein-nishina-cross-section`, `schwartz.mott-and-rutherford-limits`, `schwartz.physical-photon-polarization-sum`, `schwartz.qed-fermion-exchange-and-loop-signs`, `schwartz.qed-fermion-line-and-loop-evaluation`, `schwartz.qed-higher-order-divergence-and-renormalization-motivation`, `schwartz.qed-momentum-space-feynman-rules`, `schwartz.qed-rutherford-crossing-method`.

</details>

<details>
<summary>Section 13.1 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Fermion exchange and loop signs in QED; QED fermion-line and loop evaluation; QED momentum-space Feynman rules. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-fermion-exchange-and-loop-signs`, `schwartz.qed-fermion-line-and-loop-evaluation`, `schwartz.qed-momentum-space-feynman-rules`.

</details>

<details>
<summary>Section 13.2 — covered</summary>

The accepted result records substantively represent this section's distinct content: Gamma-matrix trace identities; Fermion exchange and loop signs in QED. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gamma-trace-identities`, `schwartz.qed-fermion-exchange-and-loop-signs`.

</details>

<details>
<summary>Section 13.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Tree e⁺e⁻→μ⁺μ⁻ amplitude and longitudinal cancellation; Center-of-mass e⁺e⁻→μ⁺μ⁻ cross section; Unpolarized e⁺e⁻→μ⁺μ⁻ squared amplitude; Gamma-matrix trace identities. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-positron-to-muon-amplitude`, `schwartz.electron-positron-to-muon-cm-cross-section`, `schwartz.electron-positron-to-muon-unpolarized-rate`, `schwartz.gamma-trace-identities`.

</details>

<details>
<summary>Section 13.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Center-of-mass e⁺e⁻→μ⁺μ⁻ cross section; Mott formula and Rutherford limits; Crossing method for QED Rutherford scattering. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-positron-to-muon-cm-cross-section`, `schwartz.mott-and-rutherford-limits`, `schwartz.qed-rutherford-crossing-method`.

</details>

<details>
<summary>Section 13.5 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Compton backscattering pole softening; Massless Compton helicity selection; QED Compton two-diagram amplitude; Unpolarized Compton squared amplitude; Klein–Nishina Compton cross section; Mott formula and Rutherford limits; Physical photon polarization sum. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.compton-backscattering-pole`, `schwartz.compton-helicity-selection`, `schwartz.compton-qed-two-diagram-amplitude`, `schwartz.compton-unpolarized-squared-amplitude`, `schwartz.klein-nishina-cross-section`, `schwartz.mott-and-rutherford-limits`, `schwartz.physical-photon-polarization-sum`.

</details>

<details>
<summary>Section 13.6 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Compton backscattering pole softening; Massless Compton helicity selection; Higher-order QED divergences and renormalization motivation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.compton-backscattering-pole`, `schwartz.compton-helicity-selection`, `schwartz.qed-higher-order-divergence-and-renormalization-motivation`.

</details>

<details>
<summary>Section 13.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Beta-decay handedness and operational-parity problem; QED Compton polarization-sum consistency problem; Decay phase space and spin-parity diagnosis problem; Fermion-loop sign proof problem; Gauge-complete diagram set problem; Relativistic Møller cross-section problem; Z energy-scaling, angular-distribution, and chiral-coupling problem; QED target-rest Rutherford derivation problem; Scalar-QED polarization-sum consistency problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.beta-decay-handedness-and-operational-parity-problem`, `schwartz.compton-qed-polarization-sum-problem`, `schwartz.decay-spin-parity-diagnosis-problem`, `schwartz.fermion-loop-sign-proof-problem`, `schwartz.gauge-complete-diagram-set-problem`, `schwartz.moller-relativistic-cross-section-problem`, `schwartz.parity-violation-and-chiral-z-problem`, `schwartz.qed-rutherford-target-rest-problem`, `schwartz.scalar-qed-polarization-sum-problem`.

</details>

<details>
<summary>Section 14 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Abelian gauge-orbit factorization assumptions; Canonical/path-integral equivalence by Schwinger–Dyson equations; Fermionic generating functional and Dirac propagator; Historical validation of Feynman’s path-integral rules; Field-configuration and momentum eigenstates; Field-theory path integral from the Hamiltonian; Free four-point pairing derivation; Free real-scalar generating functional; ξ independence of gauge-invariant correlators; Global-symmetry Ward contact derivation; Grassmann algebra and grading; Grassmann Gaussian determinant; Grassmann integration and shift method; Interacting path-integral mathematical existence status; Interacting path-integral perturbation series; Multivariable Gaussian integral method; Path-integral and canonical formulation tradeoffs; Classical stationary-phase limit of the path integral; Path-integral representation of time-ordered correlators; Gauge-orbit factorization by field redefinition; Path-integral derivation of Schwinger–Dyson contact terms; Time ordering from path-integral insertions; QED Ward identity from LSZ and contact terms; Quantum-mechanical path-integral derivation; Reflection positivity for the iε prescription; S-matrix boundary origin of the iε prescription; Schwinger–Dyson functional differential equation; Generating-functional uniqueness and boundary-condition assumption; Source generating functional for correlators; Sum-over-histories and Huygens intuition; Momentum-space Ward–Takahashi identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-gauge-orbit-factorization-assumptions`, `schwartz.canonical-path-integral-equivalence-by-schwinger-dyson`, `schwartz.fermionic-generating-functional-and-dirac-propagator`, `schwartz.feynman-path-integral-historical-validation`, `schwartz.field-configuration-and-momentum-eigenstates`, `schwartz.field-theory-path-integral-from-hamiltonian`, `schwartz.free-four-point-pairing-derivation`, `schwartz.free-scalar-generating-functional`, `schwartz.gauge-invariant-correlator-xi-independence`, `schwartz.global-symmetry-ward-contact-method`, `schwartz.grassmann-algebra-and-grading`, `schwartz.grassmann-gaussian-determinant`, `schwartz.grassmann-integration-and-shift-method`, `schwartz.interacting-path-integral-existence-status`, `schwartz.interacting-path-integral-perturbation-series`, `schwartz.multivariable-gaussian-integral-method`, `schwartz.path-integral-canonical-formulation-tradeoffs`, `schwartz.path-integral-classical-stationary-phase-limit`, `schwartz.path-integral-correlator-representation`, `schwartz.path-integral-gauge-orbit-factorization`, `schwartz.path-integral-schwinger-dyson-contact-derivation`, `schwartz.path-integral-time-ordering-result`, `schwartz.qed-ward-identity-from-lsz-and-contact-terms`, `schwartz.quantum-mechanical-path-integral-derivation`, `schwartz.reflection-positivity-for-iepsilon`, `schwartz.s-matrix-boundary-origin-of-iepsilon`, `schwartz.schwinger-dyson-functional-differential-equation`, `schwartz.schwinger-dyson-functional-uniqueness-assumption`, `schwartz.source-generating-functional-method`, `schwartz.sum-over-histories-and-huygens-intuition`, `schwartz.ward-takahashi-momentum-identity`.

</details>

<details>
<summary>Section 14.1 — covered</summary>

The accepted concept, representation records substantively represent this section's distinct content: Historical validation of Feynman’s path-integral rules; Path-integral and canonical formulation tradeoffs; Path-integral representation of time-ordered correlators; Sum-over-histories and Huygens intuition. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.feynman-path-integral-historical-validation`, `schwartz.path-integral-canonical-formulation-tradeoffs`, `schwartz.path-integral-correlator-representation`, `schwartz.sum-over-histories-and-huygens-intuition`.

</details>

<details>
<summary>Section 14.2 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Historical validation of Feynman’s path-integral rules; Field-configuration and momentum eigenstates; Field-theory path integral from the Hamiltonian; Multivariable Gaussian integral method; Classical stationary-phase limit of the path integral; Time ordering from path-integral insertions; Quantum-mechanical path-integral derivation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.feynman-path-integral-historical-validation`, `schwartz.field-configuration-and-momentum-eigenstates`, `schwartz.field-theory-path-integral-from-hamiltonian`, `schwartz.multivariable-gaussian-integral-method`, `schwartz.path-integral-classical-stationary-phase-limit`, `schwartz.path-integral-time-ordering-result`, `schwartz.quantum-mechanical-path-integral-derivation`.

</details>

<details>
<summary>Section 14.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Free four-point pairing derivation; Free real-scalar generating functional; Time ordering from path-integral insertions; Source generating functional for correlators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.free-four-point-pairing-derivation`, `schwartz.free-scalar-generating-functional`, `schwartz.path-integral-time-ordering-result`, `schwartz.source-generating-functional-method`.

</details>

<details>
<summary>Section 14.4 — covered</summary>

The accepted assumption, method records substantively represent this section's distinct content: Interacting path-integral perturbation series; Reflection positivity for the iε prescription; S-matrix boundary origin of the iε prescription. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.interacting-path-integral-perturbation-series`, `schwartz.reflection-positivity-for-iepsilon`, `schwartz.s-matrix-boundary-origin-of-iepsilon`.

</details>

<details>
<summary>Section 14.5 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Abelian gauge-orbit factorization assumptions; ξ independence of gauge-invariant correlators; Interacting path-integral mathematical existence status; Gauge-orbit factorization by field redefinition; Reflection positivity for the iε prescription. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-gauge-orbit-factorization-assumptions`, `schwartz.gauge-invariant-correlator-xi-independence`, `schwartz.interacting-path-integral-existence-status`, `schwartz.path-integral-gauge-orbit-factorization`, `schwartz.reflection-positivity-for-iepsilon`.

</details>

<details>
<summary>Section 14.6 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: ξ independence of gauge-invariant correlators; Grassmann algebra and grading; Grassmann Gaussian determinant; Grassmann integration and shift method; Gauge-orbit factorization by field redefinition. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-invariant-correlator-xi-independence`, `schwartz.grassmann-algebra-and-grading`, `schwartz.grassmann-gaussian-determinant`, `schwartz.grassmann-integration-and-shift-method`, `schwartz.path-integral-gauge-orbit-factorization`.

</details>

<details>
<summary>Section 14.7 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Canonical/path-integral equivalence by Schwinger–Dyson equations; Fermionic generating functional and Dirac propagator; Grassmann Gaussian determinant; Path-integral derivation of Schwinger–Dyson contact terms; Schwinger–Dyson functional differential equation; Generating-functional uniqueness and boundary-condition assumption. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.canonical-path-integral-equivalence-by-schwinger-dyson`, `schwartz.fermionic-generating-functional-and-dirac-propagator`, `schwartz.grassmann-gaussian-determinant`, `schwartz.path-integral-schwinger-dyson-contact-derivation`, `schwartz.schwinger-dyson-functional-differential-equation`, `schwartz.schwinger-dyson-functional-uniqueness-assumption`.

</details>

<details>
<summary>Section 14.8 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Canonical/path-integral equivalence by Schwinger–Dyson equations; Global-symmetry Ward contact derivation; QED Ward identity from LSZ and contact terms; Momentum-space Ward–Takahashi identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.canonical-path-integral-equivalence-by-schwinger-dyson`, `schwartz.global-symmetry-ward-contact-method`, `schwartz.qed-ward-identity-from-lsz-and-contact-terms`, `schwartz.ward-takahashi-momentum-identity`.

</details>

<details>
<summary>Section 14.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Complex-scalar Gaussian functional problem; Dirac canonical Schwinger–Dyson verification problem; Dirac path-integral Schwinger–Dyson verification problem; Field-eigenstate measure construction problem; Gauge-deformation consistency problem; Grassmann interaction nonvanishing problem; QED S-matrix ξ independence from the Ward identity; Scalar-QED Furry’s theorem problem; Scalar-QED Schwinger-terms problem; Spinor-QED Furry’s theorem problem; Free-field vacuum wavefunctional problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.complex-scalar-gaussian-functional-problem`, `schwartz.dirac-canonical-schwinger-dyson-verification-problem`, `schwartz.dirac-path-integral-schwinger-dyson-verification-problem`, `schwartz.field-eigenstate-measure-problem`, `schwartz.gauge-deformation-consistency-problem`, `schwartz.grassmann-interaction-nonvanishing-problem`, `schwartz.qed-s-matrix-xi-independence-from-ward-identity`, `schwartz.scalar-qed-furrys-theorem-problem`, `schwartz.scalar-qed-schwinger-terms-problem`, `schwartz.spinor-qed-furrys-theorem-problem`, `schwartz.vacuum-wavefunctional-problem`.

</details>

<details>
<summary>Section 15 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Hard-cutoff averaging for the Casimir force; Regulated integer sum for string zero-point energy; Discrete Casimir mode sum and regulator setup; Regulator-independent Casimir force; Bare-coupling inversion route for scalar scattering; Finite scalar four-point reference-scale prediction; Scalar four-point s-channel loop evaluation; String Casimir energy and critical dimensions; Vacuum-energy-density counterterm. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.casimir-hard-cutoff-averaging-method`, `schwartz.casimir-regulated-integer-sum-result`, `schwartz.casimir-regulated-mode-sum-setup`, `schwartz.casimir-regulator-independent-force`, `schwartz.scalar-four-point-bare-coupling-inversion-route`, `schwartz.scalar-four-point-finite-reference-scale-amplitude`, `schwartz.scalar-four-point-loop-renormalization`, `schwartz.string-casimir-critical-dimension-result`, `schwartz.vacuum-energy-density-counterterm`.

</details>

<details>
<summary>Section 15.1 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Hard-cutoff averaging for the Casimir force; Discrete Casimir mode sum and regulator setup. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.casimir-hard-cutoff-averaging-method`, `schwartz.casimir-regulated-mode-sum-setup`.

</details>

<details>
<summary>Section 15.2 — covered</summary>

The accepted method records substantively represent this section's distinct content: Hard-cutoff averaging for the Casimir force. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.casimir-hard-cutoff-averaging-method`.

</details>

<details>
<summary>Section 15.3 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Hard-cutoff averaging for the Casimir force; Discrete Casimir mode sum and regulator setup; Regulator-independent Casimir force; Vacuum-energy-density counterterm. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.casimir-hard-cutoff-averaging-method`, `schwartz.casimir-regulated-mode-sum-setup`, `schwartz.casimir-regulator-independent-force`, `schwartz.vacuum-energy-density-counterterm`.

</details>

<details>
<summary>Section 15.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Regulated integer sum for string zero-point energy; Bare-coupling inversion route for scalar scattering; Finite scalar four-point reference-scale prediction; Scalar four-point s-channel loop evaluation; String Casimir energy and critical dimensions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.casimir-regulated-integer-sum-result`, `schwartz.scalar-four-point-bare-coupling-inversion-route`, `schwartz.scalar-four-point-finite-reference-scale-amplitude`, `schwartz.scalar-four-point-loop-renormalization`, `schwartz.string-casimir-critical-dimension-result`.

</details>

<details>
<summary>Section 15.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Fermionic Casimir-sign problem; Gaussian-regulator Casimir-force problem; Casimir-gecko dimensional-analysis problem; Massive-field Casimir-force problem; Scalar φ⁴ counterterm perturbation route; Finite scalar four-point reference-scale prediction. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.casimir-fermion-statistics-sign-problem`, `schwartz.casimir-gaussian-regulator-problem`, `schwartz.casimir-gecko-dimensional-analysis-problem`, `schwartz.casimir-massive-field-problem`, `schwartz.scalar-four-point-counterterm-perturbation`, `schwartz.scalar-four-point-finite-reference-scale-amplitude`.

</details>

<details>
<summary>Section 16 — covered</summary>

The accepted assumption, concept, method, result records substantively represent this section's distinct content: Gauge-preserving dimensional-regularization assumption; QED charge renormalization from the Coulomb potential; QED effective charge, screening, and Landau pole; Observable-based QED renormalization principle; QED running charge and one-loop beta function; One-renormalization-condition-per-parameter rule; Scalar bubble loop and UV–IR scale separation; Scalar-QED vacuum-polarization transversality; Spinor-QED vacuum-polarization loop; Uehling potential and S-state Lamb-shift contribution. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-preserving-dimensional-regularization-assumption`, `schwartz.qed-charge-renormalization-from-coulomb-potential`, `schwartz.qed-effective-charge-and-landau-pole`, `schwartz.qed-renormalized-observable-principle`, `schwartz.qed-running-charge-beta-function`, `schwartz.scalar-bubble-renormalization-condition`, `schwartz.scalar-bubble-scale-separation-method`, `schwartz.scalar-qed-vacuum-polarization-transverse-result`, `schwartz.spinor-qed-vacuum-polarization-result`, `schwartz.uehling-potential-and-lamb-shift`.

</details>

<details>
<summary>Section 16.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: One-renormalization-condition-per-parameter rule; Scalar bubble loop and UV–IR scale separation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scalar-bubble-renormalization-condition`, `schwartz.scalar-bubble-scale-separation-method`.

</details>

<details>
<summary>Section 16.2 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: Gauge-preserving dimensional-regularization assumption; One-renormalization-condition-per-parameter rule; Scalar-QED vacuum-polarization transversality; Spinor-QED vacuum-polarization loop. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-preserving-dimensional-regularization-assumption`, `schwartz.scalar-bubble-renormalization-condition`, `schwartz.scalar-qed-vacuum-polarization-transverse-result`, `schwartz.spinor-qed-vacuum-polarization-result`.

</details>

<details>
<summary>Section 16.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: QED charge renormalization from the Coulomb potential; QED effective charge, screening, and Landau pole; QED running charge and one-loop beta function; Spinor-QED vacuum-polarization loop; Uehling potential and S-state Lamb-shift contribution. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-charge-renormalization-from-coulomb-potential`, `schwartz.qed-effective-charge-and-landau-pole`, `schwartz.qed-running-charge-beta-function`, `schwartz.spinor-qed-vacuum-polarization-result`, `schwartz.uehling-potential-and-lamb-shift`.

</details>

<details>
<summary>Section 16.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: QED running charge and one-loop beta function; Standard-Model-content Landau-pole problem; Tau-loop threshold and optical-theorem problem; Uehling-potential Fourier-transform problem; Vacuum-polarization tensor-completion problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.qed-running-charge-beta-function`, `schwartz.standard-model-landau-pole-problem`, `schwartz.tau-loop-threshold-optical-theorem-problem`, `schwartz.uehling-fourier-transform-problem`, `schwartz.vacuum-polarization-tensor-completion-problem`.

</details>

<details>
<summary>Section 17 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: On-shell QED vertex form factors; On-shell Gordon identity; One-loop anomalous magnetic moment calculation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.on-shell-vertex-form-factor-decomposition`, `schwartz.onshell-gordon-identity-result`, `schwartz.schwinger-anomalous-magnetic-moment-method`.

</details>

<details>
<summary>Section 17.1 — covered</summary>

The accepted result records substantively represent this section's distinct content: On-shell QED vertex form factors; On-shell Gordon identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.on-shell-vertex-form-factor-decomposition`, `schwartz.onshell-gordon-identity-result`.

</details>

<details>
<summary>Section 17.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: On-shell QED vertex form factors; One-loop anomalous magnetic moment calculation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.on-shell-vertex-form-factor-decomposition`, `schwartz.schwinger-anomalous-magnetic-moment-method`.

</details>

<details>
<summary>Section 17.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Supersymmetric muon magnetic-moment bound problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.supersymmetric-muon-magnetic-moment-problem`.

</details>

<details>
<summary>Section 18 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Electron pole mass and on-shell subtraction; Electron self-energy loop and its two UV structures; Fermion propagator from 1PI self-energies; Fermion mass and field-strength renormalization; Green functions, 1PI subgraphs, and UV-finiteness framework; Minimal-subtraction mass and subtraction scale; QED vacuum expectation values and tadpoles; Renormalized LSZ external-line amputation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-pole-mass-onshell-conditions`, `schwartz.electron-self-energy-loop-result`, `schwartz.fermion-1pi-propagator-resummation`, `schwartz.fermion-mass-and-field-renormalization`, `schwartz.green-functions-1pi-uv-finiteness-framework`, `schwartz.minimal-subtraction-mass-and-scale`, `schwartz.qed-vacuum-expectation-values`, `schwartz.renormalized-lsz-external-amputation`.

</details>

<details>
<summary>Section 18.1 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Green functions, 1PI subgraphs, and UV-finiteness framework; QED vacuum expectation values and tadpoles. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.green-functions-1pi-uv-finiteness-framework`, `schwartz.qed-vacuum-expectation-values`.

</details>

<details>
<summary>Section 18.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Electron pole mass and on-shell subtraction; Electron self-energy loop and its two UV structures; Fermion mass and field-strength renormalization; Minimal-subtraction mass and subtraction scale; QED vacuum expectation values and tadpoles. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-pole-mass-onshell-conditions`, `schwartz.electron-self-energy-loop-result`, `schwartz.fermion-mass-and-field-renormalization`, `schwartz.minimal-subtraction-mass-and-scale`, `schwartz.qed-vacuum-expectation-values`.

</details>

<details>
<summary>Section 18.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Electron pole mass and on-shell subtraction; Fermion propagator from 1PI self-energies; Renormalized LSZ external-line amputation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-pole-mass-onshell-conditions`, `schwartz.fermion-1pi-propagator-resummation`, `schwartz.renormalized-lsz-external-amputation`.

</details>

<details>
<summary>Section 18.4 — covered</summary>

The accepted method records substantively represent this section's distinct content: Renormalized LSZ external-line amputation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.renormalized-lsz-external-amputation`.

</details>

<details>
<summary>Section 18.5 — covered</summary>

The accepted result records substantively represent this section's distinct content: Electron pole mass and on-shell subtraction; Minimal-subtraction mass and subtraction scale. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electron-pole-mass-onshell-conditions`, `schwartz.minimal-subtraction-mass-and-scale`.

</details>

<details>
<summary>Section 18.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Minimal-subtraction mass and subtraction scale; Scalar-QED self-energy renormalization problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.minimal-subtraction-mass-and-scale`, `schwartz.scalar-qed-self-energy-renormalization-problem`.

</details>

<details>
<summary>Section 19 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Gauge-fixed photon counterterm conventions; Local-operator criterion for new counterterms; Four on-shell QED renormalization conditions; Full QED vertex–inverse-propagator Ward identity; Gauge-preserving QED renormalization assumption; QED renormalized-perturbation Lagrangian and counterterms; QED two-point counterterm renormalization; QED vertex charge-renormalization condition; QED Z1=Z2 and stable charge ratios; Ward–Takahashi proof of Z1=Z2; Effective-Lagrangian matching route to Z1=Z2; Gauge-invariance route to Z1=Z2. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-fixed-photon-counterterm-conventions`, `schwartz.local-operator-counterterm-criterion`, `schwartz.qed-four-onshell-renormalization-conditions`, `schwartz.qed-full-vertex-inverse-propagator-ward-identity`, `schwartz.qed-gauge-preserving-renormalization-assumption`, `schwartz.qed-renormalized-perturbation-lagrangian`, `schwartz.qed-two-point-counterterm-renormalization`, `schwartz.qed-vertex-charge-renormalization-condition`, `schwartz.qed-z1-equals-z2-charge-ratio-result`, `schwartz.ward-takahashi-proof-of-z1-equals-z2`, `schwartz.z1-z2-effective-matching-route`, `schwartz.z1-z2-gauge-invariance-route`.

</details>

<details>
<summary>Section 19.1 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Gauge-fixed photon counterterm conventions; Local-operator criterion for new counterterms; QED renormalized-perturbation Lagrangian and counterterms. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-fixed-photon-counterterm-conventions`, `schwartz.local-operator-counterterm-criterion`, `schwartz.qed-renormalized-perturbation-lagrangian`.

</details>

<details>
<summary>Section 19.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Gauge-fixed photon counterterm conventions; Local-operator criterion for new counterterms; QED renormalized-perturbation Lagrangian and counterterms; QED two-point counterterm renormalization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauge-fixed-photon-counterterm-conventions`, `schwartz.local-operator-counterterm-criterion`, `schwartz.qed-renormalized-perturbation-lagrangian`, `schwartz.qed-two-point-counterterm-renormalization`.

</details>

<details>
<summary>Section 19.3 — covered</summary>

The accepted method records substantively represent this section's distinct content: QED two-point counterterm renormalization; QED vertex charge-renormalization condition. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-two-point-counterterm-renormalization`, `schwartz.qed-vertex-charge-renormalization-condition`.

</details>

<details>
<summary>Section 19.4 — covered</summary>

The accepted result records substantively represent this section's distinct content: Four on-shell QED renormalization conditions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-four-onshell-renormalization-conditions`.

</details>

<details>
<summary>Section 19.5 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Four on-shell QED renormalization conditions; Full QED vertex–inverse-propagator Ward identity; Gauge-preserving QED renormalization assumption; QED Z1=Z2 and stable charge ratios; Ward–Takahashi proof of Z1=Z2; Effective-Lagrangian matching route to Z1=Z2; Gauge-invariance route to Z1=Z2. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-four-onshell-renormalization-conditions`, `schwartz.qed-full-vertex-inverse-propagator-ward-identity`, `schwartz.qed-gauge-preserving-renormalization-assumption`, `schwartz.qed-z1-equals-z2-charge-ratio-result`, `schwartz.ward-takahashi-proof-of-z1-equals-z2`, `schwartz.z1-z2-effective-matching-route`, `schwartz.z1-z2-gauge-invariance-route`.

</details>

<details>
<summary>Section 19.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Scalar-QED on-shell counterterms problem; Scalar-QED Z1=Z2 proof problem; Yang’s theorem proof problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.scalar-qed-onshell-counterterms-problem`, `schwartz.scalar-qed-z1-z2-proof-problem`, `schwartz.yang-theorem-proof-problem`.

</details>

<details>
<summary>Section 20 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Bloch–Nordsieck and KLN infrared cancellation; d-dimensional real-emission phase-space route; Dimensional real–virtual pole cancellation; d-dimensional tree cross-section normalization; Dimensional vertex UV and IR pole separation; High-energy QED vertex IR structure; Inclusive e+e−→μ+μ−(+γ) cross section; Infrared regulators cancel only in inclusive observables; Initial-state radiation and electron distribution functions; Jet algorithms and Sudakov logarithms; Resolution-defined two-jet cross section; Real-emission tensor and phase-space method; Soft and final-state collinear singularities; Timelike effective charge in annihilation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bloch-nordsieck-and-kln-qualifications`, `schwartz.dimreg-real-emission-three-body-phase-space`, `schwartz.dimreg-real-virtual-pole-cancellation`, `schwartz.dimreg-tree-cross-section-normalization`, `schwartz.dimreg-vertex-uv-ir-pole-separation`, `schwartz.high-energy-qed-vertex-ir-structure`, `schwartz.inclusive-qed-cross-section-ir-finiteness`, `schwartz.infrared-regulator-versus-observable-cancellation`, `schwartz.initial-state-radiation-and-electron-distributions`, `schwartz.jet-algorithms-and-sudakov-logs`, `schwartz.jet-resolution-ir-safe-cross-section`, `schwartz.real-emission-phase-space-method`, `schwartz.soft-and-final-state-collinear-singularities`, `schwartz.vacuum-polarization-timelike-effective-charge`.

</details>

<details>
<summary>Section 20.1 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: High-energy QED vertex IR structure; Inclusive e+e−→μ+μ−(+γ) cross section; Real-emission tensor and phase-space method; Soft and final-state collinear singularities. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.high-energy-qed-vertex-ir-structure`, `schwartz.inclusive-qed-cross-section-ir-finiteness`, `schwartz.real-emission-phase-space-method`, `schwartz.soft-and-final-state-collinear-singularities`.

</details>

<details>
<summary>Section 20.2 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Jet algorithms and Sudakov logarithms; Resolution-defined two-jet cross section; Soft and final-state collinear singularities. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.jet-algorithms-and-sudakov-logs`, `schwartz.jet-resolution-ir-safe-cross-section`, `schwartz.soft-and-final-state-collinear-singularities`.

</details>

<details>
<summary>Section 20.3 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Bloch–Nordsieck and KLN infrared cancellation; Initial-state radiation and electron distribution functions; Jet algorithms and Sudakov logarithms; Resolution-defined two-jet cross section; Timelike effective charge in annihilation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bloch-nordsieck-and-kln-qualifications`, `schwartz.initial-state-radiation-and-electron-distributions`, `schwartz.jet-algorithms-and-sudakov-logs`, `schwartz.jet-resolution-ir-safe-cross-section`, `schwartz.vacuum-polarization-timelike-effective-charge`.

</details>

<details>
<summary>Section 20.A — covered</summary>

The accepted method, result records substantively represent this section's distinct content: d-dimensional real-emission phase-space route; Dimensional real–virtual pole cancellation; d-dimensional tree cross-section normalization; Dimensional vertex UV and IR pole separation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dimreg-real-emission-three-body-phase-space`, `schwartz.dimreg-real-virtual-pole-cancellation`, `schwartz.dimreg-tree-cross-section-normalization`, `schwartz.dimreg-vertex-uv-ir-pole-separation`.

</details>

<details>
<summary>Section 20.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Dimensional real–virtual pole cancellation; Problem 20.1: derive the three-body phase-space formula; Problem 20.2: Sterman–Weinberg jet rates; Problem 20.3: initial-state inclusive rate; Problem 20.4: unfactorized dimensional-regulation rate; Problem 20.5: box and crossed-box IR diagnosis; Problem 20.6: QED splitting function. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.dimreg-real-virtual-pole-cancellation`, `schwartz.problem-20-1-three-body-phase-space`, `schwartz.problem-20-2-sterman-weinberg-rates`, `schwartz.problem-20-3-initial-state-inclusive-rate`, `schwartz.problem-20-4-unfactorized-dimreg-rate`, `schwartz.problem-20-5-box-crossed-box-ir-diagnosis`, `schwartz.problem-20-6-qed-splitting-function`.

</details>

<details>
<summary>Section 21 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Local polynomial form of UV divergences; Low-energy predictivity of non-renormalizable EFT; Power-counting diagnosis of non-renormalizability; 1PI sewing and four-photon Ward cancellation; All-orders QED counterterm closure; QED all-orders induction and BPHZ qualification; QED superficial degree of divergence. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.locality-of-divergent-counterterms`, `schwartz.nonrenormalizable-eft-low-energy-predictivity`, `schwartz.nonrenormalizable-power-counting-diagnosis`, `schwartz.qed-1pi-sewing-and-four-photon-ward-cancellation`, `schwartz.qed-all-orders-counterterm-closure`, `schwartz.qed-all-orders-induction-bphz-qualification`, `schwartz.qed-superficial-degree-of-divergence`.

</details>

<details>
<summary>Section 21.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: 1PI sewing and four-photon Ward cancellation; All-orders QED counterterm closure; QED all-orders induction and BPHZ qualification; QED superficial degree of divergence. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-1pi-sewing-and-four-photon-ward-cancellation`, `schwartz.qed-all-orders-counterterm-closure`, `schwartz.qed-all-orders-induction-bphz-qualification`, `schwartz.qed-superficial-degree-of-divergence`.

</details>

<details>
<summary>Section 21.2 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Local polynomial form of UV divergences; Low-energy predictivity of non-renormalizable EFT; Power-counting diagnosis of non-renormalizability; All-orders QED counterterm closure; QED all-orders induction and BPHZ qualification; QED superficial degree of divergence. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.locality-of-divergent-counterterms`, `schwartz.nonrenormalizable-eft-low-energy-predictivity`, `schwartz.nonrenormalizable-power-counting-diagnosis`, `schwartz.qed-all-orders-counterterm-closure`, `schwartz.qed-all-orders-induction-bphz-qualification`, `schwartz.qed-superficial-degree-of-divergence`.

</details>

<details>
<summary>Section 21.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Low-energy predictivity of non-renormalizable EFT; Problem 21.1: two-loop QED counterterm proof; Problem 21.2: Fourier range comparison; Problem 21.3: scalar interactions by dimension. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.nonrenormalizable-eft-low-energy-predictivity`, `schwartz.problem-21-1-two-loop-qed-counterterms`, `schwartz.problem-21-2-fourier-range-comparison`, `schwartz.problem-21-3-scalar-interactions-by-dimension`.

</details>

<details>
<summary>Section 22 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Chiral Lagrangian derivative expansion; Chiral symmetry protects fermion masses; Cosmological constant and tadpole vacuum shifts; Einstein–Hilbert gravity as an EFT; Electroweak UV completion of Fermi theory; Renormalized 4-Fermi theory; Fine-tuning, naturalness, and anthropic status; Quantum-gravity long-distance prediction; Scalar pole–MS mass sensitivity to heavy particles; Scalar mass self-energy from a heavy Yukawa fermion; Schrödinger equation as a derivative-expansion EFT; Cubic super-renormalizable theory at long distance; Technical naturalness from enhanced symmetry; UV completion and range of validity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-lagrangian-derivative-expansion`, `schwartz.chiral-symmetry-protects-fermion-mass`, `schwartz.cosmological-constant-and-tadpole-vacuum-shift`, `schwartz.einstein-hilbert-gravity-as-eft`, `schwartz.fermi-theory-electroweak-uv-completion`, `schwartz.fermi-theory-renormalized-low-energy-amplitudes`, `schwartz.fine-tuning-naturalness-and-anthropic-status`, `schwartz.gravity-local-versus-nonanalytic-corrections`, `schwartz.scalar-pole-ms-heavy-threshold-sensitivity`, `schwartz.scalar-yukawa-mass-self-energy`, `schwartz.schrodinger-derivative-expansion-eft`, `schwartz.superrenormalizable-cubic-long-distance-breakdown`, `schwartz.technical-naturalness-custodial-symmetry`, `schwartz.uv-completion-and-range-of-validity`.

</details>

<details>
<summary>Section 22.1 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Schrödinger equation as a derivative-expansion EFT; UV completion and range of validity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.schrodinger-derivative-expansion-eft`, `schwartz.uv-completion-and-range-of-validity`.

</details>

<details>
<summary>Section 22.2 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Electroweak UV completion of Fermi theory; Renormalized 4-Fermi theory; Schrödinger equation as a derivative-expansion EFT. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.fermi-theory-electroweak-uv-completion`, `schwartz.fermi-theory-renormalized-low-energy-amplitudes`, `schwartz.schrodinger-derivative-expansion-eft`.

</details>

<details>
<summary>Section 22.3 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Chiral Lagrangian derivative expansion; Electroweak UV completion of Fermi theory. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-lagrangian-derivative-expansion`, `schwartz.fermi-theory-electroweak-uv-completion`.

</details>

<details>
<summary>Section 22.4 — covered</summary>

The accepted result records substantively represent this section's distinct content: Chiral Lagrangian derivative expansion; Einstein–Hilbert gravity as an EFT; Quantum-gravity long-distance prediction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-lagrangian-derivative-expansion`, `schwartz.einstein-hilbert-gravity-as-eft`, `schwartz.gravity-local-versus-nonanalytic-corrections`.

</details>

<details>
<summary>Section 22.5 — covered</summary>

The accepted result records substantively represent this section's distinct content: Quantum-gravity long-distance prediction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gravity-local-versus-nonanalytic-corrections`.

</details>

<details>
<summary>Section 22.6 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Chiral symmetry protects fermion masses; Fine-tuning, naturalness, and anthropic status; Quantum-gravity long-distance prediction; Scalar pole–MS mass sensitivity to heavy particles; Scalar mass self-energy from a heavy Yukawa fermion. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-symmetry-protects-fermion-mass`, `schwartz.fine-tuning-naturalness-and-anthropic-status`, `schwartz.gravity-local-versus-nonanalytic-corrections`, `schwartz.scalar-pole-ms-heavy-threshold-sensitivity`, `schwartz.scalar-yukawa-mass-self-energy`.

</details>

<details>
<summary>Section 22.7 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Cosmological constant and tadpole vacuum shifts; Cubic super-renormalizable theory at long distance; Technical naturalness from enhanced symmetry. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cosmological-constant-and-tadpole-vacuum-shift`, `schwartz.superrenormalizable-cubic-long-distance-breakdown`, `schwartz.technical-naturalness-custodial-symmetry`.

</details>

<details>
<summary>Section 22.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem 22.1: hydrogen derivative versus logarithmic correction; Problem 22.2: M−4 Fermi matching; Problem 22.3: chiral coefficient expansion; Problem 22.4: higher-curvature potential; Problem 22.5: cubic potential and history; Cubic super-renormalizable theory at long distance. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-22-1-hydrogen-derivative-log-correction`, `schwartz.problem-22-2-fermi-m-minus-four-matching`, `schwartz.problem-22-3-chiral-coefficient-expansion`, `schwartz.problem-22-4-higher-curvature-potential`, `schwartz.problem-22-5-cubic-potential-history`, `schwartz.superrenormalizable-cubic-long-distance-breakdown`.

</details>

<details>
<summary>Section 23 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Anomalous dimensions as deviations from classical scaling; Callan–Symanzik equation for Green functions; Conserved vector current has zero anomalous dimension; Continuum and Wilsonian renormalization groups; External versus Lagrangian operator running; Fixed points, conformal theory, and RG trajectories; Four-Fermi operator renormalization and running; General solution for a multiplicatively running coefficient; Dimensional transmutation of the QED running charge; Infrared freedom, asymptotic freedom, and possible interacting fixed points; Beta functions and mass anomalous dimensions from counterterms; RG resummation of large logarithms; Unphysical scales, dimensional regularization, and RG logarithms; Scalar mass counterterm from a mass insertion; Scalar mass counterterm from the massive tadpole; Scalar-mass RG, Yukawa potential, and correlation length; Scalar phi-four beta function and mass anomalous dimension; Weak four-Fermi QED problem inputs; Wilson coefficients, matching, and operator mixing; Wilson–Fisher fixed point and universal critical exponent; Wilson–Polchinski exact RG construction; Wilsonian cutoff flow and operator relevance; Operator mixing, irrelevance, and scalar fine tuning; Wilsonian power terms, continuum logarithms, and RG eigenoperators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomalous-dimension-as-quantum-scaling-deviation`, `schwartz.callan-symanzik-green-function-rge`, `schwartz.conserved-current-zero-anomalous-dimension`, `schwartz.continuum-and-wilsonian-rg-distinction`, `schwartz.external-operator-and-lagrangian-operator-rg`, `schwartz.fixed-points-conformal-theory-and-rg-trajectory`, `schwartz.four-fermi-operator-rg-toy-scalar-route`, `schwartz.multiplicative-rg-coefficient-general-solution`, `schwartz.qed-dimensional-transmutation-and-landau-scale`, `schwartz.rg-asymptotic-behavior-classification`, `schwartz.rg-beta-and-mass-anomalous-dimensions-from-counterterms`, `schwartz.rg-large-log-resummation`, `schwartz.rg-unphysical-scale-logarithm-qualification`, `schwartz.scalar-mass-counterterm-mass-insertion-route`, `schwartz.scalar-mass-counterterm-massive-tadpole-route`, `schwartz.scalar-mass-rg-yukawa-correlation-length`, `schwartz.scalar-phi4-beta-and-mass-anomalous-dimension`, `schwartz.weak-four-fermi-qed-problem-inputs`, `schwartz.wilson-coefficients-operator-mixing-and-matching`, `schwartz.wilson-fisher-fixed-point-and-universal-critical-exponent`, `schwartz.wilson-polchinski-exact-rg-construction`, `schwartz.wilsonian-cutoff-flow-and-operator-relevance`, `schwartz.wilsonian-operator-mixing-irrelevance-and-fine-tuning`, `schwartz.wilsonian-power-terms-continuum-logs-and-eigenoperators`.

</details>

<details>
<summary>Section 23.1 — covered</summary>

The accepted assumption, method records substantively represent this section's distinct content: RG resummation of large logarithms; Unphysical scales, dimensional regularization, and RG logarithms. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.rg-large-log-resummation`, `schwartz.rg-unphysical-scale-logarithm-qualification`.

</details>

<details>
<summary>Section 23.2 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Dimensional transmutation of the QED running charge; Beta functions and mass anomalous dimensions from counterterms; Unphysical scales, dimensional regularization, and RG logarithms. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qed-dimensional-transmutation-and-landau-scale`, `schwartz.rg-beta-and-mass-anomalous-dimensions-from-counterterms`, `schwartz.rg-unphysical-scale-logarithm-qualification`.

</details>

<details>
<summary>Section 23.3 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Four-Fermi operator renormalization and running; Beta functions and mass anomalous dimensions from counterterms; Weak four-Fermi QED problem inputs. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.four-fermi-operator-rg-toy-scalar-route`, `schwartz.rg-beta-and-mass-anomalous-dimensions-from-counterterms`, `schwartz.weak-four-fermi-qed-problem-inputs`.

</details>

<details>
<summary>Section 23.4 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Anomalous dimensions as deviations from classical scaling; Callan–Symanzik equation for Green functions; Conserved vector current has zero anomalous dimension; External versus Lagrangian operator running; Four-Fermi operator renormalization and running; General solution for a multiplicatively running coefficient; Wilson coefficients, matching, and operator mixing. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomalous-dimension-as-quantum-scaling-deviation`, `schwartz.callan-symanzik-green-function-rge`, `schwartz.conserved-current-zero-anomalous-dimension`, `schwartz.external-operator-and-lagrangian-operator-rg`, `schwartz.four-fermi-operator-rg-toy-scalar-route`, `schwartz.multiplicative-rg-coefficient-general-solution`, `schwartz.wilson-coefficients-operator-mixing-and-matching`.

</details>

<details>
<summary>Section 23.5 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Anomalous dimensions as deviations from classical scaling; Fixed points, conformal theory, and RG trajectories; Scalar mass counterterm from a mass insertion; Scalar mass counterterm from the massive tadpole; Scalar-mass RG, Yukawa potential, and correlation length; Scalar phi-four beta function and mass anomalous dimension; Wilson–Fisher fixed point and universal critical exponent. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomalous-dimension-as-quantum-scaling-deviation`, `schwartz.fixed-points-conformal-theory-and-rg-trajectory`, `schwartz.scalar-mass-counterterm-mass-insertion-route`, `schwartz.scalar-mass-counterterm-massive-tadpole-route`, `schwartz.scalar-mass-rg-yukawa-correlation-length`, `schwartz.scalar-phi4-beta-and-mass-anomalous-dimension`, `schwartz.wilson-fisher-fixed-point-and-universal-critical-exponent`.

</details>

<details>
<summary>Section 23.6 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Fixed points, conformal theory, and RG trajectories; Infrared freedom, asymptotic freedom, and possible interacting fixed points; Wilson–Polchinski exact RG construction; Wilsonian cutoff flow and operator relevance; Operator mixing, irrelevance, and scalar fine tuning; Wilsonian power terms, continuum logarithms, and RG eigenoperators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.fixed-points-conformal-theory-and-rg-trajectory`, `schwartz.rg-asymptotic-behavior-classification`, `schwartz.wilson-polchinski-exact-rg-construction`, `schwartz.wilsonian-cutoff-flow-and-operator-relevance`, `schwartz.wilsonian-operator-mixing-irrelevance-and-fine-tuning`, `schwartz.wilsonian-power-terms-continuum-logs-and-eigenoperators`.

</details>

<details>
<summary>Section 23.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem: O(N) scalar Wilson–Fisher analysis; Problem: anomalous dimension and running of a QED composite operator; Problem: recover the scalar-mass RG solution; Problem: prove the weak four-Fermi QED logarithm vanishes; Problem: regulator and scheme dependence at the Wilson–Fisher point; Problem: two-loop Wilson–Fisher critical exponent; Problem: derive the Wilson–Polchinski functional RGE; Problem: Wilsonian scalar-mass sensitivity; Weak four-Fermi QED problem inputs; Operator mixing, irrelevance, and scalar fine tuning; Wilsonian power terms, continuum logarithms, and RG eigenoperators. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-on-scalar-wilson-fisher-fixed-point`, `schwartz.problem-rg-operator-anomalous-dimension-running`, `schwartz.problem-scalar-mass-rg-small-coupling-solution`, `schwartz.problem-weak-four-fermi-qed-nonrunning`, `schwartz.problem-wilson-fisher-scheme-independence`, `schwartz.problem-wilson-fisher-two-loop-critical-exponent`, `schwartz.problem-wilson-polchinski-functional-rge`, `schwartz.problem-wilsonian-scalar-mass-sensitivity`, `schwartz.weak-four-fermi-qed-problem-inputs`, `schwartz.wilsonian-operator-mixing-irrelevance-and-fine-tuning`, `schwartz.wilsonian-power-terms-continuum-logs-and-eigenoperators`.

</details>

<details>
<summary>Section 24 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Alternative physical notions of locality; Bare spectral normalization and 0≤Z≤1; Cutkosky cutting rules for discontinuities; Feynman tree theorem full-loop decomposition; Froissart total-cross-section growth bound; Generalized optical theorem; Spectral representation and positive spectral density; Locality, integrating out, and the missing-pole constraint; Longitudinal-W scattering and Higgs restoration of perturbative unitarity; Narrow-resonance coupling enhancement; Nonperturbative LSZ poles and interpolating fields; Optical theorem for decay widths and forward total cross sections; Partial-wave unitarity bound and perturbative breakdown; One-particle poles and factorization of Green functions; Two-propagator scalar loop setup for contour cutting; Scalar partial-wave Legendre representation; Spectral positivity forbids faster-than-1/p² propagators; Stueckelberg nonlocal form signals a missing longitudinal state; Unitarity, propagator numerators, and physical polarization sums; Unitary Hilbert space and complete physical states; Unstable poles, Breit–Wigner form, and narrow-width approximation; Complex-pole and MS mass schemes for unstable states. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.alternative-physical-notions-of-locality`, `schwartz.bare-spectral-normalization-and-field-strength-limit`, `schwartz.cutkosky-cutting-rules-and-feynman-tree-theorem`, `schwartz.feynman-tree-theorem-full-loop-decomposition`, `schwartz.froissart-total-cross-section-growth-bound`, `schwartz.generalized-optical-theorem`, `schwartz.kallen-lehmann-spectral-representation-and-positivity`, `schwartz.locality-integrating-out-and-missing-pole`, `schwartz.longitudinal-w-higgs-perturbative-unitarity`, `schwartz.narrow-resonance-coupling-enhancement`, `schwartz.nonperturbative-lsz-poles-and-interpolating-fields`, `schwartz.optical-theorem-decay-and-forward-cross-section`, `schwartz.partial-wave-unitarity-bound-and-perturbative-breakdown`, `schwartz.polology-one-particle-pole-factorization`, `schwartz.scalar-bubble-cutting-loop-setup`, `schwartz.scalar-partial-wave-legendre-representation`, `schwartz.spectral-positivity-propagator-falloff-bound`, `schwartz.stueckelberg-nonlocal-form-and-missing-longitudinal-state`, `schwartz.unitarity-propagator-numerator-and-physical-polarizations`, `schwartz.unitary-hilbert-space-completeness`, `schwartz.unstable-particle-breit-wigner-and-narrow-width`, `schwartz.unstable-particle-complex-pole-and-ms-mass-schemes`.

</details>

<details>
<summary>Section 24.1 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Cutkosky cutting rules for discontinuities; Feynman tree theorem full-loop decomposition; Froissart total-cross-section growth bound; Generalized optical theorem; Longitudinal-W scattering and Higgs restoration of perturbative unitarity; Narrow-resonance coupling enhancement; Optical theorem for decay widths and forward total cross sections; Partial-wave unitarity bound and perturbative breakdown; Two-propagator scalar loop setup for contour cutting; Scalar partial-wave Legendre representation; Unitarity, propagator numerators, and physical polarization sums; Unitary Hilbert space and complete physical states; Unstable poles, Breit–Wigner form, and narrow-width approximation; Complex-pole and MS mass schemes for unstable states. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.cutkosky-cutting-rules-and-feynman-tree-theorem`, `schwartz.feynman-tree-theorem-full-loop-decomposition`, `schwartz.froissart-total-cross-section-growth-bound`, `schwartz.generalized-optical-theorem`, `schwartz.longitudinal-w-higgs-perturbative-unitarity`, `schwartz.narrow-resonance-coupling-enhancement`, `schwartz.optical-theorem-decay-and-forward-cross-section`, `schwartz.partial-wave-unitarity-bound-and-perturbative-breakdown`, `schwartz.scalar-bubble-cutting-loop-setup`, `schwartz.scalar-partial-wave-legendre-representation`, `schwartz.unitarity-propagator-numerator-and-physical-polarizations`, `schwartz.unitary-hilbert-space-completeness`, `schwartz.unstable-particle-breit-wigner-and-narrow-width`, `schwartz.unstable-particle-complex-pole-and-ms-mass-schemes`.

</details>

<details>
<summary>Section 24.2 — covered</summary>

The accepted result records substantively represent this section's distinct content: Bare spectral normalization and 0≤Z≤1; Spectral representation and positive spectral density; Longitudinal-W scattering and Higgs restoration of perturbative unitarity; Partial-wave unitarity bound and perturbative breakdown; Spectral positivity forbids faster-than-1/p² propagators. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bare-spectral-normalization-and-field-strength-limit`, `schwartz.kallen-lehmann-spectral-representation-and-positivity`, `schwartz.longitudinal-w-higgs-perturbative-unitarity`, `schwartz.partial-wave-unitarity-bound-and-perturbative-breakdown`, `schwartz.spectral-positivity-propagator-falloff-bound`.

</details>

<details>
<summary>Section 24.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Bare spectral normalization and 0≤Z≤1; Nonperturbative LSZ poles and interpolating fields; One-particle poles and factorization of Green functions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bare-spectral-normalization-and-field-strength-limit`, `schwartz.nonperturbative-lsz-poles-and-interpolating-fields`, `schwartz.polology-one-particle-pole-factorization`.

</details>

<details>
<summary>Section 24.4 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Alternative physical notions of locality; Locality, integrating out, and the missing-pole constraint; Nonperturbative LSZ poles and interpolating fields; Stueckelberg nonlocal form signals a missing longitudinal state. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.alternative-physical-notions-of-locality`, `schwartz.locality-integrating-out-and-missing-pole`, `schwartz.nonperturbative-lsz-poles-and-interpolating-fields`, `schwartz.stueckelberg-nonlocal-form-and-missing-longitudinal-state`.

</details>

<details>
<summary>Section 24.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem: derive cutting rules by contour integration; Problem: Dirac spinor spectral representation; Problem: LSZ reduction in MS; Problem: scalar partial-wave unitarity bound; Stueckelberg nonlocal form signals a missing longitudinal state. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-cutting-rules-contour-derivation`, `schwartz.problem-dirac-spectral-representation`, `schwartz.problem-ms-lsz-reduction`, `schwartz.problem-scalar-partial-wave-unitarity`, `schwartz.stueckelberg-nonlocal-form-and-missing-longitudinal-state`.

</details>

<details>
<summary>Section 25 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Abelian Wilson line as parallel transport; Abelian Wilson loop and curvature; Adjoint representation of gauge fields; Anomaly coefficient definition and normalization; Axial and lightcone gauges; BRST cohomology and physical states; BRST transformations and nilpotency task; Casimir, index, and SU(N) color factors; Faddeev–Popov gauge-orbit determinant; Fundamental and antifundamental transformations; Lattice correlator mass extraction; Lattice link fields and gauge covariance; Plaquette continuum limit; Lattice Wilson action from plaquette matching; Lie generators, bracket, and Jacobi identity; Non-Abelian connection and curvature; Non-Abelian Noether current and covariant matter current; Non-Abelian path-ordered Wilson line; Orthogonal, symplectic, and exceptional simple groups; R_xi Faddeev–Popov Lagrangian and propagators; Simple and semisimple Lie algebras; Restriction from U(N) to simple SU(N) factors; SU(N) defining representation and dimension; SU(N) Fierz and trace reduction; SU(N) generator normalization and trace; SU(N) generator products and d^{abc}; Weinberg–Witten spin-one current obstruction; Weinberg–Witten spin-two obstruction and fixed-spacetime qualification; Local SU(2) Yang–Mills construction; Yang–Mills theta term qualification. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-wilson-line-as-parallel-transport`, `schwartz.abelian-wilson-loop-curvature`, `schwartz.adjoint-representation-of-gauge-fields`, `schwartz.anomaly-coefficient-definition-and-normalization`, `schwartz.axial-and-lightcone-gauges-ghost-decoupling`, `schwartz.brst-cohomological-physical-state-qualification`, `schwartz.brst-transformations-and-nilpotency-task`, `schwartz.casimir-index-and-sun-color-factors`, `schwartz.faddeev-popov-gauge-orbit-determinant`, `schwartz.fundamental-antifundamental-transformations`, `schwartz.lattice-correlator-mass-extraction`, `schwartz.lattice-link-fields-and-gauge-covariance`, `schwartz.lattice-plaquette-continuum-field-strength`, `schwartz.lattice-wilson-action-continuum-matching`, `schwartz.lie-group-generators-bracket-and-jacobi`, `schwartz.nonabelian-connection-and-curvature`, `schwartz.nonabelian-noether-current-and-covariant-matter-current`, `schwartz.nonabelian-path-ordered-wilson-line`, `schwartz.orthogonal-symplectic-and-exceptional-simple-groups`, `schwartz.rxi-faddeev-popov-lagrangian-and-propagators`, `schwartz.simple-and-semisimple-lie-algebras`, `schwartz.simple-sun-restriction-from-un-splitting`, `schwartz.sun-defining-representation-and-dimension`, `schwartz.sun-fierz-and-trace-reduction`, `schwartz.sun-generator-normalization-and-trace`, `schwartz.sun-generator-products-and-symmetric-invariant`, `schwartz.weinberg-witten-spin-one-current-obstruction`, `schwartz.weinberg-witten-spin-two-and-fixed-spacetime-qualification`, `schwartz.yang-mills-local-su2-construction`, `schwartz.yang-mills-theta-term-perturbative-qualification`.

</details>

<details>
<summary>Section 25.1 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Adjoint representation of gauge fields; Casimir, index, and SU(N) color factors; Fundamental and antifundamental transformations; Lie generators, bracket, and Jacobi identity; Orthogonal, symplectic, and exceptional simple groups; Simple and semisimple Lie algebras; SU(N) defining representation and dimension; SU(N) Fierz and trace reduction; SU(N) generator normalization and trace; SU(N) generator products and d^{abc}; Local SU(2) Yang–Mills construction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.adjoint-representation-of-gauge-fields`, `schwartz.casimir-index-and-sun-color-factors`, `schwartz.fundamental-antifundamental-transformations`, `schwartz.lie-group-generators-bracket-and-jacobi`, `schwartz.orthogonal-symplectic-and-exceptional-simple-groups`, `schwartz.simple-and-semisimple-lie-algebras`, `schwartz.sun-defining-representation-and-dimension`, `schwartz.sun-fierz-and-trace-reduction`, `schwartz.sun-generator-normalization-and-trace`, `schwartz.sun-generator-products-and-symmetric-invariant`, `schwartz.yang-mills-local-su2-construction`.

</details>

<details>
<summary>Section 25.2 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Abelian Wilson line as parallel transport; Abelian Wilson loop and curvature; Anomaly coefficient definition and normalization; Non-Abelian connection and curvature; Non-Abelian path-ordered Wilson line; SU(N) Fierz and trace reduction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-wilson-line-as-parallel-transport`, `schwartz.abelian-wilson-loop-curvature`, `schwartz.anomaly-coefficient-definition-and-normalization`, `schwartz.nonabelian-connection-and-curvature`, `schwartz.nonabelian-path-ordered-wilson-line`, `schwartz.sun-fierz-and-trace-reduction`.

</details>

<details>
<summary>Section 25.3 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: Non-Abelian connection and curvature; Non-Abelian Noether current and covariant matter current; Weinberg–Witten spin-one current obstruction; Yang–Mills theta term qualification. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.nonabelian-connection-and-curvature`, `schwartz.nonabelian-noether-current-and-covariant-matter-current`, `schwartz.weinberg-witten-spin-one-current-obstruction`, `schwartz.yang-mills-theta-term-perturbative-qualification`.

</details>

<details>
<summary>Section 25.4 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Axial and lightcone gauges; BRST cohomology and physical states; BRST transformations and nilpotency task; Faddeev–Popov gauge-orbit determinant; R_xi Faddeev–Popov Lagrangian and propagators; Weinberg–Witten spin-two obstruction and fixed-spacetime qualification. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.axial-and-lightcone-gauges-ghost-decoupling`, `schwartz.brst-cohomological-physical-state-qualification`, `schwartz.brst-transformations-and-nilpotency-task`, `schwartz.faddeev-popov-gauge-orbit-determinant`, `schwartz.rxi-faddeev-popov-lagrangian-and-propagators`, `schwartz.weinberg-witten-spin-two-and-fixed-spacetime-qualification`.

</details>

<details>
<summary>Section 25.5 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Lattice correlator mass extraction; Lattice link fields and gauge covariance; Plaquette continuum limit; Lattice Wilson action from plaquette matching. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.lattice-correlator-mass-extraction`, `schwartz.lattice-link-fields-and-gauge-covariance`, `schwartz.lattice-plaquette-continuum-field-strength`, `schwartz.lattice-wilson-action-continuum-matching`.

</details>

<details>
<summary>Section 25.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Anomaly conjugate and real-representation task; Anomaly direct-sum task; Anomaly SU(4) ten task; Anomaly tensor-product task; BRST transformations and nilpotency task; Generator-product trace identities task; Heisenberg algebra matrix and classification task; Lorentz complexification semisimplicity task; Non-Abelian Noether-current conservation task; Non-Abelian path-ordered Wilson line; Semisimplicity Hermitian-representations task; U(N) semisimplicity task; Yang–Mills gauge-invariance task. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.anomaly-conjugate-and-real-representation-task`, `schwartz.anomaly-direct-sum-task`, `schwartz.anomaly-su4-ten-task`, `schwartz.anomaly-tensor-product-task`, `schwartz.brst-transformations-and-nilpotency-task`, `schwartz.generator-product-trace-identities-task`, `schwartz.heisenberg-algebra-matrix-and-classification-task`, `schwartz.lorentz-complexification-semisimplicity-task`, `schwartz.nonabelian-noether-current-conservation-task`, `schwartz.nonabelian-path-ordered-wilson-line`, `schwartz.semisimplicity-hermitian-representations-task`, `schwartz.un-unitary-group-semisimplicity-task`, `schwartz.yang-mills-gauge-invariance-task`.

</details>

<details>
<summary>Section 26 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Strong-coupling extraction, scheme, and scale; Failure of a classical-current QCD potential; Colored fermion and scalar vertices; Fermion vacuum-polarization color factor; Four-gluon seagull scaleless integral and d=2 cancellation; General R_xi one-loop counterterm summary; Ghost bubble sign and integral; Gluon and ghost transverse vacuum polarization; Gluon bubble dimensional-regularization derivation; Higher-order QCD running expansions; Non-Abelian charge universality; Non-Abelian vertex conventions; QCD asymptotic freedom and Lambda_QCD; QCD beta function from the bare charge; QCD color-channel potentials; QCD Feynman rules with color and ghosts; QCD one-loop quark–gluon vertex counterterm; QCD one-loop two-point counterterms; QCD renormalization constants and MS UV-pole trick; QCD vacuum-polarization diagram set; NLO R_had and real–virtual IR cancellation; Tree-level hadron ratio and inclusive factorization; Wilson-loop definition of the QCD potential. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.alpha-s-extraction-scheme-and-scale`, `schwartz.classical-qcd-current-potential-failure`, `schwartz.colored-matter-vertices`, `schwartz.fermion-vacuum-polarization-color-factor`, `schwartz.four-gluon-seagull-scaleless-integral-and-d2-cancellation`, `schwartz.general-rxi-one-loop-counterterm-summary`, `schwartz.ghost-bubble-sign-and-integral`, `schwartz.gluon-and-ghost-transverse-vacuum-polarization`, `schwartz.gluon-bubble-dimensional-regularization-derivation`, `schwartz.higher-order-qcd-running-expansions`, `schwartz.nonabelian-charge-universality-slavnov-taylor-relations`, `schwartz.nonabelian-vertex-conventions`, `schwartz.qcd-asymptotic-freedom-and-lambdaqcd`, `schwartz.qcd-beta-function-from-bare-charge`, `schwartz.qcd-color-channel-potentials`, `schwartz.qcd-feynman-rules-with-color-and-ghosts`, `schwartz.qcd-one-loop-quark-gluon-vertex-counterterm`, `schwartz.qcd-one-loop-two-point-counterterms`, `schwartz.qcd-renormalization-constants-and-ms-uv-trick`, `schwartz.qcd-vacuum-polarization-diagram-set`, `schwartz.rhad-nlo-real-virtual-ir-cancellation`, `schwartz.tree-level-rhad-color-and-flavor-count`, `schwartz.wilson-loop-gauge-invariant-qcd-potential`.

</details>

<details>
<summary>Section 26.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Colored fermion and scalar vertices; Non-Abelian vertex conventions; QCD Feynman rules with color and ghosts. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.colored-matter-vertices`, `schwartz.nonabelian-vertex-conventions`, `schwartz.qcd-feynman-rules-with-color-and-ghosts`.

</details>

<details>
<summary>Section 26.2 — covered</summary>

The accepted result records substantively represent this section's distinct content: QCD color-channel potentials. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.qcd-color-channel-potentials`.

</details>

<details>
<summary>Section 26.3 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: Strong-coupling extraction, scheme, and scale; QCD color-channel potentials; NLO R_had and real–virtual IR cancellation; Tree-level hadron ratio and inclusive factorization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.alpha-s-extraction-scheme-and-scale`, `schwartz.qcd-color-channel-potentials`, `schwartz.rhad-nlo-real-virtual-ir-cancellation`, `schwartz.tree-level-rhad-color-and-flavor-count`.

</details>

<details>
<summary>Section 26.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Fermion vacuum-polarization color factor; Four-gluon seagull scaleless integral and d=2 cancellation; Ghost bubble sign and integral; Gluon and ghost transverse vacuum polarization; Gluon bubble dimensional-regularization derivation; QCD vacuum-polarization diagram set. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.fermion-vacuum-polarization-color-factor`, `schwartz.four-gluon-seagull-scaleless-integral-and-d2-cancellation`, `schwartz.ghost-bubble-sign-and-integral`, `schwartz.gluon-and-ghost-transverse-vacuum-polarization`, `schwartz.gluon-bubble-dimensional-regularization-derivation`, `schwartz.qcd-vacuum-polarization-diagram-set`.

</details>

<details>
<summary>Section 26.5 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: General R_xi one-loop counterterm summary; Gluon and ghost transverse vacuum polarization; QCD one-loop quark–gluon vertex counterterm; QCD one-loop two-point counterterms; QCD renormalization constants and MS UV-pole trick. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.general-rxi-one-loop-counterterm-summary`, `schwartz.gluon-and-ghost-transverse-vacuum-polarization`, `schwartz.qcd-one-loop-quark-gluon-vertex-counterterm`, `schwartz.qcd-one-loop-two-point-counterterms`, `schwartz.qcd-renormalization-constants-and-ms-uv-trick`.

</details>

<details>
<summary>Section 26.6 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: General R_xi one-loop counterterm summary; Higher-order QCD running expansions; QCD asymptotic freedom and Lambda_QCD; QCD beta function from the bare charge. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.general-rxi-one-loop-counterterm-summary`, `schwartz.higher-order-qcd-running-expansions`, `schwartz.qcd-asymptotic-freedom-and-lambdaqcd`, `schwartz.qcd-beta-function-from-bare-charge`.

</details>

<details>
<summary>Section 26.7 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Failure of a classical-current QCD potential; Non-Abelian charge universality; Wilson-loop definition of the QCD potential. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.classical-qcd-current-potential-failure`, `schwartz.nonabelian-charge-universality-slavnov-taylor-relations`, `schwartz.wilson-loop-gauge-invariant-qcd-potential`.

</details>

<details>
<summary>Section 26.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Colored-scalar QCD beta-function task; Ghost two-point counterterm task; Regge behavior and flux-tube evidence; Remaining QCD counterterms task; Wilson area law and confinement qualification. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.colored-scalar-qcd-beta-task`, `schwartz.ghost-two-point-counterterm-task`, `schwartz.regge-behavior-and-flux-tube-evidence`, `schwartz.remaining-qcd-counterterms-task`, `schwartz.wilson-area-law-confinement-evidence-qualification`.

</details>

<details>
<summary>Section 27 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Amplitude outlook: gravity square and open formulation; BCFW complex shift and residue recursion; BCFW large-z helicity qualification; BCFW MHV example and Parke–Taylor recursion; BCFW pole location and recursion formula; Color-ordered partial amplitudes; Color traces, photon decoupling, and double-line flow; Complex three-point kinematics; Four-point factorization implies Jacobi identity; Color-summed gg to gg cross section; Direct gg to gg MHV channel derivation; Helicity spinor brackets and sigma identities; Helicity-spinor QED annihilation check; Little-group scaling constraint on amplitudes; Massless Dirac spinors in helicity notation; Massless momentum spinor factorization; Parke–Taylor MHV formula; Reference changes implement the Ward identity; Spinor-helicity physical on-shell amplitude route; Spinor-helicity polarizations and reference momentum; Spinor products, momentum conservation, and Schouten; Three-point amplitude constraints; Tree gluon helicity vanishing selection rules. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.amplitude-outlook-gravity-square-and-open-formulation`, `schwartz.bcfw-complex-shift-and-residue-recursion`, `schwartz.bcfw-large-z-helicity-qualification`, `schwartz.bcfw-mhv-example-and-parke-taylor-recursion`, `schwartz.bcfw-pole-location-and-recursion-formula`, `schwartz.color-ordered-partial-amplitudes`, `schwartz.color-trace-reduction-and-photon-decoupling`, `schwartz.complex-three-point-kinematics`, `schwartz.four-point-factorization-implies-jacobi`, `schwartz.gg-to-gg-color-summed-cross-section`, `schwartz.gg-to-gg-mhv-channel-derivation`, `schwartz.helicity-spinor-brackets-and-sigma-identities`, `schwartz.helicity-spinor-qed-annihilation-check`, `schwartz.little-group-scaling-helicity-amplitude-constraint`, `schwartz.massless-dirac-spinors-in-helicity-notation`, `schwartz.massless-momentum-spinor-factorization`, `schwartz.parke-taylor-mhv-formula`, `schwartz.reference-change-as-ward-identity`, `schwartz.spinor-helicity-physical-onshell-amplitude-route`, `schwartz.spinor-helicity-polarizations-and-reference-momentum`, `schwartz.spinor-products-momentum-conservation-and-schouten`, `schwartz.three-point-little-group-renormalizability-and-antisymmetry`, `schwartz.tree-gluon-helicity-vanishing-selection-rules`.

</details>

<details>
<summary>Section 27.1 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Helicity spinor brackets and sigma identities; Helicity-spinor QED annihilation check; Little-group scaling constraint on amplitudes; Massless Dirac spinors in helicity notation; Massless momentum spinor factorization; Reference changes implement the Ward identity; Spinor-helicity physical on-shell amplitude route; Spinor-helicity polarizations and reference momentum; Spinor products, momentum conservation, and Schouten. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.helicity-spinor-brackets-and-sigma-identities`, `schwartz.helicity-spinor-qed-annihilation-check`, `schwartz.little-group-scaling-helicity-amplitude-constraint`, `schwartz.massless-dirac-spinors-in-helicity-notation`, `schwartz.massless-momentum-spinor-factorization`, `schwartz.reference-change-as-ward-identity`, `schwartz.spinor-helicity-physical-onshell-amplitude-route`, `schwartz.spinor-helicity-polarizations-and-reference-momentum`, `schwartz.spinor-products-momentum-conservation-and-schouten`.

</details>

<details>
<summary>Section 27.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Color traces, photon decoupling, and double-line flow; Helicity-spinor QED annihilation check; Tree gluon helicity vanishing selection rules. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.color-trace-reduction-and-photon-decoupling`, `schwartz.helicity-spinor-qed-annihilation-check`, `schwartz.tree-gluon-helicity-vanishing-selection-rules`.

</details>

<details>
<summary>Section 27.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Color-summed gg to gg cross section; Direct gg to gg MHV channel derivation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gg-to-gg-color-summed-cross-section`, `schwartz.gg-to-gg-mhv-channel-derivation`.

</details>

<details>
<summary>Section 27.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Color-ordered partial amplitudes; Color-summed gg to gg cross section; Parke–Taylor MHV formula. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.color-ordered-partial-amplitudes`, `schwartz.gg-to-gg-color-summed-cross-section`, `schwartz.parke-taylor-mhv-formula`.

</details>

<details>
<summary>Section 27.5 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: Complex three-point kinematics; Four-point factorization implies Jacobi identity; Parke–Taylor MHV formula; Three-point amplitude constraints. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.complex-three-point-kinematics`, `schwartz.four-point-factorization-implies-jacobi`, `schwartz.parke-taylor-mhv-formula`, `schwartz.three-point-little-group-renormalizability-and-antisymmetry`.

</details>

<details>
<summary>Section 27.6 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: BCFW complex shift and residue recursion; BCFW large-z helicity qualification; BCFW MHV example and Parke–Taylor recursion; BCFW pole location and recursion formula; Four-point factorization implies Jacobi identity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bcfw-complex-shift-and-residue-recursion`, `schwartz.bcfw-large-z-helicity-qualification`, `schwartz.bcfw-mhv-example-and-parke-taylor-recursion`, `schwartz.bcfw-pole-location-and-recursion-formula`, `schwartz.four-point-factorization-implies-jacobi`.

</details>

<details>
<summary>Section 27.7 — covered</summary>

The accepted concept, method records substantively represent this section's distinct content: Amplitude outlook: gravity square and open formulation; BCFW MHV example and Parke–Taylor recursion. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.amplitude-outlook-gravity-square-and-open-formulation`, `schwartz.bcfw-mhv-example-and-parke-taylor-recursion`.

</details>

<details>
<summary>Section 27.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Amplitude outlook: gravity square and open formulation; Color-ordered general formula proof task; Complex factorization branch-analysis task; Five-gluon squared-amplitude task; Helicity Compton cross-section task; Parke–Taylor BCFW proof task; Parke–Taylor cross-section verification task; Polarization-vector reference-choice task; Remaining QCD two-to-two squared-amplitudes task. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.amplitude-outlook-gravity-square-and-open-formulation`, `schwartz.color-ordered-general-formula-proof-task`, `schwartz.complex-factorization-branch-analysis-task`, `schwartz.five-gluon-squared-amplitude-task`, `schwartz.helicity-compton-cross-section-task`, `schwartz.parke-taylor-bcfw-proof-task`, `schwartz.parke-taylor-cross-section-verification-task`, `schwartz.polarization-vector-reference-choice-task`, `schwartz.remaining-qcd-two-to-two-squared-amplitudes-task`.

</details>

<details>
<summary>Section 28 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Abelian Higgs gauge shift and degree count; Abelian Higgs model and vector mass; Baryon octet and decuplet quantum-number organization; Chiral Lagrangian derivative expansion; Chiral power counting and axial pion coupling; Consequences of discrete, global, and gauged breaking; Gauged nonlinear sigma model and unitary-gauge propagator; Gell-Mann–Oakes–Renner relation; Goldstone coset transformations and order parameter; Goldstone current matrix-element normalization; Goldstone shift symmetry, decoupling, and pion current; Goldstone theorem from charged-vacuum degeneracy; Higgs mechanism and Abelian Higgs Lagrangian; Higgs radial mode and renormalizability limit; Landau scalar potential across a critical temperature; Linear sigma model polar fields and massless pion; Two-flavor QCD chiral symmetry and anomaly qualification; Noether charge generates a continuous symmetry; Non-Abelian SO(3) breaking and vector mass matrix; Pion leptonic decay measures Fπ; QCD chiral condensate breaking pattern; Rξ gauge fixing and Faddeev–Popov ghosts; Rξ propagators and gauge-dependent unphysical masses; Spontaneous versus explicit symmetry breaking; SU(2) chiral sigma field and nonlinear pion action; SU(3) baryon multiplets and the eightfold way; SU(3) chiral pseudo-Goldstone octet; SU(5) adjoint breaking to the Standard Model group; Superconducting photon mass and Meissner screening; Type-II vortices and Cooper-pair order parameter; Unitary and Feynman–’t Hooft gauge comparison; Vacuum expectation values and nonlinear Z2 realization; Z2 broken-vacuum expansion is tachyon-free. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-higgs-gauge-shift-and-degree-count`, `schwartz.abelian-higgs-model-and-vector-mass`, `schwartz.baryon-octet-decuplet-quantum-number-diagram`, `schwartz.chiral-lagrangian-derivative-operators`, `schwartz.chiral-power-counting-and-axial-pion-coupling`, `schwartz.discrete-global-gauged-breaking-outcomes`, `schwartz.gauged-nonlinear-sigma-model-and-unitary-propagator`, `schwartz.gell-mann-oakes-renner-relation`, `schwartz.goldstone-coset-transformations-and-order-parameter`, `schwartz.goldstone-current-matrix-element-normalization`, `schwartz.goldstone-shift-symmetry-and-decoupling`, `schwartz.goldstone-theorem-degeneracy-proof`, `schwartz.higgs-mechanism-and-abelian-higgs-lagrangian`, `schwartz.higgs-radial-mode-and-renormalizability-limit`, `schwartz.landau-temperature-dependent-scalar-potential`, `schwartz.linear-sigma-model-polar-fields`, `schwartz.massless-two-flavor-qcd-chiral-symmetry`, `schwartz.noether-charge-generates-continuous-symmetry`, `schwartz.nonabelian-so3-breaking-and-vector-mass-matrix`, `schwartz.pion-leptonic-decay-measures-fpi`, `schwartz.qcd-chiral-condensate-breaking-pattern`, `schwartz.rxi-gauge-fixing-and-faddeev-popov-ghosts`, `schwartz.rxi-propagators-and-gauge-dependent-unphysical-masses`, `schwartz.spontaneous-versus-explicit-breaking`, `schwartz.su2-chiral-sigma-field-and-nonlinear-pions`, `schwartz.su3-baryon-multiplets-and-eightfold-way`, `schwartz.su3-chiral-pseudo-goldstone-octet`, `schwartz.su5-adjoint-breaking-to-standard-model-group`, `schwartz.superconducting-photon-mass-and-meissner-screening`, `schwartz.type-two-vortices-and-cooper-pair-order-parameter`, `schwartz.unitary-and-feynman-thooft-gauge-comparison`, `schwartz.vacuum-expectation-values-and-nonlinear-z2`, `schwartz.z2-broken-vacuum-expansion`.

</details>

<details>
<summary>Section 28.1 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Landau scalar potential across a critical temperature; Z2 broken-vacuum expansion is tachyon-free. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.landau-temperature-dependent-scalar-potential`, `schwartz.z2-broken-vacuum-expansion`.

</details>

<details>
<summary>Section 28.2 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Baryon octet and decuplet quantum-number organization; Chiral Lagrangian derivative expansion; Chiral power counting and axial pion coupling; Gell-Mann–Oakes–Renner relation; Goldstone coset transformations and order parameter; Goldstone current matrix-element normalization; Goldstone shift symmetry, decoupling, and pion current; Goldstone theorem from charged-vacuum degeneracy; Linear sigma model polar fields and massless pion; Two-flavor QCD chiral symmetry and anomaly qualification; Noether charge generates a continuous symmetry; Pion leptonic decay measures Fπ; QCD chiral condensate breaking pattern; SU(2) chiral sigma field and nonlinear pion action; SU(3) baryon multiplets and the eightfold way; SU(3) chiral pseudo-Goldstone octet; Vacuum expectation values and nonlinear Z2 realization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.baryon-octet-decuplet-quantum-number-diagram`, `schwartz.chiral-lagrangian-derivative-operators`, `schwartz.chiral-power-counting-and-axial-pion-coupling`, `schwartz.gell-mann-oakes-renner-relation`, `schwartz.goldstone-coset-transformations-and-order-parameter`, `schwartz.goldstone-current-matrix-element-normalization`, `schwartz.goldstone-shift-symmetry-and-decoupling`, `schwartz.goldstone-theorem-degeneracy-proof`, `schwartz.linear-sigma-model-polar-fields`, `schwartz.massless-two-flavor-qcd-chiral-symmetry`, `schwartz.noether-charge-generates-continuous-symmetry`, `schwartz.pion-leptonic-decay-measures-fpi`, `schwartz.qcd-chiral-condensate-breaking-pattern`, `schwartz.su2-chiral-sigma-field-and-nonlinear-pions`, `schwartz.su3-baryon-multiplets-and-eightfold-way`, `schwartz.su3-chiral-pseudo-goldstone-octet`, `schwartz.vacuum-expectation-values-and-nonlinear-z2`.

</details>

<details>
<summary>Section 28.3 — covered</summary>

The accepted assumption, concept, method, result records substantively represent this section's distinct content: Abelian Higgs gauge shift and degree count; Abelian Higgs model and vector mass; Goldstone coset transformations and order parameter; Higgs mechanism and Abelian Higgs Lagrangian; Higgs radial mode and renormalizability limit; Non-Abelian SO(3) breaking and vector mass matrix; SU(5) adjoint breaking to the Standard Model group; Superconducting photon mass and Meissner screening; Type-II vortices and Cooper-pair order parameter. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-higgs-gauge-shift-and-degree-count`, `schwartz.abelian-higgs-model-and-vector-mass`, `schwartz.goldstone-coset-transformations-and-order-parameter`, `schwartz.higgs-mechanism-and-abelian-higgs-lagrangian`, `schwartz.higgs-radial-mode-and-renormalizability-limit`, `schwartz.nonabelian-so3-breaking-and-vector-mass-matrix`, `schwartz.su5-adjoint-breaking-to-standard-model-group`, `schwartz.superconducting-photon-mass-and-meissner-screening`, `schwartz.type-two-vortices-and-cooper-pair-order-parameter`.

</details>

<details>
<summary>Section 28.4 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Gauged nonlinear sigma model and unitary-gauge propagator; Higgs radial mode and renormalizability limit; Rξ gauge fixing and Faddeev–Popov ghosts; Rξ propagators and gauge-dependent unphysical masses; Unitary and Feynman–’t Hooft gauge comparison. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.gauged-nonlinear-sigma-model-and-unitary-propagator`, `schwartz.higgs-radial-mode-and-renormalizability-limit`, `schwartz.rxi-gauge-fixing-and-faddeev-popov-ghosts`, `schwartz.rxi-propagators-and-gauge-dependent-unphysical-masses`, `schwartz.unitary-and-feynman-thooft-gauge-comparison`.

</details>

<details>
<summary>Section 28.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Task: BCH pion transformations and isospin representation; Task: cubic interactions in the gauged nonlinear sigma model; Task: diagonalize the linear-sigma mass matrix; Task: O(n) scalar symmetries, vacua, and Goldstones; Task: SU(5) adjoint potential extrema and spectra. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-bch-pion-transformation-task`, `schwartz.problem-gauged-nonlinear-sigma-cubic-task`, `schwartz.problem-linear-sigma-mass-matrix-task`, `schwartz.problem-on-scalar-vacua-and-goldstones-task`, `schwartz.problem-su5-adjoint-potential-task`.

</details>

<details>
<summary>Section 29 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Anomalous chiral rotations and theta terms; Biunitary Yukawa diagonalization and mass basis; Charged W bosons and electromagnetic coupling; Chiral-Lagrangian theta vacuum energy; CKM charged-current mixing matrix; CKM phase CP-violation condition; CKM physical parameter count and standard form; CKM unitarity-triangle construction; Dimension-five neutrino mass operator and seesaw matching; Dirac/Majorana neutrino masses and the seesaw; Direct and interference CP violation in kaons; Electric-charge quantization and hypercharge constraint; Electromagnetic charge and neutral-current structure; Electroweak gauge mass relations and self-interactions; Electroweak high- and low-energy descriptions; Electroweak parameter inputs and renormalization-condition qualification; Electroweak theta unphysical and QCD total-derivative limit; Electroweak vev, photon–Z mixing, and normalization; Gauge-diagram cancellation in WZ scattering; GIM cancellation of flavor-changing neutral currents; Goldstone boson equivalence theorem; Goldstone equivalence explicit linear-sigma calculation; Higgs exchange unitarizes longitudinal scattering; Higgs mass and hVV couplings; Jarlskog invariant as unitarity-triangle area; Jarlskog invariant and the full weak-CP condition; Kaon mixing and indirect CP violation; Longitudinal vector high-energy growth; Muon decay rate and the Fermi constant; Muon-lifetime vev and quark charged-current tests; Neutral-current four-Fermi theory and massless-photon limit; Neutrino oscillation observables and mass-squared differences; Partial-wave unitarity and Higgs-mass constraint; Peccei–Quinn axion relaxation and quality limit; PMNS mixing and Majorana phase count; Spontaneous CP breaking as a strong-CP proposal; Standard Model chiral fermion representations; Standard Model Higgs doublet and covariant derivative; Standard Model WWZ and WWZZ vertices; Strong CP ̅θ basis-invariant phase; Theta-induced pion–nucleon coupling and neutron EDM; Tree-level four-Fermi matching; V−A charged weak currents; Weak and strong CP violation distinction; Weyl chirality and broken-phase Dirac notation; Wolfenstein approximation and the three-generation CP condition; Yukawa coefficient-reality CP test; Yukawa commutator basis-invariant CP diagnostic; Yukawa fermion masses and Higgs couplings. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomalous-chiral-rotations-and-theta-terms`, `schwartz.biunitary-yukawa-diagonalization-and-mass-basis`, `schwartz.charged-w-bosons-and-electromagnetic-coupling`, `schwartz.chiral-lagrangian-theta-vacuum-energy`, `schwartz.ckm-charged-current-mixing-matrix`, `schwartz.ckm-phase-cp-violation-condition`, `schwartz.ckm-physical-parameter-count-and-standard-form`, `schwartz.ckm-unitarity-triangle-construction`, `schwartz.dimension-five-neutrino-mass-operator-and-seesaw-matching`, `schwartz.dirac-majorana-neutrino-masses-and-seesaw`, `schwartz.direct-and-interference-cp-violation-in-kaons`, `schwartz.electric-charge-quantization-and-hypercharge-constraint`, `schwartz.electromagnetic-charge-and-neutral-current-structure`, `schwartz.electroweak-gauge-mass-relations-and-self-interactions`, `schwartz.electroweak-high-energy-and-low-energy-scope`, `schwartz.electroweak-parameter-inputs-and-renormalization-condition-qualification`, `schwartz.electroweak-theta-unphysical-and-qcd-total-derivative-limit`, `schwartz.electroweak-vev-photon-z-mixing`, `schwartz.gauge-diagram-cancellation-in-wz-scattering`, `schwartz.gim-cancellation-of-flavor-changing-neutral-currents`, `schwartz.goldstone-boson-equivalence-theorem`, `schwartz.goldstone-equivalence-explicit-linear-sigma-calculation`, `schwartz.higgs-exchange-unitarizes-longitudinal-scattering`, `schwartz.higgs-mass-and-hvv-couplings`, `schwartz.jarlskog-invariant-as-unitarity-triangle-area`, `schwartz.jarlskog-invariant-iff-cp-violation`, `schwartz.kaon-mixing-indirect-cp-violation`, `schwartz.longitudinal-vector-high-energy-growth`, `schwartz.muon-decay-rate-and-fermi-constant`, `schwartz.muon-lifetime-vev-and-quark-charged-current-tests`, `schwartz.neutral-current-four-fermi-theory-and-massless-photon-limit`, `schwartz.neutrino-oscillation-observables-and-mass-squared-differences`, `schwartz.partial-wave-unitarity-higgs-mass-constraint`, `schwartz.peccei-quinn-axion-relaxation-and-quality-limit`, `schwartz.pmns-mixing-and-majorana-phase-count`, `schwartz.spontaneous-cp-breaking-strong-cp-proposal`, `schwartz.standard-model-chiral-fermion-representations`, `schwartz.standard-model-higgs-doublet-and-covariant-derivative`, `schwartz.standard-model-w-w-z-and-w-w-z-z-vertices`, `schwartz.strong-cp-bar-theta-basis-invariant-phase`, `schwartz.theta-induced-pion-nucleon-coupling-and-neutron-edm`, `schwartz.tree-level-four-fermi-matching`, `schwartz.v-minus-a-charged-weak-currents`, `schwartz.weak-and-strong-cp-violation-distinction`, `schwartz.weyl-chirality-and-broken-phase-dirac-notation`, `schwartz.wolfenstein-approximation-and-three-generation-cp-condition`, `schwartz.yukawa-coefficient-reality-cp-test`, `schwartz.yukawa-commutator-basis-invariant-cp-diagnostic`, `schwartz.yukawa-fermion-masses-and-higgs-couplings`.

</details>

<details>
<summary>Section 29.1 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Charged W bosons and electromagnetic coupling; Electroweak gauge mass relations and self-interactions; Electroweak high- and low-energy descriptions; Electroweak vev, photon–Z mixing, and normalization; Higgs mass and hVV couplings; Standard Model Higgs doublet and covariant derivative; Standard Model WWZ and WWZZ vertices. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.charged-w-bosons-and-electromagnetic-coupling`, `schwartz.electroweak-gauge-mass-relations-and-self-interactions`, `schwartz.electroweak-high-energy-and-low-energy-scope`, `schwartz.electroweak-vev-photon-z-mixing`, `schwartz.higgs-mass-and-hvv-couplings`, `schwartz.standard-model-higgs-doublet-and-covariant-derivative`, `schwartz.standard-model-w-w-z-and-w-w-z-z-vertices`.

</details>

<details>
<summary>Section 29.2 — covered</summary>

The accepted assumption, concept, method, result records substantively represent this section's distinct content: Electroweak parameter inputs and renormalization-condition qualification; Gauge-diagram cancellation in WZ scattering; Goldstone boson equivalence theorem; Goldstone equivalence explicit linear-sigma calculation; Higgs exchange unitarizes longitudinal scattering; Longitudinal vector high-energy growth; Partial-wave unitarity and Higgs-mass constraint. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.electroweak-parameter-inputs-and-renormalization-condition-qualification`, `schwartz.gauge-diagram-cancellation-in-wz-scattering`, `schwartz.goldstone-boson-equivalence-theorem`, `schwartz.goldstone-equivalence-explicit-linear-sigma-calculation`, `schwartz.higgs-exchange-unitarizes-longitudinal-scattering`, `schwartz.longitudinal-vector-high-energy-growth`, `schwartz.partial-wave-unitarity-higgs-mass-constraint`.

</details>

<details>
<summary>Section 29.3 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Biunitary Yukawa diagonalization and mass basis; CKM charged-current mixing matrix; CKM physical parameter count and standard form; CKM unitarity-triangle construction; Dimension-five neutrino mass operator and seesaw matching; Dirac/Majorana neutrino masses and the seesaw; Electric-charge quantization and hypercharge constraint; Electromagnetic charge and neutral-current structure; Goldstone boson equivalence theorem; Jarlskog invariant as unitarity-triangle area; Standard Model chiral fermion representations; Weyl chirality and broken-phase Dirac notation; Wolfenstein approximation and the three-generation CP condition; Yukawa fermion masses and Higgs couplings. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.biunitary-yukawa-diagonalization-and-mass-basis`, `schwartz.ckm-charged-current-mixing-matrix`, `schwartz.ckm-physical-parameter-count-and-standard-form`, `schwartz.ckm-unitarity-triangle-construction`, `schwartz.dimension-five-neutrino-mass-operator-and-seesaw-matching`, `schwartz.dirac-majorana-neutrino-masses-and-seesaw`, `schwartz.electric-charge-quantization-and-hypercharge-constraint`, `schwartz.electromagnetic-charge-and-neutral-current-structure`, `schwartz.goldstone-boson-equivalence-theorem`, `schwartz.jarlskog-invariant-as-unitarity-triangle-area`, `schwartz.standard-model-chiral-fermion-representations`, `schwartz.weyl-chirality-and-broken-phase-dirac-notation`, `schwartz.wolfenstein-approximation-and-three-generation-cp-condition`, `schwartz.yukawa-fermion-masses-and-higgs-couplings`.

</details>

<details>
<summary>Section 29.4 — covered</summary>

The accepted representation, result records substantively represent this section's distinct content: Muon decay rate and the Fermi constant; Muon-lifetime vev and quark charged-current tests; Neutral-current four-Fermi theory and massless-photon limit; Neutrino oscillation observables and mass-squared differences; PMNS mixing and Majorana phase count; Tree-level four-Fermi matching; V−A charged weak currents. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.muon-decay-rate-and-fermi-constant`, `schwartz.muon-lifetime-vev-and-quark-charged-current-tests`, `schwartz.neutral-current-four-fermi-theory-and-massless-photon-limit`, `schwartz.neutrino-oscillation-observables-and-mass-squared-differences`, `schwartz.pmns-mixing-and-majorana-phase-count`, `schwartz.tree-level-four-fermi-matching`, `schwartz.v-minus-a-charged-weak-currents`.

</details>

<details>
<summary>Section 29.5 — covered</summary>

The accepted assumption, concept, result records substantively represent this section's distinct content: Anomalous chiral rotations and theta terms; Chiral-Lagrangian theta vacuum energy; CKM phase CP-violation condition; Direct and interference CP violation in kaons; Electroweak theta unphysical and QCD total-derivative limit; GIM cancellation of flavor-changing neutral currents; Jarlskog invariant and the full weak-CP condition; Kaon mixing and indirect CP violation; Peccei–Quinn axion relaxation and quality limit; Spontaneous CP breaking as a strong-CP proposal; Strong CP ̅θ basis-invariant phase; Theta-induced pion–nucleon coupling and neutron EDM; Weak and strong CP violation distinction; Yukawa coefficient-reality CP test; Yukawa commutator basis-invariant CP diagnostic. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomalous-chiral-rotations-and-theta-terms`, `schwartz.chiral-lagrangian-theta-vacuum-energy`, `schwartz.ckm-phase-cp-violation-condition`, `schwartz.direct-and-interference-cp-violation-in-kaons`, `schwartz.electroweak-theta-unphysical-and-qcd-total-derivative-limit`, `schwartz.gim-cancellation-of-flavor-changing-neutral-currents`, `schwartz.jarlskog-invariant-iff-cp-violation`, `schwartz.kaon-mixing-indirect-cp-violation`, `schwartz.peccei-quinn-axion-relaxation-and-quality-limit`, `schwartz.spontaneous-cp-breaking-strong-cp-proposal`, `schwartz.strong-cp-bar-theta-basis-invariant-phase`, `schwartz.theta-induced-pion-nucleon-coupling-and-neutron-edm`, `schwartz.weak-and-strong-cp-violation-distinction`, `schwartz.yukawa-coefficient-reality-cp-test`, `schwartz.yukawa-commutator-basis-invariant-cp-diagnostic`.

</details>

<details>
<summary>Section 29.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Task: CKM-fit constraint curves; Task: e+e−→hadrons through photon/Z including interference; Task: Higgs decay rates and branching-ratio plots; Task: integrate out right-handed neutrinos; Task: LEP Higgsstrahlung cross section and event yield; Task: longitudinal WW partial-wave unitarity; Task: multigeneration chiral theta shift; Task: solar/reaction neutrino oscillation probability and baseline; Task: PMNS phase counting for Dirac and Majorana masses; Standard Model CP summary and baryogenesis limit. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-ckm-fit-constraint-curves-task`, `schwartz.problem-ee-hadrons-photon-z-interference-task`, `schwartz.problem-higgs-decay-rates-and-branching-plots-task`, `schwartz.problem-integrating-out-right-handed-neutrinos-task`, `schwartz.problem-lep-higgsstrahlung-cross-section-task`, `schwartz.problem-longitudinal-ww-partial-wave-unitarity-task`, `schwartz.problem-multigeneration-chiral-theta-shift-task`, `schwartz.problem-neutrino-oscillation-probability-and-baseline-task`, `schwartz.problem-pmns-dirac-majorana-phase-count-task`, `schwartz.standard-model-cp-summary-and-baryogenesis-limit`.

</details>

<details>
<summary>Section 30 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Abelian chiral anomaly and one-loop exactness; Anomaly-allowed B minus L; Anomaly solutions and charge quantization; Infrared anomaly matching and trace-anomaly scope; Background-field axial anomaly; Baryon/lepton anomalies and sphalerons; Classical vector and axial currents in QED; Fujikawa measure-Jacobian method; Gauge-invariant Fujikawa regulator; Linearly divergent shift surface term; Massive-fermion pseudoscalar triangle amplitude; Massless triangle as a current correlator; Non-Abelian anomaly coefficient; pi0 diphoton decay measures color; Chiral pion–nucleon coupling and pi0 width; Pion anomaly-matching term; Pseudoscalar diphoton width; Quantum anomaly: gauge versus global consistency; Routing chooses vector-current conservation; Sakharov conditions and Standard-Model limit; Single-Weyl QED gauge anomaly; Standard Model mixed and gravitational cancellation; Standard Model U(1)_Y cubed condition; Strong-CP anomalous rotation relation; SU(3) chiral breaking from matching; t Hooft anomaly-matching hypotheses; U(1) problem: axial U(1) is not a symmetry; Witten–Veneziano topological susceptibility. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-chiral-anomaly-and-one-loop-exactness`, `schwartz.anomaly-allowed-b-minus-l`, `schwartz.anomaly-hypercharge-solutions-and-charge-quantization`, `schwartz.anomaly-ir-matching-and-trace-scope`, `schwartz.background-field-axial-anomaly`, `schwartz.baryon-lepton-anomalies-and-sphaleron-scope`, `schwartz.classical-vector-axial-currents`, `schwartz.fujikawa-measure-jacobian-method`, `schwartz.gauge-invariant-fujikawa-regulator`, `schwartz.linearly-divergent-shift-surface-term`, `schwartz.massive-pseudoscalar-triangle-amplitude`, `schwartz.massless-triangle-current-correlator`, `schwartz.nonabelian-anomaly-coefficient-and-divergence`, `schwartz.pi0-diphoton-color-measurement`, `schwartz.pion-nucleon-chiral-coupling-and-width`, `schwartz.pion-wess-zumino-anomaly-matching-term`, `schwartz.pseudoscalar-diphoton-width`, `schwartz.quantum-anomaly-gauge-versus-global-consistency`, `schwartz.routing-choice-preserves-vector-ward-identity`, `schwartz.sakharov-conditions-and-standard-model-baryogenesis-limit`, `schwartz.single-weyl-qed-gauge-anomaly`, `schwartz.standard-model-mixed-and-gravitational-anomaly-cancellation`, `schwartz.standard-model-u1-cubed-anomaly-condition`, `schwartz.strong-cp-anomalous-rotation-relation`, `schwartz.su3-chiral-breaking-from-anomaly-matching`, `schwartz.thooft-anomaly-matching-hypotheses`, `schwartz.u1-problem-axial-u1-not-a-symmetry`, `schwartz.witten-veneziano-topological-susceptibility`.

</details>

<details>
<summary>Section 30.1 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Infrared anomaly matching and trace-anomaly scope; Background-field axial anomaly; Classical vector and axial currents in QED; Massive-fermion pseudoscalar triangle amplitude; pi0 diphoton decay measures color; Chiral pion–nucleon coupling and pi0 width; Pseudoscalar diphoton width. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomaly-ir-matching-and-trace-scope`, `schwartz.background-field-axial-anomaly`, `schwartz.classical-vector-axial-currents`, `schwartz.massive-pseudoscalar-triangle-amplitude`, `schwartz.pi0-diphoton-color-measurement`, `schwartz.pion-nucleon-chiral-coupling-and-width`, `schwartz.pseudoscalar-diphoton-width`.

</details>

<details>
<summary>Section 30.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Linearly divergent shift surface term; Massless triangle as a current correlator; Routing chooses vector-current conservation; Single-Weyl QED gauge anomaly. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.linearly-divergent-shift-surface-term`, `schwartz.massless-triangle-current-correlator`, `schwartz.routing-choice-preserves-vector-ward-identity`, `schwartz.single-weyl-qed-gauge-anomaly`.

</details>

<details>
<summary>Section 30.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Abelian chiral anomaly and one-loop exactness; Fujikawa measure-Jacobian method; Gauge-invariant Fujikawa regulator. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-chiral-anomaly-and-one-loop-exactness`, `schwartz.fujikawa-measure-jacobian-method`, `schwartz.gauge-invariant-fujikawa-regulator`.

</details>

<details>
<summary>Section 30.4 — covered</summary>

The accepted result records substantively represent this section's distinct content: Abelian chiral anomaly and one-loop exactness; Anomaly-allowed B minus L; Anomaly solutions and charge quantization; Non-Abelian anomaly coefficient; Standard Model mixed and gravitational cancellation; Standard Model U(1)_Y cubed condition. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.abelian-chiral-anomaly-and-one-loop-exactness`, `schwartz.anomaly-allowed-b-minus-l`, `schwartz.anomaly-hypercharge-solutions-and-charge-quantization`, `schwartz.nonabelian-anomaly-coefficient-and-divergence`, `schwartz.standard-model-mixed-and-gravitational-anomaly-cancellation`, `schwartz.standard-model-u1-cubed-anomaly-condition`.

</details>

<details>
<summary>Section 30.5 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Anomaly-allowed B minus L; Anomaly solutions and charge quantization; Baryon/lepton anomalies and sphalerons; Sakharov conditions and Standard-Model limit; Strong-CP anomalous rotation relation; U(1) problem: axial U(1) is not a symmetry; Witten–Veneziano topological susceptibility. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.anomaly-allowed-b-minus-l`, `schwartz.anomaly-hypercharge-solutions-and-charge-quantization`, `schwartz.baryon-lepton-anomalies-and-sphaleron-scope`, `schwartz.sakharov-conditions-and-standard-model-baryogenesis-limit`, `schwartz.strong-cp-anomalous-rotation-relation`, `schwartz.u1-problem-axial-u1-not-a-symmetry`, `schwartz.witten-veneziano-topological-susceptibility`.

</details>

<details>
<summary>Section 30.6 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: Pion anomaly-matching term; SU(3) chiral breaking from matching; t Hooft anomaly-matching hypotheses; Witten–Veneziano topological susceptibility. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.pion-wess-zumino-anomaly-matching-term`, `schwartz.su3-chiral-breaking-from-anomaly-matching`, `schwartz.thooft-anomaly-matching-hypotheses`, `schwartz.witten-veneziano-topological-susceptibility`.

</details>

<details>
<summary>Section 30.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem 30.1: non-Abelian baryon anomaly; Problem 30.2: neutrino masses and B-L; Problem 30.3: SU(5)-color universe; Problem 30.4: SU(4) chiral matching; Seiberg-duality matching is evidence; SU(3) chiral breaking from matching. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-30-1-nonabelian-baryon-anomaly-diagrams`, `schwartz.problem-30-2-neutrino-mass-bminusl-anomaly`, `schwartz.problem-30-3-su5-color-anomaly-free-sm`, `schwartz.problem-30-4-su4-chiral-matching`, `schwartz.seiberg-duality-anomaly-matching-evidence-limit`, `schwartz.su3-chiral-breaking-from-anomaly-matching`.

</details>

<details>
<summary>Section 31 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Chiral fermion vacuum-polarization integrals; CKM unitarity cancels oblique divergences; Color/Fierz reduction in matching; Custodial SU(2) and rho; Custodial symmetry as current equality; Delta rho from doublet splitting; Effective charge matching; Fiducial scheme and tree-level tension; Eigenoperators and leading-log running; Four-Fermi operator-mixing RGE; Leading top/Higgs oblique dependence; IR cancellation consistency test; Muon-decay Fermi matching; New doublet S,T constraints; Oblique-correction strategy; Oblique inversion and m_W prediction; Off-shell matching IR artifact; Peskin–Takeuchi S,T,U; Pole mass from transverse self energy; Precision electroweak input observables; QCD running impact on Vcb; SMEFT shortcut for S,T; Dirac-neutrino Standard Model parameter count and testability; Technicolor application of the S constraint; Top–bottom oblique self energies; Top MS mass and one-loop predictions; Tree b to c ubar d matching; Tree-level electroweak formulas; Two-operator matching coefficients; Vcb extraction and large logarithm; Standard weak effective-Hamiltonian basis; Weak EFT locality and suppression; Z–photon mixing and A_e. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-fermion-vacuum-polarization-integrals`, `schwartz.ckm-unitarity-cancels-oblique-divergences`, `schwartz.color-fierz-reduction-in-weak-matching`, `schwartz.custodial-su2-and-rho-tree-relation`, `schwartz.custodial-symmetry-as-current-strength-equality`, `schwartz.delta-rho-doublet-mass-splitting`, `schwartz.effective-charge-vacuum-polarization-matching`, `schwartz.fiducial-input-scheme-and-tree-level-tension`, `schwartz.four-fermi-eigenoperators-and-leading-log-running`, `schwartz.four-fermi-operator-mixing-rge`, `schwartz.leading-top-and-higgs-oblique-dependence`, `schwartz.matching-ir-cancellation-consistency-test`, `schwartz.muon-decay-fermi-constant-oblique-matching`, `schwartz.new-fermion-doublet-stu-constraints`, `schwartz.oblique-corrections-strategy-and-scope`, `schwartz.oblique-inversion-and-mw-prediction`, `schwartz.off-shell-one-loop-matching-ir-artifact`, `schwartz.peskin-takeuchi-stu-definitions-and-reference`, `schwartz.pole-mass-self-energy-relation`, `schwartz.precision-electroweak-input-observables`, `schwartz.qcd-running-impact-on-vcb`, `schwartz.smeft-oblique-operator-shortcut`, `schwartz.standard-model-parameter-count-and-overconstraint`, `schwartz.technicolor-s-parameter-constraint`, `schwartz.top-bottom-oblique-self-energies`, `schwartz.top-ms-mass-and-one-loop-precision-prediction`, `schwartz.tree-level-b-to-cud-four-fermi-matching`, `schwartz.tree-level-electroweak-observable-formulas`, `schwartz.two-operator-b-to-cud-matching-coefficients`, `schwartz.vcb-hadronic-extraction-and-large-log-problem`, `schwartz.weak-effective-hamiltonian-standard-basis`, `schwartz.weak-effective-lagrangian-locality-and-power-suppression`, `schwartz.zgamma-mixing-effective-angle-and-ae`.

</details>

<details>
<summary>Section 31.1 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Chiral fermion vacuum-polarization integrals; CKM unitarity cancels oblique divergences; Effective charge matching; Fiducial scheme and tree-level tension; Muon-decay Fermi matching; Oblique-correction strategy; Oblique inversion and m_W prediction; Pole mass from transverse self energy; Precision electroweak input observables; Top–bottom oblique self energies; Top MS mass and one-loop predictions; Tree-level electroweak formulas; Z–photon mixing and A_e. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.chiral-fermion-vacuum-polarization-integrals`, `schwartz.ckm-unitarity-cancels-oblique-divergences`, `schwartz.effective-charge-vacuum-polarization-matching`, `schwartz.fiducial-input-scheme-and-tree-level-tension`, `schwartz.muon-decay-fermi-constant-oblique-matching`, `schwartz.oblique-corrections-strategy-and-scope`, `schwartz.oblique-inversion-and-mw-prediction`, `schwartz.pole-mass-self-energy-relation`, `schwartz.precision-electroweak-input-observables`, `schwartz.top-bottom-oblique-self-energies`, `schwartz.top-ms-mass-and-one-loop-precision-prediction`, `schwartz.tree-level-electroweak-observable-formulas`, `schwartz.zgamma-mixing-effective-angle-and-ae`.

</details>

<details>
<summary>Section 31.2 — covered</summary>

The accepted concept, result records substantively represent this section's distinct content: Custodial SU(2) and rho; Custodial symmetry as current equality; Delta rho from doublet splitting; Leading top/Higgs oblique dependence; Peskin–Takeuchi S,T,U. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.custodial-su2-and-rho-tree-relation`, `schwartz.custodial-symmetry-as-current-strength-equality`, `schwartz.delta-rho-doublet-mass-splitting`, `schwartz.leading-top-and-higgs-oblique-dependence`, `schwartz.peskin-takeuchi-stu-definitions-and-reference`.

</details>

<details>
<summary>Section 31.3 — covered</summary>

The accepted assumption, concept, method, result records substantively represent this section's distinct content: Color/Fierz reduction in matching; Eigenoperators and leading-log running; Four-Fermi operator-mixing RGE; IR cancellation consistency test; New doublet S,T constraints; Off-shell matching IR artifact; QCD running impact on Vcb; SMEFT shortcut for S,T; Technicolor application of the S constraint; Tree b to c ubar d matching; Two-operator matching coefficients; Vcb extraction and large logarithm; Standard weak effective-Hamiltonian basis; Weak EFT locality and suppression. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.color-fierz-reduction-in-weak-matching`, `schwartz.four-fermi-eigenoperators-and-leading-log-running`, `schwartz.four-fermi-operator-mixing-rge`, `schwartz.matching-ir-cancellation-consistency-test`, `schwartz.new-fermion-doublet-stu-constraints`, `schwartz.off-shell-one-loop-matching-ir-artifact`, `schwartz.qcd-running-impact-on-vcb`, `schwartz.smeft-oblique-operator-shortcut`, `schwartz.technicolor-s-parameter-constraint`, `schwartz.tree-level-b-to-cud-four-fermi-matching`, `schwartz.two-operator-b-to-cud-matching-coefficients`, `schwartz.vcb-hadronic-extraction-and-large-log-problem`, `schwartz.weak-effective-hamiltonian-standard-basis`, `schwartz.weak-effective-lagrangian-locality-and-power-suppression`.

</details>

<details>
<summary>Section 31.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem 31.1: muon decay; Problem 31.2(a): tree Z width; Problem 31.2(b): MS Z width; Problem 31.2(c): Z width from polarizations; Problem 31.2(d): numerical one-loop Z width; Problem 31.3: Higgs polarizations; Problem 31.4(a): b to s gamma; Problem 31.4(b): b to s gamma matching; Problem 31.4(c): b to s gamma QCD; Problem 31.4(d): b to s gamma running; Standard weak effective-Hamiltonian basis. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-31-1-muon-four-fermi-width`, `schwartz.problem-31-2a-zwidth-tree`, `schwartz.problem-31-2b-zwidth-ms`, `schwartz.problem-31-2c-zwidth-vacpol`, `schwartz.problem-31-2d-zwidth-numeric`, `schwartz.problem-31-3-higgs-vacuum-polarizations`, `schwartz.problem-31-4a-bsgamma-rate`, `schwartz.problem-31-4b-bsgamma-match`, `schwartz.problem-31-4c-bsgamma-qcd`, `schwartz.problem-31-4d-bsgamma-running`, `schwartz.weak-effective-hamiltonian-standard-basis`.

</details>

<details>
<summary>Section 32 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Bjorken scaling and the Callan–Gross relation; Breit frame and lightcone momentum decomposition; Universal quark–gluon collinear splitting; Coupled quark–gluon DGLAP system; PDF renormalization and DGLAP evolution; DIS analytic-contour route to OPE moments; DIS current product and forward Compton amplitude; Leading-power DIS matching from forward Compton scattering to local operators; DIS hadronic tensor and structure functions; DIS parton model and Bjorken x; DIS PDF scheme limitation; DIS twist-two operator basis and power counting; Gamma-star quark collinear residue derivation; Gauge-invariant lightcone PDF operator; Lightcone factorization scaling route and limit; Operator product expansion and state-independent coefficients; Parton distributions and the DIS convolution; Parton shower and Sudakov construction; Partonic DIS convolution and leading-order Callan–Gross check; PDF flavor and momentum sum rules; PDF Mellin moments and energy–momentum sum rule; PDFs as twist-two operator moments; Plus distributions for collinear endpoints; Proton elastic form factors and the Rosenbluth cross section; QCD factorization theorem and proof scope; QCD prediction of hadrons and the perturbative limit; Quark DGLAP kernel and scaling violation; Rutherford scattering as a structural probe and nuclear-size bound. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bjorken-scaling-and-callan-gross-relation`, `schwartz.breit-frame-lightcone-momentum-decomposition`, `schwartz.collinear-splitting-universality`, `schwartz.coupled-quark-gluon-dglap-system`, `schwartz.dglap-pdf-renormalization-and-evolution`, `schwartz.dis-analytic-contour-moment-route`, `schwartz.dis-current-product-and-forward-compton-amplitude`, `schwartz.dis-forward-compton-leading-power-operator-matching`, `schwartz.dis-hadronic-tensor-and-structure-functions`, `schwartz.dis-parton-model-and-bjorken-x`, `schwartz.dis-pdf-scheme-limit`, `schwartz.dis-twist-two-operator-basis-and-power-counting`, `schwartz.gamma-star-quark-collinear-residue-derivation`, `schwartz.gauge-invariant-lightcone-pdf-operator`, `schwartz.lightcone-factorization-scaling-route-and-limit`, `schwartz.operator-product-expansion-state-independent-coefficients`, `schwartz.parton-distribution-convolution`, `schwartz.parton-shower-sudakov-construction`, `schwartz.partonic-dis-convolution-and-lo-callan-gross`, `schwartz.pdf-flavor-and-momentum-sum-rules`, `schwartz.pdf-mellin-moments-and-energy-momentum-sum-rule`, `schwartz.pdfs-as-twist-two-operator-moments`, `schwartz.plus-distribution-for-collinear-endpoints`, `schwartz.proton-elastic-form-factors-and-rosenbluth-cross-section`, `schwartz.qcd-factorization-theorem-and-proof-scope`, `schwartz.qcd-hadron-prediction-and-perturbative-limit`, `schwartz.quark-dglap-splitting-kernel-and-scaling-violation`, `schwartz.rutherford-structural-probe-and-nuclear-size-bound`.

</details>

<details>
<summary>Section 32.1 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Bjorken scaling and the Callan–Gross relation; DIS hadronic tensor and structure functions; DIS parton model and Bjorken x; Parton distributions and the DIS convolution; PDF flavor and momentum sum rules; Proton elastic form factors and the Rosenbluth cross section; Rutherford scattering as a structural probe and nuclear-size bound. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.bjorken-scaling-and-callan-gross-relation`, `schwartz.dis-hadronic-tensor-and-structure-functions`, `schwartz.dis-parton-model-and-bjorken-x`, `schwartz.parton-distribution-convolution`, `schwartz.pdf-flavor-and-momentum-sum-rules`, `schwartz.proton-elastic-form-factors-and-rosenbluth-cross-section`, `schwartz.rutherford-structural-probe-and-nuclear-size-bound`.

</details>

<details>
<summary>Section 32.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Coupled quark–gluon DGLAP system; PDF renormalization and DGLAP evolution; Partonic DIS convolution and leading-order Callan–Gross check; Plus distributions for collinear endpoints; Quark DGLAP kernel and scaling violation. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.coupled-quark-gluon-dglap-system`, `schwartz.dglap-pdf-renormalization-and-evolution`, `schwartz.partonic-dis-convolution-and-lo-callan-gross`, `schwartz.plus-distribution-for-collinear-endpoints`, `schwartz.quark-dglap-splitting-kernel-and-scaling-violation`.

</details>

<details>
<summary>Section 32.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Universal quark–gluon collinear splitting; Coupled quark–gluon DGLAP system; Gamma-star quark collinear residue derivation; Parton shower and Sudakov construction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.collinear-splitting-universality`, `schwartz.coupled-quark-gluon-dglap-system`, `schwartz.gamma-star-quark-collinear-residue-derivation`, `schwartz.parton-shower-sudakov-construction`.

</details>

<details>
<summary>Section 32.4 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: DIS analytic-contour route to OPE moments; DIS current product and forward Compton amplitude; Leading-power DIS matching from forward Compton scattering to local operators; DIS twist-two operator basis and power counting; Operator product expansion and state-independent coefficients; PDF Mellin moments and energy–momentum sum rule; PDFs as twist-two operator moments; QCD factorization theorem and proof scope. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.dis-analytic-contour-moment-route`, `schwartz.dis-current-product-and-forward-compton-amplitude`, `schwartz.dis-forward-compton-leading-power-operator-matching`, `schwartz.dis-twist-two-operator-basis-and-power-counting`, `schwartz.operator-product-expansion-state-independent-coefficients`, `schwartz.pdf-mellin-moments-and-energy-momentum-sum-rule`, `schwartz.pdfs-as-twist-two-operator-moments`, `schwartz.qcd-factorization-theorem-and-proof-scope`.

</details>

<details>
<summary>Section 32.5 — covered</summary>

The accepted assumption, representation records substantively represent this section's distinct content: Breit frame and lightcone momentum decomposition; DIS PDF scheme limitation; Gauge-invariant lightcone PDF operator; Lightcone factorization scaling route and limit. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.breit-frame-lightcone-momentum-decomposition`, `schwartz.dis-pdf-scheme-limit`, `schwartz.gauge-invariant-lightcone-pdf-operator`, `schwartz.lightcone-factorization-scaling-route-and-limit`.

</details>

<details>
<summary>Section 32.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem: charge radius from a form factor; Problem: collinear transverse-momentum check; Problem: DIS lightcone dominance; Problem: forward-Compton discontinuity; Problem: flavor-current moment sum rule; Problem: g→gg splitting from collinear scattering; Problem: lightcone PDF–Mellin relation; Problem: PDF momentum sum rule; Problem: derive the plus-distribution expansion; Problem: scalar-parton alternative to Callan–Gross; Problem: Sudakov limits for pT², mass, and angle. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-charge-radius-from-form-factor`, `schwartz.problem-collinear-transverse-momentum-check`, `schwartz.problem-dis-lightcone-dominance`, `schwartz.problem-discontinuity-optical-theorem`, `schwartz.problem-flavor-current-moment-sum-rule`, `schwartz.problem-gluon-splitting-from-collinear-gg-scattering`, `schwartz.problem-lightcone-pdf-mellin-relation`, `schwartz.problem-pdf-momentum-sum-rule`, `schwartz.problem-plus-distribution-expansion`, `schwartz.problem-scalar-parton-callan-gross-test`, `schwartz.problem-sudakov-variable-limits-and-universality`.

</details>

<details>
<summary>Section 33 — covered</summary>

The accepted concept, method, representation, result records substantively represent this section's distinct content: Background-field scalar and spinor proper-time propagators; Scalar and pseudoscalar background currents and two-photon decays; Closed proper-time loops and regulated vacuum energy; Effective action: matching observables with changed degrees of freedom; Euler–Heisenberg action from constant electromagnetic fields; Low-energy light-by-light scattering from Euler–Heisenberg terms; One-loop QED beta function from Euler–Heisenberg vacuum polarization; Renormalized Euler–Heisenberg Lagrangian and its scope; Exact matter effective action and sewing of effective vertices; Field-dependent currents from proper time; Functional determinants for integrated scalar and fermion fields; Heavy-particle semiclassical classical-source limit; Heavy-scalar matching and local derivative expansion; Nonrelativistic quantum mechanics from the worldline limit; Proper-time background axial-anomaly sign discrepancy; Proper-time composition and complementary Feynman fractions; Schwinger constant-field kernel from Heisenberg evolution; Schwinger pair production from the effective-action imaginary part; Schwinger proper-time representation of a propagator; Worldline path integral for a charged scalar propagator. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.background-field-scalar-and-spinor-proper-time-propagators`, `schwartz.background-scalar-pseudoscalar-currents-and-decays`, `schwartz.closed-proper-time-loops-and-vacuum-energy`, `schwartz.effective-action-definition-and-scope`, `schwartz.euler-heisenberg-constant-field-action`, `schwartz.euler-heisenberg-low-energy-light-by-light-scattering`, `schwartz.euler-heisenberg-qed-beta-function`, `schwartz.euler-heisenberg-renormalization-and-nonperturbative-scope`, `schwartz.exact-matter-effective-action-and-effective-vertex-sewing`, `schwartz.field-dependent-current-effective-action`, `schwartz.functional-determinants-from-integrating-out-matter`, `schwartz.heavy-particle-semiclassical-source-limit`, `schwartz.matching-heavy-scalar-local-operator-expansion`, `schwartz.nonrelativistic-quantum-mechanics-worldline-limit`, `schwartz.proper-time-background-axial-anomaly-route`, `schwartz.proper-time-feynman-parameter-composition`, `schwartz.schwinger-constant-field-kernel-method`, `schwartz.schwinger-pair-production-rate-and-limit`, `schwartz.schwinger-proper-time-propagator-representation`, `schwartz.worldline-path-integral-for-background-propagation`.

</details>

<details>
<summary>Section 33.1 — covered</summary>

The accepted method records substantively represent this section's distinct content: Heavy-scalar matching and local derivative expansion. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.matching-heavy-scalar-local-operator-expansion`.

</details>

<details>
<summary>Section 33.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Background-field scalar and spinor proper-time propagators; Closed proper-time loops and regulated vacuum energy; Field-dependent currents from proper time; Heavy-scalar matching and local derivative expansion; Proper-time composition and complementary Feynman fractions; Schwinger proper-time representation of a propagator. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.background-field-scalar-and-spinor-proper-time-propagators`, `schwartz.closed-proper-time-loops-and-vacuum-energy`, `schwartz.field-dependent-current-effective-action`, `schwartz.matching-heavy-scalar-local-operator-expansion`, `schwartz.proper-time-feynman-parameter-composition`, `schwartz.schwinger-proper-time-propagator-representation`.

</details>

<details>
<summary>Section 33.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Closed proper-time loops and regulated vacuum energy; Functional determinants for integrated scalar and fermion fields. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.closed-proper-time-loops-and-vacuum-energy`, `schwartz.functional-determinants-from-integrating-out-matter`.

</details>

<details>
<summary>Section 33.4 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Euler–Heisenberg action from constant electromagnetic fields; Low-energy light-by-light scattering from Euler–Heisenberg terms; One-loop QED beta function from Euler–Heisenberg vacuum polarization; Renormalized Euler–Heisenberg Lagrangian and its scope; Exact matter effective action and sewing of effective vertices; Functional determinants for integrated scalar and fermion fields; Schwinger pair production from the effective-action imaginary part. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.euler-heisenberg-constant-field-action`, `schwartz.euler-heisenberg-low-energy-light-by-light-scattering`, `schwartz.euler-heisenberg-qed-beta-function`, `schwartz.euler-heisenberg-renormalization-and-nonperturbative-scope`, `schwartz.exact-matter-effective-action-and-effective-vertex-sewing`, `schwartz.functional-determinants-from-integrating-out-matter`, `schwartz.schwinger-pair-production-rate-and-limit`.

</details>

<details>
<summary>Section 33.5 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: Scalar and pseudoscalar background currents and two-photon decays; Renormalized Euler–Heisenberg Lagrangian and its scope; Exact matter effective action and sewing of effective vertices; Proper-time background axial-anomaly sign discrepancy. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.background-scalar-pseudoscalar-currents-and-decays`, `schwartz.euler-heisenberg-renormalization-and-nonperturbative-scope`, `schwartz.exact-matter-effective-action-and-effective-vertex-sewing`, `schwartz.proper-time-background-axial-anomaly-route`.

</details>

<details>
<summary>Section 33.6 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Heavy-particle semiclassical classical-source limit; Nonrelativistic quantum mechanics from the worldline limit; Proper-time background axial-anomaly sign discrepancy; Worldline path integral for a charged scalar propagator. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.heavy-particle-semiclassical-source-limit`, `schwartz.nonrelativistic-quantum-mechanics-worldline-limit`, `schwartz.proper-time-background-axial-anomaly-route`, `schwartz.worldline-path-integral-for-background-propagation`.

</details>

<details>
<summary>Section 33.A — covered</summary>

The accepted method records substantively represent this section's distinct content: Schwinger constant-field kernel from Heisenberg evolution. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.schwinger-constant-field-kernel-method`.

</details>

<details>
<summary>Section 33.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem 33.1: general-field Euler–Heisenberg Landau-level derivation; Problem 33.2: helicity-spinor light-by-light calculation; Problem 33.3: contour derivation of pair production; Problem 33.4: fermion semiclassical and nonrelativistic limit; Problem 33.5: constant field-strength eigenvalues; Schwinger constant-field kernel from Heisenberg evolution. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-33-1-general-field-euler-heisenberg`, `schwartz.problem-33-2-light-by-light-helicity-calculation`, `schwartz.problem-33-3-pair-production-contour-integral`, `schwartz.problem-33-4-fermion-semiclassical-spin-limit`, `schwartz.problem-33-5-field-strength-eigenvalues`, `schwartz.schwinger-constant-field-kernel-method`.

</details>

<details>
<summary>Section 34 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: 1PI action minimum and inverse two-point function; Gauge-dependent background effective action and on-shell equivalence; Background-field identity and tadpole subtraction; Background-field one-loop QCD beta function from ghost and gluon loops; Background-field renormalization and beta extraction; Coleman–Weinberg leading-log resummation; Coleman–Weinberg potential and its large-log limit; General one-loop species contribution to an effective potential; Higgs effective potential and source-era stability analysis; Legendre transform of W[J] as the 1PI action; Non-Abelian background-field gauge construction; One-loop scalar effective potential from a constant background; 1PI effective action and tree-level reconstruction; Scalar-QED effective-potential gauge dependence and physical mass ratio. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.1pi-action-vacuum-minimum-and-inverse-two-point-function`, `schwartz.background-effective-action-gauge-dependence-onshell-equivalence`, `schwartz.background-field-identity-and-tadpole-subtraction`, `schwartz.background-field-qcd-one-loop-beta-graph-result`, `schwartz.background-field-renormalization-and-beta-extraction`, `schwartz.coleman-weinberg-leading-log-resummation`, `schwartz.coleman-weinberg-potential-and-large-log-limit`, `schwartz.general-one-loop-species-effective-potential`, `schwartz.higgs-effective-potential-stability-source-era-analysis`, `schwartz.legendre-transform-connected-functional-and-1pi-action`, `schwartz.nonabelian-background-field-gauge-construction`, `schwartz.one-loop-constant-background-scalar-effective-potential`, `schwartz.one-particle-irreducible-effective-action`, `schwartz.scalar-qed-coleman-weinberg-gauge-dependence-and-mass-ratio`.

</details>

<details>
<summary>Section 34.1 — covered</summary>

The accepted concept, method, result records substantively represent this section's distinct content: 1PI action minimum and inverse two-point function; Background-field identity and tadpole subtraction; Legendre transform of W[J] as the 1PI action; 1PI effective action and tree-level reconstruction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.1pi-action-vacuum-minimum-and-inverse-two-point-function`, `schwartz.background-field-identity-and-tadpole-subtraction`, `schwartz.legendre-transform-connected-functional-and-1pi-action`, `schwartz.one-particle-irreducible-effective-action`.

</details>

<details>
<summary>Section 34.2 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Background-field identity and tadpole subtraction; Coleman–Weinberg leading-log resummation; Coleman–Weinberg potential and its large-log limit; General one-loop species contribution to an effective potential; Higgs effective potential and source-era stability analysis; One-loop scalar effective potential from a constant background; Scalar-QED effective-potential gauge dependence and physical mass ratio. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.background-field-identity-and-tadpole-subtraction`, `schwartz.coleman-weinberg-leading-log-resummation`, `schwartz.coleman-weinberg-potential-and-large-log-limit`, `schwartz.general-one-loop-species-effective-potential`, `schwartz.higgs-effective-potential-stability-source-era-analysis`, `schwartz.one-loop-constant-background-scalar-effective-potential`, `schwartz.scalar-qed-coleman-weinberg-gauge-dependence-and-mass-ratio`.

</details>

<details>
<summary>Section 34.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Gauge-dependent background effective action and on-shell equivalence; Background-field one-loop QCD beta function from ghost and gluon loops; Background-field renormalization and beta extraction; Non-Abelian background-field gauge construction; Scalar-QED effective-potential gauge dependence and physical mass ratio. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.background-effective-action-gauge-dependence-onshell-equivalence`, `schwartz.background-field-qcd-one-loop-beta-graph-result`, `schwartz.background-field-renormalization-and-beta-extraction`, `schwartz.nonabelian-background-field-gauge-construction`, `schwartz.scalar-qed-coleman-weinberg-gauge-dependence-and-mass-ratio`.

</details>

<details>
<summary>Section 34.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Gauge-dependent background effective action and on-shell equivalence; General one-loop species contribution to an effective potential; Problem 34.1: connected correlators from W[J]; Problem 34.2: general one-loop scalar effective potential; Problem 34.3: scalar-QED Coleman–Weinberg potential; Problem 34.4: W and Z contributions to the Higgs potential; Problem 34.5: RG-improved Higgs stability bound; Problem 34.6: background-field A⁴ 1PI vertex; Problem 34.7: fermion contribution to the QCD beta function; Problem 34.8: finite gauge dependence in the background effective action. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.background-effective-action-gauge-dependence-onshell-equivalence`, `schwartz.general-one-loop-species-effective-potential`, `schwartz.problem-34-1-connected-generating-functional`, `schwartz.problem-34-2-general-one-loop-scalar-potential`, `schwartz.problem-34-3-scalar-qed-coleman-weinberg`, `schwartz.problem-34-4-gauge-boson-higgs-potential`, `schwartz.problem-34-5-rg-improved-higgs-stability`, `schwartz.problem-34-6-background-field-a4-vertex`, `schwartz.problem-34-7-background-field-fermion-qcd-beta`, `schwartz.problem-34-8-background-field-finite-gauge-dependence`.

</details>

<details>
<summary>Section 35 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: HQET heavy–light current matching; HQET current anomalous dimension and decay-ratio running; Heavy-quark spin and flavor symmetry; Heavy-scalar EFT and antiparticle removal; Heavy-meson hyperfine mass scaling; Isgur–Wise form factor and zero-recoil V_cb extraction; Leading HQET spinor Lagrangian and rules; Leptonic heavy-meson decay constants; One-loop HQET field and current renormalization; HQET mass corrections from lambda_1 and lambda_2; Integrating out the small component for 1/m_Q HQET; Heavy-quark velocity and residual momentum. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hqet-current-matching-and-large-log`, `schwartz.hqet-current-rge-decay-ratio`, `schwartz.hqet-heavy-quark-limit`, `schwartz.hqet-heavy-scalar-construction`, `schwartz.hqet-hyperfine-mass-scaling`, `schwartz.hqet-isgur-wise-and-vcb`, `schwartz.hqet-leading-lagrangian`, `schwartz.hqet-leptonic-decay-scaling`, `schwartz.hqet-one-loop-renormalization`, `schwartz.hqet-power-correction-mass-parameters`, `schwartz.hqet-subleading-lagrangian`, `schwartz.hqet-velocity-residual-momentum`.

</details>

<details>
<summary>Section 35.1 — covered</summary>

The accepted result records substantively represent this section's distinct content: Isgur–Wise form factor and zero-recoil V_cb extraction; Leptonic heavy-meson decay constants. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hqet-isgur-wise-and-vcb`, `schwartz.hqet-leptonic-decay-scaling`.

</details>

<details>
<summary>Section 35.2 — covered</summary>

The accepted method, representation, result records substantively represent this section's distinct content: Heavy-scalar EFT and antiparticle removal; Isgur–Wise form factor and zero-recoil V_cb extraction; Leading HQET spinor Lagrangian and rules; Heavy-quark velocity and residual momentum. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hqet-heavy-scalar-construction`, `schwartz.hqet-isgur-wise-and-vcb`, `schwartz.hqet-leading-lagrangian`, `schwartz.hqet-velocity-residual-momentum`.

</details>

<details>
<summary>Section 35.3 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: HQET heavy–light current matching; HQET current anomalous dimension and decay-ratio running; One-loop HQET field and current renormalization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hqet-current-matching-and-large-log`, `schwartz.hqet-current-rge-decay-ratio`, `schwartz.hqet-one-loop-renormalization`.

</details>

<details>
<summary>Section 35.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: HQET current anomalous dimension and decay-ratio running; HQET mass corrections from lambda_1 and lambda_2; Integrating out the small component for 1/m_Q HQET. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.hqet-current-rge-decay-ratio`, `schwartz.hqet-power-correction-mass-parameters`, `schwartz.hqet-subleading-lagrangian`.

</details>

<details>
<summary>Section 35.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: HQET mass corrections from lambda_1 and lambda_2; Problem 35.1: reparametrization invariance; Problem 35.2: chromomagnetic anomalous dimension. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.hqet-power-correction-mass-parameters`, `schwartz.problem-35-1-reparametrization-invariance`, `schwartz.problem-35-2-chromomagnetic-anomalous-dimension`.

</details>

<details>
<summary>Section 36 — covered</summary>

The accepted assumption, concept, method, representation, result records substantively represent this section's distinct content: Abelian eikonal identity and soft Wilson lines; Collinear factorization and gauge-invariant jet fields; Dijet thrust hard–jet–soft factorization; Thrust and hemisphere event shapes; RGE resummation of factorized thrust; One-loop SCET hard function; One-loop inclusive jet function; Jet observables and the Sudakov problem; LO thrust distribution, distributions, and dijet singular limit; Non-Abelian soft Wilson lines; Jet power counting and soft/collinear modes; Resummed thrust comparison and hadronization limit; SCET sector decomposition and hard matching; Soft eikonal emission and charge sensitivity; One-loop thrust soft function and singular-term check; Universal quark splitting function from a jet field; Threshold Drell–Yan SCET factorization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-abelian-soft-wilson-lines`, `schwartz.scet-collinear-factorization-jet-fields`, `schwartz.scet-dijet-thrust-factorization`, `schwartz.scet-event-shapes-and-thrust`, `schwartz.scet-factorized-thrust-resummation`, `schwartz.scet-hard-function-one-loop`, `schwartz.scet-jet-function-one-loop`, `schwartz.scet-jets-and-sudakov-problem`, `schwartz.scet-leading-order-thrust-distribution`, `schwartz.scet-nonabelian-soft-factorization`, `schwartz.scet-power-counting-modes`, `schwartz.scet-resummed-thrust-scope`, `schwartz.scet-sector-lagrangian-and-matching`, `schwartz.scet-soft-eikonal-factorization`, `schwartz.scet-soft-function-and-singular-check`, `schwartz.scet-splitting-function-universality`, `schwartz.scet-threshold-drell-yan-factorization`.

</details>

<details>
<summary>Section 36.1 — covered</summary>

The accepted concept, representation, result records substantively represent this section's distinct content: Thrust and hemisphere event shapes; Jet observables and the Sudakov problem; LO thrust distribution, distributions, and dijet singular limit. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-event-shapes-and-thrust`, `schwartz.scet-jets-and-sudakov-problem`, `schwartz.scet-leading-order-thrust-distribution`.

</details>

<details>
<summary>Section 36.2 — covered</summary>

The accepted assumption, result records substantively represent this section's distinct content: LO thrust distribution, distributions, and dijet singular limit; Jet power counting and soft/collinear modes. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-leading-order-thrust-distribution`, `schwartz.scet-power-counting-modes`.

</details>

<details>
<summary>Section 36.3 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Abelian eikonal identity and soft Wilson lines; Non-Abelian soft Wilson lines; Jet power counting and soft/collinear modes; Soft eikonal emission and charge sensitivity. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-abelian-soft-wilson-lines`, `schwartz.scet-nonabelian-soft-factorization`, `schwartz.scet-power-counting-modes`, `schwartz.scet-soft-eikonal-factorization`.

</details>

<details>
<summary>Section 36.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Collinear factorization and gauge-invariant jet fields; Non-Abelian soft Wilson lines; Universal quark splitting function from a jet field. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-collinear-factorization-jet-fields`, `schwartz.scet-nonabelian-soft-factorization`, `schwartz.scet-splitting-function-universality`.

</details>

<details>
<summary>Section 36.5 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Dijet thrust hard–jet–soft factorization; SCET sector decomposition and hard matching; Threshold Drell–Yan SCET factorization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-dijet-thrust-factorization`, `schwartz.scet-sector-lagrangian-and-matching`, `schwartz.scet-threshold-drell-yan-factorization`.

</details>

<details>
<summary>Section 36.6 — covered</summary>

The accepted assumption, method, result records substantively represent this section's distinct content: Dijet thrust hard–jet–soft factorization; RGE resummation of factorized thrust; One-loop SCET hard function; One-loop inclusive jet function; Resummed thrust comparison and hadronization limit; One-loop thrust soft function and singular-term check. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.scet-dijet-thrust-factorization`, `schwartz.scet-factorized-thrust-resummation`, `schwartz.scet-hard-function-one-loop`, `schwartz.scet-jet-function-one-loop`, `schwartz.scet-resummed-thrust-scope`, `schwartz.scet-soft-function-and-singular-check`.

</details>

<details>
<summary>Section 36.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Problem 36.1: dijet event-shape equivalence; Problem 36.2: multiple-emission collinear factorization; Problem 36.3: gluon splitting function; Problem 36.4: soft-collinear two-emission factorization; Problem 36.5: lightcone-gauge jet function; Problem 36.6: threshold Drell–Yan; Problem 36.7: Laplace-space SCET RGEs; Problem 36.8: Sudakov RGEs; Resummed thrust comparison and hadronization limit; Universal quark splitting function from a jet field. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.problem-36-1-dijet-event-shape-equivalence`, `schwartz.problem-36-2-multiple-collinear-factorization`, `schwartz.problem-36-3-gluon-splitting`, `schwartz.problem-36-4-soft-collinear-two-emission`, `schwartz.problem-36-5-lightcone-gauge-jet-function`, `schwartz.problem-36-6-threshold-drell-yan`, `schwartz.problem-36-7-laplace-scet-rges`, `schwartz.problem-36-8-sudakov-rge-expansion`, `schwartz.scet-resummed-thrust-scope`, `schwartz.scet-splitting-function-universality`.

</details>

<details>
<summary>Section A — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Appendix dimensional-analysis problem; Dirac algebra, traces, polarizations, and field-strength identities; Free-field modes and Feynman-diagram symbols; Natural units, mass dimensions, and cross-section conversion; Appendix signs, propagators, and covariant derivative; Fourier correspondence and Appendix A normalization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-dimensional-analysis-problem`, `schwartz.appendix-dirac-algebra-and-field-strength-identities`, `schwartz.appendix-free-mode-and-diagram-conventions`, `schwartz.appendix-natural-units-and-mass-dimensions`, `schwartz.appendix-sign-propagator-and-covariant-derivative-conventions`, `schwartz.fourier-transform-derivative-operator-correspondence`.

</details>

<details>
<summary>Section A.1 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Natural units, mass dimensions, and cross-section conversion; Fourier correspondence and Appendix A normalization. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-natural-units-and-mass-dimensions`, `schwartz.fourier-transform-derivative-operator-correspondence`.

</details>

<details>
<summary>Section A.2 — covered</summary>

The accepted representation records substantively represent this section's distinct content: Free-field modes and Feynman-diagram symbols; Appendix signs, propagators, and covariant derivative. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-free-mode-and-diagram-conventions`, `schwartz.appendix-sign-propagator-and-covariant-derivative-conventions`.

</details>

<details>
<summary>Section A.3 — covered</summary>

The accepted representation records substantively represent this section's distinct content: Free-field modes and Feynman-diagram symbols. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-free-mode-and-diagram-conventions`.

</details>

<details>
<summary>Section A.4 — covered</summary>

The accepted representation records substantively represent this section's distinct content: Dirac algebra, traces, polarizations, and field-strength identities. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-dirac-algebra-and-field-strength-identities`.

</details>

<details>
<summary>Section A.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Appendix dimensional-analysis problem; Dirac algebra, traces, polarizations, and field-strength identities. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.appendix-dimensional-analysis-problem`, `schwartz.appendix-dirac-algebra-and-field-strength-identities`.

</details>

<details>
<summary>Section B — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Derivative regularization method; Dimensional-continuation conventions; Dimensional route for the logarithmic loop; Dimensional poles, IR regulation, and scaleless integrals; d-dimensional scalar-integral formulas; Dimensional field dimensions and the modified minimal-subtraction scale; d-dimensional gamma-matrix and gamma_5 assumption; Feynman-parameter identities and loop shift; Agreement of three logarithmic-loop routes; Lorentz-tensor loop reduction; Other regulator survey; Pauli--Villars ghost subtraction; Schwinger parameters and complementary Feynman fractions; Wick rotation for negative Delta problem; Wick rotation of a Feynman loop; Proper-time composition and complementary Feynman fractions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-derivative-regularization-method`, `schwartz.appendix-dimensional-continuation-conventions`, `schwartz.appendix-dimensional-logarithmic-loop-route`, `schwartz.appendix-dimensional-poles-and-scaleless-integrals`, `schwartz.appendix-dimensional-scalar-integral-formula`, `schwartz.appendix-dimreg-field-dimensions-and-scale`, `schwartz.appendix-dimreg-gamma5-assumption`, `schwartz.appendix-feynman-parameter-identities-and-shift`, `schwartz.appendix-logarithmic-loop-regularization-comparison`, `schwartz.appendix-lorentz-tensor-loop-reduction`, `schwartz.appendix-other-regulator-survey`, `schwartz.appendix-pauli-villars-regularization-method`, `schwartz.appendix-schwinger-parameter-identities`, `schwartz.appendix-wick-rotation-delta-negative-problem`, `schwartz.appendix-wick-rotation-method`, `schwartz.proper-time-feynman-parameter-composition`.

</details>

<details>
<summary>Section B.1 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Feynman-parameter identities and loop shift; Schwinger parameters and complementary Feynman fractions; Proper-time composition and complementary Feynman fractions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-feynman-parameter-identities-and-shift`, `schwartz.appendix-schwinger-parameter-identities`, `schwartz.proper-time-feynman-parameter-composition`.

</details>

<details>
<summary>Section B.2 — covered</summary>

The accepted method, representation records substantively represent this section's distinct content: Schwinger parameters and complementary Feynman fractions; Wick rotation of a Feynman loop; Proper-time composition and complementary Feynman fractions. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-schwinger-parameter-identities`, `schwartz.appendix-wick-rotation-method`, `schwartz.proper-time-feynman-parameter-composition`.

</details>

<details>
<summary>Section B.3 — covered</summary>

The accepted assumption, method, representation, result records substantively represent this section's distinct content: Dimensional-continuation conventions; Dimensional route for the logarithmic loop; Dimensional poles, IR regulation, and scaleless integrals; d-dimensional scalar-integral formulas; Dimensional field dimensions and the modified minimal-subtraction scale; d-dimensional gamma-matrix and gamma_5 assumption; Agreement of three logarithmic-loop routes; Wick rotation of a Feynman loop. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-dimensional-continuation-conventions`, `schwartz.appendix-dimensional-logarithmic-loop-route`, `schwartz.appendix-dimensional-poles-and-scaleless-integrals`, `schwartz.appendix-dimensional-scalar-integral-formula`, `schwartz.appendix-dimreg-field-dimensions-and-scale`, `schwartz.appendix-dimreg-gamma5-assumption`, `schwartz.appendix-logarithmic-loop-regularization-comparison`, `schwartz.appendix-wick-rotation-method`.

</details>

<details>
<summary>Section B.4 — covered</summary>

The accepted method, result records substantively represent this section's distinct content: Derivative regularization method; Agreement of three logarithmic-loop routes; Lorentz-tensor loop reduction; Pauli--Villars ghost subtraction. Their summaries separate results, methods, assumptions, representations, and qualifications where present; coverage was assessed from those meanings and linked route records, not from citation overlap alone.

Records: `schwartz.appendix-derivative-regularization-method`, `schwartz.appendix-logarithmic-loop-regularization-comparison`, `schwartz.appendix-lorentz-tensor-loop-reduction`, `schwartz.appendix-pauli-villars-regularization-method`.

</details>

<details>
<summary>Section B.problems — covered</summary>

The records are source-stated tasks rather than their answers and retain the independent requested work: Other regulator survey; Wick rotation for negative Delta problem. Their method/result/assumption summaries and incident prerequisite records distinguish required inputs from the task result, so this assessment is based on the represented task content rather than shared page coordinates.

Records: `schwartz.appendix-other-regulator-survey`, `schwartz.appendix-wick-rotation-delta-negative-problem`.

</details>
