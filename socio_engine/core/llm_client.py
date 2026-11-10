import os
import json
import urllib.request
import urllib.error
from typing import Dict, Any, Optional

def _load_env_file(env_path: str):
    """简易轻量 .env 文件解析器，避免引入外部依赖"""
    if not os.path.exists(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and k not in os.environ:
                    os.environ[k] = v

class LLMClient:
    """
    轻量且健壮的多供应商 LLM 客户端
    支持 DeepSeek, OpenAI, Anthropic, Ollama，支持无外部依赖原生 HTTP 调用与环境降级测试
    """
    def __init__(self, providers_config_path: Optional[str] = None):
        # 尝试自动从当前 socio_engine 根目录寻找 .env
        engine_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        _load_env_file(os.path.join(engine_root, ".env"))

        self.providers = {}
        if providers_config_path and os.path.exists(providers_config_path):
            import yaml
            with open(providers_config_path, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f)
                self.providers = cfg.get("providers", {})

    def generate(
        self,
        role_id: str,
        provider: str,
        model: str,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 1500,
        response_format_json: bool = False
    ) -> str:
        """
        统一调用入口：
        优先读取配置与环境变量中的 API Key，真实调用 LLM；
        若未配置 API Key 或脱机运行时，自动平滑降级至高仿真推演生成器
        """
        api_key = self._get_api_key(provider)
        if not api_key:
            return self._simulated_fallback(role_id, provider, model, system_prompt, user_prompt)

        # 针对 OpenAI / DeepSeek 等兼容接口
        base_url = self._get_base_url(provider)
        # DeepSeek 官方兼容格式: https://api.deepseek.com/chat/completions
        if base_url.endswith("/v1"):
            endpoint = f"{base_url}/chat/completions"
        else:
            endpoint = f"{base_url}/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        # DeepSeek 系列默认开启思考模式 (Thinking Mode)，对于多智能体决策，显式切换为非思考模式以获取纯净 JSON 并降低时延
        if "deepseek" in provider.lower():
            payload["thinking"] = {"type": "disabled"}

        if response_format_json:
            payload["response_format"] = {"type": "json_object"}

        try:
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data["choices"][0]["message"]
                content = choice.get("content", "")
                if not content and "reasoning_content" in choice:
                    content = choice["reasoning_content"]
                return content
        except Exception as e:
            print(f"    [!] LLM API 调用失败 ({provider}/{model}): {e}，将自动切换至仿真规则推演。")
            return self._simulated_fallback(role_id, provider, model, system_prompt, user_prompt, error_msg=str(e))

    def _get_api_key(self, provider: str) -> Optional[str]:
        prov_cfg = self.providers.get(provider.lower(), {})
        # 1. 优先读取 providers.yaml 中直接配置的 api_key
        explicit_key = prov_cfg.get("api_key")
        if explicit_key and not explicit_key.startswith("sk-your-"):
            return explicit_key

        # 2. 读取指定的环境变量名
        env_var = prov_cfg.get("api_key_env")
        if env_var and os.environ.get(env_var):
            return os.environ.get(env_var)

        # 3. 兜底常见环境变量
        env_map = {
            "deepseek": "DEEPSEEK_API_KEY",
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY"
        }
        fallback_var = env_map.get(provider.lower(), f"{provider.upper()}_API_KEY")
        return os.environ.get(fallback_var)

    def _get_base_url(self, provider: str) -> str:
        prov_cfg = self.providers.get(provider.lower(), {})
        return prov_cfg.get("base_url", "https://api.deepseek.com").rstrip("/")

    def _simulated_fallback(self, role_id: str, provider: str, model: str, system_prompt: str, user_prompt: str, error_msg: Optional[str] = None) -> str:
        """
        当未配置真实 API 密钥时的博弈推演兜底生成逻辑
        严格根据 role_id 输出符合 proposal_action 的合法 JSON 决策
        """
        r = role_id.lower()
        if "magistrate" in r:
            decision = {
                "action_type": "SET_TAX_POLICY",
                "intent_summary": "本官奉朝廷命官定税额，为保考绩与库银充盈，酌定基准税率每亩一钱，加派火耗一分五厘。",
                "parameters": {
                    "official_tax_per_mu": 0.10,
                    "surtax_rate": 0.15
                },
                "rent_extracted": 0.0,
                "is_covert": False
            }
        elif "clerk" in r:
            decision = {
                "action_type": "FORGE_LEDGER",
                "intent_summary": "趁新官到任不通钱谷，在鱼鳞图册中做平余，借火耗折银暗中加收一成，截留进私人腰包。",
                "parameters": {
                    "extra_surtax_rate": 0.10,
                    "skimmed_silver": 35.0
                },
                "rent_extracted": 35.0,
                "is_covert": True
            }
        elif "gentry" in r:
            decision = {
                "action_type": "HIDE_LAND_PATRONAGE",
                "intent_summary": "依仗举人优免名目，将族中及邻近自耕农之田地八十亩诡寄挂靠，逃避官府差徭。",
                "parameters": {
                    "hidden_mu": 80.0
                },
                "rent_extracted": 8.0,
                "is_covert": True
            }
        else: # peasant
            decision = {
                "action_type": "PAY_TAX",
                "intent_summary": "自耕农纳粮度日，变卖口粮勉强完税，但若官吏盘剥过甚则濒临流亡。",
                "parameters": {
                    "willing_to_pay": True
                },
                "rent_extracted": 0.0,
                "is_covert": False
            }
        return json.dumps(decision, ensure_ascii=False, indent=2)
