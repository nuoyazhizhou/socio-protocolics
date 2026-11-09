<!-- Translation record -->
<!-- C2 registration: id=chapter-08 / source=社会系统协议学白皮书.md lines 1510-2360 / sha256=d02e3780ff9c155595d1c423405e3c2f4b293f782d9d6601242b7c8bae01915c / status=phased(abridged adaptation) / auditor=independent read-only audit PASS (first pass BLOCKED-CJK @ draft L161; fixed; re-audit VERDICT PASS; 0 hard errors) / date=2026-11-08 -->
<!-- Scope: 框架正文 + §8.1–§8.6 全译；本章无本章程案例块，2.2-A/3.1-A/3.3-A/5.4-A/5.5-A 为跨章引用按引用保留 -->
<!-- claim-identity note: SP-RFC-019 = mechanism hypothesis & exploratory warning (not proven); B-A/B-B = worked pre-registration examples (illustrative); C1/C2/C3 = paired discriminating predictions, 本书预测 B 不升格 -->
<!-- symbol-scope note: B 作用域多义，全书统一口径见下方 Note on symbol scope 与 en/GLOSSARY.md §3；B_Hz 带宽(§2.1/ch01) / B 候选模型 symbols per second(ch01 §1.5.4) / C_B 介数中心性(§8.3.4) / B=10000 bootstrap 次数(§8.5.4.2) / B_{TCP},B_{UDP} 流量分类(§8.3.4；仅 B_{TCP} 亦见 ch06 §6.1.1)；R 作用域多义(\mathcal{R}_{deadlock} 综合死锁风险 / R_{drop} 立案驳回率 / \mathcal{R} of O2 奖惩规则集)；均按作用域原样保留，不合并、不互换 -->
<!-- link-repointing convention: 跨章锚点改 ](../../社会系统协议学白皮书.md#X)；同页 #X 保留 -->
---

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper. Chapter 8 carries no case-annotation block of its own; the cross-chapter case references 2.2-A / 3.1-A / 3.3-A / 5.4-A / 5.5-A are retained as references to other chapters. The block itself runs from the `<!-- SP:BEGIN chapter-08 -->` marker to the `<!-- SP:END chapter-08 -->` marker; the translation record, the chapter glossary and the notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 8

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 语义漂移指数 | Semantic Drift Index (SDI) | §8.3.1 proxy input |
| 修辞冗余填充度 | Padding Bloat Ratio (PBR) | §8.3.2 proxy input |
| 有效载荷比率 | Payload-to-Noise Ratio (PNR) | §8.3.2 proxy input |
| 系统调用阻抗与丢包率 | Syscall Impedance & Rejection Rate (SIR) | §8.3.3 proxy input |
| 传输拓扑极化与中间人劫持系数 | MITM Polarizing Metric (MPM) | §8.3.4 proxy input |
| 全局系统死机健康度综合指数 | System Health Index (SHI) | §8.3.5 composite score |
| Socio-Radar Engine | Socio-Radar Engine | §8.2 exploratory architecture (keep) |
| AI工具控制与探索性预警 | AI Tool Control and Exploratory Early-Warning | RFC 019 title (locked) |
| 综合死锁风险得分 | comprehensive deadlock-risk score $\mathcal{R}_{\text{deadlock}}$ | §8.2 / §8.3.5; homonym with $R_{\text{drop}}$ |
| 立案/审批驳回率 | case-filing / approval rejection rate $R_{\text{drop}}$ | §8.3.3; homonym with $\mathcal{R}_{\text{deadlock}}$ |
| 带宽 | bandwidth $B_{\text{Hz}}$ | §8.5.4.3 physical-channel capacity; homonym |
| 介数中心性 | betweenness centrality $C_B$ | §8.3.4; homonym with $B_{\text{Hz}}$, $B=10000$ |
| bootstrap 次数 | bootstrap repetitions $B = 10000$ | §8.5.4.2; homonym with $B_{\text{Hz}}$, $C_B$ |
| 语义突变加速度 | semantic mutation acceleration $a_{\text{drift}}$ | §8.3.1 |
| 修辞词典 | padding lexicon $\mathcal L_{padding}$ | §8.3.2 |
| 词汇告警比例门槛 | lexical alert-ratio threshold $\tau_{\text{lex}}$ | §8.3.1 (default 0.15) |
| 漂移加速度复核阈值 | drift-acceleration review threshold $\theta_{\text{review}}$ | §8.3.1 (0.25) |
| 白化/基线校准 | whitening / baseline calibration | §8.3.1 |
| 未校准研究标记 | uncalibrated research flag | §8.4 |
| 演示性预登记参数 | illustrative pre-registration parameter | §8.5.4 |
| 完整数值化预登记样例 | full numerical pre-registration worked example | §8.5.4 (B-A / B-B) |
| 成对可区分预测对照 | paired discriminating-prediction comparison | §8.5.4 (C1 / C2 / C3) |

**Convention on cross-chapter links.** In-page anchors that live in another English chapter or the appendix (#rfc-evidence-XXX, #sp-rfc-XXX) are linked directly to their corresponding English pages, maintaining full link closure within the English edition. Anchors that live in this file remain same-page links.

**Note on coordinate systems (section-local numbering).** The `L1` / `L2` / `L3` in §8.5.4 name three pre-registered DGP assumptions of that section — flow topology, the loss-correlation mechanism, and estimation-error covariance — and are local to it. They are not the L1/L2/L3 twin-track writing coordinate of Chapter 1, nor the Level 0/1/2 orthogonal pyramid, nor the L0–L5 functional stack: the three book-wide coordinate systems declared in `en/GLOSSARY.md` §3 and Chapter 1 §1.1 do not map onto one another by number, and this section-local numbering does not map onto any of them. The chapter keeps the three layers separate and states that they must not be collapsed into one.

**Note on symbol scope (cross-reference, not a definition).** The letter `B` is reused across explicitly scoped contexts in the English edition and is not one quantity: `B_{\mathrm{Hz}}` is bandwidth in hertz (§2.1, recorded in Chapter 1 §1.5.4; the same quantity is written `B_{\text{Hz}}` in this chapter's glossary), `B` in the candidate model is symbols per second (Chapter 1 §1.5.4), `C_B` is betweenness centrality (§8.3.4), `B = 10000` is a bootstrap repetition count (§8.5.4.2), and `B_{\text{TCP}}` / `B_{\text{UDP}}` are the two traffic classes of the MITM polarizing metric (§8.3.4; of the two, only `B_{\text{TCP}}` is also referenced in Chapter 6 §6.1.1). The letter `R` is likewise reused: `\mathcal{R}_{\text{deadlock}}` is the composite deadlock-risk proxy, `R_{\text{drop}}` is the case-filing / approval rejection rate, and `\mathcal{R}` in O2 (Chapter 1 §1.5) is the reward-and-penalty rule set. Chapter 1's *Scope of symbols and names* records two of the `B` senses and the O2 `\mathcal{R}` distinction as the Chinese source states them; this note is the consolidated cross-reference for the English edition, and `en/GLOSSARY.md` §3 points to it. None of these symbols is merged with, or substituted for, a symbol from another scope.

<!-- SP:BEGIN chapter-08 -->

<a id="chapter-8"></a>

## Chapter 8 — Measurement Definitions, Reference Implementations, and Research Boundaries

This chapter enters through SP-RFC-019, the cross-group tool / research norm, and then lists measurement and reference implementations. 019 was migrated from the old Chapter 7 and adds no new clauses; that a reference implementation runs does not mean the social indicators are already calibrated.



<a id="sp-rfc-019"></a>
<a id="legacy-v11-1-sec-7-3"></a>
<a id="sec-8-1"></a>

<a id="legacy-v11-1-rfc-021"></a>
<a id="legacy-v11-0-rfc-020"></a>

### 8.1 SP-RFC-019 | AI Tool Control and Exploratory Early-Warning

**Claim identity:** application and research norm.
**Dependencies and additional conditions:** the specific tool / governance objective and agent calibration; not a theorem deduced from Group VI.
**Generation and evidence card:** [G019](appendix.md#rfc-evidence-019).

**Normative Spec.**
This section is an application / research norm for tool control and exploratory measurement; it retains the Group VI entry point and links to Groups II / IV, and does not call itself a new law deduced from the sixth group. Within the same item this norm explicitly separates three duties and constraint boundaries of different kinds:

1. **Tool execution authority and verification boundary:** an LLM may translate some natural-language requests into tool calls or code; effective execution must be constrained by the principle of least privilege, relying on strict parameter parsing, allow-list verification, and two-way confirmation feedback (linked to Group IV's privilege isolation).
2. **Model-access and switching-cost hypothesis** (linked to Group II's `SP-RFC-005` and Group IV's `SP-RFC-015`): if a few providers control key models, data, or access interfaces, this may raise switching and review costs; whether it constitutes a monopoly and what harm it causes requires empirical comparative testing; open source, on-device deployment, interoperability, and independent audit are comparable governance options, each with its own costs and risks, and one cannot presuppose that any one deployment mode necessarily liberates or enslaves the agent.
3. **Use limits on uncalibrated proxy scores:** Socio-Radar is only an uncalibrated conceptual architecture and an exploratory research tool; its scores serve merely as clues that trigger internal research review, and under no circumstances does it automatically authorise real-world physical circuit-breaking, privilege revocation, or institutional restructuring.



<a id="legacy-v11-1-sec-8-1"></a>
<a id="sec-8-2"></a>

### 8.2 Social Discourse and Consensus-Health Early-Warning System Architecture (Socio-Radar Engine)

**Normative Spec.**
This section proposes the exploratory risk-proxy score $\mathcal R_{\text{deadlock}}(t)$. It is a yet-to-be-calibrated weighted indicator and does not presuppose that social collapse is a deterministic phase transition; whether it has predictive power beyond a baseline model requires testing on independent data:
$$\mathcal{R}_{\text{deadlock}}(t) = \omega_1 \cdot \underbrace{\overline{\text{SDI}}(t)}_{\text{语义漂移指数}} + \omega_2 \cdot \underbrace{\text{PBR}(t)}_{\text{修辞冗余填充度}} + \omega_3 \cdot \underbrace{\text{SIR}(t)}_{\text{系统调用阻抗}} + \omega_4 \cdot \underbrace{\text{MPM}(t)}_{\text{极化劫持系数}}$$
The baseline weights $(0.30,0.25,0.25,0.20)$ are a demonstration setting, corresponding to the four proxy inputs SDI, PBR, SIR, and MPM, and are not equivalent to physically measured quantities or statistically estimated coefficients.
When a preset threshold is exceeded, it only triggers data-quality and mechanism review; it does not, on the strength of the score, automatically call for cleansing, punishment, disconnection, or institutional restructuring. The false-positive rate, false-negative rate, and net intervention benefit of the threshold require separate verification.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. 全网多源数据接入层 (Ingestion Gateway)                              │
│    社交媒体、新闻网评、司法裁判文书、政策草案、百科编辑                    │
├────────────────────────────────────────────────────────────────────────┤
│ 2. 协议动力学分析计算内核 (Protocol Analytics Core)                     │
│    - 语义漂移计算模块 (Semantic Drift Index via BERT/Embedding)        │
│    - 反馈与扩散结构模块 (TCP/UDP 为机制类比，非善恶标签)               │
│    - 中间人结构与标签变化候选信号（是否恶意须另有独立证据）             │
│    - 系统调用阻抗测算模块 (Syscall Gap: 民间诉求与现有立法接口距离)     │
│    - 协议肥大与异味探测模块 (Spec Bloat & 官僚黑话比率测算)             │
├────────────────────────────────────────────────────────────────────────┤
│ 3. 社会共识风险预警控制台 (Social Cohesion Early Warning Dashboard)   │
│    • 🟢 绿色：低于演示阈值，不构成现实健康认证                            │
│    • 🟡 黄色：研究分数触发复核，需检查数据、模型和任务结果                  │
│    • 🔴 红色：触发演示直接阈值或低综合分数，不等于崩溃已发生                │
└────────────────────────────────────────────────────────────────────────┘
```



<a id="legacy-v11-1-sec-8-2"></a>
<a id="sec-8-3"></a>

### 8.3 Five-Dimensional Core Metrics of Protocol Dynamics and Mathematical Formulation

**Normative Spec.**
The following defines four proxy inputs and one composite score, for use in conceptual formalisation, reference-algorithm demonstration, and future research-design work. At present no evidence shows that these indicators can perform high-precision real-time measurement of social health or collapse critical points.

**Methodological Disclaimer & Empirical Research Agenda**
> **Architectural positioning and the boundary of scientific truth-seeking:** the five-dimensional mathematical expressions and state-machine indicators defined in this chapter belong to the **"Conceptual & Architectural Reference Spec" of the Socio-Protocolics analysis engine and a future empirical-research agenda in computational social science**. The following distinctions are made explicit:
> 1. **Not Pseudo-Precision:** this architecture does not claim that the current fixed constants and static weightings (such as $\omega_i, \theta$) are universally invariant a-priori physical quantities; rather it provides a testable, iterable system-measurement topological framework for subsequent quantitative computational sociology, computational jurisprudence, and network-dynamics research;
> 2. **Engineering-implementation dependence:** actual engineering deployment depends on the long-term cleansing and calibration of multi-source open corpora (judicial judgments, policy drafts, cross-platform interaction flows), cross-lingual semantic-embedding representation alignment, and the empirical reverse-fitting of econometric panel data;
> 3. **Core value:** it establishes the architectural cornerstone for the leap from "qualitative sociological exclamation" to "formalised observability of distributed protocol dynamics (Observability)".

#### 8.3.1 Semantic Drift Index ($\text{SDI}$)

For the core baseline concept lexicon of the social contract $W_{\text{core}} = \{w_1, w_2, \dots, w_K\}$ (e.g., "justice, property rights, informed consent, jurisdiction, justifiable defence"):
For any concept $w \in W_{\text{core}}$, within a time window $t$, compute its centroid vector $\vec{v}_w(t) \in \mathbb{R}^d$ through a high-dimensional contextual semantic-embedding model (such as RoBERTa, BGE, or an open-source encoding model adapted with bidirectional sentence vectors):
$$\vec{v}_w(t) = \frac{1}{|C_w(t)|} \sum_{c \in C_w(t)} \text{Embed}(c, w)$$
where $C_w(t)$ is the non-empty corpus context sample set containing concept $w$; fix the model, coordinates, and sampling convention. When the centroid-vector norm is zero or the word sample is missing, it is recorded as missing and is not treated as zero drift; the reference code rejects zero-norm inputs.

> Actual measurement must check the anisotropy of the embedding space and, under a fixed model and same-distribution baseline, choose whitening or baseline calibration, reporting its impact. A single-word mutation is separately flagged as a local lexical review (`LOCAL_LEXICAL_ALERT`); a local hit by itself does not change the global colour. Only when the proportion of distinct trigger words to the core lexicon strictly exceeds the demonstration threshold ($|W_{\text{hit}}|/K>\tau_{\text{lex}}$) does the lexicon signal trigger the global red zone; other global indicators may still trigger zoning independently. The reference value $\tau_{\text{lex}}=0.15$ is an uncalibrated proportional threshold, not a multiple-testing correction, and does not guarantee control of the false-positive rate; if one wishes to claim error-rate control, one must separately supply the null hypothesis, the family of tests, the dependence conditions, and a correction or resampling method.

Define the cosine semantic-drift magnitude of a concept over a time interval:
$$\text{SDI}(w, t_0, t) = \frac{1}{2}\left(1 - \frac{\vec{v}_w(t_0) \cdot \vec{v}_w(t)}{\|\vec{v}_w(t_0)\|_2 \|\vec{v}_w(t)\|_2}\right) \in [0, 1]$$
Network-wide baseline mean semantic drift:
$$\overline{\text{SDI}}(t) = \frac{1}{|W_{\text{core}}|} \sum_{w \in W_{\text{core}}} \text{SDI}(w, t_0, t)$$
Define the semantic mutation acceleration:
$$a_{\text{drift}}(w, t) = \frac{\text{SDI}(w, t_0, t) - 2\text{SDI}(w, t_0, t-\Delta t) + \text{SDI}(w, t_0, t-2\Delta t)}{\Delta t^2}$$

Thereby define the **aggregate semantic mutation acceleration** (a scalar) over the core lexicon:
$$\overline{a}_{\text{drift}}(t) = \frac{1}{\lvert W_{\text{core}}\rvert}\sum_{w \in W_{\text{core}}} a_{\text{drift}}(w, t),$$
where words with fewer than three observed time points or with a zero centroid-vector norm do not enter the sum, and the number of missing words is reported separately. The reference code takes the mean over the core lexicon in a single observation, which is one realisation of this aggregate quantity; after changing $\Delta t$ or the sampling unit one must re-calibrate the threshold and create a new instance.> **Exploratory alert criterion:** the word-level semantic-mutation review (Word-level Tripwire) and the network-wide macroscopic aggregate mean (Aggregate Metric) are analytical outputs of different dimensions; an abnormal trigger on a specific local word is not diluted or masked by the global mean; when time-series observation has fewer than three time points, the acceleration is recorded as "to be tested" and is not inferred as absolutely zero change. After fixing the corpus sampling frame, model version, vector coordinates, and time scale, if $a_{\mathrm{drift}}(w,t)>\theta_{\mathrm{review}}$ and $\mathrm{SDI}(w,t_0,t)>0.40$, this may trigger `SEMANTIC_CHANGE_REVIEW`. The reference code takes $\theta_{\mathrm{review}}=0.25$, the time unit being one caller-fixed sampling period, and the acceleration unit being the reciprocal of the square of that time unit; changing the sampling unit requires re-calibrating the threshold and creating a new instance. The current threshold is only a demonstration value. The alert indicates that the semantic or corpus-distribution change needs review; it does not on that basis determine malicious "runtime type overloading". The review should include a same-distribution or time-shuffled no-change control, source-and-topic matching, resampling error bounds, and blind-rated semantic annotation; any judgement of maliciousness, the responsible subject, or legal justifiability requires separate independent evidence.

#### 8.3.2 Padding Bloat Ratio ($\text{PBR}$) and Bureaucratic Information Entropy

Let the document under test be $D$, and the candidate rhetorical lexicon be $\mathcal L_{padding}$. Whether a word is redundant depends on context; a lexicon hit does not equal zero meaning. Fix the tokenizer and its version, and denote $\text{TokenCount}(D)=|\text{Tokenize}(D)|$; $\text{Prune}(D,\mathcal L_{padding})$ returns the retained subsequence of the same token sequence, and TokenCount counts it directly without re-concatenating and re-tokenizing. Prune only deletes original tokens, and its output count must not exceed that of the non-empty input; rewriting or expansion is not pruning as defined here and must be listed as a separate operator. Cross-sample comparison must fix the tokenization convention, lexicon, and pruning configuration.

One may study dependency-tree pruning or a lexicon proxy, but it must be validated by blind-rated proposition equivalence, the target-audience comprehension-accuracy rate, and execution-error testing; negatives, exceptions, rights, and procedural safeguards must not be lost through text shortening.

Define the padding bloat ratio:
$$\text{PBR}(D) = 1 - \frac{\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))}{\text{TokenCount}(D)}$$
After the original document is tokenized and fixed, and before pruning, let $V=V(D)$ be the set of distinct tokens that actually appear in the document, $|V|$ its size, and $P(w)$ the occurrence count of token $w$ divided by the total original token count; this is not an external total vocabulary nor the post-pruning vocabulary. Combining this word-frequency distribution, compute the document's normalized Shannon entropy:

$$
H_{\text{norm}}(D)=-\frac{\sum_{w\in V}P(w)\log_2P(w)}{\log_2|V|}\quad(|V|>1);\qquad H_{\text{norm}}(D)=0\quad(|V|=1).
$$

Only a non-empty document can be computed; an empty document is treated as missing data. The lexicon-count reference implementation is not equivalent to lossless semantic pruning.

Payload-to-Noise Ratio ($\text{PNR}$):
$$\text{PNR}(D) = \frac{1 - \text{PBR}(D)}{\text{PBR}(D) + \epsilon} \cdot H_{\text{norm}}(D)$$
where the stabilising term $\epsilon=1\times10^{-6}$ is used only in the PNR denominator and does not change the PBR definition.
**PNR range and numerical sensitivity:** when $PBR\in[0,1]$, $H_{\text{norm}}\in[0,1]$, and $\epsilon>0$, we have $0\le PNR\le1/\epsilon$; the current stabilising term gives an upper bound of $10^6$, and PNR is not a score normalised to $[0,1]$. When $PBR=0$, $PNR=H_{\text{norm}}/\epsilon$: it takes $10^6$ when entropy is 1, and still takes 0 when a single repeated word drives entropy to 0. Near zero padding, the value may be dominated mainly by the stabilising term and the word-frequency distribution; this does not thereby prove that semantic information is valid, comprehension is smooth, or the document is healthy, nor may one, solely on the strength of a large value, declare a statistical outlier or error. The statistical-use and sensitivity requirements are given in §8.5.1.

> **Exploratory zoning criterion:** $PBR>0.65$ and $PNR<0.20$ trigger a yellow-zone example marker, and $PBR>0.85$ triggers a red-zone example marker. They do not prove comprehension failure or that actual throughput drops to zero; the values in historical scenarios are merely hypothetical inputs.

#### 8.3.3 Syscall Impedance & Rejection Rate ($\text{SIR}$)

Let the sample set of userland inbound demands be $\mathcal{U} = \{u_1, u_2, \dots, u_M\}$ (covering real civil demands such as labour-capital disputes, contract performance, property-right confirmation, and logistics access).
Let the kernel's exported syscall interface table be $\mathcal{K} = \{k_1, k_2, \dots, k_N\}$ (constitution, statutes, formal administrative-approval entries).
Compute the minimum manifold projection residual of the demand vectors onto the legal interfaces (Projection Residual):

$$
\bar d_{\text{norm}}=\frac1M\sum_{i=1}^M\min_j\frac{1-\cos(\vec E(u_i),\vec E(k_j))}{2}.
$$

Here the normalised cosine distance, consistent with the reference code, is used explicitly. Both sample sets must be non-empty, lie in the same vector space, and have non-zero norms; missing or invalid inputs are not scored. Define the rejection rate in combination with the (stratified) application records. One must first state the conventions for application attempts, successful registration, procedural non-acceptance, substantive rejection, withdrawal, and overdue non-handling; the missing mechanism for unregistered parties is estimated separately.
$$\text{SIR} = \alpha \cdot \bar{d}_{\text{norm}}(\mathcal{U}, \mathcal{K}) + (1 - \alpha) \cdot R_{\text{drop}} \in [0, 1]$$
where $\bar{d}_{\text{norm}}$ is the average normalised semantic distance between demands and existing legal interfaces, $R_{\text{drop}}$ is the actual case-filing / approval rejection rate, and the weight $\alpha \in [0, 1]$ (baseline $\alpha=0.50$). This decoupled weighted form avoids the measurement loophole that "when a demand coincides literally with a statute ($d=0$) yet meets a 100% rejection, the multiplicative impedance is zeroed out".
One should record separately the application-registration attempts, successful registrations, procedural non-acceptances, substantive rejections, withdrawals, and overdue non-handlings, and state the sample coverage and the estimation method for unrecorded parties. The exploratory rejection rate must be stratified by ex-ante verifiable application validity, dispute type, and procedural stage, and one cannot equate lawfully rejecting an invalid application with institutional blockage. The semantic distance and the stratified rejection rate may be retained as independent observational features; before external-validity testing is completed, one must not interpret their weighted value as the closing of a legal access channel or the inevitable emergence of a shadow economy.

#### 8.3.4 MITM Polarizing Metric ($\text{MPM}$)

In the sample of a specified information-transmission topology graph $G = (V, E)$, fix in advance the encoding unit, observation window, and verifiable-feedback criterion; mutually exclusively encode the classified traffic into the following two categories, using the same measurement unit; traffic whose category cannot be confirmed is recorded as missing, with the classification coverage rate reported separately. The TCP/UDP subscripts are only mechanism-analogy labels retained by this book; they do not indicate the actual transport-protocol type, nor do they pre-judge the truth or falsity of content, the degree of emotion, or the good or evil of the subject:
- $B_{\text{TCP}}$ (traceable-feedback traffic): within the specified window there exists a response and acknowledgement loop conforming to the encoding rules; having a receipt does not mean the content is true, the organisation is reliable, or the subject is benign; guard against performative ACKs (Performative ACK): a purely formalised receipt that is not accompanied by verifiable resource or state delivery is weighted as 0 in the $B_{\text{TCP}}$ measurement, and only those with verifiable physical delivery or closed-loop feedback count as valid $B_{\text{TCP}}$;
- $B_{\text{UDP}}$ (traffic with no traceable feedback observed): under the same window and encoding rules, no such loop is found; normal notices and announcements may also fall into this category, and one cannot directly infer malicious manipulation or emotional polarisation from the classification.

Define the betweenness centrality of the main gateways and intermediary-review / opinion-leader nodes:
$$C_B(v)=\sum_{\substack{s,t\in V\setminus\{v\}\\s\ne t,\ \sigma_{st}>0}}\frac{\sigma_{st}(v)}{\sigma_{st}}.$$
Under the same graph direction, weights, and shortest-path convention, predefine the gateway subset $V_{\mathrm{gatekeeper}}\subseteq V$; unreachable node pairs do not enter the above sum. Define the following structural proxy that continues to use the name "hijacking coefficient"; the name does not constitute malice identification:
$$\text{MPM}(G) = \left(\frac{\sum_{v \in V_{\text{gatekeeper}}} C_B(v)}{\sum_{u \in V} C_B(u)}\right) \cdot \left(1 - \frac{B_{\text{TCP}}}{B_{\text{TCP}} + B_{\text{UDP}}}\right)$$
> **Exploratory criterion:** MPM is an exploratory structural statistic under a given topology graph and traffic-classification rule; one must predefine directedness, weights, and the two-way-feedback proxy; $\text{MPM} > 0.70$ is an exploratory pre-review line for topological-structure anomaly, and $\text{MPM} > 0.85$ is a demonstration red-zone direct-review line; they do not on that basis directly determine subjective manipulation, malice, or group polarisation. Betweenness share and one-way traffic cannot alone identify polarisation or factual bus blockage; when the total betweenness or total traffic is zero it is recorded as missing, and separate annotation and result verification are required.

#### 8.3.5 System Health Index ($\text{SHI}$)

Define the comprehensive deadlock-risk score $\mathcal{R}_{\text{deadlock}} = \omega_1 \overline{\text{SDI}} + \omega_2 \text{PBR} + \omega_3 \text{SIR} + \omega_4 \text{MPM} \in [0, 1]$ (where the normalised baseline weights are $\omega = (0.30, 0.25, 0.25, 0.20)$), mapped through a Sigmoid function with sensitivity gain $k = 5.0$ and steady-state bias $\omega_0 = 2.50$ (corresponding to the demonstration risk midpoint $\tau_0 = 0.50$, since $k \cdot \tau_0 = 5.0 \times 0.50 = 2.50$) to the global health-index:
$$\text{SHI} = \frac{1}{1 + \exp\left(-\left(\omega_0 - k \cdot \mathcal{R}_{\text{deadlock}}\right)\right)} = \frac{1}{1 + \exp\left(-\left(2.50 - 5.0 \sum_{i=1}^4 \omega_i X_i\right)\right)}$$
The demonstration zoning and direct-trigger conditions jointly determine the reference code's research flags:
- 🟢 **Green:** neither the yellow- nor red-zone demonstration conditions are triggered; does not indicate real-world health or that consensus has formed;
- 🟡 **Yellow:** the composite score or a single-item condition triggers review; one must check the model, samples, and task results;
- 🔴 **Red:** the composite score falls below the demonstration threshold or a direct condition triggers; does not prove irreversible avalanche or real-world collapse. The colour precedence is red, yellow, green; the specific rules are in the code; the thresholds must be independently calibrated.

**Quick reference of the zoning rules:** the table below maps item by item to §8.4; independent triggers are combined by "or", and those marked "hold simultaneously" are a joint condition; judgement proceeds in red, yellow, green order. All thresholds serve only uncalibrated research demonstration and generate no physical-intervention authorisation or health certification.

| Research zone | Trigger condition |
| :--- | :--- |
| Red zone | $SHI<0.45$, or $PBR>0.85$, or $SIR>0.85$, or $MPM>0.85$, or $\lvert W_{\mathrm{hit}}\rvert/K>\tau_{\mathrm{lex}}$, or the aggregate acceleration is known and both $\overline{a}_{\mathrm{drift}}>0.25$ and $\overline{SDI}>0.40$ hold simultaneously |
| Yellow zone | provided the red zone is not triggered, any one of the following: $SHI<0.75$; both $PBR>0.65$ and $PNR<0.20$ hold simultaneously; $SIR>0.65$; $MPM>0.70$ |
| Green zone | none of the above red- or yellow-zone conditions is triggered; does not indicate real-world health |

Here $K$ is the word count of a fixed non-empty core lexicon, and $W_{\mathrm{hit}}$ is the set of trigger words explicitly passed in this run, deduplicated and belonging to that lexicon; a duplicate list is rejected by the code. $\tau_{\mathrm{lex}}$ corresponds to the construction parameter `lexical_alert_ratio_threshold`, default 0.15; record the measurement configuration when modifying it; the remaining tabulated values correspond to the current reference implementation. Each inequality is a strict comparison as tabulated; equality with a boundary does not satisfy that item's condition, but may still satisfy other conditions; an unknown acceleration only skips the corresponding acceleration condition and does not block the judgement of other complete inputs. The single-word trigger list and the aggregate acceleration are two independent paths and must not be mixed.

<a id="legacy-v11-1-sec-8-3"></a>
<a id="sec-8-4"></a>

### 8.4 Algorithm Execution Flow and Engineering Reference-Implementation Architecture (Research Reference Implementation & Pseudo-Code)

```python
"""
Socio-Radar Engine: Uncalibrated Research Flags
Research Reference Implementation in Python 3.10+ / NumPy; not calibrated.
非物理熔断、非自动授权、非健康认证，仅研究复核；本模块没有执行干预接口。
Note: Input embeddings are assumed to be isotropy-calibrated (e.g., whitened).
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import numpy as np


@dataclass(frozen=True)
class SocioMetricSnapshot:
    timestamp: float
    semantic_drift_index: float      # SDI in [0, 1]
    drift_acceleration: Optional[float]  # None until three time points
    padding_bloat_ratio: float       # PBR in [0, 1]
    payload_to_noise: float          # PNR
    syscall_impedance_rate: float    # SIR
    mitm_polarization_metric: float  # MPM in [0, 1]
    system_health_index: float       # Legacy SHI field: uncalibrated proxy, not health probability
    health_zone: str                 # Legacy zone field: research flags, not certification
    local_lexical_alert: bool = False
    semantic_review_words: Tuple[str, ...] = ()
    drift_acceleration_ready: bool = False
    reference_version: str = field(default="v11.2-research-1", init=False)
    model_version: Optional[str] = None
    measurement_profile_id: Optional[str] = None
    input_provenance: Tuple[Tuple[str, str], ...] = ()
    missing_metadata: Tuple[str, ...] = ()
    calibration_status: str = field(default="uncalibrated", init=False)
    research_only: bool = field(default=True, init=False)
    provenance_verified: bool = field(default=False, init=False)

    @property
    def research_score(self) -> float:
        return self.system_health_index

    @property
    def research_zone(self) -> str:
        return self.health_zone


class SocioRadarEngine:
    def __init__(
        self,
        core_lexicon: List[str],
        padding_lexicon: List[str],
        weights: Tuple[float, float, float, float] = (0.30, 0.25, 0.25, 0.20),
        baseline_bias: float = 2.50,
        gain_k: float = 5.0,
        sample_interval: float = 1.0,
        lexical_alert_ratio_threshold: float = 0.15,
        drift_acceleration_threshold: float = 0.25
    ):
        weights_array = np.asarray(weights, dtype=float)
        if (weights_array.shape != (4,) or not np.all(np.isfinite(weights_array))
                or np.any(weights_array < 0) or not np.isclose(weights_array.sum(), 1.0)):
            raise ValueError("weights must be four finite nonnegative values summing to 1")
        if not np.isfinite(baseline_bias) or not np.isfinite(gain_k) or gain_k <= 0:
            raise ValueError("bias must be finite and gain_k finite and positive")
        if not np.isfinite(sample_interval) or sample_interval <= 0:
            raise ValueError("sample_interval must be finite and positive")
        if not np.isfinite(lexical_alert_ratio_threshold) or not 0 < lexical_alert_ratio_threshold <= 1:
            raise ValueError("lexical_alert_ratio_threshold must be in (0, 1]")
        if not np.isfinite(drift_acceleration_threshold) or drift_acceleration_threshold < 0:
            raise ValueError("drift_acceleration_threshold must be finite and nonnegative")
        self.sample_interval = float(sample_interval)
        self.lexical_alert_ratio_threshold = float(lexical_alert_ratio_threshold)
        self.drift_acceleration_threshold = float(drift_acceleration_threshold)
        if (not core_lexicon or any(not isinstance(w, str) or not w for w in core_lexicon)
                or len(set(core_lexicon)) != len(core_lexicon)):
            raise ValueError("core_lexicon must contain unique nonempty word identifiers")
        self.core_lexicon = tuple(core_lexicon)
        self.baseline_unit: Optional[np.ndarray] = None
        self.padding_lexicon = set(padding_lexicon)
        self.w1, self.w2, self.w3, self.w4 = weights
        self.w0 = baseline_bias
        self.gain_k = gain_k
        self.history_sdi: List[float] = []
        self.history_word_sdi: List[np.ndarray] = []
        self.latest_word_reviews: Tuple[str, ...] = ()

    @staticmethod
    def _unit_rows(value: np.ndarray) -> np.ndarray:
        value = np.asarray(value, dtype=float)
        if value.ndim != 2 or 0 in value.shape or not np.all(np.isfinite(value)):
            raise ValueError("embeddings must be a nonempty finite 2-D matrix")
        norms = np.linalg.norm(value, axis=1, keepdims=True)
        if not np.all(np.isfinite(norms)) or np.any(norms == 0):
            raise ValueError("embedding row norms must be finite and nonzero")
        return value / norms

    @staticmethod
    def _ratio(value: float, name: str) -> float:
        if not np.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(name + " must be finite and in [0, 1]")
        return float(value)

    def compute_semantic_drift(
        self,
        embeddings_t0: np.ndarray,   # Shape: (K, D), isotropy-calibrated
        embeddings_t: np.ndarray     # Shape: (K, D), isotropy-calibrated
    ) -> Tuple[float, Optional[float]]:
        """Calculates cosine semantic drift and second-order acceleration.
        调用方须先在同分布语料上完成向量空间去均值白化（Whitening）或基线校准。
        """
        norm_t0 = self._unit_rows(embeddings_t0)
        norm_t = self._unit_rows(embeddings_t)
        if norm_t0.shape != norm_t.shape or norm_t0.shape[0] != len(self.core_lexicon):
            raise ValueError("paired SDI matrices must match shape and core_lexicon length K")
        if self.baseline_unit is not None and not np.array_equal(norm_t0, self.baseline_unit):
            raise ValueError("SDI baseline/coordinate profile changed; start a new engine")
        self.baseline_unit = norm_t0.copy()
        cos_sim = np.sum(norm_t0 * norm_t, axis=1)
        per_word_sdi = 0.5 * (1.0 - np.clip(cos_sim, -1.0, 1.0))
        mean_sdi = float(np.mean(per_word_sdi))
        
        self.history_word_sdi.append(per_word_sdi)
        self.history_sdi.append(mean_sdi)
        
        if len(self.history_word_sdi) >= 3:
            word_accel = (
                self.history_word_sdi[-1]
                - 2.0 * self.history_word_sdi[-2]
                + self.history_word_sdi[-3]
            ) / (self.sample_interval ** 2)
            a_drift = float(np.mean(word_accel))
            mask = (word_accel > self.drift_acceleration_threshold) & (per_word_sdi > 0.40)
            self.latest_word_reviews = tuple(w for w, hit in zip(self.core_lexicon, mask) if hit)
        else:
            a_drift = None
            self.latest_word_reviews = ()
            
        return mean_sdi, a_drift

    def compute_padding_bloat(self, document_tokens: List[str]) -> Tuple[float, float]:
        """Lexicon-only PBR proxy; must be paired with downstream blind task comprehension tests."""
        total_tokens = len(document_tokens)
        if total_tokens == 0:
            raise ValueError("an empty document is missing data, not healthy zero padding")
        padding_tokens = sum(1 for tok in document_tokens if tok in self.padding_lexicon)
        pbr = padding_tokens / total_tokens
        
        _, counts = np.unique(document_tokens, return_counts=True)
        probs = counts / total_tokens
        shannon_entropy = -np.sum(probs * np.log2(probs))
        norm_entropy = float(shannon_entropy / np.log2(len(counts))) if len(counts) > 1 else 0.0
        
        pnr = ((1.0 - pbr) / (pbr + 1e-6)) * norm_entropy
        return float(pbr), float(pnr)

    def compute_syscall_impedance(
        self,
        demand_embeds: np.ndarray,   # Shape: (M, D) - userland demands
        syscall_embeds: np.ndarray,  # Shape: (N, D) - exported legal syscalls
        rejection_rate: float,
        alpha: float = 0.50
    ) -> float:
        """Measures impedance with decoupled semantic distance and rejection rate."""
        rejection_rate = self._ratio(rejection_rate, "rejection_rate")
        alpha = self._ratio(alpha, "alpha")
        u_norm = self._unit_rows(demand_embeds)
        k_norm = self._unit_rows(syscall_embeds)
        if u_norm.shape[1] != k_norm.shape[1]:
            raise ValueError("demand and interface embeddings must share a feature space")
        cos_dists = 0.5 * (1.0 - np.clip(u_norm @ k_norm.T, -1.0, 1.0))
        mean_min_dist = float(np.mean(np.min(cos_dists, axis=1)))
        sir = float(np.clip(alpha * mean_min_dist + (1.0 - alpha) * rejection_rate, 0.0, 1.0))
        return sir

    def evaluate_research_flags(
        self,
        sdi: float,
        a_drift: Optional[float],
        pbr: float,
        pnr: float,
        sir: float,
        mpm: float,
        timestamp: float,
        word_reviews: Tuple[str, ...] = (),
        *,
        model_version: Optional[str] = None,
        measurement_profile_id: Optional[str] = None,
        input_provenance: Tuple[Tuple[str, str], ...] = ()
    ) -> SocioMetricSnapshot:
        """仅研究复核；非物理熔断、非自动授权、非健康认证。来源声明不等于已核验。"""
        for name, value in (("sdi", sdi), ("pbr", pbr), ("sir", sir), ("mpm", mpm)):
            self._ratio(value, name)
        if (a_drift is not None and not np.isfinite(a_drift)) or not np.isfinite(timestamp):
            raise ValueError("observed acceleration and timestamp must be finite")
        if any(w not in self.core_lexicon for w in word_reviews):
            raise ValueError("review words must belong to the bound core lexicon")
        for name, value in (("model_version", model_version),
                            ("measurement_profile_id", measurement_profile_id)):
            if value is not None and (not isinstance(value, str) or not value.strip()):
                raise ValueError(name + " must be a nonempty identifier or None")
        input_provenance = tuple(input_provenance)
        if any(not isinstance(pair, tuple) or len(pair) != 2
               or pair[0] not in ("SDI", "PBR", "SIR", "MPM")
               or not isinstance(pair[1], str) or not pair[1].strip()
               for pair in input_provenance):
            raise ValueError("provenance must contain (proxy name, nonempty source identifier) pairs")
        sources = dict(input_provenance)
        if len(sources) != len(input_provenance):
            raise ValueError("provenance must not repeat a proxy name")
        missing_metadata = tuple(
            name for name, value in (("model_version", model_version),
                                     ("measurement_profile_id", measurement_profile_id))
            if value is None
        ) + tuple(name + "_source" for name in ("SDI", "PBR", "SIR", "MPM") if name not in sources)
        word_reviews = tuple(word_reviews)
        if len(set(word_reviews)) != len(word_reviews):
            raise ValueError("review words must be unique; duplicates cannot inflate the hit ratio")
        if not np.isfinite(pnr) or pnr < 0:
            raise ValueError("pnr must be finite and nonnegative")
        r_deadlock = self.w1 * sdi + self.w2 * pbr + self.w3 * sir + self.w4 * mpm
        logit = self.w0 - self.gain_k * r_deadlock
        shi = 1.0 / (1.0 + np.exp(-np.clip(logit, -709.0, 709.0)))
        
        local_lexical_alert = bool(word_reviews)
        lexical_hit_ratio = len(word_reviews) / len(self.core_lexicon)
        
        # 仅当触发词比例跨越阈值或全局宏观指标越界时，才触发全局 RED 研究复核标记
        critical_review_trigger = (
            pbr > 0.85 or
            sir > 0.85 or
            lexical_hit_ratio > self.lexical_alert_ratio_threshold or
            (a_drift is not None and a_drift > self.drift_acceleration_threshold and sdi > 0.40) or
            mpm > 0.85
        )
        if critical_review_trigger or shi < 0.45:
            zone = "RED (Uncalibrated Research Flag)"
        elif (shi < 0.75 or (pbr > 0.65 and pnr < 0.20)
              or sir > 0.65 or mpm > 0.70):
            zone = "YELLOW (Uncalibrated Research Flag)"
        else:
            zone = "GREEN (Below Illustrative Thresholds; Not Health Certification)"
            
        return SocioMetricSnapshot(
            timestamp=timestamp,
            semantic_drift_index=sdi,
            drift_acceleration=a_drift,
            local_lexical_alert=local_lexical_alert,
            semantic_review_words=word_reviews,
            drift_acceleration_ready=a_drift is not None,
            padding_bloat_ratio=pbr,
            payload_to_noise=pnr,
            syscall_impedance_rate=sir,
            mitm_polarization_metric=mpm,
            system_health_index=float(shi),
            health_zone=zone,
            model_version=model_version,
            measurement_profile_id=measurement_profile_id,
            input_provenance=input_provenance,
            missing_metadata=missing_metadata
        )

    def evaluate_system_health(self, *args, **kwargs) -> SocioMetricSnapshot:
        """兼容旧入口；返回相同的未校准研究标记，不提供健康认证或干预授权。"""
        return self.evaluate_research_flags(*args, **kwargs)
```

Calling contract for the word-level and aggregate outputs: first use the same instance to obtain `sdi, a = engine.compute_semantic_drift(baseline, current)`, then explicitly pass this observation's `word_reviews=engine.latest_word_reviews` to `evaluate_research_flags` (the old entry `evaluate_system_health` only delegates for compatibility). The zoning function does not silently read the residual flag from the previous observation; the trigger-word list is written into `semantic_review_words` and is not diluted by the mean. With fewer than three time points, `a=None` and `drift_acceleration_ready=False`; this does not prevent other already-complete inputs from raising independent research alerts. The lexicon order and baseline must be fixed; when the version, coordinates, or sampling time-scale changes, create a new instance; the model version and source are declared by the caller and retained with the snapshot, and metadata declaration is not equated with automatic verification. A local hit below the proportion threshold remains visible but does not by itself change the global colour; equality with 0.15 does not satisfy the strict greater-than threshold. A duplicate word list is rejected, avoiding inflation of the ratio.



**Concept labels and field mapping:** the `SEMANTIC_CHANGE_REVIEW` of §8.3.1 denotes the word-level review condition; the hit list is saved by the computation interface in `latest_word_reviews`, and after the caller explicitly passes it into `word_reviews` it enters the snapshot's `semantic_review_words`; `LOCAL_LEXICAL_ALERT` corresponds to `local_lexical_alert=bool(word_reviews)` in the snapshot. Both uppercase labels are concept names, not additional code event fields, nor are they equal to the global red zone; the global result is read from `research_zone`.

**Baseline and history-record contract:** the current code strictly compares the normalised baseline matrix with `np.array_equal`, requiring the same instance to reuse a fixed baseline; when recomputation or a storage-precision change causes inconsistency, first check the measurement configuration rather than defaulting to relaxing the tolerance. If a tolerance scheme is designed separately, one must fix the initial baseline, declare the error bound, and test accumulated drift, and cannot simply replace it with the default `allclose`. `history_sdi` retains the aggregate-SDI history for diagnostics, and `history_word_sdi` is used for word-level acceleration; zoning still reads only the explicit inputs. The in-memory history is not an independent evidentiary record or a persistent audit log.

**Input-source and research-output contract:** §8.4 is the numerical reference core, not an end-to-end system for corpora, topology, and causal identification. Vector calibration, traffic encoding, graph construction, and source authenticity are the responsibility of an independent measurement pipeline.

| Interface item | Behaviour of this implementation | External measurement and verification obligation |
| :--- | :--- | :--- |
| SDI / PBR / SIR | computes proxies from given vectors, tokens, and stratified rejection rates; does not check the authenticity of the original corpus | fix model, tokenization, sampling, application validity, time unit, and error; retain input artifacts and sources |
| PBR / PNR pairing | `compute_padding_bloat` returns a two-tuple from the same token sequence; the zoning interface only validates each scalar's legal range and does not verify same-source or complete pairing | use this two-tuple together, record the document, tokenization / pruning configuration, and $\epsilon$; imported externally must be recomputed or independently checked. The necessary numerical bound defined is $0\le PNR\le(1-PBR)/(PBR+\epsilon)$; satisfying this bound still does not prove same-source; one cannot reverse-engineer the entropy from the passed score to replace verification. The related artifacts are retained with the source pointed to by `PBR_source` |
| MPM | consumes only the external `mpm` scalar and validates [0,1]; does not implement graph construction, betweenness, or traffic classification | provide graph version, direction / weights, gateway set, betweenness computation records, feedback-encoding window, traffic unit, and classification coverage; when total betweenness or total traffic is zero, record as missing, not 0 |
| Numerical missing | the computation interface rejects empty, non-finite, or out-of-range required inputs; does not output SHI for incomplete rows | the caller lists missing records and reasons for non-computation separately; does not rewrite "not computed" as green or zero risk |
| Version and source | the snapshot retains `reference_version`, the caller-declared `model_version`, `measurement_profile_id`, and the four `input_provenance` items | the measurement-configuration identifier should point to corpus, model coordinates, lexicon, time-scale, and encoding rules; the source identifier should be traceable to the input artifact and cannot be only a conclusion |
| Metadata missing and credibility | unprovided items are listed in `missing_metadata`; `provenance_verified=False`, not automatically turned true by filling a string | an independent verifier checks the declaration; complete metadata does not equal correct values, valid proxies, or completed empirical verification |
| Research status and compatibility fields | `calibration_status=uncalibrated`, `research_only=True` are output with the read-only snapshot; read `research_score` / `research_zone` first | `system_health_index` / `health_zone` retain only the compatibility name; the score is not a health probability and the colour is not an official certification |

**Execution-authority isolation:** the research snapshot has no action, punished subject, or execution credential; the reference core is not wired to tools, network control, or physical-intervention interfaces. Any external access that directly replaces colour, threshold, or manual stamping with intervention authorisation violates this norm. Anything that needs to execute must separately state the authorising subject, scope of authority, validity period, factual evidence, remedy, and a revertible plan; the related authorisation and the net intervention benefit cannot be generated from the radar score. Record the execution decision and its independent basis so a reviewer can trace whether automatic authorisation has been smuggled in.

<a id="legacy-v11-1-sec-8-4"></a>
<a id="sec-8-5"></a>

### 8.5 The Operationalization Protocol & Quantitative Operators

**Normative Spec.**
The following proposes candidate research protocols for reproducible measurement. Formal empirical work must first fix the corpus, model version, tokenization, annotation, and error evaluation; the semantic fidelity of Prune and the external validity of the indicators still require independent verification, and one cannot pre-claim applicability to arbitrary historical or contemporary samples.

#### 8.5.1 Rhetorical Lexicon and Pruning Proxy Operator (PBR & SNR/PNR Research Operator)

For the regulation document, policy file, or administrative-approval draft $D$ under test:
- Use a public model and candidate pruning operators to extract task information; "losslessness" must be validated by independent annotation, retaining negatives, exceptions, rights, and procedural safeguards. The lexicon count is only a reference proxy and cannot be directly treated as true semantic redundancy. To prevent an acting subject from hollowing out the `PBR` indicator through "adversarial paraphrasing" (rewriting shirking documents using everyday vocabulary while disabling the black-jargon lexicon), the text-pruning operator must be jointly validated with the **downstream audience blind-test task-parsing accuracy** (whether an executor not involved in drafting can accurately identify the responsible subject, deadline, action, and remedy interface from the text). At the same time, in the empirical testing of the language protocol, `SP-RFC-002` (concept naming) and `SP-RFC-003` (cross-context textual stability) must be validated in a decoupled manner: the former must state in advance the object of estimation — "the overall intervention effect of naming and compression" may compare a named scheme with a descriptive scheme, but the conclusion must be confined to this combination; if one estimates the independent effect of naming, one should distinguish length, content, familiarity, and training through matching or a factorial design, avoiding conflating the mediation effect with confounders, and separately measure retrieval, correct citation, and collaboration. The latter fixes the text version, audience distribution, and interpretation task, and separately tests the version identifier and the local interpretation mechanism, reporting the explained variance, task performance, predetermined improvement amount, and error per §2.3's local hypothesis. The results of the two experiments cannot substitute for each other.
- Following the same tokenization, lexicon, and counting convention of `§8.3.2`, define the padding bloat ratio ($\text{PBR}$) and the payload-to-noise ratio ($\text{PNR}$):
  $$\text{PBR}(D) = 1 - \frac{\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))}{\text{TokenCount}(D)}, \quad \text{PNR}(D) = \frac{1 - \text{PBR}(D)}{\text{PBR}(D) + \epsilon} \cdot H_{\text{norm}}(D)$$
  where the entropy-free simplified signal-to-noise ratio is $\text{SNR}(D) = \frac{\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))}{\text{TokenCount}(D) - \text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))}$. When the denominator is zero, no finite value is reported; an empty document is recorded as missing. SNR is an entropy-free text-length ratio; PNR additionally contains the entropy weight and the $\epsilon$ stabilising term, and the two cannot be interchanged, nor are they the physical-channel signal-to-noise ratio.
- **Statistical use and sensitivity of PNR:** retain the raw PNR, PBR, entropy, $\epsilon$, tokenization, and pruning configuration; distinguish missing data, computable zero values, and large values caused by near-zero padding. Before entering regression or other statistical models, fix the objective, preprocessing rules, and comparison scheme, and report whether the conclusion is stable under reasonable candidate $\epsilon$; one does not automatically flag a value as anomalous merely because it is large. $\log(1+PNR)$, truncation, or scaling are only comparable candidate statistical variables, to be separately named, with the selection rationale recorded and raw values retained; if processing parameters are estimated from data, use only the training material and do not repeatedly optimise on the held-out results. The processed values must not directly replace the reference engine's raw PNR input nor reuse the unconverted zoning thresholds; a separate measurement configuration must be set and re-evaluated. This section does not uniformly mandate a transformation, nor does it thereby alter the existing indicator definitions or thresholds.
- **Exploratory zoning rule:** consistent with the reference code, $PBR>0.65$ and $PNR<0.20$ is one of the yellow-zone conditions, and $PBR>0.85$ is a red-zone direct-trigger condition. The thresholds are not yet calibrated, and one cannot derive from the Shannon-capacity formula that the variance index of grassroots comprehension diverges; this must be separately validated by task-completion rate, comprehension error, and latency. Calibration must include blind-rated proposition equivalence, the target-audience comprehension-accuracy rate, and execution error; word-frequency entropy alone cannot substitute for effective meaning.

#### 8.5.2 Perplexity & Token-Length Benchmark for Language-Bus Compilation Impedance

For the upgrade of a civilisation's underlying language bus (e.g., the transition from literary Chinese to vernacular):
- **Standard evaluation benchmark:** select the parallel corpus set $\{S_{\text{classical}}^{(k)}, S_{\text{vernacular}}^{(k)}\}_{k=1}^N$ expressing exactly the same mathematical / physical propositions from the 1859 Li Shanlan literary-Chinese translation *Daiwei Ji Shiji* (代微积拾级) and a **Republican-era / modern vernacular calculus textbook whose title and version must be specified in advance** (or a re-translation control of the same source, see `§2.4.1-A`).
- **Measurement indicators and proxy definition:** on a unified open-source base LLM, measure its perplexity ($\text{PPL}$) and token length per proposition, and construct the exploratory length-weighted perplexity ratio:
  $$\text{Impedance\_Ratio} = \frac{\sum_{k=1}^N \text{PPL}(S_{\text{classical}}^{(k)}) \times \text{Tokens}(S_{\text{classical}}^{(k)})}{\sum_{k=1}^N \text{PPL}(S_{\text{vernacular}}^{(k)}) \times \text{Tokens}(S_{\text{vernacular}}^{(k)})}$$
  This comparison uses, under a specific model and tokenizer, the product of perplexity and token length as an exploratory proxy; it is not equated with the total cross-entropy in information theory, nor can it be directly converted into the actual human reading and comprehension impedance; if one reports the total negative log-likelihood, one should sum over all propositions, i.e., $\sum_{k=1}^{N}\text{Tokens}(S^{(k)})\log\mathrm{PPL}(S^{(k)})$, and state the logarithm base. This draft retains the product convention only because it directly aligns with the same tokenizer, lexicon, and counting convention of §8.3.2 and can serve as a relative-ranking proxy for the same batch of parallel corpora under the specified model; this choice does not claim superiority over the total negative-log-likelihood convention, and the ranking consistency of the two conventions is left to subsequent research. Cross-genre comparison must strictly control proposition equivalence, the model's corpus-exposure bias, and the tokenization scale; human cognitive comprehension cost still requires independent behavioural-experiment testing. Cross-genre comparison must also separate at least four confounders: the stylistic difference between literary and vernacular Chinese, the content and difficulty of the English source *Elements of Analytical Geometry and of the Differential and Integral Calculus* by Loomis (1851) on which Li Shanlan relied, the historical evolution of terminology and notation, and the arithmetic-notation system composed of the heavenly stems and Chinese characters; before controls are applied, the perplexity difference cannot be attributed to the genre itself.
- **Experimental design and the hypothesis to be tested:** this item is a standard benchmark experiment design yet to be executed. The hypothesis predicts that literary Chinese has a significantly higher product of compilation perplexity and token length than vernacular Chinese on mathematical-logical and engineering-specification propositions; the specific ratio awaits reproducible evaluation under a standard parallel corpus and a specified open-source base model. This hypothesis is a **directional candidate prediction** that must be pre-registered before observation: the parallel-corpus list and its versions, the base model and tokenizer versions, the proposition-equivalence judgement rule, and the rejection criterion (including the allowed error range and the minimum sample size); this section follows the treatment convention of `§8.1` for uncalibrated scores and does not set a uniform threshold or uniform confidence level for all applications. Before a reproducible complete corpus list and run records are provided, it is not treated as an established measured conclusion; before controlling for the pre-training corpus's exposure bias toward modern vernacular, the result only represents the encoding impedance under the specified model and tokenizer, and does not equal the human reading and comprehension cost.

#### 8.5.3 Hierarchical Drift & End-to-End Validation

For the real administrative-document chain in which a central policy directive $T_0$ (centre) is issued level by level down to $T_1$ (province), $T_2$ (city), $T_3$ (county), $T_4$ (township):
- Extract the core execution-directive embedding vector $\mathbf{v}(T_i) \in \mathbb{R}^d$ of each level's document;
- Compute the adjacent semantic-distance proxy (not a direct estimate of the §3.1 serial traffic-loss rate):
  $$d_i=1-\cos(\mathbf v(T_{i-1}),\mathbf v(T_i))\in[0,2].$$
- The product of adjacent-level local similarities (only a path-deviation summary, not equal to end-to-end execution fidelity):
  $$p_{local}=\prod_{i=1}^n(1-d_i)=\prod_{i=1}^n\cos(\mathbf v(T_{i-1}),\mathbf v(T_i)).$$
> **Non-transitivity and applicability boundary:** the product of local similarities can be negative and is not a traffic-retention rate. Even if the head and tail vectors of a $0^\circ\to60^\circ\to0^\circ$ sequence coincide, the adjacent product is still only 0.25. One must independently test the head-to-tail direct similarity and the task-execution deviation, and cannot substitute the semantic distance into the loss parameter of §3.1 and then claim to have measured end-to-end throughput. Also note the scale difference: the $d_i=1-\cos\in[0,2]$ here is not normalised by $\frac{1-\cos}{2}$, differing in scale from the $\mathrm{SDI}\in[0,1]$ of `§8.3.1`, and cannot be directly substituted into the $[0,1]$-interval demonstration thresholds of this chapter.

<a id="sec-8-5-4"></a>
#### 8.5.4 Full Pre-Registration Worked Examples and Paired Discriminating-Prediction Comparisons

> **Positioning and evidence boundary of this section:** the two full numerical pre-registration worked examples (B-A / B-B) and the three paired discriminating-prediction comparisons (C1 / C2 / C3) below turn the testable programme of §8.1 into minimum effect size, power, sample size, and interval-style rejection conditions; they respond to the two criticisms that "the rejection conditions remain at a procedural template" and "there is a lack of distinguishable instances between the existing-theory prediction A and this book's prediction B". **All numerical values in this section are illustrative pre-registration parameters (illustrative) — not measured, not estimated values, not calibrated thresholds**; for formal pre-registration the executing researcher must replace the planned values, freeze the convention, and name the literature baseline. Each of this book's predictions B is a **to-be-tested empirical mechanism hypothesis and does not elevate to an established conclusion**, and the existing-theory prediction A is a refutable simplified statement and does not constitute a factual final judgement on the original text. The judgement follows interval-style rejection and a four-category judgement classification; it does not write "not statistically significant" as a refutation, nor optimises after the fact; the demonstration values serve only to show the accounting logic and do not thereby claim predictive power, and passing the automated gate does not mean the external empirical work is already complete. **Inflation-convention statement:** the "10% missing / invalid inflation" in the demonstration examples of this section uniformly adopts the multiplicative convention `×1.10` (adding a 10% buffer to the computed value), which is only a demonstration choice; for formal pre-registration one must freeze one of the multiplicative convention `×1.10` and the make-up convention `÷0.90` (`n/0.90`, i.e., making up to 100% valid sample size) and remain consistent throughout, without after-the-fact optimisation.

> **Numbering convention:** the internal sub-section numbers of each item in this section (such as 1.7, 2.1, 2.6) refer only to the corresponding sub-headings at the `######` level of this section; numbers with `§` point to the corresponding chapter of this whitepaper, as listed in each item's "corresponding clause and identity" line.

##### 8.5.4.1 Pre-Registration Worked Example B-A | SP-RFC-002 Naming and Common Identification

**Corresponding clause and identity:** SP-RFC-002 (§2.2), G002, §8.5.1. Claim identity: **empirical mechanism hypothesis** (does not elevate). Testing entry (§2.2): distinguish "the overall intervention effect of naming and compression" from "the independent naming effect", and pre-register the task, comparison object, main indicator, minimum meaningful improvement amount, and error requirement.

###### 1.1 Hypothesis and object of estimation

- Hypothesis ① (overall intervention): relative to the "description + uncompressed" control, the combination "stable shared name + compression" raises the downstream audience's blind-test parsing accuracy.
- Hypothesis ② (independent naming effect): holding text length / compression level fixed, "having a stable shared name" still raises parsing accuracy relative to "description only, no name".
- Object-of-estimation statement: the conclusion of Hypothesis ① is **confined to the "naming + compression" combination** and must not be extrapolated to the independent effect of naming; Hypothesis ② is the independent naming effect (§8.5.1). The two estimation results cannot substitute for each other.
- No conclusion beyond direction is presupposed: one does not claim that naming necessarily brings an absolute monopoly on the right of interpretation, nor claim that lacking a name means no remedy is possible (§2.2, case 2.2-A).

###### 1.2 2×2 factorial design and grouping

| | Compressed / short text `C=1` | Complete / long text `C=0` |
| :--- | :--- | :--- |
| Has stable shared name `N=1` | Cell ① (overall intervention) | Cell ② |
| No name, description only `N=0` | Cell ③ | Cell ④ (pure-description control) |

- **Orthogonalisation:** separate "naming" from "length / compression", satisfying §8.5.1's requirement to "distinguish length, content, familiarity, and training through matching or a factorial design, avoiding conflating the mediation effect with confounders".
- **Content equivalence:** the four cells express the same set of propositions, confirmed by a blind-rated proposition-equivalence test (the lower bound of rater agreement κ is frozen before observation); the length difference comes only from "redundancy removal" and "descriptive phrases" and does not change the proposition set.
- **Pairwise length matching (pre-registration verification item):** Cell ② (N=1,C=0) and Cell ④ (N=0,C=0), and Cell ① (N=1,C=1) and Cell ③ (N=0,C=1), must each undergo text-length matching (character / word count, convention frozen before observation); the tolerance and verification method are pre-registered; if the "stable shared name" is shorter than the "descriptive phrase", equal-length neutral padding is used to keep N and C orthogonal; if not satisfied, record "not applicable".
- **Randomisation and blinding:** executors are randomly assigned to cells; executors do not participate in drafting and do not know the research hypothesis; raters do not know the cell label; the analysis script is frozen before seeing the results.
- **Subjects and blind test:** target-audience executors not involved in drafting (§8.5.1 "executors not involved in drafting"); prior knowledge, education / resource / institutional background are stratified and randomised.

###### 1.3 Main / secondary indicators

- **Single main indicator:** downstream audience blind-test task-parsing accuracy, operationalised as the count of correctly identified items among 4 elements (responsible subject, deadline, action, remedy interface, §8.5.1) per executor, scored 0–4; the between-group mean difference is the effect size. **Convention statement (eliminating the "proportional accuracy / 0–4 count mean" convention slippage):** the "parsing accuracy" of §8.5.1 is proportional, while this example operationalises it with the 0–4 count mean; the two differ only by a constant factor of 1/4 (so `Δ_min=0.5` points = 12.5 percentage points of **per-element identification rate**); this example adopts the two-independent-sample mean-power formula by count mean; whether the normal approximation is feasible for the bounded discrete quantity 0–4, whether `σ=1.0` applies near the upper bound of the group mean, and the intra-cluster correlation of the same executor's 4 elements (handled with cluster-robust SE or stratification) must all be ratified by a pilot study and frozen before observation. This is a demonstration operationalisation and changes no existing numerical identity.
- **Stratified secondary indicators** (exploratory reporting only, no confirmatory inference, no after-the-fact optimisation): correct-identification time / retrieval time, accurate-citation rate, collaboration result (as listed in G002); proposition-equivalence blind rating; inter-rater agreement κ.
- **Indicators explicitly not used as criteria:** `PBR` / `PNR` / `H_norm` / `SDI` are not used as the main criteria of this example (they are the **uncalibrated** text proxies of §8.3.2 / §8.3.1, not the parsing accuracy of this task); if cited, one must note that they are uncalibrated.

###### 1.4 Δ_min, α, power (all illustrative pre-registration parameters, applicable only to this design)

- `Δ_min = 0.5` points (4-point scale, equivalent to 12.5 percentage points of element-identification rate) — **illustrative pre-registration parameter (illustrative)**, not a measured improvement amount, not an estimated value.
- `σ = 1.0` points — **demonstration planned standard deviation (illustrative)**; for formal pre-registration one must replace it with a pilot study or existing measurement and leave a trace; here it only shows that the formula can be substituted.
- `d = Δ_min/σ = 0.5` — illustrative.
- `α = 0.05` (two-sided), `power = 0.80` — **applicable only to this design**; no book-wide uniform α or uniform confidence level is set (§8.1 main text "Use limits on uncalibrated proxy scores"; this is the §8.5.2 statement adopting that convention).
- **Multiple comparisons:** the main indicator is "single"; the two main comparisons are tested in **stratified (fixed-order)** fashion — Hypothesis ① → Hypothesis ②, and only after ① is rejected by the interval style is ② tested; the family-wise error rate is controlled at 0.05, with no extra α allocation needed (G003, §2.3); secondary indicators are exploratory only, and after-the-fact optimisation is prohibited.

###### 1.5 Power calculation (formula + substitution + result + sample size; recomputed with Python)

**Formula (two independent samples, mean comparison):**

`n/组 = 2 (z_{1−α/2} + z_{1−β})² / d²`

**Substitution** (computed with Python `statistics.NormalDist.inv_cdf`):

| Quantity | Value |
| :--- | :--- |
| `z_{1−α/2}` (α=0.05 two-sided) | 1.959964 |
| `z_{1−β}` (power=0.80) | 0.841621 |
| `z_sum = 2.801585`; `z_sum²` | 7.848880 |
| `d = 0.5`; `d²` | 0.25 |

`n/组 = 2 × 7.848880 / 0.25 = 15.697760 / 0.25 = 62.791 → 63 (rounded up)`

**10% missing / invalid inflation:** `ceil(63 × 1.10) = 70` / cell.

**Sample size:** the 2×2 has 4 cells in total → total **70 × 4 = 280 executors** (illustrative pre-registration parameter, illustrative).

**Recheck:** `power = Φ(d√(n/2) − z_{1−α/2}) = Φ(0.5×√35 − 1.959964) = Φ(0.998076) = 0.8409 ≥ 0.80`.

**Conservatism note:** `n/组` is set to the stricter target of "any two-cell comparison" (the overall-intervention control of Hypothesis ①, and the fixed-length naming comparison of Hypothesis ②); after the main effect is pooled across the other factor, the effective `n = 2×70 = 140` / level, with a smaller SE, so the design is conservative.

**2×2 comparison and object-of-estimation mapping (pre-registration, avoiding the two objects substituting for each other):**
- The object of estimation `θ₁` of Hypothesis ① = Cell ①(N=1,C=1) − Cell ④(N=0,C=0), i.e., the **joint effect** of "naming + compression"; the conclusion is confined to this combination.
- The object of estimation `θ₂` of Hypothesis ② = Cell ②(N=1,C=0) − Cell ④(N=0,C=0) at the fixed `C=0` level, i.e., the simple effect of the "independent naming effect"; it may also be cross-checked at `C=1` by Cell ① − Cell ③, and one of them must be pre-registered as fixed for confirmation.
- Interaction term `N×C` = `(①−③) − (②−④)`: register its handling rule when it is uninterpretable or significant — no confirmatory inference, no rewriting of the joint effect as the independent naming effect on that basis, and if necessary record "not applicable" and report separately.
- Each of the two `θ` constructs a 95% CI and gives the rejection interval per the judgement table of B-A's §1.7; test in the fixed stratified order ① → ②; do not interpret a single `θ` as both objects of estimation simultaneously. This paragraph only clarifies the object of estimation and the comparison mapping, and does not change the interval-style rejection logic and the four-category judgement classification of B-A's §1.7 judgement table.

###### 1.6 Measurement tools and confounder control

- **Tools (frozen before observation):** text-material list and version, blind-test task sheet (4-element identification questions), scoring rules and rater-training script, tokenization / lexicon and counting convention (if measuring text proxies, follow the same convention of §8.3.2), randomisation seed, analysis-script hash.
- **Confounder control (§8.5.1 / G002 / §1.5 Group I):**
 - Content: blind-rated proposition equivalence; if it fails, the whole item is recorded as "not applicable";
 - Familiarity: pre-test stratified randomisation; prohibit using "existing name or case clue" to replace identification (§2.2, G002);
 - Training: unified training script and duration, consistent across the four cells;
 - Length: explicitly separated by the 2×2 factor; do not explain the effect afterwards by "text is shorter";
 - Education / resource / institution: stratified randomisation + pre-registered covariates; prohibit after-the-fact optimisation (§1.5 Group I).

###### 1.7 Rejection interval and judgement table (interval-style, not `p<0.05` style)

Pre-registered prediction range: improvement amount `θ ≥ Δ_min = 0.5` points (direction positive); construct the 95% CI of `θ`.

| Situation | Interval condition | Judgement (§1.5/§2.3 four categories) | Wording constraint |
| :--- | :--- | :--- | :--- |
| Improvement holds | 95% CI lower bound `≥ Δ_min` | the local prediction is "**not rejected**" within this design | do not write "has been verified / is supported" |
| Equivalent / narrowed | 95% CI falls entirely within `(−Δ_min, Δ_min)` (equivalence test holds) | **reject** / narrow the local prediction | "exclude the predetermined improvement with sufficient precision" |
| Reverse | 95% CI upper bound `< 0` | **reject** the local prediction; record that the bridging hypothesis needs recheck | do not elevate to the whole RFC being overturned |
| Insufficient precision | 95% CI crosses the `Δ_min` boundary, or CI half-width > pre-registered precision upper bound | **insufficient evidence** | a non-significant result is not by itself a refutation |
| Premise not established | proposition-equivalence blind test failed / κ below lower bound / randomisation or blinding broken | **not applicable** | do not make an interval judgement |
| Data missing | main-indicator missing rate > pre-registered upper bound and no pre-registered remedy rule | **missing** | do not merge into pass or fail |

The four-category judgement **must not be merged** (§1.5); "an unexecuted comparison is marked 'to be tested'".

###### 1.8 Time box and data freeze (illustrative pre-registration parameter, illustrative, applicable only to this design)

- **Freeze before observation:** factor-level definitions, text-material list and version, blind-test scoring rules, κ lower bound, randomisation / blinding, main indicator, `Δ_min`, `σ` planned value, `α` / `power`, sample size 280, stratified testing order, rejection interval, precision upper bound, missing-rate upper bound, analysis-script hash, data-freeze date.
- **Time box:** recruitment window ≤ 8 weeks; complete the frozen analysis within 4 weeks after data freeze; if the sample size is not reached by the window close, record "insufficient evidence" per the pre-registered rule, **do not extend the window to back-fill samples afterwards, do not optimise after the fact**.
- All times / quantities are illustrative pre-registration parameters, not measured, not calibrated thresholds.

##### 8.5.4.2 Pre-Registration Worked Example B-B | SP-RFC-004 Conditional Retention Rate of the Serial Compatibility Layer

**Corresponding clause and identity:** SP-RFC-004 (§3.1), G004, §1.5 Group II falsifiability criterion. Claim identity: **conditional model** (does not elevate). Model `η_n = ∏_{i=1}^{n}(1 − λ_i)` (§3.1); the geometric form requires the same rate, and the exponential upper bound requires a consistent positive lower bound; merely having positive per-layer loss is insufficient to guarantee exponential decay.

###### 2.1 Same-convention prerequisite checklist (any item not satisfied → record "not applicable" and trigger "build a separate model")

1. The same effective flow passes through `n` levels in series, serial, with no parallel bypass (§3.1).
2. Each level has no new output or recovery path (G004; §3.1).
3. The measurement unit is explicitly defined and kept consistent throughout (G004).
4. `λ_i` is defined as the conditional loss rate "relative to that level's input", not relative to the initial flow (§3.1).
5. The input, output, new, and recovery of each link are recorded independently (G004).
6. The throughput convention, boundary, and observation window are fixed in advance (§3.1).
7. Low-net-cost abstraction layers and privilege-rent-seeking compatibility layers are accounted separately (§3.1).
8. If a buffering level that bears the exception-handling function is removed, one must register a feasible alternative mechanism and exception-recovery performance, work-to-rule indicators, etc. (§3.1).
9. `n ≥ 4` itself is not a decay or collapse critical value (§3.1) — see B-B's §2.6.
10. The 8-percentage-point audit effect of Olken (2007) recounted in case 3.1-A is **not a layer-loss parameter** (G004) — see B-B's §2.6; this item only cites the convention already carried in the main text and does not make a factual final judgement.
11. **DGP three-layer assumptions (pre-registered, frozen before observation):**
 - **L1 flow topology:** the main design takes "the same effective flow passes through each level in series" (convention ②, consistent with §3.1 and the `M≥1509` of §2.2); convention ① "each level independently sampled, 4700 level-cells" is demoted to a **mutually exclusive alternative branch**, enabled only when through-chain data cannot be obtained; the two are **mutually exclusive and not additive**.
 - **L2 loss-correlation mechanism:** the main design declares "losses at each level are independent at the cell level, with no over-dispersion and no inter-layer common shock". If a common shock is detected (inter-layer loss positively correlated / cell-level frailty), this design records "**not applicable**" and **builds a separate model**, and does not force the process uncertainty into this interval formula.
 - **L3 estimation-error covariance:** under L1=through-chain + L2=independent binomial, `Cov(log(1−λ̂_i), log(1−λ̂_j)) = 0` (the telescope product `η̂=∏(1−λ̂_i)=D/M`, all intermediate terms cancel, and precision depends only on the starting-cell count `M`); hence the diagonal Σ sum holds, **no covariance term is added**.
   - **Explicit:** L1=through-chain (flow topology) does **not necessarily** imply L3≠0; what truly determines whether `Cov` is 0 and whether the interval is underestimated is **L2** (the inter-layer loss-correlation mechanism); the three layers must not be collapsed into one.
 - **Floor discipline:** regardless of how L2 is adjudicated, the main interval always goes through "paired / joint bootstrap of the whole chain on the starting cells" or "directly constructing a binomial / Wilson interval for `η̂=D/M`"; per-layer independent binomial / Beta resampling applies only to alternative branch ①. The nested correlation of `λ̂_i` is retained by paired resampling and is not handled as per-layer independence; the **no-after-the-fact-optimisation** discipline is retained.

###### 2.2 Separate estimation of the per-layer conditional loss rate `λ_i` and precision target (recomputable sample-size formula)

- **Estimation method:** at level `i`, take the number of flow cells "entering that level" `n_i` as the denominator and the number of "conditionally lost cells at that level" as the numerator, giving `λ̂_i = loss/input`; input / output / new / recovery are accounted in four categories separately, and new or recovery > 0 triggers building a separate model. **Note:** "separate estimation" here means each level computes its own conditional loss rate; it does not mean the levels are non-overlapping independent samples; in the main design (convention ②) the denominators decrease level by level and the samples are nested.
- `λ_i` is a proportion; use the **single-proportion 95% CI half-width formula** to set each level's precision target:

`n_i = z_{1−α/2}² · p(1−p) / h²`, taking `p = 0.5` (maximum variance, most conservative).

- **Substitution** (all illustrative pre-registration parameters, illustrative, applicable only to this design):
 - `z_{1−α/2} = 1.959964` → `z² = 3.841459`
 - `p(1−p) = 0.25`
 - target half-width `h = 0.03` (i.e., the 95% CI half-width of `λ̂_i` ≤ 3 percentage points)
 - `n_i = 3.841459 × 0.25 / 0.03² = 0.960365 / 0.0009 = 1067.0719 → 1068`
 - 10% missing / invalid inflation: `ceil(1068 × 1.10) = 1175` / level
 - `n = 4` levels, with each level independently sampled, total **4 × 1175 = 4700 level-cell records** (illustrative) — this is the sample convention of **alternative branch ① (convention ①)**, enabled only when each level can be independently sampled and through-chain data cannot be obtained; it is mutually exclusive with the main-design convention ②, **not additive**. The per-level `λ̂_i` half-width ≤3pp / `n_i≥1175` serves the "per-level estimation and build-a-separate-model criterion", and is reported **separately** from the precision of the end-to-end `η̂`.
- **Main-design convention ②: back-calculation of the starting input when the same batch of flow passes through** (§3.1 "the same effective flow passes through", this section's **pre-registered main design**): the bottleneck is the input of the last level; back-calculate using the **demonstration planned loss upper bound `λ_plan = 0.05` (5%)** — this value is used only to back-calculate the starting input amount, **not the `λ_i` estimate, not measured, not a calibrated threshold, and unrelated to Olken's 8 percentage points**:

`M ≥ 1175 / (1 − 0.05)^{4−1} = 1175 / 0.857375 = 1370.4622 → 1371` starting cells; plus a 10% starting-stage loss inflation → **M ≥ 1509** (illustrative).

- **Relationship of the three sample conventions (pre-registration statement):** `4700` (convention ① alternative branch, level-cell records with each level independently sampled) and `M≥1509` (convention ② main design, starting input of the through chain) are **two mutually exclusive main designs, not additive, not simultaneously enabled**; `833` (the end-to-end held-out cells of §2.3 of this section) is an independent validation sample that **depends on the main design and takes a separate batch**, used for `η_obs=D_end/N_end`, and is not superimposed with `M`, nor served by the same through-chain batch, avoiding the optimistic bias of "the same batch of data both estimates `λ_i` and validates `η_obs`"; its denominator and disjoint relationship must be frozen before observation. Both demonstration values of the two conventions are given below; for execution pre-registration one **takes the pre-registered main design (convention ②), without after-the-fact optimisation**.
- `α_i = 0.05` (per-level half-width), `power = 0.80`, minimum meaningful deviation `δ = 0.05` (absolute, 5 percentage points) — all **applicable only to this design**, no book-wide uniform value (§8.1 convention).

###### 2.3 Interval construction for `η̂` (main: whole-chain paired bootstrap / `η̂=D/M` interval; delta method only as a convention-① demonstration)

- **Point estimate:** `η̂ = ∏_{i=1}^{n}(1 − λ̂_i)`; under the through convention it is identically the telescope product `η̂ = D/M` (`D` = final surviving cell count, `M` = starting input cell count), with all intermediate-layer terms cancelling.
- **Main interval (convention ② main design):** perform a **paired / joint bootstrap of the whole chain on the starting cells** (resampling unit = starting cell, the whole 4-level chain travels together, `B = 10000`, random seed frozen before observation), or directly construct a binomial / Wilson interval for `η̂ = D/M` (the log-scale delta form is `Var(log η̂) = (1−η)/(Mη)`). This convention depends on `M` alone for precision, unrelated to the marginal precision of the per-layer `λ̂_i`.
- **Delta method (only as a convention-① alternative demonstration, analytically recomputable):** `log η̂ = Σ log(1 − λ̂_i)`; `Var(log η̂) ≈ Σ Var(λ̂_i)/(1−λ_i)²`, where `Var(λ̂_i) = λ_i(1−λ_i)/n_i`; `SE(log η̂) = √Var(log η̂)`; interval `η̂ · exp(± z_{1−α/2} · SE(log η̂))`. **Conditions for holding:** L1 through-chain + L2 cell-level independent binomial, no over-dispersion, no inter-layer common shock ⇒ `Cov(log(1−λ̂_i), log(1−λ̂_j)) = 0`, the Σ diagonal sum holds, **no covariance term is added**; if a common shock is detected, record "not applicable" per item 11 of B-B's same-convention prerequisite checklist and build a separate model. Per-layer binomial / Beta independent resampling also applies only to convention ①.
- **Demonstration substitution (under convention ① "each level independently sampled `n_i=1175`", not the main-design value)** (`λ̂_i = 0.05`, `n_i = 1175`, `n = 4`, `α = 0.05`; all illustrative, for showing interval construction only, **not measured**):
 - `η̂ = (1 − 0.05)⁴ = 0.81450625`
 - `Var(λ̂_i) = 0.05 × 0.95 / 1175 = 4.04255e−05`
 - `Var(log η̂) = 4 × 4.04255e−05 / 0.9025 = 0.0001791713`; `SE(log η̂) = 0.01338549`
 - `exp(±1.959964 × 0.01338549) = 1.02658225 / 0.97410607`
 - **95% PI = [0.793415, 0.836158]** (illustrative, **convention-① alternative branch demonstration**).
- **PI target-quantity statement (pre-registration):** the above is a **confidence interval for a fixed `η`** (parameter uncertainty), **not a prediction interval including process fluctuation**; if a prediction interval including process fluctuation is needed, one must build a separate model or record "not applicable" when L2 has a common shock. The per-layer `λ̂_i` half-width ≤3pp and the end-to-end `η̂` interval are two different target quantities, **reported separately**.
- **Main-design convention ② demonstration value** (`M = 1509`, `η = 0.81450625`, `α = 0.05`, 10% inflation; illustrative): `Var(log η̂) = (1−η)/(Mη) = 1.5092e−04`, `Var(η̂) = η̂²·Var(log η̂) = 1.0012e−04`; under the `δ = 0.05` budget `Var(D) ≤ (δ/z_sum)² = 3.18517e−04`, the variance left for `η_obs` `= 2.18394e−04`, hence

 `N_end ≥ η(1−η)/2.18394e−04 = 691.805 → 692`, 10% inflation → **762 independent held-out cells** (convention ② demonstration, a separate batch from `M≥1509`, not additive).
   Parallel alternative: when `M = 1371` (no further 10% starting-stage loss inflation), `N_end 726 → 799` (10% inflation, illustrative); corresponding to another M, parallel with `692→762`, not mixed.

  Convention ② interval should be given by the whole-chain paired bootstrap / `D/M` binomial interval, and does not reuse convention ①'s `[0.793415, 0.836158]`.
- **Bootstrap main (convention ②):** the resampling unit is the **starting cell**, the whole chain is resampled together, `B = 10000`, random seed frozen before observation, taking the 2.5 / 97.5 percentiles of `η̂`; per-layer binomial / Beta independent resampling **applies only to alternative branch ①** and is not the main design. The delta demonstration form of convention ① and the bootstrap convention of convention ② differ and do not cross-validate each other; at execution take the interval under the pre-registered main-design convention ②, and the convention-① values serve only as a demonstration contrast, **without after-the-fact optimisation**; if the main-design premise (L2 no common shock) does not hold, record "not applicable / build a separate model" per item 11 of B-B's same-convention prerequisite checklist, and do not use convention ① to fill the gap.
- **End-to-end held-out cohort (demonstration of convention-① alternative branch)** (for the `D = η_obs − η̂` comparison): `Var(η̂) = η̂² · Var(log η̂) = 0.0001188659`, `SE(η̂) = 0.01090256`; to detect `|D| = δ = 0.05` at `α=0.05`, `power=0.80`, requires `Var(D) ≤ (δ/z_sum)² = 0.0003185168`, leaving `η_obs` variance `0.0001996509`;

`N_end ≥ η(1−η)/0.0001996509 = 0.81450625 × 0.18549375 / 0.0001996509 = 756.7501 → 757`, 10% inflation → **833 independent held-out cells** (illustrative, **convention-① demonstration**; the convention-② main design's `692→762` is above). The convention and denominator of `η_obs` must be frozen before observation; `833` is an independent validation sample that depends on the main design and takes a separate batch, mutually exclusive with `M≥1509`, **not additive**.

###### 2.4 Minimum meaningful deviation and the bifurcation rule for reject / not-applicable / build-separate-model

The minimum meaningful deviation `δ = 0.05` (absolute, 5 percentage points, illustrative, applicable only to this design); construct the 95% CI of `D = η_obs − η̂` (including the uncertainty of both `η̂` and `η_obs`, per the whole-chain paired bootstrap / double-sampling bootstrap of the pre-registered main-design convention ②; only the combined-variance delta form is used for convention-① alternative branch). The variance budget is consistent with the main design chosen in §2.3, and is not mixed across conventions.

| Situation | Interval condition | Judgement | Follow-up action |
| :--- | :--- | :--- | :--- |
| Model deviate | `D`'s 95% CI falls entirely outside `(−δ, +δ)` | **reject** the model's applicability (§3.1) | recheck the bridging hypothesis and applicability boundary; do not rename the counterexample as a "good intermediary" |
| Consistent | `D`'s 95% CI falls entirely within `(−δ, +δ)` (equivalence holds) | **not rejected** | do not write "verified" |
| Insufficient precision | CI crosses the `±δ` boundary or half-width exceeds pre-registered upper bound | **insufficient evidence** | a non-significant result is not by itself a refutation (§1.5 Group II) |
| Premise not established | any item of B-B's same-convention prerequisite checklist is not satisfied (parallel bypass / new output / recovery path / inconsistent unit / buffering level without alternative) | **not applicable** | **build a separate model** (G004, §3.1), and one must not, after the fact, rename all counterexamples as "good intermediaries" |
| Data missing | any one of the four categories input / output / new / recovery is unaccounted | **missing** | do not merge into pass or fail |

**Prohibited items:** one cannot adjudicate solely on the number of levels or "not significantly decreased" (§1.5 Group II, §3.1); the relationship between regulatory word count and TFP cannot substitute for a direct test of this model (§1.5 Group II).

###### 2.6 Explicit exclusion of Olken's 8% and `n ≥ 4` misuse (separate sub-section)

- **Olken 8%:** the "8 percentage points" recounted in case 3.1-A is "the treatment effect of raising the audit probability from about 4% to 100% on missing expenditure"; its dimension, object of estimation, and denominator all differ from "the conditional loss rate `λ_i` of level `i` relative to its input"; G004 explicitly states "Olken's missing expenditure is not a layer-loss parameter, source convention see the source ledger". **This section does not use 8% (or 8 percentage points) as any conditional loss rate, demonstration-parameter value, or threshold**; the "Olken 8%" appearing in the text is only a reference to the excluded object; the `0.05` used to back-calculate the starting input is a demonstration planned loss upper bound and is unrelated to Olken.
- **`n ≥ 4`:** §3.1's testing method explicitly states "`n≥4` itself is not a decay or collapse critical value". This section uses `n = 4` as a demonstration layer count only to show the `∏` formula and interval construction, **and does not assign it a critical meaning**; the collapse / deadlock path must be separately tested with independent data (§1.6.1 Group II).
- Neither may be written as a calibrated threshold or empirical conclusion of this book.

---

##### 8.5.4.3 Discriminating-Prediction Comparison C1 | SP-RFC-006 TTL Quadrifold vs Approval-Latency Literature Baseline

**Corresponding clause and identity:** SP-RFC-006 (§3.3), §1.6.1 Group III. Claim identity: **conditional judgment and application comparison** (does not elevate). Symbols carried over: `T_latency` (§3.3), `Latency_Audit` / `TTL_mission` (§3.3), `T_latency ≤ Δt < T_environment` (§1.5 Group VI, §1.6.1 Group VI); no new symbols invented.

###### 3.1 Existing-theory prediction A (refutable simplified statement)

- **A:** a common simplified setting of a certain class of approval-latency / regulatory-burden literature (the **executing researcher must, at pre-registration, name the specific literature and estimation equation**) — "an increase in approval latency monotonically lowers task-completion rate and net benefit; the four types of consequences can be merged into a single scalar loss; speeding up or cancelling approval tends to raise the system's overall net benefit".
- **A is a refutable simplified statement of the literature baseline and does not represent the original authors' position; this book does not endorse the authors.**
- **Comparison objects (named only, no conclusions added):** §1.6.1 has already named Baker/Bloom/Davis 2016 (policy uncertainty, Group III), Dawson & Seater 2013 (regulatory accumulation and growth, Group II). This section adds no prediction, page number, coefficient, or estimation equation for these literatures; the naming work is left to the executing researcher at pre-registration.

###### 3.2 This book's prediction B (SP-RFC-006, does not elevate)

- **B1 (quadrifold cannot be merged):** when `Latency_Audit > TTL_mission`, one must strictly distinguish and separately measure the four types of consequences: ① the original planned path is not completed on time; ② a low-cost alternative path is available and bypass migration occurs; ③ a local exploration task fails; ④ system-level organisational-governance failure (§3.3). One cannot directly equate an individual task delay or local bypass with overall organisational collapse or wholesale failure of the regulatory tool.
- **B2 (non-monotonic, separable):** the four consequences vary **non-synchronously** with `T_latency` — "bypass migration" may rise as latency increases, while "system-level governance failure" need not rise synchronously; "original-path delay" rises but task-level failure may be compensated by an alternative path. Thus A's "mergeable and monotonic" can be distinguished by data.
- **B3 (protective hard constraint):** when the protection effect is uncertain or incomparable, one should retain the uncertainty and continue verification, and **cannot cancel necessary safeguards solely on the basis of latency** (§3.3); even if the original rule has a protection benefit, if the alternative meets the ex-ante declared protection requirement, satisfies the rights constraint, and has lower full cost, it may also constitute an improvement basis; **one does not set "the original rule has no protection benefit" as a necessary condition**.

###### 3.3 Distinguishing observables and stratified design

- **Stratification (frozen before observation):**
 - Level 1: `Latency_Audit ≤ TTL_mission` (not timed out)
 - Level 2: `TTL_mission < Latency_Audit ≤ Δt` (timed out but still within the environment time window, convention `T_latency ≤ Δt < T_environment`)
 - Level 3: `Latency_Audit > Δt` (beyond the observation window)
 - Within each level, dichotomise by "whether a low-cost alternative path exists" → `3 × 2 = 6` cells.
- **Separate independent measurement:** `T_latency` / `Latency_Audit`, compliance cost, the actual physical-blocking rate of violations, the rate of each of the four consequences, protection effect, rights impact, migration risk (§3.3).
- **Discriminating statistics (pre-registered):** the difference `Δ_bypass` between Level 2 and Level 1 in "bypass-migration rate"; and the difference `Δ_slope` between "bypass-migration slope − system-level-failure slope". A predicts `Δ_bypass ≤ Δ_min` and `Δ_slope ≈ 0` (same-direction, mergeable); B predicts `Δ_bypass ≥ Δ_min` and `Δ_slope > 0` (separable).
- **Sample size / precision** (illustrative pre-registration parameter, illustrative, applicable only to this design): `α = 0.05`, `power = 0.80`, `Δ_min = 0.15` (proportion difference); two independent proportions comparison

`n/组 = 2 p̄(1−p̄)(z_{1−α/2}+z_{1−β})² / (p1−p2)²` **(pooled-variance approximate form (a), not the strict form; strict form (c) see the cross-check of this item)**

Substitute `p1 = 0.35`, `p2 = 0.20`, `p̄ = 0.275`, `z_sum² = 7.848880`:

`n/组 = 2 × 0.275 × 0.725 × 7.848880 / 0.15² = 3.129766 / 0.0225 = 139.0996 → 140`, 10% inflation → **154 / cell**; 6 cells most conservative total **≥ 924 task cells** (illustrative).
- **Approximate-form annotation and strict-form cross-check** (illustrative): the above (a) and the "non-pooled-variance form (b)" are both simplified approximations sharing `(z_{1−α/2}+z_{1−β})²`; the strict form (c) is `n = [z_{1−α/2}√(2p̄q̄) + z_{1−β}√(p1q1+p2q2)]²/(p1−p2)²`. For this item's values `(p1=0.35, p2=0.20)`: (a) `139.0996→140→154`, (b) `135.1752→136`, (c) `137.9148→138→152`; (b) is the smallest and least conservative, and at pre-registration one must pre-register and fix one form and remain consistent throughout, to avoid mistakenly choosing (b) and causing insufficient power. The difference at the demonstration-parameter level does not change the conclusion.
- **Multiple comparisons:** the four consequences are "stratified main indicators"; pre-register a fixed order (first `Δ_bypass`, then `Δ_slope`, then report the four separately) or an equivalent Holm treatment; it is prohibited to label organisations as TCP/UDP by success or failure, and after-the-fact optimisation is prohibited (§1.5 Group V, §3.3).

###### 3.4 Judgement rules (interval-style, the four consequences not mergeable)

| Situation | Interval condition | Judgement |
| :--- | :--- | :--- |
| Separation holds | `Δ_bypass` 95% CI lower bound `> Δ_min`, and `Δ_slope` (pre-registered as "bypass-migration slope − system-level-failure slope") 95% CI lower bound `> ε_slope` | A's "mergeable and monotonic" simplification is excluded within this design; B is **not rejected** (do not write "verified") |
| Simplification holds | `Δ_bypass` 95% CI upper bound `< Δ_min`, and `Δ_slope` 95% CI falls entirely within the equivalence range `[−ε_slope, +ε_slope]` | narrow / **reject** B's local prediction |
| Insufficient precision | CI crosses the `Δ_min` boundary or half-width exceeds pre-registered upper bound | **insufficient evidence**; a non-significant result is not a refutation |
| Protection uncertain | protection-effect 95% CI crosses 0 | even if latency is significant, one **must not** output a "cancel safeguards" conclusion → record "not applicable" / "insufficient evidence", retain the uncertainty and continue verification |
| Premise not established | no clear `TTL_mission` / exemption from application, long-term permit, classification rule not included / observation window undefinable | **not applicable** |
| Data missing | any of the four consequences not recorded separately | **missing** |

The four consequences **must not be merged** into a single scalar; the four judgement categories must not be merged.

**Equivalence-boundary demonstration values** (illustrative, applicable only to this design, frozen before observation): `ε_slope = 0.05` (equivalence bound for the difference of the two slopes); `Δ_min = 0.15` (minimum meaningful improvement in the level difference of the bypass-migration rate). A predicts `Δ_bypass ≤ Δ_min` and `Δ_slope ≈ 0` (`|Δ_slope| ≤ ε_slope`); B predicts `Δ_bypass > Δ_min` and `Δ_slope > ε_slope`. The overlap on the `= Δ_min` / `= ε_slope` boundaries is covered by the "insufficient precision" row and is not a confirmatory judgement. The regression / stratified-difference setup of `Δ_slope` (slope estimated by `T_latency` stratification as linear) and the separate measurement of the four consequences must be pre-registered and fixed.

###### 3.5 Boundary and not-applicable situations

- If high latency is combined with SP-RFC-005's rent-setting condition, the latency consequence and the rent-setting evidence must be reported separately, not merged (§3.3 coupling boundary); one cannot judge rent-seeking solely on the basis of latency or charges.
- One does not derive "significant impedance" or industrial consequences from a statute (case 3.3-A); formal review cannot substitute for real safety outcomes.
- Does not elevate: RFC-006 remains "conditional judgment and application comparison", and does not claim the prediction is supported or falsified.

##### 8.5.4.4 Discriminating-Prediction Comparison C2 | SP-RFC-015 Choice-Set Identification vs Bundling-Antitrust Literature Baseline

**Corresponding clause and identity:** SP-RFC-015 (§5.5), case 5.5-A, §1.6.1 Group IV. Claim identity: **identification boundary and application hypothesis** (does not elevate). Symbols carried over: `H(Choice)` (§5.5); no new symbols invented.

###### 4.1 Existing-theory prediction A (refutable simplified statement)

- **A:** a common simplified setting of a certain class of bundling / antitrust and "voluntariness" literature (the **executing researcher must, at pre-registration, name the specific literature and estimation equation**) — "observing a single choice / bundling acceptance (in the choice set) can serve as an indicator that market dominance has deprived a feasible alternative or that voluntariness is insufficient; formal signed agreement + high concentration can presume non-voluntary / anti-competitive".
- **A is a refutable simplified statement of the literature baseline and does not represent the original authors' position; this book does not endorse the authors.**
- **Comparison objects (named only, no conclusions added):** §1.6.1 has already named Weingast 1995 (Group IV), Olson 1982 (Group II); case 5.5-A's company town and operating-system bundling lawsuit serve only as a comparison object for structural lock-in. This section adds no conclusion for them, nor makes a legal determination.

###### 4.2 This book's prediction B (SP-RFC-015, does not elevate)

- **B1 (`H(Choice)=0` indistinguishability):** observing choice entropy `H(Choice)=0` only indicates that the sample's choice set is concentrated; both **consistent preference** and **deprived feasible alternative** may produce this phenomenon, and the constraint, exit cost, and feasible choice set must be identified independently (§5.5). Therefore there is no directly derivable discriminative relationship between `H(Choice)=0` and "voluntariness / constraint".
- **B2:** one must separately test resource-control rights, bundling conditions, feasible exit paths, and ledger records, and then assess their impact on trust; if the responsibility explanation only invokes formal signed agreement without disclosing alternative options, exit costs, and historical forced contributions, then a responsibility-attribution bias and a pseudo-voluntary narrative arise (§5.5).
- **B3:** in samples where preference is consistent but the alternative is sufficient and the exit cost is low, `H(Choice)=0` should still stably appear, while voluntariness is not weakened — this is the distinguishable point between A and B.

###### 4.3 Distinguishing observables and stratified design (the `H(Choice)=0` indistinguishability must be handled)

- **2×2 factorial:**
 - Factor 1 "feasible alternative deprived": yes (constraint / high exit cost / alternative channel blocked) / no (alternative sufficient, exit cost low)
 - Factor 2 "consistent preference": high (prior-induced stable preference) / low (dispersed preference)
 - All four groups may observe `H(Choice)=0`; the key is that **under the same `H(Choice)=0` observation**, the groups must be distinguishable on independent identification quantities such as "exit cost, feasible choice set, ledger historical forced contribution".
- **Separate independent measurement:** `H(Choice)`, feasible-choice-set size and reachability, exit cost, alternative-channel availability, ledger-recorded historical forced contribution, formal signed-agreement text, trust indicator, responsibility-attribution-bias / pseudo-voluntary-narrative score. **The observation denominator must be explicit** (§5.5 original text is "make the feasible alternative, exit cost, monopoly control, and observation denominator explicit"); "freeze before observation" is this pre-registration's freeze requirement, separately specified by this design, not the original line's text.
- **Discriminating statistics (pre-registered):** within the `H(Choice)=0` sub-sample, the proportion `p` of the group "alternative sufficient (no constraint + high preference consistency)"; and the classification ability `AUC` of `H(Choice)=0` for the constraint state. **Discrimination lower-bound demonstration value `AUC_lo = 0.70` (illustrative, applicable only to this design)**: A's simplified prediction `p ≤ p0` and `AUC > AUC_lo` (discriminable); B predicts `p ≥ p1` and `AUC < AUC_lo` (indiscriminable range).
- **Sample size / precision** (illustrative pre-registration parameter, illustrative, applicable only to this design): `α = 0.05`, `power = 0.80`, `Δ_min = 0.10` (`p1 − p0`), `p0 = 0.20`, `p1 = 0.30`; single-proportion test

`n = (z_{1−α/2}√(p0(1−p0)) + z_{1−β}√(p1(1−p1)))² / (p1−p0)²`

Substitute `z_{1−α/2}=1.959964`, `z_{1−β}=0.841621`, `√0.16=0.4`, `√0.21=0.458258`:

`(1.959964×0.4 + 0.841621×0.458258)² / 0.01 = (0.783986 + 0.385668)² / 0.01 = 1.368090 / 0.01 = 136.8116 → 137`, 10% inflation → **151 (`H(Choice)=0` sub-sample size)**; 2×2 four groups most conservative total **≥ 604 (`H(Choice)=0` observations within the condition)** (illustrative). **Sub-sample-size and total-sample-size conventions:** `151` and `604` are both quantities **conditional on the `H(Choice)=0` sub-sample**, not the initial recruitment total; the initial recruitment must be scaled up by the incidence `q` of `H(Choice)=0`: taking demonstration `q = 0.50` (illustrative, frozen before observation or ratified by pilot), the initial recruitment `≥ 604 / 0.50 = 1208` observation cells. The convention of `q` and the four-group allocation must be frozen before observation.
- **Multiple comparisons:** the main indicator is "single" (proportion of unconstrained group within the `H(Choice)=0` sub-sample), and `AUC`, exit cost, trust are stratified secondaries; pre-register Holm or fixed order; after-the-fact optimisation is prohibited.

###### 4.4 Judgement rules (interval-style)

| Situation | Interval condition | Judgement |
| :--- | :--- | :--- |
| Indistinguishability holds | `p`'s 95% CI lower bound `> p1` (i.e., `H(Choice)=0` still stably appears under sufficient alternative condition), and `AUC`'s 95% CI upper bound `< AUC_lo = 0.70` (demonstration discrimination lower bound) | A's "‘H(Choice)=0’ discriminates non-voluntariness" simplification is excluded within this design; B is **not rejected** |
| Simplification holds | `p`'s 95% CI upper bound `< p0` and `AUC`'s 95% CI lower bound `> AUC_lo = 0.70` (falls entirely within the "discriminable" equivalence range) | narrow / **reject** B's local prediction |
| Insufficient precision | CI crosses the `p1` / discrimination-lower-bound boundary, or half-width exceeds upper bound | **insufficient evidence**; a non-significant result is not a refutation |
| Premise not established | feasible alternative or exit cost unobservable, observation denominator missing | **not applicable** |
| Data missing | `H(Choice)` or independent identification quantity unrecorded | **missing** |

One does not derive a responsibility-attribution bias or pseudo-voluntary narrative directly from `H(Choice)`; one does not prove voluntary or non-voluntary solely from "a single choice" (§5.5).

**Equivalence-boundary demonstration values** (illustrative, applicable only to this design, frozen before observation): `p0 = 0.20`, `p1 = 0.30`, `AUC_lo = 0.70`; the middle grey zone where `p0 < p < p1` and `AUC` crosses `AUC_lo` is covered by the "insufficient precision" row. The classifier, feature set, and `q` (`H(Choice)=0` incidence) of AUC must be frozen before observation.

###### 4.5 Boundary and not-applicable situations

- Judicial voluntariness determination must be tested against statutory elements, price evidence, and judicial judgments; this comparison is **not a legal determination** (case 5.5-A).
- "A single choice cannot alone prove voluntariness" is a mechanism critique, not a proven topological proposition; does not elevate: RFC-015 remains "identification boundary and application hypothesis".

##### 8.5.4.5 Discriminating-Prediction Comparison C3 | Group I Channel Capacity vs Readability / Print Capitalism Literature Baseline

**Corresponding clause and identity:** §1.5 Group I core proposition, §1.6.1 Group I, §8.3.2, §8.5.1. Claim identity: **citation of established physical results / conditional model / semantic application** (does not elevate). Symbols carried over (all must note uncalibrated): `PBR`, `PNR`, `H_norm` (§8.3.2); `SDI` / `SDI>0.40` / `θ_review=0.25` / `τ_lex=0.15` (§8.3.1, uncalibrated proportional threshold / demonstration value); `$I_{phys}=B_{Hz}\log_2(1+P_S/P_N)$`, `$C≤kI$` (§1.5 Group I, yet-to-be-calibrated social bridging, applicable only to the given physical model). Do not substitute PBR etc. into demonstration thresholds for judgement.

###### 5.1 Existing-theory prediction A (refutable simplified statement)

- **A:** a common simplified setting of a certain class of readability / print-capitalism / text-standardisation literature (the **executing researcher must, at pre-registration, name the specific literature and estimation equation**) — "more standardised, more compressed, more readable text monotonically lowers comprehension cost and raises collaboration and execution performance; the degree of compression is negatively monotonic with execution error".
- **A is a refutable simplified statement of the literature baseline and does not represent the original authors' position; this book does not endorse the authors.**
- **Comparison objects (named only, no conclusions added):** §1.6.1 Group I has already named James C. Scott *Seeing Like a State* (1998), Benedict Anderson *Imagined Communities* (1983). This section adds no conclusion for them.

###### 5.2 This book's prediction B (Group I, does not elevate)

- **B1 (non-monotonic):** if over-standardisation / compression loses **negatives, exceptions, rights, and procedural safeguards** (§8.3.2 "must not be lost through text shortening", §8.5.1 "retain negatives, exceptions, rights, and procedural safeguards"), it instead **raises execution error**. That is, the degree of compression `x` and the execution error `e(x)` are U-shaped / have a turning point: moderate compression lowers error, but after exceeding the critical compression (safeguard clauses are cut), error rebounds.
- **B2 (no boundary-crossing):** `$C≤kI$` is a yet-to-be-calibrated social-bridging hypothesis; one cannot derive from the Shannon-capacity formula that the variance index of grassroots comprehension diverges, nor directly derive the cultivation cycle or collaboration radius from the genre (§1.5 Group I, §8.5.1).
- **B3 (alternative explanations to control):** compare explanations such as **education, resources, institution**; one does not derive social effects directly from the genre (§1.5 Group I); content familiarity and training are controlled separately (§8.5.1 / G002).

###### 5.3 Distinguishing observables and stratified design

- **Design:** degree of compression / standardisation (low / medium / high three levels, stratified by `PBR`, turning point frozen before observation) × safeguard-clause retention (retained / cut) → `3 × 2 = 6` cells; the core manipulation is "whether negatives / exceptions / rights / procedural-safeguard clauses are retained".
- **Separate independent measurement:** target-audience comprehension-accuracy rate, execution-error rate, task-completion rate, comprehension latency (§8.5.1 calibration requirement), blind-test proposition-equivalence score; the text proxies `PBR`, `H_norm` serve only as manipulation checks and descriptions, noted as **uncalibrated**, and are not used as judgement thresholds.
- **Control variables (§1.5 Group I + §8.5.1 + G002):** education / prior knowledge, resources (time, tools), institution (rule version, remedy-interface availability), content familiarity, training — stratified randomisation or pre-registered covariates, after-the-fact optimisation prohibited; additionally follow the four-way confounder-separation discipline of §8.5.2, and do not attribute the difference to the genre / compression itself before controls are applied.
- **Discriminating statistics (pre-registered):** the execution-error-rate difference `Δ_err` between the high-compression-and-safeguard-cut group and the medium-compression-(safeguard-retained) group; and the quadratic term `β₂` in the compression-degree–error regression. A predicts `β₂ ≤ 0`, `Δ_err ≤ 0` (monotonic improvement); B predicts `β₂ > 0`, `Δ_err > 0` (rebound).
- **Sample size / precision** (illustrative pre-registration parameter, illustrative, applicable only to this design): `α = 0.05`, `power = 0.80`, `Δ_min = 0.15` (proportion difference); two independent proportions comparison

`n/组 = 2 p̄(1−p̄)(z_{1−α/2}+z_{1−β})² / (p1−p2)²` **(pooled-variance approximate form (a), not the strict form; strict form (c) see the cross-check of this item)**

Substitute `p1 = 0.30`, `p2 = 0.15`, `p̄ = 0.225`, `z_sum² = 7.848880`:

`n/组 = 2 × 0.225 × 0.775 × 7.848880 / 0.15² = 2.737296 / 0.0225 = 121.6576 → 122`, 10% inflation → **135 / cell**; 6 cells most conservative total **≥ 810 observation cells** (illustrative). **Approximate-form annotation and strict-form cross-check:** for this item's values `(p1=0.30, p2=0.15)`, (a) `121.6576→122→135`, (b) non-pooled simplified form `117.7332→118`, (c) strict form `120.4719→121→134`; at pre-registration one must pre-register and fix one form and remain consistent throughout. **`β₂` positioning (choose one of two, take "joint main criterion alongside `Δ_err`"):** `β₂` (the quadratic term of the compression-degree–error regression) and `Δ_err` are both confirmatory criteria of the §5.4 judgement table; the sample size is set by the main proportion difference `Δ_err`, and the testing power of `β₂` must be separately ratified at pre-registration by the quadratic-effect magnitude; `β₂` is no longer labelled "stratified secondary / sensitivity" so as to be consistent with §5.4's joint judgement "β₂ CI lower bound > 0 and Δ_err CI lower bound > `Δ_min`".
- **Multiple comparisons:** the main criteria are the two jointly `Δ_err` and `β₂` (a single family, pre-register Holm or fixed-order equivalent treatment, family-wise error rate controlled at 0.05); after-the-fact optimisation is prohibited.

###### 5.4 Judgement rules (interval-style)

| Situation | Interval condition | Judgement |
| :--- | :--- | :--- |
| Non-monotonic holds | `β₂`'s 95% CI lower bound `> 0` and `Δ_err`'s 95% CI lower bound `> Δ_min` | A's "monotonic" simplification is excluded within this design; B is **not rejected** |
| Simplification holds | `β₂`'s 95% CI upper bound `≤ 0` and `Δ_err`'s 95% CI upper bound `≤ Δ_min` (i.e., falls entirely within the "monotonic improvement" equivalence range `β₂ ∈ [−ε_β, 0]`, `Δ_err ∈ [−ε_e, 0]`) | narrow / **reject** B's local prediction |
| Insufficient precision | CI crosses 0 / `Δ_min` boundary or half-width exceeds upper bound | **insufficient evidence**; a non-significant result is not a refutation |
| Premise not established | proposition-equivalence blind test failed / compression did not touch safeguard clauses (must be pre-registered defined) | **not applicable** |
| Data missing | comprehension-accuracy rate or execution error unrecorded | **missing** |

**Equivalence-boundary demonstration values** (illustrative, applicable only to this design, frozen before observation): `ε_β = 0.05` (quadratic-term equivalence bound), `ε_e = Δ_min = 0.15` (execution-error-rate-difference equivalence bound); the "monotonic improvement" equivalence range is `β₂ ∈ [−0.05, 0]` and `Δ_err ∈ [−0.15, 0]`. The regression setup of `β₂` (quadratic term of the three compression levels, control variables see §5.3) and the turning point must be frozen before observation.

One must not use `$SDI>0.40$`, `$θ_review=0.25$`, `$τ_lex=0.15$`, `$PBR>0.65/0.85$` etc. **uncalibrated demonstration thresholds** as the judgement lines of this comparison (§8.3.1, §8.5.1 both note uncalibrated); one does not directly compute the social-collaboration upper bound from `$C≤kI$` (§1.6.1 Group I). Before complete operationalisation, do not report that this social-bridging proposition has passed or been falsified (§1.5 Group I).

###### 5.5 Boundary and not-applicable situations

- Proposition-equivalence blind test failed → not applicable; compression removed only redundancy and did not touch safeguard clauses → this comparison is not applicable or falls into the "monotonic region", to be defined before observation.
- Formal derivations (`$I_{phys}$`, `$C≤kI$`) hold only within the given physical model and do not substitute for social-bridging testing (§1.5 Group I).
- Does not elevate: Group I remains "citation of established physical results / conditional model / semantic application", and does not claim the prediction is supported or falsified.

<a id="legacy-v11-1-sec-8-5"></a>
<a id="sec-8-6"></a>

### 8.6 Historical-Case Indicator Interpretation Method and Simulation Examples (Illustrative Simulation & Framework Demonstration)

> ⚠️ **Methodological and evidence-boundary note:** the cases listed in this section are merely "simulation demos" that show the indicator-interpretation method and the state-machine mapping logic, intended to illustrate the computational relationships of each module **if the corresponding quantitative inputs were available**; they do not yet provide the complete corpus list, annotation method, and error assessment supporting these values, and do not thereby claim that Socio-Radar already possesses established measured precision and causal-prediction capability. A genuine predictive-power assessment must include control samples from non-crisis periods, a complete confusion-matrix test of the false-positive rate (False Positives) and the false-negative rate (False Negatives). Each SHI calculation to be shown must disclose the four complete inputs, model version, and calculation result; rows with incomplete inputs retain only the qualitative interpretation, and the SHI is labelled "inputs incomplete, not computed". Subsequent research should include non-crisis controls, out-of-time validation, false-positive / false-negative rates, and comparison with a baseline model, and report the sensitivity of weights and thresholds.
> *Source check:* [OECD / EU / EC-JRC (2008), Handbook on Constructing Composite Indicators](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf). The support scope of this handbook in this section is limited to the ten-step method for constructing composite indicators, especially weighting and aggregation (Step 6: Weighting and aggregation), uncertainty and sensitivity analysis (Step 7: Uncertainty and sensitivity analysis), and linking to other variables (Step 9: Links to other variables); **non-crisis-period control samples, out-of-time validation, and false-positive / false-negative confusion-matrix tests are self-imposed requirements raised by this book for early-warning classification assessment, and are not provided by that handbook**.

| Simulation-interpretation scenario | Hypothetical input (not measured) | Simulated SHI | Interpretation scope and evidence gap |
| :--- | :--- | :--- | :--- |
| **Pre-Reformation intermediary structure (simulation-interpretation example)** | hypothetical $PBR=0.88,SIR=0.92,MPM=0.85$; SDI not given | inputs incomplete, not computed | shows a candidate interpretation of text and organisational indicators; not a measurement of the year 1510 (here a schematic year) nor a single-cause model of the Lutheran Reformation. |
| **Road-locomotive regulation (simulation-interpretation example)** | hypothetical $PBR=0.42,SIR=0.91,MPM=0.60$; SDI not given | inputs incomplete, not computed | the effect of regulation and technological development requires combining the rule version and control samples, and one cannot infer from set values that the industry was wholly strangled (the UK Locomotive Act 1865 and its 1896 amendment, see `案例 3.3-A`). |
| **DEI label-subdivision scenario (simulation-interpretation example)** | $\text{SDI} = 0.68$<br>$a_{\text{drift}} = 0.35$<br>$\text{MPM} = 0.84$<br>all hypothetical inputs, lacking PBR, SIR | **inputs incomplete, SHI not computed** | only shows a candidate analysis path of label subdivision and semantic-coordination cost; does not thereby assert the cause of a specific enterprise's change or its social-health state. |
| **Vernacular entering national education, hypothetical scenario (1920 simulation example)** | before reform: $\text{SDI}=0.55, \text{PBR}=0.75, \text{SIR}=0.85, \text{MPM}=0.65$<br>after reform: $\text{SDI}=0.10, \text{PBR}=0.15, \text{SIR}=0.20, \text{MPM}=0.30$ | **$\text{SHI}: 0.27 \to 0.83$; demonstration zoning: red → green**<br>(simulation showing a cross-ring leap) | computes the composite score from the artificially set four inputs before and after reform; `libc` is an education-interface analogy; one does not map literary norms or decrees directly into these values, and it does not represent real historical health or an identified reform effect (the historiographical convention of the relevant decrees and textbook replacement, see `案例 5.4-A`). |

> **Table-convention supplementary note:** "inputs incomplete, not computed" in the table means that when any required scalar is missing, the engine is not called to output a composite score or a global zone; assuming a sub-item value exceeds a bound (such as $PBR=0.88$, $SIR=0.92$) serves only as a qualitative dimensional illustration and does not constitute a demonstration red-zone judgement — among these, $MPM=0.85$ and $SIR=0.85$ do not satisfy the strict inequality `>0.85` single-item red-zone condition.

<!-- SP:END chapter-08 -->
