> **Translation record**
> - Chinese source: `AGENTS.md` (sha256 `3fd935d6fbb3dbebe134b54d7109a635f650b2f7263e03bf1cf97543ab7adc62`), `社会系统协议学白皮书.md` (sha256 `e5c1eb322763a1a571aeae80327393692d00c4ac43baa937fc2c96da9aa9a148`, 338630 bytes), `核心概念速查手册_CheatSheet.md` (sha256 `6063c2e3259aa7d85c04d86c8fa7fc9606b973d207fa088a25d27b9d288b9799`, 39106 bytes), `docs/双语与写作约定.md` (sha256 `bc9f6ed607fc34af5d5f17abc7ddb574d5013362c75ab6dcbb57527941938c16`); all 2026-11-07
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-07
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: bilingual glossary (not a translation of a single Chinese document)
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Bilingual Glossary (en-v0.1)

This is a **translation aid**, not a definition source. All definitions, conditions and boundaries are authoritative only in the [Chinese master source](../社会系统协议学白皮书.md). Terms are listed here so that the English entry-layer documents use one English form per Chinese concept; a change of wording is not a change of concept. The [bilingual writing conventions](../docs/双语与写作约定.md) require a glossary before translation begins.

**Scope**: this glossary covers the four English entry-layer documents — [project introduction](./README.md), [participation guide](./CONTRIBUTING.md), [framework and case index](./FRAMEWORK_GUIDE.md) and this glossary. It is not a full-book terminology base; a complete English whitepaper would require a further pre-review before any chapter is translated.

**Authority of links**: in their bodies, the three translated documents link to the Chinese files that their Chinese sources link to; the [Chinese master source](../社会系统协议学白皮书.md) remains canonical (C2). The `./` links in the paragraph above are an editorial index of this batch's English counterparts, not a redirection of those source links. The English SSOT pointer still leads only to the Chinese master source.

**How to read the tables**: "Locked English" is the only form used in this batch. "Avoid" marks renderings that would alter the epistemic status of a claim, erase a negative guardrail, or invent a verification that has not happened.

## 1. Framework identity and versions

| Chinese | Locked English | Avoid |
|---|---|---|
| 社会系统协议学 | Socio-Protocolics | — |
| 核心架构白皮书 v11.2 | Socio-Protocolics Core Architecture Whitepaper v11.2 | — |
| 正交公理化奠基典藏版 | Orthogonal Axiomatic Foundation Edition | — |
| 双轨分层统一著作 | Dual-Track Unified Monograph | — |
| 单一事实真相源 / SSOT | canonical master source / Single Source of Truth (SSOT) | "English edition of the whitepaper" |
| 内部未删节版 | internal unabridged edition (not for public distribution) | any wording implying it is public |
| 修订发布标识 `v11.2-r20261106` | release tag `v11.2-r20261106` | v11.3, new edition, latest release |
| 中文原稿，英文待译 | Chinese original; English translation pending | — |
| 速查卡 | CheatSheet (L1 cognitive cache) | "definition source" |
| 框架与案例索引 | framework and case index | "complete introduction" |

The release tag marks a downloadable, comparable public revision snapshot. It does **not** mark a new theoretical version, a new postulate, a new SP-RFC item, or empirical validation. The theoretical version remains v11.2.

## 2. Epistemic status of claims

This is the highest-risk group. The six core proposition groups must not be rendered as six proven universal laws.

| Chinese | Locked English | Avoid |
|---|---|---|
| 公设（SP-POSTULATE-1/2/3） | postulate / first-order postulate | axiom, theorem, law, proven principle |
| 规范条文／项目（SP-RFC-001—019） | SP-RFC item / engineering specification | axiom; renumbering |
| 六组核心命题 | six core proposition groups | six laws, six proven theorems, axioms |
| 形式／条件命题 | formal / conditional proposition | theorem (unless the source is a derivation) |
| 经验机制假说／机制假说 | empirical / mechanism hypothesis | established mechanism, proven cause |
| 核算定义 | accounting definition | empirical finding |
| 规范目标／跨组规范守则 | normative objective / cross-group normative rule | descriptive law |
| 主张身份 | epistemic status of the claim | claim type |
| 主张—证据—边界三件套 | claim–evidence–boundary triad | omitting boundary |
| 表达增益／解释增益／预测增益 | expressive / explanatory / predictive gain | "improvement" for all three |
| 不升格 | does not elevate the claim to established status | omission |
| 待检验 | remains to be tested / untested | verified, validated, confirmed |

`SP-RFC-007` is a **normative operational rule**, not an objective descriptive law, and must never be listed alongside physical laws as though it were one. A group-level summary does not constitute a proof of its own sub-clauses.

## 3. Three coordinate systems

Three numbering systems coexist and **do not map onto one another**.

| Chinese | Locked English | Note |
|---|---|---|
| L1 传播层（极客白话版） | L1 Vernacular layer (The Vernacular) | Not Layer 1 of the pyramid |
| L2 理论层（多智能体对象模型） | L2 Theoretical Spec (Multi-Agent Object Model) | Not Layer 2 of the pyramid |
| L3 测度层 | L3 Future Mathematical Layer | A future direction, not an implemented layer |
| 三层正交金字塔 | three-tier orthogonal pyramid: Layer 0 postulates → Layer 1 proposition groups → Layer 2 SP-RFCs | No numeric mapping to L1/L2/L3 |
| 六层社会系统协议栈 L0—L5 | six-layer socio-protocol stack (L0—L5) | A third, functional coordinate |
| Ring-0 / Ring-3 | Ring-0 / Ring-3 (privilege-boundary analogy) | Keep "analogy"; not a real kernel |
| 「正交」 | orthogonal **as a division of responsibilities** | Not proven formal independence; that requires separate proof |
| 箭头／层级 | denotes modelling dependency and navigation | Not proof or derivation |

`3→6→19` expresses modelling dependency and clause ownership. It does **not** assert that all propositions have been strictly proved from the three postulates.

## 4. Negative guardrails

Chinese guardrails are substantive, not filler. Each has a fixed English form and must not be dropped for concision.

| Chinese guardrail | Locked English form |
|---|---|
| 不预设… | does not presuppose … |
| 不代表／不意味着… | does not imply … |
| 不由…直接推出 | does not follow directly from … |
| 须另验／另行检验 | requires separate testing / is tested separately |
| 不能替代证明／不代替实证 | does not substitute for proof / empirical validation |
| 门禁通过不代表… | passing the automated checks does not establish … |
| 仅为演示性预登记参数（illustrative） | illustrative pre-registration parameters only — not measured, estimated, or calibrated |
| 非实测警示语 | a non-empirical cautionary phrase, not a measured proportion |
| 「99% 异常路径」 | the "99% exception path" **as a cautionary phrase** |
| 概念形式化架构参考规范与未来实证研究议程 | a conceptual formalisation and reference architecture, plus a future empirical research agenda |
| 不显著不自动是反证 | a non-significant result is not by itself a refutation |
| 相关不自动是因果 | correlation does not by itself establish causation |
| 文章获得关注不等于框架得到验证 | attention received by an article does not validate the framework |
| 不以门禁通过表示章节已经审读完成 | passing the checks does not mean the chapter review is complete |
| 不因托管在 GitHub 上就自动获得授权 | hosting on GitHub does not by itself grant a licence |

The "99% exception path" is **not** a count of paths, a runtime share, or an incident rate. It is a cautionary phrase about attending to low-frequency, high-loss paths.

## 5. Register compartments

The framework deliberately keeps two registers. Flattening the whole text into neutral academic prose would remove a designed feature.

| Zone | English register | Rule |
|---|---|---|
| Normative clauses, definitions, accounting | cool, objective, restrained, clinical | No rhetoric |
| Annotations, cases, critical passages | retain the satirical and polemical edge | Do not neutralise |
| L1 engineering vernacular | keep TCP/UDP, Ring-0/3, Syscall, GC, Kernel, Compiler | Do not substitute social-science vocabulary; a plain-language gloss may be added on first use |
| Historical Chinese figures and institutions | on first use, say who he was, what the prior rule was, and what the change targeted | Do not assume familiarity with Chinese history |

Engineering analogies are there to organise questions. They are not proofs, and they do not establish that society has been measured.

## 6. Core terms

| Chinese | Locked English |
|---|---|
| O1 Agent（智能体） | O1: Agent |
| O2 Protocol（协议规范） | O2: Protocol |
| O3 Expectation & Trust（预期与信任） | O3: Expectation & Trust (subjective probability distribution mu; the expected value is not the distribution) |
| O4 Middleware（中介解释层） | O4: Middleware — intermediary interpretation layer |
| O5 Resource & Energy（物理硬约束） | O5: Resource & Energy — physical hard constraints |
| 私有目标函数 / 贴现因子 / 信息集 | private objective function U_i / discount factor beta_i / information set I_(i,t) |
| 排他控制／非生产性租金提取 | exclusive control / non-productive rent extraction |
| 寻租兼容层 | rent-seeking compatibility layer |
| 资源可行域 Ω | resource feasibility domain Omega |
| 胡适悖论 | The Hu Shi Paradox |
| 白话文总线 / 降低编译门槛 | vernacular bus / lowering the barrier to compilation |
| 计算系统工程大一统元编译器 | unified meta-compiler for computing systems engineering |
| 工业级参考实现 | industrial-grade reference implementation |
| 局部结构对应 / 机械还原论 | (local) structural correspondence / mechanical reductionism |
| 碳硅本体边界 / 硬件—协议纠缠 | carbon–silicon ontological boundary / hardware–protocol entanglement |
| 私设中间件收租 | setting up private middleware to extract rent |
| 策略性怠工断联（躺平） | strategic disengagement ("lying flat") |
| 伪造握手回执（形式主义欺骗） | forged handshake acknowledgements (performative compliance) |
| 异常路径 / Happy Path 中心主义 | exception path / happy-path centrism |
| 顶层总设计师幻觉 | the top-designer illusion |
| 演化赛马场看门人／主干合并维护者 | gatekeeper of the evolutionary racecourse / Bazaar Maintainer & Merge Architect |
| 增量绞杀式旁路 | incremental Strangler Fig bypass |
| 系统调用接口 Syscall / 用户态 Ring-3 | syscall (ABI) / userland (Ring-3) |
| 技术债核算与演化筛选 | technical-debt accounting and evolutionary screening |
| 迁移净负担 | net migration burden |
| 概念样章／待真实案例重构 | conceptual sample chapter, pending reconstruction with a real case |
| 演示性预登记样例／成对可区分预测对照 | illustrative pre-registration example / paired discriminating-prediction comparison |
| 未核 + 候选信源方向 | not verified; candidate source directions |

## 7. Verb strength

| Evidence strength | Use | Avoid |
|---|---|---|
| Strong (design and data present) | show / demonstrate / establish / reveal | — |
| Moderate (plausible, not settled) | suggest / indicate / be consistent with | prove |
| Weak / untested | may / appear to / one possibility | confirm |
| Statistical strength | "significant" only when a test was run; otherwise notable / marked | blanket "significantly" |

Numerical values in §8.5.4 of the whitepaper are **illustrative**. Do not attach statistical significance to them.

## 8. Entry-layer status vocabulary

| Chinese | Locked English | Avoid |
|---|---|---|
| 逐章讨论与增量修订 | chapter-by-chapter review and incremental revision | completed review |
| 门禁通过／自动检查 | passing the automated checks | validated, peer reviewed, empirically verified |
| 开放研究问题 | open research questions | solved problems |
| 可接手检验 | ready to be taken up and tested | established results |
| 尚未通过真实案例稿验收 | has not passed the real-case acceptance stage (T3) | rejected, failed |
| 尚无本项目效果数据 | no effect data from this project exist | "no evidence" (overstates the negation) |
| 尚未预注册、未取得效果数据 | not pre-registered; no effect data have been obtained | pre-registered draft |
| 展示计算逻辑的模拟解释示例 | illustrative worked example showing the calculation logic | measured, estimated |
| 尚未声明统一开放许可证 | no unified open licence has been declared | MIT, CC BY, or any licence chosen on the author's behalf |
| 只做机器检查时如实说明 | state plainly when only machine checks were run | omission |

`T1` material table, `T2` comparison draft, `T3` Chinese case article, `T4` English counterpart are **stage labels**, not acceptance certificates. Because T3 has not been passed, T4 case-article translation has not started; this batch translates entry-layer documents only.

## 9. Numbers and identifiers

- `3 postulates → 6 core proposition groups → 19 numbered SP-RFC items (001—019)`. Not 21 items plus a separate rule.
- `SP-RFC-007` is a cross-group normative rule; `SP-RFC-019` is a cross-group research and tooling norm located in Chapter 8; `SP-RFC-003` is a semantic application. The former v11.1 numbers 006/010 are retained as non-numbered materials and are not claimed to have been proved by another model.
- `M-01—M-05` external source items remain open; `S-01—S-14` are real-research starting conditions, not a to-do count.
- The release tag is not a theoretical version. Translation does not create a new edition, a V12, or a completed empirical study.

## 10. What this glossary does not do

It does not define the primitives, postulates, proposition groups or SP-RFC items; the [Chinese master source](../社会系统协议学白皮书.md) does. It does not record that historical cases, mathematical propositions or empirical effects have been verified — passing the automated checks establishes only structure, numbering, textual completeness and the reference implementations. It does not supply the missing external sources, does not upgrade "not verified" to "verified", and does not turn a conceptual sample chapter into an accepted case article. Where the Chinese source is updated, the affected English documents are marked as pending sync rather than treated as current.

See also the [agent rules](../AGENTS.md), the [CheatSheet](../核心概念速查手册_CheatSheet.md) and the [bilingual writing conventions](../docs/双语与写作约定.md).
