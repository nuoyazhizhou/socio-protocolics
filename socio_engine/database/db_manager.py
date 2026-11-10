import sqlite3
import json
import os
from typing import Dict, Any, List

class DatabaseManager:
    """仿真数据库管理类：保证事务隔离与事件溯源持久化"""

    def __init__(self, db_path: str):
        self.db_path = db_path
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._configure_pragmas()

    def _configure_pragmas(self):
        """配置 SQLite 高性能与并发 PRAGMA (WAL 模式)"""
        with self.conn:
            self.conn.execute("PRAGMA journal_mode = WAL;")
            self.conn.execute("PRAGMA synchronous = NORMAL;")
            self.conn.execute("PRAGMA busy_timeout = 10000;")
            self.conn.execute("PRAGMA foreign_keys = ON;")

    def init_schema(self, schema_sql_path: str):
        """执行 DDL 初始化建表"""
        with open(schema_sql_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
        with self.conn:
            self.conn.executescript(sql_script)

    def register_run(self, run_id: str, scenario_name: str, description: str, config_snapshot: Dict[str, Any]):
        """记录新的仿真场次"""
        with self.conn:
            self.conn.execute(
                """INSERT INTO sim_runs (run_id, scenario_name, description, config_snapshot)
                   VALUES (?, ?, ?, ?)""",
                (run_id, scenario_name, description, json.dumps(config_snapshot, ensure_ascii=False))
            )

    def register_agent(self, run_id: str, agent_id: str, role_type: str, role_name: str,
                       privilege_ring: int, llm_provider: str, model_name: str):
        """注册智能体身份与模型分配"""
        with self.conn:
            self.conn.execute(
                """INSERT INTO agent_registry (agent_id, run_id, role_type, role_name, privilege_ring, llm_provider, model_name)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (agent_id, run_id, role_type, role_name, privilege_ring, llm_provider, model_name)
            )

    def record_event(self, run_id: str, tick: int, actor_id: str, target_id: str,
                     action_type: str, action_payload: Dict[str, Any],
                     rent_extracted: float = 0.0, is_covert: bool = False):
        """记录具体的协议系统调用/事件流水"""
        with self.conn:
            self.conn.execute(
                """INSERT INTO protocol_events (run_id, tick_index, actor_id, target_id, action_type, action_payload, rent_extracted, is_covert)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (run_id, tick, actor_id, target_id, action_type, json.dumps(action_payload, ensure_ascii=False), rent_extracted, is_covert)
            )

    def close(self):
        if self.conn:
            self.conn.close()

