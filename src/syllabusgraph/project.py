"""Project loading and cross-file semantic validation."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from .io import ProjectError, digest, read_yaml, within

SCHEMA = json.loads(
    (Path(__file__).parent / "schemas" / "project.schema.json").read_text(encoding="utf-8")
)


def validate_shape(value: dict, kind: str) -> None:
    schema = {"$ref": f"#/$defs/{kind}", "$defs": SCHEMA["$defs"]}
    problems = sorted(
        Draft202012Validator(schema).iter_errors(value), key=lambda e: str(list(e.path))
    )
    if problems:
        detail = "; ".join(
            f"{'.'.join(map(str, p.path)) or kind}: {p.message}" for p in problems[:8]
        )
        raise ProjectError(detail)


def unique(rows: list[dict], kind: str) -> dict[str, dict]:
    result = {}
    for row in rows:
        if row["id"] in result:
            raise ProjectError(f"Duplicate {kind} id: {row['id']}")
        result[row["id"]] = row
    return result


@dataclass
class Project:
    root: Path
    config: dict
    knowledge: dict
    plans: dict[str, dict]
    plan_paths: dict[str, Path]

    @property
    def levels(self) -> dict[str, int]:
        return {name: rank for rank, name in enumerate(self.config["mastery_levels"])}

    @property
    def nodes(self) -> dict[str, dict]:
        return {n["id"]: n for n in self.knowledge["nodes"]}

    @property
    def sources(self) -> dict[str, dict]:
        return {s["id"]: s for s in self.config["sources"]}

    @property
    def content_digest(self) -> str:
        return digest({"config": self.config, "knowledge": self.knowledge, "plans": self.plans})

    @property
    def local(self) -> Path:
        return within(self.root, ".syllabusgraph")

    def with_plan(self, plan: dict) -> Project:
        validate_plan(self, plan)
        plans = deepcopy(self.plans)
        plans[plan["id"]] = plan
        result = Project(self.root, self.config, self.knowledge, plans, self.plan_paths)
        validate_prior_plans(result)
        return result


def validate_knowledge(config: dict, graph: dict) -> None:
    from .graph import topological

    validate_shape(graph, "knowledge")
    nodes = unique(graph["nodes"], "concept")
    unique(graph["edges"], "relationship")
    groups = unique(graph.get("groups", []), "group")
    unique(graph.get("motivations", []), "motivation")
    sources = {s["id"] for s in config["sources"]}
    levels = set(config["mastery_levels"])

    def refs(items):
        for ref in items:
            if ref["source"] not in sources:
                raise ProjectError(f"Unknown evidence source: {ref['source']}")

    for node in nodes.values():
        refs(node["evidence"])
        for notation in node.get("notation", []):
            if notation["source"] not in sources:
                raise ProjectError(f"Unknown notation source on {node['id']}: {notation['source']}")
        if node.get("group") and node["group"] not in groups:
            raise ProjectError(f"Unknown group on {node['id']}: {node['group']}")
        for level, estimate in node.get("estimates", {}).items():
            if level not in levels:
                raise ProjectError(f"Unknown estimate mastery level: {level}")
            if estimate["min"] > estimate["max"]:
                raise ProjectError(f"Reversed time estimate on {node['id']} / {level}")
    ordering = []
    for edge in graph["edges"]:
        if edge["from"] not in nodes or edge["to"] not in nodes:
            raise ProjectError(f"Relationship {edge['id']} names an unknown concept.")
        if edge["from"] == edge["to"]:
            raise ProjectError(f"Self relationship: {edge['id']}")
        if {edge["source_level"], edge["target_level"]} - levels:
            raise ProjectError(f"Unknown mastery level on {edge['id']}")
        refs(edge["evidence"])
        if edge["relation"] == "prerequisite":
            ordering.append((edge["from"], edge["to"]))
    topological(nodes, ordering)
    for item in graph.get("motivations", []):
        if set(item["nodes"]) - nodes.keys():
            raise ProjectError(f"Unknown concept in motivation {item['id']}")
        refs(item["evidence"])


def validate_plan(project: Project, plan: dict) -> None:
    validate_shape(plan, "plan")
    ids = set(project.nodes)
    outcomes = [o["node"] for o in plan["outcomes"]]
    if len(outcomes) != len(set(outcomes)):
        raise ProjectError("Each outcome concept must occur once per course plan.")
    choices = [(o["node"], o["level"]) for o in plan["outcomes"]]
    for field in ("background", "include", "treatments"):
        choices.extend(plan.get(field, {}).items())
    for node, level in choices:
        if node not in ids:
            raise ProjectError(f"Unknown concept in plan {plan['id']}: {node}")
        if level not in project.levels:
            raise ProjectError(f"Unknown mastery level in plan {plan['id']}: {level}")
    if set(plan.get("omit", [])) - ids:
        raise ProjectError("Omitted concepts must exist in the knowledge base.")
    if set(plan.get("unknown", [])) - ids:
        raise ProjectError("Unknown-background choices must name existing concepts.")
    groups = {g["id"] for g in project.knowledge.get("groups", [])}
    if set(plan.get("group_order", [])) - groups:
        raise ProjectError("The course narrative names an unknown group.")


def validate_prior_plans(project: Project) -> None:
    from .graph import topological

    edges = []
    for key, plan in project.plans.items():
        for prior in plan.get("prior_plans", []):
            if prior not in project.plans:
                raise ProjectError(f"Unknown prior course in {key}: {prior}")
            edges.append((prior, key))
    topological(project.plans, edges)


def load_project(path: str | Path) -> Project:
    root = Path(path).resolve()
    if root.is_file():
        root = root.parent
    config = read_yaml(root / "project.yaml")
    validate_shape(config, "project")
    unique(config["sources"], "source")
    graph = read_yaml(within(root, config["knowledge"]))
    validate_knowledge(config, graph)
    plans, plan_paths = {}, {}
    for path in sorted(within(root, config["plans_dir"]).glob("*.yaml")):
        within(root, str(path.relative_to(root)))
        plan = read_yaml(path)
        validate_shape(plan, "plan")
        if plan["id"] in plans:
            raise ProjectError(f"Duplicate course plan: {plan['id']}")
        plans[plan["id"]] = plan
        plan_paths[plan["id"]] = path
    project = Project(root, config, graph, plans, plan_paths)
    for plan in plans.values():
        validate_plan(project, plan)
    validate_prior_plans(project)
    return project
