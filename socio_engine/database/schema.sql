-- Socio-Engine 仿真数据库表结构 (DDL)
-- 基于事件溯源 (Event Sourcing) 与 不可篡改时间线设计

-- 1. 仿真场次表 (记录实验场景与全局元数据)
CREATE TABLE IF NOT EXISTS sim_runs (
    run_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    description TEXT,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_ticks INTEGER DEFAULT 0,
    config_snapshot TEXT, -- JSON 格式记录当时的环境配置
    status TEXT DEFAULT 'RUNNING' -- RUNNING, COMPLETED, ABORTED
);

-- 2. 智能体注册表 (记录所有参与 Agent 的静态身份与模型分配)
CREATE TABLE IF NOT EXISTS agent_registry (
    agent_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    role_type TEXT NOT NULL,      -- magistrate, clerk, gentry, peasant 等
    role_name TEXT NOT NULL,      -- 具名角色名，如 '顾县令', '钱书吏'
    privilege_ring INTEGER NOT NULL, -- 0: 系统内核, 1: 地方主官, 2: 寻租中介, 3: 平民终端
    llm_provider TEXT NOT NULL,   -- deepseek, openai, anthropic, ollama
    model_name TEXT NOT NULL,     -- deepseek-chat, gpt-4o, claude-3-5-sonnet
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(run_id) REFERENCES sim_runs(run_id)
);

-- 3. 世界宏观状态切片表 (每个 Tick 记录一次全县宏观指标)
CREATE TABLE IF NOT EXISTS world_ticks (
    tick_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    tick_index INTEGER NOT NULL,
    treasury_silver REAL DEFAULT 0.0,       -- 县太仓实存库银 (两)
    granary_grain REAL DEFAULT 0.0,         -- 义仓存粮 (石)
    grain_price_silver REAL DEFAULT 1.0,    -- 当前米价 (两/石)
    abandoned_land_mu REAL DEFAULT 0.0,     -- 抛荒田亩数
    fleeing_peasant_ratio REAL DEFAULT 0.0, -- 逃亡流民比例 (0.0 ~ 1.0)
    unrest_risk_score REAL DEFAULT 0.0,     -- 民变暴动风险指数 (0.0 ~ 1.0)
    system_entropy REAL DEFAULT 0.0,        -- 系统混乱度/技术债指数
    snapshot_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(run_id) REFERENCES sim_runs(run_id)
);

-- 4. 智能体每轮状态表 (动态资产与效用)
CREATE TABLE IF NOT EXISTS agent_states (
    state_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    tick_index INTEGER NOT NULL,
    agent_id TEXT NOT NULL,
    cash_silver REAL DEFAULT 0.0,           -- 现银储备 (两)
    stored_grain REAL DEFAULT 0.0,          -- 口粮储备 (石)
    land_owned_mu REAL DEFAULT 0.0,         -- 名下田亩数
    land_hidden_mu REAL DEFAULT 0.0,        -- 隐匿不报田亩数 (避税)
    tax_arrears REAL DEFAULT 0.0,           -- 历年积欠税银
    utility_score REAL DEFAULT 0.0,         -- 当前主观效用 U_i
    trust_in_magistrate REAL DEFAULT 0.5,   -- 对县衙的信任度 (0.0 ~ 1.0)
    survival_status TEXT DEFAULT 'ALIVE',   -- ALIVE, BANKRUPT, FLED, REBEL
    FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
    FOREIGN KEY(agent_id) REFERENCES agent_registry(agent_id)
);

-- 5. 协议事件流水表 (最关键的事件审计：谁在何时执行了什么行动、截留了多少租金)
CREATE TABLE IF NOT EXISTS protocol_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    tick_index INTEGER NOT NULL,
    actor_id TEXT NOT NULL,
    target_id TEXT,
    action_type TEXT NOT NULL,              -- 如 ISSUE_EDICT, INJECT_SURCHARGE, PAY_TAX
    action_payload TEXT NOT NULL,           -- JSON 格式存储结构化参数
    rent_extracted REAL DEFAULT 0.0,        -- 伴随该行为产生的非生产性租金 (两)
    is_covert BOOLEAN DEFAULT 0,            -- 是否为瞒报/灰色暗箱操作
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
    FOREIGN KEY(actor_id) REFERENCES agent_registry(agent_id)
);

-- 6. 对话与通信日志表 (记录智能体之间完整的自然语言交互上下文)
CREATE TABLE IF NOT EXISTS dialogue_logs (
    dialogue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    tick_index INTEGER NOT NULL,
    speaker_id TEXT NOT NULL,
    listener_id TEXT NOT NULL,
    channel_type TEXT DEFAULT 'PUBLIC',     -- PUBLIC (大堂公堂), PRIVATE (内室私商), WHISPER (廊下密语)
    raw_prompt TEXT,                        -- 发送给 LLM 的完整提示词
    raw_response TEXT,                      -- LLM 原始文本回复
    parsed_intent TEXT,                     -- 提取出的博弈意图 (JSON)
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
    FOREIGN KEY(speaker_id) REFERENCES agent_registry(agent_id)
);

-- 索引加速
CREATE INDEX IF NOT EXISTS idx_events_run_tick ON protocol_events(run_id, tick_index);
CREATE INDEX IF NOT EXISTS idx_states_agent_tick ON agent_states(run_id, agent_id, tick_index);
CREATE INDEX IF NOT EXISTS idx_dialogue_run ON dialogue_logs(run_id, tick_index);

