# Graph explorer and website

The read-only explorer works without a course plan. It uses the actual graph
records, with no model calls, external fonts, analytics, or JavaScript packages.
A local editable course designer remains a separate interface.

Ask your agent to follow [SETUP.md](../SETUP.md) to open it. The commands below
are for agents and maintainers.

```bash
syllabusgraph site serve --port 8767 --open
syllabusgraph explore -p local-courses/my-course --port 8768 --open
```

`site serve` builds the explicit [catalog](../site/catalog.json) and serves it
on loopback. `explore` does the same for one project. Restart/rebuild after graph
edits. The public catalog contains the QFT collection; new projects remain
subject-neutral. To show other graphs, supply your own `--catalog PATH` with
`graphs` entries containing `id`, `path`, `title`, and optional `kind`.
Paths are relative to the catalog file.

## Reading the map

- Search labels, summaries, or IDs; filter by book treatment or concept type.
- Select a concept to show its immediate neighbors. Arrows preserve the recorded
  relationship direction. Prerequisites entering the selection are ochre;
  dependent concepts are blue; other relationships are gray and dashed.
- The detail panel retains summaries, notation, book origins, section/page
  evidence, relationship rationale, necessity, and mastery levels. Follow a
  book treatment to its original node. Copy a link to the selected concept.
- Book overlap counts shared nodes with independent treatments in both books.
  Imported textbook inputs are excluded, matching the graph-bank checker.
  The relevant book graphs must be included in the catalog to resolve overlap;
  a single exported subject graph retains origin links but cannot compute it.
- The overview shows every filtered concept and relationship. Its positions and
  colors are visual grouping aids, not a scientific embedding or teaching order.
  Dense neighborhoods show up to 60 nodes per relation category; the full
  connection list and JSON download retain every relationship.
- Drag to pan, use zoom buttons, or Ctrl/Command-scroll. Keyboard users can
  select concepts and relationships through ordinary buttons in the list.

The graph JSON includes the complete knowledge graph and selected bibliography
fields, review status, digest, and derived comparison metadata. It does not
include sources, PDFs, private workflows, quotations, credentials, or local file
paths. This export is **not a redaction service**: never put private material in
public graph fields. Review new catalog entries before publication.

## Cloudflare handoff

The site is an assets-only Cloudflare Worker. It has no runtime model calls,
account system, database, upload endpoint, or public access to your local server.
See the current [Cloudflare static assets documentation](https://developers.cloudflare.com/workers/static-assets/).

From the repository, after Python setup:

```bash
syllabusgraph site build
npm ci
npm run deploy:check
npm run preview
```

`wrangler.jsonc` points only at `.syllabusgraph/site/`. `preview` uses Wrangler
locally at port 8787; `deploy:check` validates the actual build without deploying.
Node and Wrangler are needed only for this hosting path, not the local app.

When the owner chooses a hostname and authorizes publication, the deploying
agent checks `npx wrangler whoami`, chooses the correct account, and configures
an explicit custom-domain route or an agreed path integration. Do not replace an
existing Science with Agents worker. For a standalone custom domain, add a
route of the form `{"pattern":"<chosen-hostname>","custom_domain":true}` and
verify ownership/account in Cloudflare. Do not commit personal account IDs or
automatically create a guessed domain. All asset URLs are relative, so the
export can also be mounted under a prefix by the parent site.

```bash
npm run deploy
```

That command rebuilds the catalog before publishing. Deploy only the generated
site directory. A rebuild rejects unexpected files in the output directory.
Never upload the repository root or use the writable course server as a public
service. A collaborator can host the same static output elsewhere.
