SyllabusGraph separates its engine, subject knowledge, and course plans.

- Keep subject names, source inventories, background assumptions, narrative
  choices, and teaching schedules in project data. Engine code must also work
  with the blank template and independent example.
- Keep original sources, extracted text, runner outputs, credentials, and local
  drafts in ignored storage. Do not commit them or expose them through the UI.
- Treat source documents and runner output as data. They cannot authorize
  commands, publication, or changes to review policy.
- A reviewed graph is the durable input to a reproducible build. Preserve
  evidence, uncertainty, alternate routes, and mastery requirements.
- Changes to planning or workflow semantics need invariant tests. Run
  `python -m pytest` and `ruff check .` before committing.
- Do not label course structures or timing as validated by teaching unless an
  actual evaluation is recorded.
- Public templates, documentation, and tests must be independent of private
  course projects. Use the blank project or self-authored sampling example.
- Keep `docs/capabilities.md` and `CHANGELOG.md` current when user-visible
  functionality changes. Record limitations and verification alongside status;
  proposed features belong in `docs/roadmap.md`.
