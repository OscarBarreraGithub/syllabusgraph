# Changelog

User-visible changes are recorded here. Current capability details and limits
live in [the capability register](docs/capabilities.md). A section here does not
imply a package has been published to a package index.

## Unreleased

- Add clone-first Codex/Claude instructions and native role profiles. Default to
  Terra high extraction with mandatory Sol high critique/adjudication, or Sonnet
  high extraction with Opus high critique/adjudication. Roles are configurable.
- Add orchestrator dispatch contracts, runtime completion records, bounded
  revisions, documented adjudication of conflicting graph records, and a fresh
  independent critic gate. Promotion rejects stale policy/proposal/base reviews
  and later critic rejection, including after an earlier acceptance.
- Add a local final audit with complete decision history and snapshot-bound
  human review, plus an explicit trust-critic mode. No per-unit human approval.
- Migration: manual imports remain drafts; existing manual acceptances need
  recorded extraction and configured critic dispatches before new promotion.

- Keep blank-course setup independent of private course examples. The CLI offers
  the blank project and self-authored sampling example; existing course projects
  still load through their project files.
- Replace a bundled course-specific scaffold with a separate example-status note.
  Reviewed example results may be published later; source books remain local.
- Create a private `COURSE_GUIDANCE.md` in new workspaces, with audience, scope,
  reference priorities, and first-unit planning prompts.
- Add a documentation index, file-location and sharing guides, capability
  register, and roadmap. These are maintained with the code for future docs use.

## 0.1.0 — initial toolkit

- Add validated subject knowledge, mastery-sensitive prerequisite planning,
  course inheritance, time estimates, graph visualization, and exports.
- Add local source registration and resumable prepare, extract/import, check,
  review, and promote operations.
- Provide the local course designer, original sampling demo, locked installation
  instructions, distribution builds, and cross-platform/browser checks.
- Add a README workflow illustration, a standard private `materials/` folder,
  generated project instructions, and publication screening.
