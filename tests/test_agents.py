from copy import deepcopy
import json
import sys

import pytest

from syllabusgraph import agents, pacing, workflow as wf
from syllabusgraph.cli import main
from syllabusgraph.io import ProjectError, digest, write_json, write_yaml
from syllabusgraph.project import load_project
from test_workflow import unit  # shared original, two-page source fixture

__all__ = ["unit"]


def configure(project, *args, **kwargs):
    """Existing review tests explicitly opt into a large session budget."""
    result = agents.configure(project, *args, **kwargs)
    if pacing.read(project)['session'] is None:
        pacing.start(project, dispatches=100, minutes=60, workers=2)
    return result


def send(project, stage, value, *, identity=None):
    task = agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session")
    try:
        return agents.complete(
            project, "unit-one", task["id"], value,
            agent_id=identity or "worker-" + task["id"],
            model=task["model"], effort=task["effort"],
        )
    except ProjectError:
        agents.fail(project, "unit-one", task["id"], reason="Rejected test response.")
        raise



def extracted(unit):
    project, _, proposal = unit
    configure(project)
    send(project, "extract", proposal, identity="extractor-session")
    return project, proposal


def critique(project, proposal, verdict="accept"):
    return send(
        project,
        "critique",
        {
            "proposal_digest": digest(proposal),
            "verdict": verdict,
            "notes": ["Definition checked against the source and existing concepts."],
        },
    )


def decision(proposal):
    return {
        "verdict": "accept",
        "proposal": proposal,
        "decisions": [
            {
                "issue": "Conflicting definition",
                "finding": 0,
                "alternatives": [
                    "Retain the old definition",
                    "Use the source-supported definition",
                ],
                "resolution": "Use the source-supported definition",
                "rationale": "The source defines an event as a set of outcomes.",
                "evidence": [{"source": "primer", "section": "Events", "pages": [1]}],
                "affected_records": [{"kind": "nodes", "id": "event"}],
            }
        ],
    }


def test_provider_defaults_custom_roles_and_cli(blank, capsys):
    assert agents.policy(blank, required=False)["accepted"] is False
    assert (
        main(
            [
                "agent",
                "-p",
                str(blank.root),
                "configure",
                "--provider",
                "claude",
                "--accept-defaults",
            ]
        )
        == 0
    )
    assert agents.policy(blank)["extractor"] == {"model": "sonnet", "effort": "high"}
    assert agents.policy(blank)["critic"]["model"] == "opus"
    custom = configure(
        blank, extractor_model="gpt-5.6-luna", orchestrator_model="gpt-6-astra", audit_mode="trust"
    )
    assert custom["critic"] == {"model": "gpt-5.6-sol", "effort": "high"}
    assert custom["extractor"]["model"] == "gpt-5.6-luna"
    with pytest.raises(ProjectError, match="explicit models"):
        configure(blank, extractor_model="inherit")


def test_manual_draft_cannot_bypass_mandatory_critic(unit):
    project, _, proposal = unit
    wf.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError, match="mandatory critic"):
        wf.review(project, "unit-one", decision="accept", reviewer="operator", notes=["Looks good"])


def test_dispatch_requires_accepted_policy_and_runtime_roles(unit):
    project, _, proposal = unit
    with pytest.raises(ProjectError, match="Accept an agent policy"):
        agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    configure(project, orchestrator_model="gpt-6-astra")
    with pytest.raises(ProjectError, match="Configured orchestrator"):
        agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    task = agents.dispatch(
        project,
        "unit-one",
        stage="extract",
        orchestrator="host-session",
        orchestrator_model="gpt-6-astra",
    )
    for identity, model, effort, message in [
        ("host-session", "gpt-5.6-terra", "high", "separate worker"),
        ("worker", "gpt-5.6-luna", "high", "differs"),
        ("worker", "gpt-5.6-terra", "low", "differs"),
    ]:
        with pytest.raises(ProjectError, match=message):
            agents.complete(
                project,
                "unit-one",
                task["id"],
                proposal,
                agent_id=identity,
                model=model,
                effort=effort,
            )
    assert not (wf.unit_dir(project, "unit-one") / "proposal.json").exists()


def test_independent_critic_and_latest_rejection_gate_promotion(unit):
    project, proposal = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    value = {
        "proposal_digest": digest(proposal),
        "verdict": "accept",
        "notes": ["Checked the definition."],
    }
    with pytest.raises(ProjectError, match="own critic"):
        agents.complete(
            project,
            "unit-one",
            task["id"],
            value,
            agent_id="extractor-session",
            model="gpt-5.6-sol",
            effort="high",
        )
    agents.fail(project, "unit-one", task["id"], reason="Non-independent critic rejected.")
    critique(project, proposal)
    critique(project, proposal, "reject")
    with pytest.raises(ProjectError, match="critic requested"):
        wf.promote(project, "unit-one")


def test_policy_and_proposal_changes_invalidate_review(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    configure(project, critic_model="custom-reviewer")
    with pytest.raises(ProjectError, match="policy changed"):
        wf.promote(project, "unit-one")
    configure(project)
    changed = deepcopy(proposal)
    changed["graph"]["nodes"][0]["summary"] = "A changed definition."
    wf.import_proposal(project, "unit-one", changed)
    with pytest.raises(ProjectError, match="exact proposal"):
        wf.promote(project, "unit-one")
    with pytest.raises(ProjectError):
        critique(project, changed)  # current critic alone cannot bless an un-dispatched edit


def test_dispatch_staleness_immutable_results_and_retry(unit):
    project, proposal = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    changed = deepcopy(proposal)
    changed["graph"]["nodes"][0]["summary"] = "Changed after dispatch."
    wf.import_proposal(project, "unit-one", changed)
    value = {"proposal_digest": digest(proposal), "verdict": "accept", "notes": ["Checked."]}
    with pytest.raises(ProjectError, match="Proposal changed"):
        agents.complete(
            project,
            "unit-one",
            task["id"],
            value,
            agent_id="critic",
            model="gpt-5.6-sol",
            effort="high",
        )
    wf.import_proposal(project, "unit-one", proposal)
    agents.complete(
        project,
        "unit-one",
        task["id"],
        value,
        agent_id="critic",
        model="gpt-5.6-sol",
        effort="high",
    )
    agents.complete(
        project,
        "unit-one",
        task["id"],
        value,
        agent_id="critic",
        model="gpt-5.6-sol",
        effort="high",
    )
    value["verdict"] = "reject"
    with pytest.raises(ProjectError, match="immutable"):
        agents.complete(
            project,
            "unit-one",
            task["id"],
            value,
            agent_id="critic",
            model="gpt-5.6-sol",
            effort="high",
        )


def advance_graph(project, node=None):
    knowledge = deepcopy(project.knowledge)
    knowledge["nodes"].append(node or {
        "id": "frequency",
        "label": "Frequency",
        "summary": "A count divided by the total.",
        "kind": "concept",
        "evidence": [{"source": "primer", "section": "Frequencies", "pages": [2]}],
    })
    write_yaml(project.root / project.config["knowledge"], knowledge)
    return load_project(project.root)


def test_extraction_can_finish_after_graph_update_but_needs_current_review(unit):
    project, packet, proposal = unit
    configure(project)
    task = agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    other_packet = wf.prepare(project, "unit-two", "primer", 2, 2, scope="Define frequency.")
    other = deepcopy(proposal)
    other.update(packet_digest=other_packet["packet_digest"], pages_read=[2], quote_checks=[{
        "source": "primer", "page": 2, "quote": "A frequency is a count divided by the total."
    }])
    other["graph"]["nodes"] = [{
        "id": "frequency", "label": "Frequency", "kind": "concept",
        "summary": "A count divided by the total.",
        "evidence": [{"source": "primer", "section": "Frequencies", "pages": [2]}],
    }]
    for stage, value in [("extract", other), ("critique", {
        "proposal_digest": digest(other), "verdict": "accept",
        "notes": ["Checked the frequency definition against page two."],
    })]:
        other_task = agents.dispatch(project, "unit-two", stage=stage, orchestrator="host-session")
        agents.complete(project, "unit-two", other_task["id"], value,
                        agent_id="other-" + stage, model=other_task["model"],
                        effort=other_task["effort"])
    wf.promote(project, "unit-two")
    fresh = load_project(project.root)
    agents.complete(project, "unit-one", task["id"], proposal,
                    agent_id="extractor", model=task["model"], effort=task["effort"])
    directory = wf.unit_dir(fresh, "unit-one")
    assert load_project(project.root).knowledge == fresh.knowledge
    assert wf.read_json(directory / "packet.json") == packet
    assert wf.read_json(directory / "state.json")["status"] == "proposed"
    assert not (directory / "review.json").exists()
    with pytest.raises(ProjectError, match="mandatory critic"):
        wf.review(fresh, "unit-one", decision="accept", reviewer="operator", notes=["Checked."])
    task = agents.dispatch(fresh, "unit-one", stage="critique", orchestrator="host-session")
    request = wf.read_json(directory / "dispatches" / task["id"] / "request.json")
    assert request["current_knowledge"] == fresh.knowledge
    assert request["checks"]["warnings"]
    agents.complete(fresh, "unit-one", task["id"],
                    {"proposal_digest": digest(proposal), "verdict": "accept",
                     "notes": ["Checked against the updated graph and source."]},
                    agent_id="critic", model=task["model"], effort=task["effort"])
    wf.promote(fresh, "unit-one")
    assert set(load_project(project.root).nodes) == {"event", "frequency"}


def test_stale_extraction_cannot_overwrite_a_concurrently_added_record(unit):
    project, _, proposal = unit
    configure(project)
    task = agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    accepted = deepcopy(proposal["graph"]["nodes"][0])
    accepted["summary"] = "An accepted, differently scoped event definition."
    fresh = advance_graph(project, accepted)
    agents.complete(project, "unit-one", task["id"], proposal,
                    agent_id="extractor", model=task["model"], effort=task["effort"])
    assert not wf.check(fresh, "unit-one")["ok"]
    with pytest.raises(ProjectError, match="source-check failures"):
        critique(fresh, proposal)
    assert load_project(project.root).nodes["event"] == accepted
    assert not (wf.unit_dir(fresh, "unit-one") / "receipt.json").exists()


@pytest.mark.parametrize("stage", ["critique", "adjudicate"])
def test_review_dispatch_still_rejects_graph_changes(unit, stage):
    project, proposal = extracted(unit)
    if stage == "adjudicate":
        critique(project, proposal, "reject")
    task = agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session")
    fresh = advance_graph(project)
    value = decision(proposal) if stage == "adjudicate" else {
        "proposal_digest": digest(proposal), "verdict": "accept", "notes": ["Checked."]}
    with pytest.raises(ProjectError, match="Knowledge changed during dispatch"):
        agents.complete(fresh, "unit-one", task["id"], value,
                        agent_id="reviewer", model=task["model"], effort=task["effort"])
    assert load_project(project.root).knowledge == fresh.knowledge
    assert not (wf.unit_dir(fresh, "unit-one") / "review.json").exists()


def test_revision_limit_forces_documented_adjudication(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")
    send(project, "extract", proposal)
    critique(project, proposal, "revise")
    with pytest.raises(ProjectError, match="adjudicator"):
        send(project, "extract", proposal)
    send(project, "adjudicate", decision(proposal))
    wf.promote(project, "unit-one")
    report = agents.audit(project)["units"][0]
    assert report["decision_history"]
    assert [d["stage"] for d in report["dispatch_history"]] == [
        "extract",
        "critique",
        "extract",
        "critique",
        "adjudicate",
    ]


def test_adjudicator_override_is_final_and_requires_evidence(unit):
    project, proposal = extracted(unit)
    old = deepcopy(proposal["graph"])
    old["nodes"][0]["summary"] = "One single outcome only."
    write_yaml(project.root / "knowledge/graph.yaml", old)
    project = load_project(project.root)
    assert not wf.check(project, "unit-one")["ok"]
    critique(project, proposal, "revise")
    bad = decision(proposal)
    bad["decisions"][0]["affected_records"] = []
    with pytest.raises(ProjectError, match="Every overridden"):
        send(project, "adjudicate", bad)
    bad = decision(proposal)
    bad["decisions"][0]["evidence"][0]["pages"] = [2]
    with pytest.raises(ProjectError, match="quote witnesses"):
        send(project, "adjudicate", bad)
    send(project, "adjudicate", decision(proposal))
    assert wf.check(project, "unit-one")["ok"]
    receipt = wf.promote(project, "unit-one")
    assert receipt["critic"]["model"] == "gpt-5.6-sol"
    assert (
        load_project(project.root).nodes["event"]["summary"]
        == proposal["graph"]["nodes"][0]["summary"]
    )
    assert wf.promote(project, "unit-one") == receipt


def test_adjudication_cannot_override_mechanical_evidence_checks(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")
    proposal["quote_checks"][0]["quote"] = "This sentence never appeared."
    result = send(project, "adjudicate", decision(proposal))
    assert result["status"] == "deferred"
    with pytest.raises(ProjectError, match="Deferred"):
        wf.promote(project, "unit-one")
    assert not wf.check(project, "unit-one")["ok"]


@pytest.fixture
def removable_edge_unit(unit):
    project, packet, proposal = unit
    base = deepcopy(proposal["graph"])
    other = deepcopy(base["nodes"][0])
    other.update(id="outcome", label="Outcome")
    base["nodes"].append(other)
    base["edges"].append({
        "id": "unsupported-input", "from": "outcome", "to": "event",
        "relation": "prerequisite", "source_level": "use", "target_level": "recognize",
        "necessity": "necessary", "rationale": "An overstated prerequisite.",
        "failure_mode": "This claim needs source review.",
        "evidence": [{"source": "primer", "section": "Events", "pages": [1]}],
    })
    write_yaml(project.root / "knowledge/graph.yaml", base)
    project, proposal = extracted((load_project(project.root), packet, proposal))
    value = decision(proposal)
    value["removals"] = [{"kind": "edges", "id": "unsupported-input"}]
    value["decisions"][0]["affected_records"] = deepcopy(value["removals"])
    return project, proposal, value


def test_final_edge_removal_is_explicit_and_recovers_atomically(removable_edge_unit):
    project, proposal, value = removable_edge_unit
    # Omitting a canonical edge from a proposal is never an implicit deletion.
    assert wf._combine(project, proposal["graph"])["edges"][0]["id"] == "unsupported-input"
    critique(project, proposal, "revise")
    send(project, "adjudicate", value)
    assert wf.check(project, "unit-one")["ok"]
    expected = agents.accepted_candidate(project, "unit-one", proposal)
    assert expected["edges"] == []
    assert {n["id"] for n in expected["nodes"]} == {"event", "outcome"}
    # A crash after writing the graph must still recover the exact reviewed removal.
    write_yaml(project.root / "knowledge/graph.yaml", expected)
    receipt = wf.promote(project, "unit-one")
    assert load_project(project.root).knowledge == expected
    assert wf.promote(project, "unit-one") == receipt
    history = agents.audit(project)["units"][0]["decision_history"]
    assert any(entry.get("removals") == value["removals"] for entry in history)


def test_critic_cannot_authorize_removal(removable_edge_unit):
    project, proposal, value = removable_edge_unit
    with pytest.raises(ProjectError, match="Only final adjudication"):
        send(project, "critique", {"proposal_digest": digest(proposal), "verdict": "accept",
                                  "notes": ["Remove the unsupported prerequisite."],
                                  "removals": value["removals"]})
    assert len(load_project(project.root).knowledge["edges"]) == 1


def test_removal_authorization_cannot_be_changed_after_final(removable_edge_unit):
    project, proposal, value = removable_edge_unit
    critique(project, proposal, "revise")
    send(project, "adjudicate", value)
    path = wf.unit_dir(project, "unit-one") / "adjudication.json"
    record = wf.read_json(path)
    record["removals"] = []
    write_json(path, record)
    with pytest.raises(ProjectError, match="Adjudication record changed"):
        wf.promote(project, "unit-one")
    assert len(load_project(project.root).knowledge["edges"]) == 1


@pytest.mark.parametrize("case, message", [
    ("undocumented", "affected-record decision"),
    ("unknown", "unknown accepted edge"),
    ("duplicate", "Duplicate edge removal"),
    ("also-proposed", "both proposed and removed"),
    ("node", "explicit existing edge identities"),
    ("defer", "deferral cannot remove"),
])
def test_invalid_removals_preserve_canonical_graph(removable_edge_unit, case, message):
    project, proposal, value = removable_edge_unit
    critique(project, proposal, "revise")
    before = deepcopy(project.knowledge)
    if case == "undocumented":
        value["decisions"][0]["affected_records"] = []
    elif case == "unknown":
        value["removals"][0]["id"] = "missing-edge"
    elif case == "duplicate":
        value["removals"] *= 2
    elif case == "also-proposed":
        value["proposal"]["graph"]["edges"] = deepcopy(before["edges"])
    elif case == "node":
        value["removals"] = [{"kind": "nodes", "id": "event"}]
    else:
        value["verdict"] = "defer"
    with pytest.raises(ProjectError, match=message):
        send(project, "adjudicate", value)
    assert load_project(project.root).knowledge == before


def test_human_audit_is_final_optional_and_snapshot_bound(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    wf.promote(project, "unit-one")
    report = agents.audit(project)
    assert report["audit_status"] == "pending-human-audit"
    assert report["unfinished_units"] == []
    assert (
        agents.audit(
            project, reviewer="human reviewer", notes="Checked decisions and source coverage."
        )["audit_status"]
        == "reviewed"
    )
    changed = load_project(project.root)
    changed.config["title"] = "A revised course"
    write_yaml(project.root / "project.yaml", changed.config)
    assert agents.audit(project)["audit_status"] == "pending-human-audit"
    configure(project, audit_mode="trust")
    assert agents.audit(project)["audit_status"] == "trusted-critic"


def test_tampered_dispatch_is_rejected(unit):
    project, _, proposal = unit
    configure(project)
    task = agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    path = wf.unit_dir(project, "unit-one") / "dispatches" / task["id"] / "request.json"
    request = wf.read_json(path)
    request["scope"] = "Unapproved scope"
    write_json(path, request)
    with pytest.raises(ProjectError, match="request changed"):
        agents.complete(
            project,
            "unit-one",
            task["id"],
            proposal,
            agent_id="worker",
            model=task["model"],
            effort=task["effort"],
        )


def test_adjudication_needs_findings_and_ends_review(unit):
    project, proposal = extracted(unit)
    with pytest.raises(ProjectError):
        send(project, "adjudicate", decision(proposal))
    critique(project, proposal)
    with pytest.raises(ProjectError, match="current critic findings"):
        send(project, "adjudicate", decision(proposal))
    critique(project, proposal, "revise")
    bad = decision(proposal)
    bad["decisions"][0]["finding"] = 1
    with pytest.raises(ProjectError, match="Every critic finding"):
        send(project, "adjudicate", bad)
    send(project, "adjudicate", decision(proposal), identity="adjudicator-session")
    with pytest.raises(ProjectError, match="Final adjudication"):
        send(
            project,
            "critique",
            {"proposal_digest": digest(proposal), "verdict": "accept", "notes": ["Checked."]},
            identity="adjudicator-session",
        )


def test_recovery_cannot_bless_unreviewed_graph_superset(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    superset = deepcopy(proposal["graph"])
    other = deepcopy(superset["nodes"][0])
    other["id"] = "unreviewed-concept"
    superset["nodes"].append(other)
    write_yaml(project.root / "knowledge/graph.yaml", superset)
    with pytest.raises(ProjectError, match="changed since acceptance"):
        wf.promote(project, "unit-one")


def test_pending_new_critic_and_superseded_result_block_old_acceptance(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    with pytest.raises(ProjectError, match="latest critic"):
        wf.promote(project, "unit-one")
    agents.fail(project, "unit-one", task["id"], reason="Superseded critic stopped.")
    critique(project, proposal, "reject")
    with pytest.raises(ProjectError, match="failed"):
        agents.complete(
            project,
            "unit-one",
            task["id"],
            {
                "proposal_digest": digest(proposal),
                "verdict": "accept",
                "notes": ["Stale reviewer."],
            },
            agent_id="old-critic",
            model="gpt-5.6-sol",
            effort="high",
        )
    with pytest.raises(ProjectError, match="critic requested"):
        wf.promote(project, "unit-one")


def test_native_failures_and_human_audits_preserve_history(unit):
    project, proposal = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    agents.fail(
        project, "unit-one", task["id"], reason="Requested model unavailable in this account."
    )
    report = agents.audit(project)
    assert any(d["failures"] for d in report["units"][0]["dispatch_history"])
    critique(project, proposal)
    wf.promote(project, "unit-one")
    agents.audit(project, reviewer="first human", notes="Checked decisions.")
    report = agents.audit(project, reviewer="second human", notes="Checked scope.")
    assert len(report["human_audit_history"]) == 2


@pytest.mark.parametrize("stage", ["extract", "critique", "adjudicate"])
def test_explicit_runner_binds_to_native_dispatch(unit, tmp_path, stage):
    project, proposal = extracted(unit)
    value = proposal
    if stage == "critique":
        value = {
            "proposal_digest": digest(proposal),
            "verdict": "accept",
            "notes": ["Checked definition against the source."],
        }
    elif stage == "adjudicate":
        critique(project, proposal, "revise")
        value = decision(proposal)
    task = agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session")
    result_file = tmp_path / "result.json"
    result_file.write_text(json.dumps(value))
    runner = tmp_path / "adapter.py"
    runner.write_text(
        "import json,sys\nr=json.load(sys.stdin)\nassert r['dispatch']['stage']==sys.argv[1]\nprint(open(sys.argv[2]).read())\n"
    )
    result = wf.run(
        project,
        "unit-one",
        [sys.executable, str(runner), stage, str(result_file)],
        stage=stage,
        model=task["model"],
        effort=task["effort"],
        dispatch_id=task["id"],
        agent_id="adapter-session",
    )
    assert result["recorded"]
    assert agents.audit(project)["units"][0]["dispatch_history"][-1]["completed"]


def test_bound_runner_failure_is_preserved_in_audit(unit):
    project, _ = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    with pytest.raises(ProjectError, match="Runner failed"):
        wf.run(
            project,
            "unit-one",
            [sys.executable, "-c", "raise SystemExit(4)"],
            stage="critique",
            model=task["model"],
            effort=task["effort"],
            dispatch_id=task["id"],
            agent_id="failed-adapter",
        )
    history = agents.audit(project)["units"][0]["dispatch_history"]
    assert history[-1]["failures"][0]["dispatch_id"] == task["id"]
    with pytest.raises(ProjectError, match="without rerunning"):
        wf.run(
            project,
            "unit-one",
            [sys.executable, "-c", "raise AssertionError('must not rerun')"],
            stage="critique",
            model=task["model"],
            effort=task["effort"],
            dispatch_id=task["id"],
            agent_id="failed-adapter",
        )


def test_final_deferral_is_visible_and_does_not_block_other_units(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "reject")
    value = decision(proposal)
    value["verdict"] = "defer"
    value["decisions"][0]["resolution"] = "Defer until notation can be verified."
    value["decisions"][0]["rationale"] = "The source evidence cannot settle the reported ambiguity."
    value["decisions"][0]["evidence"] = []  # Deferral must not require invented support.
    record = send(project, "adjudicate", value)
    assert record["status"] == "deferred"
    assert not load_project(project.root).nodes
    report = agents.audit(project)
    assert report["deferred_units"] == ["unit-one"]
    assert report["unfinished_units"] == []
    assert report["units"][0]["deferral"]["reason"]
    for stage in ("extract", "critique", "adjudicate"):
        assert (
            agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session") == record
        )
    with pytest.raises(ProjectError, match="closed"):
        wf.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError, match="Deferred"):
        wf.promote(project, "unit-one")
    from syllabusgraph.cli import _coverage

    assert _coverage(project, "primer", 1, 1)["missing_pages"] == [1]
    wf.prepare(project, "unit-two", "primer", 2, 2, scope="Define frequency.")
    assert (
        agents.dispatch(project, "unit-two", stage="extract", orchestrator="host-session")["stage"]
        == "extract"
    )


def test_retry_budget_closes_unit_even_when_runtime_never_completes(unit):
    project, _, _ = unit
    configure(project)
    for attempt in range(6):
        task = agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
        agents.fail(
            project, "unit-one", task["id"], reason=f"Runtime failed on attempt {attempt + 1}."
        )
    # Reconfiguration cannot reset a work unit's original budget.
    configure(project, revision_limit=10)
    record = agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    assert record["status"] == "deferred"
    assert "6 calls" in record["reason"]
    assert len(agents.audit(project)["units"][0]["dispatch_history"]) == 6


def test_final_adjudication_cannot_request_another_review(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "reject")
    bad = decision(proposal)
    bad["verdict"] = "revise"
    with pytest.raises(ProjectError, match="final decision"):
        send(project, "adjudicate", bad)
    send(project, "adjudicate", decision(proposal))
    for stage in ("extract", "critique", "adjudicate"):
        with pytest.raises(ProjectError, match="Final adjudication"):
            agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session")
    # Recover a crash after the final decision's atomic graph write.
    expected = agents.accepted_candidate(project, "unit-one", proposal)
    write_yaml(project.root / "knowledge/graph.yaml", expected)
    assert wf.promote(project, "unit-one")["knowledge_digest"] == digest(expected)
