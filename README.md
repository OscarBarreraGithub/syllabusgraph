# SyllabusGraph

**Turn source material into a map of ideas, then shape a course around it.**

![SyllabusGraph: bring your own material and copy one setup prompt](docs/home.png)

Bring your references. Your coding agent handles installation, extraction, and
independent review. You decide what to cover and, later, what to teach.

| Bring | Connect | Shape | Share |
|---|---|---|---|
| Drop your material into a private folder. | Build concepts and relationships with source evidence. | Choose goals, background, and time. | Publish graphs and course plans; keep the books private. |

## Get started

Paste this into **Codex or Claude Code**:

```text
Get me set up with SyllabusGraph. Read and follow
https://github.com/OscarBarreraGithub/syllabusgraph/blob/main/SETUP.md
Handle the technical setup for me, then show me where to put my materials.
Use the slow, checkpointed mode. Ask about scope and model choices before extraction.
```

Your agent opens the local website, creates your workspace, and explains the
next step. You don't need an API key to browse existing graphs. Extraction uses
your coding agent's model access: Terra/high + Sol/high by default in Codex,
Sonnet + Opus in Claude. The choices are configurable; an independent critic is required.

> **Graph creation can use a lot of your model allowance.** Start with a few
> pages. Slow mode allows two worker dispatches per session, with one worker
> at a time, then pauses. Resume whenever you choose—even weeks later.
> These are call limits, **not a token or spending cap**. One call and the
> orchestrator can still use substantial allowance. Nothing runs in the background.

To continue another day, tell your agent: **“Resume my SyllabusGraph project for
one slow session. Read its saved state first.”**

## Explore the example

The [QFT demo](graphs/subjects/qft/concepts/README.md) organizes **2,351 book
records into 117 concepts**. **82 concepts have treatments in all three works**:
Peskin–Schroeder, Schwartz, and Weinberg I + II. Each book keeps its own graph.

![The shared QFT concepts, with book treatments one click away](docs/atlas.png)

Choose **Explore the demo → Open the concept map**. Start with 27 landmarks,
show the full inventory, compare the books, or follow a connection to its source
evidence. The original records and detailed shared graph remain accessible.
No course has been chosen; browsing makes no model calls.

The concept assignments are model-reviewed; human audit is pending. Coverage
means a book has an associated treatment, not that its derivation is identical.
[Review, scope, and reproducible counts](graphs/subjects/qft/concepts/README.md).

[Field guide / docs](docs/README.md) · [Graph library](graphs/README.md) ·
[Usage & run history](docs/usage-estimates.md) · [Contribute](CONTRIBUTING.md)

To have your agent explain the documentation, paste:

```text
Read https://github.com/OscarBarreraGithub/syllabusgraph/blob/main/docs/README.md
and explain the next step for my SyllabusGraph project. Inspect saved work first;
do not start extraction or renew a work budget just to answer.
```

MIT licensed. Source books are supplied locally and are not distributed here.
