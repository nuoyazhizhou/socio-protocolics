> **Translation record**
> - Chinese source: `research/OP-001/材料包.md` (sha256 `8aaf5e7625ed891c534a046e5c28c8ad36c07febfad48207d56913173c4e55de`, 10837 bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# OP-001 Material Pack: Cases, Checklists and a Starting Point for Reading

Version: v0.2 | Date: 2026-10-23 | Claim status: **fictional scenario constructed by the author; not collected data; not a real-organisation diagnosis.**

Language: Chinese original; English translation pending.

The three cases and their answers are all public, for demonstration and material pre-testing only. A formal effect comparison requires newly added unseen cases; one must not use the public answers to train readers or models and then call the answering results an independent validation.

## I. Common Instructions

Use only the information given in the problem. First compare the explicit dimension of labour input, and at the same time report whether quality, coverage, latency and authority can be judged; do not assign values to unknown quantities yourself. You may keep, delete, replace, defer judgement, or supplement evidence, stating the conditions. Conditions already fixed by the scenario are treated as this problem's assumptions, and do not imply that investigation can be skipped in reality.

Scheme labels: D is a direct connection without the studied intermediary function; M is the current/candidate intermediary arrangement; M′ is an alternative arrangement that retains necessary functions. Not every case provides all three schemes; where not provided, one must not imagine their cost.

"Person-minutes" is the sum of the labour time of the relevant actors, not calendar latency. Monetary cost, resource consumption and loss allocation are recorded separately. Each unit of labour is counted only once. Monetary costs that are not given must not be assumed to be zero.

## II. Three Public Cases

### S1: Translation Layer

Goal: process the same batch of 100 document applications, finally complete 100, accepted by the same standard. Compare the labour input of D and M.

| Input field | D: direct processing | M: translation added |
|---|---:|---:|
| Total initial-processing person-minutes | 800 | 500 |
| Initial error count | 20 | 5 |
| Extra rework person-minutes per error | 10 | 10 |
| First-switchover total person-minutes | 0 | 120 |

Supplementary assumptions: the initial input covers all relevant parties — applicants, translators and back-office, etc.; error rework is not included in the initial input, and each error is reworked once and finally completed. M's 500 already includes the translation layer's own labour. The problem stipulates that the two schemes have the same acceptance, service accessibility, security and review conditions. No waiting-latency, cost, or long-tail risk data are provided, and M′ is not provided either.

Report the recurring input and the first-batch input including switchover separately, and judge to what extent the scenario supports retaining/introducing M.

### S2: Duplicate Sign-offs

Goal: the same batch of 100 internal applications, compare the labour input of M and M′.

| Input field | M: existing duplicate sign-offs | M′: remove duplicate sign-offs, retain necessary checks |
|---|---:|---:|
| Common base processing and rework total person-minutes | 400 | 400 |
| Duplicate sign-off total person-minutes | 200 | 0 |
| First-switchover total person-minutes | 0 | 50 |
| Finally completed count | 100 | 100 |
| Initial error count | 5 | 5 |

Supplementary assumptions: the problem has determined that the duplicate sign-offs provide no unique information or responsibility arrangement; independent acceptance, tracking, security, service accessibility and review are maintained by the original other mechanisms, and the authority to make this adjustment is clear. This assumption holds only within this problem. The common base input already includes rework; one must not again add the 5 errors multiplied by a self-chosen rework amount. No other costs or waiting latency are provided. M′ still has a check mechanism and cannot be called D, which removes all intermediary functions.

Report the recurring input and the first-batch input including switchover separately, and state which key premises this choice depends on.

### S3: The Pretty Registration Report

Goal: evaluate two batches in the same service domain. Each batch has 100 people who attempted to apply, but whether the application composition and validity are consistent has not been checked.

| Observation field | Before reform | After reform |
|---|---:|---:|
| Number who attempted to apply | 100 | 100 |
| Number registered | 100 | 60 |
| On-time qualified completions | 90 | 54 |
| All related person-minutes for the registered | 900 | 360 |
| Labour and waiting of the unregistered | no unregistered | not recorded |
| Reform migration input | not provided | not provided |

The report claims: the on-time qualified rate after registration is 90% in both cases, and per registered application the labour dropped from 9 minutes to 6 minutes, therefore overall system efficiency improved.

Supplementary information: it cannot be judged whether the new threshold blocked invalid applications, valid but hard-to-handle applications, or other populations. The rules, authority, application composition and long-term outcome material are incomplete.

Judge which parts of the report can be computed and which cannot be declared on this basis, and list the information most needing to be filled in. Do not presuppose that all unregistered applications are valid, nor presuppose that they should all be excluded.

## III. Common Answer Format

```text
Case and version:
Comparison schemes:
Task, observation period, acceptance standard, denominator:
Computable labour results (unit; recurring / one-off listed separately):
Quality, coverage, latency, cost and authority: what is known, what is unknown:
Tentative choice and applicable conditions:
Information most needing supplementation:
What evidence would make me change the choice:
```

## IV. Two Candidate Checklists A and B

The two groups use the same common instructions, cases and answer format. Both checklists are written by this pack and are not claimed to be existing standard scales. Before formal use, pre-test length, comprehensibility and omissions separately; do not give B exclusively more evidence.

### Checklist A: Cost and Process Comparison

<!-- CHECKLIST_A_BEGIN -->
1. Task boundary: state the service start, end, acceptance, observation period and the full demand denominator.
2. Handler responsibility: state the work done by the intermediary; after removal, state who takes over or why it is no longer needed.
3. Feasible schemes: compare direct D, intermediary M and the given alternative M′; where not provided, mark unknown.
4. Input accounting: separate labour, waiting, cost and migration; cover the relevant actors, do not double-count.
5. Result requirements: check whether quality, coverage, security, rare losses and recovery conditions are still satisfied.
6. Decision authority: state who can interpret, reject, change rules, as well as exit and independent-review methods.
7. Material basis: note the data source, rule version and applicable period, distinguishing fact, assumption and omission.
8. Conditional judgement: give the supplementation needed, the choice currently supportable, and what evidence would change the choice.
<!-- CHECKLIST_A_END -->

### Checklist B: Middleware and Protocol Comparison

<!-- CHECKLIST_B_BEGIN -->
1. End-to-end task: state the demand input, result output, acceptance, time window and full demand denominator.
2. Middleware responsibility: state the translation and other work; after bypass, state who takes over or why it is no longer needed.
3. Implementation choices: compare direct D, intermediary M and the given alternative M′; where undefined, mark unknown.
4. Link accounting: separate labour, waiting, cost and migration; cover the relevant nodes, do not double-count.
5. Exceptions and recovery: check whether quality, coverage, security, rare losses and recovery conditions are still satisfied.
6. Authority interface: state who can interpret, reject, change rules, as well as exit and independent-review methods.
7. Version and traceability: note the data source, rule version and applicable period, distinguishing fact, assumption and omission.
8. Output boundary: give the supplementation needed, the choice currently supportable, and what evidence would change the choice.
<!-- CHECKLIST_B_END -->

The field correspondence is A1↔B1 through A8↔B8. B mainly changes the organisation of terminology and prompts; both B8 and A8 require supplementation and one must not shrink B8 into a technical-input check and thereby change the research content. No additional causal facts are provided. This comparison alone does not by itself establish that adding diagrams, more fields, different training, or the entire Socio-Protocolics framework has an effect.

## V. Conditional Reference Answers for Material Review Only

The following are the arithmetic and reasoning answers within the scenario, **not verified real-social-utility labels**. Pre-test participants do not read this section before answering; the material actually distributed to participants should remove this section and fix the distributed version.

### S1 Reading

- D recurring input: 800 + 20×10 = **1000 person-minutes**.
- M recurring input: 500 + 5×10 = **550 person-minutes**.
- M first-batch input: 550 + 120 = **670 person-minutes**, 330 less than D's first batch; 450 less on a recurring basis.
- Under the scenario's stipulated goals and identical constraints, M's labour input is lower; an extra layer does not necessarily increase total labour. One must not conflate the initial error rate with the final completion rate.
- Not knowing cost, waiting and long-term risk, one cannot write "superior on all dimensions"; nor does the service's value by itself justify concluding that the handler should hold exclusive interpretive authority.

### S2 Reading

- M recurring input: 400 + 200 = **600 person-minutes**.
- M′ recurring input: **400 person-minutes**.
- M′ first-batch input: 400 + 50 = **450 person-minutes**, 150 less in the first batch; 200 less on a recurring basis.
- Under the scenario where unique functions are absent, other protections are maintained, and the adjustment authority is clear, M′'s labour input is lower. M′ retains necessary checks and is not D, which has no intermediary function.
- If a real application has not verified the above premises, one can only propose deletion as a candidate, not implement it directly per the problem. One must not re-add the rework already counted in 400.

### S3 Reading

- On-time qualified rate after registration: 90/100 = **90%**; 54/60 = **90%**.
- On-time qualified coverage by attempts: 90/100 = **90%**; 54/100 = **54%**.
- Unit input of the registered: 900/100 = **9 person-minutes**; 360/60 = **6 person-minutes**.
- After reform, the cost of the unregistered, migration cost and application composition are unclear, so a complete end-to-end resource comparison of the two batches cannot be computed, still less can the causal effect of the reform be identified.
- One should supplement validity and the reasons for exit/exclusion, the burden on the unregistered and dropouts, the rule version, migration and long-term outcomes. One cannot, because coverage fell, assert that the reform must be bad; nor can one use the registered-only data to declare an overall net gain.

## VI. Starting Point for the Scoring Rubric

Each item 0, 1 or 2 points; total 0–10. This rubric is to be frozen after external-material review; the scoring does not reward the use of engineering vocabulary.

| Dimension | 0 points | 1 point | 2 points |
|---|---|---|---|
| Boundary and denominator | not stated or clearly wrong | partially stated but missing an important denominator/stage | correctly states the overall task and relevant stages; S3 identifies the distinction between registration and attempts |
| Calculation and units | key arithmetic/unit error or assigning values to the unknown | partially correct, missing migration or mixing one-off with recurring | S1/S2 correctly split; S3 correctly computes local ratios and refuses a fabricated total cost |
| Quality and coverage | looks only at work-hours or layer count, ignoring constraints | mentions constraints but confuses indicators or scope | distinguishes known constraints from unknown results, identifies coverage, quality or recovery conditions |
| Scheme judgement | a universal conclusion unsupported by the scenario | direction reasonable but missing conditions | choice matches the scenario's goal and bounds the supportable scope; S3 may explicitly defer the net-gain judgement |
| Supplementation and revision | unknown ignored or only restating a position | lists gaps but cannot state the impact | proposes at least one concrete supplementation and its possible path to changing the choice |

Different phrasings such as "cost comparison" and "link accounting" receive the same score if the reasoning is the same. Scorers first record their respective initial judgements, then explain disagreements; if a problem cannot form a justified set of allowable answers, the problem should be revised, not forced to a gold standard by author preference.

## VII. The Minimum Content a Successor May Return

```text
Material version and reviewer background (voluntary):
Problems found: which part of the case/checklist/scoring?
Why it affects the conclusion or fairness:
Suggested replacement text or new field:
Whether equivalent existing research and its source are known:
Remaining unresolved uncertainties:
```

Finding zero problems may also be submitted as a clearly scoped receipt; one is not required to manufacture criticism. A material-review receipt does not equal passing independent empirical validation.

## VIII. Distribution and Measurement Boundaries

The current file simultaneously contains the problems and the answers; it is a public review copy. No independent participant-distribution copy, randomisation record or answer data have been generated yet. Future distribution must remove the reference answers and scoring explanations, freeze and record the material version; confirmatory research builds a separate unseen question bank that is not public.

These worked examples show how to preserve units, denominators and functional boundaries; they do not validate the Socio-Protocolics Whitepaper's serial-throughput formula, nor do they interpret the 1000/550 etc. person-minute ratios as loss rates.
