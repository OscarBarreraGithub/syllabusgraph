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

The homepage explains **SyllabusGraph**, its workflow, and how to reuse it with
your own references. Copy the setup prompt directly from the page. The prompt
selects slow, checkpointed mode and points the coding agent to the full setup
guide. Usage limits are explained before the example.

![The reusable tool and copyable setup prompt](home.png)

Choose **Explore the demo** to open the collection's **Overview**. It explains
the book graphs, shared graph, and exact record matches. The example is separate
from the product homepage. **Overview** returns to the collection introduction;
the brand link returns to the product homepage.

![The collection overview and starting point](overview.png)

The **Exact overlap** workspace shows records explicitly matched across the
compared works, with their connections and basic statistics. It is not an
established conceptual backbone or a count of every shared topic. See the
[abstraction audit](graph-abstraction.md) for the distinction and missing work.
It does not choose a course, reading sequence, audience, or timetable.

![The shared core and overlap statistics](explorer.png)

The QFT catalog compares Peskin–Schroeder, Schwartz, and Weinberg I + II by
default. **Compare → Individual volumes** treats the four book graphs separately.
**Include** widens the intersection to concepts matched in at least two books.
The graph displays every qualifying concept and every shared-graph relation
whose endpoints qualify. Hover to highlight connections; click a concept for
its wider neighborhood and source evidence. Scroll in either direction, drag
the map (including from a card), or use the arrow buttons to move. A focused
map also accepts arrow keys. **Expand graph** gives it the window; the exit
button or Escape returns to the normal workspace. Zoom with +/− or Ctrl/Command
and the wheel; **Reset** returns to the start at 100%. Jump to separate
components from the sidebar or the selector above the map. On touch screens,
swipe to move. The overview scrolls as a normal page; the map scrolls within its
own viewport. Short windows can also scroll the page to reach the controls.

The counts distinguish exact book membership, prerequisite relations, connected
components, isolated concepts, and the fraction of the whole shared graph.
Components use all relation types, ignoring direction only when measuring
connectivity. Layout ranks use prerequisite arrows. Nodes shared by all books
do **not** imply that every connecting relationship is asserted in every book.
Imported prerequisites are excluded from independent treatments. These are
recorded correspondences, not proof of exhaustive overlap. Paths through
nonqualifying concepts are not silently replaced by new edges.

Grouping is explicit catalog data: use `comparison_group: {"id": "work-id",
"title": "Work title"}` on book entries that should count as one work. No author
names or project-name prefixes are inferred by the engine. A core comparison
requires the book graphs named by the shared graph's origins to be in the
catalog; missing exports cannot silently lower the comparison denominator.

**Book index** is a secondary way to find concepts using source chapter/page
order. It is not a course. Change **Read through** to browse another book without
leaving the shared graph. **All concepts** and the search box cover the whole
selected graph, including concepts outside the current book or common core.
Standalone textbook and example graphs have their own overview and a direct
button to their concept index. Empty projects offer the setup guide.

Open a card to follow its **Connections**. Prerequisites are on the left,
dependents on the right, and other connections in a separate column. Arrows
preserve the recorded direction; dashed arrows denote other relation types.
Full concept names remain visible. Click a neighbor to make it the selection,
or use **Reveal** to add its neighbors to the current diagram. **Back** retraces
concepts you have opened. Hover or keyboard focus highlights connected cards.

![A selected concept with readable prerequisites and dependents](explorer-connections.png)

**Trace prerequisites** follows only recorded prerequisite edges, recursively.
**One step** restores the immediate neighborhood. Large columns initially show
eight concepts with explicit totals and **Show more** buttons; every remaining
concept can be revealed. Drag empty space, use the scrollbars, or swipe to pan.
Zoom buttons adjust card size; **Center** returns to the selection at 100%.
This is a reading interface, not a proposed course sequence or a whole-graph
force layout.

**Evidence** opens the summary, notation, qualifications, source sections and
pages, and the complete list of connections. Expand a relationship to read its
rationale, necessity, mastery levels, and evidence. Follow a book treatment to
its original node, or copy a link to the selected concept. **Book overlap**
opens pairwise comparisons based on independent treatments; imported textbook
inputs are excluded, matching the graph-bank checker. Include the relevant book
graphs in the catalog to resolve those comparisons.

### Where chapter columns come from

The exporter reads chapter page ranges from a project's public `coverage.yaml`,
when present. For a shared graph, it follows exact book origins before assigning
chapter membership. Companion pagination and imported evidence are not treated
as pages in the primary book. A concept with citations in several chapters can
appear in several columns; the reading-view total counts it once. Shared concept
counts can differ from the original book's node count.

Chapter topic captions summarize existing graph groups; they are **not official
chapter titles**. Unmapped records remain in an **Other concepts** column. Without
a chapter inventory, the interface uses existing groups and an ungrouped column.
Blank projects need no chapter configuration. In a multi-book catalog, mark the
combined graph `kind: shared` and the individual books `kind: textbook` to create
book reading views. A standalone export still works without the other books.

The graph JSON retains the complete, unchanged knowledge graph. It adds selected
bibliography fields, review status, digest, and derived reading/comparison
metadata. It does not include source files, PDFs, private workflows, credentials,
or local paths. This export is **not a redaction service**: never put private
material in public graph fields. Review new catalog entries before publication.

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
