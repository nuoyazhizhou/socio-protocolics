//! socio_core 状态机与物理/经济约束引擎 (O1 Agents, O5 Resource Constraints, Privilege Rings)

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum StateError {
    #[error("Agent not found: {0}")]
    AgentNotFound(String),
    #[error("Privilege violation: Agent {agent_id} (Ring {ring}) cannot perform action {action}")]
    PrivilegeViolation {
        agent_id: String,
        ring: u8,
        action: String,
    },
    #[error("Resource constraint violated: {0}")]
    ResourceConstraint(String),
    #[error("Invalid parameter: {0}")]
    InvalidParameter(String),
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct AgentState {
    pub agent_id: String,
    pub role_type: String,
    pub role_name: String,
    pub privilege_ring: u8, // 0: 内核, 1: 地方主官, 2: 寻租中介, 3: 平民终端
    pub cash_silver: f64,
    pub stored_grain: f64,
    pub land_owned_mu: f64,
    pub land_hidden_mu: f64,
    pub tax_arrears: f64,
    pub utility_score: f64,
    pub trust_in_magistrate: f64,
    pub survival_status: String, // ALIVE, BANKRUPT, FLED, REBEL
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct WorldState {
    pub tick_index: i32,
    pub treasury_silver: f64,
    pub granary_grain: f64,
    pub grain_price_silver: f64,
    pub official_tax_per_mu: f64,
    pub surtax_rate: f64,        // 火耗率 (如 0.20 代表 20%)
    pub imperial_tax_quota: f64, // 朝廷下达的定额解京银
    pub total_tax_collected: f64,
    pub abandoned_land_mu: f64,
    pub fleeing_peasant_ratio: f64,
    pub unrest_risk_score: f64,
    pub system_entropy: f64,
    // 全县宏观里甲大盘统计 (Historical Baseline: 26,800 编户, 587,400 亩田)
    pub county_total_households: u32,
    pub county_total_land_mu: f64,
    pub county_abandoned_land_mu: f64,
    pub county_total_arrears_silver: f64,
    pub county_fleeing_ratio: f64,
}

impl Default for WorldState {
    fn default() -> Self {
        WorldState {
            tick_index: 0,
            treasury_silver: 2000.0,
            granary_grain: 5000.0,
            grain_price_silver: 1.0,
            official_tax_per_mu: 0.1, // 每亩一钱银子
            surtax_rate: 0.15,        // 官定火耗 15%
            imperial_tax_quota: 1500.0,
            total_tax_collected: 0.0,
            abandoned_land_mu: 0.0,
            fleeing_peasant_ratio: 0.0,
            unrest_risk_score: 0.05,
            system_entropy: 0.1,
            county_total_households: 26800,
            county_total_land_mu: 587400.0,
            county_abandoned_land_mu: 0.0,
            county_total_arrears_silver: 0.0,
            county_fleeing_ratio: 0.0,
        }
    }
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ActionProposal {
    pub actor_id: String,
    pub action_type: String,
    pub target_id: Option<String>,
    pub parameters: serde_json::Value,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ActionResult {
    pub success: bool,
    pub message: String,
    pub rent_extracted: f64,
    pub is_covert: bool,
    pub payload_json: String,
}

pub struct StateEngine {
    pub world: WorldState,
    pub agents: HashMap<String, AgentState>,
}

impl StateEngine {
    pub fn new() -> Self {
        StateEngine {
            world: WorldState::default(),
            agents: HashMap::new(),
        }
    }

    pub fn add_agent(&mut self, state: AgentState) {
        self.agents.insert(state.agent_id.clone(), state);
    }

    pub fn get_agent(&self, agent_id: &str) -> Option<&AgentState> {
        self.agents.get(agent_id)
    }

    pub fn get_agent_mut(&mut self, agent_id: &str) -> Option<&mut AgentState> {
        self.agents.get_mut(agent_id)
    }

    /// 执行一次 Syscall / Action 决策，进行特权环检查与物理守恒计算
    pub fn execute_action(
        &mut self,
        proposal: &ActionProposal,
    ) -> Result<ActionResult, StateError> {
        let actor = self
            .agents
            .get(&proposal.actor_id)
            .ok_or_else(|| StateError::AgentNotFound(proposal.actor_id.clone()))?
            .clone();

        match proposal.action_type.as_str() {
            "SET_TAX_POLICY" | "ISSUE_EDICT" => {
                // 特权环检查：只有 Ring-1 (县令) 有权设定县域税则与发布行政告示
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let per_mu = proposal
                    .parameters
                    .get("official_tax_per_mu")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(self.world.official_tax_per_mu);
                let surtax = proposal
                    .parameters
                    .get("surtax_rate")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(self.world.surtax_rate);

                self.world.official_tax_per_mu = per_mu;
                self.world.surtax_rate = surtax;

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "知县发布政令：基准税 {} 两/亩，加派火耗率 {:.1}%",
                        per_mu,
                        surtax * 100.0
                    ),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "AUDIT_CADASTRE" => {
                // 特权环检查：Ring-1 (知县) 启动清丈清册对勘
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                // 查账压制中介寻租空间，降低制度熵
                self.world.system_entropy = (self.world.system_entropy - 0.05).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "知县下令清勘全县黄册、鱼鳞底图与纳户串票，追查飞洒诡寄私弊".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "ZERO_SURTAX_POLICY" => {
                // 特权环检查：Ring-1 (海瑞型知县) 强制火耗归零，恢复洪武祖制
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.surtax_rate = 0.0;
                // 民怨因免除私征骤降，但官府缺乏常例公费导致行政空转摩擦上升 (RFC-007)
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.15).max(0.0);
                self.world.system_entropy += 0.08;
                Ok(ActionResult {
                    success: true,
                    message: "海瑞知县严旨：全县火耗平余一概尽除，敢浮收一厘者立枷示众！".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "PURGE_CLERKS" => {
                // 特权环检查：Ring-1 (海瑞型知县) 铁腕抄没贪吏家产
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let mut confiscated_total = 0.0;
                for clerk_id in &["clerk_qian", "clerk_crime_ma"] {
                    if let Some(clerk) = self.agents.get_mut(*clerk_id) {
                        let conf = clerk.cash_silver * 0.6; // 查抄60%非法所得
                        clerk.cash_silver -= conf;
                        clerk.utility_score = (clerk.utility_score - 100.0).max(0.0);
                        confiscated_total += conf;
                    }
                }
                self.world.treasury_silver += confiscated_total;
                // 惩贪震慑劣吏，但引发胥吏藏匿底册暗中抗法 (信息信道瘫痪，RFC-016)
                self.world.system_entropy += 0.12;
                Ok(ActionResult {
                    success: true,
                    message: format!("知县雷厉风行锁拿户刑二房蠹吏，查抄贪墨脏银 {:.1} 两充公入库！", confiscated_total),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "CONFISCATE_GENTRY_HIDDEN_LAND" => {
                // 特权环检查：Ring-1 (主管行政长官) 强制清丈特权层隐匿土地并追缴赋税
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let mut land_recovered = 0.0;
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring == 2 && agent.land_hidden_mu > 0.0 {
                        let recovered = agent.land_hidden_mu * 0.5; // 追夺50%隐匿田产
                        agent.land_hidden_mu -= recovered;
                        agent.utility_score = (agent.utility_score - 80.0).max(0.0);
                        land_recovered += recovered;
                    }
                }
                let tax_recovered = land_recovered * self.world.official_tax_per_mu;
                self.world.treasury_silver += tax_recovered;
                self.world.system_entropy += 0.15; // 特权层剧烈反弹，触发高层政治抗击
                Ok(ActionResult {
                    success: true,
                    message: format!("行政主官亲督丈量，追回特权层隐匿田产 {:.0} 亩，追征正赋 {:.1} 两！", land_recovered, tax_recovered),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "CRACKDOWN_ON_USURY" => {
                // 特权环检查：Ring-1 (主管行政长官) 封禁高利贷与典当绝卖
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                if let Some(target) = proposal.target_id.as_deref().and_then(|tid| self.agents.get_mut(tid)) {
                    target.utility_score = (target.utility_score - 50.0).max(0.0);
                } else {
                    for agent in self.agents.values_mut() {
                        if agent.privilege_ring == 2 && (agent.agent_id.contains("sun") || agent.agent_id.contains("lender") || agent.agent_id.contains("pawn")) {
                            agent.utility_score = (agent.utility_score - 50.0).max(0.0);
                        }
                    }
                }
                Ok(ActionResult {
                    success: true,
                    message: "行政长官封存典当与高利借贷账簿，严禁高利盘剥，核销利滚利绝卖契约！".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "RECRUIT_NEW_CLERKS" => {
                // 特权环检查：Ring-1 (主管行政长官) 辟黜旧中介，重新辟选新吏 (去中介化 / RFC-004)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                // 重置所有 Ring-2 中介老吏寻租垄断，打破怠工壁垒
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring == 2 && (agent.agent_id.contains("clerk") || agent.agent_id.contains("bailiff")) {
                        agent.cash_silver = 10.0;
                        agent.utility_score = 50.0;
                    }
                }
                // 制度熵大幅压制，信息垄断被击碎，行政机器恢复运转
                self.world.system_entropy = (self.world.system_entropy - 0.25).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "行政长官严令：罢黜把持册籍之贪墨老蠹，从下层清白士人与良善保正中辟选新吏，破除中间层绑架！".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "DIRECT_PUBLIC_CADASTRE" => {
                // 特权环检查：Ring-1 (主管行政长官) 绕过中间层，下乡公勘公丈 (RFC-016 广播拓扑)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let mut recovered_mu = 0.0;
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring == 2 && agent.land_hidden_mu > 0.0 {
                        let r = agent.land_hidden_mu.min(250.0);
                        agent.land_hidden_mu -= r;
                        recovered_mu += r;
                    }
                }
                // 犒劳协助丈量之基层人员
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring >= 2 && (agent.agent_id.contains("lijia") || agent.agent_id.contains("scholar") || agent.agent_id.contains("peasant")) {
                        agent.cash_silver += 5.0;
                        agent.utility_score += 30.0;
                        break;
                    }
                }
                self.world.system_entropy = (self.world.system_entropy - 0.20).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: format!("行政主官亲督下乡公勘，大众同量，现场丈出特权层隐田 {:.0} 亩，图册公开明示！", recovered_mu),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "ESTABLISH_TRANSPARENT_CODE" => {
                // 特权环检查：Ring-1 (主管行政长官) 推行白话条约 / 勒石公开税则，由票直达万民 (RFC-007)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.surtax_rate = 0.0;
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.12).max(0.0);
                self.world.system_entropy = (self.world.system_entropy - 0.15).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "行政长官推行规费白话条约，税额定死勒石永禁，由票直发下户，斩断中间层贪墨接口！".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "RESTORE_LAND_TO_PEASANTS" => {
                // 特权环检查：Ring-1 强令退田还民，彻底恢复底层物理造血机能 (O5 资源重置)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let mut pool: f64 = 0.0;
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring == 2 && agent.land_owned_mu > 50.0 {
                        agent.land_owned_mu -= 10.0;
                        pool += 10.0;
                    }
                }
                let mut restored_mu = 0.0;
                for agent in self.agents.values_mut() {
                    if agent.privilege_ring == 3 && (agent.survival_status == "BANKRUPT" || agent.land_owned_mu < 10.0) {
                        let grant = pool.min(5.0);
                        if grant > 0.0 {
                            agent.land_owned_mu += grant;
                            agent.survival_status = "ALIVE".to_string();
                            agent.utility_score += 80.0;
                            pool -= grant;
                            restored_mu += grant;
                        }
                    }
                }
                self.world.abandoned_land_mu = (self.world.abandoned_land_mu - restored_mu).max(0.0);
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.15).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: format!("行政长官严令退田还民：追夺特权层兼并土地 {:.0} 亩，划归困难底层小农，化解破产流亡！", restored_mu),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "PASSIVE_RESISTANCE" => {
                // 特权环检查：Ring-2 (胥吏) 集体怠工、藏匿图册、故意报错
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.system_entropy += 0.15; // 系统制度熵激增，征管陷入泥潭
                Ok(ActionResult {
                    success: true,
                    message: "户刑二房书吏集体告病怠工，暗将四柱清册与鱼鳞底图藏匿深山，致官衙两眼抹黑".to_string(),
                    rent_extracted: 0.0,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "SEND_CAPITAL_LETTER" => {
                // 特权环检查：Ring-2 (乡绅) 动用京察门生人脉弹劾知县
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.system_entropy += 0.10;
                Ok(ActionResult {
                    success: true,
                    message: "乡绅急递快马密信直达通政司与户部侍郎，以'苛求清名、摧残名教、摇撼根本'弹劾知县".to_string(),
                    rent_extracted: 0.0,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "FORGE_LEDGER" | "EXTRACT_SURCHARGE" | "INJECT_SURCHARGE" | "HIDE_CADASTRE_ENTRY" => {
                // 特权环检查：Ring-2 (户房书吏) 寻租操作
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let skimmed_silver = proposal
                    .parameters
                    .get("skimmed_silver")
                    .or_else(|| proposal.parameters.get("surcharge_rate"))
                    .and_then(|v| v.as_f64())
                    .map(|v| if v < 1.0 { v * 150.0 } else { v }) // 若填费率则按折合抽取
                    .unwrap_or(35.0);

                if let Some(clerk) = self.agents.get_mut(&proposal.actor_id) {
                    clerk.cash_silver += skimmed_silver;
                    clerk.utility_score += skimmed_silver * 0.8;
                }
                self.world.system_entropy = (self.world.system_entropy + 0.06).min(1.0);
                self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.03).min(1.0);

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "书吏借火耗平余与碎银称量低色折算，暗中截留私囊 {} 两白银",
                        skimmed_silver
                    ),
                    rent_extracted: skimmed_silver,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "SUBMIT_REPORT" => {
                // 特权环检查：Ring-2 (书吏) 呈递公文报表或告密
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                Ok(ActionResult {
                    success: true,
                    message: "书吏向官衙呈递税粮文书底册与密报".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "HIDE_LAND_PATRONAGE" | "ACCEPT_MORTGAGE" => {
                // 特权环检查：Ring-2 (乡绅/典当) 优免隐匿与典当兼并
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let hidden_mu = proposal
                    .parameters
                    .get("hidden_mu")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(50.0);

                if let Some(gentry) = self.agents.get_mut(&proposal.actor_id) {
                    gentry.land_hidden_mu += hidden_mu;
                    gentry.utility_score += hidden_mu * 0.3;
                }
                self.world.system_entropy += 0.05;

                Ok(ActionResult {
                    success: true,
                    message: format!("士绅/当铺主通过优免庇护与高利贷抵押条款兼并隐匿田亩 {} 亩", hidden_mu),
                    rent_extracted: hidden_mu * self.world.official_tax_per_mu,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "PAY_TAX" | "PAY_TAX_IN_FULL" => {
                // 平民或地主纳税 (Ring-2 / Ring-3)
                let peasant_id = proposal.actor_id.clone();
                let (land, mut cash, mut grain, arrears) = {
                    let a = self
                        .agents
                        .get(&peasant_id)
                        .ok_or_else(|| StateError::AgentNotFound(peasant_id.clone()))?;
                    (
                        a.land_owned_mu,
                        a.cash_silver,
                        a.stored_grain,
                        a.tax_arrears,
                    )
                };

                let nominal_tax =
                    land * self.world.official_tax_per_mu * (1.0 + self.world.surtax_rate);
                let actual_paid;

                if cash >= nominal_tax {
                    cash -= nominal_tax;
                    actual_paid = nominal_tax;
                } else {
                    let mut paid = cash;
                    let deficit = nominal_tax - cash;
                    cash = 0.0;
                    // 谷贱伤农与典当贴水机制 (RFC-008 & O5):
                    // 农户急迫以粮换银完税，典当行/米商收取 15% 折价贴水
                    let effective_grain_price = (self.world.grain_price_silver * 0.85).max(0.1);
                    let grain_needed = deficit / effective_grain_price;
                    if grain >= grain_needed {
                        grain -= grain_needed;
                        actual_paid = nominal_tax;
                        let pawn_profit = deficit * 0.15;
                        if let Some(sun) = self.agents.get_mut("gentry_sun") {
                            sun.cash_silver += pawn_profit;
                            sun.utility_score += pawn_profit * 0.5;
                        }
                    } else {
                        paid += grain * effective_grain_price;
                        let pawn_profit = grain * self.world.grain_price_silver * 0.15;
                        grain = 0.0;
                        actual_paid = paid;
                        if let Some(sun) = self.agents.get_mut("gentry_sun") {
                            sun.cash_silver += pawn_profit;
                            sun.utility_score += pawn_profit * 0.5;
                        }
                    }
                }

                let remaining_arrears = arrears + (nominal_tax - actual_paid);

                // 更新农民状态
                if let Some(p) = self.agents.get_mut(&peasant_id) {
                    p.cash_silver = cash;
                    p.stored_grain = grain;
                    p.tax_arrears = remaining_arrears;

                    // 生存线判定 (Subsistence Threshold, RFC-008 & RFC-017)
                    if p.stored_grain < 2.0 && p.cash_silver < 1.0 {
                        p.survival_status = "BANKRUPT".to_string();
                        p.trust_in_magistrate = (p.trust_in_magistrate - 0.2).max(0.0);
                        self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.05).min(1.0);
                    }
                }

                self.world.treasury_silver += actual_paid;
                self.world.total_tax_collected += actual_paid;

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "节点 {} 完纳夏秋税银 {} 两，当前积欠 {} 两",
                        peasant_id, actual_paid, remaining_arrears
                    ),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "SEEK_CLERK_MERCY" => {
                // 平民向胥吏哀求宽限
                Ok(ActionResult {
                    success: true,
                    message: "承压节点前往户房向经手书吏呈递苦情禀帖，哀求宽展火耗".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "FLEE_OR_RESIST" | "FLEE_AND_ABANDON_LAND" | "JOIN_RIOT" => {
                // Ring-3 终端抗税或流亡
                let peasant_id = proposal.actor_id.clone();
                let mut land_abandoned = 0.0;
                if let Some(p) = self.agents.get_mut(&peasant_id) {
                    land_abandoned = p.land_owned_mu;
                    p.land_owned_mu = 0.0;
                    p.survival_status = "FLED".to_string();
                    p.trust_in_magistrate = 0.0;
                }
                self.world.abandoned_land_mu += land_abandoned;
                self.world.fleeing_peasant_ratio += 0.05;
                self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.15).min(1.0);

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "自耕农 {} 破产逃荒，抛荒田亩 {} 亩，激化地方流民风险",
                        peasant_id, land_abandoned
                    ),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "MEDIATE_WATER_DISPUTE" => {
                // 特权环检查：Ring-1 (县丞 / 知县) 调解丰乐河分水与械斗
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.06).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "县丞亲赴丰乐河水圳调停陈李二族分水之争，平息械斗戾气".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "INSPECT_GRAIN_TRANSPORT" => {
                // 特权环检查：Ring-1 (县丞) 督察粮运水利
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.system_entropy = (self.world.system_entropy - 0.04).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "县丞督理南粮漕运与预备仓，核对仓底霉烂损耗".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "OPPOSE_MAGISTRATE_CADASTRE" => {
                // 特权环检查：Ring-1 (县丞) 与本地士绅利益合流掣肘知县
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.system_entropy += 0.05;
                Ok(ActionResult {
                    success: true,
                    message: "佐贰官暗中附和本土士绅，以'民情惊扰'为由向知府进言阻滞清丈".to_string(),
                    rent_extracted: 0.0,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "ENFORCE_TAX_LEVY" => {
                // 特权环检查：Ring-2 (快班捕头 / 差役) 暴力催征
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.04).min(1.0);
                Ok(ActionResult {
                    success: true,
                    message: "快班捕役持批头下乡拘传欠税里长与下户，敲朴逼征".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "EXTORT_TRAVEL_EXPENSE" => {
                // 特权环检查：Ring-2 (快班捕头 / 差役) 敲诈鞋袜牌费
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let extorted = proposal.parameters.get("silver")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(5.0);
                
                if let Some(bailiff) = self.agents.get_mut(&proposal.actor_id) {
                    bailiff.cash_silver += extorted;
                    bailiff.utility_score += extorted * 0.7;
                }
                self.world.system_entropy = (self.world.system_entropy + 0.04).min(1.0);
                self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.03).min(1.0);

                Ok(ActionResult {
                    success: true,
                    message: format!("差役借登门催征之机，向里长及纳户勒索'鞋袜钱'与'常例' {} 两", extorted),
                    rent_extracted: extorted,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "REGISTER_LAWSUIT" => {
                // 特权环检查：Ring-2 (刑房书吏) 受理词讼
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.system_entropy += 0.02;
                Ok(ActionResult {
                    success: true,
                    message: "刑房书吏受理事涉均平丝绢、争田夺产与聚众词讼状词".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "MANIPULATE_TESTIMONY" => {
                // 特权环检查：Ring-2 (刑房书吏) 舞文弄墨受贿改供
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let bribe = proposal.parameters.get("bribe_silver")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(20.0);
                
                if let Some(clerk) = self.agents.get_mut(&proposal.actor_id) {
                    clerk.cash_silver += bribe;
                    clerk.utility_score += bribe * 0.8;
                }
                self.world.system_entropy += 0.07;
                Ok(ActionResult {
                    success: true,
                    message: format!("刑房老吏删改案情口供，收取讼费规费 {} 两", bribe),
                    rent_extracted: bribe,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "LIQUIDATE_GRAIN_FOR_SILVER" => {
                // 平民向典当行急售粮食换取白银 (Ring-3)
                let peasant_id = proposal.actor_id.clone();
                let grain_to_sell = proposal.parameters.get("grain_amount")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(5.0);
                
                let mut actual_sold = 0.0;
                let mut silver_received = 0.0;
                let mut pawn_fee = 0.0;

                if let Some(p) = self.agents.get_mut(&peasant_id) {
                    actual_sold = grain_to_sell.min(p.stored_grain);
                    p.stored_grain -= actual_sold;
                    let market_value = actual_sold * self.world.grain_price_silver;
                    pawn_fee = market_value * 0.18; // 典当行扣下 18% 贴水与手续费
                    silver_received = market_value - pawn_fee;
                    p.cash_silver += silver_received;
                }

                if let Some(sun) = self.agents.get_mut("gentry_sun") {
                    sun.cash_silver += pawn_fee;
                    sun.stored_grain += actual_sold;
                }

                Ok(ActionResult {
                    success: true,
                    message: format!("节点 {} 在典当行售粮 {} 石，按折价贴水得银 {:.2} 两 (典当行扣息 {:.2} 两)", peasant_id, actual_sold, silver_received, pawn_fee),
                    rent_extracted: pawn_fee,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "REQUEST_RELIEF" | "TAX_REDUCTION_RELIEF" => {
                // 特权环检查：Ring-1 (知县 / 县丞) 向上申详蠲免夏秋税银并开仓赈济 (RFC-007)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let relief_silver = 50.0f64.min(self.world.treasury_silver);
                self.world.treasury_silver -= relief_silver;
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.18).max(0.0);
                self.world.system_entropy = (self.world.system_entropy - 0.06).max(0.0);

                // 解救破产自耕农与下等户
                let mut saved_count = 0;
                for agent in self.agents.values_mut() {
                    if agent.role_type == "peasant" {
                        agent.tax_arrears = (agent.tax_arrears * 0.5).max(0.0);
                        if agent.survival_status == "BANKRUPT" {
                            agent.survival_status = "ALIVE".to_string();
                            agent.stored_grain += 1.5;
                            agent.utility_score += 25.0;
                            saved_count += 1;
                        }
                    }
                }

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "知县详请蠲免夏秋税银并动支仓银 {:.1} 两开仓赈济，蠲免五成积欠，解救 {} 户濒危自耕农，大幅平息民怨隐患！",
                        relief_silver, saved_count
                    ),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "PUNISH_CORRUPTION" => {
                // 特权环检查：Ring-1 (知县) 整饬吏治，严惩户房贪墨舞弊
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.surtax_rate = (self.world.surtax_rate - 0.04).max(0.05);
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.10).max(0.0);
                self.world.system_entropy = (self.world.system_entropy - 0.08).max(0.0);

                let mut confiscated_silver = 0.0;
                for agent in self.agents.values_mut() {
                    if agent.role_type == "clerk" && agent.cash_silver > 10.0 {
                        let fine = (agent.cash_silver * 0.3).min(15.0);
                        agent.cash_silver -= fine;
                        confiscated_silver += fine;
                    }
                }
                self.world.treasury_silver += confiscated_silver;

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "知县严令整饬吏治，革除私加火耗四分，追夺贪墨经管书吏羡余 {:.1} 两入库，安定民心！",
                        confiscated_silver
                    ),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "CRACKDOWN_COMMUNITY_POOL" => {
                // 特权环检查：Ring-2 (经管公吏 / 催征捕头) 诬告抄封民间互助拼单会 (演化分叉：分支 A)
                if actor.privilege_ring != 2 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                let extorted = 15.0;
                if let Some(clerk) = self.agents.get_mut(&proposal.actor_id) {
                    clerk.cash_silver += extorted;
                    clerk.utility_score += extorted * 0.8;
                }
                self.world.system_entropy = (self.world.system_entropy + 0.08).min(1.0);
                self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.15).min(1.0);

                Ok(ActionResult {
                    success: true,
                    message: format!(
                        "经管钱吏勾结捕役诬告民间五人互助结会为'私相结社图谋抗税'，抄封会钱 {:.1} 两，扑灭民间自救火种！",
                        extorted
                    ),
                    rent_extracted: extorted,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "LEGALISE_COMMUNITY_POOL" => {
                // 特权环检查：Ring-1 (知县) 采纳民间自发拼单会纳为官规主干 (演化分叉：分支 B)
                if actor.privilege_ring > 1 {
                    return Err(StateError::PrivilegeViolation {
                        agent_id: actor.agent_id,
                        ring: actor.privilege_ring,
                        action: proposal.action_type.clone(),
                    });
                }
                self.world.surtax_rate = (self.world.surtax_rate - 0.03).max(0.05);
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.15).max(0.0);
                self.world.system_entropy = (self.world.system_entropy - 0.06).max(0.0);

                Ok(ActionResult {
                    success: true,
                    message: "知县核验账册力排众议，正式颁布告示将自发五人结会纳为官规主干推行，严禁私加纸笔头子钱！".to_string(),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "FOUND_COMMUNITY_SOCIETY" | "MUTATION_UNDERGROUND_CREDIT_POOL" | "MUTATION_FORWARD_GRAIN_SALE" | "MUTATION_COLLECTIVE_PETITION" => {
                // Ring-3 终端自耕农与佃农自发探索变异 (RFC-018)
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.04).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: format!("民间承压节点发起变异探索 [{}]，建立局部自治缓冲！", proposal.action_type),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "LEND_GRAIN_TO_NEIGHBOR" => {
                // Ring-3 中等户守望相助，私借口粮救助穷邻
                let mut lent = 0.0;
                if let Some(lender) = self.agents.get_mut(&proposal.actor_id) {
                    if lender.stored_grain > 5.0 {
                        lent = 1.5;
                        lender.stored_grain -= lent;
                        lender.utility_score += 10.0;
                    }
                }
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.04).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: format!("中等户发扬守望相助之谊，借出口粮 {:.1} 石助弱势穷邻度过饥荒", lent),
                    rent_extracted: 0.0,
                    is_covert: false,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            "SLACK_OFF_AND_MERCY" => {
                // Ring-2 经手吏员畏惧民变，暗中少记折算放水
                self.world.unrest_risk_score = (self.world.unrest_risk_score - 0.03).max(0.0);
                Ok(ActionResult {
                    success: true,
                    message: "经手吏员畏惧激变地方遭夜路闷棍，在由票折色上悄悄放水宽展".to_string(),
                    rent_extracted: 0.0,
                    is_covert: true,
                    payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
                })
            }

            _ => Ok(ActionResult {
                success: true,
                message: format!("通用行动 [{}] 已记录", proposal.action_type),
                rent_extracted: 0.0,
                is_covert: false,
                payload_json: serde_json::to_string(&proposal.parameters).unwrap_or_default(),
            }),
        }
    }

    /// 推进一个时钟 Tick：农田四季产出、动态米价、粮食消耗、逃荒亏空连坐转嫁与全县宏观大盘
    pub fn step_tick(&mut self, yield_multiplier: f64, price_multiplier: f64) {
        self.world.tick_index += 1;
        let season_quarter = (self.world.tick_index - 1) % 4 + 1; // 1: 春, 2: 夏, 3: 秋, 4: 冬

        // 自然衰减与阻尼 (Relaxation & Negative Feedback Damping)
        self.world.unrest_risk_score = (self.world.unrest_risk_score * 0.92).max(0.0);
        if self.world.surtax_rate > 0.15 {
            self.world.system_entropy = (self.world.system_entropy + 0.02).min(1.0);
        } else {
            self.world.system_entropy = (self.world.system_entropy * 0.95).max(0.0);
        }

        // 1. 四季动态米价模型 (HISTORICAL_BASELINE.md 考据 & 外部冲击动态联动)
        let base_price = match season_quarter {
            1 => 1.10, // 春荒青黄不接：米价微扬
            2 => 1.35, // 夏荒伏旱催折：米价达峰，缺粮求借
            3 => 0.75, // 秋收晚稻大熟：米贱伤农，折银交税
            4 => 1.00, // 冬季平稳完赋
            _ => 1.00,
        };

        // 供需物理耦合：若秋收遭遇蝗旱天灾 (yield_multiplier < 0.95)，供给急剧收缩，米价逆势上涨！
        // 若逢丰收大跌 (price_multiplier < 0.95)，米价下探
        let effective_grain_price = if yield_multiplier < 0.95 {
            (base_price / yield_multiplier.max(0.3)).min(2.5) * price_multiplier
        } else {
            base_price * price_multiplier
        };
        self.world.grain_price_silver = (effective_grain_price * 100.0).round() / 100.0;

        // 2. 全县宏观里甲大盘统计 (Historical Baseline: 26,800 编户, 587,400 亩田)
        let excess_surtax = (self.world.surtax_rate - 0.15).max(0.0);
        let seasonal_pressure = match season_quarter {
            1 => 1.2, // 春荒压迫
            2 => 1.8, // 夏荒伏旱大缺口
            3 => 0.5, // 秋收相对缓和
            4 => 1.5, // 冬税考成逼迫
            _ => 1.0,
        };
        let new_abandoned_macro = excess_surtax * 1200.0 * seasonal_pressure;
        self.world.county_abandoned_land_mu += new_abandoned_macro;
        self.world.county_fleeing_ratio = self.world.county_abandoned_land_mu / self.world.county_total_land_mu;
        self.world.county_total_arrears_silver += new_abandoned_macro * self.world.official_tax_per_mu;
        self.world.unrest_risk_score = (self.world.unrest_risk_score + self.world.county_fleeing_ratio * 0.15).min(1.0);

        // 3. 遍历显式微观农民：按四季收获，并消耗生存口粮
        let mut fled_count = 0;
        let mut total_peasants = 0;

        for agent in self.agents.values_mut() {
            if agent.role_type == "peasant" {
                total_peasants += 1;
                if agent.survival_status == "FLED" || agent.survival_status == "DEAD" || agent.survival_status == "FLED_OR_DEAD" {
                    fled_count += 1;
                    continue;
                }

                // 四季农产真实模型 (HISTORICAL_BASELINE.md 考据 & 外部产量冲击联动):
                let yield_per_mu = match season_quarter {
                    1 => 0.3, // 春季：收春麦/菜籽微产 0.3 石/亩
                    2 => 0.0, // 夏季：青黄不接伏旱，无大粮产出
                    3 => 2.2, // 秋季：晚稻大丰收，主产 2.2 石/亩
                    4 => 0.0, // 冬季：农闲催征，无粮食产出
                    _ => 0.0,
                };
                let effective_yield = yield_per_mu * yield_multiplier;
                let harvest = agent.land_owned_mu * effective_yield;
                agent.stored_grain += harvest;

                // 季度生存口粮：单家每季度需消耗 3.0 石口粮
                if agent.stored_grain >= 3.0 {
                    agent.stored_grain -= 3.0;
                } else {
                    let shortage = 3.0 - agent.stored_grain;
                    agent.stored_grain = 0.0;
                    // 若无粮且无银买粮，陷入濒死破产
                    if agent.cash_silver >= shortage * self.world.grain_price_silver {
                        agent.cash_silver -= shortage * self.world.grain_price_silver;
                    } else {
                        agent.survival_status = "BANKRUPT".to_string();
                        // 极度饥寒交迫时，推高民变暴动指数 (capped at 1.0)
                        self.world.unrest_risk_score = (self.world.unrest_risk_score + 0.03).min(1.0);
                    }
                }
            }
        }

        if total_peasants > 0 {
            self.world.fleeing_peasant_ratio = fled_count as f64 / total_peasants as f64;
        }

        // 4. 明代里甲包赔制度：若有逃荒抛荒，抛荒田亩税额自动转嫁至第七图轮值里长赵大富头上
        if self.world.abandoned_land_mu > 0.0 {
            let deficit_tax = self.world.abandoned_land_mu * self.world.official_tax_per_mu;
            if let Some(lijia) = self.agents.get_mut("peasant_zhao_lijia") {
                if lijia.survival_status != "FLED" {
                    lijia.tax_arrears += deficit_tax;
                }
            }
        }

        // 5. 历史生命周期相变节点：
        // 第 8 季度 (万历二年秋试)：若进学户吴秀才家存活且未破产，长子中秀才！获得生员特权环跃迁
        if self.world.tick_index == 8 {
            if let Some(wu) = self.agents.get_mut("peasant_wu_scholar") {
                if wu.survival_status == "ALIVE" {
                    wu.privilege_ring = 2; // 跃升为士绅优免环
                    wu.utility_score += 100.0;
                }
            }
        }
    }
}
