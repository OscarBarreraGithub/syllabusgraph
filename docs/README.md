# Documentation

SyllabusGraph separates reusable software, locally supplied sources, and reviewed
course data. These pages are maintained alongside the implementation. They are
the source for a future documentation site or wiki; no separate wiki is maintained.

## Start a course

| Guide | What it answers |
|---|---|
| [Quickstart](../README.md#try-it) | How to install and run the included example |
| [File locations](file-locations.md) | Where books, guidance, prior work, graphs, and outputs belong |
| [Source workflow](source-workflow.md) | How to prepare, extract, check, review, promote, and resume |
| [PDF reading](pdf-reading.md) | Set up and diagnose private, page-faithful PDF reading without fixing one tool stack |
| [Project format](project-format.md) | How bibliography, concepts, evidence, and course plans are represented |
| [Sharing a course](sharing.md) | Which reviewed results can be published and which files stay local |
| [Native agent setup](agent-setup.md) | Configure and audit bounded Codex or Claude source work |
| [Time and usage](usage-estimates.md) | Record model calls, elapsed time, available token counters, and their measurement limits |
| [Graph bank](../graphs/README.md) | Reuse or contribute independent textbook graphs and compare reviewed correspondences |

## Understand and maintain the tool

| Record | Purpose |
|---|---|
| [Capability register](capabilities.md) | Current functionality, interfaces, evidence, and limits |
| [Architecture](architecture.md) | Engine boundaries, planning behavior, and storage design |
| [Roadmap](roadmap.md) | Proposed work, kept separate from working features |
| [Changelog](../CHANGELOG.md) | Changes to behavior and project setup |
| [Release checks](releasing.md) | Tests, package checks, and publication audit |
| [Contributing](../CONTRIBUTING.md) | How changes are proposed and documented |

## Examples

The [sampling example](../examples/sampling/project.yaml) includes original source
text and a runnable graph. The [QFT graph collection](../graphs/subjects/qft/README.md)
contains separate textbook projects and a shared graph, with bounded coverage
and review records; course plans are a later step. Source books are supplied
privately. Examples are separate from
the blank project created for a new subject.

- [Agent setup](agent-setup.md): clone-first onboarding, configurable native roles, mandatory critique, and final audit.
