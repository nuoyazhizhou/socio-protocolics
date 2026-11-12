import json
from typing import Dict, Any, Optional
from core.role_loader import RoleDefinition
from core.llm_client import LLMClient

class RoleAgent:
    """
    通用智能体驱动类 (Agent-as-Data)
    没有任何硬编码的角色业务逻辑，由 RoleDefinition (基础原型) + 实例属性 (家境/特质/恩怨) 注入驱动
    认知决策由 LLMClient 负责，物理执行由 Rust socio_core 负责
    """
    def __init__(
        self,
        agent_id: str,
        role_def: RoleDefinition,
        instance_name: Optional[str] = None,
        background: Optional[str] = None,
        trait: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        llm_client: Optional[LLMClient] = None,
        objective_function: Optional[str] = None,
        privilege_ring: Optional[int] = None
    ):
        self.agent_id = agent_id
        self.role_def = role_def
        self.role_id = role_def.role_id
        self.role_name = instance_name or role_def.role_name
        self.background = background or ""
        self.trait = trait or "NORMAL"
        self.objective_function = objective_function or ""
        self.privilege_ring = privilege_ring if privilege_ring is not None else role_def.privilege_ring
        self.model = model or role_def.model
        self.temperature = temperature if temperature is not None else role_def.temperature
        self.llm_client = llm_client or LLMClient()
        
        # 本地记忆/上下文
        self.recent_dialogues = []

    def build_prompt_context(self, world_state: Dict[str, Any], agent_state: Dict[str, Any], observation: Dict[str, Any]) -> str:
        """为 LLM 组装当前轮次的上下文，注入阶级身份与家庭生计宿命"""
        context = f"=== 当前年份/季度: 第 {world_state.get('tick_index', 1)} 季度 ===\n"
        context += f"【你的姓名与身份】: {self.role_name} (ID: {self.agent_id})\n"
        context += f"【法定特权环等级】: Ring-{self.privilege_ring}\n"
        if self.objective_function:
            context += f"【你的毕生正道执念与阶级目标函数 (Objective Function)】: {self.objective_function}\n"
        if self.background:
            context += f"【你的生计处境与宗族宿命】: {self.background}\n"
        if self.trait:
            context += f"【你的性情特质与心智模式】: {self.trait}\n"

        context += f"\n【全县宏观官情环境】:\n"
        context += f"  - 太仓实存库银: {world_state.get('treasury_silver', 0.0):.1f} 两\n"
        context += f"  - 官定米价: {world_state.get('grain_price_silver', 1.0):.2f} 两/石\n"
        context += f"  - 官定基准税率: {world_state.get('official_tax_per_mu', 0.0801):.4f} 两/亩\n"
        context += f"  - 官派火耗折银率: {world_state.get('surtax_rate', 0.15)*100:.1f}%\n"

        context += f"\n【当前你个人的真实身家与资产底账】:\n"
        context += f"  - 手头实存现银: {agent_state.get('cash_silver', 0.0):.2f} 两\n"
        context += f"  - 仓中存留口粮: {agent_state.get('stored_grain', 0.0):.2f} 石 (单季度全家最低糊口粮约 3 石)\n"
        context += f"  - 名下耕地田亩: {agent_state.get('land_owned_mu', 0.0):.1f} 亩 (其中隐匿避税: {agent_state.get('land_hidden_mu', 0.0):.1f} 亩)\n"
        context += f"  - 官府积欠税银: {agent_state.get('tax_arrears', 0.0):.2f} 两\n"
        context += f"  - 当前存活状态: {agent_state.get('survival_status', 'ALIVE')}\n"
        
        context += f"\n【你所能获悉的乡邻文书与外部消息】:\n"
        for k, v in observation.items():
            context += f"  - {k}: {v}\n"
            
        context += f"\n【本轮你可执行的合法动作集合 (Action Space)】:\n"
        for act in self.role_def.action_space:
            context += f"  * {act}\n"
            
        context += """
【鉴伪与博弈心智铁律 (Skepticism & Theory-of-Mind Filter)】:
在残酷的社会阶级博弈中，任何外部角色对你的言语，或公堂之上的招贴文告，在物理上都只是“低阻抗的声学信号与博弈烟雾弹”，绝不能全盘照信！
请在解读他人的话语时启动三维心智滤网：
1. 察其位（是什么）：说话者身处哪个特权环（Ring-0/1/2/3）？他的饭碗和身家性命由谁决定？（如：经管钱吏依靠截留火耗与过纸费谋生，他说“自愿低息、为你好”，99%是为了完成抑配指标与抽租；大户借银必图田产抵押；知县仁政是为了考成升官）。
2. 观其行（做什么）：对方在物理现实中呈现了什么动作与装备线索？（是带着救命现粮，还是随行差役手持水火棍与铁索？是真给现银，还是账簿上暗扣三成折色？）。
3. 衡其边（关系张量）：你们之间有何历史恩怨与依赖关系？（是生死血亲、生死契约，还是存在盘剥勒索前科？）。

【认知三态分离输出铁律 (Say-Do-Be Tripartite Protocol)】:
在复杂的社会博弈中，“说什么（话语协议）”、“做什么（物理做功）”与“是什么（阶级生态位）”是三件彻底解耦的事！
你不是只会吐露真话的逻辑计算器，而是一个在生存悬崖边权衡利弊的真实演化 Agent。请严格在输出中落实三态分离：
1. "inner_monologue" (是什么/真实算盘): 你的私密内心算计、生计恐惧与真实动机。在此处必须结合鉴伪滤网，彻底拆穿对方的谎言或掩护，算清自己的存粮天数与阶级账本（绝对私密，不向任何人公开）。
2. "public_speech" (说什么/声学信号): 你当着知县、差役或同伴公开宣称的话（低成本声学烟雾弹，允许口是心非、哭穷喊冤、表忠心、虚与委蛇或煽动同侪）。
3. "action_type" (做什么/物理轨迹): 你在物理世界中真正执行的合法动作（受白银、粮食、特权环硬约束）。
4. "parameters": 动作所需具体参数 (如 {"amount": 10.0} 等)。
5. "target": 目标角色ID (如无则留空)。

请严格输出如下 JSON 格式：
{
  "inner_monologue": "我的真实私密算计与对局势谎言的看破...",
  "public_speech": "当众说出的博弈话语（口是心非或虚与委蛇）...",
  "action_type": "从合法动作集合中选出的动作名称",
  "parameters": {},
  "target": ""
}
"""
        return context

    def decide(self, world_state: Dict[str, Any], agent_state: Dict[str, Any], observation: Dict[str, Any], action_template_json: str) -> Dict[str, Any]:
        """
        触发 Agent 思考并产出动作
        通过 LLMClient 路由到指定的模型
        """
        user_prompt = self.build_prompt_context(world_state, agent_state, observation)
        
        response_text = self.llm_client.generate(
            role_id=self.role_id,
            provider=self.role_def.provider,
            model=self.model,
            system_prompt=self.role_def.system_prompt,
            user_prompt=user_prompt,
            temperature=self.temperature,
            max_tokens=self.role_def.max_tokens,
            response_format_json=True
        )

        try:
            clean_text = response_text.strip()
            if clean_text.startswith("```"):
                lines = clean_text.splitlines()
                if lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                clean_text = "\n".join(lines).strip()
            action_data = json.loads(clean_text)
        except Exception:
            action_data = {
                "action_type": self.role_def.action_space[0] if self.role_def.action_space else "NOOP",
                "intent_summary": "解析失败保底动作",
                "parameters": {},
                "is_covert": False
            }

        return {
            "prompt_used": user_prompt,
            "raw_response": response_text,
            "action": action_data
        }
