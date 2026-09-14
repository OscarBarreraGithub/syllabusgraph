# Native agent setup

SyllabusGraph can coordinate a bounded extraction → critique → adjudication
workflow with native Codex or Claude agents. It does not include a model API
client, credentials, or unattended background runner. The native host runs the
selected agent, while SyllabusGraph prepares immutable JSON requests and records
their completed results.

This is designed for private material: original sources, quotations, packets,
run output, and policy are under the course's ignored `.syllabusgraph/`
directory. They are never part of the public graph or course plan merely because
an agent read them.

## Start from a clone

Clone the repository, read its agent instructions, then ask the native agent to
tell you the next step:

```text
Clone https://github.com/OscarBarreraGithub/syllabusgraph, read the repository
agent instructions, and tell me the next steps for my course project.
```

[Codex reads repository AGENTS.md instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md);
[Claude loads CLAUDE.md](https://code.claude.com/docs/en/memory), which imports
the shared instructions here. After cloning during an existing session, explicitly
read those files instead of assuming they were loaded at session startup.

For a course you already initialized, start from the generated `AGENTS.md` and
`COURSE_GUIDANCE.md`. The guidance describes goals and scope but is private,
human-readable input; it does not override the workflow or grant authority to
extract or publish.

In a new Codex project, trust the project and restart before relying on its
`.codex/agents/` profiles. Custom profiles load at session start and are not
guaranteed to be discovered immediately. If a profile is unavailable or was
added during the current session, use a trusted restart or have the host spawn a
generic native agent with the policy's explicit model and effort and the
immutable request contract.

## Configure the local policy

Prepare and register a small source unit first, then configure a provider in the
course project's directory:

```bash
syllabusgraph agent configure --provider codex --accept-defaults
syllabusgraph agent policy
```

For example, this keeps the default high effort while pinning the orchestrator
to GPT-6 Astra and selecting Luna for extraction:

```bash
syllabusgraph agent configure --provider codex --accept-defaults \
  --orchestrator-model gpt-6-astra --extractor-model gpt-5.6-luna
```

Accepted settings are stored only in `.syllabusgraph/agent-policy.json`. Use
configuration options to select a provider, override extractor, critic, or
orchestrator models and efforts, and choose audit mode. The defaults are:

| Provider | Extractor | Critic and adjudicator | Orchestrator |
|---|---|---|---|
| Codex | `gpt-5.6-terra`, high | `gpt-5.6-sol`, high | current session/inherit; configurable, including GPT-6 Astra |
| Claude | Sonnet, high | Opus, high | current session/inherit |

The committed [Codex custom-agent files](https://learn.chatgpt.com/docs/agent-configuration/subagents)
and [Claude subagent files](https://code.claude.com/docs/en/subagents) implement
those native defaults. The project policy records the requested role settings at
run time. When you override a setting, make the host invoke a matching custom
role or native runtime configuration; a policy file cannot rewrite a named
native agent profile that pins its own model.

The policy asks a runtime for a model. It cannot cryptographically guarantee
which underlying model ran. Check the runtime's agent ID, reported model, and
effort before completing a dispatch. A mismatch or unavailable requested setting
is a failure to record, never a reason to silently substitute another model.
Record a host error or unavailable native runtime with `syllabusgraph agent fail
UNIT DISPATCH_ID --reason TEXT`, then decide how to restore the requested native
configuration. Do not complete that dispatch with a fallback runtime.
When the policy pins an orchestrator model, provide the matching
`--orchestrator-model` on every dispatch; provide `--orchestrator-effort` too
when the policy pins an effort. Neither flag is needed for the inherited default.

## Run the bounded workflow

The orchestrator is the only role that dispatches or advances work. It dispatches
one immutable request at a time; the host runs the real native agent and passes
the JSON result back with its runtime identity. A critic is mandatory after every
extraction. Its recorded `accept` permits the orchestrator to promote once the
current checks pass. There is no required human approval for each unit. The
critic's runtime identity must differ from the extractor's.

If a critic leaves disputes unresolved, the adjudicator returns a full revised
proposal and a decision log that names each issue, at least two alternatives,
chosen resolution, rationale, source/section/page evidence, and every affected
record. Each decision's `finding` is the zero-based index of exactly one
actionable note from the current adverse critic; every adverse note needs one
decision. The revision limit counts adverse completions cumulatively for the
unit: two revisions require adjudication, and a `reject` does so immediately.
The adjudicator makes the final `accept` or `defer` decision. It is not sent to
another critic. Failed final validation defers the unit without promoting it.
Default flow has one correction pass and a six-dispatch total budget including
retries. Budget exhaustion closes the unit as deferred; the orchestrator
continues elsewhere and reports the omission in the audit. Style preferences
and reasonable planning tradeoffs are not grounds for blocking approval. See
[orchestration](../workflows/orchestrate.md),
[extraction](../workflows/extract.md), and [review](../workflows/review.md).
Do not stop for human approval between normal units; seek direction only when
course guidance or required native access is actually missing.

In `end` mode, record a final human check with `syllabusgraph agent audit
--reviewer NAME --notes TEXT`. `trust` mode keeps the critic mandatory but makes
the final human audit optional. `agent audit` shows the stored dispatches,
runtime records, current and archived decisions, acceptance, promotion, and any
end-human audit.

## Manual fallback

You can still author a proposal or run your own explicit adapter, then import it
as a draft with `import-proposal`. Manual imports do not acquire the native
workflow's recorded extraction or critique history and cannot promote until
those dispatches are completed. The existing
[source workflow](source-workflow.md) describes the packet, evidence checks,
and review requirements.
