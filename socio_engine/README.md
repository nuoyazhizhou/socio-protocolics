# Socio-Engine: 社会系统协议多智能体仿真沙盘

> **理论底座**：《社会系统协议学（Socio-Protocolics）》v11.2 (正交公理化奠基典藏版)  
> **设计模式**：Rust 物理特权环与 WAL 账本 + Python 动态认知与配置注入 (Agent-as-Data)  
> **国际化指南**：[English Documentation & QuickStart (README_EN.md)](./README_EN.md)

---

## 快速导航
- 📖 [用户使用与 API Key 配置指南 (USER_GUIDE.md)](./USER_GUIDE.md)
- 🌐 [English Readme & Architecture (README_EN.md)](./README_EN.md)
- 📜 [跨朝代通用剧本提示词生成模板 (UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md)](./docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md)
- 📑 [海瑞知县铁腕整肃与中介设租推演实验报告 (docs/EXPERIMENT_REPORT_HAI_RUI.md)](./docs/EXPERIMENT_REPORT_HAI_RUI.md)
- 📑 [王安石青苗法四季度全景推演实验报告 (docs/EXPERIMENT_REPORT_WANG_AN_SHI.md)](./docs/EXPERIMENT_REPORT_WANG_AN_SHI.md)
- 📊 [跨版本与多轮次方差对比看板 (scripts/query_experiments.py)](./scripts/query_experiments.py)
- ⚖️ [跨轮次演化分歧与零心智基线比对工具 (scripts/compare_trials.py)](./scripts/compare_trials.py)
- 📑 [北宋青苗法三态分离与制度吸引子跨轮次分析报告 (docs/CROSS_TRIAL_COMPARISON_SUMMARY.md)](./docs/CROSS_TRIAL_COMPARISON_SUMMARY.md)
- ⚙️ [模型网关配置 (config/providers.yaml)](./config/providers.yaml)
- 🔑 API 密钥环境变量示例 (`.env.example`)
- 👥 角色配置与 Prompt 注入目录 (`roles/`)

---

## 核心设计理念

1. **角色即数据，代码零硬编码 (Agent-as-Data)**：
   - 所有的角色逻辑均通过 `roles/<role_id>/role_config.yaml`（模型/温度/算力分配）与 `system_prompt.md`（阶级立场/目标函数 $U_i$/认知偏差）定义；
   - 通用的 `core/agent.py` 负责驱动所有角色的状态机转换、Prompt 渲染与结构化行动输出。
2. **异构模型心智映射 (Heterogeneous Model Allocation)**：
   - 宏观调度者（如知县）：分配高推理算力模型（`deepseek-flash` / `claude-3-5-sonnet`）；
   - 微观寻租中介（如户房书吏）：分配高博弈模型，专注在规范空白处收租（`deepseek-flash` / `gpt-4o-mini`）；
   - 终端承压节点（如自耕农）：反映生存阻抗与极端压力。
3. **Rust 底层物理特权环与门禁 (Ring-0 到 Ring-3)**：
   - 由 `socio_core` (PyO3) 编译的原生 Rust 引擎守门，角色的系统调用受特权环严格约束，越权调用直接抛出异常驳回。
4. **不可篡改事件溯源账本 (Immutable Event-Sourcing Ledger)**：
   - 借鉴 Callwarden 的 SQLite WAL 生产级实践，所有事件、决策、隐秘抽租、篡改账册记录均落入专用数据库（`database/socio_sim.db`）。
5. **社会依附图论与爆炸半径 (Social Graph & Blast Radius)**：
   - 借鉴 Callwarden `graph.rs` / `impact.rs` 拓扑算法，计算寻租中介卡位度（Chokepoints）与逃荒抗税波及半径。
6. **三态分离与零心智对照基线 (Say-Do-Be Tripartite & Null Model)**：
   - **说什么 (Public Speech)**：低阻抗声学控制信号与博弈烟雾弹；
   - **做什么 (Physical Action)**：高阻抗能量与资产双入账做功；
   - **是什么 (Ecological Niche)**：不可逾越的法定特权环与抽取链生态位；
   - **零心智对照基线 (Dice Null Model)**：在完全相同的种子（`--seed 42`）与合法动作空间内进行均匀随机抽取，以对照组击穿“无锚语言漫游”，证明 LLM 决策被底层资产负债表严格支配。

---

## 快速运行

### 1. 基础推演与多轮控制

```powershell
# 运行智能体认知推演 (固定种子保证可复现性)
python socio_engine/run_simulation.py --config config/sim_config_wang_an_shi.yaml --ticks 4 --trial 1 --seed 42

# 运行零心智骰子对照基线 (Null Model Baseline)
python socio_engine/run_simulation.py --config config/sim_config_wang_an_shi.yaml --ticks 4 --trial 101 --mode dice --seed 42
```

### 2. 跨轮次审计与比对分析

```powershell
# 运行跨轮次分歧与引力场收敛分析工具
python socio_engine/scripts/compare_trials.py
```
详细配置步骤请参阅 [USER_GUIDE.md](./USER_GUIDE.md)。
