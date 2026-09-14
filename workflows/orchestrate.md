# Native agent orchestration

Use this workflow for a bounded source unit when a course project's local agent
policy is configured. The policy lives in ignored
`.syllabusgraph/agent-policy.json`; it contains provider, model, effort, and
audit-mode choices. It does not place credentials, sources, or agent results in
tracked project data.

Only the orchestrator may dispatch an agent, accept a completion, advance a
unit, or promote a reviewed proposal. Extractors, critics, and adjudicators have
one immutable work contract at a time and return their required JSON. They do
not spawn further agents or take workflow actions. This avoids a per-unit human
approval loop while preserving a complete audit trail.

## Configure once per course project

From the course project directory, accept the provider defaults or customize the
role models and efforts:

```bash
syllabusgraph agent configure --provider codex --accept-defaults
syllabusgraph agent policy
```

For example, keep the default high effort while requesting GPT-6 Astra for the
orchestrator and Luna for extraction:

```bash
syllabusgraph agent configure --provider codex --accept-defaults \
  --orchestrator-model gpt-6-astra --extractor-model gpt-5.6-luna
```

Codex defaults request `gpt-5.6-terra` at high effort for extraction and
`gpt-5.6-sol` at high effort for critique and adjudication. Claude defaults
request Sonnet at high effort for extraction and Opus at high effort for critique
and adjudication. The orchestrator inherits the current native session by
default; a local policy may explicitly set an orchestrator model, including
GPT-6 Astra. Configuration options can override any role model or effort and
choose `end` or `trust` audit mode.

The policy records the requested runtime contract. If a named native profile
pins a different model or effort, use a matching custom role or host
configuration for the override; the policy file does not rewrite that native
profile.

The configuration requests a model; it cannot cryptographically attest that a
provider used that model. Before accepting a completion, compare the native
runtime's displayed or returned agent ID, model, and effort with the dispatch.
Do not silently fall back to another provider, model, or effort. Record a
failure and stop the dispatch if they differ, cannot be verified, or the native
runtime is unavailable:

```bash
syllabusgraph agent fail chapter-01 DISPATCH_ID --reason "Native runtime unavailable"
```

## Run a unit through the host-native agent

Prepare the bounded packet with `syllabusgraph prepare` first. The orchestrator
then asks SyllabusGraph to create a dispatch, passes the resulting immutable
request JSON to the selected Codex or Claude native agent, and binds its JSON
result to that dispatch:

```bash
syllabusgraph prepare --unit chapter-01 --source reference-one --first 1 --last 10 \
  --scope "Core definitions" --context other-source:10:12
```

The optional `--context` range becomes immutable packet evidence alongside the
primary source. Primary and context pages total at most 80 pages; workers may
not quote or cite material outside those recorded ranges.

```bash
syllabusgraph agent dispatch chapter-01 --stage extract --orchestrator SESSION_ID
syllabusgraph agent complete chapter-01 DISPATCH_ID result.json \
  --agent-id RUNTIME_ID --model MODEL --effort high
```

When the policy pins an orchestrator model, every dispatch must report the
matching runtime with `--orchestrator-model`; include
`--orchestrator-effort` too when the policy pins an effort. For example, an
Astra/high orchestrator uses
`--orchestrator-model gpt-6-astra --orchestrator-effort high`. An inherited
orchestrator needs neither flag.

The application never supplies an API client, provider credential, or automatic
background loop. The host invokes the native agent and passes the result back to
`complete`. A manual `import-proposal` remains a draft: it cannot promote until
the corresponding extraction and critic dispatches are recorded.

Keep plans short and start useful work. Course-plan choices do not require an
agent approval loop. For source units, use the following finite sequence:

1. Extract, then review once. Collect material issues in that review; wording
   and acceptable alternative approaches are nonblocking suggestions.
2. If needed, give the extractor one correction pass and recheck the findings.
3. If disagreement remains, dispatch the configured critic model as adjudicator.
   A `reject` goes directly to adjudication. Sol/high (or Opus/high for Claude)
   makes the final decision and logs the alternatives, evidence, and reasons.
4. Final `accept` authorizes promotion if mechanical checks pass. Final `defer`
   closes the unit without promoting its draft. Failed final validation also
   defers the unit. There is no review after adjudication.

An adjudication contains a full proposal, final `verdict` (`accept` or `defer`),
and one decision for each current finding. Each decision identifies its
zero-based critic-note index and affected records. An accepted revision may
remove unsupported claims while explaining the omission in the ledger. A whole
unit deferral preserves its draft unchanged. Do not manufacture citations to
justify a deferral.

The existing `revision_limit` controls escalation: default 2 means one
correction before the second adverse review goes to adjudication. Total dispatch
budget is `2 * max(1, revision_limit) + 2`, fixed when a unit first dispatches:
six by default, allowing the normal five-call dispute path plus one runtime
retry. Each native worker invocation needs its own dispatch, including a retry
after failure. Re-importing an existing result does not launch a worker. Failed
and superseded dispatches consume that budget. Exhaustion returns
a terminal `deferred` record rather than another request. The host must inspect
that status and move to the next unit.

The orchestrator can also close a blocked unit directly:

```bash
syllabusgraph agent defer chapter-01 --reason "Source notation cannot be verified"
```

Deferrals retain their reasons in the audit and do not count as extracted source
coverage. Continue with independent units; do not restart the same dispute under
another ID or seek further reviewers merely to obtain agreement. Revisit it
only when new evidence or explicit user direction changes the task. Keep accepted
work as it stands; a final decision is followed by promotion or deferral.

## End-of-run audit

`end` is the default audit mode: after the run, record a human check before
treating it as finished:

```bash
syllabusgraph agent audit --reviewer "Reviewer name" --notes "What I checked."
```

`trust` mode makes that final human audit optional; it never removes the forced
critic or its evidence requirements. Use `syllabusgraph agent audit` to inspect
the dispatch, runtime, current and archived decision history, acceptance,
promotion, and human-audit trail.
