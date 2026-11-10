# 跨朝代/跨社会系统通用剧本生成提示词模板与扩展规范
# Universal Socio-Scenario Prompt Template & Extension Guide

> **适用引擎**：Socio-Engine (社会系统协议多智能体仿真沙盘 v1.0+)  
> **理论依据**：《社会系统协议学（Socio-Protocolics）》v11.2 (正交公理化奠基典藏版)  
> **设计哲学**：底层物理状态机与特权环解耦，所有朝代、历史事件、阶级身份均通过 **数据与提示词驱动 (Agent-as-Data)**。

---

## 一、 为什么需要剧本与内核解耦？

在初始原型开发中，由于针对万历初年徽州歙县赋役案进行了深度拟合，部分测试逻辑曾硬编码了“海瑞”、“钱老吏”、“吴员外”等特定实体。

**当前引擎已完成 100% 公理化解耦**：
1. **Rust 底层物理机（`socio_core`）**：只负责通用物理守恒（双式记账、货币/粮食/土地实物守恒、饿死与破产判断）、特权环门禁（Ring-0 到 Ring-3 越权拦截）与图论拓扑中介中心性计算。**底层无任何朝代特有人名或词汇**。
2. **场景剧本层（`config/sim_config_<scenario>.yaml`）**：定义宏观定额、时间步长、物价基准、事件编年表与社会依附网络。
3. **阶级角色层（`roles/<role_id>/`）**：定义各阶级的目标函数 $U_i$、贴现因子 $\beta_i$、行动空间（Action Space）与认知 Prompt。

---

## 二、 跨朝代概念映射对照表 (Concept Mapping)

当你希望模拟其他朝代（如唐代两税法、北宋青苗法、明代一条鞭法、清代摊丁入亩、甚至古罗马或架空社会）时，请遵循以下特权环与物理量映射法则：

| 社会系统协议学原语 | 含义与物理约束 | 明代徽州基准 | 北宋熙宁变法 (青苗法) | 唐代建中元年 (两税法) | 古罗马帝国 (戴克里先限价) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ring-0** | 帝国中央/法定最高权力 | 朝廷户部/神宗实录 | 宋神宗/中书门下 | 唐德宗/户部度支司 | 罗马元老院/戴克里先皇帝 |
| **Ring-1** | 地方主管长官/执法主官 | 歙县知县/知府/巡抚 | 提举常平司官 / 知县 | 刺史 / 州县令 | 行省行台总督 / 市政官 |
| **Ring-2** | 官僚中介/寄生中介/豪绅 | 户刑二房书吏、典当行、致仕乡绅 | 常平仓经办吏、开封府高利贷柜坊、兼并大姓 | 州县胥吏、牙商、庄园主 | 税吏 (Publicans)、大庄园主 (Latifundia) |
| **Ring-3** | 终端生产/承压节点 | 自耕农、水尾贫农、绝户老汉、里长 | 乡村保甲自耕农、佃客、厢军老兵 | 客户、课户自耕农、流民 | 自由小农、行会工匠、隶农 (Coloni) |
| **货币流通量** | 市场结算与完税媒介 | 白银 (两) | 铜钱/铁钱 (贯/文) | 绢帛与铜钱 (匹/贯) | 第纳尔银币 (Denarius) |
| **生存物资** | 物理能量维持与刚性消耗 | 稻谷 (石) | 小麦/粟米 (石) | 粟/麦 (石) | 小麦 (Modius) |
| **生产资料** | 土地/生产工具 | 耕地 (亩) | 官私耕地 (亩) | 永业田/口分田 (亩) | 庄园农田 (Jugera) |

---

## 三、 关键机制：如何确保外部大模型真正按《社会系统协议学》运行？

> [!IMPORTANT]
> **关于 LLM 理论先验的严谨说明**：  
> 主流公有云大模型（如 ChatGPT、Claude、DeepSeek 等）在其通用预训练语料中并没有完整的《社会系统协议学（Socio-Protocolics）》公理体系。  
> 如果仅发送一句话“*你是一位精通社会系统协议学的专家*”，LLM 只会退化为通用的历史小说角色扮演或浅层政治经济学，**无法自发施加物理双式记账守恒、特权环隔离阻断与中介寄生模型**！

为了让任何外部大模型都能精确、严密地生成符合《社会系统协议学》的剧本，我们提供两种使用模式：

### 模式 A（推荐·即拷即用）：内嵌公理微内核的“自包含元编译器提示词”
我们将《社会系统协议学》的五大原语、三大公设与特权环严格数学逻辑**直接内嵌在提示词头部**。无需外挂任何文档，任意纯净大模型均能作为严格的“协议编译器”输出合规代码！

### 模式 B（学术深度级）：外挂知识库挂载模式
如果你正在使用支持长文本上下文或知识库挂载的模型（如 Claude Projects、Custom GPTs、NotebookLM、或带有 RAG 的开发环境）：
1. 将本项目根目录的 **`核心概念速查手册_CheatSheet.md`**（仅 16 KB 高密度公理集）或 **`socio_protocolics_whitepaper.md`** 上传为知识库/上下文附件；
2. 再发送下方的生成指令，LLM 即可实现 100% 逐条对齐 RFC-001 至 RFC-019 的深层推演！

---

## 四、 自包含元编译器提示词（可直接复制给任意大模型）

将以下整段提示词复制，仅需修改其中的【目标历史课题】即可直接发送：

````markdown
# ROLE: 《社会系统协议学（Socio-Protocolics）》多智能体沙盘架构编译器

你现在担任基于《社会系统协议学（Socio-Protocolics）》体系的多智能体历史仿真沙盘架构师。

## 1. 强制内嵌公理规约（Axiomatic Micro-Kernel）
在生成任何场景与角色前，你必须严格遵循以下系统协议学公理：
- **公设 P1 (有限物理能量与双式守恒)**：严禁凭空生成货币或粮食！所有赋税、借贷、火耗、租金的转移必须满足物质守恒。每季度小农必须扣除最低口粮（如 3.0 石），不足者触发破产 (BANKRUPT) 或逃亡 (FLED)；
- **公设 P2 (主体自博弈公设)**：每个 Agent 都是以自身私有效用 $U_i$、家庭代际延续和生存底线为最高准则的博弈单元，拒绝道德脸谱化，严禁“大公无私的圣人”或“无脑作恶的恶棍”；
- **公设 P3 (预期诱导均衡公设)**：官府政令只是协议提案（Protocol Proposal），基层节点根据主观信念与风险收益权衡是否遵从；
- **五大基石原语**：
  * **O1 Agent**: 具有效用 $U_i$ 与贴现因子 $\beta_i$ 的决策单元；
  * **O2 Protocol**: 跨节点交互规则集合 $\mathcal{P} = \langle \Sigma, \mathcal{S}, \delta, \mathcal{R} \rangle$；
  * **O3 Expectation**: 主体主观概率分布 $\mu_i$；
  * **O4 Middleware (核心机制)**: 介于主官与终端之间的转译与寻租中介（胥吏、包税人、牙商），具有非生产性租金提取行为；
  * **O5 Resource**: 土地、粮食、货币等有限资源集合。
- **四大特权环隔离机制 (Privilege Rings)**：
  * **Ring-0 (帝国根权力)**: 皇权/户部定额，设定不可抗拒的宏观考成指标；
  * **Ring-1 (地方行政主官)**: 知县/太守/改革官，可颁布政令、清丈田亩、查处中介，但受上级考成与同僚掣肘；
  * **Ring-2 (官僚中介与特权豪绅)**: 掌握信息黑箱，通过浮收加派、隐匿田产、典当高利贴水剥削两端；具有跨环向京城直通弹劾的信道；
  * **Ring-3 (终端生产承压节点)**: 自耕农、佃客，承担不可转嫁的刚性实体成本，具有生存底线。

---

## 2. 【本次生成目标历史课题】
- **历史朝代与地点**：[例如：北宋神宗熙宁二年（1069）开封府祥符县]
- **核心制度改革与历史冲突**：[例如：王安石推行《青苗法》，常平仓按二分取息官贷，遭到保守派司马光反对，地方经办胥吏趁机抑配摊派并强行收取火钱头子钱，富室柜坊抵制，小农陷入新债务陷阱]
- **推演步长与时长**：[例如：8 个季度 / 2 年周期]

---

## 3. 请生成以下符合 Socio-Engine 规格的两套文件：

### 文件 1: `config/sim_config_[scenario_id].yaml`
必须包含：
1. `scenario`: 场景名、朝代坐标、时间范围、max_ticks、tick_unit；
2. `database`: `db_path: "database/socio_sim.db"`, `wal_mode: true`；
3. `historical_timeline_events`: 1 到 N 步的真实/推演历史大事件编年表；
4. `macro_environment`: initial_treasury_silver, imperial_tax_quota, base_grain_price, official_tax_per_mu, official_surtax_rate, subsistence_grain_per_tick；
5. `population`:
   - `magistrates` (Ring-1): 主官 (附带 ID, name, role_type, privilege_ring: 1, initial_assets)
   - `clerks` (Ring-2): 经办胥吏 (附带 trait, initial_assets, land_hidden_mu)
   - `gentry` (Ring-2): 兼并大户/放贷者 (附带 initial_assets, land_hidden_mu)
   - `peasants` (Ring-3): 贫农/自耕农/承压者 (附带 initial_assets: 极低现金与口粮)
6. `social_relations`: 节点间的拓扑关系边（SubordinateTo, CollusionAlliance, HostileRival, DebtorTo, TaxPayerTo, CoercionHarass）。

### 文件 2: 代表性核心角色的配置与 Prompt (`roles/<role_id>/`)
挑选至少 3 个处于不同特权环的核心对立角色（如：Ring-1 改革官、Ring-2 寻租吏、Ring-3 承贷贫农），为每个角色编写：
- `role_config.yaml`:
  `role_id`, `privilege_ring`, `action_space` (全大写下划线合法动作列表), `observation_scope`；
- `system_prompt.md`:
  注入阶级立场、目标函数 $U_i$、家庭代际危机、生计底线、合法的动作决策规则。必须严格要求输出 `proposal_action` JSON 规范结构。
````

---

## 五、 实战范例：北宋熙宁二年（1069）王安石青苗法变法沙盘

以下是已通过该模板生成的北宋青苗法标准配置片段（可直接参考）：

### 1. `config/sim_config_song_qingmiao.yaml` (片段展示)
```yaml
scenario:
  name: "北宋熙宁二年开封府祥符县青苗法推行与官吏抑配博弈沙盘"
  county: "京畿路 开封府 祥符县"
  historical_year_start: 1069
  historical_year_end: 1070
  max_ticks: 8
  tick_unit: "QUARTER"

database:
  db_path: "database/socio_sim.db"
  wal_mode: true

historical_timeline_events:
  1: "【熙宁二年春】制置三司条例司颁布《青苗法》：令常平仓出陈粮与现钱，按二分年息（20%）贷与乡村五等农户！"
  2: "【熙宁二年夏】祥符县常平仓开仓放贷，主簿与斗级书吏借机索要‘耗折钱’与‘印券费’，富室柜坊借机放高利贷折算！"
  3: "【熙宁二年秋】秋收起息！官府考成严催‘青苗钱全额回笼’；下等贫户因青黄不接无力还钱，胥吏强行抑配富户保结连坐！"
  4: "【熙宁二年冬】御史中丞吕诲、翰林学士司马光连章上疏痛陈‘青苗法名为惠民，实乃官府放高利贷、抑配残民’！"

macro_environment:
  initial_treasury_silver: 5000.0  # 祥符县常平仓本钱 (贯)
  imperial_tax_quota: 12000.0       # 两税正额 (贯)
  base_grain_price: 1.0             # 官定麦价 (贯/石)
  official_tax_per_mu: 0.05
  official_surtax_rate: 0.02
  subsistence_grain_per_tick: 3.0

population:
  magistrates:
    - id: "magistrate_wang_reformer"
      name: "常平司提举官 (新党先锋)"
      role_type: "magistrate"
      privilege_ring: 1
      model: "deepseek-flash"
      temperature: 0.2
      background: "奉荆公王安石之命推行新法，急于在考成中做出政绩，严令常平钱必须贷满千贯"
      initial_assets: { silver: 50.0, grain: 40.0, land: 0.0 }

  clerks:
    - id: "clerk_douji_zhao"
      name: "赵斗级 (常平仓经办吏)"
      role_type: "clerk"
      privilege_ring: 2
      model: "deepseek-flash"
      temperature: 0.6
      trait: "GREEDY_CALCULATING"
      background: "利用农户不识字与印券繁复之机，私自扣除一分耗折钱入己私囊，甚至勾结柜坊放高利"
      initial_assets: { silver: 40.0, grain: 30.0, land: 20.0 }

  gentry:
    - id: "gentry_han_landlord"
      name: "韩大户 (城关柜坊兼并豪民)"
      role_type: "gentry"
      privilege_ring: 2
      model: "deepseek-flash"
      temperature: 0.4
      background: "原本垄断民间五分（50%）高利贷，对官办青苗贷恨之入骨，联合朝中旧党权贵四处搜集民怨材料"
      initial_assets: { silver: 1200.0, grain: 800.0, land: 200.0 }

  peasants:
    - id: "peasant_song_fifth_class"
      name: "宋小五 (五等贫农 / 承贷下户)"
      role_type: "peasant"
      privilege_ring: 3
      model: "deepseek-flash"
      temperature: 0.8
      trait: "DESPERATE_STRESSED"
      background: "春荒无粮，被保长强行拉去领官贷，扣除胥吏常例后实得不足八成，秋收面临十倍催逼"
      initial_assets: { silver: 0.2, grain: 2.0, land: 4.0 }

social_relations:
  - { from: "clerk_douji_zhao", to: "magistrate_wang_reformer", type: "SubordinateTo", weight: 1.0 }
  - { from: "peasant_song_fifth_class", to: "clerk_douji_zhao", type: "CoercionHarass", weight: 2.5 }
  - { from: "clerk_douji_zhao", to: "gentry_han_landlord", type: "CollusionAlliance", weight: 3.0 }
```

---

## 五、 如何执行新朝代沙盘？

只需在终端输入一行命令即可启动任意朝代推演：

```powershell
# 运行北宋青苗法场景
python socio_engine/run_simulation.py --version exp_song_qingmiao --trial 1 --config config/sim_config_song_qingmiao.yaml

# 运行完成后，查看跨版本对比看板
python socio_engine/scripts/query_experiments.py --version exp_song_qingmiao
```

至此，Socio-Engine 真正实现了从“万历歙县特定小案例”向“**跨文明、跨时代、跨体制通用社会协议编译与推演平台**”的跃升！

