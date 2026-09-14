# Whole-book graph reconciliation

This report records a review of the combined textbook graph after all its source scopes were accepted. Terra/high assessed semantic section coverage, cross-unit dependencies, independent routes, and proof limits. Sol/high independently reviewed that assessment and made the final recorded decision.

The audited baseline contains **359 nodes, 411 edges, and 88 inventory sections**. It is identified by the graph-content digest below. Subsequent source-backed amendments are listed separately; this snapshot is not an automatic review of arbitrary later changes.

`sha256:a55d32dac8b3eb9a45e4ef5fd0b41a92ea987e26682e82fe10cd36b59e42c662`

The end human audit is **pending**. Shared-graph alignment and cross-volume follow-ups remain separate from this book's audit. See the current [review declaration](review.yaml), [coverage ledger](coverage.yaml), and [scientific decision log](adjudications.yaml).

## Findings and source-backed amendments

### weinberg-2-pending-wi-ch12-power-counting-correspondence

The graph is correctly conditional, but it lacks a source-reviewed correspondence stating whether the Volume I criterion supplies the particular Chapter 12.1 input used in the Volume II hard-flow and low-energy counts, and how the external proof limit propagates.

**Pending source-backed amendment.** Dispatch one bounded cross-book amendment review over the listed Volume I Chapter 12 context and already cited Volume II use pages. Add a correspondence only if the source statements align at the stated use level; retain the external-proof qualification and do not replace either accepted node or claim either book proves the theorem.

Source context: weinberg-1 pp. 504–532; weinberg-2 pp. 256–291; weinberg-2 pp. 323–323.

## Final audit decisions

**Pending power-counting issue omits its full-008 use page.** Add Weinberg II page 323 as a separate source-context slice while preserving the issue and its external-proof limits.

The accepted full-008 artifact places both weinberg-2.dynamical-breaking-low-energy-power-counting and weinberg-2.edge-imported-power-counting-to-dynamical-power-counting on page 323. The source there says the low-energy count follows the analysis of Sections 19.4-19.6. Including that page is therefore necessary for the later bounded amendment to decide whether the accepted Volume I Chapter 12 convergence criterion supplies this particular Volume II route. A separate one-page slice is more precise than enlarging the existing Chapter 20 range. This adjudication corrects only the report context; it does not resolve the graph issue, add a correspondence, or weaken the external-proof qualification.

Alternatives considered: Add Weinberg II page 323 as a separate source-context slice. / Expand the existing Weinberg II source-context range from pages 256-291 through page 323.

## Cross-unit assessment

- Receipt and state inspection matched accepted proposal and knowledge digests for conventions-001, full-001 through full-010, pilot-01, and supplement-ch20-problem3-extended. Every frozen node and edge maps to these accepted unit records; none was inferred from an inventory page hit alone.
- Chapter 15 forms a real ladder: Faddeev–Popov gauge fixing and the ghost determinant lead to BRST transformations, nilpotence, exact gauge fixing, and physical-state cohomology. The distinct anomaly uses are represented by weinberg-2.brst-nilpotence-to-anomaly-cohomology, weinberg-2.brst-transformations-to-anomaly-cohomology, and weinberg-2.brst-cohomology-to-form-derivation; BV remains the separate open/reducible-symmetry treatment.
- The effective-action Goldstone route is distinct from the current-spectral route. Accepted 1PI-kernel and linear-Slavnov–Taylor edges support one proof, while current spectral functions, current matrix elements, and soft limits support another; they must not be collapsed because their conclusions overlap.
- RG and QCD records provide actual later routes: asymptotic freedom and sliding operator renormalization feed Chapter 20 OPE coefficients, while QCD representation, beta function, and dimensional transmutation feed twist operators and instanton suppression. The edge mastery levels identify use or derivation, not chapter order.
- Chapter 19 CCWZ covariants and Goldstone EFT counting feed Chapter 21 dynamical-breaking records. The global Goldstone theorem is helpful evidence for the local Higgs mechanism, preserving the global/local distinction rather than asserting that a global theorem proves gauge-boson mass generation.
- H^5 classification, the integer Wess–Zumino–Witten term, and Chapter 22 anomaly matching/QCD color coefficient are different outcomes: topology classifies allowed terms, while the anomaly treatment fixes a coefficient under its routing and symmetry hypotheses. The WZW route is a prerequisite, not a duplicate pair.
- The accepted Compton imports are complete at the required use level: weinberg-2.imported-compton-invariant-cross-section-formula and weinberg-2.imported-compton-spin-sum-amplitude-square retain their exact Weinberg I origins and necessary edges to weinberg-2.problem-derive-parton-dis-cross-section. The latter does not claim a Volume II proof of those formulas.
- The Chapter 12.1 input is an explicit imported assumption with necessary uses in scalar hard-flow, general hard-flow, and dynamical-breaking counting. The accepted Volume I convergence record is related enough to need a reviewed correspondence, but its proof is external and this audit does not equate it with either Volume II application.
- The Volume I BRST deferral is not silently made equivalent to the Volume II treatment: Chapter 15.7 supplies construction, cohomology, and a QED polarization example, but the frozen evidence lacks a reviewed correspondence to the Volume I Coulomb-gauge discussion.
- Global topology is kept distinct from local de Rham reasoning. weinberg-2.goldstone-boundary-compactification-and-homotopy classifies global finite-action based maps, while the Volume I p-form result is local Poincaré exactness on contractible regions; neither entails a de Rham/homotopy equivalence.
- Problem records remain independent tasks. Necessary, evidence, and helpful edges preserve actual source roles without making alternative methods, appendices, or background calculations universal required mastery.

## Conventions and proof boundaries

Accepted roman-xx–xxi companion evidence fixes metric and Levi-Civita signs, raised-versus-lowered Dirac matrices, matrix/antifield notation, natural units and charge normalization. These are reading conditions for formula-sensitive records, not duplicate physical concepts.

Records: `weinberg-2.spacetime-index-and-dirac-notation`, `weinberg-2.matrix-spinor-and-antifield-notation`, `weinberg-2.natural-unit-charge-and-uncertainty-conventions`.

Chapter 20 states and applies its Chapter 12.1 input without proving it, and its appendix limits the fully general hard-flow claim because subintegrations can diverge. The related Volume I convergence criterion reports an external proof; both limits are retained.

Records: `weinberg-2.imported-chapter12-power-counting-theorem`, `weinberg-2.scalar-hard-flow-power-counting`, `weinberg-2.general-hard-flow-ope-power-counting`, `weinberg-2.general-hard-flow-ope-rigor-qualification`.

These are exact accepted Volume I inputs for a Volume II task, including their stated exclusions and polarization/spin-average conditions; no new Compton proof is claimed.

Records: `weinberg-2.imported-compton-invariant-cross-section-formula`, `weinberg-2.imported-compton-spin-sum-amplitude-square`, `weinberg-2.problem-derive-parton-dis-cross-section`.

The book reports the gist of Adler–Bardeen and cites the Barnich–Brandt–Henneaux classification. The records retain the external-theorem qualifications.

Records: `weinberg-2.adler-bardeen-radiative-and-mass-decoupling-qualification`, `weinberg-2.bv-antibracket-anomaly-cohomology-and-all-orders-removal`.

The Cartan–Maurer normalization uses cited Bott content, and Appendix B reports rather than derives its catalog and kernel rule; later uses remain at that reported level.

Records: `weinberg-2.cartan-maurer-standard-su2-normalization`, `weinberg-2.homotopy-reference-table-and-coset-kernel`.

These establish the accepted Volume II BRST treatment, but no reviewed edge yet resolves the Volume I Coulomb-gauge deferral.

Records: `weinberg-2.brst-cohomology-of-physical-states`, `weinberg-2.brst-electrodynamic-polarization-example`, `weinberg-2.brst-unitarity-and-general-gauge-fixing`.

Global homotopy constructs and tables do not prove the separately qualified local de Rham/Poincaré-exactness discussion in Volume I.

Records: `weinberg-2.goldstone-boundary-compactification-and-homotopy`, `weinberg-2.homotopy-reference-table-and-coset-kernel`.

## Section coverage assessment

These mappings follow the accepted records' section evidence and content. A shared boundary page may contribute to multiple sections; a table number does not determine its section.

<details>
<summary>Section 15 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Adjoint representation from structure constants; Anti-BRST observation about ghost and antighost roles; Axial gauge canonical reduction; Deriving the covariant gauge-field path integral from axial gauge; Why BRST must extend power counting and bilinear Faddeev–Popov actions. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adjoint-representation`, `weinberg-2.anti-brst-ghost-antighost-role-observation`, `weinberg-2.axial-gauge-canonical-reduction`, `weinberg-2.axial-gauge-path-integral-to-covariant-action`, `weinberg-2.brst-beyond-power-counting-and-bilinear-faddeev-popov`, `weinberg-2.brst-cohomology-of-physical-states`, `weinberg-2.brst-conditional-ghost-free-gauge-independence`, `weinberg-2.brst-electrodynamic-polarization-example`, `weinberg-2.brst-exact-gauge-fixing`, `weinberg-2.brst-field-transformations`, `weinberg-2.brst-nilpotence`, `weinberg-2.brst-unitarity-and-general-gauge-fixing`, `weinberg-2.bv-antibracket-classical-master-equation`, `weinberg-2.bv-anticanonical-transformations`, `weinberg-2.bv-antifields-and-graded-master-action`, `weinberg-2.bv-formalism-for-open-and-reducible-symmetries`, `weinberg-2.bv-gauge-fixing-fermion-and-on-shell-brst`, `weinberg-2.bv-generalized-brst-antibracket-differential`, `weinberg-2.bv-master-equation-open-algebra-consistency-tower`, `weinberg-2.bv-minimal-and-trivial-pairs`, `weinberg-2.bv-quantum-brst-observable-condition`, `weinberg-2.bv-quantum-master-equation`, `weinberg-2.compact-simple-lie-algebra-classification`, `weinberg-2.compactness-and-hermitian-representations`, `weinberg-2.covariant-derivative`, `weinberg-2.covariant-field-equation-and-matter-current`, `weinberg-2.covariant-gauge-ghost-propagator-and-vertex`, `weinberg-2.dewitt-notation-general-local-symmetry`, `weinberg-2.dynamical-gauge-fields-give-local-symmetry-physical-content`, `weinberg-2.faddeev-popov-gauge-fixed-functional-integral`, `weinberg-2.faddeev-popov-gauge-fixing-independence`, `weinberg-2.faddeev-popov-ghost-determinant`, `weinberg-2.finite-gauge-transformations`, `weinberg-2.gauge-and-affine-connection-curvature-analogy`, `weinberg-2.gauge-charge-includes-gauge-fields`, `weinberg-2.gauge-field-lagrangian-restrictions`, `weinberg-2.gauge-field-transformation`, `weinberg-2.gauge-invariant-functional-measure-assumption`, `weinberg-2.gauge-invariant-lagrangian-ingredients`, `weinberg-2.gauge-theory-heavy-trapped-and-ghost-loop-framing`, `weinberg-2.general-brst-cohomology-functional-result`, `weinberg-2.general-brst-cohomology-proof-completion`, `weinberg-2.general-faddeev-popov-dewitt-theorem`, `weinberg-2.generalized-brst-slavnov-operator`, `weinberg-2.generalized-feynman-gauge-propagator`, `weinberg-2.ghost-loop-compensation-and-power-counting`, `weinberg-2.lie-algebra-structure-constants`, `weinberg-2.local-matter-gauge-transformations`, `weinberg-2.local-pointwise-and-component-gauge-choices`, `weinberg-2.nonabelian-bianchi-identity`, `weinberg-2.nonabelian-field-strength`, `weinberg-2.nonabelian-gauge-self-interaction`, `weinberg-2.original-yang-mills-su2-representation-example`, `weinberg-2.positive-invariant-lie-algebra-metric`, `weinberg-2.pure-gauge-flatness`, `weinberg-2.reducible-gauge-symmetry-and-ghosts-of-ghosts`, `weinberg-2.renormalizable-yang-mills-lagrangian-assumption`, `weinberg-2.string-light-cone-and-gravity-brst-limitation`, `weinberg-2.theta-term-nonperturbative-effects`, `weinberg-2.yang-mills-coupling-normalization`, `weinberg-2.yang-mills-field-equations-and-total-current`, `weinberg-2.yang-mills-first-class-constraints`, `weinberg-2.yang-mills-original-massless-vector-obstacle`, `weinberg-2.yang-mills-three-and-four-vector-vertices`.

</details>

<details>
<summary>Section 15.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Adjoint representation from structure constants; Covariant derivative of matter fields; Finite gauge transformations; Gauge connection-curvature analogy and its limit; Inhomogeneous gauge-field transformation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adjoint-representation`, `weinberg-2.covariant-derivative`, `weinberg-2.finite-gauge-transformations`, `weinberg-2.gauge-and-affine-connection-curvature-analogy`, `weinberg-2.gauge-field-transformation`, `weinberg-2.lie-algebra-structure-constants`, `weinberg-2.local-matter-gauge-transformations`, `weinberg-2.local-pointwise-and-component-gauge-choices`, `weinberg-2.nonabelian-field-strength`, `weinberg-2.original-yang-mills-su2-representation-example`, `weinberg-2.pure-gauge-flatness`.

</details>

<details>
<summary>Section 15.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Classification consequences for compact simple gauge algebras; Compact gauge algebras and Hermitian finite representations; Gauge connection-curvature analogy and its limit; Gauge-field terms and mass restriction; Gauge-covariant ingredients for a Lagrangian. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.compact-simple-lie-algebra-classification`, `weinberg-2.compactness-and-hermitian-representations`, `weinberg-2.gauge-and-affine-connection-curvature-analogy`, `weinberg-2.gauge-field-lagrangian-restrictions`, `weinberg-2.gauge-invariant-lagrangian-ingredients`, `weinberg-2.nonabelian-gauge-self-interaction`, `weinberg-2.positive-invariant-lie-algebra-metric`, `weinberg-2.theta-term-nonperturbative-effects`, `weinberg-2.yang-mills-coupling-normalization`.

</details>

<details>
<summary>Section 15.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Gauge-covariant field equation and matter-current conservation; Non-Abelian charge includes the gauge-field contribution; Non-Abelian Bianchi identity; Renormalizable Yang–Mills Lagrangian truncation; Yang–Mills field equation and ordinarily conserved total current. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.covariant-field-equation-and-matter-current`, `weinberg-2.gauge-charge-includes-gauge-fields`, `weinberg-2.nonabelian-bianchi-identity`, `weinberg-2.renormalizable-yang-mills-lagrangian-assumption`, `weinberg-2.yang-mills-field-equations-and-total-current`.

</details>

<details>
<summary>Section 15.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Axial gauge canonical reduction; Deriving the covariant gauge-field path integral from axial gauge; Gauge invariance of the functional measure; First-class constraints in canonical Yang–Mills theory. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.axial-gauge-canonical-reduction`, `weinberg-2.axial-gauge-path-integral-to-covariant-action`, `weinberg-2.gauge-invariant-functional-measure-assumption`, `weinberg-2.yang-mills-first-class-constraints`.

</details>

<details>
<summary>Section 15.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Faddeev–Popov gauge-fixed functional integral; Gauge-fixing independence in the Faddeev–Popov theorem; Generalized Feynman (ξ) gauge; Three- and four-vector Yang–Mills vertices. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.faddeev-popov-gauge-fixed-functional-integral`, `weinberg-2.faddeev-popov-gauge-fixing-independence`, `weinberg-2.generalized-feynman-gauge-propagator`, `weinberg-2.yang-mills-three-and-four-vector-vertices`.

</details>

<details>
<summary>Section 15.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Why BRST must extend power counting and bilinear Faddeev–Popov actions; Adjoint massless ghost propagator and ghost–gauge vertex; Faddeev–Popov determinant as ghost fields; Ghost loops compensate gauge overcounting. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.brst-beyond-power-counting-and-bilinear-faddeev-popov`, `weinberg-2.covariant-gauge-ghost-propagator-and-vertex`, `weinberg-2.faddeev-popov-ghost-determinant`, `weinberg-2.ghost-loop-compensation-and-power-counting`.

</details>

<details>
<summary>Section 15.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Why BRST must extend power counting and bilinear Faddeev–Popov actions; Physical states as BRST cohomology; BRST cohomology removes unphysical photon and ghost states; Gauge fixing as a BRST-exact term; BRST transformations with auxiliary field. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.brst-beyond-power-counting-and-bilinear-faddeev-popov`, `weinberg-2.brst-cohomology-of-physical-states`, `weinberg-2.brst-electrodynamic-polarization-example`, `weinberg-2.brst-exact-gauge-fixing`, `weinberg-2.brst-field-transformations`, `weinberg-2.brst-nilpotence`, `weinberg-2.brst-unitarity-and-general-gauge-fixing`.

</details>

<details>
<summary>Section 15.8 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Anti-BRST observation about ghost and antighost roles; Conditional ghost-free gauge independence from BRST cohomology; De Witt notation for general local symmetries; General BRST cohomology of ghost-number-zero functionals; Completion of the general BRST cohomology proof. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.anti-brst-ghost-antighost-role-observation`, `weinberg-2.brst-conditional-ghost-free-gauge-independence`, `weinberg-2.dewitt-notation-general-local-symmetry`, `weinberg-2.general-brst-cohomology-functional-result`, `weinberg-2.general-brst-cohomology-proof-completion`, `weinberg-2.general-faddeev-popov-dewitt-theorem`, `weinberg-2.generalized-brst-slavnov-operator`, `weinberg-2.reducible-gauge-symmetry-and-ghosts-of-ghosts`, `weinberg-2.string-light-cone-and-gravity-brst-limitation`.

</details>

<details>
<summary>Section 15.9 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Antibracket form of the classical master equation; BV anticanonical transformations preserve the master structure; BV antifields and the graded master action; Batalin-Vilkovisky formalism for open and reducible gauge symmetries; BV gauge fixing by a fermion and on-shell BRST closure. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bv-antibracket-classical-master-equation`, `weinberg-2.bv-anticanonical-transformations`, `weinberg-2.bv-antifields-and-graded-master-action`, `weinberg-2.bv-formalism-for-open-and-reducible-symmetries`, `weinberg-2.bv-gauge-fixing-fermion-and-on-shell-brst`, `weinberg-2.bv-generalized-brst-antibracket-differential`, `weinberg-2.bv-master-equation-open-algebra-consistency-tower`, `weinberg-2.bv-minimal-and-trivial-pairs`, `weinberg-2.bv-quantum-brst-observable-condition`, `weinberg-2.bv-quantum-master-equation`.

</details>

<details>
<summary>Section 15.A — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: Appendix proof of the positive-metric compact-algebra criterion. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.appendix-a-proof-of-compact-algebra-criterion`.

</details>

<details>
<summary>Section 15.B — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: Cartan catalog of compact classical families; Exceptional algebras, low-rank isomorphisms, and covering-group qualification. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.cartan-catalog-compact-classical-families`, `weinberg-2.cartan-exceptional-algebras-and-low-rank-isomorphisms`.

</details>

<details>
<summary>Section 15.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem prompt: BRST classification and BV identities; Problem prompt: gauge-fixing propagator and ghost calculations; Problem prompt: holonomy, curvature, and local pure gauge; Problem prompt: exclude a four-generator simple Lie algebra; Problem prompt: derive the non-Abelian Bianchi identity. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-brst-and-bv-algebra-exercises`, `weinberg-2.problem-gauge-fixing-propagator-and-ghost-calculations`, `weinberg-2.problem-holonomy-curvature-and-local-pure-gauge`, `weinberg-2.problem-no-four-generator-simple-lie-algebra`, `weinberg-2.problem-nonabelian-bianchi-identity`.

</details>

<details>
<summary>Section 16 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Effective action as 1PI vertices and tree reconstruction; Effective potential for a constant background; Effective potential as constrained minimum energy density; Convexity of the exact effective potential and the mixed-state region; External-source generating and connected functionals. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.effective-action-1pi-tree-reconstruction`, `weinberg-2.effective-potential-constant-background`, `weinberg-2.effective-potential-constrained-energy-interpretation`, `weinberg-2.exact-effective-potential-convexity-and-mixed-state-region`, `weinberg-2.external-source-generating-functional`, `weinberg-2.fermion-versus-boson-effective-potential-loop-sign`, `weinberg-2.full-two-point-function-is-inverse-1pi-kernel`, `weinberg-2.legendre-quantum-effective-action`, `weinberg-2.linear-symmetry-slavnov-taylor-identity-for-effective-action`, `weinberg-2.nonlinear-symmetry-average-obstruction-for-effective-action`, `weinberg-2.one-loop-effective-potential-determinant-method`.

</details>

<details>
<summary>Section 16.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Effective action as 1PI vertices and tree reconstruction; External-source generating and connected functionals; Full two-point function as inverse 1PI kernel; Legendre definition and stationary equation of the quantum effective action. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.effective-action-1pi-tree-reconstruction`, `weinberg-2.external-source-generating-functional`, `weinberg-2.full-two-point-function-is-inverse-1pi-kernel`, `weinberg-2.legendre-quantum-effective-action`.

</details>

<details>
<summary>Section 16.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Effective potential for a constant background; Fermion contribution to the effective potential has opposite determinant sign; One-loop effective potential from a quadratic determinant. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.effective-potential-constant-background`, `weinberg-2.fermion-versus-boson-effective-potential-loop-sign`, `weinberg-2.one-loop-effective-potential-determinant-method`.

</details>

<details>
<summary>Section 16.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Effective potential as constrained minimum energy density; Convexity of the exact effective potential and the mixed-state region. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.effective-potential-constrained-energy-interpretation`, `weinberg-2.exact-effective-potential-convexity-and-mixed-state-region`.

</details>

<details>
<summary>Section 16.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Linear action symmetries yield Slavnov–Taylor identities for Γ; Nonlinear symmetry average obstructs identical Γ transformations. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.linear-symmetry-slavnov-taylor-identity-for-effective-action`, `weinberg-2.nonlinear-symmetry-average-obstruction-for-effective-action`.

</details>

<details>
<summary>Section 16.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem prompt: finite linear symmetry inherited by W and Γ; Problem prompt: higher connected correlators from Γ derivatives; Problem prompt: one-loop pseudoscalar Yukawa effective potential; Problem prompt: six-dimensional cubic-scalar effective potential. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-finite-linear-symmetry-of-effective-action`, `weinberg-2.problem-higher-connected-correlators-from-effective-action`, `weinberg-2.problem-one-loop-pseudoscalar-yukawa-effective-potential`, `weinberg-2.problem-six-dimensional-cubic-effective-potential`.

</details>

<details>
<summary>Section 17 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Background-field gauge and formal background invariance; Formal background transformations differ from true gauge transformations; Background gauge invariance ties coupling renormalization to the field-strength term; BV cohomological renormalization of general gauge theories; Cohomology theorem and limits of structural renormalizability. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.background-field-gauge-formal-invariance`, `weinberg-2.background-formal-versus-true-gauge-transformations`, `weinberg-2.background-gauge-coupling-renormalization-from-field-strength`, `weinberg-2.bv-cohomological-renormalization-of-general-gauge-theories`, `weinberg-2.bv-cohomology-theorem-and-renormalizability-limits`, `weinberg-2.constant-background-one-loop-gauge-coupling-method`, `weinberg-2.direct-brst-renormalizability-induction`, `weinberg-2.one-loop-nonabelian-coupling-divergence-group-factors`, `weinberg-2.ultraviolet-and-infrared-regulation-of-one-loop-gauge-integral`, `weinberg-2.zinn-justin-equation-for-quantum-effective-action`.

</details>

<details>
<summary>Section 17.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Zinn–Justin equation for the quantum effective action. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.zinn-justin-equation-for-quantum-effective-action`.

</details>

<details>
<summary>Section 17.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Direct BRST proof for the displayed simple Yang–Mills fermion sector. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.direct-brst-renormalizability-induction`.

</details>

<details>
<summary>Section 17.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: BV cohomological renormalization of general gauge theories; Cohomology theorem and limits of structural renormalizability. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bv-cohomological-renormalization-of-general-gauge-theories`, `weinberg-2.bv-cohomology-theorem-and-renormalizability-limits`.

</details>

<details>
<summary>Section 17.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Background-field gauge and formal background invariance; Formal background transformations differ from true gauge transformations; Background gauge invariance ties coupling renormalization to the field-strength term. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.background-field-gauge-formal-invariance`, `weinberg-2.background-formal-versus-true-gauge-transformations`, `weinberg-2.background-gauge-coupling-renormalization-from-field-strength`.

</details>

<details>
<summary>Section 17.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Constant-background determinant method for one-loop gauge coupling renormalization; One-loop non-Abelian coupling divergence from gauge, ghost, and matter group factors; Ultraviolet and infrared regulation of the one-loop gauge integral. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.constant-background-one-loop-gauge-coupling-method`, `weinberg-2.one-loop-nonabelian-coupling-divergence-group-factors`, `weinberg-2.ultraviolet-and-infrared-regulation-of-one-loop-gauge-integral`.

</details>

<details>
<summary>Section 17.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem prompt: BRST quantization in background-field gauge; Problem prompt: extend the direct renormalizability proof to scalars; Problem prompt: one-loop gauge coupling relation with scalars; Problem prompt: derive coupling relation from a spacetime-dependent background. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-background-field-brst-quantization`, `weinberg-2.problem-direct-renormalizability-with-elementary-scalars`, `weinberg-2.problem-one-loop-gauge-coupling-with-elementary-scalars`, `weinberg-2.problem-spacetime-dependent-background-coupling-relation`.

</details>

<details>
<summary>Section 18 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Asymptotic freedom and logarithmic scaling; Scheme invariance of the first two beta coefficients; Correlation-length critical exponent from RG; Fixed-point anomalous power scaling; Coordinate invariance of fixed-point stability eigenvalues. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.asymptotic-freedom-logarithmic-scaling`, `weinberg-2.beta-function-first-two-coefficients-scheme-invariant`, `weinberg-2.correlation-length-critical-exponent-from-rg`, `weinberg-2.fixed-point-anomalous-power-scaling`, `weinberg-2.fixed-point-eigenvalue-coordinate-invariance`, `weinberg-2.ir-relevant-marginal-irrelevant-directions`, `weinberg-2.landau-pole-physicality-and-triviality-qualification`, `weinberg-2.mass-independent-renormalization-group-parameters`, `weinberg-2.mass-singularities-and-infrared-safe-observables`, `weinberg-2.minimal-subtraction-beta-from-simple-poles`, `weinberg-2.modified-minimal-subtraction-and-dimensional-selection`, `weinberg-2.multicoupling-fixed-point-stability-matrix`, `weinberg-2.nonrenormalizable-flow-and-asymptotic-safety`, `weinberg-2.qcd-confinement-hypothesis-from-infrared-growth`, `weinberg-2.qcd-dimensional-transmutation-and-threshold-matching`, `weinberg-2.qcd-infrared-safe-inclusive-and-jet-rates`, `weinberg-2.qcd-one-loop-beta-and-active-flavors`, `weinberg-2.qcd-renormalizable-lagrangian-and-effective-symmetry-qualification`, `weinberg-2.qcd-su3-quark-color-representation`, `weinberg-2.qed-running-charge-at-sliding-scale`, `weinberg-2.rg-high-energy-mode-elimination`, `weinberg-2.rg-improved-effective-potential-and-validity`, `weinberg-2.rg-leading-log-prediction-from-lower-orders`, `weinberg-2.single-coupling-asymptotic-flow-types`, `weinberg-2.sliding-operator-renormalization-and-anomalous-dimension`, `weinberg-2.sliding-scale-coupling-callan-symanzik-method`, `weinberg-2.universality-class-from-long-wavelength-content`, `weinberg-2.wilson-fisher-epsilon-expansion`.

</details>

<details>
<summary>Section 18.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Mass singularities and infrared-safe observables; Renormalization group as high-energy mode elimination. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.mass-singularities-and-infrared-safe-observables`, `weinberg-2.rg-high-energy-mode-elimination`.

</details>

<details>
<summary>Section 18.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: QED running charge at a sliding scale; RG-improved effective potential and its validity limits; Sliding operator renormalization and anomalous dimensions; Sliding-scale coupling and Callan–Symanzik flow. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.qed-running-charge-at-sliding-scale`, `weinberg-2.rg-improved-effective-potential-and-validity`, `weinberg-2.sliding-operator-renormalization-and-anomalous-dimension`, `weinberg-2.sliding-scale-coupling-callan-symanzik-method`.

</details>

<details>
<summary>Section 18.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Scheme invariance of the first two beta coefficients; Physicality and triviality qualifications for divergent flow; Asymptotic flow types for one coupling. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.beta-function-first-two-coefficients-scheme-invariant`, `weinberg-2.landau-pole-physicality-and-triviality-qualification`, `weinberg-2.single-coupling-asymptotic-flow-types`.

</details>

<details>
<summary>Section 18.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Coordinate invariance of fixed-point stability eigenvalues; Mass-independent RG parameters and mass flow; Multi-coupling fixed-point stability matrix; Nonrenormalizable flow and asymptotic safety. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.fixed-point-eigenvalue-coordinate-invariance`, `weinberg-2.mass-independent-renormalization-group-parameters`, `weinberg-2.multicoupling-fixed-point-stability-matrix`, `weinberg-2.nonrenormalizable-flow-and-asymptotic-safety`.

</details>

<details>
<summary>Section 18.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Correlation-length critical exponent from RG; Relevant, marginal, and irrelevant infrared directions; Universality class from long-wavelength degrees of freedom; Wilson–Fisher epsilon expansion. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.correlation-length-critical-exponent-from-rg`, `weinberg-2.ir-relevant-marginal-irrelevant-directions`, `weinberg-2.universality-class-from-long-wavelength-content`, `weinberg-2.wilson-fisher-epsilon-expansion`.

</details>

<details>
<summary>Section 18.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Minimal subtraction beta-functions from simple poles; Modified minimal subtraction and dimensional selection rules. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.minimal-subtraction-beta-from-simple-poles`, `weinberg-2.modified-minimal-subtraction-and-dimensional-selection`.

</details>

<details>
<summary>Section 18.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Confinement hypothesis from infrared growth; QCD dimensional transmutation and threshold matching; Infrared-safe inclusive and jet rates in QCD; QCD one-loop beta-function and active-flavor condition; QCD renormalizable Lagrangian and effective symmetry qualification. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.qcd-confinement-hypothesis-from-infrared-growth`, `weinberg-2.qcd-dimensional-transmutation-and-threshold-matching`, `weinberg-2.qcd-infrared-safe-inclusive-and-jet-rates`, `weinberg-2.qcd-one-loop-beta-and-active-flavors`, `weinberg-2.qcd-renormalizable-lagrangian-and-effective-symmetry-qualification`, `weinberg-2.qcd-su3-quark-color-representation`.

</details>

<details>
<summary>Section 18.8 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: RG prediction of leading logarithms from lower orders. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.rg-leading-log-prediction-from-lower-orders`.

</details>

<details>
<summary>Section 18.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: tune the third beta coefficient by a coupling redefinition; Problem: effective electric charge at 100 GeV; Problem: large-momentum electron propagator; Problem: fixed-point operator correction; Problem: O(N) epsilon-expansion critical exponent. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-coupling-redefinition-third-beta-coefficient`, `weinberg-2.problem-effective-charge-at-100-gev`, `weinberg-2.problem-electron-propagator-asymptotics`, `weinberg-2.problem-fixed-point-operator-correction`, `weinberg-2.problem-on-epsilon-critical-exponent`, `weinberg-2.problem-sun-scalar-loop-gauge-beta`.

</details>

<details>
<summary>Section 19 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Adler-Weisberger sum rule in the exact chiral limit; Anomalous Goldstone action terms from H⁵(G/H; R); Compensator transformation and H-covariant EFT building blocks; Chiral breaking to isospin and pion identification; Chiral nucleon redefinition and general leading pion-nucleon Lagrangian. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adler-weisberger-sum-rule-exact-chiral-limit`, `weinberg-2.anomalous-goldstone-action-terms-and-h5`, `weinberg-2.ccwz-compensator-and-h-covariants`, `weinberg-2.chiral-breaking-to-isospin-and-pion-identification`, `weinberg-2.chiral-nucleon-redefinition-and-general-leading-lagrangian`, `weinberg-2.chiral-pion-effective-field-theory-power-counting`, `weinberg-2.chiral-su2-times-su2-qcd-symmetry`, `weinberg-2.current-algebra-and-effective-lagrangian-for-multigoldstone-processes`, `weinberg-2.degenerate-vacua-and-cluster-selection`, `weinberg-2.general-broken-symmetry-eft-softness-and-power-counting`, `weinberg-2.general-explicit-breaking-operator-construction`, `weinberg-2.general-g-to-h-goldstone-coordinate-separation`, `weinberg-2.general-goldstone-kinetic-metric-and-canonical-fields`, `weinberg-2.goldberger-treiman-relation`, `weinberg-2.goldstone-boson-theorem-current-spectral-route`, `weinberg-2.goldstone-boson-theorem-effective-action-route`, `weinberg-2.goldstone-boson-theorem-for-broken-global-symmetry`, `weinberg-2.goldstone-current-matrix-elements-and-decay-constant`, `weinberg-2.leading-pion-pion-scattering-and-scattering-lengths`, `weinberg-2.nonlinear-chiral-realization-and-pion-covariant-derivative`, `weinberg-2.on-model-goldstone-mode-counting`, `weinberg-2.order-parameter-at-continuous-symmetry-restoration`, `weinberg-2.pcac-pion-pole-qualification`, `weinberg-2.persistent-mass-condition-conjecture`, `weinberg-2.pion-decay-constant-from-axial-current`, `weinberg-2.pion-mass-from-quark-mass-breaking`, `weinberg-2.pion-nucleon-chiral-power-counting`, `weinberg-2.pseudo-goldstone-mass-double-commutator`, `weinberg-2.q4-pion-eft-renormalization-and-fpi-matching`, `weinberg-2.quark-mass-pion-nucleon-contact-corrections`, `weinberg-2.right-cosets-cartan-decomposition-and-exponential-representatives`, `weinberg-2.soft-forward-pion-nucleon-amplitude`, `weinberg-2.soft-goldstone-external-line-theorem`, `weinberg-2.su3-first-order-nonpseudoscalar-multiplet-mass-shift`, `weinberg-2.su3-leading-meson-lagrangian-and-fpi-normalization`, `weinberg-2.su3-matrix-element-reduction-for-multiplet-mass-shifts`, `weinberg-2.su3-nucleon-quark-mass-splitting-relation`, `weinberg-2.su3-pseudoscalar-masses-electromagnetism-and-gmo`, `weinberg-2.su3-spurion-construction-and-q4-meson-eft`, `weinberg-2.three-flavor-chiral-symmetry-and-u-field`, `weinberg-2.threshold-pion-nucleon-scattering-lengths`, `weinberg-2.u1a-problem-extra-pseudoscalar-prediction`, `weinberg-2.vacuum-alignment-for-approximate-symmetry`, `weinberg-2.vafa-witten-unbroken-vector-flavor-symmetry`, `weinberg-2.wess-zumino-witten-term-and-integer-coefficient`, `weinberg-2.zero-momentum-goldstone-effective-vertices`.

</details>

<details>
<summary>Section 19.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Infinite-volume vacuum sectors and cluster selection. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.degenerate-vacua-and-cluster-selection`.

</details>

<details>
<summary>Section 19.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Goldstone theorem from current spectral functions; Goldstone theorem from the effective action; Goldstone theorem for a broken global continuous symmetry; Goldstone current matrix elements and symmetry-breaking scale; O(N) model check of Goldstone-mode counting. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.goldstone-boson-theorem-current-spectral-route`, `weinberg-2.goldstone-boson-theorem-effective-action-route`, `weinberg-2.goldstone-boson-theorem-for-broken-global-symmetry`, `weinberg-2.goldstone-current-matrix-elements-and-decay-constant`, `weinberg-2.on-model-goldstone-mode-counting`, `weinberg-2.soft-goldstone-external-line-theorem`, `weinberg-2.zero-momentum-goldstone-effective-vertices`.

</details>

<details>
<summary>Section 19.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Pseudo-Goldstone mass from the explicit-breaking double commutator; Vacuum alignment under small explicit breaking. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.pseudo-goldstone-mass-double-commutator`, `weinberg-2.vacuum-alignment-for-approximate-symmetry`.

</details>

<details>
<summary>Section 19.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Chiral breaking to isospin and pion identification; Two-flavor chiral SU(2) × SU(2) symmetry of massless QCD; Goldberger–Treiman relation; PCAC as pion-pole dominance of an otherwise small axial divergence; Pion decay constant from the axial current. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.chiral-breaking-to-isospin-and-pion-identification`, `weinberg-2.chiral-su2-times-su2-qcd-symmetry`, `weinberg-2.goldberger-treiman-relation`, `weinberg-2.pcac-pion-pole-qualification`, `weinberg-2.pion-decay-constant-from-axial-current`, `weinberg-2.pion-mass-from-quark-mass-breaking`.

</details>

<details>
<summary>Section 19.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Adler-Weisberger sum rule in the exact chiral limit; Chiral nucleon redefinition and general leading pion-nucleon Lagrangian; Chiral pion EFT and derivative power counting; Current algebra and symmetry-respecting effective Lagrangians for multi-Goldstone processes; Leading pion-pion scattering amplitude and scattering lengths. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adler-weisberger-sum-rule-exact-chiral-limit`, `weinberg-2.chiral-nucleon-redefinition-and-general-leading-lagrangian`, `weinberg-2.chiral-pion-effective-field-theory-power-counting`, `weinberg-2.current-algebra-and-effective-lagrangian-for-multigoldstone-processes`, `weinberg-2.leading-pion-pion-scattering-and-scattering-lengths`, `weinberg-2.nonlinear-chiral-realization-and-pion-covariant-derivative`, `weinberg-2.pion-nucleon-chiral-power-counting`, `weinberg-2.q4-pion-eft-renormalization-and-fpi-matching`, `weinberg-2.quark-mass-pion-nucleon-contact-corrections`, `weinberg-2.soft-forward-pion-nucleon-amplitude`, `weinberg-2.threshold-pion-nucleon-scattering-lengths`.

</details>

<details>
<summary>Section 19.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Compensator transformation and H-covariant EFT building blocks; Softness and power counting for Goldstone EFT with heavy fields; Constructing explicit-breaking operators from their H components; Goldstone-coordinate separation for compact G broken to H; Goldstone kinetic metric and canonical normalization. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.ccwz-compensator-and-h-covariants`, `weinberg-2.general-broken-symmetry-eft-softness-and-power-counting`, `weinberg-2.general-explicit-breaking-operator-construction`, `weinberg-2.general-g-to-h-goldstone-coordinate-separation`, `weinberg-2.general-goldstone-kinetic-metric-and-canonical-fields`, `weinberg-2.order-parameter-at-continuous-symmetry-restoration`, `weinberg-2.right-cosets-cartan-decomposition-and-exponential-representatives`.

</details>

<details>
<summary>Section 19.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: First-order quark-mass shift of a non-pseudoscalar SU(3) multiplet; SU(3) leading meson Lagrangian and Fπ normalization; SU(3) matrix-element reduction for multiplet mass shifts; SU(3) relation for the quark-mass nucleon splitting; SU(3) pseudoscalar masses, electromagnetic shift, and Gell-Mann-Okubo relation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.su3-first-order-nonpseudoscalar-multiplet-mass-shift`, `weinberg-2.su3-leading-meson-lagrangian-and-fpi-normalization`, `weinberg-2.su3-matrix-element-reduction-for-multiplet-mass-shifts`, `weinberg-2.su3-nucleon-quark-mass-splitting-relation`, `weinberg-2.su3-pseudoscalar-masses-electromagnetism-and-gmo`, `weinberg-2.su3-spurion-construction-and-q4-meson-eft`, `weinberg-2.three-flavor-chiral-symmetry-and-u-field`.

</details>

<details>
<summary>Section 19.8 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Anomalous Goldstone action terms from H⁵(G/H; R); Wess-Zumino-Witten action term and integer coefficient. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.anomalous-goldstone-action-terms-and-h5`, `weinberg-2.wess-zumino-witten-term-and-integer-coefficient`.

</details>

<details>
<summary>Section 19.9 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Persistent-mass condition as a heuristic for unbroken vector symmetries; Vafa-Witten result for massive vector flavor symmetries. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.persistent-mass-condition-conjecture`, `weinberg-2.vafa-witten-unbroken-vector-flavor-symmetry`.

</details>

<details>
<summary>Section 19.10 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: U(1)A problem and the missing extra pseudoscalar. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.u1a-problem-extra-pseudoscalar-prediction`.

</details>

<details>
<summary>Section 19.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: Adler sum rule for pion-pion scattering; Problem: derive the SU(3) nucleon mass relation; Problem: pion transformations in exponential SU(2) coset coordinates; Problem: one-loop pion-pion scattering with finite pion mass; Problem: SO(3) to SO(2) Goldstone EFT and scattering. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-adler-sum-rule-pion-scattering`, `weinberg-2.problem-derive-su3-nucleon-mass-relation`, `weinberg-2.problem-exponential-su2-coset-pion-transformations`, `weinberg-2.problem-one-loop-massive-pion-scattering`, `weinberg-2.problem-so3-to-so2-goldstone-eft`, `weinberg-2.problem-sun-vacuum-alignment-residual-symmetry`.

</details>

<details>
<summary>Section 20 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Altarelli–Parisi evolution from OPE moments; Asymptotically free logarithmic OPE coefficients; Borel transform for factorial perturbative growth; Chiral selection of spectral sum rules; Composite-operator normalization from a finite matrix element. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.altarelli-parisi-evolution-from-ope-moments`, `weinberg-2.asymptotically-free-ope-logarithmic-coefficients`, `weinberg-2.borel-transform-asymptotic-series-method`, `weinberg-2.chiral-current-operator-selection-for-sum-rules`, `weinberg-2.composite-operator-normalization-by-matrix-element`, `weinberg-2.current-spectral-functions-positivity-and-symmetry`, `weinberg-2.dis-flavor-mixing-and-strict-scaling-violation`, `weinberg-2.dis-ope-dispersion-connection`, `weinberg-2.dis-structure-functions-and-bjorken-limit`, `weinberg-2.finite-uv-fixed-point-ope-coefficients`, `weinberg-2.generalized-colliding-insertions-ope`, `weinberg-2.imported-chapter12-power-counting-theorem`, `weinberg-2.infrared-renormalons-from-ope-power-corrections`, `weinberg-2.instanton-negative-borel-singularity-example`, `weinberg-2.locality-path-integral-ope-derivation`, `weinberg-2.ope-coefficients-preserve-broken-symmetry`, `weinberg-2.parton-dis-compton-polarization-sum-input`, `weinberg-2.parton-model-dis-scaling-and-sum-rules`, `weinberg-2.parton-model-pre-cross-section-kinematic-inputs`, `weinberg-2.qcd-corrected-scaling-and-callan-gross`, `weinberg-2.rg-matrix-equation-for-ope-coefficients`, `weinberg-2.scalar-hard-flow-power-counting`, `weinberg-2.scalar-hard-subgraph-leading-phi2-ope`, `weinberg-2.scalar-one-loop-ope-factorization-check`, `weinberg-2.short-distance-operator-product-expansion`, `weinberg-2.short-distance-spectral-sum-rule-criterion`, `weinberg-2.state-independent-dis-coefficient-matching`, `weinberg-2.twist-and-leading-qcd-dis-operators`, `weinberg-2.two-particle-irreducible-induction-for-ope`, `weinberg-2.vector-axial-spectral-sum-rules`.

</details>

<details>
<summary>Section 20.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Generalized OPE for multiple colliding insertions; Locality-based path-integral route to the OPE; Short-distance operator product expansion. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.generalized-colliding-insertions-ope`, `weinberg-2.locality-path-integral-ope-derivation`, `weinberg-2.short-distance-operator-product-expansion`.

</details>

<details>
<summary>Section 20.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Composite-operator normalization from a finite matrix element; Imported Chapter 12 power-counting theorem; Scalar hard-flow power counting and bridge selection; Hard-subgraph origin of the leading φ² OPE term; One-loop off-shell check of scalar OPE factorization. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.composite-operator-normalization-by-matrix-element`, `weinberg-2.imported-chapter12-power-counting-theorem`, `weinberg-2.scalar-hard-flow-power-counting`, `weinberg-2.scalar-hard-subgraph-leading-phi2-ope`, `weinberg-2.scalar-one-loop-ope-factorization-check`, `weinberg-2.two-particle-irreducible-induction-for-ope`.

</details>

<details>
<summary>Section 20.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Asymptotically free logarithmic OPE coefficients; Finite-UV-fixed-point scaling of OPE coefficients; RG matrix evolution of OPE coefficient functions. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.asymptotically-free-ope-logarithmic-coefficients`, `weinberg-2.finite-uv-fixed-point-ope-coefficients`, `weinberg-2.rg-matrix-equation-for-ope-coefficients`.

</details>

<details>
<summary>Section 20.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: OPE coefficients preserve the full underlying symmetry. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.ope-coefficients-preserve-broken-symmetry`.

</details>

<details>
<summary>Section 20.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Chiral selection of spectral sum rules; Current spectral-function positivity and symmetry; Short-distance criterion for spectral-function sum rules; Vector–axial spectral sum rules. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.chiral-current-operator-selection-for-sum-rules`, `weinberg-2.current-spectral-functions-positivity-and-symmetry`, `weinberg-2.short-distance-spectral-sum-rule-criterion`, `weinberg-2.vector-axial-spectral-sum-rules`.

</details>

<details>
<summary>Section 20.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Altarelli–Parisi evolution from OPE moments; Flavor mixing and violation of strict Bjorken scaling; DIS OPE connection through the time-ordered tensor; DIS structure functions and Bjorken limit; Polarization-sum identity for the parton DIS derivation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.altarelli-parisi-evolution-from-ope-moments`, `weinberg-2.dis-flavor-mixing-and-strict-scaling-violation`, `weinberg-2.dis-ope-dispersion-connection`, `weinberg-2.dis-structure-functions-and-bjorken-limit`, `weinberg-2.parton-dis-compton-polarization-sum-input`, `weinberg-2.parton-model-dis-scaling-and-sum-rules`, `weinberg-2.parton-model-pre-cross-section-kinematic-inputs`, `weinberg-2.qcd-corrected-scaling-and-callan-gross`, `weinberg-2.state-independent-dis-coefficient-matching`, `weinberg-2.twist-and-leading-qcd-dis-operators`.

</details>

<details>
<summary>Section 20.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Borel transform for factorial perturbative growth; Infrared renormalons from OPE power corrections; Instanton origin of a negative-axis Borel singularity. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.borel-transform-asymptotic-series-method`, `weinberg-2.infrared-renormalons-from-ope-power-corrections`, `weinberg-2.instanton-negative-borel-singularity-example`.

</details>

<details>
<summary>Section 20.A — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: General hard-flow OPE from power counting; Qualification of the general hard-flow argument; Imported Chapter 12 power-counting theorem. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.general-hard-flow-ope-power-counting`, `weinberg-2.general-hard-flow-ope-rigor-qualification`, `weinberg-2.imported-chapter12-power-counting-theorem`.

</details>

<details>
<summary>Section 20.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: derive the parton-model DIS cross section; Problem: list twist-four QCD tensors; Problem: scalar–pseudoscalar spectral sum rules; Problem: scalar-theory renormalon singularity loci; Problem: Yukawa OPE operators and one-loop coefficients. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-derive-parton-dis-cross-section`, `weinberg-2.problem-list-twist-four-qcd-tensors`, `weinberg-2.problem-scalar-pseudoscalar-spectral-sum-rules`, `weinberg-2.problem-scalar-renormalon-singularity-loci`, `weinberg-2.problem-yukawa-ope-operators-and-one-loop-coefficients`.

</details>

<details>
<summary>Section 21 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: BCS effective electron theory near a Fermi surface; Elementary-scalar broken-gauge vector mass matrix and unbroken kernel; Renormalizable ξ-gauge fixing for a broken gauge theory; ξ-gauge spectrum, cancellation, and renormalizability qualification; CKM mixing from quark mass diagonalization and three-generation CP violation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bcs-effective-electron-theory-near-fermi-surface`, `weinberg-2.broken-gauge-vector-mass-matrix-kernel`, `weinberg-2.broken-theory-xi-gauge-fixing`, `weinberg-2.broken-theory-xi-spectrum-and-renormalizability`, `weinberg-2.ckm-mass-diagonalization-and-three-generation-cp-violation`, `weinberg-2.complex-scalar-vector-mass-matrix`, `weinberg-2.cooper-channel-marginality`, `weinberg-2.custodial-symmetry-electroweak-mass-ratio`, `weinberg-2.dynamical-breaking-covariant-building-blocks`, `weinberg-2.dynamical-breaking-low-energy-power-counting`, `weinberg-2.dynamically-broken-local-symmetry-small-gauge-coupling-framework`, `weinberg-2.electroweak-mixing-and-charged-neutral-vectors`, `weinberg-2.electroweak-precision-inputs-and-one-loop-mass-sensitivity`, `weinberg-2.electroweak-running-charge-neutral-current-tests`, `weinberg-2.electroweak-su2l-u1-lepton-representations`, `weinberg-2.general-unitarity-gauge-and-universal-vector-mass-formula`, `weinberg-2.gim-quark-doublets-and-flavor-changing-neutral-current-cancellation`, `weinberg-2.ginzburg-landau-order-parameter-and-length-scales`, `weinberg-2.grand-unification-generator-normalization-coupling-relation`, `weinberg-2.grand-unification-running-scale-and-proton-decay`, `weinberg-2.higgs-mechanism-local-goldstone-modes`, `weinberg-2.hubbard-stratonovich-pair-field-effective-action`, `weinberg-2.meissner-critical-field-and-flux-quantization`, `weinberg-2.microscopic-superconductor-goldstone-electromagnetic-effective-action`, `weinberg-2.pairing-instability-attractive-channel-debye-qualification`, `weinberg-2.renormalizable-standard-model-accidental-baryon-lepton-conservation-and-eft-limit`, `weinberg-2.renormalized-cooper-kernel-rg-and-eigenchannels`, `weinberg-2.spin-singlet-gap-effective-potential-and-gap-equation`, `weinberg-2.standard-model-dimension-five-neutrino-mass-operator`, `weinberg-2.standard-model-scalar-doublet-yukawa-breaking`, `weinberg-2.superconductor-u1-over-z2-goldstone-effective-action`, `weinberg-2.technicolor-dynamical-electroweak-breaking-qualification`, `weinberg-2.tree-electroweak-masses-and-fermi-scale`, `weinberg-2.unbroken-gauge-field-canonical-normalization-and-charge`, `weinberg-2.unitarity-gauge-goldstone-elimination`, `weinberg-2.unitarity-gauge-propagator-ultraviolet-limitation`, `weinberg-2.vortex-core-cylindrical-asymptotics`, `weinberg-2.vortex-flux-core-stability-and-type-classification`, `weinberg-2.vortex-state-field-ranges-and-flux-qualification`, `weinberg-2.xi-gauge-s-matrix-independence-and-unitarity-gauge-equivalence`, `weinberg-2.zero-gauge-coupling-vector-goldstone-exchange-equivalence`, `weinberg-2.zero-resistance-and-ac-josephson-effect`.

</details>

<details>
<summary>Section 21.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Elementary-scalar broken-gauge vector mass matrix and unbroken kernel; Vector mass matrix for a complex scalar representation; Unbroken gauge field: canonical normalization and charge; Unitarity gauge eliminates gauge Goldstone coordinates; Unitarity-gauge propagator ultraviolet limitation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.broken-gauge-vector-mass-matrix-kernel`, `weinberg-2.complex-scalar-vector-mass-matrix`, `weinberg-2.unbroken-gauge-field-canonical-normalization-and-charge`, `weinberg-2.unitarity-gauge-goldstone-elimination`, `weinberg-2.unitarity-gauge-propagator-ultraviolet-limitation`, `weinberg-2.zero-gauge-coupling-vector-goldstone-exchange-equivalence`.

</details>

<details>
<summary>Section 21.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Renormalizable ξ-gauge fixing for a broken gauge theory; ξ-gauge spectrum, cancellation, and renormalizability qualification; ξ-gauge S-matrix independence and unitarity-gauge equivalence. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.broken-theory-xi-gauge-fixing`, `weinberg-2.broken-theory-xi-spectrum-and-renormalizability`, `weinberg-2.xi-gauge-s-matrix-independence-and-unitarity-gauge-equivalence`.

</details>

<details>
<summary>Section 21.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: CKM mixing from quark mass diagonalization and three-generation CP violation; Electroweak mixing and W±, Z, photon fields; Electroweak precision inputs and one-loop top/Higgs sensitivity; Running-charge correction and neutral-current tests of electroweak theory; Electroweak SU(2)L × U(1) lepton representation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.ckm-mass-diagonalization-and-three-generation-cp-violation`, `weinberg-2.electroweak-mixing-and-charged-neutral-vectors`, `weinberg-2.electroweak-precision-inputs-and-one-loop-mass-sensitivity`, `weinberg-2.electroweak-running-charge-neutral-current-tests`, `weinberg-2.electroweak-su2l-u1-lepton-representations`, `weinberg-2.gim-quark-doublets-and-flavor-changing-neutral-current-cancellation`, `weinberg-2.renormalizable-standard-model-accidental-baryon-lepton-conservation-and-eft-limit`, `weinberg-2.standard-model-dimension-five-neutrino-mass-operator`, `weinberg-2.standard-model-scalar-doublet-yukawa-breaking`, `weinberg-2.tree-electroweak-masses-and-fermi-scale`.

</details>

<details>
<summary>Section 21.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Custodial symmetry and the electroweak W/Z mass ratio; Covariant building blocks for a dynamically broken gauge EFT; Low-energy power counting for dynamically broken gauge symmetry; Small-gauge-coupling framework for dynamically broken local symmetry; General unitarity gauge and universal vector mass formula. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.custodial-symmetry-electroweak-mass-ratio`, `weinberg-2.dynamical-breaking-covariant-building-blocks`, `weinberg-2.dynamical-breaking-low-energy-power-counting`, `weinberg-2.dynamically-broken-local-symmetry-small-gauge-coupling-framework`, `weinberg-2.general-unitarity-gauge-and-universal-vector-mass-formula`, `weinberg-2.technicolor-dynamical-electroweak-breaking-qualification`.

</details>

<details>
<summary>Section 21.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Grand-unified generator normalization and coupling relation; Running unification scale and suppressed baryon/lepton violation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.grand-unification-generator-normalization-coupling-relation`, `weinberg-2.grand-unification-running-scale-and-proton-decay`.

</details>

<details>
<summary>Section 21.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: BCS effective electron theory near a Fermi surface; Cooper-channel exception to Fermi-surface irrelevance; Ginzburg–Landau order parameter and superconducting length scales; Hubbard–Stratonovich pair field and exact effective action; Meissner effect, critical field, and flux quantization. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bcs-effective-electron-theory-near-fermi-surface`, `weinberg-2.cooper-channel-marginality`, `weinberg-2.ginzburg-landau-order-parameter-and-length-scales`, `weinberg-2.hubbard-stratonovich-pair-field-effective-action`, `weinberg-2.meissner-critical-field-and-flux-quantization`, `weinberg-2.microscopic-superconductor-goldstone-electromagnetic-effective-action`, `weinberg-2.pairing-instability-attractive-channel-debye-qualification`, `weinberg-2.renormalized-cooper-kernel-rg-and-eigenchannels`, `weinberg-2.spin-singlet-gap-effective-potential-and-gap-equation`, `weinberg-2.superconductor-u1-over-z2-goldstone-effective-action`, `weinberg-2.vortex-core-cylindrical-asymptotics`, `weinberg-2.vortex-flux-core-stability-and-type-classification`, `weinberg-2.vortex-state-field-ranges-and-flux-qualification`, `weinberg-2.zero-resistance-and-ac-josephson-effect`.

</details>

<details>
<summary>Section 21.A — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: Appendix construction of general unitarity gauge. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.appendix-general-unitarity-gauge-construction`.

</details>

<details>
<summary>Section 21.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: fourth generation and unification predictions; Problem: generalized unitarity-gauge ghost calculation; Problem: incommensurate condensate charges in a superconductor; Problem: lowest-order W and Z magnetic moments; Problem: one-loop Z and neutral-scalar muon anomalous moment. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-fourth-generation-unification-predictions`, `weinberg-2.problem-generalized-unitarity-gauge-ghost`, `weinberg-2.problem-incommensurate-condensate-charges`, `weinberg-2.problem-lowest-order-w-z-magnetic-moments`, `weinberg-2.problem-muon-anomalous-moment-z-neutral-scalar`, `weinberg-2.problem-triplet-higgs-electroweak-breaking`.

</details>

<details>
<summary>Section 22 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Radiative nonrenormalization and symmetry-allowed mass decoupling; Gauge algebras with automatic local anomaly absence; Anomaly-matched Goldstone effective action; AVV/AAA routing and exact gauge-invariant anomaly completions; Gauge versus chiral invariance in axial-current regularization. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adler-bardeen-radiative-and-mass-decoupling-qualification`, `weinberg-2.anomaly-free-gauge-algebras-and-standard-model-risk`, `weinberg-2.anomaly-matching-goldstone-effective-action`, `weinberg-2.avv-aaa-routing-and-gauge-invariant-completion`, `weinberg-2.axial-anomaly-gauge-chiral-regulator-tradeoff`, `weinberg-2.brst-cohomology-classification-of-local-anomalies`, `weinberg-2.bv-antibracket-anomaly-cohomology-and-all-orders-removal`, `weinberg-2.differential-form-consistency-derivation-of-symmetric-anomaly`, `weinberg-2.euclidean-fujikawa-spectrum-and-index-theorem`, `weinberg-2.fujikawa-fermionic-measure-chiral-variation`, `weinberg-2.fujikawa-gauge-invariant-regulator-abelian-anomaly`, `weinberg-2.gauge-anomaly-cancellation-d-symbol-condition`, `weinberg-2.general-left-handed-triangle-anomaly-setup`, `weinberg-2.h-anomaly-free-counterterm-goldstone-action`, `weinberg-2.hypercharge-anomaly-constraints-and-b-minus-l-extension`, `weinberg-2.left-handed-projector-two-triangle-integral`, `weinberg-2.local-and-global-chiral-determinant-obstructions`, `weinberg-2.n2-anomaly-matching-example-and-n3-obstruction`, `weinberg-2.pi0-two-photon-anomaly-color-prediction`, `weinberg-2.pi0-two-photon-chiral-suppression-puzzle`, `weinberg-2.pure-gauge-goldstone-wess-zumino-functional`, `weinberg-2.qcd-wess-zumino-witten-action-and-color-coefficient`, `weinberg-2.quantum-anomaly-regulator-symmetry-trace`, `weinberg-2.quantum-master-equation-measure-anomaly-repair`, `weinberg-2.standard-model-gauge-and-mixed-gravitational-cancellation`, `weinberg-2.stora-zumino-descent-and-schwinger-term-cohomology`, `weinberg-2.surface-term-evaluation-and-local-counterterm-obstruction`, `weinberg-2.symmetric-d-symbol-obstruction-to-three-current-conservation`, `weinberg-2.t-hooft-anomaly-matching-massless-bound-states`, `weinberg-2.t-hooft-decoupling-and-persistent-mass-qualifications`, `weinberg-2.t-hooft-matching-equations-and-three-flavor-qcd-breaking`, `weinberg-2.wess-zumino-consistency-condition-for-anomalies`.

</details>

<details>
<summary>Section 22.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: The chiral-suppression puzzle in π⁰ → 2γ. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.pi0-two-photon-chiral-suppression-puzzle`.

</details>

<details>
<summary>Section 22.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Gauge versus chiral invariance in axial-current regularization; Euclidean spectral derivation and the Dirac index; Fujikawa variation of the fermionic measure; Gauge-invariant Fujikawa regulator and Abelian anomaly; Anomaly prediction for π⁰ → 2γ and N_c. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.axial-anomaly-gauge-chiral-regulator-tradeoff`, `weinberg-2.euclidean-fujikawa-spectrum-and-index-theorem`, `weinberg-2.fujikawa-fermionic-measure-chiral-variation`, `weinberg-2.fujikawa-gauge-invariant-regulator-abelian-anomaly`, `weinberg-2.pi0-two-photon-anomaly-color-prediction`.

</details>

<details>
<summary>Section 22.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Radiative nonrenormalization and symmetry-allowed mass decoupling; AVV/AAA routing and exact gauge-invariant anomaly completions; General left-handed triangle-anomaly setup; Left-handed projector and the two-triangle current integral; Local and global obstructions to a chiral determinant. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.adler-bardeen-radiative-and-mass-decoupling-qualification`, `weinberg-2.avv-aaa-routing-and-gauge-invariant-completion`, `weinberg-2.general-left-handed-triangle-anomaly-setup`, `weinberg-2.left-handed-projector-two-triangle-integral`, `weinberg-2.local-and-global-chiral-determinant-obstructions`, `weinberg-2.surface-term-evaluation-and-local-counterterm-obstruction`, `weinberg-2.symmetric-d-symbol-obstruction-to-three-current-conservation`.

</details>

<details>
<summary>Section 22.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Gauge algebras with automatic local anomaly absence; Gauge-anomaly cancellation from D_{aβγ}=0; Hypercharge constraints and anomaly-free B−L extension; First-generation Standard Model gauge and gravitational cancellation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.anomaly-free-gauge-algebras-and-standard-model-risk`, `weinberg-2.gauge-anomaly-cancellation-d-symbol-condition`, `weinberg-2.hypercharge-anomaly-constraints-and-b-minus-l-extension`, `weinberg-2.standard-model-gauge-and-mixed-gravitational-cancellation`.

</details>

<details>
<summary>Section 22.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: n=2 matching example and n=3 obstruction; ’t Hooft matching requires massless bound states; Decoupling and persistent-mass qualifications; ’t Hooft matching equations for chiral bound states. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.n2-anomaly-matching-example-and-n3-obstruction`, `weinberg-2.t-hooft-anomaly-matching-massless-bound-states`, `weinberg-2.t-hooft-decoupling-and-persistent-mass-qualifications`, `weinberg-2.t-hooft-matching-equations-and-three-flavor-qcd-breaking`.

</details>

<details>
<summary>Section 22.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: BRST cohomology classification of local anomalies; BV antibracket anomaly cohomology and all-orders removal; Differential-form derivation of the symmetric anomaly; Quantum master equation repairs a non-invariant measure; Stora-Zumino descent and Schwinger-term candidates. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.brst-cohomology-classification-of-local-anomalies`, `weinberg-2.bv-antibracket-anomaly-cohomology-and-all-orders-removal`, `weinberg-2.differential-form-consistency-derivation-of-symmetric-anomaly`, `weinberg-2.quantum-master-equation-measure-anomaly-repair`, `weinberg-2.stora-zumino-descent-and-schwinger-term-cohomology`, `weinberg-2.wess-zumino-consistency-condition-for-anomalies`.

</details>

<details>
<summary>Section 22.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Anomaly-matched Goldstone effective action; Counterterm construction for G→H with anomaly-free H; Pure-gauge Goldstone Wess-Zumino functional; QCD Wess-Zumino-Witten action fixes its color coefficient. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.anomaly-matching-goldstone-effective-action`, `weinberg-2.h-anomaly-free-counterterm-goldstone-action`, `weinberg-2.pure-gauge-goldstone-wess-zumino-functional`, `weinberg-2.qcd-wess-zumino-witten-action-and-color-coefficient`.

</details>

<details>
<summary>Section 22.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: chiral SU(3) anomaly with symmetric tensors; Problem: η → γγ at leading order in m_s; Problem: ’t Hooft matching solutions for n=4 and n=2; Problem: Zinn-Justin equation from the quantum master equation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-chiral-su3-anomaly-with-symmetric-tensors`, `weinberg-2.problem-eta-to-two-photons-leading-ms`, `weinberg-2.problem-t-hooft-matching-n4-and-alternate-n2`, `weinberg-2.problem-zinn-justin-from-quantum-master-equation`.

</details>

<details>
<summary>Section 23 — covered</summary>

Accepted evidence.section assignments cover the chapter-wide distinct methods, results, qualifications, and task branches. Anchor records: Axion–pion effective Lagrangian and mass; Bounce negative mode, rate prefactor, and multi-bounce exponentiation; Bounce O(4) equation and positive action; BPS monopole radial solution and restored core; BPST instanton action, winding, and coupling convention. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.axion-pion-effective-lagrangian-and-mass`, `weinberg-2.bounce-negative-mode-rate-and-exponentiation`, `weinberg-2.bounce-ode-scaling-positivity`, `weinberg-2.bps-monopole-radial-solution`, `weinberg-2.bpst-instanton-action-and-normalization`, `weinberg-2.cartan-maurer-form-invariance`, `weinberg-2.cartan-maurer-standard-su2-normalization`, `weinberg-2.cluster-decomposition-fixes-theta-weights`, `weinberg-2.collective-coordinate-semiclassical-expansion`, `weinberg-2.cosmological-monopole-overabundance-report`, `weinberg-2.derrick-scaling-and-higher-derivative-balance`, `weinberg-2.dirac-patch-quantization-for-monopoles`, `weinberg-2.domain-wall-topological-bound-and-first-order-profile`, `weinberg-2.extended-configuration-physical-roles`, `weinberg-2.false-vacuum-euclidean-bounce-setup`, `weinberg-2.fermionic-zero-mode-selection`, `weinberg-2.finite-functional-topological-sectors`, `weinberg-2.fundamental-group-concatenation`, `weinberg-2.gauge-higgs-defect-classification-and-cores`, `weinberg-2.goldstone-boundary-compactification-and-homotopy`, `weinberg-2.higher-homotopy-products-and-winding`, `weinberg-2.instanton-anomaly-and-electroweak-selection-rules`, `weinberg-2.instanton-path-integral-suppression`, `weinberg-2.instanton-self-duality-and-topological-action-bound`, `weinberg-2.instanton-zero-mode-prefactor-counting`, `weinberg-2.monopole-embedding-and-covering-group-qualification`, `weinberg-2.monopole-flux-winding-and-bogomolnyi-bound`, `weinberg-2.peccei-quinn-axion-relaxation`, `weinberg-2.pure-gauge-asymptotics-and-instanton-dimension`, `weinberg-2.temporal-gauge-instanton-tunneling`, `weinberg-2.theta-term-chiral-rephasing-invariant`, `weinberg-2.thin-wall-bounce-approximation`, `weinberg-2.thooft-polyakov-finite-energy-and-electromagnetic-tensor`, `weinberg-2.unbroken-subgroup-reduction-at-d-four`.

</details>

<details>
<summary>Section 23.1 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Derrick scaling and higher-derivative stabilization; Domain-wall topological bound and first-order profile; Finite functional sectors and local minima; Gauge-Higgs defect classification and restored-symmetry cores; Goldstone boundary compactification and global homotopy class. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.derrick-scaling-and-higher-derivative-balance`, `weinberg-2.domain-wall-topological-bound-and-first-order-profile`, `weinberg-2.finite-functional-topological-sectors`, `weinberg-2.gauge-higgs-defect-classification-and-cores`, `weinberg-2.goldstone-boundary-compactification-and-homotopy`, `weinberg-2.pure-gauge-asymptotics-and-instanton-dimension`, `weinberg-2.unbroken-subgroup-reduction-at-d-four`.

</details>

<details>
<summary>Section 23.2 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Fundamental group by based-loop concatenation and vortex fusion; Higher homotopy products and winding conservation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.fundamental-group-concatenation`, `weinberg-2.higher-homotopy-products-and-winding`.

</details>

<details>
<summary>Section 23.3 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: BPS monopole radial solution and restored core; Reported cosmological monopole overabundance argument; Dirac patch quantization for monopoles; Monopole classification depends on subgroup embedding; Monopole flux–winding relation and Bogomol’nyi bound. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bps-monopole-radial-solution`, `weinberg-2.cosmological-monopole-overabundance-report`, `weinberg-2.dirac-patch-quantization-for-monopoles`, `weinberg-2.monopole-embedding-and-covering-group-qualification`, `weinberg-2.monopole-flux-winding-and-bogomolnyi-bound`, `weinberg-2.thooft-polyakov-finite-energy-and-electromagnetic-tensor`.

</details>

<details>
<summary>Section 23.4 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Cartan–Maurer integral invariant; Cartan–Maurer winding normalization in standard SU(2). The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.cartan-maurer-form-invariance`, `weinberg-2.cartan-maurer-standard-su2-normalization`.

</details>

<details>
<summary>Section 23.5 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: BPST instanton action, winding, and coupling convention; Instanton anomaly effects and electroweak selection rules; Instanton path-integral suppression and running-coupling qualification; Instanton self-duality and topological action bound; Temporal-gauge instanton as winding-sector tunneling. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bpst-instanton-action-and-normalization`, `weinberg-2.instanton-anomaly-and-electroweak-selection-rules`, `weinberg-2.instanton-path-integral-suppression`, `weinberg-2.instanton-self-duality-and-topological-action-bound`, `weinberg-2.temporal-gauge-instanton-tunneling`.

</details>

<details>
<summary>Section 23.6 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Axion–pion effective Lagrangian and mass; Cluster decomposition fixes winding-sector weights; Peccei–Quinn axion relaxation mechanism; Theta term and chiral-rephasing invariant. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.axion-pion-effective-lagrangian-and-mass`, `weinberg-2.cluster-decomposition-fixes-theta-weights`, `weinberg-2.peccei-quinn-axion-relaxation`, `weinberg-2.theta-term-chiral-rephasing-invariant`.

</details>

<details>
<summary>Section 23.7 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Collective-coordinate semiclassical expansion; Fermionic zero-mode saturation selection rule; Instanton prefactor from collective zero-mode counting. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.collective-coordinate-semiclassical-expansion`, `weinberg-2.fermionic-zero-mode-selection`, `weinberg-2.instanton-zero-mode-prefactor-counting`.

</details>

<details>
<summary>Section 23.8 — covered</summary>

Accepted evidence.section assignments cover the named subsection derivations, results, assumptions, and qualifications. Anchor records: Bounce negative mode, rate prefactor, and multi-bounce exponentiation; Bounce O(4) equation and positive action; False-vacuum Euclidean bounce setup; Thin-wall (big-bubble) bounce approximation. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.bounce-negative-mode-rate-and-exponentiation`, `weinberg-2.bounce-ode-scaling-positivity`, `weinberg-2.false-vacuum-euclidean-bounce-setup`, `weinberg-2.thin-wall-bounce-approximation`.

</details>

<details>
<summary>Section 23.A — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: Euclidean canonical amplitude and ground-state limit; Euclidean phase-space path integral and nonunitary eigenstates; Quadratic-momentum Euclidean configuration integral. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.euclidean-canonical-amplitude-and-ground-state-limit`, `weinberg-2.euclidean-phase-space-path-integral`, `weinberg-2.quadratic-momentum-euclidean-configuration-integral`.

</details>

<details>
<summary>Section 23.B — covered</summary>

Accepted evidence.section assignments cover the appendix construction and its stated proof/reporting scope. Anchor records: Reported homotopy table and coset kernel rule. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.homotopy-reference-table-and-coset-kernel`.

</details>

<details>
<summary>Section 23.problems — covered</summary>

Accepted evidence.section assignments cover independent source tasks and their scoped input routes. Anchor records: Problem: stabilize 4D Euclidean Goldstone topology; Problem: prove π_n(M) Abelian for n>1; Problem: six-dimensional SU(2) skyrmion conservation; Problem: axion mass for small u,d,s masses; Problem: SU(4) unit-instanton coupling dependence. The full list follows semantic section labels; shared boundary-page content remains in every applicable accepted treatment. Table and equation numbers were not treated as section identifiers.

Records: `weinberg-2.problem-four-dimensional-skyrmion-stabilization`, `weinberg-2.problem-prove-higher-homotopy-abelian`, `weinberg-2.problem-six-space-dimensional-skyrmion-conservation`, `weinberg-2.problem-small-three-flavor-axion-mass`, `weinberg-2.problem-su4-unit-instanton-coupling`, `weinberg-2.problem-tilted-quartic-vacuum-decay`.

</details>
