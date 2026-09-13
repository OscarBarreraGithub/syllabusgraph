"""The portable SyllabusGraph command-line interface."""

from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
import shutil
import sys

from . import __version__
from .export import render
from .io import ProjectError, bundled, read_yaml, write_json, write_text, write_yaml
from .planner import build_plan, compare_plans
from .project import load_project, validate_shape
from .server import serve
from . import sources, workflow


def initialize(destination: Path, template: str, *, title: str | None = None):
    if destination.exists() and any(destination.iterdir()):
        raise ProjectError("Choose a new or empty directory for the course project.")
    source = (
        bundled("templates") / "new-course"
        if template == "blank"
        else bundled("examples") / template
    )
    shutil.copytree(
        source,
        destination,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".syllabusgraph", "__pycache__"),
    )
    if title:
        config = read_yaml(destination / "project.yaml")
        config["title"] = title
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        config["id"] = slug if slug and slug[0].isalpha() else "course-" + (slug or "new")
        write_yaml(destination / "project.yaml", config)
    write_text(
        destination / ".gitignore", ".syllabusgraph/\n.env\n.env.*\n*.pdf\n*.epub\n__pycache__/\n"
    )
    return load_project(destination)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="syllabusgraph", description="Build source-backed knowledge and design courses."
    )
    root.add_argument("--version", action="version", version=__version__)
    commands = root.add_subparsers(dest="action", required=True)

    def project_command(name, help):
        p = commands.add_parser(name, help=help)
        p.add_argument("--project", "-p", type=Path, default=Path("."))
        return p

    p = commands.add_parser("init", help="Create a new course project.")
    p.add_argument("destination", type=Path)
    p.add_argument("--template", choices=["blank", "sampling", "qft"], default="blank")
    p.add_argument("--title")
    p = commands.add_parser("demo", help="Create or resume the included example and open it.")
    p.add_argument("--destination", type=Path, default=Path("sampling-course"))
    p.add_argument("--port", type=int, default=8766)
    p.add_argument("--no-open", action="store_true")
    project_command("validate", "Validate all project data and course references.")
    p = project_command("build", "Rebuild JSON, syllabi, notes, and diagrams.")
    p.add_argument("--out", type=Path)
    p.add_argument("--strict", action="store_true")
    p = project_command("plan", "Inspect or export a course plan.")
    p.add_argument("--plan", required=True)
    p.add_argument("--format", choices=["json", "syllabus", "notes", "mermaid"], default="json")
    p.add_argument("--out", type=Path)
    p.add_argument("--strict", action="store_true")
    p = project_command("compare", "Compare two course plans over one knowledge base.")
    p.add_argument("first")
    p.add_argument("second")
    p = project_command("serve", "Open the local course-design interface.")
    p.add_argument("--port", type=int, default=8766)
    p.add_argument("--open", action="store_true")
    project_command("status", "Show resumable extraction work units.")
    p = project_command("source", "Register source metadata or attach local material.")
    subs = p.add_subparsers(dest="source_action", required=True)
    sub = subs.add_parser("add")
    sub.add_argument("id")
    sub.add_argument("--title", required=True)
    sub.add_argument("--author", action="append", default=[])
    sub.add_argument("--edition")
    sub = subs.add_parser("register")
    sub.add_argument("id")
    sub.add_argument("file", type=Path)
    sub.add_argument("--page-offset", type=int, default=0, help="PDF page = printed page + offset.")
    sub.add_argument("--replace", action="store_true")
    subs.add_parser("status")
    sub = subs.add_parser("coverage")
    sub.add_argument("id")
    sub.add_argument("--first", type=int, required=True)
    sub.add_argument("--last", type=int, required=True)
    p = project_command("prepare", "Create an immutable source packet for a work unit.")
    p.add_argument("--unit", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--first", type=int, required=True)
    p.add_argument("--last", type=int, required=True)
    p.add_argument("--scope", required=True)
    p.add_argument("--budget", type=int, default=15)
    p = project_command("run", "Run an explicit JSON-in/JSON-out extraction or critic command.")
    p.add_argument("--unit", required=True)
    p.add_argument(
        "--model", required=True, help="Record the model or tool version used by your runner."
    )
    p.add_argument("--stage", choices=["extract", "critique"], default="extract")
    p.add_argument("--timeout", type=float, default=180)
    p.add_argument(
        "runner", nargs=argparse.REMAINDER, help="After --, supply an executable and its arguments."
    )
    p = project_command(
        "import-proposal", "Import a manually prepared or externally extracted proposal."
    )
    p.add_argument("--unit", required=True)
    p.add_argument("file", type=Path)
    for name in ("check", "promote"):
        p = project_command(
            name,
            "Verify a proposal against sources."
            if name == "check"
            else "Promote an accepted proposal.",
        )
        p.add_argument("--unit", required=True)
    p = project_command("review", "Record review of the exact checked proposal revision.")
    p.add_argument("--unit", required=True)
    p.add_argument("--decision", required=True, choices=["accept", "revise", "reject"])
    p.add_argument("--reviewer", required=True)
    p.add_argument("--note", required=True, action="append")
    return root


def _coverage(project, source, first, last):
    if source not in project.sources or first < 1 or last < first:
        raise ProjectError("Choose a registered source and a valid printed-page scope.")
    counts = {}
    for row in workflow.status(project)["units"]:
        if row["status"] != "merged":
            continue
        packet = workflow.read_json(workflow.unit_dir(project, row["unit"]) / "packet.json")
        if packet["source"]["id"] == source:
            for page in packet["pages"]:
                n = page["print_page"]
                counts[n] = counts.get(n, 0) + 1
    missing = sorted(set(range(first, last + 1)) - counts.keys())
    return {
        "source": source,
        "requested_scope": [first, last],
        "missing_pages": missing,
        "overlap_pages": sorted(p for p, n in counts.items() if n > 1 and first <= p <= last),
        "complete": not missing,
        "basis": "Accepted and promoted work-unit coverage within this explicit scope.",
    }


def execute(args) -> int:
    if args.action == "init":
        project = initialize(args.destination, args.template, title=args.title)
        print(f"Created {project.config['title']} in {args.destination}")
        return 0
    if args.action == "demo":
        if not (args.destination / "project.yaml").exists():
            initialize(args.destination, "sampling")
        serve(args.destination, args.port, open_browser=not args.no_open)
        return 0
    project = load_project(args.project)
    result = None
    if args.action == "validate":
        result = {
            "valid": True,
            "project": project.config["id"],
            "concepts": len(project.nodes),
            "relationships": len(project.knowledge["edges"]),
            "plans": list(project.plans),
            "digest": project.content_digest,
        }
    elif args.action == "serve":
        serve(project.root, args.port, open_browser=args.open)
        return 0
    elif args.action in {"build", "plan"}:
        plan_ids = list(project.plans) if args.action == "build" else [args.plan]
        built = {plan_id: build_plan(project, plan_id) for plan_id in plan_ids}
        if args.action == "plan":
            text = render(project, built[args.plan], args.format)
            if args.out:
                write_text(args.out, text)
            else:
                print(text, end="")
        else:
            directory = args.out or project.local / "build"
            for plan_id, value in built.items():
                for format, extension in [
                    ("json", "json"),
                    ("syllabus", "md"),
                    ("notes", "md"),
                    ("mermaid", "mmd"),
                ]:
                    write_text(
                        directory / f"{plan_id}-{format}.{extension}",
                        render(project, value, format),
                    )
            write_json(
                directory / "manifest.json",
                {
                    "schema_version": 1,
                    "project_digest": project.content_digest,
                    "plans": {k: v["plan_digest"] for k, v in built.items()},
                },
            )
            print(f"Built {len(built)} course plans in {directory}")
        return (
            2
            if args.strict
            and any(i["severity"] == "error" for b in built.values() for i in b["issues"])
            else 0
        )
    elif args.action == "compare":
        result = compare_plans(build_plan(project, args.first), build_plan(project, args.second))
    elif args.action == "status":
        result = workflow.status(project)
    elif args.action == "source":
        if args.source_action == "status":
            result = sources.public_status(project)
        elif args.source_action == "coverage":
            result = _coverage(project, args.id, args.first, args.last)
        elif args.source_action == "register":
            with workflow.project_lock(project):
                entry = sources.register(
                    project, args.id, args.file, offset=args.page_offset, replace=args.replace
                )
            result = {
                "source": args.id,
                "sha256": entry["sha256"],
                "pages": entry["page_count"],
                "empty_pages": entry["empty_pages"],
            }
        else:
            source = {
                "id": args.id,
                "title": args.title,
                "authors": args.author,
                "status": "expected",
            }
            if args.edition:
                source["edition"] = args.edition
            validate_shape(source, "source")
            with workflow.project_lock(project):
                current = load_project(project.root)
                if args.id in current.sources:
                    raise ProjectError("That source ID already exists.")
                config = deepcopy(current.config)
                config["sources"].append(source)
                write_yaml(project.root / "project.yaml", config)
            result = {"added": args.id}
    elif args.action == "prepare":
        packet = workflow.prepare(
            project,
            args.unit,
            args.source,
            args.first,
            args.last,
            scope=args.scope,
            budget=args.budget,
        )
        result = {
            "unit": args.unit,
            "packet_digest": packet["packet_digest"],
            "packet": str(workflow.unit_dir(project, args.unit) / "packet.json"),
        }
    elif args.action == "run":
        command = args.runner[1:] if args.runner[:1] == ["--"] else args.runner
        result = workflow.run(
            project, args.unit, command, model=args.model, timeout=args.timeout, stage=args.stage
        )
    elif args.action == "import-proposal":
        result = workflow.import_proposal(project, args.unit, read_yaml(args.file))
    elif args.action == "check":
        result = workflow.check(project, args.unit)
    elif args.action == "review":
        result = workflow.review(
            project, args.unit, decision=args.decision, reviewer=args.reviewer, notes=args.note
        )
    elif args.action == "promote":
        result = workflow.promote(project, args.unit)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 2 if isinstance(result, dict) and result.get("ok") is False else 0


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    try:
        return execute(args)
    except (ProjectError, OSError) as exc:
        print(f"syllabusgraph: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
