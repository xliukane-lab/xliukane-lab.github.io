LAB_ZH = "智能系统设计与优化实验室"
LAB_EN = "Intelligent System Design and Optimization Lab"
FACULTY = "https://me.bit.edu.cn/szdw/jsml/zzgcx/gygcyjs/gygcyjsqnjs/127ba53935674ff2b9f8f99c90305632.htm"
SCHOLAR = "https://scholar.google.com/citations?hl=en&user=9hSdRHQAAAAJ&view_op=list_works&sortby=pubdate"
EMAIL = "xliu826@bit.edu.cn"

# Each language pair contains Chinese followed by English.
BIO = (
    "研究方向为工业智能，关注数据科学与智能优化算法在生产制造、物流、可再生能源和产品设计中的交叉融合，通过数据挖掘理论开展装备/系统运行环境的不确定性分析预测，并创新智能优化技术提升装备控制及系统调度效能。",
    "My research focuses on industrial intelligence, bringing data science and intelligent optimisation into manufacturing, logistics, renewable energy and product design. I use data mining to analyse and forecast uncertainty in the operating environments of equipment and systems, and develop optimisation methods to improve equipment control and system scheduling."
)
EDUCATION = [
    ("2012-2016", ("北京理工大学","Beijing Institute of Technology"), ("工业工程","Industrial Engineering"), ("本科","Bachelor’s degree")),
    ("2015-2016", ("德国卡尔斯鲁厄理工学院","Karlsruhe Institute of Technology, Germany"), ("机械工程","Mechanical Engineering"), ("访学","Visiting student")),
    ("2017-2021", ("香港城市大学","City University of Hong Kong"), ("数据科学","Data Science"), ("直博","Direct-entry PhD"))
]
APPOINTMENTS = [
    ("2016-2017", ("电子六所","Sixth Research Institute (CEC)"), ("工程师","Engineer"), ("","")),
    ("2021", ("香港城市大学","City University of Hong Kong"), ("数据科学学院 · 科研助理","School of Data Science · Research Assistant"), ("","")),
    ("2021-至今", ("北京理工大学","Beijing Institute of Technology"), ("机械与车辆学院 · 预聘助理教授","School of Mechanical Engineering · Tenure-track Assistant Professor"), ("",""))
]
COURSES = [
    (("《智能制造系统》", "Intelligent Manufacturing Systems"), ("工业工程", "Industrial Engineering"), ("专业选修课", "Programme elective")),
    (("《制造系统感知分析与决策》", "Sensing, Analysis and Decision-Making for Manufacturing Systems"), ("智能制造工程", "Intelligent Manufacturing Engineering"), ("专业核心课", "Core course")),
    (("《工程管理》", "Engineering Management"), ("研究生", "Graduate studies"), ("公共课", "University-wide course")),
    (("《复杂装备健康管理与运维》", "Health Management, Operations and Maintenance of Complex Equipment"), ("工业工程", "Industrial Engineering"), ("专业限选课", "Restricted elective"))
]

TRACKS = [
    dict(
        id="manufacturing",
        name=("智能制造与物流", "Intelligent Manufacturing and Logistics"),
        intro=("在以大规模定制为主题下的新一代智能制造模式中，系统存在多种复杂的内外扰动。我们研究怎样把现场数据转化为决策依据，开展布局设计、生产调度、设备健康管理、工艺优化等相关垂域模型研发及验证，综合实现TQCSE全面提升。",
               "Intelligent manufacturing for mass customisation faces complex internal and external disturbances. We turn operational data into a basis for decisions, developing and validating domain models for layout design, production scheduling, equipment health management and process optimisation to improve TQCSE performance."),
        keywords=("生产系统设计、垂域模型评价、设备健康管理、工艺优化设计、代理模型预测、生产调度",
                  "Production system design; domain model evaluation; equipment health management; process design optimisation; surrogate prediction; production scheduling"),
        project=("科技部重大专项课题", "Major project of the Ministry of Science and Technology"),
        works=["agv", "fault"],
        figure="agv",
        fig=("堆场无人导引车调度场景", "AGV scheduling in a container terminal yard")
    ),
    dict(
        id="energy",
        name=("可再生能源", "Renewable Energy"),
        intro=("以双碳战略为导向，着力于解决风电系统的设计、分析预测与运行控制，通过时序预测揭示可再生能源系统短期运行模式，结合优化理论提升可再生能源系统运行效能。",
               "Guided by carbon peaking and carbon neutrality goals, our research addresses the design, analysis, forecasting and operational control of wind energy systems. Time-series forecasting reveals short-term operating patterns, while optimisation methods improve system performance."),
        keywords=("时间序列预测、风速预测、风电预测、时空超分辨率、场景生成、微观布局优化、预测性控制",
                  "Time-series forecasting; wind speed forecasting; wind power forecasting; spatiotemporal super-resolution; scenario generation; micro-siting optimisation; predictive control"),
        project=("国家自然科学基金青年基金", "NSFC Young Scientists Fund"),
        works=["wind", "impute"],
        figure="wind",
        fig=("GAPGAN 风速场景生成框架", "GAPGAN framework for wind speed scenario generation")
    ),
    dict(
        id="design",
        name=("智能设计", "Intelligent Design"),
        intro=("工程需求常以不完整的文本描述开始。我们研究怎样从模糊的输入中挖掘用户的产品需求，让模型在工程知识约束下生成候选概念，再通过人-大语言模型-知识库多元协同的模式实现概念方案设计生成，在产品生命周期的起点保证产品质量。",
               "Engineering requirements often begin as incomplete text. We extract product needs from ambiguous input and generate candidate concepts grounded in engineering knowledge. Collaboration among people, large language models and knowledge bases then guides concept generation to support product quality from the beginning of the lifecycle."),
        keywords=("需求分析、概念设计、知识图谱、生成式设计、自然语言处理",
                  "Requirements analysis; conceptual design; knowledge graphs; generative design; natural language processing"),
        project=("国家自然科学基金面上基金", "NSFC General Program"),
        works=["design", "color"],
        figure="design",
        fig=("KnowLoop 人机协同概念设计框架", "KnowLoop framework for human-AI collaborative concept design")
    )
]

WORKS = {
    "agv": (
        ("堆场 AGV 实时调度", "Real-time AGV scheduling"),
        ("物流堆场里的一次派车会同时改变车辆位置和后续任务的等待时间。为保证调度实时性，我们将派车表述为马尔可夫决策过程，以多智能体深度强化学习共同考虑总完工时间和车辆能耗。在不同规模堆场的仿真实验中，比较了所提策略与基准方法的运行效率和用能表现，验证了方法有效性。",
         "A dispatch in a logistics yard changes both vehicle positions and waiting times for subsequent jobs. To support real-time scheduling, we formulate dispatch as a Markov decision process and use multi-agent deep reinforcement learning to consider makespan and vehicle energy consumption jointly. Simulations across different yard sizes compare operational and energy performance against benchmark methods, demonstrating the effectiveness of the proposed strategy.")
    ),
    "fault": (
        ("跨工况多模态故障诊断", "Multimodal fault diagnosis across operating conditions"),
        ("转速与负载改变时，振动信号也会变，而新工况的故障样本往往很少。MXProto 融合不同模态共有及特有的特征，再动态调整各原型分类器的权重。论文用公开数据集和消融实验检验两级融合对跨工况诊断的贡献。",
         "Changes in speed and load alter vibration signals, yet faults recorded under new conditions can be scarce. MXProto fuses shared and modality-specific features, then adjusts the weights of prototype classifiers. Benchmark experiments and ablation studies examine how both fusion stages contribute to cross-condition diagnosis.")
    ),
    "wind": (
        ("GAPGAN 风速场景生成", "GAPGAN wind speed scenario generation"),
        ("单条预测曲线难以表达一股风电机组捕风情况的不确定性程度。提出 GAPGAN 方法，将多机组历史观测转成图，再从同一段历史生成不同风速场景，实现“平行时空”式预测。论文在验证方法精度的同时，检验了轨迹形态和情景多样性。",
         "A single forecast curve cannot express the uncertainty in wind conditions experienced by turbines. GAPGAN converts historical observations from multiple turbines into a graph, then generates different wind speed scenarios from the same history, producing forecasts of alternative possible futures. Evaluation examines trajectory shape and scenario diversity alongside forecasting accuracy.")
    ),
    "impute": (
        ("风机缺失数据的时空融合修复", "Spatiotemporal fusion for missing turbine data"),
        ("风机监控系统既会丢失零星读数，也会出现连续的数据空段。STF-GAIN 分别估计不同数据表示下的缺失值，再根据置信度融合结果。论文比较了随机缺失与成块缺失下的修复精度，并进一步检查修复数据对下游预测的影响。",
         "Turbine monitoring systems lose individual readings as well as continuous blocks of data. STF-GAIN estimates missing values from different representations and combines the estimates according to confidence. The study compares both missingness patterns and examines the effects on downstream prediction.")
    ),
    "design": (
        ("KnowLoop 人机协同概念设计", "KnowLoop human-AI collaborative concept design"),
        ("为结合大语言模型的生成能力，人的决策能力及知识库的可靠性，提出 KnowLoop 设计框架：先用功能、行为和结构之间的关系整理需求，再以领域知识图谱约束大语言模型，并由专家参与修订。在三项水处理装备设计任务中，取得最高设计方案评分。",
         "KnowLoop combines the generative capabilities of large language models, human decision-making and the reliability of knowledge bases. It first structures requirements through relationships among function, behaviour and structure, then grounds language-model generation in a domain knowledge graph with expert revision. The framework achieves the highest design scores in three water-treatment equipment design tasks.")
    ),
    "color": (
        ("知识与数据驱动的界面配色设计", "Knowledge- and data-driven interface colour design"),
        ("同一主题可以有多种配色，但颜色之间仍需协调。CS-Ganerator 从图像中提取配色样本，并把色彩知识引入条件生成模型。生成后用和谐度筛选，再按冷暖与明暗整理结果，便于设计师在同一主题下比较方案。",
         "A design theme can support many palettes, but the colours still need to work together. CS-Ganerator extracts palettes from images and integrates colour knowledge into a conditional generative model. Candidates are filtered for harmony and grouped by warmth and darkness for comparison.")
    )
}
