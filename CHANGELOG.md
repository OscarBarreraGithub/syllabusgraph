# Changelog

User-visible changes are recorded here. Current capability details and limits
live in [the capability register](docs/capabilities.md). A section here does not
imply a package has been published to a package index.

## Unreleased

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
