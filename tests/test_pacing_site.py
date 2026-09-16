from datetime import timedelta
import json
from pathlib import Path

import pytest

from syllabusgraph import agents, pacing, site, workflow as wf
from syllabusgraph.cli import main
from syllabusgraph.io import ProjectError, write_json
from test_workflow import unit

__all__ = ["unit"]


def send(project):
    return agents.dispatch(project, "unit-one", stage="extract", orchestrator="host")


def test_slow_default_requires_start_counts_failures_and_resumes(unit):
    project, _, _ = unit
    agents.configure(project)
    with pytest.raises(ProjectError, match="work start"):
        send(project)
    first = pacing.start(project)
    assert first["dispatches_remaining"] == 2
    for _ in range(2):
        ticket = send(project)
        agents.fail(project, "unit-one", ticket["id"], reason="Fixture runtime unavailable")
    with pytest.raises(ProjectError, match="allowance reached"):
        send(project)
    # Policy changes must not renew a work budget.
    agents.configure(project, audit_mode="trust")
    assert pacing.status(project)["dispatches_remaining"] == 0
    with pytest.raises(ProjectError, match="already exists"):
        pacing.start(project)
    pacing.start(project, resume=True)
    assert pacing.status(project)["dispatches_remaining"] == 2
    assert len(list((project.local / "work-sessions").glob("*.json"))) == 1


def test_serial_blocks_duplicate_and_other_unit_but_allows_late_result(unit, monkeypatch):
    project, _, proposal = unit
    agents.configure(project)
    pacing.start(project)
    ticket = send(project)
    wf.prepare(project, "unit-two", "primer", 2, 2, scope="Another scope")
    for name in ("unit-one", "unit-two"):
        with pytest.raises(ProjectError, match="Worker limit"):
            agents.dispatch(project, name, stage="extract", orchestrator="host")
    with pytest.raises(ProjectError, match="pending dispatch"):
        pacing.start(project, resume=True)
    current = pacing.now()
    monkeypatch.setattr(pacing, "now", lambda: current + timedelta(minutes=21))
    report = pacing.status(project)
    assert report["active"][0]["check_progress"]
    assert report["pause_reason"] == "session deadline reached"
    agents.complete(
        project,
        "unit-one",
        ticket["id"],
        proposal,
        agent_id="extractor",
        model=ticket["model"],
        effort=ticket["effort"],
    )
    assert (wf.unit_dir(project, "unit-one") / "proposal.json").exists()
    assert wf.read_json(
        wf.unit_dir(project, "unit-one") / "dispatches" / ticket["id"] / "done.json"
    )["completed_at"]
    with pytest.raises(ProjectError, match="expired"):
        agents.dispatch(project, "unit-one", stage="critique", orchestrator="host")


def test_pause_keeps_result_and_resume_does_not_reextract(unit):
    project, _, proposal = unit
    agents.configure(project)
    pacing.start(project)
    ticket = send(project)
    pacing.pause(project)
    agents.complete(
        project,
        "unit-one",
        ticket["id"],
        proposal,
        agent_id="extractor",
        model=ticket["model"],
        effort=ticket["effort"],
    )
    pacing.start(project, resume=True)
    assert pacing.status(project)["units"][0]["status"] == "proposed"
    critic = agents.dispatch(project, "unit-one", stage="critique", orchestrator="host")
    assert critic["stage"] == "critique"


def test_recovery_family_shares_six_call_budget(unit):
    project, _, _ = unit
    agents.configure(project)
    pacing.start(project, dispatches=10)
    for _ in range(5):
        t = send(project)
        agents.fail(project, "unit-one", t["id"], reason="Fixture failure")
    wf.prepare(project, "unit-two", "primer", 2, 2, scope="New evidence")
    pacing.family(project, "unit-two", "unit-one")
    t = agents.dispatch(project, "unit-two", stage="extract", orchestrator="host")
    agents.fail(project, "unit-two", t["id"], reason="Fixture failure")
    with pytest.raises(ProjectError, match="family dispatch budget exhausted"):
        agents.dispatch(project, "unit-two", stage="extract", orchestrator="host")
    pacing.start(project, resume=True)
    with pytest.raises(ProjectError, match="family dispatch budget exhausted"):
        agents.dispatch(project, "unit-two", stage="extract", orchestrator="host")
    with pytest.raises(ProjectError, match="immutable"):
        pacing.family(project, "unit-two", "unit-one")


def test_context_limit_rejects_before_ticket_and_cli_reports(unit, capsys):
    project, _, _ = unit
    agents.configure(project)
    pacing.start(project, request_kb=1)
    with pytest.raises(ProjectError, match="context allowance"):
        send(project)
    assert not pacing.tickets(project)
    assert main(["work", "-p", str(project.root), "status"]) == 0
    assert json.loads(capsys.readouterr().out)["dispatches_used"] == 0


def test_static_export_is_source_free_and_preserves_graph(sample, tmp_path):
    (sample.root / "materials/private.txt").write_text("PRIVATE MARKER")
    write_json(sample.local / "private.json", {"secret": "PRIVATE MARKER"})
    out = tmp_path / "site"
    manifest = site.build_site([{"path": sample.root}], out)
    payload = json.loads((out / manifest["graphs"][0]["file"]).read_text(encoding="utf-8"))
    assert payload["knowledge"] == sample.knowledge
    assert payload["digest"] == sample.content_digest
    assert "PRIVATE MARKER" not in "\n".join(p.read_text(encoding="utf-8") for p in out.rglob("*") if p.is_file())
    assert not list(out.rglob("*.pdf"))
    (out / "accidental-private.txt").write_text("private")
    with pytest.raises(ProjectError, match="unexpected"):
        site.build_site([{"path": sample.root}], out)
    assert (out / "accidental-private.txt").exists()
    with pytest.raises(ProjectError, match="contain an input"):
        site.build_site([{"path": sample.root}], sample.root)


def test_graph_only_export_and_cli(blank, tmp_path):
    for p in (blank.root / "plans").glob("*.yaml"):
        p.unlink()
    catalog = tmp_path / "catalog.json"
    write_json(catalog, {"graphs": [{"id": "blank", "path": str(blank.root)}]})
    assert main(["site", "build", "--catalog", str(catalog), "--out", str(tmp_path / "web")]) == 0
    assert (tmp_path / "web/data/blank.json").exists()
    payload = json.loads((tmp_path / "web/data/blank.json").read_text(encoding="utf-8"))
    assert not payload["knowledge"]["nodes"]


def test_site_overlap_excludes_imported_textbook_inputs(tmp_path):
    # Compare independently against the bank checker on the real public collection.
    from scripts.check_graph_bank import inspect_bank

    root = Path(__file__).resolve().parents[1]
    manifest = site.build_catalog(root / "site/catalog.json", tmp_path / "site")
    assert len(manifest["graphs"]) == 5
    payload = json.loads((tmp_path / "site/data/qft.json").read_text(encoding="utf-8"))
    bank = inspect_bank(root / "graphs")
    for row in bank["overlap"]:
        expected = set(row["shared_nodes"])
        actual = {
            n for n, books in payload["direct_books"].items() if set(row["books"]) <= set(books)
        }
        assert actual == expected
