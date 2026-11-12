# Population Convergence and Mutation Architecture (Socio-Engine v2.0)

> **Version**: v2.0-draft | **Created**: 2026-11-12  
> **Repository Subsystem**: [Socio-Engine](../README_EN.md) | [Socio-Protocolics Whitepaper](../../en/whitepaper/chapter-01.md)  
> **Theoretical Anchors**: `SP-POSTULATE-2` (Autonomous Agent Postulate), `SP-RFC-004/005` (Middleware Alienation), `SP-RFC-018` (Evolutionary Arena)

---

## 1. Why Population Scaling and Mutation Engines (v2.0)?

In `Socio-Engine v1.0` (Hai Rui and Ming Fiscal Sandbox), simulations operated with individual representative agents (e.g., 1 magistrate, 2 clerks, 2 gentry, 3 peasants). 

While proving the causal dynamics of anti-corruption versus bureaucratic pushback, this design suffered from two methodological limitations:
1. **Sample Idiosyncrasy**: Individual choices could be questioned as prompt-dependent noise;
2. **Lack of Statistical Mechanics**: Real human societies consist of stratified populations. Agents of the same class share similar structural constraints with micro-heterogeneity, exhibiting **statistical convergence** under macro institutional stress;
3. **Absence of Endogenous Innovation**: Living grassroots agents do not passively submit forever; a minority endowed with high risk tolerance occasionally experience an **"innovation spark (mutation)"** to break systemic deadlocks.

---

## 2. Architecture: Three-Tier Swarm Evolutionary Model

```
                      ┌──────────────────────────────────────────────┐
                      │      Socio-Engine v2.0 Swarm Scheduler       │
                      └──────────────────────┬───────────────────────┘
                                             │
             ┌───────────────────────────────┼──────────────────────────────┐
             ▼                               ▼                              ▼
    [Kernel & Middleware (Ring-0/1/2)]    [Stratified Swarm (Ring-3)]      [Evolutionary Mutation]
   - Magistrate / Imperial Commissioner   - Upper-class Gentry (3-5)       - ε-exploration rate (5%~10%)
   - Sub-bureaucracy Clerks / Headmen    - Middle Freeholders (5-8)       - "Innovation Spark" action pool
                                         - Lower 5th-Grade Peasants (10-15)- Neighborhood imitation & memes
             │                               │                              │
             └───────────────────────────────┼──────────────────────────────┘
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │    Rust Physical Ledger + Convergence Stats  │
                      │  - Gini index / Default rate time-series     │
                      │  - Convergence metrics: HHI / Action entropy │
                      │  - Innovation survival and slashing tracking │
                      └──────────────────────────────────────────────┘
```

---

## 3. Core Engine Components

### 3.1. Swarm Population Generator
Supports declarative archetype instantiation in YAML:
* **Archetype**: Base character persona, privilege ring, and behavioral prompts;
* **Parametric Sampling**:
  * Micro-asset perturbation: `silver: Uniform(1.0, 3.0)`, `land: Uniform(2.0, 5.0)`;
  * Risk aversion perturbation: `risk_aversion: Normal(2.25, 0.3)`;
  * Cognitive temperature perturbation: `temperature: Uniform(0.2, 0.6)`.

### 3.2. Evolutionary Mutation and Innovation Pool
Introduces an exploration probability $\epsilon$ (default 8%):
* Standard actions: `APPLY_LOAN`, `REFUSE_LOAN`, `PAY_BACK`, `FLEE`;
* **Triggered Mutation ($\text{rand}() < \epsilon$)**:
  * **Strategy A (Underground Grassroots Credit Pools)**: Micro-agents pooling loans to hedge against extortion;
  * **Strategy B (Informal Commodity Notes)**: Arbitrage by converting official grain pledges into shadow market liquidity;
  * **Strategy C (Asymmetric Collective Appeal)**: Grassroots petitioning leveraging filial or distress norms;
* **Evolutionary Selection**: If a mutation improves 2-quarter survival without being suppressed (slashed), it triggers **social imitation (Meme diffusion)** among neighbors.

### 3.3. Statistical Convergence Metrics
At the end of each simulated quarter, the system writes to SQLite `socio_sim.db`:
* **Action Entropy**: Measuring behavioral dispersion versus lockstep convergence;
* **Default Concentration**: The quarter in which lower-tier peasants converge (>80%) on uniform default/flight;
* **Mutation Survival Rate**: Percentage of innovative strategies successfully incorporated versus crushed.

---

## 4. Benchmark Scenario: Northern Song Green Sprouts Reform (`W-SIM-01`)

* **Historical Baseline**: Kaifeng Xiangfu County, 1070 CE;
* **Stratified Swarm**:
  * **Ring-1**: Commissioner & Magistrate (quota and interest return pressure);
  * **Ring-2**: Sub-bureaucracy Clerks (kickback extraction);
  * **Ring-3 (Upper)**: 3-5 Large Landowners (usury, state credit arbitrage);
  * **Ring-3 (Middle)**: 5-8 Freeholders (compulsory joint liability guarantors);
  * **Ring-3 (Lower)**: 10-15 5th-Grade Destitute Peasants (mandatory forced borrowing);
  * **Ring-3 (Town)**: 3-5 Urban Shopkeepers (monopoly market pressure under Shi Yi Fa).
