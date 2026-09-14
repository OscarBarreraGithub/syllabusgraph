from copy import deepcopy

import pytest

from syllabusgraph import agents, workflow as wf
from syllabusgraph.io import ProjectError, digest, write_json, write_yaml
from test_agents import critique, decision, extracted, send
from test_workflow import unit

__all__ = ["unit"]


def test_adverse_critique_and_pending_stage_cannot_be_bypassed(unit):
    project, proposal = extracted(unit)
    pending = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    with pytest.raises(ProjectError, match="active dispatch"):
        agents.dispatch(project, "unit-one", stage="adjudicate", orchestrator="host-session")
    agents.fail(project, "unit-one", pending["id"], reason="Critic runtime unavailable.")

    critique(project, proposal, "revise")
    with pytest.raises(ProjectError, match="Resolve adverse critic findings"):
        agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")

    send(project, "extract", proposal)
    with pytest.raises(ProjectError):
        agents.dispatch(project, "unit-one", stage="adjudicate", orchestrator="host-session")
    critique(project, proposal)


def test_policy_change_does_not_reset_cumulative_rejection_gate(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "reject")
    agents.configure(project, audit_mode="trust")

    with pytest.raises(ProjectError, match="adjudicator"):
        agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")


def test_response_import_crash_keeps_dispatch_active_for_recovery(unit):
    project, proposal = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    value = {
        "proposal_digest": digest(proposal),
        "verdict": "accept",
        "notes": ["Checked the proposal against its source witness."],
    }
    provenance = {
        "dispatch_id": task["id"],
        "agent_id": "critic-after-crash",
        "model": task["model"],
        "effort": task["effort"],
    }
    dispatch_dir = wf.unit_dir(project, "unit-one") / "dispatches" / task["id"]
    write_json(dispatch_dir / "result.json", {"provenance": provenance, "value": value})

    with pytest.raises(ProjectError, match="active dispatch"):
        agents.dispatch(project, "unit-one", stage="extract", orchestrator="host-session")

    agents.complete(
        project,
        "unit-one",
        task["id"],
        value,
        agent_id=provenance["agent_id"],
        model=task["model"],
        effort=task["effort"],
    )
    assert (dispatch_dir / "done.json").exists()


def test_identical_new_producer_still_requires_fresh_critic(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)

    send(project, "extract", proposal, identity="second-extractor")
    with pytest.raises(ProjectError, match="fresh critique"):
        wf.promote(project, "unit-one")

    critique(project, proposal)
    wf.promote(project, "unit-one")


def test_adjudication_rejects_duplicate_alternatives_and_findings(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")

    duplicate_alternative = decision(proposal)
    duplicate_alternative["decisions"][0]["alternatives"] = [
        "Keep the current definition",
        "Keep the current definition",
    ]
    with pytest.raises(ProjectError, match="two alternatives"):
        send(project, "adjudicate", duplicate_alternative)

    duplicate_finding = decision(proposal)
    duplicate_finding["decisions"].append(deepcopy(duplicate_finding["decisions"][0]))
    with pytest.raises(ProjectError, match="Every critic finding"):
        send(project, "adjudicate", duplicate_finding)


def test_stale_policy_authorization_allows_new_work_to_repair(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")
    send(project, "adjudicate", decision(proposal))

    agents.configure(project, critic_model="replacement-critic")
    send(project, "extract", proposal, identity="repair-extractor")
    result = send(
        project,
        "critique",
        {
            "proposal_digest": digest(proposal),
            "verdict": "accept",
            "notes": ["Rechecked after the policy change."],
        },
        identity="replacement-critic-session",
    )
    assert result["recorded"] is True


def test_policy_change_can_close_an_unfinished_dispatch(unit):
    project, proposal = extracted(unit)
    critique(project, proposal, "revise")
    pending = agents.dispatch(project, "unit-one", stage="adjudicate", orchestrator="host-session")
    agents.configure(project, audit_mode="trust")

    failure = agents.fail(
        project,
        "unit-one",
        pending["id"],
        reason="Policy changed before the adjudicator started.",
    )
    assert failure["dispatch_id"] == pending["id"]


def test_exact_atomic_promotion_recovery_uses_reviewed_base(unit):
    project, proposal = extracted(unit)
    critique(project, proposal)
    expected = agents.accepted_candidate(project, "unit-one", proposal)

    write_yaml(project.root / "knowledge" / "graph.yaml", expected)
    receipt = wf.promote(project, "unit-one")

    assert receipt["knowledge_digest"] == digest(expected)


def test_repeated_completion_is_file_level_idempotent(unit):
    project, proposal = extracted(unit)
    task = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host-session")
    value = {
        "proposal_digest": digest(proposal),
        "verdict": "accept",
        "notes": ["Checked the proposal against its source witness."],
    }
    arguments = {
        "agent_id": "idempotent-critic",
        "model": task["model"],
        "effort": task["effort"],
    }
    first = agents.complete(project, "unit-one", task["id"], value, **arguments)
    directory = wf.unit_dir(project, "unit-one")
    before = {
        str(path.relative_to(directory)): path.read_bytes()
        for path in directory.rglob("*")
        if path.is_file()
    }

    second = agents.complete(project, "unit-one", task["id"], value, **arguments)
    after = {
        str(path.relative_to(directory)): path.read_bytes()
        for path in directory.rglob("*")
        if path.is_file()
    }

    assert second == first
    assert after == before
