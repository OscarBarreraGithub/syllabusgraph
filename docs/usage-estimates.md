# Usage, slow sessions, and checkpoints

**A full graph can exhaust your model allowance. Start small.** Browsing the
website uses no models. Extraction, critique, corrections, and your orchestrator
all use the native host's allowance. Even one long call can be expensive.

The default is a deliberately slow session that you resume when you choose.
Tell your agent: “Resume this project for one slow session; read its saved state
first.” You can space sessions over weeks. Closing the host does not discard
packets, accepted records, or completed reviews. There is no background runner.

| Control | Default | What it actually enforces |
|---|---|---|
| Worker calls per session | 2 | New `agent dispatch` tickets; failures count. |
| Concurrent workers | 1 | Another ticket waits until a pending one is completed or failed. |
| Admission window | 20 minutes | Stops new dispatches after the deadline; does not kill an existing call. |
| Request context | 750 KB | Compact JSON request content before ticket issuance, including the current graph. Not a token cap. |
| Recovery family | 6 calls | Tickets across explicitly linked units, including earlier failed calls. |
| Review path | One correction + recheck, then final decision | No reviewer-after-adjudicator loop. |

The engine cannot enforce your provider's token or spending limit, know your
remaining allowance, or meter ordinary orchestrator turns. Manual/external
runner invocations outside `agent dispatch` are also outside these gates.
The orchestrator must not bypass the gates with those routes. Consult the
host's own usage display before starting. Codex documents its dashboard and
CLI `/status` in its [usage guide](https://learn.chatgpt.com/docs/pricing).
Limits depend on models and context; don't translate a call budget into dollars.

## Commands for the agent

Use `-p PROJECT` for your actual course directory:

```bash
syllabusgraph work -p PROJECT status
syllabusgraph work -p PROJECT start
syllabusgraph work -p PROJECT pause
syllabusgraph work -p PROJECT start --resume
```

`start` does not call models. The first session needs it before any dispatch;
subsequent starts require `--resume` and a new user request. It refuses renewal
while a dispatch is unresolved. Complete or fail that existing ticket first.
Reconfiguring models cannot renew the allowance. At a cap, completion and
promotion remain available, so already paid-for work can be saved.

For an explicitly requested larger session:

```bash
syllabusgraph work -p PROJECT start --resume --dispatches 6 --minutes 60 --workers 1 --request-kb 1500
```

Choose limits case by case. Don't silently increase them when a request is too
large. The full graph currently contributes to each request, so a small source
scope alone does not guarantee a small request. The tool rejects oversize
context before issuing a worker ticket; see the [run lessons](qft-run-retrospective.md).

When new evidence requires a replacement packet, prepare a fresh unit and link
it before dispatch:

```bash
syllabusgraph work -p PROJECT link recovery-unit --parent original-unit
```

The immutable family link prevents a fresh unit ID from resetting the six-call
budget. It does not detect semantic duplicates automatically: the orchestrator
must link them honestly. Families are local to a project. Do not move a recovery
to a different project to evade limits. Deferred work is reported, never counted
as coverage. New user direction or scope needs an explicit recorded decision;
there is no silent family-budget reset command.

Checkpoints are the atomic packet, ticket, result, state, receipt, and work-session
files under `.syllabusgraph/`. `work status` summarizes them without model calls
or loading request bodies. It flags outstanding calls older than ten minutes;
that is a prompt to inspect once, not proof of a stalled model. Never spawn a
monitoring agent or repeatedly poll a long operation.

A private backup must include source working copies and `.syllabusgraph/` if you
want to resume on another machine. Git intentionally does not carry them. A new
public clone contains the reviewed results but none of your private run state.

## What the first large run cost

The [QFT retrospective](qft-run-retrospective.md) audits the complete creation
history. Its construction report records about **42 hours including pauses,
652 dispatches, and 222 distinct worker sessions**. The last independently
verified counter snapshot was **68.8 million comparable tokens**, but it ends
before completion. There is no trustworthy final token total or billed cost.
Treat this as a cautionary first run, not a price quote or a target for your
course. Reusing a reviewed graph is much cheaper than extracting it again.

The later [concept-inventory repair](../graphs/subjects/qft/concepts/README.md)
used six sequential worker calls across two units in the same bounded family.
It publishes dispatch intervals separately from the
[completion-work host counter](qft-share-ready-usage.json), which also covers
orchestration, website work, and verification up to its stated cutoff. These
are different scopes; do not add their counters or infer a billed total.

## Recording your own measurements


Keep measurements as the work runs, so a finished graph can include an honest
estimate of the effort required to reproduce it. Record the source scope, model
and effort settings, elapsed time, available token counters, and completion
status. Record the host's worker limit separately from any measured concurrency.

The repository includes a small metadata reporter:

```bash
python scripts/report_usage.py local-courses/my-course \
  --output .syllabusgraph/usage/latest.json
```

Pass multiple project directories to summarize a collection. It counts recorded
dispatches by model, effort, and stage, failures, and distinct worker sessions
confirmed by results. A reused worker counts once overall, even if it handles
several calls. Supplemental dispatch/completion ledgers can be included with
`--extra-dispatch-dir`. These counts cover available local records; a fresh
clone without private logs cannot reconstruct historical usage.

Token and time measurements come from the native host when available. Choose
the host's current reporting mechanism; this script does not install a provider
client or infer tokens from text length. An optional `--goal-snapshot PATH`
accepts a JSON object with a `goal` object containing integer `tokens_used` and
`elapsed_seconds` counters plus ISO `started_at` and `updated_at` timestamps.
Save only actual observations. The start timestamp also filters dispatches;
`--since` can explicitly select a different dispatch interval. Retain successive
snapshots privately rather than adding their cumulative counters together.

The report exports numeric counters and timestamps, not prompts, quotes,
worker identities, source paths, or failure explanations. Inspect it before
sharing. Keep underlying host logs and snapshots in ignored `.syllabusgraph/`
storage; publish only the selected aggregate report alongside the graph.

Elapsed time includes the activities covered by the host's clock; it is not
summed model computation time. Dispatch timestamps and file modification times
cannot establish active worker hours. An aggregate token counter does not
establish whether child-agent usage or cached tokens are included. Report these
limits, and keep unavailable values unknown.

Dollar or credit estimates need the applicable model rates and usage breakdown.
OpenAI distinguishes input, cached input, and output tokens; its account usage
records provide the appropriate billing context. [Official pricing and usage
documentation](https://learn.chatgpt.com/docs/pricing)

The [QFT measurements](../graphs/subjects/qft/usage.md) are a worked example.
They include development and review overhead. Construction and its model review
are complete, but the historical token counter ends before completion; the
measurements are not a promised runtime or complete billed cost for another course.
