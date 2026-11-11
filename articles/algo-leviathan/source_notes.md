# 算法利维坦的单机幻觉与零摩擦深渊：事实与证据来源说明

> **版本**：v1.0｜**所属体系**：[社会系统协议学](../../社会系统协议学白皮书.md) 案例工程部  
> **关联文章**：[算法利维坦的单机幻觉与零摩擦深渊.md](./算法利维坦的单机幻觉与零摩擦深渊.md)  
> **关联立项卡**：[research/cases/II-SYS-A_算法单机沙盒与零摩擦脆断立项卡.md](../../research/cases/II-SYS-A_算法单机沙盒与零摩擦脆断立项卡.md)

本文档依照《社会系统协议学》[AGENTS.md 红线第八、九条](../../AGENTS.md) 与 [案例驱动写作与命题检验](../../docs/案例驱动写作与命题检验.md) 规程建立，为案例文章中的历史引证、工业实测数据与控制论模型提供逐条可核验的来源指针，清晰标定**实证文献事实**、**工程事故记录**与**协议学理论映射边界**。

---

## 一、 核心文献与历史史料出处

### 1. 欧文新和谐公社（New Harmony）与公地悲剧
* **核心事实**：罗伯特·欧文于 1825 年购买印第安纳州哈莫尼镇成立公社，废除货币与私有制；在欧文亲自巡查期间运转良好，但在其离开并扩大陌生人加入后，因劳动搭便车与分配不均在 24 个月内（1827–1828）瓦解并诉诸私有化清算。
* **文献定位**：
  * Owen, Robert (1826). *The New Harmony Gazette*, Vol. 1 & 2. (公社原始档案与规章文献)
  * Podmore, Frank (1906). *Robert Owen: A Biography*. London: Hutchinson & Co., Chapter 15: "New Harmony".
  * Harrison, J. F. C. (1969). *Quest for the New Moral World: Robert Owen and the Owenites in Britain and America*. New York: Charles Scribner's Sons.

### 2. 苏联计划委员会（Gosplan）与古德哈特指标失真
* **核心事实**：以单一物理量（总重量、总件数）作为自上而下刚性考核指标时，引发工厂极端恶意合规（重型螺栓、脆弱细针）；1960–70 年代尝试建立全苏经济自动化核算网络（OGAS）因地方部委伪造与隐瞒数据而无法实现闭环排产。
* **文献定位**：
  * Nove, Alec (1986). *The Soviet Economic System* (3rd ed.). Boston: Allen & Unwin. (系统分析苏联计划经济中的“指标寻租”与扭曲激励)
  * Gerovitch, Slava (2008). *InterNyet: Why the Soviet Union Did Not Build a Nation-Wide Computer Network*. *Information & Culture*, 43(4), 335–359.
  * Goodhart, C. A. E. (1975). *Problems of Monetary Management: The U.K. Experience*. Papers in Monetary Economics, Reserve Bank of Australia. (古德哈特定律出处)

### 3. 亚马逊 TOT 算法与现代工业调度
* **核心事实**：算法对仓储工人扫描枪间隔时间（Time Off Task / TOT）进行秒级追踪，累积超标自动触发解雇；实测数据显示其严重工伤率高出同业一倍以上，年离职率高达 150%。
* **文献定位**：
  * Kantor, Jodi, & Weise, Karen (2021-06-15). *The Amazon That Customers Don’t See*. *The New York Times*. (普利策获奖深度调查报道，披露内部 TOT 算法运行机制与人力流失数据)
  * Gutelius, Beth, & Theodore, Nik (2019). *The Future of Warehouse Work: Technological Change in the U.S. Logistics Industry*. UC Berkeley Labor Center.

### 4. 戴克里先《最高价格敕令》与罗马商业终局性崩溃
* **核心事实**：公元 301 年罗马皇帝戴克里先颁布敕令，对 1000 多种商品和劳务制定刚性上限价格，违者处死；结果导致全面罢市、商品转入黑市、农田大量荒芜与劳动力逃亡。
* **文献定位**：
  * Jones, A. H. M. (1964). *The Later Roman Empire, 284–602: A Social, Economic, and Administrative Survey*. Oxford: Blackwell, Chapter 3.
  * Frank, Tenney (1940). *An Economic Survey of Ancient Rome*, Vol. V: *Rome and Italy of the Empire*. Johns Hopkins Press. (包含《最高价格敕令》铭文残片的英译考证与物价对照)

### 5. 控制论、系统动力学与博弈论数学基准
* **文献定位**：
  * Ashby, W. Ross (1956). *An Introduction to Cybernetics*. London: Chapman & Hall. (第 11 章阐述“必要多样性定律”：$V_C \ge V_R$)
  * Scott, James C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. Yale University Press. (详述 Mētis / 地方默会知识与 Techne / 抽象官僚技术之间的张力)
  * Axelrod, Robert (1984). *The Evolution of Cooperation*. New York: Basic Books. (阐明重复博弈中合作涌现与贴现因子 $\beta$ 的关键关系)

---

## 二、 协议学概念与理论映射边界

1. **单机沙盒（Localhost Sandbox）**：映射小规模、高道德算力看门狗在场、无网络时延的局部封闭环境；不可外推至超大规模广域对抗网络；
2. **热节流阻尼（Thermal Throttling Slack）**：将基层节点的生理休息、人情调解与局部裁量权，形式化为防止控制回路发生超频雪崩的物理阻尼；
3. **主权级任意回滚（Arbitrary Rollback / Rug Pull）**：将权力对既往合法合规交易的无偿取缔，形式化为破坏状态机不可逆提交状态（Committed State）的恶意故障；
4. **跨期贴现塌缩（$\beta \to 0$）**：证明当规则不可信赖时，个体的短期自保、游资化与绝育反抗是纯粹由数学期望诱导出的理性纳什均衡，而非无理智的任性。
