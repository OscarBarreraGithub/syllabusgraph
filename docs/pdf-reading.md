# Reading PDFs faithfully and efficiently

SyllabusGraph currently registers PDF text with the installed `pypdf` reader.
That gives the workflow page-addressable local text, but it does not turn PDF
extraction into a source of truth. A PDF can store text in an order unlike its
page, omit an equation from the text layer, or contain a scan with no useful
text layer at all. The durable contract is to keep source evidence faithful,
work from an immutable packet, flag ambiguity, keep textbook material private,
and use the course's selected model and reviewer policy. Reader, renderer,
vision, and OCR choices are operational choices that should be made for the
particular source and current environment; the examples here may change.

## Included PDF support

The normal project installation already includes `pypdf`; no separate PDF
engine is required to register an ordinary, text-based book. Confirm the
project environment, then register one source. These commands assume you have
followed the [installation and project setup](../README.md#create-your-own-course)
and placed the file in its private material folder. Skip `source add` if the
bibliography entry already exists:

```bash
source .venv/bin/activate
syllabusgraph --version
syllabusgraph source -p local-courses/my-course add reference-one \
  --title "Reference title" --author "Author name"
syllabusgraph source -p local-courses/my-course register reference-one \
  local-courses/my-course/materials/reference.pdf --page-offset 12
syllabusgraph source -p local-courses/my-course status
syllabusgraph source -p local-courses/my-course coverage reference-one --first 1 --last 3
```

On Windows, activate the environment with `.venv\Scripts\activate`. The
`--page-offset 12` example means printed page 1 is physical PDF page 13. Before
preparing work, sample several distinctive printed page labels, including the
first and last pages you expect to cite, and compare them with the registered
mapping. Sampling plus targeted visual checks of unclear formulas, tables,
diagrams, or notation often avoids rendering an entire readable book just to
check a few claims. Expand visual inspection when the source warrants it.

One registration uses one page offset and positive integer citation pages.
If a source has separate numbering systems, such as roman-numbered notation
before an arabic-numbered main text, preserve that distinction. One option is
a private companion PDF or numbered export with its own source ID and mapping.
Explain the citation labels in its public bibliography description and retain
the original page correspondence privately. Do not apply the main-text offset
to frontmatter whose numbering follows a different rule.

Registration copies the source and its page text into the ignored
`.syllabusgraph/sources/` workspace. Treat both as private: do not commit them,
paste them into public graph data, or send them to a service that the course's
privacy policy does not permit. Prepare small packets after the page mapping
checks out; primary and explicit context pages share an 80-page default budget.
The orchestrator can choose `prepare --page-budget N` for the required evidence
and current model context before freezing a packet.
Workers and reviewers may use only the packet pages, and reviewers should check
the original rendered page when the text is ambiguous.

Before reporting a registered original as missing, check its path in the
project's `.syllabusgraph/sources/index.json`; stored paths are relative to that
project. Ordinary repository searches can hide ignored source files. Inspect
the registered path directly, or include ignored files in a search limited to
that private source directory. This does not expand the packet's reading scope.

Rendered source pages and screenshots are private source material too. Save
inspection images under the project's ignored `.syllabusgraph/`, including
temporary renders, rather than an unignored top-level temporary directory.

When a readable equation is missing from the registered text, retain a private
inspection note with the original page coordinates, relevant render, and checked
transcription. The critic should verify that transcription against the original
page. Keep the proposal's text witnesses faithful to the registered text; a
visually recovered formula must not be presented as a matching text-layer quote.
Text matching locates evidence, while scientific review checks the actual
equation. If visual inspection cannot resolve the notation, keep it unresolved
or prepare a documented replacement source through the process below.

## Diagnose before adding a tool

Use the first failed or uncertain pages to choose the next tool. Registration
reports empty pages; an empty or visibly garbled sample is evidence to inspect,
not a reason to process a whole book again. `pypdf` explains that it reads PDF
content streams rather than interpreting page semantics, and that it cannot OCR
images; tables, positioned text, and mathematical notation can therefore need
visual comparison. See the [pypdf text-extraction guide](https://pypdf.readthedocs.io/en/stable/user/extract-text.html).

An empty text layer may also belong to a blank page or publisher-only matter.
Inspect the original before deciding to use OCR or exclude it. Record verified
nonconceptual exclusions in the coverage ledger; keep mixed problem/reference
pages in scope. If later inspection changes a reviewed inventory, preserve the
earlier decision and document the new evidence and correction explicitly.

For a scan or a few unreadable pages, choose a suitable local OCR or native
PDF-rendering/vision route that suits the file, platform, language, and privacy
requirements. OCR is optional and should target the affected pages or a
separate source export. Do not OCR an already-good whole book by default:
OCR can introduce new errors, while the existing text layer can retain useful
font and encoding information. If OCRmyPDF is suitable, use its current
[platform-specific installation documentation](https://ocrmypdf.readthedocs.io/en/latest/installation.html)
as an alternative, rather than assuming that one operating-system command or
one OCR stack fits every user.

Some source fonts can emit pypdf's `fontTools` runtime warning; its current
message concerns fully parsing the encoding of a CFF Type 1 font. Check the
installed package before reacting:

```bash
python -m pip show pypdf fonttools
```

For example, pypdf 6.18.1 declares `fonttools` in its optional `fonts` extra;
the base project installation does not require it. Verify your installed
version rather than assuming this remains the right remedy. If a warning prevents faithful reading of a
specific source, consult the installed package metadata and the current
[pypdf installation guide](https://pypdf.readthedocs.io/en/stable/user/installation.html)
before choosing an isolated remedy. Do not add optional reader, rendering, or
OCR dependencies to the core project merely to handle one source. When the
installed version's metadata confirms `fonttools` addresses the warning, a
project-local installation is one option:

```bash
python -m pip install fonttools
```

Record the installed version in the private run notes. A PDF viewer, native
vision, or optional renderer such as Poppler may also supply the visual checks;
none is a universal requirement. Choose a renderer supported on the current
platform and consult its current installation instructions before installing.

## Keep the evidence chain reproducible

Never edit `.pages.json` or another registered text cache in place. It is
content-checked evidence for packets that may already have been reviewed. If a
different reader produces a better result, make a stable, numbered UTF-8 text
or Markdown export with clear page boundaries (form-feed separators), and
record privately which reader, settings, source file, and page mapping produced
it. Then either register that documented export as a new source, or explicitly
replace the existing registration:

```bash
syllabusgraph source -p local-courses/my-course register reference-one \
  local-courses/my-course/materials/reference-export.txt --page-offset 12 --replace
```

Here `12` is valid only if the export preserves twelve preceding physical
pages. An export starting at printed page 1 normally uses offset `0`; verify
the actual boundaries rather than copying the example offset.

A replacement may change the registered file checksum, mapping, or reader
output. Packets whose selected page text changes are rejected even when the
original PDF checksum stays the same. A change confined to an uncited,
out-of-packet page does not invalidate an otherwise identical packet. When
packet evidence changes, its reviews no longer apply: prepare new unit IDs,
run extraction and the selected independent review policy again, and retain the
older local records as historical evidence. Changing a tool never authorizes
expanding packet scope, altering evidence silently, or bypassing ambiguity and
review checks.
