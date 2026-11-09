> **Translation record**
> - Chinese source: `research/README.md` (sha256 `eacec9237c905f9da8164894d4e34c9795572dafde1c552d5c85bd3fe88052e3`, `5266` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Research questions that can be taken up

The first three cards take up the [Hu Shi article](../articles/hu-shih/how_to_evaluate_hu_shis_works.md); OP-001 takes up the [intermediary article](../articles/intermediary/two_approvals_removed.md); OP-002 opens research on certification, authorisation and organisational autonomy; PR-001 studies agent collaboration scale separately. They are drafts of material verification and research design; none has been formally pre-registered, none has run experiments under its own protocol, and none has effect data.

## Raise questions, and also accept that a question may be rejected

The whitepaper can supply questions that can be taken up, candidate mechanisms and checking interfaces; it does not require the author to complete every empirical study personally. Participants may freely choose materials and suitable methods, and may also point out that a research question is already covered by existing theory; one need not first support protocolics, nor complete modelling, simulation and comparative history all at once.

Each project should write out its specific sub-claims, existing explanations, supporting and overturning observations, and the corresponding whitepaper position. Different lines of thought may be proposed first; methodological innovation and explanatory gain are judged by later comparison. The maintainer is responsible for definitions and source quality, and does not substitute waiting for external papers for the verification that should be done now.

Research results are collected under "sub-claim — evidence — competing explanation — verdict — intended write-back position". Support only strengthens the sub-claim under the corresponding conditions; opposition, zero gain and a better explanation should prompt withdrawal, narrowing or rewriting of the corresponding prediction, and one cannot register both kinds of result as verified. Where evidence is insufficient, defer the verdict; one should not declare the whole whitepaper established or invalidated on the strength of a single paper. Implementation follows [case-driven writing and proposition testing](../CASE_DRIVEN_TESTING.md), and submission and authorisation are covered in the [participation guide](../CONTRIBUTING.md).

## Project entry points

Cross-case work first registers scope, outcome dimensions, competing explanations and evidence per [the case selection and comparison method](./case_selection_and_comparison_method.md). That file is an exploration plan, not an already-completed cross-national comparison or a new formal pre-registration card.

[The I—VI thematic implementation plan](./topic_plan/README.md) already lists the concrete Chinese and foreign candidates, source starting points, rejection conditions and first task for the six groups of language interface, intermediary, commitment, authority, feedback and migration. The [standalone Group I plan](./topic_plan/I_channel_capacity_and_semantic_boundary.md) integrates H01—H03, existing case material and the 002 naming/response task; 002 has not yet been written into the Hu Shi main text, and the [preliminary naming-response table](./cases/CN-HU_naming_and_response_mapping.md) has been delivered; the [Second-Simplification evidence table v0.2](./cases/CN-S2_evidence_starting_point.md) records counter-test status and new-clue handling, and does not claim that the cognitive effect has been verified. They do not replace H01—H03 or PR-001, nor do they mean that the case study is complete. Submit the material first, then decide what conclusion it can support.

| Number | Question | First submittable deliverable |
|---|---|---|
| [H01](./H01_expression_and_understanding_cost.md) | Does making expression explicit lower comprehension cost? | A set of comparison texts checked by domain readers, with information kept as equal as possible |
| [H02](./H02_formal_status_and_adoption.md) | Through what pathway does formal status affect adoption? | Source, coding and counter-evidence records for a small number of contemporaneous texts |
| [H03](./H03_rules_and_actual_migration.md) | What lies between promulgated rules and actual migration? | A scope-check table for one directive and two textbooks |
| [OP-001](./OP-001/question_card.md) | Compared with an ordinary checklist carrying the same information, can engineered orchestration reduce intermediary analysis errors? | A check of three fabricated problems, the A/B checklist and a scoring starting point, plus the submission of one well-grounded material revision |
| [OP-002](./OP-002/question_card.md) | When does certified access transfer control, and when does it protect organisational autonomy and independent exploration? | A rights-allocation table from one charter or franchise document, distinguishing what is stipulated, what is actually executed and what is unknown |
| [PR-001](./PR-001_agent_collaboration_scale.md) | Does lowering access cost change the optimal agent collaboration scale? | A process description that records join/reject decisions and costs, or a contribution-scoring scheme |

PR-001 still has parameters to be locked; its public purpose is to solicit methodological feedback, and it cannot be executed directly as though it were an already-registered experimental protocol. The [source and revision note](./PR-001_source_and_revision_notes.md) explains how it differs from the original card.

OP-001 already provides a [research note](./OP-001/research_notes.md), a [material pack](./OP-001/material_pack.md) and [source boundaries](./OP-001/source_and_boundary.md). The public problems and answers may serve only as demonstration and material pre-testing, and one cannot use a high score after training on them to validate the method. For the real process, see instead [Zhejiang registration work outcomes](./cases/II-CN-A_housing_fund_registration_disposition.md) and [foreign research checks](./cases/II-INT_audit_and_driving_license_research_check.md); no institutional document has been turned into measured data.

OP-002 already provides a [research note](./OP-002/research_notes.md) and [source boundaries](./OP-002/source_and_boundary.md), registering certification investment, control, protective authorisation and exploration space separately as candidate hypotheses. The existing initial-check material only calibrates classification and does not constitute a Chinese–Western causal comparison; it connects to the concrete questions of Groups IV/VI, and adds no RFC nor claims that the core theory has been verified.

The minimal task aims at one person's material trial lasting about one to two weeks; the actual time adjusts with data availability. Success of a trial means accurate material and a reproducible method; one cannot treat completing a trial on time as establishing the theory.

Pre-registration requires locking the plan before the corresponding data collection or analysis begins, and stating clearly the existing knowledge, assumptions, variables, exclusion rules, sample plan and analysis method. Exploratory findings and later tests are marked separately. A Git record can trace versions, but commit dates can be specified and history rewritten; when registration is needed, use a registration service with an independent time record, and disclose later deviations. See the [Git date note](https://git-scm.com/docs/git-commit) and the [OSF registration note](https://help.osf.io/article/330-welcome-to-registrations).
