"""Mastery-sensitive prerequisite closure and transparent session planning."""

from __future__ import annotations

from collections import defaultdict, deque
from copy import deepcopy
import math

from .graph import layout, topological
from .io import ProjectError, digest
from .project import Project, validate_plan


def _background(project: Project, plan: dict) -> tuple[dict[str, str], dict[str, str]]:
    levels = project.levels
    background, origin = {}, {}
    for prior_id in plan.get("prior_plans", []):
        prior = project.plans[prior_id]
        if prior["status"] != "ready" or not prior["outcomes"]:
            raise ProjectError(f"Prior course {prior_id} must have ready, explicit outcomes.")
        # Validate the predecessor itself before trusting its promised exit mastery.
        prior_result = build_plan(project, prior)
        if any(i["severity"] == "error" for i in prior_result["issues"]):
            raise ProjectError(f"Prior course {prior_id} has unresolved planning errors.")
        for outcome in prior["outcomes"]:
            node, level = outcome["node"], outcome["level"]
            if node not in background or levels[level] > levels[background[node]]:
                background[node], origin[node] = level, prior_id
    # Explicit audience answers override inherited assumptions, including downgrades.
    for node, level in plan["background"].items():
        background[node], origin[node] = level, "audience"
    for node in plan.get("unknown", []):
        background.pop(node, None)
        origin.pop(node, None)
    return background, origin


def _partition(order: list[str], nodes: dict, levels: dict, count: int, capacity: int) -> list:
    """Exact contiguous partition; report missing estimates separately from the cost model."""
    n = len(order)
    if not n:
        return []
    if n > 1000:
        raise ProjectError(
            "This plan selects more than 1,000 concepts. Split the course or specify more entry background before session planning."
        )
    count = min(count, n)
    known = [
        sum(nodes[i]["estimates"][levels[i]][k] for k in ("min", "max")) / 2
        for i in order
        if levels[i] in nodes[i].get("estimates", {})
    ]
    neutral = sorted(known)[len(known) // 2] if known else 1
    weights = []
    for node in order:
        estimate = nodes[node].get("estimates", {}).get(levels[node])
        weights.append((estimate["min"] + estimate["max"]) / 2 if estimate else neutral)
    # With no timing evidence, balance concept counts; never present this as minutes.
    target = capacity if known else max(sum(weights) / count, 1)
    prefix = [0.0]
    for weight in weights:
        prefix.append(prefix[-1] + weight)
    group = [nodes[i].get("group", "") for i in order]
    costs = {}
    for start in range(n):
        seen = set()
        for end in range(start + 1, n + 1):
            seen.add(group[end - 1])
            load = (prefix[end] - prefix[start]) / target
            cut = 0.3 if end < n and group[end - 1] == group[end] else 0
            costs[start, end] = (
                (load - 1) ** 2 + 3 * max(load - 1, 0) ** 2 + cut + 0.12 * (len(seen) - 1)
            )
    scores = {(0, 0): 0.0}
    previous = {}
    for k in range(1, count + 1):
        for end in range(k, n - (count - k) + 1):
            best = (math.inf, -1)
            for start in range(k - 1, end):
                candidate = scores.get((k - 1, start), math.inf) + costs[start, end]
                if (candidate, start) < best:
                    best = candidate, start
            scores[k, end], previous[k, end] = best
    segments, end = [], n
    for k in range(count, 0, -1):
        start = previous[k, end]
        segments.append(order[start:end])
        end = start
    return list(reversed(segments))


def build_plan(project: Project, plan: dict | str) -> dict:
    if isinstance(plan, str):
        if plan not in project.plans:
            raise ProjectError(f"Unknown course plan: {plan}")
        plan = project.plans[plan]
    validate_plan(project, plan)
    ranks, nodes = project.levels, project.nodes
    issues = []
    try:
        background, background_origin = _background(project, plan)
    except ProjectError as exc:
        background = {
            k: v for k, v in plan["background"].items() if k not in plan.get("unknown", [])
        }
        background_origin = dict.fromkeys(background, "audience")
        issues.append({"severity": "error", "code": "prior_plan", "message": str(exc), "nodes": []})
    targets = {o["node"]: o["level"] for o in plan["outcomes"]}
    for node, level in plan.get("include", {}).items():
        if node not in targets or ranks[level] > ranks[targets[node]]:
            targets[node] = level
    for node, level in plan.get("treatments", {}).items():
        if node in targets and ranks[level] < ranks[targets[node]]:
            issues.append(
                {
                    "severity": "warning",
                    "code": "outcome_depth",
                    "message": f"{nodes[node]['label']}: the stated outcome requires {targets[node]}; a lower treatment cannot satisfy it.",
                    "nodes": [node],
                }
            )
        elif node in targets:
            targets[node] = level
    if not targets:
        issues.append(
            {
                "severity": "warning",
                "code": "empty",
                "message": "Choose learning outcomes or include a concept to begin.",
                "nodes": [],
            }
        )
    omitted = set(plan.get("omit", []))
    allowed = set(plan.get("necessity", ["necessary", "typical"]))
    edges = [
        e
        for e in project.knowledge["edges"]
        if e["relation"] == "prerequisite" and e["necessity"] in allowed
    ]
    incoming = defaultdict(list)
    for edge in edges:
        incoming[edge["to"]].append(edge)
    for rows in incoming.values():
        rows.sort(key=lambda e: e["id"])
    required, required_by, assumed_used = {}, defaultdict(set), {}
    queue = deque(sorted(targets.items()))
    while queue:
        node, level = queue.popleft()
        if node in background and ranks[background[node]] >= ranks[level] and node not in targets:
            old = assumed_used.get(node)
            if old is None or ranks[level] > ranks[old]:
                assumed_used[node] = level
            continue
        treatment = plan.get("treatments", {}).get(node)
        if treatment and ranks[treatment] > ranks[level]:
            level = treatment
        if node in required and ranks[required[node]] >= ranks[level]:
            continue
        required[node] = level
        if node in omitted:
            continue
        for edge in incoming[node]:
            if ranks[level] >= ranks[edge["target_level"]]:
                required_by[edge["from"]].add(node)
                queue.append((edge["from"], edge["source_level"]))
    for node in sorted(omitted & required.keys()):
        issues.append(
            {
                "severity": "error",
                "code": "omitted_requirement",
                "message": f"{nodes[node]['label']} is omitted but required by this plan.",
                "nodes": [node, *sorted(required_by[node])],
            }
        )
    for node, requested in plan.get("treatments", {}).items():
        if node in required and node not in targets and ranks[requested] < ranks[required[node]]:
            issues.append(
                {
                    "severity": "warning",
                    "code": "required_depth",
                    "message": f"{nodes[node]['label']}: a selected topic requires {required[node]}, so the requested {requested} treatment is insufficient.",
                    "nodes": [node],
                }
            )
    taught = set(required) - omitted
    active = [
        e
        for e in edges
        if e["from"] in taught
        and e["to"] in taught
        and ranks[required[e["to"]]] >= ranks[e["target_level"]]
    ]
    group_order = {g: i for i, g in enumerate(plan.get("group_order", []))}
    group_default = {g["id"]: i for i, g in enumerate(project.knowledge["groups"])}

    def key(node):
        group = nodes[node].get("group", "")
        return group_order.get(group, len(group_order) + group_default.get(group, 999)), node

    order = topological(taught, [(e["from"], e["to"]) for e in active], key)
    groups = {g["id"]: g["title"] for g in project.knowledge["groups"]}
    sessions = []
    partitions = _partition(order, nodes, required, plan["sessions"], plan["minutes_per_session"])
    unknown = []
    for number, members in enumerate(partitions, 1):
        minimum, maximum, missing = 0, 0, []
        titles = list(
            dict.fromkeys(groups.get(nodes[i].get("group"), "Foundations") for i in members)
        )
        for node in members:
            estimate = nodes[node].get("estimates", {}).get(required[node])
            if estimate:
                minimum += estimate["min"]
                maximum += estimate["max"]
            else:
                missing.append(node)
        unknown.extend(missing)
        timing = (
            "unestimated"
            if missing
            else (
                "overloaded"
                if minimum > plan["minutes_per_session"]
                else "tight"
                if maximum > plan["minutes_per_session"]
                else "within_estimate"
            )
        )
        sessions.append(
            {
                "number": number,
                "title": " / ".join(titles[:2]),
                "nodes": members,
                "minutes": {"min": minimum, "max": maximum, "unestimated": missing},
                "timing": timing,
            }
        )
        if timing in {"overloaded", "tight"}:
            issues.append(
                {
                    "severity": "warning",
                    "code": timing,
                    "message": f"Session {number}: estimated {minimum:g}–{maximum:g} minutes for a {plan['minutes_per_session']}-minute slot.",
                    "nodes": members,
                }
            )
    if unknown:
        issues.append(
            {
                "severity": "warning",
                "code": "missing_estimates",
                "message": f"{len(unknown)} concept treatments need time estimates. Session balance is provisional.",
                "nodes": unknown,
            }
        )
    source_ids = {ref["source"] for n in taught for ref in nodes[n]["evidence"]}
    return {
        "schema_version": 1,
        "project_id": project.config["id"],
        "project_title": project.config["title"],
        "project_digest": project.content_digest,
        "plan_digest": digest(plan),
        "plan": deepcopy(plan),
        "order": order,
        "levels": {n: required[n] for n in order},
        "roles": {n: "target" if n in targets else "supporting" for n in order},
        "required_by": {n: sorted(required_by[n]) for n in sorted(required_by)},
        "background": {
            n: {"required": level, "assumed": background[n], "origin": background_origin[n]}
            for n, level in sorted(assumed_used.items())
        },
        "edges": active,
        "sessions": sessions,
        "issues": issues,
        "layout": layout(order, [(e["from"], e["to"]) for e in active]),
        "stats": {
            "targets": len(taught & targets.keys()),
            "supporting": len(taught - targets.keys()),
            "assumed": len(assumed_used),
            "concepts": len(order),
            "sessions": len(sessions),
            "unused_sessions": plan["sessions"] - len(sessions),
            "estimated_min": sum(s["minutes"]["min"] for s in sessions),
            "estimated_max": sum(s["minutes"]["max"] for s in sessions),
            "unestimated": len(unknown),
            "sources": len(source_ids),
        },
    }


def compare_plans(first: dict, second: dict) -> dict:
    a, b = set(first["order"]), set(second["order"])
    return {
        "first": first["plan"]["id"],
        "second": second["plan"]["id"],
        "shared": sorted(a & b),
        "only_first": sorted(a - b),
        "only_second": sorted(b - a),
        "jaccard": len(a & b) / len(a | b) if a | b else None,
        "depth_changes": {
            n: [first["levels"][n], second["levels"][n]]
            for n in sorted(a & b)
            if first["levels"][n] != second["levels"][n]
        },
    }
