# Record time and usage

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
They include development and review overhead and remain provisional until the
shared graph is complete; they are not a promised runtime for another course.
