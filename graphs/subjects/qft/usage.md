# QFT construction: time and usage

**Work in progress.** These observations cover the graph-construction goal that
started at 2026-09-14T04:32:54+00:00. Earlier repository setup and work before that
goal are not included in its token or elapsed-time counters.

| Measurement | Recorded value |
|---|---:|
| Goal tracker tokens | 59,502,458 |
| Goal tracker elapsed hours | 23.29 |
| Recorded dispatches in this interval | 586 |
| Recorded native results | 568 |
| Distinct worker sessions confirmed in results | 216 |
| Dispatches with failure records | 17 |

Goal counters were observed through 2026-09-15T03:50:25+00:00; dispatch and
graph totals were collected at 2026-09-15T14:50:23.359818+00:00. These are cumulative
observations; do not add successive snapshots together.

The host token and elapsed-time counter stopped during an interruption. The displayed counter values cover work only through their stated timestamp; resumed work is tracked by dispatch records. A complete-run token total is not available from this counter.

A separate reconstruction from local session metadata extends the token measurement through **2026-09-15T14:50:04.552375Z**. At the interruption timestamp, the same calculation exactly reproduces the host's 59,502,458 tokens.

| Local session measurement | Recorded tokens |
|---|---:|
| Input excluding reported cached input | 56,703,400 |
| Output, including reasoning output | 10,574,563 |
| Comparable total: input excluding cache + output | 67,277,963 |
| Cached input traffic, reported separately | 1,730,461,824 |

This reconstruction covers the orchestrator and its descendant sessions with token events (224 sessions), including support and failed work. Cached traffic includes repeated input processing. Reasoning output is already included in output. Do not add this total to the frozen goal counter or to earlier snapshots. These measurements do not establish billing or active compute hours.

| Observed runtime model / effort | Input excluding cache | Output | Comparable total |
|---|---:|---:|---:|
| `gpt-5.6-sol` / high | 28,685,002 | 4,683,338 | 33,368,340 |
| `gpt-5.6-terra` / high | 22,711,050 | 4,234,337 | 26,945,387 |
| `gpt-6-astra` / xhigh | 5,307,348 | 1,656,888 | 6,964,236 |

Model attribution follows recorded session contexts. Mixed or missing profiles remain separate; the table includes orchestration and support work as well as source units.

| Requested model and effort | Recorded dispatches | Recorded results |
|---|---:|---:|
| `gpt-5.6-sol` / high | 336 | 324 |
| `gpt-5.6-terra` / high | 250 | 244 |

The current host allows one orchestrator and up to three workers. This run now
uses one worker at a time. Historical
peak concurrency and active worker hours were not measured. A worker can handle
several calls; session counts across stages overlap and must not be summed.
Failures can also have recorded results, so those columns overlap too.

At this snapshot, 4 textbook graphs have completed model review,
with 2,351 nodes and 2,857 relationships.
The shared graph has 1718 nodes and 2279 relationships,
representing 1922 book concepts. Shared construction and its
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
