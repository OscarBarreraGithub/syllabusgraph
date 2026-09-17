# Native agent orchestration

Read [graph troubleshooting](../docs/graph-troubleshooting.md) before expanding
or reconciling a collection. A completed extraction can still lack a coherent
concept map. Define the intended level in the packet, preserve source-specific
treatments under shared concepts, and inspect one bounded visual pilot before
scaling. Do not call an exact-record intersection the backbone or interpret
missing matches as absent topic coverage. This checkpoint must not become a
repeated plan-review gate. Keep the existing dispatch and review limits.

Establish stable cross-source concept identities before treating mappings as a
subject overview. Record whether a treatment is equivalent, narrower, or an
alternative route; do not force all distinctions into separate overview nodes.
Define the backbone's selection rule and retain relevant boundary context.
Check recognizable subject coverage as well as preservation of input records.
Statistics from a small pilot must never stand in for full-collection overlap.
For a subject inventory, verify all memberships and native-source coverage before
publishing counts. A source-relationship projection can support navigation without
asserting new universal prerequisites; label that meaning and retain exact source
witnesses. Test a real path from overview to concept to original treatment and
back. Newly observed material errors need bounded new evidence and the linked
family budget; they do not justify an unrestricted review of the adjudicator.

Start with [the agent bootstrap](../SETUP.md) for installation and onboarding.
Before dispatch, run `syllabusgraph work -p PROJECT status`, then `work start`
only for authorized work. Defaults: two dispatches, one worker, 20 minutes for
admitting new work, 750 KB request content. Save returned results and pause at
a limit; never auto-renew. A later user request permits `work start --resume`.
Link recovery units with `work link CHILD --parent PARENT` before issuing a
ticket. Read [usage limits](../docs/usage-estimates.md) and
[the run lessons](../docs/qft-run-retrospective.md) before large extraction.

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

For whole-book construction, first inventory chapters, subsections, appendices,
projects, substantive problems, nonconceptual exclusions, and notation needed
to interpret claims. Verify source boundaries, including mixed problem/reference
pages and separate frontmatter numbering. Review this as source evidence;
do not turn it into repeated plan approval or hold up independent bounded units.
Keep full-book completion pending until the section coverage and the graph's
concepts, dependencies, and cross-unit consistency have all been reviewed.

Reconcile sections using the accepted records' section evidence and actual
content. One page can finish a section and begin another, so nonoverlapping
inventory page ranges cannot determine a concept's section assignment. Retain
shared boundary-page content in each applicable section and check that the
coverage assessment describes the records actually assigned to it.

Prepare the bounded packet with `syllabusgraph prepare` first. The orchestrator
then asks SyllabusGraph to create a dispatch, passes the resulting immutable
request JSON to the selected Codex or Claude native agent, and binds its JSON
result to that dispatch:

```bash
syllabusgraph prepare --unit chapter-01 --source reference-one --first 1 --last 10 \
  --scope "Core definitions" --context other-source:10:12
```

The optional `--context` range becomes immutable packet evidence alongside the
primary source. Primary and context pages share a budget of 80 pages by default.
Use `--page-budget N` when the necessary comparison evidence needs a different
bounded allowance, chosen for the sources and current model context. The budget
is recorded in the immutable packet; workers may not change it or quote or cite
material outside the recorded ranges. Changing a budget needs a new packet and
does not reset a work family's correction or dispatch limits.

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

Extraction drafts may finish after another unit is promoted. Their original
source packet and runtime response remain immutable; completion records a draft
without changing the accepted graph. Dispatch its independent critic against
the current graph, including any conflicts or duplicate concepts introduced
while extraction ran. A graph change during critique or adjudication still
invalidates that review, and promotion requires acceptance against the current
graph. Serialize potentially accepting reviews and promotions; running
extractors alone do not require a merge to wait.

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

One correction is a maximum, not a required extra pass. If the critic supports
the proposed science and its only remaining finding is that replacing an
accepted record requires adjudicator authority, dispatch final adjudication
directly. Another extractor pass cannot grant that authority. Preserve the
critic's finding and the adjudicator's decision in the normal audit trail.

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
