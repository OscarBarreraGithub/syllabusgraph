# Preparing the QFT example

The QFT template is ready to receive material. It does not yet contain an
extracted or reviewed physics graph, nor a finished QFT I/II syllabus.

```bash
syllabusgraph init local-courses/qft --template qft
syllabusgraph serve -p local-courses/qft --open
```

Put the books in **`local-courses/qft/materials/`**. In the app's **References**
tab, choose **Attach file** on the corresponding book's card, select its file,
and confirm the page offset. You can also attach a file from any other local
directory. Placing a file in the folder alone does not register or extract it.

This is the same `materials/` convention used by every course. The template adds
the QFT bibliography and two plan files; the engine and storage rules are shared.
`examples/qft/` holds the reusable template, while the `init` destination holds
your working project. Its generated `README.md` explains this workflow and its
`.gitignore` excludes the materials and processing data.

Its reference shelf contains Weinberg volumes I and II, Peskin–Schroeder, and
Schwartz. These are expected sources, not bundled files. Confirm the exact
editions and volumes against the uploaded materials before editing their
metadata or preparing page ranges. Add any further source volumes explicitly.

## Before extraction

Set the intended audience and entry mastery, the available teaching time, the
desired calculations and conceptual outcomes, and the intended boundary
between QFT I and QFT II. The template's 24 sessions of 90 minutes are editable
placeholders, not a recommendation about what constitutes a complete course.

Attach material through References or `source register`. Verify printed-page
mappings on actual pages. Start with one coherent unit and complete the entire
extract/check/review/promote process before extending the scope.

The books should provide source evidence, treatments, and different expert
routes through the subject. Their presentation orders do not automatically
become prerequisites. Keep notation differences and alternative derivations
visible. Prior graphs can be useful candidate inventories, but imported claims
must satisfy the same evidence and review standard as new proposals.

## Two courses, one knowledge base

Both plan files refer to the shared `knowledge/graph.yaml`. As concepts are
reviewed, define explicit QFT I outcomes with assessment descriptions. Once its
plan is ready, QFT II can use those stated outcomes as entry assumptions through
`prior_plans: [qft-i]`. This is a declared entry requirement; it does not certify
that individual students have acquired it.

Establish the quality of the plans with instructor review, representative
worked problems, assessment alignment, actual lecture preparation, and eventual
teaching feedback. Acyclic structure alone cannot establish an optimal course.

## Intended first joint session

1. Confirm editions and source mappings after uploads.
2. Define one bounded learning outcome and its expected mastery.
3. Prepare its relevant source pages and review a small concept proposal.
4. Promote the accepted records and open the course designer.
5. Change assumptions and treatment depth; inspect how the prerequisites change.
6. Export the preparation scaffold and identify what an actual lecture still needs.

The sampling example remains the runnable end-to-end course demo while this
source-backed QFT knowledge base is developed.
