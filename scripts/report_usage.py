"""Summarize local dispatch metadata without exporting prompts or source material."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path


def read(path):
    return json.loads(path.read_text())


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def summarize(projects, *, since=None, extra_dispatch_dir=None):
    records = {}
    units = Counter()
    for project in sorted({Path(p).resolve() for p in projects}):
        for path in sorted((project / ".syllabusgraph/runs").glob("*/dispatches/*/ticket.json")):
            ticket = read(path)
            if since and timestamp(ticket["at"]) < since:
                continue
            directory = path.parent
            result = read(directory / "result.json") if (directory / "result.json").exists() else None
            provenance = result.get("provenance", {}) if result else {}
            key = (str(project), ticket["unit"], ticket["id"])
            records[key] = {
                "model": ticket["model"], "effort": ticket["effort"],
                "stage": ticket["stage"], "kind": "source-workflow",
                "has_result": result is not None,
                "has_failure": any((directory / "failures").glob("*.json")),
                "agent": provenance.get("agent_id"),
            }
            units[(str(project), ticket["unit"])] += 1
    if extra_dispatch_dir:
        for path in sorted(Path(extra_dispatch_dir).glob("*-dispatch.json")):
            ticket = read(path)
            # Normal workflow pointer files duplicate the immutable tickets above.
            if "id" in ticket or "request_digest" not in ticket:
                continue
            at = ticket.get("recorded_at")
            if since and (not at or timestamp(at) < since):
                continue
            model = ticket.get("model", ticket.get("native_model"))
            if not model:
                continue
            completion_path = path.with_name(path.name.replace("-dispatch.json", "-completion.json"))
            completion = read(completion_path) if completion_path.exists() else None
            if completion and completion.get("request_digest") != ticket["request_digest"]:
                raise ValueError("Custom completion does not match its dispatch")
            records[("custom", ticket["request_digest"])] = {
                "model": model, "effort": ticket.get("effort", "unspecified"),
                "stage": ticket.get("stage", "scheduling"), "kind": "supplemental-ledger",
                "has_result": bool(completion and completion.get("recorded")),
                "has_failure": False,
                "agent": completion.get("agent") if completion else None,
            }
    groups = defaultdict(list)
    for record in records.values():
        groups[(record["model"], record["effort"], record["stage"], record["kind"])].append(record)

    def counts(rows):
        return {
            "dispatches_recorded": len(rows),
            "native_results_recorded": sum(r["has_result"] for r in rows),
            "dispatches_with_failure_records": sum(r["has_failure"] for r in rows),
            "distinct_confirmed_worker_sessions": len({r["agent"] for r in rows if r["agent"]}),
        }

    return {
        "since": since.isoformat() if since else None,
        **counts(list(records.values())),
        "source_work_units": len(units),
        "source_work_unit_dispatch_histogram": dict(sorted(Counter(units.values()).items())),
        "by_model_effort_stage": [
            {"model": model, "effort": effort, "stage": stage, "record_type": kind, **counts(rows)}
            for (model, effort, stage, kind), rows in sorted(groups.items())
        ],
    }


def goal_measurement(path):
    """Export only numeric counters and timestamps; never copy free-text metadata."""
    snapshot = read(path)
    goal = snapshot["goal"]
    for name in ("tokens_used", "elapsed_seconds"):
        value = goal[name]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError(f"Invalid goal counter: {name}")
    return {
        "reported_tokens": goal["tokens_used"],
        "reported_elapsed_seconds": goal["elapsed_seconds"],
        "started_at": timestamp(goal["started_at"]).isoformat(),
        "counter_updated_at": timestamp(goal["updated_at"]).isoformat(),
        "token_breakdown": None,
        "billed_cost": None,
        "child_agent_token_coverage": "not specified by the counter interface",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("projects", nargs="+", type=Path)
    parser.add_argument("--since", help="Only dispatches issued at or after this ISO timestamp")
    parser.add_argument("--goal-snapshot", type=Path, help="Optional locally recorded host goal counters")
    parser.add_argument("--extra-dispatch-dir", type=Path, help="Optional supplemental dispatch/completion ledgers")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    goal = goal_measurement(args.goal_snapshot) if args.goal_snapshot else None
    since = timestamp(args.since) if args.since else timestamp(goal["started_at"]) if goal else None
    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "goal_counter": goal,
        "dispatch_accounting": summarize(args.projects, since=since, extra_dispatch_dir=args.extra_dispatch_dir),
        "limitations": [
            "Dispatch counts measure recorded work requests, not tokens or inference time. Failures can also have recorded native results; these columns overlap.",
            "Distinct worker sessions count only identities confirmed in recorded results. A session can serve multiple calls and stages; row counts must not be summed for a global session count.",
            "Work without these local ledgers, including orchestration and some setup or support tasks, is absent from dispatch totals. Missing logs are not zero historical usage.",
            "Goal counters cover their reported goal interval. Input, cached input, output, model-specific tokens and child-agent inclusion are not inferred from an aggregate counter.",
            "Elapsed goal time is not summed worker compute time. Historical active worker hours and peak concurrency are not reconstructed from file modification times.",
            "No monetary cost is inferred; use provider usage records with the applicable rates for billing estimates.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["dispatch_accounting"]))


if __name__ == "__main__":
    main()
