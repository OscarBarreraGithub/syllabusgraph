# Set up SyllabusGraph for a person

This is the coding agent's entry point. Handle the commands yourself. Give the
person a working local website, an exact materials-folder path, and a short
explanation of what happens next. A setup request authorizes installation and
local demonstration, **not an unbounded extraction run or public upload**.

Read `AGENTS.md` after cloning (Claude also reads `CLAUDE.md`). If this document
was opened on GitHub, clone the repository before following relative links.
Repository instructions must be read explicitly when cloning inside an existing
session; do not assume your host reloads them automatically.

## 1. Find or install the local tool

Inspect the current directory and available tools. Reuse an existing checkout;
do not overwrite changes, delete a project, or create a second copy by accident.
Otherwise clone `https://github.com/OscarBarreraGithub/syllabusgraph.git` into a
suitable new directory and work there.

You need Git and Python **3.11 or later** with `venv` and `pip`. Inspect versions
first. Node, Homebrew, Docker, Cloudflare, and a model API key are **not required**
for local use. Prefer an existing suitable Python. If missing, choose an
appropriate current installer using official documentation for the actual OS:

- macOS: an existing package manager can install Python, or use python.org.
- Windows: inspect `py -3 --version`; use the official Python installer or an
  already available package manager. Avoid relying on PowerShell activation.
- Linux: use the distribution's supported Python/venv packages or a suitable
  user-local interpreter. Do not replace system Python.

Install missing prerequisites yourself when permitted. An OS administrator
prompt, account sign-in, or host trust dialog may require the person; explain
that specific action without handing them a generic command checklist. Do not
install a new package manager merely because an example uses it.

From the checkout, on macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python -m pip install --no-deps -e .
.venv/bin/python -m syllabusgraph --version
```

On Windows, use `py -3 -m venv .venv`, then the same commands with
`.venv\Scripts\python.exe` instead of `.venv/bin/python`. All commands below use
`syllabusgraph` for brevity; invoke it as `.venv/bin/python -m syllabusgraph`
(or the Windows equivalent). No shell activation is required. If `.venv`
already exists, verify it before installing; do not overwrite a working setup.

## 2. Show something that works, without model calls

```bash
syllabusgraph site serve --port 8767 --open
```

Run it in a persistent local terminal/process, check the HTTP response, and
provide **http://127.0.0.1:8767**. It builds the public graph catalog and serves
only generated assets. If the port is occupied, check whether this is the
existing app; otherwise choose a free port and report the actual URL. Do not
expose a local project server publicly. The site is read-only and needs no PDFs.
For the editable, self-authored course example, use `syllabusgraph demo` (8766).

## 3. Create or resume their workspace

Look for an existing user project and inspect its `project.yaml`, generated
`AGENTS.md`, `COURSE_GUIDANCE.md`, `syllabusgraph status`, `agent policy`, and
`work status`. Preserve accepted settings and completed work. If no project
exists, choose a neutral descriptive name:

```bash
syllabusgraph init local-courses/my-course --title "My course"
```

Give the person the **absolute path to `local-courses/my-course/materials/`**.
Say they can drop PDF, TXT, or Markdown references there, or provide a path and
you will copy files in. Preserve originals; don't overwrite an existing copy.
Books, working extracts, guidance, and checkpoints are private by default.
Nothing starts merely because a file appears in the folder.

For graph-only work, ask only about sources, scope, and useful concept
resolution. Do not demand an audience, semester length, or course goals yet.
Keep separate textbook graphs when comparing books, plus a shared subject graph.
The included QFT bank is a public example, not a template for their subject.

## 4. Explain the usage choice before extraction

Tell the person plainly: **whole-book graph construction can exhaust a model
allowance**. Browsing costs no model usage; running this setup agent does.
Recommend a small pilot (for example, a few coherent pages) and slow mode.

Default slow session: **two dispatches, one worker, 20-minute admission window,
750 KB request allowance**. A dispatch is one worker invocation, including
failed attempts. Two calls might complete extraction + review, or leave a
correction for another day. The deadline gates new work; it does not terminate
an in-flight call. The byte limit is a context-size proxy, not a token estimate.
Orchestrator calls and manual/external runners are outside these limits.

A person can choose larger explicit session bounds and custom models. Never
silently raise a limit, buy credits, switch to paid API billing, or renew a
session to keep going. There is no automatic provider-quota detector or weekly
scheduler. Slow mode is deliberately user-resumed, so it can span weeks.
Show the [usage guide](docs/usage-estimates.md) and preserve choices already
made in this conversation.

Show defaults and ask once whether they suit the work:

| Host | Extractor | Required critic / final adjudicator |
|---|---|---|
| Codex | `gpt-5.6-terra`, high | `gpt-5.6-sol`, high |
| Claude | Sonnet, high | Opus, high |

The orchestrator inherits the host session. All roles are configurable.
`--audit-mode end` leaves final human review pending; `trust` makes it optional.
Critic review remains mandatory in both. Verify native model/effort availability
before work; never substitute silently. Account access or unsupported model
selection may need one human decision. See [native setup](docs/agent-setup.md).

After settings are accepted, configure the actual provider on the project:

```bash
syllabusgraph agent -p local-courses/my-course configure --provider codex --accept-defaults
```

Use `--provider claude` in Claude. Role overrides include `--extractor-model`,
`--extractor-effort`, `--critic-model`, `--critic-effort`, and corresponding
orchestrator flags. Do not reset an existing accepted policy.

## 5. Register sources, sample reading quality, and start the pilot

Read [PDF reading](docs/pdf-reading.md) and [source workflow](docs/source-workflow.md).
Inspect the files, title/edition, and print/PDF page mapping. Use the bundled
reader where suitable; choose other readers, rendering, or OCR case by case
using current primary docs. Never claim mathematical fidelity from extracted
text alone. Cache text and page renders privately, preserving printed page
identity. Image-only sources need an OCR step, not fabricated text.

```bash
syllabusgraph source -p local-courses/my-course add reference-one --title "Actual reference title"
syllabusgraph source -p local-courses/my-course register reference-one local-courses/my-course/materials/reference.pdf --page-offset 12
```

The offset is **an example**: PDF page = printed page + offset. Confirm it for
this edition. File paths are relative to the shell's working directory.
Do not fetch copyrighted textbooks or upload private sources as part of setup.

Only when the person has authorized extraction and scope:

```bash
syllabusgraph work -p local-courses/my-course start
syllabusgraph prepare -p local-courses/my-course --unit pilot-01 --source reference-one --first 1 --last 3 --scope "Agreed pilot scope" --budget 10
```

The page range and concept budget are examples; use coherent source boundaries.
Read [orchestration](workflows/orchestrate.md), then dispatch native workers
using immutable requests and record results with actual runtime identity.
Only the orchestrator launches workers. Extractors do not launch critics.
Use an independent configured critic, at most one correction and recheck, then
final adjudication if needed. No review of the final adjudicator. Check the
result mechanically and promote accepted work; defer unresolved work.

At a budget boundary, save any returned result and mechanically promote already
accepted work if valid. Run `work pause`. Give a short progress update and stop.
Do not consume allowance polling, re-planning, or waiting for a reset. Do not
start the next budget window on your own. Read the
[run lessons](docs/qft-run-retrospective.md) before orchestrating large work.

## 6. Resume, inspect, then design a course

On a later request, read the checkpoint before doing anything expensive:

```bash
syllabusgraph work -p local-courses/my-course status
syllabusgraph status -p local-courses/my-course
syllabusgraph agent -p local-courses/my-course audit
```

If a worker is still pending, inspect its actual host state/result and finish
recording it; don't launch a duplicate. Old runtime IDs may no longer exist in
a new session. Preserve the packet and failure reason, count the failed attempt,
and retry within the same unit/family only when justified. Once pending work
is settled and the person has requested another session:

```bash
syllabusgraph work -p local-courses/my-course start --resume
```

The state survives closing the host or computer. There is no hidden job to keep
alive. Keep source copies and `.syllabusgraph/` for resumption; they are ignored
by Git, so a fresh clone alone does not contain private checkpoints. Arrange a
private backup if the person needs to resume on another computer.

Use `syllabusgraph explore -p local-courses/my-course --open` to inspect a graph
without course plans. Once they want a course, collect desired capabilities,
entry knowledge, depth, teaching time, preferred routes, and assessment needs.
Use the [project format](docs/project-format.md) to create plans and
`syllabusgraph serve -p local-courses/my-course --open` for the course designer.
Validate and build before sharing. The planner produces a teaching scaffold;
lecture writing and real classroom validation remain separate work.

End setup with the running URL, materials-folder path, current model/budget
choices, and exactly what the person needs to supply next. Link the
[field guide](docs/README.md). Do not claim extraction happened during setup.
