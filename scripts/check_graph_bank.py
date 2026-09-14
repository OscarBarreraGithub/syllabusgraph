"""Validate the public bank and list reviewed correspondences; no source files needed."""

from itertools import combinations
import json
from pathlib import Path

from syllabusgraph.io import ProjectError, digest, read_yaml
from syllabusgraph.project import load_project


def inspect_bank(root):
    projects, kinds, reviewed = {}, {}, set()
    for pattern in ("textbooks/*/project.yaml", "subjects/*/project.yaml"):
        for path in sorted(root.glob(pattern)):
            project = load_project(path.parent)
            identity = project.config["id"]
            if identity in projects:
                raise ProjectError(f"Duplicate bank project: {identity}")
            projects[identity] = project
            kinds[identity] = pattern.split("/")[0]
            if project.plans or any("public_file" in s for s in project.sources.values()):
                raise ProjectError(f"Bank projects contain graphs without plans or source files: {identity}")
            review_path = project.root / "review.yaml"
            if not review_path.is_file():
                raise ProjectError(f"Missing public review summary: {identity}")
            review = read_yaml(review_path)
            if review.get("status") in {"partial-model-reviewed", "model-reviewed", "human-reviewed"}:
                if review.get("graph_digest") != digest(project.knowledge):
                    raise ProjectError(f"Stale public review summary: {identity}")
                reviewed.add(identity)
            elif project.nodes:
                raise ProjectError(f"Populated bank graph needs a current review summary: {identity}")
            coverage_path = project.root / "coverage.yaml"
            if coverage_path.is_file():
                coverage = read_yaml(coverage_path)
                if coverage.get("source") != identity:
                    raise ProjectError(f"Coverage ledger names another project: {identity}")
                if coverage.get("graph_digest") != digest(project.knowledge):
                    raise ProjectError(f"Stale public coverage ledger: {identity}")
    overlaps = {}
    for identity, project in projects.items():
        for node in project.nodes.values():
            seen = set()
            for origin in node.get("origins", []):
                if kinds[identity] != "subjects":
                    raise ProjectError(f"Only shared subject graphs have origins in this bank: {identity}")
                key = (origin["project"], origin["node"])
                if key in seen:
                    raise ProjectError(f"Duplicate origin on {identity}/{node['id']}: {key}")
                seen.add(key)
                target = projects.get(origin["project"])
                if target is None or origin["node"] not in target.nodes:
                    raise ProjectError(f"Unknown origin on {identity}/{node['id']}: {key}")
                if kinds[origin["project"]] != "textbooks":
                    raise ProjectError(f"Origin must name a textbook graph: {key}")
                if origin["project"] not in reviewed:
                    raise ProjectError(f"Origin needs a reviewed textbook graph: {key}")
            for pair in combinations(sorted({p for p, _ in seen}), 2):
                overlaps.setdefault((identity, *pair), []).append(node["id"])
    return {
        "projects": {identity: {"nodes": len(p.nodes), "edges": len(p.knowledge["edges"]),
                                "plans": len(p.plans), "digest": p.content_digest}
                     for identity, p in sorted(projects.items())},
        "overlap": [{"shared_graph": shared, "books": [a, b], "count": len(nodes),
                     "shared_nodes": sorted(nodes)}
                    for (shared, a, b), nodes in sorted(overlaps.items())],
        "scope": "Reviewed correspondences in extracted portions only; not full-book overlap.",
    }


if __name__ == "__main__":
    print(json.dumps(inspect_bank(Path(__file__).resolve().parents[1] / "graphs"), indent=2))
