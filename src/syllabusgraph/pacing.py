"""Local dispatch budgets. No scheduler, provider quota inference, or model client."""

from datetime import datetime, timedelta, timezone
from uuid import uuid4

from .io import ProjectError, write_json, canonical
from . import workflow as wf


def now():
    return datetime.now(timezone.utc)


def tickets(project):
    return [
        (p, wf.read_json(p))
        for p in sorted((project.local / "runs").glob("*/dispatches/*/ticket.json"))
    ]


def pending(project):
    return [
        (p, t)
        for p, t in tickets(project)
        if not (p.parent / "done.json").exists() and not any((p.parent / "failures").glob("*.json"))
    ]


def initialize(project):
    """Called while configuring policy under the project lock; preserve old sessions."""
    path = project.local / "work-budget.json"
    if not path.exists():
        write_json(path, {"version": 1, "family_limit": 6, "families": {}, "session": None})


def read(project):
    path = project.local / "work-budget.json"
    if not path.exists():
        raise ProjectError("Start a bounded session with work start before dispatching.")
    return wf.read_json(path)


def start(project, *, dispatches=2, minutes=20, resume=False, workers=1, request_kb=750):
    if type(dispatches) is not int or not 1 <= dispatches <= 100:
        raise ProjectError("Session dispatch allowance must be 1–100.")
    if type(minutes) is not int or not 1 <= minutes <= 1440:
        raise ProjectError("Session duration must be 1–1440 minutes.")
    if type(workers) is not int or not 1 <= workers <= 32:
        raise ProjectError("Worker concurrency must be 1–32.")
    if type(request_kb) is not int or not 1 <= request_kb <= 20000:
        raise ProjectError("Request size allowance must be 1–20000 KB.")
    with wf.project_lock(project):
        initialize(project)
        budget = read(project)
        previous = budget.get("session")
        if previous and not resume:
            raise ProjectError(
                "A session already exists. Inspect work status; use --resume only for a newly authorized session."
            )
        if pending(project):
            raise ProjectError(
                "Finish or record failure of the pending dispatch before starting a session."
            )
        if previous:
            write_json(project.local / "work-sessions" / (previous["id"] + ".json"), previous)
        at = now()
        budget["session"] = {
            "id": uuid4().hex,
            "started_at": at.isoformat(),
            "expires_at": (at + timedelta(minutes=minutes)).isoformat(),
            "dispatch_limit": dispatches,
            "paused": False,
            "workers": workers,
            "request_bytes": request_kb * 1000,
        }
        write_json(project.local / "work-budget.json", budget)
    return status(project)


def pause(project):
    with wf.project_lock(project):
        budget = read(project)
        if budget.get("session"):
            budget["session"]["paused"] = True
            write_json(project.local / "work-budget.json", budget)
    return status(project)


def family(project, unit, parent):
    """Link recoveries before issuance. Historical calls count, including failures."""
    if unit == parent:
        raise ProjectError("Recovery unit and parent must differ.")
    with wf.project_lock(project):
        wf.read_json(wf.unit_dir(project, unit) / "state.json")
        wf.read_json(wf.unit_dir(project, parent) / "state.json")
        budget = read(project)
        mapping = budget["families"]
        if mapping.get(parent) == unit:
            raise ProjectError("Recovery families cannot form cycles.")
        root = mapping.get(parent, parent)
        if unit in mapping or any(t["unit"] == unit for _, t in tickets(project)):
            raise ProjectError(
                "Link a fresh recovery unit before its first dispatch; family links are immutable."
            )
        if unit in mapping.values():
            raise ProjectError("A family root with children cannot be relinked.")
        mapping[unit] = root
        write_json(project.local / "work-budget.json", budget)
    return {"unit": unit, "family": root, "limit": budget["family_limit"]}


def status(project):
    path = project.local / "work-budget.json"
    budget = (
        read(project) if path.exists() else {"session": None, "families": {}, "family_limit": 6}
    )
    session = budget["session"]
    all_tickets = tickets(project)
    used = sum(t.get("work_session") == session["id"] for _, t in all_tickets) if session else 0
    reason = (
        "not started"
        if not session
        else "paused"
        if session["paused"]
        else "dispatch allowance reached"
        if used >= session["dispatch_limit"]
        else "session deadline reached"
        if now() >= datetime.fromisoformat(session["expires_at"])
        else None
    )
    active = []
    for p, t in all_tickets:
        if (p.parent / "done.json").exists() or any((p.parent / "failures").glob("*.json")):
            continue
        age = max(0, (now() - datetime.fromisoformat(t["at"])).total_seconds())
        active.append(
            {
                "unit": t["unit"],
                "dispatch": t["id"],
                "stage": t["stage"],
                "minutes_since_dispatch": round(age / 60, 1),
                "check_progress": age >= 600,
            }
        )
    units = []
    for path in sorted((project.local / "runs").glob("*/state.json")):
        s = wf.read_json(path)
        units.append(
            {
                "unit": path.parent.name,
                "status": s["status"],
                "active_dispatch": s.get("active_dispatch"),
            }
        )
    return {
        "session": session,
        "dispatches_used": used,
        "dispatches_remaining": max(0, session["dispatch_limit"] - used) if session else 0,
        "can_dispatch": reason is None and len(active) < session.get("workers", 1),
        "pause_reason": reason,
        "active": active,
        "units": units,
        "limits": "Limits gate new worker dispatches, not tokens or in-flight calls. Orchestrator usage is outside this budget.",
        "next": "Finish/check the existing dispatch first."
        if active
        else "Resume only on a new user request; do not renew allowances automatically."
        if reason
        else "Continue from recorded unit state; do not repeat accepted work.",
    }


def guard(project, unit):
    """Run inside the dispatch write lock. Never prevents saving a worker result."""
    budget = read(project)
    session = budget.get("session")
    if not session:
        raise ProjectError("Start a bounded session with work start before dispatching.")
    if session["paused"] or now() >= datetime.fromisoformat(session["expires_at"]):
        raise ProjectError(
            "Work session paused or expired. Save results and stop; resume on a new user request."
        )
    all_tickets = tickets(project)
    if (
        sum(t.get("work_session") == session["id"] for _, t in all_tickets)
        >= session["dispatch_limit"]
    ):
        raise ProjectError(
            "Session dispatch allowance reached. Save results and stop; do not auto-renew."
        )
    outstanding = pending(project)
    if any(t["unit"] == unit for _, t in outstanding) or len(outstanding) >= session.get(
        "workers", 1
    ):
        raise ProjectError(
            "Worker limit reached: complete or fail the pending dispatch before issuing another."
        )
    root = budget["families"].get(unit, unit)
    calls = sum(budget["families"].get(t["unit"], t["unit"]) == root for _, t in all_tickets)
    if calls >= budget["family_limit"]:
        raise ProjectError(
            "Recovery family dispatch budget exhausted. Defer unresolved work; do not reset it under a new ID."
        )
    return session["id"]


def check_request(project, request):
    session = read(project)["session"]
    size = len(canonical(request))
    if size > session.get("request_bytes", 750000):
        raise ProjectError(
            f"Request is {size} bytes, exceeding the session context allowance. "
            "No worker was dispatched. Reduce the scope or explicitly choose a larger allowance; "
            "never silently raise it. Full current graph context contributes to this size."
        )
    return size
