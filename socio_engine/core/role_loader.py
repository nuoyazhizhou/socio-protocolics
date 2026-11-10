import os
import yaml
from dataclasses import dataclass
from typing import Dict, Any, List

@dataclass
class RoleDefinition:
    role_id: str
    role_name: str
    privilege_ring: int
    provider: str
    model: str
    temperature: float
    max_tokens: int
    action_space: List[str]
    system_prompt: str
    raw_config: Dict[str, Any]

class RoleLoader:
    """动态角色加载器：完全从 roles/<role_id>/ 的 yaml + md 加载定义"""
    
    def __init__(self, roles_dir: str):
        self.roles_dir = roles_dir
        self.roles: Dict[str, RoleDefinition] = {}

    def load_all_roles(self) -> Dict[str, RoleDefinition]:
        """扫描 roles 目录下所有子目录并装配 RoleDefinition"""
        if not os.path.exists(self.roles_dir):
            raise FileNotFoundError(f"Roles directory not found: {self.roles_dir}")

        for entry in os.scandir(self.roles_dir):
            if entry.is_dir() and entry.name != "templates":
                role_def = self._load_single_role(entry.path)
                if role_def:
                    self.roles[role_def.role_id] = role_def
        return self.roles

    def _load_single_role(self, role_path: str) -> RoleDefinition:
        config_path = os.path.join(role_path, "role_config.yaml")
        prompt_path = os.path.join(role_path, "system_prompt.md")

        if not os.path.exists(config_path) or not os.path.exists(prompt_path):
            print(f"[WARN] Incomplete role definition in {role_path}, skipping.")
            return None

        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        with open(prompt_path, "r", encoding="utf-8") as f:
            system_prompt = f.read()

        llm_cfg = cfg.get("llm_settings", {})
        
        return RoleDefinition(
            role_id=cfg.get("role_id", os.path.basename(role_path)),
            role_name=cfg.get("role_name", "Unknown"),
            privilege_ring=cfg.get("privilege_ring", 3),
            provider=llm_cfg.get("provider", "deepseek"),
            model=llm_cfg.get("model", "deepseek-chat"),
            temperature=llm_cfg.get("temperature", 0.7),
            max_tokens=llm_cfg.get("max_tokens", 1000),
            action_space=cfg.get("action_space", []),
            system_prompt=system_prompt,
            raw_config=cfg
        )

