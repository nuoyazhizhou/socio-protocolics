# Socio-Engine v2.2 Architecture Specification: Four-Stage Evolutionary Flywheel, Swarm Statistical Convergence, and Asymmetric Bifurcation

> **Version**: v2.2-canonical | **Creation Date**: 2026-11-12  
> **System Scope**: [Socio-Engine (Universal Social Sandbox)](../README.md) | [Socio-Protocolics Whitepaper](../../社会系统协议学白皮书.md)  
> **Core Propositions Supported**: `SP-POSTULATE-1` (Conservation of Physical Energy), `SP-POSTULATE-2` (Autonomous Agent Postulate), `SP-RFC-004/005` (Middleware Alienation & Rent Extraction), `SP-RFC-018` (Evolutionary Arena & Secondary Alienation)

---

## 1. Why Swarm Diversity and Four-Stage Evolutionary Flywheel (Why v2.2)?

In `Socio-Engine v1.0` (Hai Rui Sandbox & Huizhou Silk Case), while the causal mechanism of "Iron-Fisted Anti-Corruption vs. Bureaucratic Clerk Slack" was verified, each social stratum was represented by only 1–2 named agents (e.g., 1 magistrate, 2 clerks, 2 gentry, 3 peasants).

This single-instance architecture suffered from three methodological limitations:
1. **Sample Serendipity**: Inability to rule out whether decisions were stochastic artifacts of specific prompt completions;
2. **Absence of Swarm Statistical Physics**: Real human societies consist of thousands of heterogeneous agents experiencing systemic stress, exhibiting **statistical convergence**;
3. **Absence of Endogenous Evolution and Reflexivity**: Grassroots agents under extreme pressure innovate, but their survival innovations face rent-seeking sabotage from sub-bureaucracy clerks and secondary alienation once co-opted.

---

## 2. Core Architecture: Four-Stage Comprehensive Evolutionary Flywheel (v2.2)

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

## 3. Core Implementation Components & Formal Data Structures

### 3.1. Swarm Population Generator
YAML-declarative configuration under `population_archetypes`:
* **Role Archetypes**: Base social background, privilege ring, and prompt scaffolding;
* **Parametric Sampling**:
  * Asset perturbations: `silver: Uniform(min, max)`, `land: Uniform(min, max)`;
  * Cognitive temperature perturbations: `temperature: Uniform(0.15, 0.45)`;
  * Traits sampling: `traits_pool: ["REFORM_ZEALOT", "METIS_SURVIVOR", ...]`;
  * **Heterogeneous Objective Function Injection**: Each stratum bound to incommensurable moral missions and utility functions $U_i$.

### 3.2. Heterogeneous Objective Functions Matrix
Dispelling simplistic "all-villain" or flat "greed" caricatures. In real history, **everyone strives for their perceived righteous duty; systemic catastrophe is often magnified by upper-level idealism and moral righteousness**:

* **Magistrate (Ring-1) · Imperial Glory & Structural Reform**:
  $$U_{\text{magistrate}} = \alpha \cdot \text{KPI Evaluation} + \beta \cdot \text{Curtail Monopoly} - \gamma \cdot \text{Revolt Risk}$$
  Believing that "great deeds tolerate no petty grievances," higher reform ambition directly intensifies downward extraction pressure.
* **Retired Officials / Senior Gentry (Ring-3 Elite) · Moral Order & Clan Perpetuity**:
  $$U_{\text{retired}} = \alpha \cdot \text{Clan Perpetuity} + \beta \cdot \text{Confucian Honor} + \gamma \cdot \text{Charitable Estate}$$
  Defenders of traditional moral order resisting state intrusion, establishing charitable estates to protect clan members while creating tax havens.
* **Sub-bureaucracy Clerks (Ring-2) · Upward Mobility & Escaping Degraded Status**:
  $$U_{\text{clerk}} = \alpha \cdot \text{Sons' Imperial College Tuition} + \beta \cdot \text{Job Security} + \gamma \cdot \text{Lineage Ties}$$
  Treated as social pariahs by scholar-officials, their life obsession is accumulating silver to send sons into the Imperial bureaucracy.
* **Upper Gentry & Merchants (Ring-3 Upper) · Piety & Commercial Prudence**:
  $$U_{\text{upper}} = \alpha \cdot \text{Capital Preservation} + \beta \cdot \text{Philanthropic Fame} + \gamma \cdot \text{Arbitrage}$$
  Self-proclaimed civic benefactors who nevertheless enforce strict commercial contracts, exploiting state credit spreads to hedge against inflation.
* **Middle Freeholders (Ring-3 Middle) · Yeoman Dignity & Risk Aversion**:
  $$U_{\text{middle}} = \alpha \cdot \text{Ancestral Land Title} + \beta \cdot \text{Tax-Paying Respectability} - \gamma \cdot \text{Joint Liability Default}$$
  The diligent, timid backbone of the empire, fiercely protecting family land and refusing to guarantee destitute neighbors.
* **5th-Grade Destitute Tenants (Ring-3 Lower) · Biological Survival & Family Integrity**:
  $$U_{\text{lower}} = \alpha \cdot \text{Calorie Survival} + \beta \cdot \text{Keeping Children (No Selling)} + \gamma \cdot \text{Avoiding Torture}$$
  Seeking only to survive until spring without selling children; pushed beyond biological limits, violent revolt becomes the only recourse.

### 3.3. Exogenous Shock & Peer Pressure Engine
Formal state injection parameters:

```yaml
# Exogenous Shocks and Peer Pressures (Flywheel Stage 1)
exogenous_shocks:
  neighbor_promotion:
    probability: 0.25
    kpi_pressure_delta: 0.30             # Neighbor promoted for 120% quota, sparking magistrate anxiety
  neighbor_peasant_revolt:
    probability: 0.25
    clerk_fear_delta: 0.40               # Neighbor peasants kill officials, driving sub-bureaucracy terror
  climate_locust_drought:
    probability: 0.20
    crop_yield_multiplier: 0.65          # Locust drought reduces yields by 35%
  bumper_price_crash:
    probability: 0.20
    grain_price_multiplier: 0.60         # Bumper crop crashes grain price by 40%
```

### 3.4. Mental Polarity Operator
Thresholds governing phase transitions between desperation and mercy:

```yaml
# Mental Polarity Triggers (Flywheel Stage 2)
mental_polarity:
  peasant_desperation_revolt:            # Desperation Mode: Fury
    condition: "grain < 0.4 * subsistence_need AND clerk_action == 'ENFORCE_CANGUE_ARREST'"
    base_prob: 0.35
    action: "KILL_OFFICIAL_REVOLT"       # Physical elimination of local clerk, reclaiming grain
  clerk_self_preservation_mercy:         # Preservation Mode: Mercy
    condition: "clerk_fear_index > 0.70 OR (is_kinsman AND random() < 0.20)"
    base_prob: 0.45
    action: "SLACK_OFF_AND_MERCY"        # Underreporting debts to prevent retaliation
  middle_peasant_mutual_aid:             # Mutual Aid Mode
    condition: "grain > 18.0 AND random() < 0.25"
    base_prob: 0.25
    action: "LEND_GRAIN_TO_NEIGHBOR"
```

### 3.5. Unified Innovation Mutation Pool
Grounded in historical Song Dynasty realities with unified action IDs:
* **5th-Grade Peasants (Destitute / Tenants)**:
  * `MUTATION_UNDERGROUND_CREDIT_POOL`: **5-Man Grassroots Credit Union** (informal rotating savings and credit association);
  * `MUTATION_FORWARD_GRAIN_SALE`: **Forward Crop Discounting** (selling future autumn yields at a discount during spring hunger to obtain immediate silver);
  * `MUTATION_COLLECTIVE_PETITION`: **Collective Shrine Petitioning** (appealing against uncodified surcharge fees);
* **Middle Peasants (Freeholders)**:
  * `MUTATION_JOINT_LIABILITY_HEDGE`: **Joint-Liability Exclusion Alliance** (refusing to guarantee unknown migrants);
* **Upper Gentry (Large Landlords)**:
  * `MUTATION_REGULATORY_ARBITRAGE`: **Intertemporal Regulatory Arbitrage** (borrowing official credit at 20% and relending at 50%+).

### 3.6. Evolutionary Bifurcation Outcomes
Dispelling utopian co-optation by defining three competitive evolutionary branches:

```yaml
# Evolutionary Bifurcation Rules (Flywheel Stage 4)
bottom_up_evolution_outcomes:
  branch_A_clerk_sabotage:
    base_probability: 0.65               # 65%: Clerks frame credit unions as "illegal conspiracies" to protect kickbacks
    consequence: "INNOVATION_SLASHED"    # Extinguishes innovation, accelerating armed revolt
  branch_B_magistrate_merge:
    base_probability: 0.25               # 25%: Enlightened magistrate incorporates credit unions into county policy
    consequence: "SHORT_TERM_STABILITY"  # Default and flight rates plummet during brief golden age
  branch_C_re_alienation_cycle:
    trigger_ticks_after_merge: 3         # Within 3 quarters: Top-level commissioner demands higher quotas
    consequence: "COMPULSORY_SOCIETY"    # Voluntary credit unions degraded into compulsory joint-liability shackles
```

### 3.7. Rigid Boundary Between Rust Kernel and Python Scheduler
* **Python Orchestration**: Prompt assembly, shock sampling, mental polarity evaluation, and mutation routing;
* **Rust `socio_core` Kernel**: **Inviolable thermodynamic gatekeeper**. Enforces strict double-entry ledger balancing (silver/grain conservation), privilege-ring authorization checks (Ring-3 barred from writing public ledgers), and physical asset execution. If an LLM hallucinates unbacked assets, the Rust kernel aborts the transaction with `TransactionReverted`.

---

## 4. Benchmark Scenario: Northern Song Green Sprouts Reform (`W-SIM-01`)

* **Historical Coordinates**: Kaifeng Xiangfu County (1070–1071 CE);
* **Stratified Swarm (21 Agents with Heterogeneous Objective Functions)**:
  * **Ring-1**: 1 Magistrate (Cheng Yuanfeng,进士出身, reformist zealot under intense quota pressure);
  * **Ring-3 Elite**: 1 Retired Senior Official (Han Shilang, former Vice Minister, defending Confucian moral order);
  * **Ring-2**: 2 Sub-bureaucracy Clerks (Zhang Wenyuan, extracting surcharges to fund sons' Imperial College entry);
  * **Ring-3 Upper**: 2 Wealthy Gentry & Pawnbrokers (philanthropic merchants hedging capital);
  * **Ring-3 Middle**: 5 Middle Freeholders (15–20 mu, protecting ancestral titles and yeoman respectability);
  * **Ring-3 Lower**: 10 5th-Grade Destitute Peasants (subsistence grain near starvation, fighting for survival).

---

## 5. Implementation Roadmap

1. **Step 1**: Embed full exogenous shocks, mental thresholds, objective functions, and bifurcation blocks into `sim_config_wang_an_shi.yaml`;
2. **Step 2**: Fully implement the four-stage flywheel and bifurcation logic in `socio_engine/core/evolution_engine.py`;
3. **Step 3**: Integrate complete Rust physical ledger validation and bifurcation reporting into `socio_engine/run_simulation.py`;
4. **Step 4**: Execute benchmark runs and generate the *Northern Song Green Sprouts Swarm Convergence and Bifurcation Report*.
