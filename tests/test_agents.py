from copy import deepcopy
import json
import sys

import pytest

from syllabusgraph import agents, workflow as wf
from syllabusgraph.cli import main
from syllabusgraph.io import ProjectError, digest, write_json, write_yaml
from syllabusgraph.project import load_project
from test_workflow import unit  # shared original, two-page source fixture

__all__ = ["unit"]


def send(project, stage, value, *, identity=None):
    task = agents.dispatch(project, "unit-one", stage=stage, orchestrator="host-session")
    return agents.complete(
        project,
        "unit-one",
        task["id"],
        value,
        agent_id=identity or "worker-" + task["id"],
        model=task["model"],
        effort=task["effort"],
    )


def extracted(unit):
    project, _, proposal = unit
    agents.configure(project)
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
    custom = agents.configure(
        blank, extractor_model="gpt-5.6-luna", orchestrator_model="gpt-6-astra", audit_mode="trust"
    )
    assert custom["critic"] == {"model": "gpt-5.6-sol", "effort": "high"}
    assert custom["extractor"]["model"] == "gpt-5.6-luna"
    with pytest.raises(ProjectError, match="explicit models"):
        agents.configure(blank, extractor_model="inherit")


def test_manual_draft_cannot_bypass_mandatory_critic(unit):
    project, _, proposal = unit
    wf.import_proposal(project, "unit-one", proposal)
    with pytest.raises(ProjectError, match="mandatory critic"):
        wf.review(project, "unit-one", decision="accept", reviewer="operator", notes=["Looks good"])


def test_dispatch_requires_accepted_policy_and_runtime_roles(unit):
    project, _, proposal = unit
    with pytest.raises(ProjectError, match="Accept an agent policy"):
        agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")
    agents.configure(project, orchestrator_model="gpt-6-astra")
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
    critique(project, proposal)
    critique(project, proposal, "reject")
    with pytest.raises(ProjectError, match="critic requested"):
        wf.promote(project, "unit-one")


def test_policy_and_proposal_changes_invalidate_review(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    agents.configure(project, critic_model="custom-reviewer")
    with pytest.raises(ProjectError, match="policy changed"):
        wf.promote(project, "unit-one")
    agents.configure(project)
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


def test_revision_limit_forces_documented_adjudication(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")
    send(project, "extract", proposal)
    critique(project, proposal, "revise")
    with pytest.raises(ProjectError, match="adjudicator"):
        send(project, "extract", proposal)
    send(project, "adjudicate", decision(proposal))
    critique(project, proposal)
    wf.promote(project, "unit-one")
    assert agents.audit(project)["units"][0]["decision_history"]


def test_adjudicator_override_requires_evidence_and_fresh_critic(unit):
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
    with pytest.raises(ProjectError):
        wf.promote(project, "unit-one")
    critique(project, proposal)
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
    send(project, "adjudicate", decision(proposal))
    with pytest.raises(ProjectError, match="failures"):
        critique(project, proposal)
    assert not wf.check(project, "unit-one")["ok"]


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
    agents.configure(project, audit_mode="trust")
    assert agents.audit(project)["audit_status"] == "trusted-critic"


def test_tampered_dispatch_is_rejected(unit):
    project, _, proposal = unit
    agents.configure(project)
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


def test_adjudication_needs_findings_and_independent_final_critic(unit):
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
    with pytest.raises(ProjectError, match="fresh independent critic"):
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
    critique(project, proposal, "reject")
    with pytest.raises(ProjectError, match="superseded"):
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
