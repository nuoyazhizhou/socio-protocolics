# Socio-Engine 用户使用与配置全景指南

> **理论底座**：《社会系统协议学（Socio-Protocolics）》v11.2  
> **技术架构**：Rust 内核 (socio_core, PyO3) + Python 认知推演层 (Agent-as-Data)

---

## 一、 API 密钥配置指南 (在哪里配 Key？)

系统支持以下 **三种配置方式**（按优先级从高到低自动加载），任选一种即可：

### 方式 1：使用 `.env` 配置文件（推荐，最安全）
在 `socio_engine/` 目录下创建 `.env` 文件（或直接复制模版 `cp .env.example .env`）：

```bash
# socio_engine/.env
DEEPSEEK_API_KEY=sk-your-real-deepseek-api-key-here
```
> [!NOTE]
> 系统自带轻量原生环境变量加载器，无需额外安装 `python-dotenv`，读取后会自动注入进程环境。

---

### 方式 2：在 `config/providers.yaml` 中显式指定
打开 `socio_engine/config/providers.yaml`，在 `deepseek` 节点下取消注释并填入 `api_key`：

```yaml
providers:
  deepseek:
    base_url: "https://api.deepseek.com"
    api_key: "sk-your-real-deepseek-api-key-here"  # <--- 直接填在这里
    api_key_env: "DEEPSEEK_API_KEY"
    default_model: "deepseek-flash"
```

---

### 方式 3：通过系统 / 终端环境变量注入
在运行脚本前，在终端临时设置环境变量：

- **Windows PowerShell**:
  ```powershell
  $env:DEEPSEEK_API_KEY="sk-your-real-deepseek-api-key-here"
  python socio_engine/run_simulation.py
  ```
- **Windows CMD**:
  ```cmd
  set DEEPSEEK_API_KEY=sk-your-real-deepseek-api-key-here
  python socio_engine/run_simulation.py
  ```

---

## 二、 DeepSeek 模型选型说明

根据 DeepSeek 官方最新接口规格：
- **Base URL (OpenAI 兼容协议)**：`https://api.deepseek.com`
- **主流可用模型**：
  1. `deepseek-flash` (DeepSeek-V4.1-Flash-1017，支持思考与非思考模式、图像与 JSON 强输出)
  2. `deepseek-v4-pro` (DeepSeek-V4-Pro-0813)
- **模型路由一致性**：官方确认 `deepseek-v4-pro` 在当前调度底层实际上与 `deepseek-flash` 共享集群，因此在配置中填入 `deepseek-flash` 或 `deepseek-v4-pro` 均可正常调用。
- **脱机保底保障**：若未配置 API Key 或遇到网络超时，系统会自动启动内置的高保真离线博弈推演，保证仿真沙盘永不崩溃中断。

---

## 三、 项目核心目录结构

```text
socio_engine/
├── .env.example                 # 环境变量配置模板
├── Cargo.toml                   # Rust 工作区配置
├── run_simulation.py            # 仿真入口启动脚本
├── config/
│   ├── sim_config.yaml          # 宏观场景设定 (初始太仓银、米价、朝廷定额税)
│   └── providers.yaml           # 模型网关与 API 路由
├── database/
│   ├── schema.sql               # SQLite DDL 表结构 (事件溯源与六大表)
│   └── socio_sim.db             # WAL 模式生产级持久化数据库
├── core/
│   ├── role_loader.py           # 动态角色扫描器 (Agent-as-Data，零硬编码)
│   ├── agent.py                 # 通用 RoleAgent 驱动器
│   └── llm_client.py            # 多模型适配客户端 (带自动 .env 解析与错误降级)
├── roles/                       # 角色库 (每个角色一个独立目录)
│   ├── magistrate/              # 角色 1：知县 (Ring-1 主官)
│   │   ├── role_config.yaml     # 绑定模型 deepseek-flash、温度、合法动作
│   │   └── system_prompt.md     # 官声、考绩与目标函数 U_i
│   ├── clerk/                   # 角色 2：户房书吏 (Ring-2 寻租中介)
│   │   ├── role_config.yaml     # 绑定模型、灰色截留动作空间
│   │   └── system_prompt.md     # 火耗羡余、隐匿田亩、自保寻租动机
│   ├── gentry/                  # 角色 3：地方缙绅 (Ring-2 既得利益)
│   │   ├── role_config.yaml
│   │   └── system_prompt.md     # 优免特权、田产诡寄、兼并小农
│   ├── peasant/                 # 角色 4：自耕农 (Ring-3 承压终端)
│   │   ├── role_config.yaml
│   │   └── system_prompt.md     # 生存口粮线、现金流、逃荒抗税阻抗
│   └── templates/
│       └── proposal_action.json # 统一系统调用 (Syscall) 报文契约
└── socio_core/                  # Rust 底层高性能物理与图论内核 (PyO3)
    ├── Cargo.toml
    └── src/
        ├── lib.rs               # PyO3 Python 模块接口导出
        ├── db.rs                # SQLite WAL 高并发账本 (借鉴 Callwarden db_conn.rs)
        ├── state.rs             # 物理资源守恒与特权环约束 (O5 与 Ring-0~3)
        └── topology.rs          # 社会关系依存网络与卡位点算法 (借鉴 Callwarden graph.rs)
```

---

## 四、 快速运行与验证

### 1. 运行仿真沙盘
在终端进入项目根目录执行：
```powershell
python socio_engine/run_simulation.py
```

### 2. 输出说明
终端推演将展示三个层面的信息：
1. **社会依存网络分析**：
   - 识别系统中的**中介卡位点（Chokepoints）**，例如户房书吏如何汇聚全县赋税资金流；
   - 计算终端小农破产抗税时的**影响爆炸半径（Blast Radius）**。
2. **微观博弈与特权环检查**：
   - 每个智能体根据各自的私有目标函数提出动作决策；
   - Rust 内核严格检查权限：若书吏尝试发布知县法令，或小农尝试篡改鱼鳞图册，Rust 内核将直接抛出越权驳回。
3. **宏观世界演化**：
   - 追踪每季度的太仓存银、火耗截留总额、抛荒田亩数、流民逃荒率以及系统技术债（制度熵）。

### 3. 查看数据库记录
推演结束后，数据全部落入 `socio_engine/database/socio_sim.db`，可通过任意 SQLite 工具或 Python 脚本查询：
- `sim_runs`：仿真场次元数据
- `agent_registry`：参与 Agent 身份与模型绑定
- `world_ticks`：宏观世界状态指标时序
- `agent_states`：每个 Agent 在每季度的个人资产与效用变化
- `protocol_events`：不可篡改的协议行动与截留租金流水账本
- `dialogue_logs`：Agent 自然语言交互与意图日志

