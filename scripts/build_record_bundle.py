"""Make a deterministic, page-addressable source from selected reviewed records.

This reuses public graph records, not original textbook pages. Selection is an
explicit manifest; scientific grouping remains the producer/critic's task.
"""

import argparse
import json
from pathlib import Path

from syllabusgraph.io import ProjectError
from syllabusgraph.project import load_project


def record_bundle(project, manifest):
    if manifest["graph_digest"] != project.content_digest:
        raise ProjectError("The input graph changed; review the selection before regenerating.")
    ids = manifest["records"]
    if len(ids) != len(set(ids)) or not ids or not set(ids) <= set(project.nodes):
        raise ProjectError("Select distinct, existing records.")
    chosen = set(ids)
    edges = [e for e in project.knowledge["edges"] if {e["from"], e["to"]} <= chosen]
    pages = []
    for number, identity in enumerate(ids, 1):
        content = {
            "bundle_page": number,
            "project": project.config["id"],
            "graph_digest": project.content_digest,
            "record": project.nodes[identity],
            "outgoing_within_selection": [e for e in edges if e["from"] == identity],
        }
        pages.append(json.dumps(content, ensure_ascii=False, indent=2))
    return "\f".join(pages)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    text = record_bundle(load_project(args.project), manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Wrote {len(manifest['records'])} derived-record pages to {args.output}")


if __name__ == "__main__":
    main()
