# QFT construction: time and usage

**Work in progress.** These observations cover the graph-construction goal that
started at 2026-09-14T04:32:54+00:00. Earlier repository setup and work before that
goal are not included in its token or elapsed-time counters.

| Measurement | Recorded value |
|---|---:|
| Goal tracker tokens | 50,480,940 |
| Goal tracker elapsed hours | 18.57 |
| Recorded dispatches in this interval | 398 |
| Recorded native results | 389 |
| Distinct worker sessions confirmed in results | 202 |
| Dispatches with failure records | 6 |

Goal counters were observed through 2026-09-14T23:07:22+00:00; dispatch and
graph totals were collected at 2026-09-14T23:07:47.871770+00:00. These are cumulative
observations; do not add successive snapshots together.

| Requested model and effort | Recorded dispatches | Recorded results |
|---|---:|---:|
| `gpt-5.6-sol` / high | 229 | 222 |
| `gpt-5.6-terra` / high | 169 | 167 |

The current host allows one orchestrator and up to three workers. Historical
peak concurrency and active worker hours were not measured. A worker can handle
several calls; session counts across stages overlap and must not be summed.
Failures can also have recorded results, so those columns overlap too.

At this snapshot, 4 textbook graphs have completed model review,
with 2,351 nodes and 2,857 relationships.
The shared graph has 806 nodes and 802 relationships,
representing 922 book concepts. Shared construction and its
combined audit remain in progress; the end human audit is pending.

The token counter does not expose input, cached-input, output or per-model
breakdowns, and its interface does not specify child-agent inclusion. It is a
reported runtime counter, **not a verified billing total**. No dollar cost or
active computation time is inferred. Dispatch counts cover the available local
workflow and supplemental ledgers; orchestration and unlogged support work are
outside those counts.

This first construction includes corrections and development overhead. Its
unfinished totals are observations, not a promised cost or runtime for another
course. [Machine-readable measurements](usage.json) include the stage breakdown
and explicit accounting limits. [Recording guide](../../../docs/usage-estimates.md)
explains how to collect comparable measurements with the host available to you.
