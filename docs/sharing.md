# Share reviewed results, keep source books local

A course's knowledge graph, original conclusions, bibliography, citations, and
course plans can be public. Raw source books and the private processing workspace
are separate inputs and working records.

| Publish after review | Keep local |
|---|---|
| `project.yaml` with bibliographic metadata | Textbook PDFs and other supplied source files |
| `knowledge/graph.yaml` with original summaries and source citations | Raw extracted text, copied passages, and quote witnesses |
| Course-plan YAML files in `plans/` | Prepared source packets, runner logs, critiques, and review notes |
| Selected syllabus, diagram, JSON, or preparation exports | `COURSE_GUIDANCE.md` and private planning conversations |
| A short example README explaining scope and current status | Local inventories, credentials, source caches, and registrations |

The generated `.gitignore` excludes `materials/`, `COURSE_GUIDANCE.md`, and
`.syllabusgraph/`, including text and Markdown inside the private directories.
Within a SyllabusGraph checkout, `local-courses/` is excluded too. Git ignore
rules do not remove files that were already tracked or prevent explicit force-adds.
Inspect the staged files before publishing a course.

## Prepare a public example

1. Finish the source checks and substantive review for the records you intend
   to share. Write original summaries and conclusions, retaining bibliographic
   citations; do not embed source books or copied source text in graph records.
2. Select the project configuration, reviewed graph, and relevant plan files
   into a separate public example or course repository. Keep their relative paths
   valid. Do not copy the whole working directory.
3. Include a README describing the audience, scope, supported outcomes, source
   editions, review status, and limits. Leave claims about teaching effectiveness
   unverified unless there is actual evaluation evidence.
4. Run `syllabusgraph validate -p <public-project>` and
   `syllabusgraph build -p <public-project> --strict` there. A published reviewed
   graph can be planned and exported without the original books or local caches;
   further extraction requires the reader's own source files.
5. Inspect the exact files, exports, and Git history before publishing. Use the
   [release checks](releasing.md) and publication audit as screening aids.

Original sample text that is intentionally distributed, such as the included
sampling primer, can use `public_file` in its reference metadata. Remove local
source-file bindings from public configurations. The source bibliography and
page citations remain useful without distributing the underlying textbooks.

Course-specific examples can live in their own clearly identified directories.
They do not change the blank project's defaults, instructions, or source list.
