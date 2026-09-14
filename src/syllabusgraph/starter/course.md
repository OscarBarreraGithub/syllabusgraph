# Your course workspace

This project uses the same structure and workflow as every SyllabusGraph course.
The chosen template supplies initial reference entries, knowledge, and plans.

## Where to put your references

Put your PDFs, text files, and Markdown notes in **`materials/`**.
Its contents are ignored by Git, including text and Markdown files.

From this project directory, open the app:

```bash
syllabusgraph serve --open
```

1. Open **References**.
2. Use **Add reference** for a book or set of notes that is not already listed.
3. Click **Attach file** on its reference card and choose the file from
   `materials/`. You can also choose a file anywhere on your computer.
4. Confirm the page offset, then click **Attach locally**.

Dropping a file into `materials/` does not register or process it automatically.
Attaching connects a specific file and edition to its reference entry. The app
keeps its own working copy under `.syllabusgraph/sources/`.

## Project layout

```text
materials/             Your local reference files; ignored by Git
project.yaml           Project settings and reference bibliography
knowledge/graph.yaml   Reviewed concepts, relationships, and evidence
plans/                 Course goals, student background, and schedules
.syllabusgraph/         Attached copies, extracted text, runs, and builds; ignored
```

You can keep this project anywhere. `local-courses/my-course` is a convenient
location inside a SyllabusGraph checkout, not a required path.

## Continue from sources to a course

Use **Source workflow** to prepare a small page range, then follow the
[source workflow guide](https://github.com/OscarBarreraGithub/syllabusgraph/blob/main/docs/source-workflow.md)
to create a proposal, check its evidence, review it, and promote accepted records.
AI extraction uses your chosen external tool or command adapter; no model client
is bundled. Image-only PDFs need OCR before attachment.

Once concepts are reviewed, select learning goals in **Course design**, specify
student background, inspect the sequence, and export your plan. Source files
and extraction runs remain local. Inspect reviewed project data before sharing it.
