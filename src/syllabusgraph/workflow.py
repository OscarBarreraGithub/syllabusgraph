"""Resumable proposal, evidence-check, review, and promotion workflow.

Runner commands are supplied explicitly by the operator. Source text and model
output are never evaluated as code. All packets and runs stay in local storage.
"""

from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import unicodedata

from .io import ProjectError, bundled, digest, within, write_json, write_yaml
from .project import SCHEMA, Project, load_project, unique, validate_knowledge, validate_shape
from .sources import source_pages


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def project_lock(project: Project):
    project.local.mkdir(parents=True, exist_ok=True)
    lock = project.local / "write.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ProjectError(
            "Another project write is active. After an interrupted process, inspect and remove .syllabusgraph/write.lock to recover."
        ) from exc
    try:
        os.write(descriptor, str(os.getpid()).encode())
        os.close(descriptor)
        yield
    finally:
        lock.unlink(missing_ok=True)


def unit_dir(project: Project, unit: str) -> Path:
    if not re.fullmatch(r"[a-z][a-z0-9_.-]*", unit):
        raise ProjectError(
            "Work-unit IDs use lowercase letters, numbers, dots, underscores, and hyphens."
        )
    return within(project.local, "runs/" + unit)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ProjectError(f"Missing or invalid workflow file: {path.name}") from exc


def prepare(
    project: Project, unit: str, source: str, first: int, last: int, *, scope: str, budget: int = 15
) -> dict:
    if first < 1 or last < first or last - first >= 80:
        raise ProjectError("Choose an ordered print-page range of 1–80 pages.")
    if budget < 1 or budget > 100:
        raise ProjectError("Concept budget must be between 1 and 100.")
    entry, pages = source_pages(project, source)
    start, end = first + entry["page_offset"], last + entry["page_offset"]
    if start < 1 or end > len(pages):
        raise ProjectError(
            "The requested printed pages map outside this source. Check --page-offset."
        )
    selected = [
        {
            "print_page": p,
            "pdf_page": p + entry["page_offset"],
            "text": pages[p + entry["page_offset"] - 1],
        }
        for p in range(first, last + 1)
    ]
    empty = [p["print_page"] for p in selected if not p["text"].strip()]
    if empty:
        raise ProjectError(
            f"Pages {empty} contain no text. Resolve OCR or adjust the documented scope before preparing."
        )
    packet = {
        "schema_version": 1,
        "unit": unit,
        "source": deepcopy(project.sources[source]),
        "source_sha256": entry["sha256"],
        "scope": scope,
        "node_budget": budget,
        "page_offset": entry["page_offset"],
        "mastery_levels": project.config["mastery_levels"],
        "pages": selected,
        "base_knowledge_digest": digest(project.knowledge),
        "existing_knowledge": project.knowledge,
        "sources": project.config["sources"],
        "instructions": (bundled("workflows") / "extract.md").read_text(encoding="utf-8"),
        "response_schema": {"$ref": "#/$defs/proposal", "$defs": SCHEMA["$defs"]},
    }
    packet["packet_digest"] = digest(packet)
    with project_lock(project):
        directory = unit_dir(project, unit)
        if directory.exists():
            previous = read_json(directory / "packet.json")
            if previous["packet_digest"] == packet["packet_digest"]:
                return previous
            raise ProjectError(
                "Work-unit inputs changed. Use a new unit ID to preserve its review history."
            )
        write_json(directory / "packet.json", packet)
        write_json(directory / "state.json", {"status": "prepared", "prepared_at": timestamp()})
    return packet


def _ensure_packet(project: Project, directory: Path) -> dict:
    packet = read_json(directory / "packet.json")
    stored = packet["packet_digest"]
    if digest({k: v for k, v in packet.items() if k != "packet_digest"}) != stored:
        raise ProjectError("The work packet changed after preparation. Prepare a new unit.")
    source, _ = source_pages(project, packet["source"]["id"])
    if (
        source["sha256"] != packet["source_sha256"]
        or source["page_offset"] != packet["page_offset"]
    ):
        raise ProjectError("The registered source changed after preparation. Prepare a new unit.")
    return packet


def import_proposal(
    project: Project, unit: str, value: dict, *, runner: dict | None = None
) -> dict:
    validate_shape(value, "proposal")
    with project_lock(project):
        directory = unit_dir(project, unit)
        packet = _ensure_packet(project, directory)
        state = read_json(directory / "state.json")
        if state["status"] == "merged":
            raise ProjectError(
                "Merged work units are immutable; create another unit for amendments."
            )
        if value["packet_digest"] != packet["packet_digest"]:
            raise ProjectError("Proposal belongs to a different source packet.")
        if len(value["graph"]["nodes"]) > packet["node_budget"]:
            raise ProjectError("Proposal exceeds the declared concept budget.")
        if (directory / "proposal.json").exists():
            previous = read_json(directory / "proposal.json")
            write_json(
                directory / "revisions" / (digest(previous).split(":")[1] + ".json"), previous
            )
        write_json(directory / "proposal.json", value)
        state.update(
            {
                "status": "proposed",
                "proposal_digest": digest(value),
                "proposed_at": timestamp(),
                "runner": runner or {"kind": "manual"},
            }
        )
        write_json(directory / "state.json", state)
        (directory / "last_failure.json").unlink(missing_ok=True)
    return state


def run(
    project: Project,
    unit: str,
    command: list[str],
    *,
    model: str,
    timeout: float = 180,
    stage: str = "extract",
) -> dict:
    if not command or timeout <= 0:
        raise ProjectError("Supply a runner executable and positive timeout.")
    directory = unit_dir(project, unit)
    packet = _ensure_packet(project, directory)
    request = deepcopy(packet)
    if stage == "critique":
        request["proposal"] = read_json(directory / "proposal.json")
        request["proposal_digest"] = digest(request["proposal"])
        request["checks"] = check(project, unit)
        request["instructions"] = (bundled("workflows") / "review.md").read_text(encoding="utf-8")
    request["stage"] = stage
    try:
        response = subprocess.run(
            command,
            input=json.dumps(request),
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=timeout,
            cwd=project.root,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        write_json(
            directory / "last_failure.json",
            {
                "stage": stage,
                "at": timestamp(),
                "reason": "timeout"
                if isinstance(exc, subprocess.TimeoutExpired)
                else "executable_unavailable",
            },
        )
        raise ProjectError(
            "Runner did not complete. The packet is saved; retry the same unit."
        ) from exc
    if response.returncode != 0:
        write_json(
            directory / "last_failure.json",
            {
                "stage": stage,
                "at": timestamp(),
                "exit_code": response.returncode,
                "stderr": response.stderr[-10000:],
            },
        )
        raise ProjectError(
            "Runner failed. Its diagnostic output is saved in the local run directory."
        )
    if len(response.stdout) > 20_000_000:
        raise ProjectError("Runner response exceeds 20 MB.")
    try:
        value = json.loads(response.stdout)
    except ValueError as exc:
        raise ProjectError(
            "Runner must emit exactly one JSON object, without Markdown fences."
        ) from exc
    if stage == "extract":
        return import_proposal(
            project,
            unit,
            value,
            runner={
                "kind": "command",
                "model": model,
                "executable": Path(command[0]).name,
                "stage": stage,
            },
        )
    if not isinstance(value, dict) or value.get("verdict") not in {"accept", "revise", "reject"}:
        raise ProjectError("Critic output needs a verdict: accept, revise, or reject.")
    if value.get("proposal_digest") != digest(request["proposal"]):
        raise ProjectError("Critic reviewed a different proposal revision.")
    if (
        not isinstance(value.get("notes"), list)
        or not value["notes"]
        or not all(isinstance(note, str) and note.strip() for note in value["notes"])
    ):
        raise ProjectError("Critic output needs substantive review notes.")
    value.update({"model": model, "at": timestamp()})
    write_json(directory / "critique.json", value)
    (directory / "last_failure.json").unlink(missing_ok=True)
    return value


def _combine(project: Project, proposed: dict) -> dict:
    combined = deepcopy(project.knowledge)
    for kind in ("nodes", "edges", "groups", "motivations"):
        unique(proposed[kind], kind)
        existing = {r["id"]: r for r in combined[kind]}
        for row in proposed[kind]:
            if row["id"] in existing:
                if row != existing[row["id"]]:
                    raise ProjectError(
                        f"Conflicting {kind} record {row['id']}; reconcile it explicitly before promotion."
                    )
            else:
                combined[kind].append(row)
                existing[row["id"]] = row
        combined[kind].sort(key=lambda r: r["id"])
    validate_knowledge(project.config, combined)
    return combined


def _normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).split())


def check(project: Project, unit: str) -> dict:
    directory = unit_dir(project, unit)
    packet = _ensure_packet(project, directory)
    proposal = read_json(directory / "proposal.json")
    validate_shape(proposal, "proposal")
    errors, warnings = [], []
    if proposal["packet_digest"] != packet["packet_digest"]:
        errors.append("Proposal packet digest does not match.")
    expected = {p["print_page"] for p in packet["pages"]}
    if set(proposal["pages_read"]) != expected:
        errors.append("Reported page coverage must equal the prepared page range.")
    if len(proposal["graph"]["nodes"]) > packet["node_budget"]:
        errors.append("Concept budget exceeded.")
    if proposal["unresolved"]:
        errors.append(
            "Unresolved extraction questions need a revised proposal or explicit removal of the affected claims."
        )
    try:
        _combine(project, proposal["graph"])
    except ProjectError as exc:
        errors.append(str(exc))
    quotes, supported, loaded_sources = [], set(), {}
    for witness in proposal["quote_checks"]:
        source = witness["source"]
        try:
            if source not in loaded_sources:
                loaded_sources[source] = source_pages(project, source)
            binding, pages = loaded_sources[source]
            physical = witness["page"] + binding["page_offset"]
            if physical < 1 or physical > len(pages):
                raise ProjectError("Citation maps outside the registered source.")
            text, quote = _normalize(pages[physical - 1]), _normalize(witness["quote"])
            # Boundary guards prevent a quoted fragment from silently truncating a word.
            match = bool(quote and re.search(r"(?<!\w)" + re.escape(quote) + r"(?!\w)", text))
            quotes.append({"source": source, "page": witness["page"], "match": match})
            if match:
                supported.add((source, witness["page"]))
            else:
                errors.append(
                    f"Quote not found on {source} p. {witness['page']}; inspect the source and revise."
                )
        except ProjectError as exc:
            errors.append(str(exc))
    for kind in ("nodes", "edges", "motivations"):
        old = {row["id"]: row for row in project.knowledge[kind]}
        for row in proposal["graph"][kind]:
            if old.get(row["id"]) == row:
                continue
            for ref in row["evidence"]:
                for page in ref["pages"]:
                    if (ref["source"], page) not in supported:
                        errors.append(
                            f"{row['id']}: missing verified quote witness for {ref['source']} p. {page}."
                        )
    if digest(project.knowledge) != packet["base_knowledge_digest"]:
        warnings.append(
            "The knowledge base changed since extraction. Review the merged candidate against its current contents."
        )
    report = {
        "ok": not errors,
        "errors": sorted(set(errors)),
        "warnings": warnings,
        "quote_checks": quotes,
        "packet_digest": packet["packet_digest"],
        "proposal_digest": digest(proposal),
        "current_knowledge_digest": digest(project.knowledge),
        "scope": "Checks confirm structure, declared coverage, and quote location. A reviewer must assess whether evidence supports each claim.",
    }
    write_json(directory / "checks.json", report)
    return report


def review(project: Project, unit: str, *, decision: str, reviewer: str, notes: list[str]) -> dict:
    if (
        decision not in {"accept", "revise", "reject"}
        or not reviewer.strip()
        or not notes
        or not all(isinstance(note, str) and note.strip() for note in notes)
    ):
        raise ProjectError(
            "Review needs a decision, reviewer identity, and at least one substantive note."
        )
    with project_lock(project):
        directory = unit_dir(project, unit)
        if read_json(directory / "state.json")["status"] == "merged":
            raise ProjectError("Merged units cannot be re-reviewed in place.")
        report = check(project, unit)
        if decision == "accept" and not report["ok"]:
            raise ProjectError("Resolve the source-check failures before accepting this proposal.")
        critique_path = directory / "critique.json"
        if decision == "accept" and critique_path.exists():
            critique = read_json(critique_path)
            if (
                critique.get("proposal_digest") == report["proposal_digest"]
                and critique["verdict"] != "accept"
            ):
                raise ProjectError(
                    "The current critic requested revisions or rejection. Resolve its findings and re-run critique before accepting."
                )
        record = {
            "decision": decision,
            "reviewer": reviewer,
            "notes": notes,
            "at": timestamp(),
            "proposal_digest": report["proposal_digest"],
            "knowledge_digest": report["current_knowledge_digest"],
            "packet_digest": report["packet_digest"],
        }
        write_json(directory / "review.json", record)
        state = read_json(directory / "state.json")
        state["status"] = "reviewed" if decision == "accept" else decision
        write_json(directory / "state.json", state)
    return record


def promote(project: Project, unit: str) -> dict:
    with project_lock(project):
        project = load_project(project.root)
        directory = unit_dir(project, unit)
        state = read_json(directory / "state.json")
        proposal = read_json(directory / "proposal.json")
        record = read_json(directory / "review.json")
        if record["decision"] != "accept" or record["proposal_digest"] != digest(proposal):
            raise ProjectError("Promotion requires acceptance of this exact proposal revision.")
        if state["status"] == "merged":
            return read_json(directory / "receipt.json")
        report = check(project, unit)
        if not report["ok"]:
            raise ProjectError("Source checks no longer pass; review again before promotion.")
        combined = _combine(project, proposal["graph"])
        expected = digest(combined)
        current = digest(project.knowledge)
        if record["knowledge_digest"] != current and expected != current:
            raise ProjectError(
                "The knowledge base changed since acceptance. Review against the current base before promotion."
            )
        # Recovery: a crash after the atomic graph write can safely finish its receipt.
        write_yaml(within(project.root, project.config["knowledge"]), combined)
        receipt = {
            "unit": unit,
            "proposal_digest": digest(proposal),
            "knowledge_digest": expected,
            "source_sha256": read_json(directory / "packet.json")["source_sha256"],
            "reviewer": record["reviewer"],
            "merged_at": timestamp(),
        }
        write_json(directory / "receipt.json", receipt)
        state["status"] = "merged"
        write_json(directory / "state.json", state)
    return receipt


def status(project: Project) -> dict:
    units = []
    directory = project.local / "runs"
    if directory.exists():
        for path in sorted(directory.iterdir()):
            if path.is_dir() and (path / "state.json").is_file():
                state = read_json(path / "state.json")
                units.append(
                    {
                        "unit": path.name,
                        "status": state["status"],
                        "retryable_failure": (path / "last_failure.json").exists(),
                    }
                )
    return {
        "project": project.config["id"],
        "units": units,
        "next": "Register a source and prepare a page range."
        if not units
        else "Inspect each unit; retries preserve its packet and prior proposal revisions.",
    }
