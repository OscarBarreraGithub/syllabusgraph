"""Portable public artifacts assembled exclusively from reviewed project data."""

from __future__ import annotations

import json

from .project import Project


def reference(project: Project, ref: dict) -> str:
    source = project.sources[ref["source"]]
    metadata = [source["title"]]
    if source.get("volume"):
        metadata.append(f"volume {source['volume']}")
    if source.get("edition"):
        metadata.append(source["edition"])
    pages = ", ".join(str(p) for p in ref["pages"])
    return f"{' · '.join(metadata)}, {ref['section']}, p. {pages}"


def markdown(project: Project, result: dict, *, notes: bool = False) -> str:
    plan, nodes = result["plan"], project.nodes
    lines = [
        f"# {plan['title']}",
        "",
        plan.get("description", ""),
        "",
        f"Audience: {plan['audience']}",
        "",
        f"Schedule: {plan['sessions']} sessions × {plan['minutes_per_session']} minutes.",
        "",
        "Timing ranges are author estimates unless their individual basis records an evaluation.",
        "",
        "## Learning outcomes",
        "",
    ]
    for outcome in plan["outcomes"]:
        lines.extend(
            [
                f"- **{nodes[outcome['node']]['label']}** ({outcome['level']}): {outcome['assessment']}"
            ]
        )
    if not plan["outcomes"]:
        lines.append("Learning outcomes have not been defined.")
    if result["issues"]:
        lines.extend(["", "## Planning notes", ""])
        lines.extend(f"- {i['severity'].upper()}: {i['message']}" for i in result["issues"])
    if result["background"]:
        lines.extend(["", "## Assumed background used by this plan", ""])
        for node, value in result["background"].items():
            lines.append(f"- {nodes[node]['label']}: {value['assumed']} (from {value['origin']}).")
    for session in result["sessions"]:
        timing = session["minutes"]
        estimate = f"{timing['min']:g}–{timing['max']:g} minutes"
        if timing["unestimated"]:
            estimate += f" for estimated concepts; {len(timing['unestimated'])} unestimated"
        lines.extend(
            ["", f"## Session {session['number']}: {session['title']}", "", estimate + ".", ""]
        )
        for node_id in session["nodes"]:
            node = nodes[node_id]
            lines.append(
                f"{'###' if notes else '-'} {node['label']} — {result['levels'][node_id]} ({result['roles'][node_id]})"
            )
            if notes:
                lines.extend(["", node["summary"], ""])
                for item in project.knowledge["motivations"]:
                    if node_id in item["nodes"]:
                        lines.extend([f"Teaching motivation: {item['summary']}", ""])
                prerequisites = [e for e in result["edges"] if e["to"] == node_id]
                if prerequisites:
                    lines.append("Prerequisite checks:")
                    lines.extend(
                        f"- {nodes[e['from']]['label']}: {e['failure_mode']}" for e in prerequisites
                    )
                    lines.append("")
                for notation in node.get("notation", []):
                    lines.extend(
                        [
                            f"Notation ({project.sources[notation['source']]['title']}): {notation['note']}",
                            "",
                        ]
                    )
            for ref in node["evidence"]:
                lines.append(f"{'- Reading:' if notes else '  Reading:'} {reference(project, ref)}")
            if notes:
                lines.extend(
                    [
                        "",
                        "Development / worked example:",
                        "",
                        "Instructor preparation to complete.",
                        "",
                    ]
                )
    if result["stats"]["unused_sessions"]:
        lines.extend(["", f"{result['stats']['unused_sessions']} session slots remain unassigned."])
    if plan.get("notes"):
        lines.extend(["", "## Course notes", "", *[f"- {n}" for n in plan["notes"]]])
    lines.extend(
        [
            "",
            "---",
            f"Project content: `{result['project_digest']}`",
            "",
            f"Plan content: `{result['plan_digest']}`",
            "",
        ]
    )
    return "\n".join(lines)


def mermaid(project: Project, result: dict) -> str:
    # Numeric identifiers and escaped labels keep arbitrary subject text out of syntax.
    indexes = {node: f"n{i}" for i, node in enumerate(result["order"])}
    lines = ["flowchart LR"]
    for node in result["order"]:
        label = (
            project.nodes[node]["label"]
            .replace("&", "&amp;")
            .replace('"', "&quot;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", " ")
        )
        lines.append(f'  {indexes[node]}["{label}"]')
    for edge in result["layout"]["edges"]:
        lines.append(f"  {indexes[edge[0]]} --> {indexes[edge[1]]}")
    return "\n".join(lines) + "\n"


def render(project: Project, result: dict, format: str) -> str:
    if format == "json":
        return json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if format == "mermaid":
        return mermaid(project, result)
    return markdown(project, result, notes=format == "notes")
