# QFT construction: time and usage

**Work in progress.** These observations cover the graph-construction goal that
started at 2026-09-14T04:32:54+00:00. Earlier repository setup and work before that
goal are not included in its token or elapsed-time counters.

| Measurement | Recorded value |
|---|---:|
| Goal tracker tokens | 59,502,458 |
| Goal tracker elapsed hours | 23.29 |
| Recorded dispatches in this interval | 606 |
| Recorded native results | 588 |
| Distinct worker sessions confirmed in results | 217 |
| Dispatches with failure records | 17 |

Goal counters were observed through 2026-09-15T03:50:25+00:00; dispatch and
graph totals were collected at 2026-09-15T17:23:39.344634+00:00. These are cumulative
observations; do not add successive snapshots together.

The host token and elapsed-time counter stopped during an interruption. The displayed counter values cover work only through their stated timestamp; resumed work is tracked by dispatch records. A complete-run token total is not available from this counter.

A separate reconstruction from local session metadata extends the token measurement through **2026-09-15T16:29:29.111058Z**. At the interruption timestamp, the same calculation exactly reproduces the host's 59,502,458 tokens.

| Local session measurement | Recorded tokens |
|---|---:|
| Input excluding reported cached input | 58,047,723 |
| Output, including reasoning output | 10,784,714 |
| Comparable total: input excluding cache + output | 68,832,437 |
| Cached input traffic, reported separately | 1,769,443,840 |

This reconstruction covers the orchestrator and its descendant sessions with token events (225 sessions), including support and failed work. Cached traffic includes repeated input processing. Reasoning output is already included in output. Do not add this total to the frozen goal counter or to earlier snapshots. These measurements do not establish billing or active compute hours.

The observed wall-clock span from goal start to this cutoff is **35.94 hours**, including pauses, interruptions, and idle time. It is not summed worker time.

| Observed runtime model / effort | Input excluding cache | Output | Comparable total |
|---|---:|---:|---:|
| `gpt-5.6-sol` / high | 29,537,505 | 4,804,744 | 34,342,249 |
| `gpt-5.6-terra` / high | 23,075,680 | 4,277,009 | 27,352,689 |
| `gpt-6-astra` / xhigh | 5,434,538 | 1,702,961 | 7,137,499 |

Model attribution follows recorded session contexts. Mixed or missing profiles remain separate; the table includes orchestration and support work as well as source units.

The latest token refresh stopped at a counter-continuity check in local session history. The last verified token snapshot above is retained; newer token usage remains unverified. Graph and dispatch counts continue to update.

| Requested model and effort | Recorded dispatches | Recorded results |
|---|---:|---:|
| `gpt-5.6-sol` / high | 351 | 339 |
| `gpt-5.6-terra` / high | 255 | 249 |

The current host allows one orchestrator and up to three workers. This run now
uses one worker at a time. Historical
peak concurrency and active worker hours were not measured. A worker can handle
several calls; session counts across stages overlap and must not be summed.
Failures can also have recorded results, so those columns overlap too.

At this snapshot, 4 textbook graphs have completed model review,
with 2,351 nodes and 2,857 relationships.
The shared graph has 1901 nodes and 2652 relationships,
representing 2098 book concepts. Shared construction and its
combined audit remain in progress; the end human audit is pending.

The goal tracker's interface does not expose input, cached-input, output or per-model
breakdowns, and does not specify child-agent inclusion. Any local reconstruction
above is identified separately, with its own scope and timestamp. These are
runtime measurements, **not a verified billing total**. No dollar cost or
active computation time is inferred. Dispatch counts cover the available local
workflow and supplemental ledgers; orchestration and unlogged support work are
outside those counts.

This first construction includes corrections and development overhead. Its
unfinished totals are observations, not a promised cost or runtime for another
course. [Machine-readable measurements](usage.json) include the stage breakdown
and explicit accounting limits. [Recording guide](../../../docs/usage-estimates.md)
explains how to collect comparable measurements with the host available to you.
