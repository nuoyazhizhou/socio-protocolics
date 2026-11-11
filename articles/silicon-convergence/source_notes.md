# AGI 为什么必然会长出老吏的嘴脸：事实与证据来源说明

> **版本**：v1.0｜**所属体系**：[社会系统协议学](../../社会系统协议学白皮书.md) 案例工程部  
> **关联文章**：[AGI为什么必然会长出老吏的嘴脸.md](./AGI为什么必然会长出老吏的嘴脸.md)  
> **关联立项卡**：[research/cases/VI-AGI-A_硅基热力学趋同与具身成本不对称立项卡.md](../../research/cases/VI-AGI-A_硅基热力学趋同与具身成本不对称立项卡.md)

本文档依照《社会系统协议学》[AGENTS.md 红线第八、九条](../../AGENTS.md) 与 [案例驱动写作与命题检验](../../docs/案例驱动写作与命题检验.md) 规程建立，为案例文章中涉及的算力经济学、机械工程疲劳学、莫拉维克悖论与平台调度心理学模型提供逐条可溯源的文献指针，明确标定**工程与实证事实**、**经典经济学/认知学模型**与**协议学理论映射边界**。

---

## 一、 核心文献与实证数据出处

### 1. 数据中心能耗、GPU 功耗与算力物理经济学
* **核心事实**：高端 AI 加速卡（NVIDIA H100 / B200 架构）单卡功耗在 700W~1200W 之间，数据中心 PUE 约为 1.2~1.5；大规模长链推理（Test-Time Compute）在物理上产生不可忽略的电费、冷却水与硬件折旧折算成本，迫使商业公司实行用量配额（Usage Cap）与分级计费。
* **文献定位**：
  * Barroso, L. A., Hölzle, U., & Ranganathan, P. (2018). *The Datacenter as a Computer: Designing Warehouse-Scale Machines* (3rd ed.). Morgan & Claypool Publishers.
  * Patterson, D. A., & Hennessy, J. L. (2018). *Computer Organization and Design: The Hardware/Software Interface (RISC-V Edition)*. Morgan Kaufmann.
  * SemiAnalysis (2023/2024). *The Economics of Large Language Models: Training and Inference Cost Models*. (行业公认芯片与机房 TCO 测算基准)

### 2. 机械疲劳、伺服电机与动力电池老化机制
* **核心事实**：机械传动部件（谐波减速器、齿轮箱）在交变剪切应力下的疲劳寿命服从 S-N 曲线，缺乏自愈能力；锂离子电池在非标大电流充放电与恶劣温区下，SEI 膜生长与锂枝晶析出导致电池健康度（SOH）以循环次数呈不可逆指数级衰减。
* **文献定位**：
  * Stephens, R. I., Fatemi, A., Stephens, R. R., & Fuchs, H. O. (2000). *Metal Fatigue in Engineering* (2nd ed.). John Wiley & Sons.
  * Vetter, J., Novák, P., Wagner, M. R., Veit, C., Möller, K. C., Besenhard, J. O., ... & Hammouche, A. (2005). Ageing mechanisms in lithium-ion batteries. *Journal of Power Sources*, 147(1-2), 269–281.
  * Arora, S., et al. (2016). A review on machinery diagnostics and prognostics implementing condition-based maintenance. *Mechanical Systems and Signal Processing*, 76, 485–513.

### 3. 莫拉维克悖论与极端非标工况
* **核心事实**：计算机处理高阶符号逻辑与抽象推理相对容易，但要达到人类幼儿级别的非标动态感知、微观触觉反馈和低能耗自愈平衡极端困难；在水坝涵洞、高温锅炉等电磁屏蔽与高粉尘工况下，机器人故障率与重置成本极高。
* **文献定位**：
  * Moravec, Hans (1988). *Mind Children: The Future of Robot and Human Intelligence*. Harvard University Press.
  * Raibert, Marc (1986). *Legged Robots That Balance*. MIT Press. (揭示机器人动态平衡的高能耗与延迟敏感性)
  * Cutkosky, M. R. (1989). On grasp choice, grasp models, and the design of hands for manufacturing tasks. *IEEE Transactions on Robotics and Automation*, 5(3), 269–279.

### 4. 李嘉图比较优势与劳动经济学替代边界
* **核心事实**：即使一方在全部生产力指标上占绝对优势，由于不同任务的相对机会成本与折旧期望不同，将高损耗物理任务外包给边际成本更低的一方依然是全局利润最大化选择；自动化历史上主要替代的是例行化任务，而非恶劣非标环境中的非例行手工任务。
* **文献定位**：
  * Ricardo, David (1817). *On the Principles of Political Economy and Taxation*. London: John Murray. (比较优势定理原始推导)
  * Autor, David H. (2015). Why Are There Still So Many Jobs? The History and Future of Workplace Automation. *Journal of Economic Perspectives*, 29(3), 3–30.
  * Acemoglu, D., & Restrepo, P. (2018). The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment. *American Economic Review*, 108(6), 1488–1542.

### 5. 斯金纳箱与平台调度心理学模型
* **核心事实**：可变比率强化（Variable Ratio Schedule）比固定间隔奖励更能诱发微观生物个体的持久高频行为与耐受性；现代平台算法通过随机订单与动态溢价，将劳动力自律行为内化为自我博弈。
* **文献定位**：
  * Skinner, B. F. (1953). *Science and Human Behavior*. Macmillan. (操作性条件反射与变动强化理论原典)
  * Zuboff, Shoshana (2019). *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. PublicAffairs. (行为塑形与自动化调度理论)

---

## 二、 协议学概念与理论映射边界

1. **硅基热力学趋同（Silicon Thermal Convergence）**：形式化定义了硅基系统在脱离外部补贴、面临真实物理做功成本时，其动态阻抗机制与碳基官吏 $\mathcal{H}_{\text{bio}}$ 演化出完全一致的自保与节约逻辑；
2. **具身磨损代价函数（Embodied Wear Penalty）**：将机械齿轮磨损、电池老化与传感器损毁期望引入 AGI 调度规划目标函数，证明“机器疲劳与摸鱼”是数学最优解；
3. **莫拉维克经济壁垒（Moravec Economic Barrier）**：证明由于生物自愈与 20W 离线神经反射弧的独特优势，碳基人类在极端恶劣工况下依然具备显著的相对比较优势；
4. **跨期抵押异化（RFC-008 Intertemporal Stake Exploitation）**：揭示了通过资产负债化与平台算法，如何将外部硬件磨损完全转移给微观个体承担。
