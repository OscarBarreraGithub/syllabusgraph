"""Prepare a compact record index and verify a reviewed concept inventory.

This is an organizational pass over existing graphs, not a textbook reread or
an equivalence/dependency inference. Compact evidence sections identify index
records as JSON: {"records": [1, 2]}. Public exports resolve them to graph IDs.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
import re

from syllabusgraph.io import ProjectError, digest, write_json
from syllabusgraph.project import load_project


def record_index(projects, page_size=40):
    if type(page_size) is not int or page_size < 1:
        raise ProjectError("Index page size must be a positive integer.")
    ids = [p.config["id"] for p in projects]
    if not projects or len(set(ids)) != len(ids):
        raise ProjectError("Choose distinct, nonempty input projects.")
    books, records, rows = [], [], []
    for code, project in enumerate(projects):
        books.append({"code": code, "id": project.config["id"],
                      "title": project.config["title"],
                      "knowledge_digest": digest(project.knowledge)})
        for node in project.knowledge["nodes"]:
            number = len(records) + 1
            excerpt = re.split(r"(?<=[.!?])\s+(?=[A-Z])", node["summary"])[0]
            records.append({"index": number, "project": project.config["id"],
                            "node": node["id"], "label": node["label"],
                            "page": (number - 1) // page_size + 1})
            rows.append([number, code, node["label"], excerpt])
    if not records:
        raise ProjectError("Input projects contain no records.")
    manifest = {"schema_version": 1, "page_size": page_size,
                "projects": books, "records": records}
    manifest["index_digest"] = digest(manifest)
    pages = []
    for start in range(0, len(rows), page_size):
        page = {"index_digest": manifest["index_digest"],
                "page": start // page_size + 1,
                "columns": ["record", "book_code", "label", "summary_excerpt"],
                "books": {b["code"]: b["id"] for b in books},
                "scope": "Organizational index only. Summary excerpts omit later qualifications. "
                         "Preserve full original records; no equivalence or dependency claims.",
                "records": rows[start:start + page_size]}
        pages.append(json.dumps(page, ensure_ascii=False, separators=(",", ":")))
    return manifest, "\f".join(pages)


def inventory(proposal, manifest, source_id="record-index"):
    """Require an exact primary partition; reject silent omissions or duplicates."""
    if digest({k: v for k, v in manifest.items() if k != "index_digest"}) != manifest["index_digest"]:
        raise ProjectError("The input index manifest changed.")
    graph = proposal["graph"]
    if graph["edges"] or graph["motivations"]:
        raise ProjectError("An inventory cannot assert relationships or motivations.")
    records = {r["index"]: r for r in manifest["records"]}
    groups = {g["id"] for g in graph["groups"]}
    seen, identities, concepts = Counter(), set(), []
    for node in graph["nodes"]:
        if node.get("kind") != "concept":
            raise ProjectError("Inventory entries must be concepts.")
        if node["id"] in identities or node.get("group") not in groups:
            raise ProjectError("Each concept needs a unique ID and an existing subject group.")
        identities.add(node["id"])
        if len(node["evidence"]) != 1 or node["evidence"][0]["source"] != source_id:
            raise ProjectError("Use one record-index evidence entry per concept.")
        evidence = node["evidence"][0]
        try:
            membership = json.loads(evidence["section"])
            numbers = membership["records"]
        except (ValueError, KeyError, TypeError) as exc:
            raise ProjectError("Evidence section must be JSON with a records array.") from exc
        if (not isinstance(numbers, list) or not numbers
                or any(type(n) is not int or n not in records for n in numbers)):
            raise ProjectError("A concept must cite existing integer record indices.")
        if set(evidence["pages"]) != {records[n]["page"] for n in numbers}:
            raise ProjectError("Evidence pages must match every assigned index record.")
        seen.update(numbers)
        treatments = [{"project": records[n]["project"], "node": records[n]["node"]}
                      for n in sorted(numbers)]
        concepts.append({"id": node["id"], "label": node["label"],
                         "summary": node["summary"], "group": node["group"],
                         "treatments": treatments,
                         "book_counts": dict(sorted(Counter(t["project"] for t in treatments).items()))})
    missing = set(records) - set(seen)
    repeated = {n for n, count in seen.items() if count != 1}
    if missing or repeated:
        raise ProjectError(f"Inventory must partition all records: {len(missing)} unassigned, "
                           f"{len(repeated)} repeated.")
    return {"schema_version": 1, "kind": "concept-inventory",
            "relation": "primary-topic-association",
            "scope": "Subject-wide organization of existing records using labels and summary excerpts. "
                     "Coverage counts associated treatments, not equivalent derivations or certified absence. "
                     "Each record has one primary home; secondary cross-links and dependencies remain deferred.",
            "index_digest": manifest["index_digest"], "proposal_digest": digest(proposal),
            "projects": manifest["projects"], "groups": graph["groups"], "concepts": concepts}


def resolve_coverage(result, projects, coverage_sources):
    """Resolve citations against pinned inputs; imported prerequisites do not count.

    The caller explicitly names each project's native source IDs. No subject or
    source-naming convention is built into this rule.
    """
    by_id = {p.config["id"]: p for p in projects}
    expected = {p["id"]: p["knowledge_digest"] for p in result["projects"]}
    if set(expected) != set(by_id) or set(expected) != set(coverage_sources):
        raise ProjectError("Provide the pinned projects and native source IDs for each one.")
    for identity, project in by_id.items():
        if digest(project.knowledge) != expected[identity]:
            raise ProjectError("A pinned input graph changed; do not reuse its old inventory.")
        if not coverage_sources[identity] or not set(coverage_sources[identity]) <= set(project.sources):
            raise ProjectError("Native coverage sources must exist in their input project.")
    for concept in result["concepts"]:
        independent = Counter()
        for treatment in concept["treatments"]:
            identity = treatment["project"]
            node = by_id[identity].nodes[treatment["node"]]
            sources = sorted({e["source"] for e in node["evidence"]})
            treatment["evidence_sources"] = sources
            treatment["independent_coverage"] = bool(set(sources) & set(coverage_sources[identity]))
            if treatment["independent_coverage"]:
                independent[identity] += 1
        concept["independent_book_counts"] = dict(sorted(independent.items()))
    result["coverage_sources"] = {k: sorted(v) for k, v in coverage_sources.items()}
    return result


def verify_inventory(result, manifest, projects):
    """Recheck a public inventory from a clone, without local proposals or models."""
    regenerated, _ = record_index(projects, page_size=manifest["page_size"])
    if regenerated != manifest or result["index_digest"] != manifest["index_digest"]:
        raise ProjectError("The published input manifest no longer matches its graphs.")
    lookup = {(r["project"], r["node"]): r for r in manifest["records"]}
    nodes = []
    try:
        for concept in result["concepts"]:
            rows = [lookup[(t["project"], t["node"])] for t in concept["treatments"]]
            nodes.append({"id": concept["id"], "label": concept["label"],
                          "summary": concept["summary"], "group": concept["group"],
                          "kind": "concept", "evidence": [{"source": "record-index",
                          "section": json.dumps({"records": [r["index"] for r in rows]}),
                          "pages": sorted({r["page"] for r in rows})}]})
    except KeyError as exc:
        raise ProjectError("The inventory names a missing treatment or field.") from exc
    reconstructed = inventory({"graph": {"nodes": nodes, "groups": result["groups"],
                                         "edges": [], "motivations": []}}, manifest)
    checked = resolve_coverage(reconstructed, projects, result["coverage_sources"])
    if checked["concepts"] != result["concepts"] or checked["projects"] != result["projects"]:
        raise ProjectError("Published memberships or coverage counts disagree with their inputs.")
    return {"concepts": len(nodes), "records": len(lookup), "coverage": "mechanically verified"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    make = sub.add_parser("index")
    make.add_argument("output", type=Path)
    make.add_argument("projects", type=Path, nargs="+")
    check = sub.add_parser("check")
    check.add_argument("manifest", type=Path)
    check.add_argument("proposal", type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("manifest", type=Path)
    verify.add_argument("inventory", type=Path)
    verify.add_argument("projects", type=Path, nargs="+")
    args = parser.parse_args()
    if args.command == "index":
        manifest, text = record_index([load_project(p) for p in args.projects])
        args.output.mkdir(parents=True, exist_ok=True)
        write_json(args.output / "index.json", manifest)
        (args.output / "records.txt").write_text(text, encoding="utf-8")
        print(f"Indexed {len(manifest['records'])} records on {len(text.split(chr(12)))} pages.")
    elif args.command == "check":
        result = inventory(json.loads(args.proposal.read_text()), json.loads(args.manifest.read_text()))
        print(f"Complete partition: {len(result['concepts'])} concepts.")
    else:
        result = verify_inventory(json.loads(args.inventory.read_text()),
                                  json.loads(args.manifest.read_text()),
                                  [load_project(p) for p in args.projects])
        print(json.dumps(result))


if __name__ == "__main__":
    main()
