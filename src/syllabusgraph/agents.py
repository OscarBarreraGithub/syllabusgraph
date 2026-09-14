"""Host-agent dispatch, mandatory independent critique, and local audit records.

The trusted orchestrator supplies runtime identity. These records enforce the
workflow contract; they are not cryptographic proof of a provider's model.
"""

from copy import deepcopy
from dataclasses import replace
import re
from uuid import uuid4

from .io import ProjectError, bundled, digest, write_json
from .project import load_project, validate_shape
from . import workflow as wf

KINDS = ("nodes", "edges", "groups", "motivations")


def defaults(provider="codex"):
    if provider not in {"codex", "claude"}:
        raise ProjectError("Choose provider codex or claude.")
    extractor, critic = (
        ("gpt-5.6-terra", "gpt-5.6-sol") if provider == "codex" else ("sonnet", "opus")
    )
    return {
        "schema_version": 1,
        "provider": provider,
        "orchestrator": {"model": "inherit", "effort": "inherit"},
        "extractor": {"model": extractor, "effort": "high"},
        "critic": {"model": critic, "effort": "high"},
        "audit_mode": "end",
        "revision_limit": 2,
    }


def policy(project, *, required=True):
    path = project.local / "agent-policy.json"
    if not path.exists():
        if required:
            raise ProjectError("Accept an agent policy with agent configure before dispatching.")
        return {"accepted": False, "defaults": {p: defaults(p) for p in ("codex", "claude")}}
    value = wf.read_json(path)
    validate_policy(value)
    return value


def validate_policy(value):
    if set(value) != set(defaults()) or value["schema_version"] != 1:
        raise ProjectError("Invalid agent policy fields/version.")
    defaults(value["provider"])
    for role in ("orchestrator", "extractor", "critic"):
        row = value[role]
        if not isinstance(row, dict) or set(row) != {"model", "effort"}:
            raise ProjectError("Each agent role needs a model and effort.")
        if not isinstance(row["model"], str) or not row["model"].strip():
            raise ProjectError("Agent models must be explicit nonempty names.")
        efforts = {"low", "medium", "high", "xhigh", "max", "ultra"}
        if role == "orchestrator":
            efforts.add("inherit")
        elif row["model"] == "inherit":
            raise ProjectError("Extraction and critique need explicit models.")
        if row["effort"] not in efforts:
            raise ProjectError("Unsupported reasoning effort in agent policy.")
    if value["audit_mode"] not in {"end", "trust"}:
        raise ProjectError("Audit mode must be end or trust.")
    if type(value["revision_limit"]) is not int or not 0 <= value["revision_limit"] <= 10:
        raise ProjectError("Revision limit must be an integer from 0 to 10.")


def configure(project, provider="codex", **overrides):
    value = defaults(provider)
    for key, setting in overrides.items():
        if setting is None:
            continue
        if key in {"audit_mode", "revision_limit"}:
            value[key] = setting
        else:
            role, field = key.rsplit("_", 1)
            value[role][field] = setting
    validate_policy(value)
    with wf.project_lock(project):
        write_json(project.local / "agent-policy.json", value)
        write_json(project.local / "policies" / (digest(value)[7:] + ".json"), value)
    return value


def _identity(text):
    return isinstance(text, str) and bool(text.strip()) and len(text) <= 200


def dispatch(
    project, unit, *, stage, orchestrator, orchestrator_model=None, orchestrator_effort=None
):
    if stage not in {"extract", "critique", "adjudicate"} or not _identity(orchestrator):
        raise ProjectError("Dispatch needs a stage and orchestrator session identity.")
    with wf.project_lock(project):
        project = load_project(project.root)
        config = policy(project)
        for field, actual in (("model", orchestrator_model), ("effort", orchestrator_effort)):
            if (
                config["orchestrator"][field] != "inherit"
                and actual != config["orchestrator"][field]
            ):
                raise ProjectError(
                    f"Configured orchestrator {field} must match the actual session; supply --orchestrator-{field}."
                )
        directory = wf.unit_dir(project, unit)
        state = wf.read_json(directory / "state.json")
        if state["status"] == "merged":
            raise ProjectError("Merged units are immutable; prepare an amendment unit.")
        active = state.get("active_dispatch")
        if active:
            active_path = directory / "dispatches" / active
            active_ticket = wf.read_json(active_path / "ticket.json")
            if (
                active_ticket["stage"] != stage
                and not (active_path / "done.json").exists()
                and not any((active_path / "failures").glob("*.json"))
            ):
                raise ProjectError(
                    "Finish or record failure of the active dispatch before changing stages."
                )
        if stage == "critique" and (directory / "critique.json").exists():
            previous = wf.read_json(directory / "critique.json")
            if previous.get("verdict") in {"revise", "reject"} and previous.get(
                "producer_dispatch"
            ) == state.get("producer_dispatch"):
                raise ProjectError(
                    "Resolve adverse critic findings through extraction or adjudication before another critique."
                )
        if stage == "extract":
            findings = [
                wf.read_json(p)["value"]
                for p in (directory / "dispatches").glob("*/result.json")
                if wf.read_json(p.parent / "ticket.json")["stage"] == "critique"
            ]
            adverse = [
                v
                for v in findings
                if isinstance(v, dict) and v.get("verdict") in {"revise", "reject"}
            ]
            if adverse and (
                len(adverse) >= config["revision_limit"]
                or any(v["verdict"] == "reject" for v in adverse)
            ):
                raise ProjectError(
                    "Revision limit reached or critic rejected; dispatch the adjudicator to decide and document the outcome."
                )
        packet = wf._ensure_packet(project, directory)
        role = "extractor" if stage == "extract" else "critic"
        request = deepcopy(packet)
        request.update({"stage": stage, "current_knowledge": project.knowledge})
        proposal_digest = None
        if (directory / "proposal.json").exists():
            request["proposal"] = wf.read_json(directory / "proposal.json")
            proposal_digest = digest(request["proposal"])
            request["proposal_digest"] = proposal_digest
            request["checks"] = wf.check(project, unit)
        elif stage != "extract":
            raise ProjectError("Extraction must produce a proposal before review.")
        if stage == "adjudicate":
            critique = wf.read_json(directory / "critique.json")
            critic_ticket, finding = _completion(
                project,
                directory,
                critique.get("provenance", {}),
                stage="critique",
                historical=True,
            )
            if finding.get("proposal_digest") != proposal_digest or finding.get("verdict") not in {
                "revise",
                "reject",
            }:
                raise ProjectError(
                    "Adjudication requires current critic findings requesting revision or rejection."
                )
            if (
                critic_ticket["producer_dispatch"] != state.get("producer_dispatch")
                or state.get("dispatches", {}).get("critique") != critic_ticket["id"]
            ):
                raise ProjectError("The current producer needs a fresh critic before adjudication.")
        for name in ("critique", "adjudication"):
            if (directory / f"{name}.json").exists():
                request["previous_" + name] = wf.read_json(directory / f"{name}.json")
        if stage != "extract":
            request["instructions"] = (bundled("workflows") / "review.md").read_text()
            request["proposal_schema"] = request.pop("response_schema")
            request["response_contract"] = (
                {
                    "proposal_digest": proposal_digest,
                    "verdict": "accept|revise|reject",
                    "notes": ["substantive source assessment"],
                }
                if stage == "critique"
                else {
                    "proposal": "full revised proposal matching proposal_schema",
                    "decisions": [
                        {
                            "issue": "dispute",
                            "finding": 0,
                            "alternatives": ["option one", "option two"],
                            "resolution": "selected option or deferral",
                            "rationale": "why",
                            "evidence": [
                                {"source": "source-id", "section": "section", "pages": [1]}
                            ],
                            "affected_records": [{"kind": "nodes", "id": "concept-id"}],
                        }
                    ],
                }
            )
        ticket = {
            "id": uuid4().hex,
            "unit": unit,
            "stage": stage,
            "orchestrator": orchestrator,
            "orchestrator_model": orchestrator_model or "inherit",
            "orchestrator_effort": orchestrator_effort or "inherit",
            "role": role,
            **config[role],
            "provider": config["provider"],
            "policy_digest": digest(config),
            "packet_digest": packet["packet_digest"],
            "knowledge_digest": digest(project.knowledge),
            "proposal_digest": proposal_digest,
            "producer_dispatch": state.get("producer_dispatch"),
            "at": wf.timestamp(),
        }
        request["dispatch"] = ticket
        path = directory / "dispatches" / ticket["id"]
        write_json(path / "request.json", request)
        ticket["request_digest"] = digest(request)
        write_json(path / "ticket.json", ticket)
        state = wf.read_json(directory / "state.json")
        state.setdefault("dispatches", {})[stage] = ticket["id"]
        state["active_dispatch"] = ticket["id"]
        write_json(directory / "state.json", state)
    return {
        **ticket,
        "request": str(path / "request.json"),
        "next": "Orchestrator: launch a separate agent with this model and effort, then record its result with agent complete.",
    }


def _ticket(project, directory, dispatch_id, *, current_policy=True, check_packet=True):
    if not re.fullmatch(r"[a-f0-9]{32}", dispatch_id):
        raise ProjectError("Invalid dispatch ID.")
    path = directory / "dispatches" / dispatch_id
    ticket = wf.read_json(path / "ticket.json")
    request = wf.read_json(path / "request.json")
    if digest(request) != ticket.get("request_digest") or request["dispatch"] != {
        k: v for k, v in ticket.items() if k != "request_digest"
    }:
        raise ProjectError("Dispatch request changed after issuance.")
    if current_policy and ticket["policy_digest"] != digest(policy(project)):
        raise ProjectError("Agent policy changed; issue a new dispatch.")
    if (
        check_packet
        and ticket["packet_digest"] != wf._ensure_packet(project, directory)["packet_digest"]
    ):
        raise ProjectError("Dispatch packet changed.")
    return path, ticket, request


def _completion(project, directory, record, *, stage, historical=False):
    path, ticket, _ = _ticket(
        project,
        directory,
        record.get("dispatch_id", ""),
        current_policy=not (historical or stage == "extract"),
    )
    result = wf.read_json(path / "result.json")
    if ticket["stage"] != stage or result.get("provenance") != record:
        raise ProjectError("Missing matching orchestrator dispatch provenance.")
    return ticket, result["value"]


def _validate_decisions(value):
    decisions = value.get("decisions")
    if not isinstance(decisions, list) or not decisions:
        raise ProjectError("Adjudication requires a decision ledger.")
    for decision in decisions:
        if not isinstance(decision, dict) or set(decision) != {
            "issue",
            "finding",
            "alternatives",
            "resolution",
            "rationale",
            "evidence",
            "affected_records",
        }:
            raise ProjectError(
                "Each decision needs issue, alternatives, resolution, rationale, evidence, affected_records."
            )
        if type(decision["finding"]) is not int or decision["finding"] < 0:
            raise ProjectError("Decision finding must index a critic note (zero-based).")
        if (
            any(not _identity(decision[key]) for key in ("issue", "resolution"))
            or not isinstance(decision["rationale"], str)
            or not decision["rationale"].strip()
        ):
            raise ProjectError("Decision rationale and resolution must be substantive.")
        options = decision["alternatives"]
        if (
            not isinstance(options, list)
            or len(options) < 2
            or not all(isinstance(x, str) and x.strip() for x in options)
            or len(set(options)) != len(options)
        ):
            raise ProjectError("Record at least two alternatives per decision.")
        if not isinstance(decision["evidence"], list) or not decision["evidence"]:
            raise ProjectError("Each decision needs source evidence.")
        for evidence in decision["evidence"]:
            validate_shape(evidence, "evidence")
        if not isinstance(decision["affected_records"], list):
            raise ProjectError("Affected records must be a list.")
        for row in decision["affected_records"]:
            if (
                not isinstance(row, dict)
                or set(row) != {"kind", "id"}
                or row["kind"] not in KINDS
                or not _identity(row["id"])
            ):
                raise ProjectError("Invalid affected record in decision.")


def complete(project, unit, dispatch_id, value, *, agent_id, model, effort):
    if not isinstance(value, dict):
        raise ProjectError("An agent must return one JSON object.")
    directory = wf.unit_dir(project, unit)
    # Validate and persist the immutable runtime response under the project lock.
    with wf.project_lock(project):
        project = load_project(project.root)
        path, ticket, request = _ticket(project, directory, dispatch_id)
        if not _identity(agent_id) or agent_id == ticket["orchestrator"]:
            raise ProjectError(
                "A separate worker identity is required; the orchestrator cannot self-review."
            )
        if (model, effort) != (ticket["model"], ticket["effort"]):
            _record_failure(
                directory, dispatch_id, "Actual runtime model/effort did not match the dispatch."
            )
            raise ProjectError(
                "Actual model/effort differs from dispatch; explicitly reconfigure, never silently substitute."
            )
        provenance = {
            "dispatch_id": dispatch_id,
            "agent_id": agent_id,
            "model": model,
            "effort": effort,
        }
        result = {"provenance": provenance, "value": value}
        if (path / "result.json").exists():
            if wf.read_json(path / "result.json") != result:
                raise ProjectError("Completed dispatches are immutable; issue a new dispatch.")
            if (path / "done.json").exists():
                return wf.read_json(path / "done.json")
        if wf.read_json(directory / "state.json")["status"] == "merged":
            raise ProjectError("Merged units are immutable.")
        if (
            wf.read_json(directory / "state.json").get("dispatches", {}).get(ticket["stage"])
            != dispatch_id
        ):
            raise ProjectError(
                "Dispatch was superseded; only the latest dispatch of this stage may complete."
            )
        if ticket["knowledge_digest"] != digest(project.knowledge):
            raise ProjectError(
                "Knowledge changed during dispatch; review the current base with a new dispatch."
            )
        if wf.read_json(directory / "state.json").get("active_dispatch") != dispatch_id:
            raise ProjectError("Dispatch was superseded by a later workflow stage.")
        current_path = directory / "proposal.json"
        current = wf.read_json(current_path) if current_path.exists() else None
        # Idempotent completion can recover after importing its own response.
        incoming = value if ticket["stage"] == "extract" else value.get("proposal")
        if (digest(current) if current else None) != ticket[
            "proposal_digest"
        ] and current != incoming:
            raise ProjectError("Proposal changed during dispatch; issue a new dispatch.")
        if ticket["stage"] in {"extract", "adjudicate"}:
            validate_shape(incoming, "proposal")
            if (
                incoming["packet_digest"] != ticket["packet_digest"]
                or len(incoming["graph"]["nodes"]) > request["node_budget"]
            ):
                raise ProjectError("Response exceeds its packet or concept contract.")
        if ticket["stage"] != "extract":
            extraction = wf.read_json(directory / "extraction.json")
            _, extracted = _completion(project, directory, extraction, stage="extract")
            if agent_id == extraction["agent_id"]:
                raise ProjectError("The extractor cannot act as its own critic/adjudicator.")
            if ticket["stage"] == "critique":
                adjudication_path = directory / "adjudication.json"
                if adjudication_path.exists():
                    adjudication = wf.read_json(adjudication_path)
                    if (
                        adjudication["proposal_digest"] == ticket["proposal_digest"]
                        and agent_id == adjudication["provenance"]["agent_id"]
                    ):
                        raise ProjectError("The adjudicator requires a fresh independent critic.")
                if not isinstance(value, dict) or value.get("verdict") not in {
                    "accept",
                    "revise",
                    "reject",
                }:
                    raise ProjectError("Critic needs accept, revise, or reject verdict.")
                if value.get("proposal_digest") != ticket["proposal_digest"]:
                    raise ProjectError("Critic reviewed a different proposal revision.")
                if (
                    not isinstance(value.get("notes"), list)
                    or not value["notes"]
                    or not all(isinstance(n, str) and n.strip() for n in value["notes"])
                ):
                    raise ProjectError("Critic needs substantive notes.")
            else:
                _validate_decisions(value)
                findings = request["previous_critique"]
                if {d["finding"] for d in value["decisions"]} != set(
                    range(len(findings["notes"]))
                ) or len(value["decisions"]) != len(findings["notes"]):
                    raise ProjectError("Every critic finding must have a documented resolution.")
                affected = {
                    (r["kind"], r["id"]) for d in value["decisions"] for r in d["affected_records"]
                }
                for kind in KINDS:
                    before = {r["id"]: r for r in request["proposal"]["graph"][kind]}
                    after = {r["id"]: r for r in incoming["graph"][kind]}
                    if any(
                        before.get(i) != after.get(i) and (kind, i) not in affected
                        for i in before.keys() | after.keys()
                    ):
                        raise ProjectError(
                            "Every adjudicated change needs an affected-record decision."
                        )
                    old = {r["id"]: r for r in project.knowledge[kind]}
                    for row in incoming["graph"][kind]:
                        if (
                            row["id"] in old
                            and row != old[row["id"]]
                            and (kind, row["id"]) not in affected
                        ):
                            raise ProjectError(
                                "Every overridden record needs a documented decision."
                            )
                # Verify all decision citations have an actual packet/registered page witness.
                witnessed = {(w["source"], w["page"]) for w in incoming["quote_checks"]}
                if any(
                    (e["source"], p) not in witnessed
                    for d in value["decisions"]
                    for e in d["evidence"]
                    for p in e["pages"]
                ):
                    raise ProjectError(
                        "Decision evidence needs quote witnesses in the revised proposal."
                    )
        write_json(path / "result.json", result)
        if ticket["stage"] == "extract":
            wf.import_proposal(project, unit, value, runner=provenance, _locked=True)
            write_json(directory / "extraction.json", provenance)
        elif ticket["stage"] == "adjudicate":
            wf.import_proposal(project, unit, incoming, runner=provenance, _locked=True)
            write_json(
                directory / "adjudication.json",
                {
                    "provenance": provenance,
                    "proposal_digest": digest(incoming),
                    "knowledge_digest": ticket["knowledge_digest"],
                    "decisions": value["decisions"],
                },
            )
        else:
            write_json(
                directory / "critique.json",
                {
                    **value,
                    "provenance": provenance,
                    "knowledge_digest": ticket["knowledge_digest"],
                    "producer_dispatch": ticket["producer_dispatch"],
                    "at": wf.timestamp(),
                },
            )
            if value["verdict"] != "accept":
                state = wf.read_json(directory / "state.json")
                state["status"] = value["verdict"]
                write_json(directory / "state.json", state)
        (directory / "last_failure.json").unlink(missing_ok=True)
        if ticket["stage"] in {"extract", "adjudicate"}:
            state = wf.read_json(directory / "state.json")
            state["producer_dispatch"] = dispatch_id
            write_json(directory / "state.json", state)
    if ticket["stage"] == "critique" and value["verdict"] == "accept":
        try:
            wf.review(project, unit, decision="accept", reviewer=agent_id, notes=value["notes"])
        except ProjectError:
            _record_failure(
                directory,
                dispatch_id,
                "Critic response recorded, but workflow acceptance failed; inspect current checks and provenance.",
            )
            raise
    summary = {"unit": unit, "stage": ticket["stage"], "dispatch_id": dispatch_id, "recorded": True}
    write_json(path / "done.json", summary)
    return summary


def _record_failure(directory, dispatch_id, reason):
    record = {"dispatch_id": dispatch_id, "reason": reason, "at": wf.timestamp()}
    write_json(
        directory / "dispatches" / dispatch_id / "failures" / (uuid4().hex + ".json"), record
    )
    write_json(directory / "last_failure.json", record)
    return record


def fail(project, unit, dispatch_id, *, reason):
    if not isinstance(reason, str) or not reason.strip():
        raise ProjectError("Record a substantive native dispatch failure reason.")
    with wf.project_lock(project):
        directory = wf.unit_dir(project, unit)
        path, _, _ = _ticket(
            project, directory, dispatch_id, current_policy=False, check_packet=False
        )
        if wf.read_json(directory / "state.json")["status"] == "merged":
            raise ProjectError("Merged units are immutable.")
        if (path / "done.json").exists() or wf.read_json(directory / "state.json").get(
            "active_dispatch"
        ) != dispatch_id:
            raise ProjectError("Only an active unfinished dispatch can fail.")
        return _record_failure(directory, dispatch_id, reason)


def accepted_candidate(project, unit, proposal):
    """Derive recovery's exact expected graph from the base actually reviewed."""
    directory = wf.unit_dir(project, unit)
    critique = wf.read_json(directory / "critique.json")
    _, ticket, request = _ticket(
        project, directory, critique.get("provenance", {}).get("dispatch_id", "")
    )
    base = replace(project, knowledge=request["current_knowledge"])
    if digest(base.knowledge) != ticket["knowledge_digest"]:
        raise ProjectError("Critic base changed.")
    return wf._combine(base, proposal["graph"], replacements=replacements(base, unit, proposal))


def replacements(project, unit, proposal, *, recovering=False):
    directory = wf.unit_dir(project, unit)
    path = directory / "adjudication.json"
    if not path.exists():
        return set()
    record = wf.read_json(path)
    if record["proposal_digest"] != digest(proposal):
        return set()
    try:
        ticket, value = _completion(project, directory, record["provenance"], stage="adjudicate")
    except ProjectError:
        return set()  # Stale authorization grants no replacement; allow new work to repair it.
    if value["proposal"] != proposal or record["decisions"] != value["decisions"]:
        raise ProjectError("Adjudication record changed.")
    if ticket["knowledge_digest"] != digest(project.knowledge) and not recovering:
        raise ProjectError(
            "Knowledge changed since adjudication; adjudicate against the current base."
        )
    return {(r["kind"], r["id"]) for d in value["decisions"] for r in d["affected_records"]}


def require_critic(project, unit, report, *, recovering=False):
    directory = wf.unit_dir(project, unit)
    if not (directory / "critique.json").exists():
        raise ProjectError(
            "A mandatory critic dispatch must accept this proposal before promotion."
        )
    critique = wf.read_json(directory / "critique.json")
    if critique.get("verdict") != "accept":
        raise ProjectError("The current critic requested revisions or rejection.")
    if wf.read_json(directory / "state.json").get("dispatches", {}).get("critique") != critique.get(
        "provenance", {}
    ).get("dispatch_id"):
        raise ProjectError("The latest critic dispatch has not accepted this proposal.")
    state = wf.read_json(directory / "state.json")
    if state.get("active_dispatch") != critique["provenance"]["dispatch_id"]:
        raise ProjectError("A later extraction/adjudication dispatch needs fresh critique.")
    ticket, value = _completion(
        project, directory, critique.get("provenance", {}), stage="critique"
    )
    if ticket["producer_dispatch"] != state.get("producer_dispatch"):
        raise ProjectError("The latest proposal producer needs fresh critique.")
    if any(critique.get(k) != value.get(k) for k in ("proposal_digest", "verdict", "notes")):
        raise ProjectError("Critic record changed.")
    if value["proposal_digest"] != report["proposal_digest"]:
        raise ProjectError("The critic must accept this exact proposal revision.")
    if ticket["knowledge_digest"] != report["current_knowledge_digest"] and not recovering:
        raise ProjectError("Knowledge changed since acceptance; dispatch a new critic.")
    extraction = wf.read_json(directory / "extraction.json")
    _, original = _completion(project, directory, extraction, stage="extract")
    proposal = wf.read_json(directory / "proposal.json")
    if original != proposal:
        adjudication = wf.read_json(directory / "adjudication.json")
        _, revised = _completion(project, directory, adjudication["provenance"], stage="adjudicate")
        if revised["proposal"] != proposal:
            raise ProjectError("Proposal needs a matching extractor or adjudicator dispatch.")
    if critique["provenance"]["agent_id"] == extraction["agent_id"]:
        raise ProjectError("Independent critic required.")
    if (directory / "adjudication.json").exists():
        adjudication = wf.read_json(directory / "adjudication.json")
        if (
            adjudication["proposal_digest"] == digest(proposal)
            and critique["provenance"]["agent_id"] == adjudication["provenance"]["agent_id"]
        ):
            raise ProjectError("The adjudicator requires a fresh independent critic.")
    return critique


def audit(project, *, reviewer=None, notes=None):
    with wf.project_lock(project):
        project = load_project(project.root)
        config = policy(project)
        units = []
        for state in wf.status(project)["units"]:
            directory = wf.unit_dir(project, state["unit"])
            full_state = wf.read_json(directory / "state.json")
            records = {}
            for name in ("extraction", "critique", "adjudication", "receipt"):
                if (directory / f"{name}.json").exists():
                    records[name] = wf.read_json(directory / f"{name}.json")
            # Include all adjudications, including decisions superseded by later revisions.
            decisions = []
            for path in sorted((directory / "dispatches").glob("*/result.json")):
                result = wf.read_json(path)
                if "decisions" in result["value"]:
                    decisions.append(
                        {
                            "provenance": result["provenance"],
                            "decisions": result["value"]["decisions"],
                            "at": wf.read_json(path.parent / "ticket.json")["at"],
                        }
                    )
            dispatches = []
            for path in sorted((directory / "dispatches").glob("*/ticket.json")):
                ticket = wf.read_json(path)
                result_path = path.parent / "result.json"
                result = wf.read_json(result_path) if result_path.exists() else {}
                dispatches.append(
                    {
                        **ticket,
                        "active": ticket["id"] == full_state.get("active_dispatch"),
                        "completed": (path.parent / "done.json").exists(),
                        "provenance": result.get("provenance"),
                        "verdict": result.get("value", {}).get("verdict"),
                        "notes": result.get("value", {}).get("notes"),
                        "failures": [
                            wf.read_json(p)
                            for p in sorted((path.parent / "failures").glob("*.json"))
                        ],
                    }
                )
            dispatches.sort(key=lambda r: r["at"])
            decisions.sort(key=lambda r: r["at"])
            units.append(
                {**state, **records, "decision_history": decisions, "dispatch_history": dispatches}
            )
        snapshot = {"project_digest": project.content_digest, "policy": config, "units": units}
        snapshot_digest = digest(snapshot)
        human_dir = project.local / "human-audits" / snapshot_digest[7:]
        if reviewer is not None:
            if not _identity(reviewer) or not isinstance(notes, str) or not notes.strip():
                raise ProjectError("Human audit needs a reviewer and substantive notes.")
            write_json(
                human_dir / (uuid4().hex + ".json"),
                {
                    "snapshot_digest": snapshot_digest,
                    "reviewer": reviewer,
                    "notes": notes,
                    "at": wf.timestamp(),
                },
            )
        human_audits = sorted(
            (wf.read_json(p) for p in human_dir.glob("*.json")), key=lambda r: r["at"]
        )
        result = {
            **snapshot,
            "snapshot_digest": snapshot_digest,
            "human_audit": human_audits[-1] if human_audits else None,
            "human_audit_history": human_audits,
            "audit_status": "reviewed"
            if human_audits
            else ("trusted-critic" if config["audit_mode"] == "trust" else "pending-human-audit"),
            "unfinished_units": [u["unit"] for u in units if u["status"] != "merged"],
            "scope_note": "Unit coverage is not proof of whole-course completeness. Inspect source coverage and agreed guidance at the final audit.",
        }
        write_json(project.local / "audit.json", result)
    return result
