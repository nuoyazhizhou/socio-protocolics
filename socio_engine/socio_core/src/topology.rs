//! socio_core 社会网络拓扑与中介依附分析 (借鉴 Callwarden graph.rs 与 impact.rs 的拓扑分析能力)

use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::Direction;
use serde::{Deserialize, Serialize};
use std::collections::{HashMap, HashSet, VecDeque};

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum EdgeType {
    SubordinateTo,    // 上下级行政隶属 (书吏 -> 县令)
    TaxPayerTo,       // 赋税征缴链 (小农 -> 书吏)
    PatronClient,     // 缙绅庇护与田产挂靠 (小农 -> 乡绅)
    DebtorTo,         // 债务高利贷绑定 (小农 -> 缙绅/典当)
    CollusionAlliance,// 寻租同盟与利益输送 (书吏 <-> 乡绅)
    CoercionHarass,   // 暴力差役催逼与勒索 (差役 -> 里长/自耕农)
    HostileRival,     // 宗族世仇与利益死斗 (争水村落世仇)
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct EdgeData {
    pub edge_type: EdgeType,
    pub weight: f64, // 资金流或依赖强度
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ImpactReport {
    pub target_id: String,
    pub affected_agents: Vec<String>,
    pub depth_map: HashMap<String, usize>,
    pub total_tax_at_risk: f64,
}

pub struct SocialGraph {
    graph: DiGraph<String, EdgeData>,
    node_map: HashMap<String, NodeIndex>,
    reverse_node_map: HashMap<NodeIndex, String>,
}

impl SocialGraph {
    pub fn new() -> Self {
        SocialGraph {
            graph: DiGraph::new(),
            node_map: HashMap::new(),
            reverse_node_map: HashMap::new(),
        }
    }

    pub fn get_or_create_node(&mut self, agent_id: &str) -> NodeIndex {
        if let Some(&idx) = self.node_map.get(agent_id) {
            return idx;
        }
        let idx = self.graph.add_node(agent_id.to_string());
        self.node_map.insert(agent_id.to_string(), idx);
        self.reverse_node_map.insert(idx, agent_id.to_string());
        idx
    }

    pub fn add_relation(&mut self, source_id: &str, target_id: &str, edge_type: EdgeType, weight: f64) {
        let u = self.get_or_create_node(source_id);
        let v = self.get_or_create_node(target_id);
        self.graph.add_edge(u, v, EdgeData { edge_type, weight });
    }

    /// 爆炸半径分析 (借鉴 Callwarden impact.rs)：
    /// 当某一节点破产、逃亡、叛乱或被查办时，顺着依附链与债务链波及的所有下游/上游主体
    pub fn compute_blast_radius(&self, start_id: &str, max_depth: usize) -> Option<ImpactReport> {
        let &start_idx = self.node_map.get(start_id)?;
        let mut affected = Vec::new();
        let mut depth_map = HashMap::new();
        let mut visited = HashSet::new();
        let mut queue = VecDeque::new();

        visited.insert(start_idx);
        queue.push_back((start_idx, 0));

        while let Some((curr_idx, depth)) = queue.pop_front() {
            if depth > max_depth {
                break;
            }
            if let Some(agent_id) = self.reverse_node_map.get(&curr_idx) {
                if curr_idx != start_idx {
                    affected.push(agent_id.clone());
                    depth_map.insert(agent_id.clone(), depth);
                }
            }

            // 遍历所有相连边 (无论入边出边，代表社会关系纠缠)
            for neighbor in self.graph.neighbors_undirected(curr_idx) {
                if !visited.contains(&neighbor) {
                    visited.insert(neighbor);
                    queue.push_back((neighbor, depth + 1));
                }
            }
        }

        Some(ImpactReport {
            target_id: start_id.to_string(),
            affected_agents: affected,
            depth_map,
            total_tax_at_risk: 0.0,
        })
    }

    /// 识别系统中的核心中介卡位点 (Chokepoint / Middleman Centrality)
    /// 计算每个节点的度中心性与中介承载权重 (RFC-004 中介寄生)
    pub fn find_chokepoints(&self) -> Vec<(String, usize, f64)> {
        let mut results = Vec::new();
        for (agent_id, &idx) in &self.node_map {
            let in_degree = self.graph.neighbors_directed(idx, Direction::Incoming).count();
            let out_degree = self.graph.neighbors_directed(idx, Direction::Outgoing).count();
            let total_degree = in_degree + out_degree;

            // 累计通过该节点的权重
            let mut total_weight = 0.0;
            for edge in self.graph.edges_directed(idx, Direction::Incoming) {
                total_weight += edge.weight().weight;
            }
            for edge in self.graph.edges_directed(idx, Direction::Outgoing) {
                total_weight += edge.weight().weight;
            }

            results.push((agent_id.clone(), total_degree, total_weight));
        }

        // 按连接度排序
        results.sort_by(|a, b| b.1.cmp(&a.1).then(b.2.partial_cmp(&a.2).unwrap_or(std::cmp::Ordering::Equal)));
        results
    }
}
