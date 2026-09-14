# Capability register

This is the record of implemented functionality. Update it with user-visible
changes; link the relevant code, verification, and guide. **Implemented** means
the listed behavior exists and is tested. **Manual** means a person or external
tool performs that step using supported files or commands. Proposed work is in
the [roadmap](roadmap.md), not implied by a working interface.

| ID | Capability and status | Interface and verification | Practical limits |
|---|---|---|---|
| C01 | **Implemented:** initialize a blank course or self-contained sampling example | `init`, `demo`; [onboarding tests](../tests/test_onboarding.py), [CLI tests](../tests/test_http_cli.py) | New courses have no private subject assumptions. Existing projects are not overwritten. |
| C02 | **Implemented:** standard material folders and private guidance brief | Generated `README.md`, `materials/`, `COURSE_GUIDANCE.md`; [file locations](file-locations.md), [onboarding tests](../tests/test_onboarding.py) | Guidance is human-readable; the engine does not parse or enforce it. Dropping files does not start processing. |
| C03 | **Implemented:** bibliography and local source registration | References UI; `source add/register/status`; [source code](../src/syllabusgraph/sources.py), [workflow tests](../tests/test_workflow.py), [browser checks](../scripts/test_browser.py) | PDF, UTF-8 TXT, and Markdown; 200 MB import limit. Image-only pages need external OCR. Mathematical extraction needs inspection. |
| C04 | **Implemented:** page-addressable, repeatable source packets | Source workflow UI; `prepare`; [workflow tests](../tests/test_workflow.py), [source guide](source-workflow.md) | One constant print/PDF offset per registration; at most 80 primary/context pages and 100 proposed concepts per unit; citations must be in that packet. Changed inputs need a new unit ID. |
| C05 | **Implemented:** native-agent dispatch contracts and external draft imports | `agent dispatch/complete`, `import-proposal`, `run`; [agent setup](agent-setup.md), [agent tests](../tests/test_agents.py) | The host launches models using its own account/tools. No bundled API client. Model identity relies on the trusted orchestrator's runtime report. |
| C06 | **Implemented:** mandatory configured critic, evidence checks, and atomic promotion | `check`, `agent complete`, `review`, `promote`; [workflow tests](../tests/test_workflow.py), [agent tests](../tests/test_agents.py) | Promotion requires a matching extractor result and independent critic or final adjudicator acceptance. Mechanical checks cannot certify scientific correctness. CLI workflow; existing manual drafts require new dispatches. |
| C07 | **Implemented:** validated concepts, relationships, evidence, notation, and motivations | [Data contract](project-format.md), [schema](../src/syllabusgraph/schemas/project.schema.json), [planning tests](../tests/test_planning.py) | Prerequisites must be acyclic. Alternate derivations and editorial relationships are explicit, separate relation types. Valid syntax is not scientific validation. |
| C08 | **Implemented:** mastery-sensitive closure and course inheritance | Course design UI, `plan`; [planner](../src/syllabusgraph/planner.py), [planning tests](../tests/test_planning.py) | Prior courses supply ready, explicit outcomes, not every topic they mention. Student background can override inherited assumptions. |
| C09 | **Implemented:** interactive course editing and saved drafts | Goals, treatment depth, assessments, background, exclusions, and session controls; [browser checks](../scripts/test_browser.py), [HTTP tests](../tests/test_http_cli.py) | Add/rename plan files and edit audience/narrative order in YAML. Conflicting saves require reloading. No hosted multi-user editing. |
| C10 | **Implemented:** estimated session partitioning and visible constraints | Course design UI, `build --strict`; [planner](../src/syllabusgraph/planner.py), [planning tests](../tests/test_planning.py) | Up to 1,000 selected concepts. Missing estimates and overload remain visible. Estimates are not calibrated teaching evidence. |
| C11 | **Implemented:** concept map, exports, and cross-course comparison | Concept map UI; `plan --format`, `build`, `compare`; [exports](../src/syllabusgraph/export.py), [planning tests](../tests/test_planning.py), [browser checks](../scripts/test_browser.py) | Exports: Markdown syllabus/preparation scaffold, JSON, Mermaid. Preparation notes need actual lecture development. No generated complete lecture prose. |
| C12 | **Implemented:** local persistence, recovery, and HTTP boundaries | Content digests, source checksums, atomic writes, review receipts, loopback server; [workflow tests](../tests/test_workflow.py), [HTTP tests](../tests/test_http_cli.py) | Interrupted locks require operator inspection. The app is local, not an authenticated hosted service. A reproducible reviewed build does not imply repeatable model output. |
| C13 | **Implemented:** package, verification, and publication checks | [CI](../.github/workflows/ci.yml), [release checks](releasing.md), [audit script](../scripts/audit_public.py) | CI covers Linux with Python 3.11/3.14 and macOS/Windows with Python 3.14, plus Chromium browser tests. Automated audit is a screening aid. |
| C14 | **Manual:** publish reviewed course results independently of textbooks | [Sharing guide](sharing.md); existing builds work from reviewed project files | No one-command publication or automatic textbook-redaction tool. Review selected files before committing; original course materials remain local. |
| C15 | **Implemented:** clone-first Codex/Claude onboarding and configurable role defaults | `AGENTS.md`, `CLAUDE.md`, native profiles, generated course instructions, `agent configure/policy`; [setup](agent-setup.md), [onboarding tests](../tests/test_onboarding.py), [agent tests](../tests/test_agents.py) | Terra high/Sol high or Sonnet high/Opus high. Host availability must be verified. Custom policy needs matching runtime settings; no silent substitution. |
| C16 | **Implemented:** bounded revisions and critic adjudication with decision history | `agent dispatch/complete --stage adjudicate`; [agent code](../src/syllabusgraph/agents.py), [agent tests](../tests/test_agents.py) | Two adverse reviews by default force escalation; rejection escalates immediately. One correction by default, then final accept/defer adjudication without another critic. Six dispatches including retries; exhaustion and invalid final results defer the unit. Reasons remain in the audit; deferred work does not count as coverage. |
| C17 | **Implemented:** final human audit or explicit trust-critic mode | `agent audit`, `agent configure --audit-mode`; [agent tests](../tests/test_agents.py) | Audit is local and snapshot-bound. It reports unfinished units; human review is operator-attested. Agents must not invent a human sign-off; the engine cannot authenticate human identity. |

## What is not implemented

- A built-in AI extraction provider or autonomous textbook-to-course button.
- Integrated OCR or reliable automatic reconstruction of mathematical notation.
- In-app proposal editing, substantive critique, and promotion controls.
- Automatic proof of scientific correctness, course completeness, or teaching quality.
- An authenticated hosted workspace, institutional syllabus corpus, or wiki deployment.

Tests and code substantiate the software behavior above. Public course examples
need their own content-review record; software tests do not certify their claims.

Native Codex smoke verification used an original short primer: a real Terra/high
worker extracted two concepts and one prerequisite, and a separate Sol/high
worker accepted the exact proposal before promotion. No private course material
was processed. Claude role files and policy behavior are validated by configuration
and protocol tests; a live Claude session has not been exercised in this change.
