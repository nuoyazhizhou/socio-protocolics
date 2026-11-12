# Population Convergence, Four-Stage Evolution Flywheel, and Asymmetric Bifurcation (Socio-Engine v2.2)

> **Version**: v2.2-canonical | **Created**: 2026-11-12  
> **Repository Subsystem**: [Socio-Engine](../README_EN.md) | [Socio-Protocolics Whitepaper](../../en/whitepaper/chapter-01.md)  
> **Theoretical Anchors**: `SP-POSTULATE-1` (Conservation of Physical Energy), `SP-POSTULATE-2` (Autonomous Agent Postulate), `SP-RFC-004/005` (Middleware Sabotage and Rent-Seeking), `SP-RFC-018` (Evolutionary Arena & Secondary Alienation)

---

## 1. Why Swarm Scaling and the Four-Stage Evolution Flywheel (v2.2)?

In `Socio-Engine v1.0` (Hai Rui and Ming Fiscal Sandbox), simulations operated with individual representative agents (e.g., 1 magistrate, 2 clerks, 2 gentry, 3 peasants). 

This "single-instance" architecture suffered from three methodological limitations:
1. **Sample Idiosyncrasy**: Individual choices could be questioned as prompt-dependent noise;
2. **Lack of Statistical Mechanics**: Real human societies consist of stratified populations. Agents of the same class share similar structural constraints with micro-heterogeneity, exhibiting **statistical convergence** under macro institutional stress;
3. **Absence of Endogenous Evolution and Dynamic Reflexivity**: Living grassroots agents do not passively submit forever; however, grassroots self-help innovations face both sabotage by incumbent middleware (clerks) and secondary alienation once co-opted into official policy.

---

## 2. Architecture: Four-Stage Comprehensive Evolution Flywheel (v2.2)

```
                      ┌────────────────────────────────────────────────────────┐
                      │    Exogenous Shock & Peer Effects Engine (Stage 1)     │
                      │  - Neighbor aggressive quota promotion / Neighbor riot │
                      │  - Natural disasters (locusts/drought) / Price crashes │
                      └───────────────────────────┬────────────────────────────┘
                                                  │ Broadcasts local ambient state
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │                Mental Polarity Operator (Stage 2)                      │
             │   [Desperation Mode: Fury]                 [Preservation Mode: Mercy]  │
             │   - Trigger: Starvation line / Arrest      - Trigger: Peer rebellion   │
             │   - Action: Armed revolt, ledger burning   - Action: Silent slack-off  │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │            Micro-Innovation Mutation Pool (Stage 3)                    │
             │   - 5th-Grade Peasants: 5-man credit unions, forward crop sales        │
             │   - Middle Peasants: Joint-liability exclusion alliances               │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │       Evolutionary Bifurcation & Asymmetric Game (Stage 4)             │
             │   - Branch A [Clerk Sabotage 65%]: Clerks suppress unions as "illegal" │
             │   - Branch B [Enlightened Merge 25%]: Magistrate adopts credit union   │
             │   - Branch C [Secondary Alienation]: Top KPI turns union into tyranny  │
             └────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Implementation Components & Formal Data Structures

To bridge the gap between architecture and production code, responsibilities are partitioned between the **Rust Physical Ledger Kernel** and the **Python Cognitive Orchestration Layer**:

### 3.1. Swarm Population Generator
Supports declarative archetype instantiation in YAML:
* **Archetype**: Base character persona, privilege ring, and behavioral prompts;
* **Parametric Sampling**:
  * Micro-asset perturbation: `silver: Uniform(min, max)`, `land: Uniform(min, max)`;
  * Risk aversion perturbation: `risk_aversion: Normal(mean, std)`;
  * Cognitive temperature perturbation: `temperature: Uniform(0.15, 0.45)`.

### 3.2. Exogenous Shock Engine
Shocks inject tangible parameters into the simulation environment:

```yaml
# Exogenous Shocks & Peer Effects Specification (Flywheel Stage 1)
exogenous_shocks:
  neighbor_promotion_event:
    probability: 0.25
    effect_on_magistrate_kpi: +0.15      # Neighbor promoted for 120% quota, spiking magistrate KPI anxiety
  neighbor_rebellion_event:
    probability: 0.25
    effect_on_clerk_fear: +0.60          # Neighbor riot and clerk murder spikes clerk fear index
  climate_locust_drought:
    probability: 0.20
    yield_multiplier: 0.55               # Severe drought/locusts reduces yields by 45%
  bumper_price_crash:
    probability: 0.20
    grain_price_multiplier: 0.60         # Grain price crashes, cutting off silver liquidity
```

### 3.3. Mental Polarity Operator
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
```

### 3.4. Unified Innovation Mutation Pool
Grounded in historical Song Dynasty realities with unified action IDs:
* **5th-Grade Peasants (Destitute / Tenants)**:
  * `MUTATION_UNDERGROUND_CREDIT_POOL`: **5-Man Grassroots Credit Union** (informal rotating savings and credit association);
  * `MUTATION_FORWARD_GRAIN_SALE`: **Forward Crop Discounting** (selling future autumn yields at a discount during spring hunger to obtain immediate silver);
  * `MUTATION_COLLECTIVE_PETITION`: **Collective Shrine Petitioning** (appealing against uncodified surcharge fees);
* **Middle Peasants (Freeholders)**:
  * `MUTATION_JOINT_LIABILITY_HEDGE`: **Joint-Liability Exclusion Alliance** (refusing to guarantee unknown migrants);
* **Upper Gentry (Large Landlords)**:
  * `MUTATION_REGULATORY_ARBITRAGE`: **Intertemporal Regulatory Arbitrage** (borrowing official credit at 20% and relending at 50%+).

### 3.5. Evolutionary Bifurcation Outcomes
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

### 3.6. Rigid Boundary Between Rust Kernel and Python Scheduler
* **Python Orchestration**: Prompt assembly, shock sampling, mental polarity evaluation, and mutation routing;
* **Rust `socio_core` Kernel**: **Inviolable thermodynamic gatekeeper**. Enforces strict double-entry ledger balancing (silver/grain conservation), privilege-ring authorization checks (Ring-3 barred from writing public ledgers), and physical asset execution. If an LLM hallucinates unbacked assets, the Rust kernel aborts the transaction with `TransactionReverted`.

---

## 4. Benchmark Scenario: Northern Song Green Sprouts Reform (`W-SIM-01`)

* **Historical Coordinates**: Kaifeng Xiangfu County (1070–1071 CE);
* **Stratified Swarm (21 Agents)**:
  * **Ring-1**: 1 Commissioner / Magistrate (under intense KPI pressure from Emperor Shenzong);
  * **Ring-2**: 2 Sub-bureaucracy Clerks (extracting surcharges and paperwork fees);
  * **Ring-3 (Upper)**: 3 Wealthy Gentry (large landholdings, engaging in arbitrage);
  * **Ring-3 (Middle)**: 5 Freeholders (15–20 mu, coerced into joint-liability guarantors);
  * **Ring-3 (Lower)**: 10 5th-Grade Destitute Peasants (subsistence grain near starvation, facing forced loans).

---

## 5. Implementation Roadmap

1. **Step 1**: Embed full exogenous shocks, mental thresholds, and bifurcation blocks into `sim_config_wang_an_shi.yaml`;
2. **Step 2**: Fully implement the four-stage flywheel and bifurcation logic in `socio_engine/core/evolution_engine.py`;
3. **Step 3**: Integrate complete Rust physical ledger validation and bifurcation reporting into `socio_engine/run_simulation.py`;
4. **Step 4**: Execute benchmark runs and generate the *Northern Song Green Sprouts Swarm Convergence and Bifurcation Report*.
