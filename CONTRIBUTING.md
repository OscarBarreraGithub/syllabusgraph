# Contributing

Start with a small, reproducible issue or a focused pull request. Describe the
behavior you expect and the source evidence for any proposed course claim.

Textbook graph contributions are welcome in the [graph bank](graphs/README.md).
Contribute a bounded, reviewed section with bibliography, printed-page citations,
coverage and omissions, and original summaries. Keep a book's graph independent
of a particular audience or course. Shared graphs preserve links to the book
nodes and explain correspondences; matching labels alone do not justify a merge.
Contributors retain their source files and quotation checks locally. A public
graph must validate from a fresh clone without those files or a model account.

Engine changes should work with an empty project and the independent sampling
example. Keep subject knowledge and editorial choices in project data. Add
invariant tests when changing closure, mastery, ordering, timing, or review
semantics. Run `python -m pytest` and `ruff check .`.

Source material, extracted quotations, model logs, credentials, and private
course decisions must remain outside commits. The included examples should
remain usable without model accounts or external documents. Do not label a
proposed graph or timing estimate as verified teaching evidence.

Keep the [capability register](docs/capabilities.md) current when functionality
changes: record its status, interface, verification, and limitations. Add
user-visible changes to [the changelog](CHANGELOG.md). Proposed work belongs in
the [roadmap](docs/roadmap.md). Update guides in this repository so a future docs
site or wiki can use the same maintained source.
