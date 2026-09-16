# Releasing a project

Build and publish from a clean checkout. Runtime inputs do not belong in source
or distribution artifacts: exclude local registrations, source files, extracted
text, private run logs, credentials, and local course drafts.

The wheel includes an explicit list of example/template files, generic UI
assets, schemas, and workflow instructions. It does not recursively package
example workspaces. The source distribution must also be inspected.

Before release:

```bash
python -m pytest
ruff check .
python scripts/test_browser.py
python scripts/test_explorer.py
python -m build
python scripts/audit_public.py
```

Inspect the resulting wheel and source archive, then install the wheel in a
new virtual environment outside this checkout. Initialize the sampling
example and blank project there. Validate/build the example and
verify the included UI and exports. Test the documented locked installation
path from a fresh checkout as well.

The publication audit checks Git content and distribution artifacts for local
storage, source binaries, common credentials, private absolute paths, and
non-public contact identifiers. Project-specific exclusion patterns can be
supplied with repeated `--deny-pattern` options without embedding private
strings in the published policy. Inspect matches in context and review the
exact commit tree manually; automated matching is a screening aid.

When starting a public project from private work, initialize a separate Git
repository from individually reviewed content. Its first commit must already
be suitable for publication. Do not copy old Git directories, branches, tags,
operational notes, or private fixtures. File deletion in a later commit does
not erase earlier history. Audit all intended refs and commit messages, not
only the working tree.

## Development setup

Follow [SETUP.md](../SETUP.md), then install development dependencies with
`.venv/bin/python -m pip install -e '.[dev,browser]'` (Windows: use the venv's
`Scripts/python.exe`). For a locked environment use `uv sync --locked --all-extras`.
Install the test browser with `python -m playwright install chromium` inside
that environment. The browser tests use disposable projects and no model calls.
For the optional Cloudflare build, run `npm ci` and `npm run deploy:check`.
