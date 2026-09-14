from copy import deepcopy
import json
import sys

import pytest

from syllabusgraph.io import ProjectError, digest, within, write_json, write_yaml
from syllabusgraph.project import load_project
from syllabusgraph.sources import register, source_pages
from syllabusgraph import agents, workflow


@pytest.fixture
def unit(blank, tmp_path):
    config = deepcopy(blank.config)
    config["sources"] = [
        {"id": "primer", "title": "An original primer", "authors": [], "status": "expected"}
    ]
    write_yaml(blank.root / "project.yaml", config)
    project = load_project(blank.root)
    text = tmp_path / "primer.txt"
    text.write_text("An event is a set of outcomes.\fA frequency is a count divided by the total.")
    register(project, "primer", text)
    packet = workflow.prepare(project, "unit-one", "primer", 1, 1, scope="Define events.")
    proposal = {
        "packet_digest": packet["packet_digest"],
        "pages_read": [1],
        "unresolved": [],
        "quote_checks": [
            {"source": "primer", "page": 1, "quote": "An event is a set of outcomes."}
        ],
        "graph": {
            "nodes": [
                {
                    "id": "event",
                    "label": "Event",
                    "summary": "A collection of possible outcomes.",
                    "kind": "concept",
                    "evidence": [{"source": "primer", "section": "Events", "pages": [1]}],
                }
            ],
            "edges": [],
            "groups": [],
            "motivations": [],
        },
    }
    return project, packet, proposal


def accept(project):
    directory = workflow.unit_dir(project, "unit-one")
    proposal = workflow.read_json(directory / "proposal.json")
    agents.configure(project)
    task = agents.dispatch(project, "unit-one", stage="extract", orchestrator="test-orchestrator")
    agents.complete(
        project,
        "unit-one",
        task["id"],
        proposal,
        agent_id="test-extractor",
        model="gpt-5.6-terra",
        effort="high",
    )
    if not (directory / "critique.json").exists():
        task = agents.dispatch(
            project, "unit-one", stage="critique", orchestrator="test-orchestrator"
        )
        agents.complete(
            project,
            "unit-one",
            task["id"],
            {
                "proposal_digest": digest(proposal),
                "verdict": "accept",
                "notes": ["Read the source and checked the proposed definition against it."],
            },
            agent_id="test-critic",
            model="gpt-5.6-sol",
            effort="high",
        )
    return workflow.review(
        project,
        "unit-one",
        decision="accept",
        reviewer="test reviewer",
        notes=["Read the source and checked the proposed definition against it."],
    )


def test_complete_manual_workflow_and_idempotent_promotion(unit):
    project, packet, proposal = unit
    assert workflow.prepare(project, "unit-one", "primer", 1, 1, scope="Define events.") == packet
    workflow.import_proposal(project, "unit-one", proposal)
    assert workflow.check(project, "unit-one")["ok"]
    accept(project)
    first = workflow.promote(project, "unit-one")
    assert workflow.promote(load_project(project.root), "unit-one") == first
    fresh = load_project(project.root)
    assert "event" in fresh.nodes
    assert "quote_checks" not in json.dumps(fresh.knowledge)
    assert workflow.status(fresh)["units"][0]["status"] == "merged"


def test_pdf_import_preserves_printed_page_mapping(blank, tmp_path):
    from pypdf import PdfWriter
    from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

    blank.config["sources"] = [
        {"id": "pdf-primer", "title": "Original PDF fixture", "authors": [], "status": "expected"}
    ]
    writer = PdfWriter()
    for text in ["Front matter", "An event is a set of outcomes."]:
        page = writer.add_blank_page(width=300, height=300)
        font = DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
            }
        )
        page[NameObject("/Resources")] = DictionaryObject(
            {NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})}
        )
        stream = DecodedStreamObject()
        stream.set_data(f"BT /F1 12 Tf 20 250 Td ({text}) Tj ET".encode("ascii"))
        page[NameObject("/Contents")] = stream
    path = tmp_path / "original.pdf"
    writer.write(path)
    entry = register(blank, "pdf-primer", path, offset=1)
    assert entry["page_count"] == 2
    packet = workflow.prepare(blank, "pdf-unit", "pdf-primer", 1, 1, scope="Define events.")
    assert packet["pages"] == [
        {"print_page": 1, "pdf_page": 2, "text": "An event is a set of outcomes."}
    ]
    with pytest.raises(ProjectError, match="outside"):
        workflow.prepare(blank, "outside", "pdf-primer", 2, 2, scope="Beyond the source.")


@pytest.mark.parametrize("changed_page,context,stale", [(0, False, True), (1, True, True), (1, False, False)])
def test_new_reader_output_for_same_file_invalidates_only_affected_packets(
    unit, monkeypatch, changed_page, context, stale
):
    from syllabusgraph import sources

    project, _, proposal = unit
    packet = workflow.prepare(
        project, "reader-change", "primer", 1, 1, scope="Same original file, changed reader.",
        context=[{"source": "primer", "first": 2, "last": 2}] if context else [],
    )
    proposal["packet_digest"] = packet["packet_digest"]
    workflow.import_proposal(project, "reader-change", proposal)
    entry, old_pages = source_pages(project, "primer")
    new_pages = list(old_pages)
    new_pages[changed_page] += " Additional text recovered by another reader."
    monkeypatch.setattr(sources, "extract_pages", lambda path: new_pages)
    replacement = register(project, "primer", project.root / entry["file"], replace=True)
    assert replacement["sha256"] == entry["sha256"]
    assert replacement["text_digest"] != entry["text_digest"]
    if stale:
        with pytest.raises(ProjectError, match="page text changed"):
            workflow.check(project, "reader-change")
    else:
        assert workflow.check(project, "reader-change")["ok"]


def test_successful_retry_clears_failure_status(unit):
    project, _, proposal = unit
    directory = workflow.unit_dir(project, "unit-one")
    write_json(directory / "last_failure.json", {"reason": "timeout"})
    workflow.import_proposal(project, "unit-one", proposal)
    assert not workflow.status(project)["units"][0]["retryable_failure"]


def test_review_needs_nonempty_notes(unit):
    project, _, proposal = unit
    workflow.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError, match="substantive"):
        workflow.review(
            project, "unit-one", decision="accept", reviewer="test reviewer", notes=["  "]
        )


def test_cannot_promote_without_exact_acceptance(unit):
    project, _, proposal = unit
    workflow.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError):
        workflow.promote(project, "unit-one")
    accept(project)
    proposal["graph"]["nodes"][0]["summary"] = "Revised definition after review."
    workflow.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError, match="exact proposal"):
        workflow.promote(project, "unit-one")


@pytest.mark.parametrize(
    "quote",
    ["An event is a set of outcome", "event is a set of out", "An event is a single outcome."],
)
def test_inexact_or_truncated_quotes_fail(unit, quote):
    project, _, proposal = unit
    proposal["quote_checks"][0]["quote"] = quote
    workflow.import_proposal(project, "unit-one", proposal)
    assert not workflow.check(project, "unit-one")["ok"]
    with pytest.raises(ProjectError, match="failures"):
        accept(project)


def test_cited_pages_each_need_a_witness(unit):
    project, _, proposal = unit
    proposal["graph"]["nodes"][0]["evidence"][0]["pages"] = [1, 2]
    workflow.import_proposal(project, "unit-one", proposal)
    assert any("missing verified quote" in e for e in workflow.check(project, "unit-one")["errors"])


def test_coverage_and_unresolved_claims_block_review(unit):
    project, _, proposal = unit
    proposal["pages_read"] = [2]
    proposal["unresolved"] = ["Unsure whether the proposed definition is correct."]
    workflow.import_proposal(project, "unit-one", proposal)
    report = workflow.check(project, "unit-one")
    assert len(report["errors"]) >= 2


def test_changed_source_and_cache_are_detected(unit, tmp_path):
    project, _, proposal = unit
    entry, _ = source_pages(project, "primer")
    write_json(within(project.root, entry["text"]), ["A forged cached page."])
    with pytest.raises(ProjectError, match="Cached"):
        workflow.import_proposal(project, "unit-one", proposal)


def test_changed_mapping_invalidates_packet(unit, tmp_path):
    project, _, proposal = unit
    entry, _ = source_pages(project, "primer")
    register(project, "primer", within(project.root, entry["file"]), offset=1, replace=True)
    with pytest.raises(ProjectError, match="changed"):
        workflow.import_proposal(project, "unit-one", proposal)


def test_packet_edits_are_detected(unit):
    project, packet, proposal = unit
    packet["scope"] = "An edited contract."
    write_json(workflow.unit_dir(project, "unit-one") / "packet.json", packet)
    with pytest.raises(ProjectError, match="changed"):
        workflow.import_proposal(project, "unit-one", proposal)


def test_new_base_requires_new_review(unit):
    project, _, proposal = unit
    workflow.import_proposal(project, "unit-one", proposal)
    accept(project)
    other = deepcopy(proposal["graph"])
    other["nodes"][0]["id"] = "another-event"
    write_yaml(project.root / "knowledge/graph.yaml", other)
    with pytest.raises(ProjectError, match="changed since acceptance"):
        workflow.promote(project, "unit-one")


def test_atomic_graph_write_recovery(unit):
    project, _, proposal = unit
    workflow.import_proposal(project, "unit-one", proposal)
    accept(project)
    # Simulate a crash after the atomic graph replacement, before receipt/state.
    write_yaml(project.root / "knowledge/graph.yaml", workflow._combine(project, proposal["graph"]))
    receipt = workflow.promote(project, "unit-one")
    assert receipt["knowledge_digest"] == digest(load_project(project.root).knowledge)


def test_conflicting_existing_concept_is_not_overwritten(unit):
    project, _, proposal = unit
    other = deepcopy(proposal["graph"])
    other["nodes"][0]["summary"] = "An incompatible meaning."
    write_yaml(project.root / "knowledge/graph.yaml", other)
    project = load_project(project.root)
    workflow.import_proposal(project, "unit-one", proposal)
    assert any("Conflicting" in e for e in workflow.check(project, "unit-one")["errors"])


def test_command_runner_protocol_and_retry(unit, tmp_path):
    project, _, proposal = unit
    runner = tmp_path / "runner.py"
    data = tmp_path / "proposal.json"
    data.write_text(json.dumps(proposal))
    runner.write_text(
        "import json,sys\npacket=json.load(sys.stdin)\nassert packet['stage']=='extract'\nprint(open(sys.argv[1]).read())\n"
    )
    result = workflow.run(
        project, "unit-one", [sys.executable, str(runner), str(data)], model="test-runner-v1"
    )
    assert result["status"] == "proposed"
    with pytest.raises(ProjectError, match="did not complete"):
        workflow.run(
            project,
            "unit-one",
            [sys.executable, "-c", "import time; time.sleep(5)"],
            model="timeout-test",
            timeout=0.05,
        )
    assert workflow.check(project, "unit-one")["ok"]


def test_critic_revision_cannot_be_silently_accepted(unit):
    project, _, proposal = unit
    workflow.import_proposal(project, "unit-one", proposal)
    write_json(
        workflow.unit_dir(project, "unit-one") / "critique.json",
        {"proposal_digest": digest(proposal), "verdict": "revise", "notes": ["Review a claim."]},
    )
    with pytest.raises(ProjectError, match="critic"):
        accept(project)


def test_work_unit_ids_cannot_escape_local_storage(unit):
    project, _, _ = unit
    with pytest.raises(ProjectError):
        workflow.unit_dir(project, "../../escape")


def test_scanned_or_empty_text_needs_attention(blank, tmp_path):
    blank.config["sources"] = [
        {"id": "empty", "title": "Empty", "authors": [], "status": "expected"}
    ]
    path = tmp_path / "empty.txt"
    path.write_text("   ")
    with pytest.raises(ProjectError, match="No extractable"):
        register(blank, "empty", path)


def test_witnesses_need_explicit_packet_context(unit):
    project, _, proposal = unit
    proposal["quote_checks"].append(
        {"source": "primer", "page": 2, "quote": "A frequency is a count divided by the total."}
    )
    workflow.import_proposal(project, "unit-one", proposal)
    assert any(
        "outside the immutable packet" in e for e in workflow.check(project, "unit-one")["errors"]
    )
    packet = workflow.prepare(
        project,
        "with-context",
        "primer",
        1,
        1,
        scope="Compare definitions.",
        context=[{"source": "primer", "first": 2, "last": 2}],
    )
    assert packet["context_pages"][0]["print_page"] == 2
    proposal["packet_digest"] = packet["packet_digest"]
    workflow.import_proposal(project, "with-context", proposal)
    assert workflow.check(project, "with-context")["ok"]


def test_context_source_changes_invalidate_whole_packet(unit, tmp_path):
    project, _, _ = unit
    config = deepcopy(project.config)
    config["sources"].append(
        {"id": "second", "title": "Second original primer", "authors": [], "status": "expected"}
    )
    write_yaml(project.root / "project.yaml", config)
    project = load_project(project.root)
    source = tmp_path / "second.txt"
    source.write_text("An event can contain multiple outcomes.")
    register(project, "second", source)
    workflow.prepare(
        project,
        "comparison",
        "primer",
        1,
        1,
        scope="Compare sources.",
        context=[{"source": "second", "first": 1, "last": 1}],
    )
    source.write_text("An updated comparison source.")
    register(project, "second", source, replace=True)
    with pytest.raises(ProjectError, match="context source changed"):
        workflow._ensure_packet(project, workflow.unit_dir(project, "comparison"))
