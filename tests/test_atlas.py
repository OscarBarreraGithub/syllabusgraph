from copy import deepcopy
from dataclasses import replace
import json

import pytest

from syllabusgraph.atlas import concept_atlas
from syllabusgraph.inventory import inventory, record_index, resolve_coverage
from syllabusgraph.io import ProjectError
from syllabusgraph.io import digest, write_json, write_yaml
from syllabusgraph.site import build_site


def make_inventory(projects):
    manifest, _ = record_index(projects)
    # The self-authored fixture's first record is one idea; the rest form another.
    first = next(iter(projects[0].nodes))
    nodes = []
    for identity, match in [("one", True), ("two", False)]:
        selected = [r for r in manifest["records"] if (r["node"] == first) == match]
        nodes.append({"id": identity, "label": identity, "summary": "Fixture scope.",
                      "kind": "concept", "group": "sampling", "evidence": [{
                      "source": "record-index", "section": json.dumps({"records": [r["index"] for r in selected]}),
                      "pages": sorted({r["page"] for r in selected})}]})
    proposal = {"graph": {"nodes": nodes, "groups": [{"id": "sampling", "title": "Sampling"}],
                          "edges": [], "motivations": []}}
    result = inventory(proposal, manifest)
    return resolve_coverage(result, projects, {p.config["id"]: list(p.sources) for p in projects})


def test_atlas_preserves_exact_links_and_explicit_work_grouping(sample):
    other = replace(sample, config={**sample.config, "id": "other"}, knowledge=deepcopy(sample.knowledge))
    projects = [sample, other]
    result = make_inventory(projects)
    books = [{"project_id": p.config["id"], "knowledge": p.knowledge} for p in projects]
    entries = [{"project_id": p.config["id"], "title": p.config["title"]} for p in projects]
    atlas = concept_atlas(result, books, entries)
    assert atlas["counts"]["all_works"] == 2
    assert atlas["counts"]["records"] == 2 * len(sample.nodes)
    assert (atlas["counts"]["within_concept_relationships"]
            + atlas["counts"]["between_concept_relationships"]) == 2 * len(sample.knowledge["edges"])
    for link in atlas["links"]:
        assert link["from"] != link["to"]
        for witness in link["records"]:
            original = next(e for b in books if b["project_id"] == witness["project"]
                            for e in b["knowledge"]["edges"] if e["id"] == witness["edge"])
            assert all(witness[k] == original[k] for k in ("from", "to", "relation", "necessity"))
    for entry in entries:
        entry["comparison_group"] = {"id": "one-work", "title": "Two volumes"}
    grouped = concept_atlas(result, books, entries)
    assert len(grouped["works"]) == 1
    assert grouped["counts"]["two_or_more"] == 0
    broken = deepcopy(result)
    broken["concepts"][1]["treatments"].append(broken["concepts"][0]["treatments"][0])
    with pytest.raises(ProjectError, match="two primary"):
        concept_atlas(broken, books, entries)


def test_site_requires_accepted_inventory_and_exact_inputs(sample, blank, tmp_path):
    directory = tmp_path / "inventory"
    result = make_inventory([sample])
    manifest, _ = record_index([sample])
    write_json(directory / "inventory.json", result)
    write_json(directory / "inputs.json", manifest)
    entries = [{"path": sample.root, "kind": "textbook"},
               {"path": blank.root, "kind": "shared", "inventory": directory}]
    for status, fingerprint in [("reject", digest(result)), ("model-reviewed", "stale")]:
        write_yaml(directory / "review.yaml", {"status": status, "inventory_digest": fingerprint})
        with pytest.raises(ProjectError, match="accepted inventory"):
            build_site(entries, tmp_path / "site")
        assert not (tmp_path / "site").exists()
    write_yaml(directory / "review.yaml", {"status": "model-reviewed", "inventory_digest": digest(result),
                                           "human_audit": "pending"})
    site_manifest = build_site(entries, tmp_path / "site")
    target = site_manifest["graphs"][1]
    assert target["atlas"]["concepts"] == 2
    public = json.loads((tmp_path / "site" / target["file"]).read_text())
    assert public["atlas"]["review"]["human_audit"] == "pending"
    sample.knowledge["nodes"][0]["summary"] = "A changed input snapshot."
    write_yaml(sample.root / sample.config["knowledge"], sample.knowledge)
    with pytest.raises(ProjectError, match="no longer matches"):
        build_site(entries, tmp_path / "changed")
