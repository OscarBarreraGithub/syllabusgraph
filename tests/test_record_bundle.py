import json

import pytest

from scripts.build_record_bundle import record_bundle
from syllabusgraph.io import ProjectError


def test_record_bundle_keeps_selected_records_and_scoped_edges(sample):
    ids = list(sample.nodes)[:2]
    manifest = {"graph_digest": sample.content_digest, "records": ids}
    text = record_bundle(sample, manifest)
    pages = [json.loads(page) for page in text.split("\f")]
    assert [p["bundle_page"] for p in pages] == [1, 2]
    assert [p["record"] for p in pages] == [sample.nodes[id] for id in ids]
    emitted = [e for p in pages for e in p["outgoing_within_selection"]]
    assert emitted == [e for e in sample.knowledge["edges"] if {e["from"], e["to"]} <= set(ids)]
    assert text == record_bundle(sample, manifest)


def test_record_bundle_rejects_stale_or_ambiguous_inputs(sample):
    identity = next(iter(sample.nodes))
    for digest, ids in [("stale", [identity]), (sample.content_digest, [identity] * 2),
                        (sample.content_digest, ["missing"]), (sample.content_digest, [])]:
        with pytest.raises(ProjectError):
            record_bundle(sample, {"graph_digest": digest, "records": ids})
