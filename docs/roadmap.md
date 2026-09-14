# Roadmap

These are candidate extensions, not promised or implemented features. Current
behavior and verification are tracked in the [capability register](capabilities.md).
Choose priorities based on actual course-building experience.

| Area | Proposed work | Evidence needed before calling it complete |
|---|---|---|
| Source extraction | Optional model adapters with explicit provider configuration and useful failure recovery | A documented installation path, protocol tests, and successful reviewed extraction on representative sources |
| PDF fidelity | OCR support, difficult notation handling, and more flexible page mappings | Original-page comparison, visible uncertainty, and tests against permitted representative fixtures |
| Review interface | Edit proposals, inspect evidence, record critique, and promote accepted records in the app | The same stale-review, conflict, and atomic-promotion protections as the CLI |
| Course examples | Publish reviewed graphs, original conclusions, and course plans from real source workflows | Content review, runnable builds without private caches, and confirmation that books and raw extracts are excluded |
| Documentation | Publish the repository's guides as a docs site or wiki | Stable navigation, valid links, version correspondence, and a single maintained source of truth |
| Teaching evaluation | Improve time estimates, assessment alignment, and sequencing based on use | Instructor feedback, worked assessments, and recorded evidence from actual teaching |
| Sharing and collaboration | Easier export of reviewed project files; consider hosted collaboration separately | Clear file boundaries; for hosting, authentication, authorization, persistence, and concurrency design |

New work should update the capability register and changelog when it becomes
usable. Do not move a feature to implemented status solely because its interface
or documentation exists.
