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

After extraction, dispatch a critic for that exact proposal. A critic `accept`
is recorded as the workflow's operator acceptance; `revise` or `reject` cannot
be promoted. Every adverse critic note is an actionable finding. The policy
counts adverse critic completions cumulatively for the unit: two revisions
require adjudication, and a `reject` requires it immediately. Dispatch an
adjudicator only with a current adverse critic. Its completion must contain a
complete revised proposal and exactly one decision for every finding, using that
finding's zero-based critic-note index, at least two alternatives, rationale,
source/section/pages evidence, and every affected proposal record. Run a fresh
critic with a native identity different from both extractor and adjudicator on
the revision. If later adverse cycles reach the limit, adjudication remains
mandatory under the configured critic/adjudicator policy; do not replace it with
a per-unit human approval loop. Under the default Codex policy, those decisions
continue to use `gpt-5.6-sol` at high effort. The orchestrator promotes only
after current checks and a current recorded critic acceptance.

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
