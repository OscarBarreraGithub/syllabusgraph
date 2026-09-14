# Where files go

Run `syllabusgraph init local-courses/my-course --title "My course"`. Every new
project starts with the same structure, an empty source bibliography and graph,
and a draft course plan. The optional `--template sampling` provides the included
self-authored example instead.

The name `my-course` is yours to choose. A project can live outside the tool's
checkout as well. No private course name or textbook inventory is copied into
a new blank project.

| Location, relative to the project | What belongs here | Sharing behavior |
|---|---|---|
| `README.md` | Instructions for using this workspace | Generic instructions; may be shared |
| `materials/` | Source PDFs, UTF-8 text, Markdown notes, and optional subfolders | Ignored by Git |
| `materials/README.md` | An optional inventory of local filenames and their roles | Ignored by Git |
| `materials/prior-work/` | Optional existing notes, candidate graphs, or related work | Ignored; create this subfolder when needed |
| `COURSE_GUIDANCE.md` | Audience, goals, entry background, scope, source priorities, and review directions | Ignored by Git; a human-readable brief |
| `project.yaml` | Public-facing title, source bibliography, mastery levels, and relative data paths | Candidate for sharing after inspection |
| `knowledge/graph.yaml` | Reviewed concepts, relationships, original summaries, and citations | Candidate for sharing after review |
| `plans/` | Course outcomes, background, teaching time, and ordering choices | Candidate for sharing after review |
| `.syllabusgraph/sources/` | Attached working copies, page text, and source registrations | Ignored by Git |
| `.syllabusgraph/runs/` | Prepared packets, proposals, quote witnesses, critiques, reviews, and receipts | Ignored by Git |
| `.syllabusgraph/build/` | Generated syllabi, preparation scaffolds, JSON, and Mermaid exports | Ignored by default; selected reviewed exports may be shared |

Inside a tool checkout, `local-courses/` is itself ignored, so the entire working
course stays out of software commits. A separately published course uses selected,
reviewed data files as described in the [sharing guide](sharing.md).

## From files to a source unit

1. Put references in `materials/`. Keep meaningful filenames; no special naming
   pattern is required. You can record a local inventory in `materials/README.md`.
2. Record the intended course in `COURSE_GUIDANCE.md`, or have the person or agent
   doing the work record the guidance you give them. It is not parsed or enforced
   by the engine; agreed choices become course data and extraction scopes later.
3. In **References**, add a bibliography entry if needed, then use **Attach file**
   on its card and confirm the edition's printed-page mapping. You can select a
   file anywhere on your computer without moving it into `materials/` first.
4. In **Source workflow**, prepare a bounded page range. Follow the
   [extraction and review workflow](source-workflow.md) before promoting a graph.

Copying files into the folder does not attach them or start extraction. A prior
graph is candidate material to inspect against sources; it is not automatically
accepted as reviewed knowledge. When working with an agent, provide scope and
review criteria before asking it to start.

## Existing workspaces

Existing projects still load without the optional folder and brief. To adopt
the convention, add `materials/` and `/COURSE_GUIDANCE.md` to the project's
`.gitignore`, then create those files and folders. Existing registered sources
continue working in their current storage. Changes to the software do not
overwrite your existing course guidance or reference files.
