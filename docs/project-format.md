# Project format, version 1

Every project contains `project.yaml`, a knowledge file, and a directory of
course-plan YAML files. Paths are relative to the project root and cannot
escape it. Duplicate YAML keys, unknown fields, missing references, duplicate
IDs, invalid timing ranges, and prerequisite cycles are rejected. The executable
contract is [project.schema.json](../src/syllabusgraph/schemas/project.schema.json).

```yaml
schema_version: 1
id: my-subject
title: My subject
description: The scope of this knowledge base.
mastery_levels: [recognize, use, derive]
sources: []
knowledge: knowledge/graph.yaml
plans_dir: plans
```

Mastery level names are configurable and ordered from least to most demanding.
All plans and dependencies must use this same order. The supplied defaults are
suited to technical subjects; choose appropriate labels and review criteria
for other disciplines.

## Sources and evidence

A source has an ID, title, authors, and status (`expected` or `available`).
Edition, volume, year, URL, and description are optional. `available` describes
the reference catalog; actual local attachment status is tracked separately.
An optional `public_file` identifies original/openly included project material.
Regular textbooks are attached through local registration and have no tracked
file path. Source entries must be created before they are cited.

Evidence records identify a source, a section, and printed pages:

```yaml
source: reference-one
section: "2.3 Expected values"
pages: [18, 19]
note: A short, original description of the supporting argument.
```

The note is optional. A citation is not a substitute for reading the source.
Print-to-PDF mappings and file checksums live in ignored local registration.
The current format uses positive integer printed pages; for documents with
other locators, create a documented, stable numbered text export first.

## Knowledge

The knowledge file contains four lists: `nodes`, `edges`, `groups`, and
`motivations`. All may initially be empty.

A node has `id`, `label`, `summary`, `kind`, and evidence. Kinds are concept,
method, result, assumption, or representation. Optional fields are `group`,
source-specific `notation` records, and timing `estimates` keyed by mastery.

```yaml
estimates:
  use:
    min: 15
    max: 25
    basis: Instructor estimate for one explanation and a worked example.
```

Ranges are minutes. Absence means unknown, not zero. Avoid claiming calibrated
time without a recorded teaching evaluation.

An edge has an ID, `from`, `to`, `relation`, `source_level`, `target_level`,
`necessity`, `rationale`, `failure_mode`, and evidence. Necessity is necessary,
typical, or helpful. Relations are prerequisite, alternative, evidence, or
pedagogical. Only prerequisites drive closure/order. Do not promote a mere
textbook presentation sequence into a compulsory dependency.

Groups have ID/title and optionally an organizing question. Motivations have
ID, concept IDs in `nodes`, an original source-backed `summary`, and evidence.
The public knowledge format contains no verbatim quotation field; local
proposals keep quotation witnesses separately for source checking.

## Course plans

Required fields: `id`, `title`, `status` (draft/ready), `audience`, `sessions`,
`minutes_per_session`, `outcomes`, and `background`.

```yaml
id: course-one
title: Course one
status: draft
audience: Students with the declared entry background.
sessions: 12
minutes_per_session: 60
outcomes:
  - node: subject.topic
    level: use
    assessment: Solve a representative problem and explain the assumptions.
background:
  subject.foundation: use
```

The IDs above are illustrative; they must exist in your knowledge base before
validation. Each outcome concept appears once and has an assessment description.

Optional fields:

| Field | Meaning |
|---|---|
| `description` | Course overview |
| `include` | Additional selected concept → mastery map |
| `treatments` | Desired treatment overrides; cannot silently weaken outcomes or prerequisites |
| `prior_plans` | Earlier courses whose explicit outcomes are assumed |
| `unknown` | Concepts explicitly not assumed, overriding inherited or explicit background |
| `omit` | Deliberately excluded concepts; required omissions produce blocking issues |
| `group_order` | Preferred narrative order of topic-group IDs |
| `necessity` | Dependency strengths to include; default necessary and typical |
| `notes` | Instructor-authored course notes |

The UI edits selected topics, depth, outcome assessments, background, and
session parameters. Add or rename plans and edit narrative order in YAML.
An empty draft is valid while its knowledge base is being built. Marking a plan
ready is an instructor declaration, not an automatic certification.
