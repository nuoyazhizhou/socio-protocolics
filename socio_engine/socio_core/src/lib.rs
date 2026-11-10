//! socio_core Python 扩展绑定库 (PyO3)
//! 提供状态机、SQLite WAL 存储与社会拓扑图论加速

pub mod db;
pub mod state;
pub mod topology;

use pyo3::exceptions::{PyRuntimeError, PyValueError};
use pyo3::prelude::*;
use std::sync::Arc;
use parking_lot::Mutex;

#[pyclass]
pub struct PySocioEngine {
    db: Arc<db::Database>,
    state_engine: Arc<Mutex<state::StateEngine>>,
}

#[pymethods]
impl PySocioEngine {
    #[new]
    #[pyo3(signature = (db_path = None))]
    pub fn new(db_path: Option<&str>) -> PyResult<Self> {
        let db = match db_path {
            Some(p) => db::Database::open(p)
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to open DB: {}", e)))?,
            None => db::Database::open_in_memory()
                .map_err(|e| PyRuntimeError::new_err(format!("Failed to open in-memory DB: {}", e)))?,
        };

        Ok(PySocioEngine {
            db: Arc::new(db),
            state_engine: Arc::new(Mutex::new(state::StateEngine::new())),
        })
    }

    #[pyo3(signature = (run_id, scenario, desc, config_json, experiment_version = "v1.0", trial_index = 1))]
    pub fn start_sim_run(
        &self,
        run_id: &str,
        scenario: &str,
        desc: &str,
        config_json: &str,
        experiment_version: &str,
        trial_index: i32,
    ) -> PyResult<()> {
        self.db.start_sim_run(run_id, scenario, desc, config_json, experiment_version, trial_index)
            .map_err(|e| PyRuntimeError::new_err(format!("Failed to start sim run: {}", e)))
    }

    #[pyo3(signature = (run_id, agent_id, role_type, role_name, privilege_ring, provider, model, initial_silver = 10.0, initial_grain = 20.0, initial_land = 10.0))]
    pub fn register_agent(
        &self,
        run_id: &str,
        agent_id: &str,
        role_type: &str,
        role_name: &str,
        privilege_ring: i32,
        provider: &str,
        model: &str,
        initial_silver: f64,
        initial_grain: f64,
        initial_land: f64,
    ) -> PyResult<()> {
        // 注册到数据库
        self.db.register_agent(run_id, agent_id, role_type, role_name, privilege_ring, provider, model)
            .map_err(|e| PyRuntimeError::new_err(format!("DB registration error: {}", e)))?;

        // 注册到状态机内存
        let mut engine = self.state_engine.lock();
        engine.add_agent(state::AgentState {
            agent_id: agent_id.to_string(),
            role_type: role_type.to_string(),
            role_name: role_name.to_string(),
            privilege_ring: privilege_ring as u8,
            cash_silver: initial_silver,
            stored_grain: initial_grain,
            land_owned_mu: initial_land,
            land_hidden_mu: 0.0,
            tax_arrears: 0.0,
            utility_score: 50.0,
            trust_in_magistrate: 0.8,
            survival_status: "ALIVE".to_string(),
        });

        // 记录初始状态快照
        self.db.record_agent_state(
            run_id,
            0,
            agent_id,
            initial_silver,
            initial_grain,
            initial_land,
            0.0,
            0.0,
            50.0,
            0.8,
            "ALIVE",
        ).map_err(|e| PyRuntimeError::new_err(format!("State log error: {}", e)))?;

        Ok(())
    }

    pub fn step_tick(&self, run_id: &str) -> PyResult<String> {
        let mut engine = self.state_engine.lock();
        engine.step_tick();

        // 持久化宏观数据
        let w = &engine.world;
        self.db.record_world_tick(
            run_id,
            w.tick_index,
            w.treasury_silver,
            w.granary_grain,
            w.grain_price_silver,
            w.abandoned_land_mu,
            w.fleeing_peasant_ratio,
            w.unrest_risk_score,
            w.system_entropy,
        ).map_err(|e| PyRuntimeError::new_err(format!("World tick log error: {}", e)))?;

        // 持久化所有 Agent 的当前状态
        for agent in engine.agents.values() {
            self.db.record_agent_state(
                run_id,
                w.tick_index,
                &agent.agent_id,
                agent.cash_silver,
                agent.stored_grain,
                agent.land_owned_mu,
                agent.land_hidden_mu,
                agent.tax_arrears,
                agent.utility_score,
                agent.trust_in_magistrate,
                &agent.survival_status,
            ).map_err(|e| PyRuntimeError::new_err(format!("Agent state log error: {}", e)))?;
        }

        serde_json::to_string(w)
            .map_err(|e| PyRuntimeError::new_err(format!("JSON serialization error: {}", e)))
    }

    pub fn execute_action(
        &self,
        run_id: &str,
        actor_id: &str,
        action_type: &str,
        target_id: Option<&str>,
        params_json: &str,
    ) -> PyResult<String> {
        let params: serde_json::Value = serde_json::from_str(params_json)
            .map_err(|e| PyValueError::new_err(format!("Invalid params JSON: {}", e)))?;

        let proposal = state::ActionProposal {
            actor_id: actor_id.to_string(),
            action_type: action_type.to_string(),
            target_id: target_id.map(|s| s.to_string()),
            parameters: params,
        };

        let mut engine = self.state_engine.lock();
        let tick_index = engine.world.tick_index;

        let result = engine.execute_action(&proposal)
            .map_err(|e| PyRuntimeError::new_err(format!("Action execution rejected: {}", e)))?;

        // 记入事件日志表 (不可篡改账本)
        self.db.record_protocol_event(
            run_id,
            tick_index,
            actor_id,
            target_id,
            action_type,
            &result.payload_json,
            result.rent_extracted,
            result.is_covert,
        ).map_err(|e| PyRuntimeError::new_err(format!("Failed to record protocol event: {}", e)))?;

        serde_json::to_string(&result)
            .map_err(|e| PyRuntimeError::new_err(format!("JSON error: {}", e)))
    }

    pub fn record_dialogue(
        &self,
        run_id: &str,
        tick_index: i32,
        speaker_id: &str,
        listener_id: &str,
        channel: &str,
        prompt: &str,
        response: &str,
        intent: &str,
    ) -> PyResult<i64> {
        self.db.record_dialogue(run_id, tick_index, speaker_id, listener_id, channel, prompt, response, intent)
            .map_err(|e| PyRuntimeError::new_err(format!("Dialogue log error: {}", e)))
    }

    pub fn get_agent_state_json(&self, agent_id: &str) -> PyResult<String> {
        let engine = self.state_engine.lock();
        let agent = engine.get_agent(agent_id)
            .ok_or_else(|| PyValueError::new_err(format!("Agent {} not found", agent_id)))?;
        serde_json::to_string(agent)
            .map_err(|e| PyRuntimeError::new_err(format!("JSON error: {}", e)))
    }

    pub fn get_world_state_json(&self) -> PyResult<String> {
        let engine = self.state_engine.lock();
        serde_json::to_string(&engine.world)
            .map_err(|e| PyRuntimeError::new_err(format!("JSON error: {}", e)))
    }
}

#[pyclass]
pub struct PySocialGraph {
    inner: topology::SocialGraph,
}

#[pymethods]
impl PySocialGraph {
    #[new]
    pub fn new() -> Self {
        PySocialGraph {
            inner: topology::SocialGraph::new(),
        }
    }

    pub fn add_relation(&mut self, source_id: &str, target_id: &str, edge_type: &str, weight: f64) -> PyResult<()> {
        let t = match edge_type {
            "SubordinateTo" => topology::EdgeType::SubordinateTo,
            "TaxPayerTo" => topology::EdgeType::TaxPayerTo,
            "PatronClient" => topology::EdgeType::PatronClient,
            "DebtorTo" => topology::EdgeType::DebtorTo,
            "CollusionAlliance" => topology::EdgeType::CollusionAlliance,
            "CoercionHarass" => topology::EdgeType::CoercionHarass,
            "HostileRival" => topology::EdgeType::HostileRival,
            _ => return Err(PyValueError::new_err(format!("Unknown edge type: {}", edge_type))),
        };
        self.inner.add_relation(source_id, target_id, t, weight);
        Ok(())
    }

    pub fn compute_blast_radius(&self, start_id: &str, max_depth: usize) -> PyResult<String> {
        let report = self.inner.compute_blast_radius(start_id, max_depth)
            .ok_or_else(|| PyValueError::new_err(format!("Node {} not found", start_id)))?;
        serde_json::to_string(&report)
            .map_err(|e| PyRuntimeError::new_err(format!("JSON error: {}", e)))
    }

    pub fn find_chokepoints(&self) -> PyResult<Vec<(String, usize, f64)>> {
        Ok(self.inner.find_chokepoints())
    }
}

#[pymodule]
fn socio_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PySocioEngine>()?;
    m.add_class::<PySocialGraph>()?;
    Ok(())
}

