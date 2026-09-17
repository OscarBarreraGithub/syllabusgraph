from copy import deepcopy
import json

import pytest

from scripts.concept_inventory import inventory, record_index, resolve_coverage, verify_inventory
from syllabusgraph.io import ProjectError


def proposal_for(manifest):
    return {"graph": {"groups": [{"id": "sampling", "title": "Sampling"}],
                      "nodes": [{"id": "sampling-concepts", "kind": "concept",
                                 "label": "Sampling concepts", "summary": "Organizing scope.",
                                 "group": "sampling", "evidence": [{"source": "record-index",
                                 "section": json.dumps({"records": [r["index"] for r in manifest["records"]]}),
                                 "pages": sorted({r["page"] for r in manifest["records"]})}]}],
                      "edges": [], "motivations": []}}


def test_index_is_reproducible_and_resolves_every_original(sample):
    original = deepcopy(sample.knowledge)
    manifest, text = record_index([sample], page_size=2)
    assert (manifest, text) == record_index([sample], page_size=2)
    pages = [json.loads(p) for p in text.split("\f")]
    rows = [r for p in pages for r in p["records"]]
    assert len(rows) == len(sample.nodes)
    assert [r[0] for r in rows] == list(range(1, len(rows) + 1))
    result = inventory(proposal_for(manifest), manifest)
    assert {t["node"] for t in result["concepts"][0]["treatments"]} == set(sample.nodes)
    assert sample.knowledge == original
    altered = deepcopy(manifest)
    altered["records"][0]["node"] = "changed"
    with pytest.raises(ProjectError, match="manifest changed"):
        inventory(proposal_for(manifest), altered)
    with pytest.raises(ProjectError, match="distinct"):
        record_index([sample, sample])


@pytest.mark.parametrize("failure", ["missing", "duplicate", "unknown", "page", "edge"])
def test_inventory_cannot_hide_omissions_duplicates_or_invented_edges(sample, failure):
    manifest, _ = record_index([sample], page_size=2)
    proposal = proposal_for(manifest)
    evidence = proposal["graph"]["nodes"][0]["evidence"][0]
    numbers = json.loads(evidence["section"])["records"]
    if failure == "missing":
        numbers.pop()
        evidence["pages"] = sorted({manifest["records"][n - 1]["page"] for n in numbers})
    elif failure == "duplicate":
        numbers.append(numbers[0])
    elif failure == "unknown":
        numbers.append(99999)
    elif failure == "page":
        evidence["pages"].append(999)
    else:
        proposal["graph"]["edges"] = [{"id": "unreviewed"}]
    evidence["section"] = json.dumps({"records": numbers})
    with pytest.raises(ProjectError):
        inventory(proposal, manifest)


def test_coverage_uses_explicit_source_evidence_and_pinned_inputs(sample):
    # The first record represents an imported prerequisite in a book project.
    sample.config["sources"].append({"id": "imported", "title": "Imported", "authors": [], "status": "available"})
    first = next(iter(sample.nodes.values()))
    first["evidence"] = [{"source": "imported", "section": "Prerequisite", "pages": [1]}]
    manifest, _ = record_index([sample])
    result = inventory(proposal_for(manifest), manifest)
    native = {sample.config["id"]: [s["id"] for s in sample.config["sources"] if s["id"] != "imported"]}
    result = resolve_coverage(result, [sample], native)
    assert verify_inventory(result, manifest, [sample])["records"] == len(sample.nodes)
    concept = result["concepts"][0]
    assert sum(concept["book_counts"].values()) == len(sample.nodes)
    assert sum(concept["independent_book_counts"].values()) == len(sample.nodes) - 1
    changed_count = deepcopy(result)
    changed_count["concepts"][0]["independent_book_counts"][sample.config["id"]] += 1
    with pytest.raises(ProjectError, match="counts disagree"):
        verify_inventory(changed_count, manifest, [sample])
    changed_membership = deepcopy(result)
    changed_membership["concepts"][0]["treatments"].pop()
    with pytest.raises(ProjectError, match="unassigned"):
        verify_inventory(changed_membership, manifest, [sample])
    first["summary"] = "A changed input must invalidate the coverage export."
    with pytest.raises(ProjectError, match="changed"):
        resolve_coverage(result, [sample], native)
