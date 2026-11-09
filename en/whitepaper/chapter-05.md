> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-05` — 207 lines, 26087 bytes, block sha256 `7bf448ef45fbee70fd33d01037f0b0ef774e2092a91a5e59ebf30f47052db52d`, taken as the content between the `<!-- SP:BEGIN chapter-05 -->` and `<!-- SP:END chapter-05 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch05`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this chapter block, including all 13 case-annotation entries (batch 4, 2026-11-09); nothing inside the block is omitted
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: Proposition Group IV shows an internal SSOT inconsistency. The overview tables (SSOT lines 276, 305, 2427–2429), the already-landed appendix / chapter-01, and the C12 locked ledger all use "第四组核心命题：特权环隔离与脑裂传染" → "Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion". However the chapter-05 heading (line 1050) and the table of contents (line 37) read "第四组：权限、冲突、激励与退出" (Authority, Conflict, Incentive, and Exit). This translation follows the landed/locked form for book-wide consistency and flags the heading discrepancy for maintainer reconciliation.

**Scope and edition status.** This file is one block of a **phased** translation. As of batch 4 (2026-11-09), this file contains the complete chapter block, including the full case-annotation layer: the normative framework text, RFC 5.1–5.5, the conditional derivation IV-1, the §5.6 authorisation-implementation / receiver-side-regulation cases, the Syscall Lifecycle diagram, and all 13 case-annotation entries listed in the translation record are translated, and the Chinese master source remains authoritative (C2). The case-annotation sections retain the source's sharp register. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-05 -->` marker to the `<!-- SP:END chapter-05 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 5

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第四组核心命题：特权环隔离与脑裂传染 | Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion | group name, unique form in the whole book (landed/locked; see note above) |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 权限模型与社会桥接 | authority model and social bridging | claim identity (011) |
| 状态区分与机制假说 | state distinction and mechanism hypothesis | claim identity (012) |
| 有限两行动博弈的条件推导 | conditional derivation of a finite two-action game | claim identity (013) |
| 制度实例化与规范边界 | institutional instantiation and normative boundary | claim identity (014) |
| 识别边界与应用假说 | identification boundary and application hypothesis | claim identity (015) |
| 用户态资源保护 | user-mode resource protection | Ring-3 |
| Ring-3 保护 | Ring-3 Protection | §5.1 analogy |
| Ring-0 | Ring-0 | highest privilege level |
| 系统调用 | system call (Syscall) | §5.4 / §5.6 |
| 网络分区 | Network Partition | §5.2 |
| 脑裂 | Split-Brain | §5.2 |
| 可信承诺 | Credible Commitment | North & Weingast (1989); §5.1-C |
| 动态不一致性 | Time Inconsistency | Kydland & Prescott (1977); §5.1-C |
| 互补性垄断 | Complementary Monopolies | Olson (1993); §5.2-C |
| 流寇 / 坐寇 | roving bandits / stationary bandits | Olson; §5.2-C |
| 严格占优 | Strict Dominance | §5.3 |
| 纳什均衡 | Nash Equilibrium | §5.3 |
| 拜占庭雪崩 | Byzantine avalanche | §5.3 |
| 责任归因偏差与假性自愿叙事 | Attribution Distortion & Pseudo-Voluntary Narrative | §5.5 |
| 选择熵 | Choice Entropy | $H(\text{Choice})$, §5.5 |
| 特权环穿越 | Privilege-Ring Crossing | §5.6.1 diagram |
| 僵化经院化 | Scholastic Bloat | §5.6.1 (Entropic Trap) |
| 内核恐慌 | Kernel Panic | §5.6.2 |
| 恶意系统调用反模式 | Malicious Syscall Anti-Pattern | §5.6.2 |
| BGP 路由劫持 | BGP Hijacking | §5.2 analogy |
| 恶意在途截留 | Rogue Transit | §5.2 analogy |
| 合法拒绝或撤销程序 | lawful denial or revocation procedure | §5.4 |

**Note on claim identities.** The claim-identity labels in this chapter (RFC 011: authority model and social bridging; RFC 012: state distinction and mechanism hypothesis; RFC 013: conditional derivation of a finite two-action game; RFC 014: institutional instantiation and normative boundary; RFC 015: identification boundary and application hypothesis) are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words. The labels are not upgraded into proven conclusions; the negation guardrails in the source (does not / cannot / has not / one cannot / has not yet been proven) are preserved. Note also that SP-RFC-014 itself states that "applying for authorisation" and "constraining power" are not formally absolutely orthogonal, which is an explicit correction of the orthogonality metaphor within the source and is preserved as such.

**Convention on cross-chapter links.** In-page anchors that live in another English chapter or the appendix (#rfc-evidence-XXX, #sp-rfc-XXX) are linked directly to their corresponding English pages, maintaining full link closure within the English edition. Anchors that live in this file remain same-page links.

---

<!-- SP:BEGIN chapter-05 -->
<a id="chapter-5"></a>

## Chapter 5: Proposition Group IV — Privilege Ring Isolation & Split-Brain Contagion



<a id="sp-rfc-011"></a>
<a id="legacy-v11-1-sec-5-1"></a>
<a id="sec-5-1"></a>

<a id="legacy-v11-1-rfc-013"></a>
<a id="legacy-v11-0-rfc-009"></a>

### 5.1 SP-RFC-011 | Privilege Isolation and Constraints on the Executor

**Claim identity:** authority model and social bridging.
**Dependencies and additional conditions:** O2 and the specific execution structure; independent review, remedy, and compensation are specified separately.
**Generation and evidence card:** [G011](appendix.md#rfc-evidence-011).

**Normative Spec (规范条文).**
Modern rule-of-law property rights can be likened to user-mode resource protection with clear authority boundaries (Ring-3 Protection). In a conventional operating system, user-mode isolation is enforced with the kernel's participation and cannot by itself constrain the kernel itself; the social mapping must therefore also show how constraints such as independent review, separation of powers, remedy, and compensation act upon the power executor. When expropriation authority lacks these constraints and can expand arbitrarily, agents face a higher risk of property-rights withdrawal, and long-term investment may be suppressed; the degree and duration should be judged by institutional conditions and evidence — one cannot assert from the Ring-3 analogy alone that the capital-sinking function permanently falls to zero.

> 📜 **[Rule-of-law evolution annotation · Case 5.1-A] (England's 1215 Magna Carta and the establishment of privilege boundaries)**  
> *Paraphrase and scope of the original text*: Clause 39 of the 1215 Magna Carta lists restrictions on dispositions against free men: unless by the lawful judgment of his peers or by the law of the land, the detentions, dispossessions, and other treatments listed in the clause shall not be inflicted. "Or by the law of the land" is a conditional branch, not a statement that lawful disposition was likewise banned across the board; the extent of "free men" at the time also cannot be equated directly with modern universal civil rights. See [the Latin original of Clause 39 with translation](https://magnacarta.cmp.uea.ac.uk/read/magna_carta_1215/Clause_39).
> *Systemic analysis*: In protocolics, this is a major institutional milestone that constrains the highest privilege level (Ring-0) from carrying out arbitrary out-of-bounds operations. Although the "free men" to whom Clause 39 initially applied were a limited class, and it was no direct declaration of modern universal civil rights, in the subsequent centuries of constitutional evolution (including Sir Edward Coke's drive behind the 1628 Petition of Right and successive statutes such as the 1679 Habeas Corpus Act) the principle went through a double generalisation (API Widening) via judicial precedent and written legislation, gradually expanding into universal legal protection of person and property. It co-evolved with the common-law system and became an important historical-mechanism reference in institutional scholarship on constraining the crown and strengthening credible commitment, but it cannot be simple-linearly derived as the sole determinant of the Industrial Revolution.

> 📜 **[Violence-overreach annotation · Case 5.1-B] (Zimbabwe and Venezuela: the great memory-out-of-bounds collapse)**  
> *Case scope*: Zimbabwe's farmland expropriations and Venezuela's business expropriations and oil-industry layoffs can be used to study the relations among property rights, governance, and production capacity. The PDVSA layoffs covered many kinds of positions, and the total headcount cannot all be recorded as engineers; the specific figures, occupational composition, periods, and expropriation procedures must be verified against the original records, and this paragraph does not report precise headcounts for now.
> *Systemic analysis*: An unconstrained `sys_unmap_all()` can model the risk of arbitrary deprivation of resource control, but it cannot substitute for the two countries' separate event timelines. Output and inflation changes also involve fiscal-monetary, industry-management, external-condition, and other factors; this paragraph does not explain all consequences with multiples or single events that have not been verified on the same accounting basis.

> 📊 **[New institutional economics and macro-evidence annotation · Case 5.1-C] (North–Weingast credible commitment, the long-run movement of interest rates, and measured EPU investment elasticity)**  
> *Classic monograph and Nobel anchor*: Nobel economics laureate Douglass North and political scientist Barry Weingast, in the classic literature *Constitutions and Commitment* (1989), pointed out that constitutional arrangements such as the 1689 Bill of Rights, by strengthening parliamentary budget authority and judicial independence, significantly strengthened the institutional constraints on the crown's (Ring-0) arbitrary expropriation of property rights, providing the classic historical case for discussing the sovereign's "**credible commitment (Credible Commitment)**"; this mechanism is closely related theoretically to the 2004 economics Nobel laureates Kydland and Prescott's analysis of "**time inconsistency (Time Inconsistency)**" (Kydland & Prescott, 1977).  
> *Review of external empirical research*:  
> 1. **Historical evidence on credible commitment and long-run public credit**: North & Weingast (1989, pp. 822–824) record that in the early 1690s after the Glorious Revolution the English government obtained part of its initial long-term loans at about 14% interest; by the end of that decade it had fallen to about 6%–8%, and in the 1730s to about 3%. The authors also discuss the expansion of government borrowing and treat these secular changes as evidence of strengthened credible commitment. They are not a single risk-premium decline occurring instantly after an institutional switch, nor can the growth of government debt be relabelled as growth of the whole society's long-run capital pool.
> 2. **The empirical association between policy uncertainty and investment**: Baker, Bloom, and Davis (2016, *Quarterly Journal of Economics*) construct an EPU index from the frequency of economic-, policy-, and uncertainty-related coverage in newspapers. In a US quarterly VAR, an EPU innovation of about 90 points — comparable to the change in means from 2005–2006 to 2011–2012 — corresponds to a peak decline of about 6% in total investment. Here it is located at page 24 and appendix figure C7 of the 10 March 2016 author manuscript. The authors also report firm-level and 12-country panel analyses, but caution that the macro response need not admit a causal interpretation. The result supports continued research on the relation between rule uncertainty and investment, and cannot be treated as a one-standard-deviation structural elasticity of firm CAPEX with respect to contract-lifetime variance.
> *Verification sources*: [Baker, Bloom & Davis (2016), Measuring Economic Policy Uncertainty, author's public manuscript](https://www.policyuncertainty.com/media/EPU_BBD_Mar2016.pdf); [Baker, Bloom & Davis (2016), journal publication page](https://doi.org/10.1093/qje/qjw024).



<a id="sp-rfc-012"></a>
<a id="legacy-v11-1-sec-5-2"></a>
<a id="sec-5-2"></a>

<a id="legacy-v11-1-rfc-014"></a>
<a id="legacy-v11-0-rfc-010"></a>

### 5.2 SP-RFC-012 | Resource Cutoff, Communication Partition, and Conflicting Writes

**Claim identity:** state distinction and mechanism hypothesis.
**Dependencies and additional conditions:** P1 resource background; communication, authority, arbitration, and competitive incentive are each defined separately.
**Generation and evidence card:** [G012](appendix.md#rfc-evidence-012).

**Normative Spec (规范条文).**
When a central node can no longer continuously transfer to edge nodes the resources needed to sustain collaboration, service degradation, relationship decoupling, or control-right competition may appear. A network partition refers only to communication isolation; only when multiple nodes or partitions simultaneously claim valid write authority over the same resource and produce conflicting decisions does it constitute the split-brain referred to here. If arbitration, authority isolation, and stop-write-on-disconnect mechanisms are effective, a partition may manifest as a partial service pause without rewriting confirmed state. Mapping this mechanism onto regional warlordism requires separately proving the link between resource cutoff, failure of constraints, and competitive expropriation; the analogies of local malicious in-transit interception (Rogue Transit) and BGP-route hijacking with forged jurisdiction should also be checked separately, and cannot be inferred from fiscal distress alone.

> 📜 **[Historical evidence annotation · Case 5.2-A] (The Holy Roman Empire's robber knights and barrier networks)**  
> *Pending historical-comparison leads*: The Holy Roman Empire's merchant-route passage, toll privileges, and the armed men known as "robber knights" can be used to study the boundary between lawful charging and violent extortion; the specific periods, toll stations, and rights texts must be verified case by case, and the distribution and frequency of the toll stations must be determined from historical materials.  
> *Systemic analysis*: An in-transit controller intercepting resources can model Rogue Transit; forged cross-domain authority is separately modelled as a BGP Hijacking analogy. The empire's local privileges cannot be interpreted directly as an interruption of modern central transfer payments, nor can charging disputes yield wholesale severance of merchant travel or conflicting multi-writer writes.

> 📜 **[Early-modern history annotation · Case 5.2-B] (The institutional carcinogenesis of state-licensed privateers at the turn of the 17th to 18th centuries)**  
> *Pending historical-comparison leads*: Privateering commissions, wartime authorisations, and the armed employment after a truce can be used to study delegated violence and the cost of revoking authority. The periods of wars, treaties, armed groups, and piracy must be distinguished; the overall starting point of the "Golden Age of Piracy" cannot be attributed to a single truce, and unlocated instantaneous conversion headcounts are not reported.  
> *Systemic analysis*: Revoking delegated violence's authority may face real enforcement friction; this can model nodes that retain action capability after their credentials are revoked. Whether they turn pirate, whether they can be cleared, and the scope of harm must be argued separately; permanent irrevocability cannot be inferred from the granting of authority.

> 📊 **[Feudal fragmentation and dual-monopoly mark-up evidence annotation · Case 5.2-C] (The proliferation of Rhine toll stations and the Olken–Barron trucking-extortion measurements)**  
> *Classic theoretical anchor*: In "Dictatorship, Democracy, and Development" (1993, *APSR*), Mancur Olson used "roving bandits" and "stationary bandits" to distinguish plunder incentives under different time horizons: if a ruler expects to control the tax base long term, self-interested motives may still lead him to maintain order and some public goods; if his tenure shortens markedly, the relative gain from confiscating existing assets may rise. Fiscal cutoff and violent competition may therefore intensify short-sighted plunder, but whether they change tenure expectations, tax-base interests, and constraint mechanisms must be tested. The charging externality of multiple toll stations is another testable mechanism, and one cannot assert from it that all local nodes necessarily become roving bandits or erect toll stations without limit.
> *Review of external empirical research*:  
> 1. **The Holy Roman Empire's in-transit interception mechanism on the Rhine**: in the late-medieval period when the empire's central control slackened, lords' toll stations and transit dues proliferated along the main stem of the Rhine, forming a typical structure of multiple dispersed toll points and in-transit extraction that markedly raised the transaction and clearance costs of long-distance commercial shipping; the exact number of toll stations and cumulative toll rates in the primary sources vary by river segment, cargo, and statistical basis, but the complementary-monopolies (Complementary Monopolies) rent-extraction pattern they display became a standard historical reference in institutional economics for discussing decentralised plunder and coordination failure;  
> 2. **Barrier market structure and extortion pricing**: Olken and Barron (2009, *Journal of Political Economy*) sent surveyors riding along to record 304 trips on routes related to Aceh, Indonesia, directly observing more than 6,000 illegal payments. Exploiting the change in checkpoints caused by the troop withdrawal after a peace agreement, the study found that after some checkpoints disappeared, the average single-station payment on the remaining segments rose, consistent with the pricing mechanism of complementary monopolies. Illegal payments averaged about 13% of each trip's total transport cost (the paper's Table 1 cost figures use the 282 trips with complete wage data and do not move the 304-trip full sample into each column's denominator). These findings support bringing the strategic interaction among toll stations into the analysis; this book does not use them to give a verifiable estimate that "dispersed charging is nearly twice unified charging".
> *Verification sources*: [Olken & Barron (2009), The Simple Economics of Extortion](https://economics.mit.edu/sites/default/files/publications/090701%20Trucking%20paper%20JPE%20published.pdf).



<a id="sp-rfc-013"></a>
<a id="legacy-v11-1-sec-5-3"></a>
<a id="sec-5-3"></a>

<a id="legacy-v11-1-rfc-015"></a>
<a id="legacy-v11-0-rfc-012"></a>

### 5.3 SP-RFC-013 | Predatory Gain, Strict Dominance, and Static Equilibrium

**Claim identity:** conditional derivation of a finite two-action game.
**Dependencies and additional conditions:** P2-type choice; complete net payoff, strict dominance over all opponent strategies; dynamics argued separately.
**Generation and evidence card:** [G013](appendix.md#rfc-evidence-013).

**Normative Spec (规范条文).**
**Freeing malicious nodes from penalties raises the plunder incentive:** absence of slashing lowers the cost of plunder, but $\text{Penalty}_{\text{slash}}=0$ and $E[R_{\text{plunder}}]>0$ by themselves do not guarantee that plunder dominates cooperation. In a clearly specified two-strategy static game, if every node accurately maximises net expected utility and, for all opponent strategies $a_{-i}$, $Q_i(D,a_{-i})>Q_i(H,a_{-i})$, then plunder $D$ strictly dominates cooperation $H$, and universal plunder forms the unique Nash equilibrium. Whether a real system converges to this state, and whether a Byzantine avalanche or physical downtime appears, still requires stating the strategy-update mechanism, resource thresholds, and fault-tolerance boundaries.

**Conditional derivation IV-1: strict dominance and the unique static equilibrium.** Restricted explicitly to a normal-form game with a finite number of nodes, where each node has only the two actions cooperation $H$ and plunder $D$; $Q_i(a_i,a_{-i})$ denotes the net expected utility given in the payoff table. If for every node $i$ and every pure-strategy opponent profile $a_{-i}$ we have $Q_i(D,a_{-i})>Q_i(H,a_{-i})$, then for any mixed opponent strategy the probability-weighted average of the positive difference remains strictly positive, so $H$ is not a best response. No Nash equilibrium can assign positive probability to $H$; when all choose $D$, each node is again making the unique best response, so it is the unique Nash equilibrium, ruling out other mixed-strategy equilibria as well.
This conclusion applies only to this two-action payoff table. If extra strategies are allowed, reputation and punishment from repeated interaction are brought into the strategy space, or the strict inequality fails, the dominance condition must be re-examined; even if the static-equilibrium conclusion holds, it has not yet been proven that an arbitrary learning process converges, still less that communication split-brain, resource exhaustion, or physical collapse is proven.



<a id="sp-rfc-014"></a>
<a id="legacy-v11-1-sec-5-4"></a>
<a id="sec-5-4"></a>

<a id="legacy-v11-1-rfc-016"></a>
<a id="legacy-v11-0-rfc-013"></a>

### 5.4 SP-RFC-014 | Authorisation Interface for Specific Public Objectives

**Claim identity:** institutional instantiation and normative boundary.
**Dependencies and additional conditions:** specified jurisdiction, public objective, authorisation, and procedure; not every collaboration must enter the kernel.
**Generation and evidence card:** [G014](appendix.md#rfc-evidence-014).

**Normative Spec (规范条文).**
User space (Ring-3) can continuously organise collaboration through autonomous rules, community norms, contracts, and technical standards. For programmes that require nationwide coercive enforcement, public taxation, or statutory education standards, the authorisation and procedure interface that enters the national kernel (Ring-0) — call it a system call (Syscall) — is an important path to that specific objective. State recognition, institutional nesting, and direct state adoption are distinct relations; one cannot take becoming a state-default daemon as the uniform success criterion for all ideas, paradigms, or technology movements.

> **Institutional interface boundary and empirical-limitation statement**:
> 1. **Delimitation of its relation to SP-RFC-011**: SP-RFC-011 specifies how those in power are subject to institutional constraint and responsibility isolation, while SP-RFC-014 specifies what authorisation procedure a specific public objective depends on. "Applying for authorisation" and "constraining power" are highly interwoven and overlapping in real institutions and legal systems; one cannot claim that the two are formally absolutely orthogonal merely because their logical directions are opposite.
> 2. **Conceptual illustration, not fully automated code**: this item is currently a conceptual framework for institutionalised authorisation interfaces, not a fully automated machine-executable specification; an implementable institutional interface must delimit the jurisdiction, the scope of authorised actors, the statutory list of authorised acts, lawful denial or revocation procedures, and an independent channel for objection and remedy.

> 📜 **[Historical evidence annotation · Case 5.4-A] (Hu Shih and the 1920 vernacular-language directive: a Syscall successfully merged into the national standard library)**  
> *Period materials*: The Capital Metropolitan Education Affairs Bureau's Directive No. 4 of 23 January 1920, carried in [issue 7 of volume 1 (1920) of the Bureau's *Educational Administration Monthly*, scanned page 8](https://upload.wikimedia.org/wikipedia/commons/6/6e/NLC404-01J002135-24988_%E4%BA%AC%E5%B8%AB%E5%AD%B8%E5%8B%99%E5%B1%80%E6%95%99%E8%82%B2%E8%A1%8C%E6%94%BF%E6%9C%88%E5%88%8A_1920%E5%B9%B41%E5%8D%B77%E6%9C%9F.pdf#page=8), recites 案奉“教育部訓令第一二號” [receiving "Ministry of Education Directive No. 1-2"] (fixed as No. 12 per the OCR transcription of the contemporaneous scan and the Ministry's directive numbering system), requiring that in the autumn of that year grades one and two of the national schools “先改国文为语体文” [first change guowen (literary Chinese) into yutiwen (vernacular)] (transcribed in simplified characters). Here only what the linked forwarding directive of the Bureau records is transcribed; the Ministry of Education's 12 January 1920 circular No. 38 to the provinces and districts has been located (*Educational Gazette*, year 7, issue 2, official-correspondence section p. 12, 20 February 1920; cited at second hand in the Liang Peidong 2019 and Xueshushi Tan 2023 articles), but the imagery of that issue was not obtained this round, so no final determination is made. Central ministry orders and local forwarding orders must be distinguished; the material does not show that government documents nationwide switched to the vernacular in one stroke, nor does it show that Hu Shih personally drafted this administrative order.
> *Systemic analysis*: The Ministry of Education's 1920 directive marks a key node in the vernacular's entry into the institution of national education. The vernacular went from a civic intellectual proposal to formal inscription in the statutory standard of the national schools (entering the system call and the base environment). This section uses the system call (Syscall) as the analogy for the institutional authorisation interface, but the documentary provisions, textbook supply, teacher training, and actual diffusion across regions must be examined separately, and cannot be equated with all network nodes completing a synchronised switch instantly under a single instruction.

> 📜 **[Cross-civilizational annotation · Case 5.4-B] (Constantine's Edict of Milan and the Edict of Thessalonica: the institutionalization of Christianity and privilege-ring evolution)**  
> *Text of the edicts*: The 313 document usually called the Edict of Milan deals, in [the English translation of the text preserved by Lactantius](https://sourcebooks.fordham.edu/source/edict-milan.asp), with religious choice and the restitution of property to Christian bodies; [the Latin of Codex Theodosianus XVI.1.2 with its 27 February 380 date annotation](https://www.thelatinlibrary.com/theodosius/theod16.shtml) and [the edict's English translation](https://sourcebooks.fordham.edu/source/theodcodeXVI.asp) prescribe the recognised Trinitarian faith and mark out heretics. The two can be used to compare different interfaces of toleration, property rights, and orthodox authorisation, and the latter is not taken as proof that all religious practice switched in synchrony on a single day.
> *Systemic analysis*: This book likens the different legal arrangements above to an evolution of authorisation interfaces. Legal texts can confirm the expression of rules; actual enforcement, diffusion, and political motives must be argued separately; diffusion effects cannot be inferred from authorisation, still less can Constantine's and Theodosius' different measures be compressed into a single Syscall.



<a id="sp-rfc-015"></a>
<a id="legacy-v11-1-sec-5-5"></a>
<a id="sec-5-5"></a>

<a id="legacy-v11-1-rfc-017"></a>
<a id="legacy-v11-0-rfc-015"></a>

### 5.5 SP-RFC-015 | Feasible Choice Set, Exit, and Voluntariness Identification

**Claim identity:** identification boundary and application hypothesis.
**Dependencies and additional conditions:** clearly specified feasible alternative, exit cost, monopoly control, and observed denominator.
**Generation and evidence card:** [G015](appendix.md#rfc-evidence-015).

**Normative Spec (规范条文).**
When a central node monopolises basic resources and service interfaces and forcibly bundles indispensable basic services with other obligations, the terminal's feasible choice set may shrink markedly. If the accountability explanation merely invokes formal signing consent without disclosing alternative options, exit costs, and historical coerced contributions, an attribution distortion and pseudo-voluntary narrative arises. One should separately test resource control rights, bundling conditions, feasible exit paths, and ledger records before assessing their effect on trust. Observing choice entropy $H(\text{Choice})=0$ only shows that the choice set is concentrated within the sample; both preference homogeneity and deprivation of feasible alternatives can produce this phenomenon, so the constraint, exit cost, and feasible choice set must be identified independently.

> 📜 **[Antitrust engineering evidence annotation · Case 5.5-A] (From the "Company Town" to forced operating-system bundling)**  
> *Institutional history*: The "company towns (Company Town)" built by coal mines in Appalachia and other parts of the 19th-century United States frequently provoked serious disputes over exclusive scrip (Company Scrip), company stores (Truck System), and housing bundling; workers faced high exit costs and limited alternatives, making this a classic topic in antitrust and labour-law research on involuntary bundling. In antitrust case history, as in the litigation over Microsoft's bundling of the IE browser with the Windows operating system, the judicial focus likewise centred on whether the platform used its market dominance to strip downstream competitors and consumers of feasible alternatives. The analogy is meant to expose the structural lock-in mechanism; the voluntariness finding in any specific case must still be tested against statutory elements, price evidence, and judicial decisions.  
> *Systemic analysis*: When a critical survival interface is exclusively controlled, exit is costly, and alternative channels are blocked, a single choice cannot by itself demonstrate voluntariness. Waving "voluntary debt, buyer beware" to skip these constraints is covering up power relations that need verification; this paragraph is a mechanism critique, not a proven topological proposition.

> 📜 **[Institutional-economics annotation · Case 5.5-B] (The agricultural–industrial price scissors and the attribution bias over historical contributions)**  
> *Literature leads and verification scope*: Knight & Song (1999), *The Rural-Urban Divide*, and Lin Yifu, Cai Fang, and Li Zhou, *The China Miracle: Development Strategy and Economic Reform* (1994), are literature entry points for studying urban–rural relations, the heavy-industry-first strategy, and resource transfers. This section has not yet filled in the chapter-page citations supporting its statements on unified state purchase and sale, relative prices, and migration restrictions, and a book-title entry cannot be treated as item-by-item verification completed. The scale, periods, and attribution of macro resource transfers must be traced separately; this section reports no quantitative estimates of them.
> *Authors' proposal and mechanism explanation*: The book recommends disclosing early institutional constraints and inter-group resource flows when discussing intertemporal sharing; whether late-period entitlements are allocated on that basis still requires stating explicitly the fairness criterion adopted, group boundaries, periods, units of measurement, and rules of individual attribution. The fact of resource transfer does not by itself yield individual legal entitlements or a unique allocation ratio. "The decoupling of the historical-contribution record from after-the-fact responsibility attribution" and `git commit --amend` are only a critical analogy for selective attribution; they do not prove that historical records were deleted, nor do they fix any subject's causal responsibility; their effect on trust is tested separately by empirical work.



<a id="legacy-v11-1-sec-5-6"></a>
<a id="sec-5-6"></a>

### 5.6 Authorisation Implementation, Carriage, and Receiver-Side Regulation Cases



<a id="legacy-v11-1-sec-5-6-1"></a>
<a id="sec-5-6-1"></a>

#### 5.6.1 Relation between authorisation and implementation

The diagram below shows only the institutionalised branch that requires state authorisation; autonomy, contracts, and technical standards can continue to evolve at Ring-3 without uniformly entering the kernel. Post-entry rigidity is a risk path to be examined, not an inevitable life cycle.

```
┌────────────────────────────────────────────────────────────────────────┐
│      Privilege-Ring Crossing & Syscall Lifecycle Model (Syscall Lifecycle)     │
├────────────────────────────────────────────────────────────────────────┤
│  Userland / Ring-3                                                            │
│   - Civilian exploration / civic literature / fringe thought / open-source   │
│     drafts (fault-tolerant sandbox, but no hardware-scheduling authority)     │
│       │                                                                      │
│       ▼ On needing state authorisation, issue a system call                  │
│         (Trap / Software Interrupt)                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│  Kernel Space / Ring-0                                                        │
│   - Constitutional text / statutory standards / compulsory-education syllabus │
│     / official daemons (holds the privilege of violent scheduling)            │
│       │                                                                      │
│       ▼ If exit, review and feedback fail, institutional rigidity             │
│         (Entropic Trap) may arise                                            │
│  Scholastic Bloat                                                             │
│   - may become a privilege firewall that hinders innovation; specific        │
│     organisations must prove this independently                               │
└────────────────────────────────────────────────────────────────────────┘
```



<a id="legacy-v11-1-sec-5-6-2"></a>
<a id="sec-5-6-2"></a>

#### 5.6.2 Malicious and out-of-bounds syscalls: privilege instructions burning through physical hardware (The Malicious Syscall Anti-Pattern)

**Normative Spec (规范条文).**
When a sovereign kernel, detached from the carrying capacity of the underlying physical hardware, forcibly issues high-cost Syscalls lacking type checking and graceful-degradation fault tolerance, it may exhaust the underlying fault-tolerance margin and significantly raise the systemic risk of micro-level disconnection, production paralysis, and kernel panic.

> 📜 **[Historical evidence annotation · Case 5.6.2-A] (Heavy taxation detached from physical reality and system load)**  
> *Pending materials*: The parliamentary debates on the window tax are at §3.7-B; the tax-farming system of the French Ancien Régime is retained in this section only as a research lead, with the specific contracts, periods, and regional materials still missing. State fiscal revenue and risk allocation, collectors' incentives, taxpayers' burdens, and feasible alternative mechanisms must be checked separately, without presupposing that tax farming was necessarily more harmful than all alternatives.
> *Candidate mechanism*: If the full cost of a specified collection rule exceeds some subjects' carrying capacity and lacks shifting or buffering paths, reactions such as contraction, exit, and informal transactions can be tested; this section provides no incidence or causal estimates of these effects — the engineering analogy only organises pending questions.

> **[Policy-text comparison annotation · Case 5.6.2-B] (The wild-boar list adjustment, independent of the fiscal cases)**  
> *Policy text and official explanation*: [National Forestry and Grassland Administration Announcement No. 17 of 2023](https://www.forestry.gov.cn/c/www/gkzfwj/509750.jhtml) published the new list; [the policy interpretation carried on the Administration's website](https://www.forestry.gov.cn/c/www/gkzcjd/510106.jhtml) explains that the wild boar was moved out of the list and reminds readers that the adjustment does not mean the animal may be killed at will. This case is limited to the facts of the policy evolution in 2023, offers no advice on current individual enforcement cases, and does not treat the list revision as a measured optimal governance outcome.



<a id="legacy-v11-1-sec-5-6-3"></a>
<a id="sec-5-6-3"></a>

#### 5.6.3 Broadcast channel and receiver-side responsibility

> 📜 **[Cold War history annotation · Case 5.6.3-A] (Cold War East Germany's regulation of Western broadcast reception and channel tension)**  
> *Empirical observation*: During the Cold War, East Germany's (the German Democratic Republic's) policies, social pressure, and enforcement regulation of residents' reception of Western broadcast and television signals went through changes across different historical stages. In the 1950s–1960s (around the building of the Berlin Wall in 1961 and during the Free German Youth's antenna-cleanup campaigns), openly watching or listening to Western programmes was officially treated as serious ideological infiltration and political indiscipline, and organised dissemination or open group listening could face searches, detention, or charges under specific offences from the state-security organ (the Stasi) (under differing statutes touching incitement or sedition, among others); by the late 1970s (especially through the middle and later years of Erich Honecker's rule), private household viewing of West German television was in fact tolerated by limited default, but open dissemination and specific politically sensitive groups remained under close surveillance.  
> *Systemic analysis*: This is a typical case in protocolics for discussing **the physical properties of the broadcast channel and institutional-semantic regulation**. A broadcast has a certain coverage footprint under given frequency, power, terrain, and receiving equipment, and does not stop automatically at political boundaries. When a system cannot block effectively at the physical transmission end, it often turns to applying legal, social, or administrative pressure on the receiving end. This inversion of responsibility between the sending end and the receiving end confronts micro nodes with asymmetric institutional compliance costs in obtaining an objective physical signal; the differences in enforcement intensity across periods also show that the actual impedance of information control depends on the dynamic balance between the state's external technical feasibility and its internal social-governance costs.

<!-- SP:END chapter-05 -->
