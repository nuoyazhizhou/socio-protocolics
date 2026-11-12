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
  * 认知温度微扰：`temperature: Uniform(0.15, 0.45)`；
  * 性情池随机抽取：`traits_pool: ["REFORM_ZEALOT", "METIS_SURVIVOR", ...]`;
  * **异质目标函数注入**：每个阶级绑定不可通约的正道执念与效用函数 $U_i$。

### 2. 阶级异质目标函数矩阵（Heterogeneous Objective Functions Matrix）
彻底破除“全员恶人”或“脸谱化贪婪”的浅薄建模。真实历史中，**每个人都在为自己的“正道”拼尽全力，系统的毁灭性往往恰恰来自上位者的崇高事业心与道德正义感**：

* **知县 (Ring-1) · 致君尧舜与变法图强**：
  $$U_{\text{magistrate}} = \alpha \cdot \text{考成政绩} + \beta \cdot \text{摧抑兼并} - \gamma \cdot \text{民变扣分}$$
  坚信“成大事者不恤小怨”，越有事业心，越容易向下层层加码，将官僚机器压榨潜能拉满。
* **致仕退官/乡绅 (Ring-3 顶层) · 护持道统与宗族千秋**：
  $$U_{\text{retired}} = \alpha \cdot \text{宗族永续} + \beta \cdot \text{士林清议} + \gamma \cdot \text{义庄义田规模}$$
  自认天下斯文与道德良心，抗击新法“与民争利”，置办义田庇荫族人，却在客观上形成了抗税避风港。
* **经管钱吏 (Ring-2) · 洗刷吏籍与家族跃迁**：
  $$U_{\text{clerk}} = \alpha \cdot \text{子弟太学捐纳银} + \beta \cdot \text{保全铁饭碗} + \gamma \cdot \text{乡党人情香火}$$
  祖孙三代为贱民走狗，毕生夙愿是攒足银两送幼子应试中举。公事公办是自保，收取头子钱是为子谋身。
* **一、二等大户商贾 (Ring-3 上等) · 积善传家与在商言商**：
  $$U_{\text{upper}} = \alpha \cdot \text{资财增殖保全} + \beta \cdot \text{修桥造桥善名} + \gamma \cdot \text{官民息差套现}$$
  自命乐善好施，但借贷经商信奉契约白纸黑字，必须收回本息；善于利用特权低吸高放以抗通胀。
* **三、四等中等自耕农 (Ring-3 中等) · 耕读家风与死守体面**：
  $$U_{\text{middle}} = \alpha \cdot \text{祖传田契所有权} + \beta \cdot \text{完税不涉公堂体面} - \gamma \cdot \text{被穷保连坐破产}$$
  帝国最勤勉也最胆怯的基石。宁可独善其身，绝不替穷邻连坐担责，生怕跌入佃农阶层受全村耻笑。
* **五等下等赤贫佃农 (Ring-3 下等) · 骨肉保全与生命底线**：
  $$U_{\text{lower}} = \alpha \cdot \text{热量维持(防饿死)} + \beta \cdot \text{骨肉不离散(不卖儿)} + \gamma \cdot \text{免受严刑}$$
  只求全家活着见到开春，绝境中生发微型互助；若被逼到绝路，天理良心下唯有柴刀掀桌。

### 3. 外部异动与同侪压力广播（Exogenous Shock Engine）
外部冲击直接以形式化参数注入世界状态：

```yaml
# 外部异动与同侪压力配置规范 (飞轮第一阶)
exogenous_shocks:
  neighbor_promotion:
    probability: 0.25
    kpi_pressure_delta: 0.30             # 隔壁县令 120% 达标升官，引发本县知县同侪恐慌
  neighbor_peasant_revolt:
    probability: 0.25
    clerk_fear_delta: 0.40               # 隔壁县严苛逼债激起民变杀官，基层吏员怕走夜路
  climate_locust_drought:
    probability: 0.20
    crop_yield_multiplier: 0.65          # 蝗旱灾害导致收成骤降 35%
  bumper_price_crash:
    probability: 0.20
    grain_price_multiplier: 0.60         # 谷贱伤农：粮价暴跌导致现银兑换现金流断裂
```

### 4. 双极心智极化算子（Mental Polarity Operator）
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
  middle_peasant_mutual_aid:             # 守望相助模式
    condition: "grain > 18.0 AND random() < 0.25"
    base_prob: 0.25
    action: "LEND_GRAIN_TO_NEIGHBOR"
```

### 5. 统一的变异与灵光一闪策略池（Innovation Mutation Pool）
严格尊重北宋社会经济史实，统一枚举 ID：
* **五等户（赤贫/佃农）**：
  * `MUTATION_UNDERGROUND_CREDIT_POOL`：**五人结会拼单贷**（民间微额互保金融雏形，拼凑本金周转小买卖）；
  * `MUTATION_FORWARD_GRAIN_SALE`：**指苗预卖（青黄不接时私下折价预卖秋收期谷，获取即期白银）**；
  * `MUTATION_COLLECTIVE_PETITION`：**宗族联名哭庙与长跪御史**（越级抗辩官吏私加头子钱）；
* **三、四等户（自耕农）**：
  * `MUTATION_JOINT_LIABILITY_HEDGE`：**保结排他自保同盟**（私下立约拒为不知底细流民作保）；
* **一、二等户（大地主/富商）**：
  * `MUTATION_REGULATORY_ARBITRAGE`：**跨期官民利差套利**（冒领低息官银，转手高息放贷）。

### 6. 演化分叉口与非对称博弈（Bifurcation Outcomes）
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

### 7. Rust 物理内核与 Python 调度层的刚性边界
* **Python 调度层职责**：运行 LLM 提示词注入、采样外部冲击、评估心智相变与变异策略生成；
* **Rust `socio_core` 内核职责**：**不可逾越的物理守恒闸门**。负责双式记账校验（银粮总额守恒）、特权环门禁鉴权（Ring-3 禁止写公共账本）、以及执行 `engine.execute_action()` 扣减微观资产；若 LLM 产出虚假资产，Rust 内核直接抛出 `TransactionReverted` 异常强行拒绝！

---

## 四、 首发落地的历史实验剧本：北宋王安石青苗法（`W-SIM-01`）

* **历史坐标**：北宋开封府祥符县（熙宁三年至四年，1070–1071 年）；
* **群体阶层设计（21 人异质性集群，全员各具独特生命史与目标函数）**：
  * **Ring-1 提举官与县令（1人）**：祥符知县程元凤，进士出身，王安石新党中坚，面临考成重压；
  * **Ring-3 顶层致仕退官（1人）**：致仕韩侍郎，历仕名宦，守卫道统，在乡置办义田义学；
  * **Ring-2 县衙钱谷公吏（2人）**：经管钱吏张文远等，收取头子钱，毕生执念攒钱送子进太学；
  * **Ring-3 上等户大姓员外（2人）**：城外大姓员外/孙掌柜，开设米肆典当，在商言商规避烂账；
  * **Ring-3 中等自耕农（5人）**：丰乐乡自耕农，祖传十五亩薄田，死守体面，拒替穷邻连坐；
  * **Ring-3 下等五等佃农（10人）**：下等佃农，口粮濒临 3.0 石饿毙线，全家活命是唯一底线。

---

## 五、 后续实施路线图

1. **Step 1**：在 `sim_config_wang_an_shi.yaml` 中完备录入外部异动、心智阈值、异质目标函数与演化分叉配置块；
2. **Step 2**：在 `socio_engine/core/evolution_engine.py` 中完整实现四阶飞轮与分叉判定逻辑；
3. **Step 3**：在 `socio_engine/run_simulation.py` 中接入完整的 Rust 物理会计校验与分叉报告输出；
4. **Step 4**：运行推演实验，产出《北宋熙宁青苗法群体趋同与演化分叉推演报告》。
