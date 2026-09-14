import json
from pathlib import Path
import runpy

import pytest


REPORT = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts/report_usage.py"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def dispatch(project, identity, *, at="2026-09-14T12:00:00+00:00", stage="critique", agent=None):
    folder = project / ".syllabusgraph/runs/unit/dispatches" / identity
    write(folder / "ticket.json", {
        "id": identity, "unit": "unit", "at": at, "stage": stage,
        "model": "test-reviewer", "effort": "high",
    })
    if agent:
        write(folder / "result.json", {
            "provenance": {"agent_id": agent},
            "value": {"private_text": "DO_NOT_EXPORT_SOURCE_TEXT"},
        })
    return folder


def test_calls_sessions_cutoff_and_failure_overlap(tmp_path):
    project = tmp_path / "project"
    dispatch(project, "old", at="2026-09-13T12:00:00+00:00", agent="old-worker")
    dispatch(project, "first", agent="PRIVATE_WORKER_ID")
    second = dispatch(project, "second", stage="adjudicate", agent="PRIVATE_WORKER_ID")
    write(second / "failures/check.json", {"reason": "DO_NOT_EXPORT_FAILURE"})
    dispatch(project, "pending")
    report = REPORT["summarize"]([project, project], since=REPORT["timestamp"]("2026-09-14T00:00:00Z"))
    assert report["dispatches_recorded"] == 3
    assert report["native_results_recorded"] == 2
    assert report["distinct_confirmed_worker_sessions"] == 1
    assert report["dispatches_with_failure_records"] == 1
    assert report["source_work_unit_dispatch_histogram"] == {3: 1}
    serialized = json.dumps(report)
    assert "DO_NOT_EXPORT" not in serialized
    assert "PRIVATE_WORKER_ID" not in serialized
    assert str(tmp_path) not in serialized


def test_distinct_projects_and_missing_logs(tmp_path):
    left, right = tmp_path / "left", tmp_path / "right"
    dispatch(left, "same-id", agent="one")
    dispatch(right, "same-id", agent="two")
    report = REPORT["summarize"]([left, right, tmp_path / "no-local-logs"])
    assert report["dispatches_recorded"] == 2
    assert report["source_work_units"] == 2
    assert REPORT["summarize"]([tmp_path / "no-local-logs"])["dispatches_recorded"] == 0


def test_supplemental_ledger_deduplication_and_binding(tmp_path):
    ticket = {"request_digest": "request-one", "model": "test-extractor", "effort": "high"}
    completion = {"request_digest": "request-one", "recorded": True, "agent": "worker"}
    for name in ("one", "copy"):
        write(tmp_path / f"{name}-dispatch.json", ticket)
        write(tmp_path / f"{name}-completion.json", completion)
    write(tmp_path / "normal-pointer-dispatch.json", {**ticket, "id": "already-counted-elsewhere"})
    report = REPORT["summarize"]([], extra_dispatch_dir=tmp_path)
    assert report["dispatches_recorded"] == 1
    assert report["native_results_recorded"] == 1
    write(tmp_path / "copy-completion.json", {**completion, "request_digest": "wrong-request"})
    with pytest.raises(ValueError, match="does not match"):
        REPORT["summarize"]([], extra_dispatch_dir=tmp_path)


def test_goal_snapshot_exports_only_measured_fields(tmp_path):
    path = tmp_path / "snapshot.json"
    goal = {"tokens_used": 123, "elapsed_seconds": 60,
            "started_at": "2026-09-14T12:00:00Z", "updated_at": "2026-09-14T12:01:00Z",
            "objective": "PRIVATE_TASK"}
    write(path, {"goal": goal, "private_log": "DO_NOT_EXPORT"})
    report = REPORT["goal_measurement"](path)
    assert report["reported_tokens"] == 123
    assert report["billed_cost"] is None
    assert "PRIVATE_TASK" not in json.dumps(report)
    write(path, {"goal": {**goal, "tokens_used": True}})
    with pytest.raises(ValueError, match="Invalid goal counter"):
        REPORT["goal_measurement"](path)
