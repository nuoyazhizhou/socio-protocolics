> **Translation record**
> - Chinese source: `docs/双语与写作约定.md` (sha256 `bc9f6ed607fc34af5d5f17abc7ddb574d5013362c75ab6dcbb57527941938c16`, 7476 bytes, 2026-11-08)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-08
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Chinese First, Case Pairing and Writing Conventions

Version: v0.4 | Date: 2026-10-27 | This is an English translation of the Chinese source; the Chinese source remains authoritative.

These conventions are distilled from the existing Chinese publication plan and sample drafts, rearranged according to the current state of the repository. Historical drafts, the full review process and source backups remain local. Framework definitions are governed by [Whitepaper v11.2, the sole canonical text](../社会系统协议学白皮书.md).

## Chinese First

Reader-facing project introductions, articles, framework guides, research cards, material notes and contribution guides are written in Chinese first, and an English counterpart is produced for each one afterwards. Third-party original texts, programs, configuration, stable numbering and data fields retain their original form, with the necessary Chinese explanations supplied; no separate translated set of code or source texts is created.

Each translation records six items: the corresponding Chinese file, the Chinese version or content hash, the translation version, the translation date, the check status, and changes not yet synchronised. After a correction to the Chinese source, the English text may be marked as pending sync and cannot continue to be labelled unconditionally as current. When a substantive problem is found in the English text, fix the Chinese source first and then synchronise; a translation cannot become a separate authoritative set of definitions on its own.

Compile a bilingual glossary first. The six core proposition groups must not be translated back into six proven universal laws; postulates, conditional propositions, mechanism hypotheses, accounting definitions and normative choices each retain their own status. Check in particular the distinctions between may/must, correlation/causation, the author's claim/independent evidence, and legislation/implementation/effect.

## Purpose Branches for the Same Theme

Distinguish first among theme, writing purpose, language and version. A single Hu Shi theme may have a research note, a long Zhihu post, a Reddit discussion draft and an academic paper at the same time; these are different deliverables. Version numbers are compared only within the same purpose branch: a research draft at v0.6 being lower than a Zhihu post at v1.0 does not make the former outdated, nor may an outreach draft be discarded by the stylistic standards of a research draft.

Each purpose branch registers its target readers, the problem it addresses, the action it hopes readers will take, its main files, its version and its actual status. When a single purpose has several process drafts, choose one primary working copy by content completeness, goal fit, unique material and known errors; move the rest to historical archives or label them explicitly as supplementary material. Where different purposes genuinely have value, keep them separately and do not merge them into one piece merely to reduce the number of files.

| Purpose of deliverable | Task this project intends to complete | Selection and maintenance priorities |
|---|---|---|
| Research note / exploratory article | Develop material, mechanisms, competing explanations and conditions that would change the verdict, for follow-up research | Source location, unknowns and proposition receipts; do not register a draft as an academic paper or as having passed the real-case acceptance stage (T3) merely because it is called a research draft |
| Long Zhihu post or short answer | Enter through a specific controversy, let readers understand one method of judgement and be willing to keep discussing | Narrative, pacing, engineering analogies and take-away questions; record long and short forms separately, and do not judge merit by length |
| Reddit discussion draft | Invite a specified community to supplement, refute or compare around a clearly stated question | First write a Chinese adaptation outline, setting out unfamiliar background, the discussion question and community fit; if it is not written, mark it as to be produced, and do not pass off a Chinese long draft renamed as an English draft |
| Academic paper | Answer a bounded question and submit a contribution relative to existing research, with the corresponding methods and evidence | Research question, literature, identification or argument, material and limitations; when the research is not complete, register only the plan, and do not rename an outreach article as a paper |

Different purposes may adjust structure, length, tone, background explanation and the presentation of citations; historical facts, sources and evidence strength are shared. Reach is not mechanism verification, and reading experience need not be written up in the form of a paper. Corrections to key facts and limitations that would change the conclusion must be checked draft by draft; it is not acceptable to fix only the research note while leaving known errors in the outreach draft.

Platform adaptations and complete translations are labelled separately. A complete translation follows the case-pairing requirements below; a separate adaptation must record its source draft and the purpose of the changes, and cannot be labelled a complete translation of the original. When no counterpart draft exists yet, register only the task; do not create a blank finished draft or invent a publication status.

## Chinese and Foreign Cases Appearing Together

Every case has a Chinese original and an English counterpart. Both languages keep the same set of cases and the same core comparison; background may be added and the order of explanation adjusted, but a different case must not be substituted in the English text while still labelling it a complete translation of the same piece.

For Chinese figures, explain to foreign readers "who he was, what the prior rule was, and what the change targeted"; for foreign figures, supply the background to Chinese readers in the same way. Do not assume that all English-language readers are familiar with European or American history.

Cases are paired by the same question and must not be spliced together merely by country or by a quota of good and bad outcomes. For the specific rules see [Case Selection and Comparison Method](../research/案例选择与比较方法.md). The "success" dimension may differ from case to case, but in that case the comparison is only heuristic and cannot be called a strict causal control.

## The Case-First Requirement

All topics, drafting, continuations and translations first follow [Case-Driven Writing and Proposition Testing](../docs/案例驱动写作与命题检验.md) and Article 9 of AGENTS.md. Read back the topic card first and make explicit the sub-claim, the real main case, real counter-material or a sourced competing explanation, the verdict and the position for theoretical write-back.

Each piece rests on at least one developed real process; key facts must be traceable, and engineering concepts enter afterwards. Conceptual explanation, simulated accounting and scattered name-checks of real material cannot replace a real case article; anything that does not meet the requirement is labelled a "conceptual sample chapter, pending reconstruction with a real case". A stylistic reference inherits only pacing and expression, not the numbers or "verified" claims in the sample text.

## Article Skeleton

Enter through a concrete puzzle, put forward a bounded judgement, and develop it with works, documents or process material. Each piece chooses one dominant engineering model and explains which relations it retains and which it does not retain. Engineering terms must help the reasoning, not merely rename the objects.

Keep a distinct viewpoint and readability, and place key conditions next to the judgement they qualify. Fictional scenarios, simulated numbers, other people's empirical results and the author's mappings are labelled clearly on first appearance, not patched up at the end.

Each piece treats at least one counterexample or competing explanation that could change the conclusion. The ending gives take-away checking steps and a concrete task to take up; "the material is insufficient" is an acceptable answer, and readers must not be asked to believe the whole framework first.

## Minimal Connections at the End of an Article

Each piece explains in several short paragraphs:

1. Existing research or historical sources: the original author, version and location; what they support and what they do not support.
2. Position in the framework: the primitives, postulates, proposition groups or RFCs used directly; background connections are listed separately, without hanging the entire system on the piece.
3. The author's mapping: engineering objects and social objects, relations retained and properties lost.
4. Assumptions and boundaries: audience, task, competing explanations, and what observation would force a revision.
5. Questions ready to be taken up: material already available, the first submittable result, and the current gap; label as a candidate when no mature card exists.
6. Version and language: the body text, source note, position in the master source and the status of the other language; do not invent links to files or URLs that have not been generated.

Key sources are also placed near the relevant body text. Mutual links between the project's own articles and the whitepaper provide navigation only and do not constitute external evidence.

Framework citations use explicit numbering and links to the original text, written as "postulate background → main proposition group/clause → normative objective or qualitative extension → untested parts → open questions". The source note lists positions in the body text separately; it is not enough to write "based on protocolics" only in an endnote, or to attach the whole 3→6→19 chain as a label. For a concrete example see the [Hu Shi article endnotes](../articles/hu-shih/如何评价胡适的作品.md#article-framework) and the [3→6→19 Theme and Case Index](../docs/框架与案例索引.md).

## From Examples Back to the Framework

Fact corrections first modify the corresponding article; where a definition or proposition changes, first record the original claim, opposing evidence, competing explanations and the proposed scope of change, then update the master source and affected derived drafts incrementally. Whether a method works, whether a mechanism holds and whether a postulate is appropriate are different questions, and favourable reviews of an article cannot substitute for one another.

New cases and translations must be added to the public manifest, with links and text scope checked; when modifying the whitepaper, the CheatSheet or AGENTS, also run regression according to [the verification gate rules](../AGENTS.md). Internal material and audit evidence are not made public automatically merely by being used in writing.
