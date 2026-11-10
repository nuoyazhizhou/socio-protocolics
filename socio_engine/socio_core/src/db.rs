//! socio_core 数据库持久化层 (借鉴 Callwarden db_conn.rs 的 WAL 模式与并发安全实践)

use rusqlite::{params, Connection};
use parking_lot::Mutex;
use std::path::Path;
use std::sync::Arc;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum DbError {
    #[error("SQLite error: {0}")]
    Sqlite(#[from] rusqlite::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("Simulation run not found: {0}")]
    RunNotFound(String),
}

pub struct Database {
    conn: Arc<Mutex<Connection>>,
}

impl Database {
    pub fn open<P: AsRef<Path>>(path: P) -> std::result::Result<Self, DbError> {
        let conn = Connection::open(path)?;

        // 配置 SQLite 生产级高性能 & WAL 机制 (对齐 Callwarden db_conn 实践)
        conn.pragma_update(None, "journal_mode", "WAL")?;
        conn.pragma_update(None, "synchronous", "NORMAL")?;
        conn.pragma_update(None, "busy_timeout", 5000)?;
        conn.pragma_update(None, "foreign_keys", "ON")?;

        let db = Database {
            conn: Arc::new(Mutex::new(conn)),
        };
        db.init_schema()?;
        Ok(db)
    }

    pub fn open_in_memory() -> std::result::Result<Self, DbError> {
        let conn = Connection::open_in_memory()?;
        conn.pragma_update(None, "foreign_keys", "ON")?;
        let db = Database {
            conn: Arc::new(Mutex::new(conn)),
        };
        db.init_schema()?;
        Ok(db)
    }

    pub fn init_schema(&self) -> std::result::Result<(), DbError> {
        let conn = self.conn.lock();
        conn.execute_batch(
            r#"
            CREATE TABLE IF NOT EXISTS sim_runs (
                run_id TEXT PRIMARY KEY,
                scenario_name TEXT NOT NULL,
                experiment_version TEXT DEFAULT 'v1.0',
                trial_index INTEGER DEFAULT 1,
                description TEXT,
                start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_ticks INTEGER DEFAULT 0,
                config_snapshot TEXT,
                status TEXT DEFAULT 'RUNNING'
            );

            CREATE TABLE IF NOT EXISTS agent_registry (
                agent_id TEXT PRIMARY KEY,
                run_id TEXT NOT NULL,
                role_type TEXT NOT NULL,
                role_name TEXT NOT NULL,
                privilege_ring INTEGER NOT NULL,
                llm_provider TEXT NOT NULL,
                model_name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(run_id) REFERENCES sim_runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS world_ticks (
                tick_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                tick_index INTEGER NOT NULL,
                treasury_silver REAL DEFAULT 0.0,
                granary_grain REAL DEFAULT 0.0,
                grain_price_silver REAL DEFAULT 1.0,
                abandoned_land_mu REAL DEFAULT 0.0,
                fleeing_peasant_ratio REAL DEFAULT 0.0,
                unrest_risk_score REAL DEFAULT 0.0,
                system_entropy REAL DEFAULT 0.0,
                snapshot_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(run_id) REFERENCES sim_runs(run_id)
            );

            CREATE TABLE IF NOT EXISTS agent_states (
                state_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                tick_index INTEGER NOT NULL,
                agent_id TEXT NOT NULL,
                cash_silver REAL DEFAULT 0.0,
                stored_grain REAL DEFAULT 0.0,
                land_owned_mu REAL DEFAULT 0.0,
                land_hidden_mu REAL DEFAULT 0.0,
                tax_arrears REAL DEFAULT 0.0,
                utility_score REAL DEFAULT 0.0,
                trust_in_magistrate REAL DEFAULT 0.5,
                survival_status TEXT DEFAULT 'ALIVE',
                FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
                FOREIGN KEY(agent_id) REFERENCES agent_registry(agent_id)
            );

            CREATE TABLE IF NOT EXISTS protocol_events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                tick_index INTEGER NOT NULL,
                actor_id TEXT NOT NULL,
                target_id TEXT,
                action_type TEXT NOT NULL,
                action_payload TEXT NOT NULL,
                rent_extracted REAL DEFAULT 0.0,
                is_covert BOOLEAN DEFAULT 0,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
                FOREIGN KEY(actor_id) REFERENCES agent_registry(agent_id)
            );

            CREATE TABLE IF NOT EXISTS dialogue_logs (
                dialogue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                tick_index INTEGER NOT NULL,
                speaker_id TEXT NOT NULL,
                listener_id TEXT NOT NULL,
                channel_type TEXT DEFAULT 'PUBLIC',
                raw_prompt TEXT,
                raw_response TEXT,
                parsed_intent TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(run_id) REFERENCES sim_runs(run_id),
                FOREIGN KEY(speaker_id) REFERENCES agent_registry(agent_id)
            );

            CREATE INDEX IF NOT EXISTS idx_events_run_tick ON protocol_events(run_id, tick_index);
            CREATE INDEX IF NOT EXISTS idx_states_agent_tick ON agent_states(run_id, agent_id, tick_index);
            CREATE INDEX IF NOT EXISTS idx_dialogue_run ON dialogue_logs(run_id, tick_index);
            "#
        )?;

        // 自动增量迁移旧表结构 (兼容历史 runs)
        let _ = conn.execute("ALTER TABLE sim_runs ADD COLUMN experiment_version TEXT DEFAULT 'v1.0'", []);
        let _ = conn.execute("ALTER TABLE sim_runs ADD COLUMN trial_index INTEGER DEFAULT 1", []);

        Ok(())
    }

    pub fn start_sim_run(
        &self,
        run_id: &str,
        scenario: &str,
        desc: &str,
        config_json: &str,
        experiment_version: &str,
        trial_index: i32,
    ) -> std::result::Result<(), DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT OR REPLACE INTO sim_runs (run_id, scenario_name, experiment_version, trial_index, description, config_snapshot, status)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, 'RUNNING')",
            params![run_id, scenario, experiment_version, trial_index, desc, config_json],
        )?;
        Ok(())
    }

    pub fn register_agent(
        &self,
        run_id: &str,
        agent_id: &str,
        role_type: &str,
        role_name: &str,
        privilege_ring: i32,
        llm_provider: &str,
        model_name: &str,
    ) -> std::result::Result<(), DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT OR REPLACE INTO agent_registry (agent_id, run_id, role_type, role_name, privilege_ring, llm_provider, model_name)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)",
            params![agent_id, run_id, role_type, role_name, privilege_ring, llm_provider, model_name],
        )?;
        Ok(())
    }

    pub fn record_world_tick(
        &self,
        run_id: &str,
        tick_index: i32,
        treasury_silver: f64,
        granary_grain: f64,
        grain_price_silver: f64,
        abandoned_land_mu: f64,
        fleeing_peasant_ratio: f64,
        unrest_risk_score: f64,
        system_entropy: f64,
    ) -> std::result::Result<(), DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT INTO world_ticks (run_id, tick_index, treasury_silver, granary_grain, grain_price_silver, abandoned_land_mu, fleeing_peasant_ratio, unrest_risk_score, system_entropy)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)",
            params![run_id, tick_index, treasury_silver, granary_grain, grain_price_silver, abandoned_land_mu, fleeing_peasant_ratio, unrest_risk_score, system_entropy],
        )?;
        conn.execute(
            "UPDATE sim_runs SET total_ticks = ?1 WHERE run_id = ?2",
            params![tick_index, run_id],
        )?;
        Ok(())
    }

    pub fn record_agent_state(
        &self,
        run_id: &str,
        tick_index: i32,
        agent_id: &str,
        cash_silver: f64,
        stored_grain: f64,
        land_owned_mu: f64,
        land_hidden_mu: f64,
        tax_arrears: f64,
        utility_score: f64,
        trust_in_magistrate: f64,
        survival_status: &str,
    ) -> std::result::Result<(), DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT INTO agent_states (run_id, tick_index, agent_id, cash_silver, stored_grain, land_owned_mu, land_hidden_mu, tax_arrears, utility_score, trust_in_magistrate, survival_status)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11)",
            params![run_id, tick_index, agent_id, cash_silver, stored_grain, land_owned_mu, land_hidden_mu, tax_arrears, utility_score, trust_in_magistrate, survival_status],
        )?;
        Ok(())
    }

    pub fn record_protocol_event(
        &self,
        run_id: &str,
        tick_index: i32,
        actor_id: &str,
        target_id: Option<&str>,
        action_type: &str,
        action_payload: &str,
        rent_extracted: f64,
        is_covert: bool,
    ) -> std::result::Result<i64, DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT INTO protocol_events (run_id, tick_index, actor_id, target_id, action_type, action_payload, rent_extracted, is_covert)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)",
            params![run_id, tick_index, actor_id, target_id, action_type, action_payload, rent_extracted, is_covert as i32],
        )?;
        Ok(conn.last_insert_rowid())
    }

    pub fn record_dialogue(
        &self,
        run_id: &str,
        tick_index: i32,
        speaker_id: &str,
        listener_id: &str,
        channel_type: &str,
        raw_prompt: &str,
        raw_response: &str,
        parsed_intent: &str,
    ) -> std::result::Result<i64, DbError> {
        let conn = self.conn.lock();
        conn.execute(
            "INSERT INTO dialogue_logs (run_id, tick_index, speaker_id, listener_id, channel_type, raw_prompt, raw_response, parsed_intent)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8)",
            params![run_id, tick_index, speaker_id, listener_id, channel_type, raw_prompt, raw_response, parsed_intent],
        )?;
        Ok(conn.last_insert_rowid())
    }
}
