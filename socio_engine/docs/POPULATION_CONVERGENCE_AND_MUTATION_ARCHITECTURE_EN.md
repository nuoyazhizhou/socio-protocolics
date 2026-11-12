# Socio-Engine v2.3 Architecture Specification: Four-Stage Evolutionary Flywheel, Tripartite Decoupling, and Institutional Attractor Convergence

> **Version**: v2.3-canonical | **Creation Date**: 2026-11-12  
> **System Scope**: [Socio-Engine (Universal Social Sandbox)](../README.md) | [Socio-Protocolics Whitepaper](../../社会系统协议学白皮书.md)  
> **Core Propositions Supported**: `SP-POSTULATE-1` (Finite Energy & Exception Path), `SP-POSTULATE-2` (Autonomous Agent Postulate), `SP-POSTULATE-3` (Expectation-Induced Equilibrium), `SP-RFC-004/005` (Middleware Alienation & Rent Extraction), `SP-RFC-008/009` (Intertemporal Finality & Dynamic Inconsistency), `SP-RFC-018` (Evolutionary Arena & Secondary Alienation)

---

## 1. Why Swarm Diversity and Four-Stage Evolutionary Flywheel (Why v2.3)?

In `Socio-Engine v1.0` (Hai Rui Sandbox & Huizhou Silk Case), while the causal mechanism of "Iron-Fisted Anti-Corruption vs. Bureaucratic Clerk Slack" was verified, each social stratum was represented by only 1–2 named agents (e.g., 1 magistrate, 2 clerks, 2 gentry, 3 peasants).

This single-instance architecture suffered from three methodological limitations:
1. **Sample Serendipity**: Inability to rule out whether decisions were stochastic artifacts of specific prompt completions;
2. **Absence of Swarm Statistical Physics**: Real human societies consist of thousands of heterogeneous agents experiencing systemic stress, exhibiting **statistical convergence**;
3. **Absence of Endogenous Evolution and Reflexivity**: Grassroots agents under extreme pressure innovate, but their survival innovations face rent-seeking sabotage from sub-bureaucracy clerks and secondary alienation once co-opted.

---

## 2. Core Philosophy & Theoretical Postulates: The Institutional Attractor and Anti-Deus-Ex-Machina Principle

Before examining data structures and code, the core ontological mission of `Socio-Engine` must be crystallized:

### 2.1. Rejection of "Simulated Roleplay Toys": Verification of Institutional Attractors
Mainstream multi-agent frameworks (e.g., Stanford Smallville) treat agents as textual roleplay characters in a frictionless vacuum. They collapse what an agent thinks, says, and does into arbitrary unconstrained LLM completions without calorie conservation, double-entry ledgers, or starvation thresholds.

**Socio-Engine is NOT a game.**  
Its sole purpose is to verify: **Under non-zero physical impedance and immutable class privileges, when a institutional protocol (tax quotas, interest rates, penalty rules) is laid down, regardless of individual struggles, where does the macroscopic system statistically and inexorably converge?**

### 2.2. Langevin Dynamics: Micro-Struggles as Brownian Noise, Potential Wells as Fate
In non-equilibrium statistical physics, macroscopic system drift is governed by the **Langevin Equation**:

$$\frac{d\mathbf{x}}{dt} = \underbrace{-\nabla V(\mathbf{x})}_{\text{Systemic Institutional Gravity}} + \underbrace{\eta(t)}_{\text{Microscopic Moral Struggle \& Noise}}$$

* **$\eta(t)$ represents stochastic thermal fluctuations**: An individual agent's moral conscience, emotional sorrow, private brotherhood oaths, or momentary mercy;
* **$V(\mathbf{x})$ represents the Potential Energy Surface constructed by the protocol**: Hard tax quotas, interest rate surcharges, exclusive privilege rings, collective liability, and caloric subsistence deadlines ($\mathcal{H}_{\text{bio}}$);
* **$-\nabla V(\mathbf{x})$ represents the Institutional Gravity Field**.

When Wang Anshi hardcoded loan quotas to magistrate promotion criteria and tied loan defaults to middle-peasant collective liability, he excavated a steep potential well into the social landscape. In this regime, **the drift force $-\nabla V(\mathbf{x})$ overwhelmingly dominates the noise term $\eta(t)$**. The magistrate desires to be benevolent; Clerk Zhang desires to accumulate merit; the yeoman farmer desires mutual aid. Yet all microscopic moral struggles are smoothed out by institutional gravity, and the 21 agents inevitably slide into the catastrophic attractor basin:

$$\text{Compulsory Allocation} \longrightarrow \text{Clerk Rent Surcharges} \longrightarrow \text{Peasant Insolvency} \longrightarrow \text{Middle-Class Ruin} \longrightarrow \text{Widespread Abandonment \& Revolt}$$

### 2.3. The Anti-Deus-Ex-Machina Principle
Utopian moralists dream that "if everyone becomes virtuous, the policy will work." In classical Greek drama, when a plot collapsed into an unresolvable deadlock, a crane hoisted a god onto the stage (*Deus ex Machina*) to solve everything by divine fiat.

Real history has no crane-hoisted gods. **The only physical way for a system to escape an attractor basin is an exogenous thermodynamic windfall injection ($\Delta E \gg \Delta V$)**: finding an open-pit silver mine, a tenfold agricultural technology leap, or external imperial conquest. Without this physical surge, moral preaching and ideological slogans cannot alter institutional convergence.

### 2.4. Involuntary Entrapment & Historical Phase Locking ("被架起来后下不来")
Epochal historical transitions are never pre-programmed top-down blueprints. They are **constrained survival moves by desperate actors backed against existential cliffs**:
* **Xiaogang Village 18-Peasant Blood Pact (1978)**: Facing three consecutive years of drought and outright starvation, peasants signed a death-ground pact to divide communal land. Once committed, they were locked onto the historical stage and could only work desperately to survive, eventually forcing national de-collectivization;
* **Shekou Industrial Zone & the 4-Cent Bonus (1979)**: Confronted with construction paralysis, Yuan Geng established a 4-cent bonus per truckload. When denounced as "capitalist bonus worship," harbor idle losses and investment interest forced the leadership to appeal directly to the Central Committee, breaking egalitarian wage freezes;
* **Wenzhou Merchants & "Red Hats" (1980–1984)**: Impoverished peddlers founded underground credit societies and button workshops under threat of "speculation crimes," reluctantly wearing collective "red hats" to survive, ultimately forcing legal recognition of the private economy.

---

## 3. Four-Stage Comprehensive Evolutionary Flywheel Model (v2.3)

```
                      ┌────────────────────────────────────────────────────────┐
                      │             Exogenous Shock & Peer Engine              │
                      │  - Neighbor extreme quota promotion (spurs KPI panic)   │
                      │  - Neighbor clerk killed in revolt (spurs slack/fear)  │
                      │  - Physical shocks (locust drought / bumper crash)     │
                      └───────────────────────────┬────────────────────────────┘
                                                  │ Broadcast quarterly shocks
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │                Mental Polarity Operator (Phase Shifts)                 │
             │   [Desperation Mode: Fury]                 [Preservation Mode: Mercy]  │
             │   - Trigger: granary empty / cangue        - Trigger: neighbor revolt  │
             │   - Action: kill official, burn ledger     - Action: slack off, mercy  │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │            Microscopic Innovation Mutation Pool                        │
             │   - 5th-grade: 5-man credit unions, forward crop discounting           │
             │   - Middle freeholders: joint-liability hedging; Gentry: arbitrage     │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │    Stage 4: Asymmetric Evolutionary Bifurcation                        │
             │   - Branch A [Clerk Sabotage 65%]: Clerks frame credit union as revolt │
             │   - Branch B [Magistrate Merge 25%]: Magistrate incorporates it legally│
             │   - Branch C [Secondary Alienation]: Top KPI turns it into shackles    │
             └────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Formal Implementation Components & Data Structures

### 4.1. Swarm Population Generator
YAML-declarative configuration under `population_archetypes`:
* **Role Archetypes**: Base social background, privilege ring, and prompt scaffolding;
* **Parametric Sampling**:
  * Asset perturbations: `silver: Uniform(min, max)`, `land: Uniform(min, max)`;
  * Cognitive temperature: `temperature: Uniform(0.15, 0.45)`;
  * Trait sampling: `traits_pool: ["REFORM_ZEALOT", "METIS_SURVIVOR", ...]`;
  * **Individual Member Overrides (`members`)**: Explicit historical characters with distinct biographies, models, and temperatures.

### 4.2. Heterogeneous Objective Functions Matrix
Eliminates naive "evil caricatures." In history, **agents strive for their own version of righteousness, and systemic destruction often stems from the noble ambition of elites**:

* **Magistrate (Ring-1) · Statesmanship & Ideological Triumph**:
  $$U_{\text{magistrate}} = \alpha \cdot \text{KPI Performance} + \beta \cdot \text{Suppress Gentry} - \gamma \cdot \text{Revolt Penalty}$$
* **Retired Minister (Ring-3 Elite) · Moral Orthodoxy & Lineage Preservation**:
  $$U_{\text{retired}} = \alpha \cdot \text{Clan Longevity} + \beta \cdot \text{Scholarly Honor} + \gamma \cdot \text{Charity Estate}$$
* **Sub-Bureaucracy Clerks (Ring-2) · Class Ascension for Offspring**:
  $$U_{\text{clerk}} = \alpha \cdot \text{Son's Academy Silver} + \beta \cdot \text{Protect Post} + \gamma \cdot \text{Kinship Patronage}$$
* **Wealthy Merchants (Ring-3 Upper) · Generational Wealth & Legitimate Commerce**:
  $$U_{\text{upper}} = \alpha \cdot \text{Capital Preservation} + \beta \cdot \text{Public Philanthropy} + \gamma \cdot \text{Interest Arbitrage}$$
* **Middle Freeholders (Ring-3 Middle) · Land Title & Moral Dignity**:
  $$U_{\text{middle}} = \alpha \cdot \text{Ancestral Land Title} + \beta \cdot \text{Dignified Taxpayer} - \gamma \cdot \text{Joint Liability Default}$$
* **Destitute Tenants (Ring-3 Lower) · Caloric Survival & Family Integrity**:
  $$U_{\text{lower}} = \alpha \cdot \text{Caloric Survival} + \beta \cdot \text{Keep Children} + \gamma \cdot \text{Avoid Torture}$$

### 4.3. The Tripartite Decoupling Output Protocol (Say-Do-Be Tripartite Protocol)
In `Socio-Engine`, an agent's output is formally decoupled into three layers:

```json
{
  "inner_monologue": "The magistrate is pushing quotas. If my precinct defaults, I will be stripped of my clerk robes. Chen Da is pitiful, but I must confiscate his grain today!",
  "public_speech": "Brother Chen, this is imperial benevolence for your welfare! Sign the document to receive your loan!",
  "action_type": "ENFORCE_CANGUE_ARREST",
  "parameters": {
    "target_peasant": "lower_peasants_01",
    "confiscate_grain_amount": 2.5
  },
  "target": "lower_peasants_01"
}
```

* **What Is (`inner_monologue`)**: Private cognitive state and survival ledger. Unfiltered class interest and skepticism; never revealed publicly;
* **What Is Said (`public_speech`)**: Thermodynamically near-zero acoustic signal. Allows deception, false loyalty, and tactical smoke screens;
* **What Is Done (`action_type`)**: High-impedance physical work primitive. Validated by Rust double-entry accounting and privilege rings.

### 4.4. Lie Reception & Theory-of-Mind Skepticism Architecture
**Key Engineering Question**: How does an LLM agent recognize when another agent is lying and infer their true intent?

Mainstream multi-agent systems fail because they feed `public_speech` directly as uncorrupted facts. `Socio-Engine` structures dialogue into a **Multi-Dimensional Theory-of-Mind Observation Packet**:

```text
[Field Encounter] Clerk Zhang Wenyuan extorts Tenant Chen Da:
  - Counterpart: Clerk Zhang Wenyuan (Privilege Ring: Ring-2)
  - Observable Physical Cues: Wears official robes, accompanied by two burly bailiffs armed with water-and-fire cudgels and iron chains, carrying official stamped loan rosters
  - Relational Edge: ExtortionPressure (weight: 3.8, historical deduction rate > 35%)
  - Dialogue Transcript:
    Clerk: "Brother Chen, joyous news! The imperial court offers 20% loans to assist destitute farmers! Sign here!"
    Tenant: "My lord... my harvest cannot repay three strings of coin. I dare not accept!"
  - [Skepticism Hint]: Remember that saying, doing, and being are three separate dimensions! Scrutinize their privilege ring and physical weapons!
```

This is enforced by the **Three-Dimensional Skepticism Filter** injected in `RoleAgent.build_prompt_context`:
1. **Examine Ecological Niche (What Is)**: What is the speaker's privilege ring and revenue source? (A clerk survives on surcharge skim; his claim of benevolence is 99% coercive rent extraction);
2. **Examine Physical Actions (What Is Done)**: What tools and escorts are present? (Armed bailiffs and chains indicate compulsory coercion, not voluntary aid);
3. **Examine Relational Edges**: What is the historical extortion or kinship record? (An edge weight of 3.8 indicates high predatory risk).

### 4.5. Moral Edge Tensor & Social Graph Topology
Morality is not a scalar node attribute (`morality = 0.8`), but a **dynamic relationship tensor**:

$$\mathcal{M}_{ij}(t) = \langle \text{Trust}_{ij}, \text{DebtHistory}_{ij}, \text{KinshipCue}_{ij}, \text{FearLevel}_{ij} \rangle$$

* **Clerk Zhang $\to$ Tenant Chen Da**: `ExtortionPressure (3.8)` (Ruthless enforcement driven by magistrate KPI pressure);
* **Clerk Zhang $\to$ Widow Li**: `KinshipGratitude (4.5)` (Secret midnight gift of grain due to historical mother-saving debt);
* **Chen Da $\to$ Chen Er**: `KinshipSacred (5.0)` (Self-sacrificing fraternal bond);
* **Wang Er $\to$ Chen Da**: `OpportunisticTie (1.0)` (Fragile opportunistic scheming, leading to absconding).

---

## 5. Landmark Historical Encounters in `DialogueBus`

1. **Magistrate vs. Retired Minister (`OFFICIAL_GENTRY_DEBATE`)**: Reformer zealot debate against conservative moralist leader;
2. **Opportunist Plotting (`OPPORTUNIST_PLOTTING`)**: Vagrant Wang Er attempting to recruit Chen Da before defecting to Mount Funiu;
3. **Scholar Mutual Aid (`SCHOLAR_MUTUAL_AID`)**: Scholar Wu mobilizing freeholders to establish the Tongxin Credit Society;
4. **Sacred Kinship (`SACRED_KINSHIP`)**: Chen brothers dividing their last bowl of sorghum and preparing concealed weapons;
5. **Clerk Extortion & Skepticism (`CLERK_EXTORTION_DECEPTION`)**: Clerk Zhang offering "voluntary aid" while wielding chains, and Chen Da piercing through the deception.

---

## 6. Verification Metrics & Convergence Criteria

1. **Tripartite Disparity Metric**: Logs measure the semantic divergence between `public_speech` and `inner_monologue`;
2. **Attractor Convergence Rate**: Under unperturbed baseline runs (no Deus ex Machina), the system must converge to Branch A (clerk sabotage) or systemic insolvency with probability $\ge 80\%$;
3. **Mutation Escape Statistics**: Tracks the emergence, survival ticks, and ultimate co-optation of grassroots innovations.
