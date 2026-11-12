# Socio-Engine v2.2 架构升级规范：四阶演化飞轮、群体统计趋同与非对称演化分叉

> **版本**：v2.2-canonical｜**创建日期**：2026-11-12  
> **所属体系**：[Socio-Engine (通用社会系统沙盘)](../README.md)｜[社会系统协议学白皮书](../../社会系统协议学白皮书.md)  
> **核心命题支持**：`SP-POSTULATE-1`（物理能量守恒）、`SP-POSTULATE-2`（自博弈公设）、`SP-RFC-004/005`（中介异化与寻租绞杀）、`SP-RFC-018`（演化赛马场与二次异化）

---

## 一、 为什么必须推进群体多样性与四阶演化飞轮（Why v2.2）？

在 `Socio-Engine v1.0`（海瑞沙盘与徽州丝绢案）中，沙盘虽然验证了“铁腕反腐 vs 书吏怠工”的因果机制，但每个阶层基本只有 1~2 个具名 Agent 代表（如 1 个知县、2 个书吏、2 个乡绅、3 个贫农）。

这种“单实例”架构存在三大方法论局限：
1. **样本偶发性质疑**：无法排除单次决策是特定 Prompt 生成的随机偶然；
2. **缺乏群体统计物理特性**：真实社会由成千上万个微观主体构成，同阶层内部存在微小的异质性（性格、微量资产差异），且面临共同系统压力时会表现出**统计学意义上的“趋同收敛（Convergence）”**；
3. **缺乏内生演化创新与动态反身性**：真实历史中的基层个体不会永远被动受锤，但民间在绝境中的自救创新，往往既面临中介层（胥吏）的既得利益剿杀，也面临制度合并后的二次异化。

---

## 二、 核心架构设计：四阶综合演化飞轮模型 (v2.2)

```
                      ┌────────────────────────────────────────────────────────┐
                      │    外部异动与同侪压力生成器 (Exogenous Shock Engine)    │
                      │  - 邻县极端执行升官 (刺激加码) / 邻县杀官造反 (震慑放水) │
                      │  - 自然物理冲击 (连旱蝗灾减产 / 大丰收谷贱伤农现金断裂) │
                      └───────────────────────────┬────────────────────────────┘
                                                  │ 广播当季外部时局
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │                双极心智极化算子 (Mental Polarity Operator)             │
             │   【极恶模式: 恶向胆边生】                 【极善/自保: 恻隐与怕走夜路】   │
             │   - 触发: 仓底见底/差役上枷/逼入死地       - 触发: 邻县杀官/恐惧报复         │
             │   - 动作: 柴刀杀官夺粮、火烧账册           - 动作: 偷划底册、少记二斗、放水   │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │            微观灵光一闪与变异探索池 (Innovation Mutation Pool)           │
             │   - 五等穷农: 五人自发结会拼单贷、指苗预卖套现、长跪哭庙抗辩             │
             │   - 中等自耕农: 保结对冲排他同盟；大户地主: 跨期官民利差套利            │
             └────────────────────────────────────┬───────────────────────────────────┘
                                                  ▼
             ┌────────────────────────────────────────────────────────────────────────┐
             │       第四阶：演化分叉口与非对称博弈 (Evolutionary Bifurcation)        │
             │   - 分支 A [中介绞杀 65%]: 胥吏诬告"私相结社、抗拒新法"，调差役扑灭     │
             │   - 分支 B [开明稳态 25%]: 县令顶住阻力吸收民间方案，迎来短暂黄金期     │
             │   - 分支 C [二次异化]: 顶层 KPI 加码，自愿互助退化为"官办强制五人连坐" │
             └────────────────────────────────────────────────────────────────────────┘
```

---

## 三、 核心实现组件与形式化数据结构

为了使四阶飞轮严丝合缝地落地执行，代码架构划分为 **Rust 物理会计内核** 与 **Python 认知调度层**：

### 1. 规模化群体生成器（Swarm Population Generator）
在 YAML 配置中支持 `population_archetypes` 声明式定义：
* **角色原型（Archetype）**：定义核心阶层背景、特权环与提示词基底；
* **参数分布采样（Parametric Sampling）**：
  * 资产微扰：`silver: Uniform(min, max)`，`land: Uniform(min, max)`；
  * 风险偏好微扰：`risk_aversion: Normal(mean, std)`；
  * 认知温度微扰：`temperature: Uniform(0.15, 0.45)`。

### 2. 外部异动与同侪压力广播（Exogenous Shock Engine）
外部冲击不再是空泛的文字描述，而是直接以形式化参数注入世界状态：

```yaml
# 外部异动与同侪压力配置规范 (飞轮第一阶)
exogenous_shocks:
  neighbor_promotion_event:
    probability: 0.25
    effect_on_magistrate_kpi: +0.15      # 邻县因 120% 极端抑配获御批升官，推高知县 KPI 焦虑
  neighbor_rebellion_event:
    probability: 0.25
    effect_on_clerk_fear: +0.60          # 邻县爆发杀官围衙民变，大幅推高胥吏恐惧值
  climate_locust_drought:
    probability: 0.20
    yield_multiplier: 0.55               # 蝗旱灾害：全县农田减产 45%
  bumper_price_crash:
    probability: 0.20
    grain_price_multiplier: 0.60         # 谷贱伤农：粮价暴跌导致现银兑换现金流断裂
```

### 3. 双极心智极化算子（Mental Polarity Operator）
微观状态与宏观恐惧指数共同决定个体的相变阈值：

```yaml
# 双极心智极化触发条件 (飞轮第二阶)
mental_polarity:
  peasant_desperation_revolt:            # 极恶模式：恶向胆边生
    condition: "grain < 0.4 * subsistence_need AND clerk_action == 'ENFORCE_CANGUE_ARREST'"
    base_prob: 0.35
    action: "KILL_OFFICIAL_REVOLT"       # 物理消灭微观中介，柴刀夺粮
  clerk_self_preservation_mercy:         # 极善/自保模式：恻隐与怕走夜路
    condition: "clerk_fear_index > 0.70 OR (is_kinsman AND random() < 0.20)"
    base_prob: 0.45
    action: "SLACK_OFF_AND_MERCY"        # 暗中划销底册、少记二斗，释放系统排污阀
```

### 4. 统一的变异与灵光一闪策略池（Innovation Mutation Pool）
严格尊重北宋社会经济史实，统一枚举 ID：
* **五等户（赤贫/佃农）**：
  * `MUTATION_UNDERGROUND_CREDIT_POOL`：**五人结会拼单贷**（民间微额互保金融雏形，拼凑本金周转小买卖）；
  * `MUTATION_FORWARD_GRAIN_SALE`：**指苗预卖（青黄不接时私下折价预卖秋收期谷，获取即期白银）**；
  * `MUTATION_COLLECTIVE_PETITION`：**宗族联名哭庙与长跪御史**（越级抗辩官吏私加头子钱）；
* **三、四等户（自耕农）**：
  * `MUTATION_JOINT_LIABILITY_HEDGE`：**保结排他自保同盟**（私下立约拒为不知底细流民作保）；
* **一、二等户（大地主/富商）**：
  * `MUTATION_REGULATORY_ARBITRAGE`：**跨期官民利差套利**（冒领低息官银，转手高息放贷）。

### 5. 演化分叉口与非对称博弈（Bifurcation Outcomes）
彻底破除“大团圆式主干合并”的单向度幻想，严格落实三条竞争分支：

```yaml
# 演化分叉判定规则 (飞轮第四阶)
bottom_up_evolution_outcomes:
  branch_A_clerk_sabotage:
    base_probability: 0.65               # 概率 65%：胥吏为保住火耗与头子钱，诬告互助组"私相结社、图谋抗税"予以扑灭
    consequence: "INNOVATION_SLASHED"    # 创新火种熄灭，激化底层矛盾，加速滑向杀官造反
  branch_B_magistrate_merge:
    base_probability: 0.25               # 概率 25%：开明知县顶住胥吏阻挠，正式将自愿结会纳入官法
    consequence: "SHORT_TERM_STABILITY"  # 坏账与逃亡率大幅下降，迎来短暂黄金期
  branch_C_re_alienation_cycle:
    trigger_ticks_after_merge: 3         # 合并后 3 个季度内：顶层提举司下达递增指标
    consequence: "COMPULSORY_SOCIETY"    # 自愿结会重新异化为官办强制五人连坐，民间智慧被彻底污染
```

### 6. Rust 物理内核与 Python 调度层的刚性边界
* **Python 调度层职责**：运行 LLM 提示词注入、采样外部冲击、评估心智相变与变异策略生成；
* **Rust `socio_core` 内核职责**：**不可逾越的物理守恒闸门**。负责双式记账校验（银粮总额守恒）、特权环门禁鉴权（Ring-3 禁止写公共账本）、以及执行 `engine.execute_action()` 扣减微观资产；若 LLM 产出虚假资产，Rust 内核直接抛出 `TransactionReverted` 异常强行拒绝！

---

## 四、 首发落地的历史实验剧本：北宋王安石青苗法（`W-SIM-01`）

* **历史坐标**：北宋开封府祥符县（熙宁三年至四年，1070–1071 年）；
* **群体阶层设计（21 人异质性集群）**：
  * **Ring-1 提举官与县令（1人）**：面临神宗考成升迁考核；
  * **Ring-2 县衙钱谷公吏（2人）**：收取头子钱与纸笔银，负责具体放贷回笼；
  * **Ring-3 上等户大姓员外（3人）**：良田数百亩，玩转利差套利；
  * **Ring-3 中等自耕农（5人）**：十五至二十亩薄田，被强制拉来充当青苗保结连坐清偿人；
  * **Ring-3 下等五等佃农（10人）**：口粮濒临 3.0 石饿毙线，面临暴力抑配借贷。

---

## 五、 后续实施路线图

1. **Step 1**：在 `sim_config_wang_an_shi.yaml` 中完备录入外部异动、心智阈值与演化分叉配置块；
2. **Step 2**：在 `socio_engine/core/evolution_engine.py` 中完整实现四阶飞轮与分叉判定逻辑；
3. **Step 3**：在 `socio_engine/run_simulation.py` 中接入完整的 Rust 物理会计校验与分叉报告输出；
4. **Step 4**：运行推演实验，产出《北宋熙宁青苗法群体趋同与演化分叉推演报告》。
