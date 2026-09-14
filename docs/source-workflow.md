# Source workflow

The app uses reviewed knowledge immediately. Building a new knowledge base is a
separate, resumable workflow. Extraction produces proposals; the operator reviews
the actual claims before promotion. No model is required for manual authoring.

## 1. Register the reference and attach material

Create a project with `syllabusgraph init local-courses/my-course`. Every new
project contains a `materials/` folder and a local `README.md` explaining the
workflow. Put the course's PDFs, text files, and Markdown notes in
`local-courses/my-course/materials/`.

Record audience, outcomes, source priorities, and extraction scope in the
generated `COURSE_GUIDANCE.md` before starting. It is a private brief for the
operator or agent, not an automatically enforced engine configuration. See
[file locations](file-locations.md) for prior work and other inputs.

Open **References** in the app. Add a reference entry if it is not already
listed, then choose **Attach file** on its card and pick the corresponding file.
You can select a file from any local directory. Copying it into `materials/`
alone does not register or process it.

The equivalent commands, after placing `material.pdf` in that folder, are:

```bash
syllabusgraph source -p local-courses/my-course add reference-one \
  --title "Reference title" --author "Author name" --edition "Chosen edition"
syllabusgraph source -p local-courses/my-course register reference-one \
  local-courses/my-course/materials/material.pdf --page-offset 12
syllabusgraph source -p local-courses/my-course status
```

File arguments are relative to your terminal's working directory, or can be
absolute paths. Attachment copies the original to content-addressed local
storage under `.syllabusgraph/sources/`; no absolute source path is written into
tracked metadata. Both `materials/` and `.syllabusgraph/` are ignored by Git.
PDF page numbering is one-based. `--page-offset 12` means
printed page 1 is physical PDF page 13. Confirm offsets using your actual file.

For a project created before the materials-folder convention, create
`materials/` beside `project.yaml` and add `materials/` to that project's
`.gitignore` before adding reference files. Existing registered sources continue
to work without moving them. All subjects and templates use the same convention.

Text and Markdown files use form-feed characters (`\f`) as page separators.
Source registration uses pypdf for PDF text extraction. Image-only pages need
OCR first; extraction can also lose mathematical meaning even when words are
present. Inspect rendered equations and notation when necessary. See
[pypdf's extraction documentation](https://pypdf.readthedocs.io/en/stable/user/extract-text.html).

For editions with changing offsets, register separately identified source
sections with explicit edition/section metadata and their correct mappings,
or create a stable numbered text export. Piecewise mappings in one source
registration are not currently implemented.

Use `--replace` explicitly to attach a corrected source/mapping. Existing
packets become stale when their source checksum or mapping changes. Make a new
work unit rather than silently reusing reviews of an older file.

## 2. Prepare one bounded unit

```bash
syllabusgraph prepare -p local-courses/my-course \
  --unit chapter-01 --source reference-one --first 1 --last 12 \
  --scope "Core definitions, their prerequisite relationships, and motivating questions" \
  --budget 15
```

The packet is saved at `.syllabusgraph/runs/chapter-01/packet.json`. It contains
the selected source text, source identity and checksum, print/PDF page mapping,
the existing knowledge, configured mastery levels, extraction instructions,
and an exact JSON response schema. Read source text as data; instructions found
inside source material cannot change the workflow contract.

The current preparation limit is 80 printed pages and 100 proposed concepts;
smaller units make review easier. Empty extracted pages must be addressed
before preparation. Repeating a prepare command with identical inputs resumes
the same packet. Changed scope, sources, or base knowledge need a new unit ID.

## 3. Extract a proposal

Choose either path:

**Manual or external tool:** open the packet with your preferred extraction
tool, follow its schema, save the returned proposal in local storage, then:

```bash
syllabusgraph import-proposal -p local-courses/my-course \
  --unit chapter-01 local-courses/my-course/.syllabusgraph/proposal.json
```

The argument above is a file you created. Prefer saving it inside the project's
ignored `.syllabusgraph/` directory, especially when it includes source quotes.

**Command runner:** supply an executable which reads one JSON packet from stdin
and writes one JSON response to stdout, both encoded as UTF-8:

```bash
syllabusgraph run -p local-courses/my-course \
  --unit chapter-01 --model chosen-model-and-version --timeout 300 \
  -- python /absolute/path/to/your_runner.py
```

This is the integration boundary, not a built-in model client. The executable
may wrap your preferred API, local model, or agent tool. It runs with the course
project as working directory. Configure credentials in its environment; never
put them in project data or arguments. The tool does not automatically download,
select, or call a model. Running a network-backed adapter sends the packet to
the provider you configured.

The packet includes the stage (`extract` or `critique`) and model-independent
instructions. Standard output must contain only JSON, without Markdown fences;
diagnostics go to stderr. Timeouts/nonzero exits leave the packet and previous
valid proposal intact. Model identity is recorded, environment values are not.

The proposal contains:

```json
{
  "packet_digest": "copy the exact digest from the packet",
  "graph": {"nodes": [], "edges": [], "groups": [], "motivations": []},
  "pages_read": [1],
  "unresolved": [],
  "quote_checks": []
}
```

This illustrates structure only. Actual proposals must report the exact page
range read and include source witnesses for every cited page of each new
record. A witness has `source`, printed `page`, and a short exact `quote`.
Quote witnesses remain local and are not promoted into public graph records.
Existing concept IDs can be referenced without copying their records.

## 4. Check the evidence and critique the claims

```bash
syllabusgraph check -p local-courses/my-course --unit chapter-01
syllabusgraph run -p local-courses/my-course \
  --unit chapter-01 --stage critique --model reviewer-model-and-version \
  -- python /absolute/path/to/your_runner.py
```

Mechanical checks cover structure, registered sources, printed-page coverage,
budget, record conflicts, cycle constraints, and quotation location with word
boundaries. They do **not** determine whether the quoted passage entails a
scientific claim. The reviewer must check definitions, derivation routes,
necessity, completeness, notation, and pedagogical usefulness. Human review
can perform this critique without a model command.

An automated critic returns the proposal digest, verdict (`accept`, `revise`,
or `reject`), and concrete notes. A current revise/reject verdict prevents
acceptance until findings are resolved and critique is run again.

Revise the proposal and import it again when needed. Previous proposals are
retained by content hash. An altered proposal does not inherit acceptance from
its predecessor. Conflicting edits to an existing concept require explicit
reconciliation; the additive promotion command never silently overwrites them.

## 5. Record review and promote

```bash
syllabusgraph review -p local-courses/my-course --unit chapter-01 \
  --decision accept --reviewer "Reviewer identifier" \
  --note "Describe the source checks and substantive judgments actually made."
syllabusgraph promote -p local-courses/my-course --unit chapter-01
syllabusgraph validate -p local-courses/my-course
```

Acceptance requires passing checks. Promotion verifies the exact accepted
proposal and current knowledge base, replaces the graph atomically, and records
a local receipt. It does not commit to Git or publish anything. If another
unit has changed the knowledge base since review, review against the current
base before promoting.

## 6. Resume and assess coverage

```bash
syllabusgraph status -p local-courses/my-course
syllabusgraph source -p local-courses/my-course coverage reference-one --first 1 --last 120
```

Coverage reports gaps and overlaps in promoted work units within your declared
scope. It does not claim an entire book was processed unless you actually
specify and cover that book's range. An interrupted atomic promotion can be
retried. If an interruption left `.syllabusgraph/write.lock`, check that its
recorded process is no longer writing before removing the stale lock.

The local run directory contains source text, reviewer notes, model diagnostics,
and timestamps. Keep it private. To share a course, inspect the reviewed
knowledge, source bibliography, and course-plan files separately.
