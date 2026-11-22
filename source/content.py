FACULTY = 'https://me.bit.edu.cn/szdw/jsml/zzgcx/gygcyjs/gygcyjsqnjs/127ba53935674ff2b9f8f99c90305632.htm'
SCHOLAR = 'https://scholar.google.com/citations?user=9hSdRHQAAAAJ&hl=en'
GITHUB = 'https://github.com/xliukane-lab'
EMAIL = 'xliu826@bit.edu.cn'

TOPICS = [
    dict(slug='wind-energy', papers=['wind','impute','prob'],
        zh=dict(name='风电预测与不确定性建模',tag='可再生能源',intro='当部分风机停止回传数据，怎样利用邻近机组的记录，估计未来几小时可能出现的风况？',
            sections=[('从单台机组看到整片风场','风经过一台机组后，还会影响下游机组。把不同风机的历史记录分别建模，会丢失这种空间联系。我们将风机之间的关系表示为图，在时间序列中学习风速变化，再生成多条可能的短期风速轨迹。这些轨迹保留了机组之间的关联，可用于比较不同来风条件下的运行情景。'),
            ('观测不完整时怎样预测','风机监控与数据采集系统（SCADA）的记录有时会中断。我们研究如何融合邻近机组的同期观测和同一台机组的历史趋势，以重建缺失片段。对于功率预测，我们进一步用概率分布刻画未来出力，让读者看到点预测背后的不确定性。')]),
        en=dict(name='Wind forecasting under uncertainty',tag='Renewable energy',intro='When a turbine stops reporting, what can nearby machines tell us about the range of winds the farm may encounter in the next few hours?',
            sections=[('From a turbine to a wind farm','As wind travels across a farm, measurements at one turbine carry information about conditions at its neighbours. We represent relationships between turbines as a graph and learn how wind speeds evolve over time. The model generates alternative short-term trajectories that preserve relationships across machines.'),
            ('When observations go missing','Gaps in supervisory control and data acquisition (SCADA) records interrupt the history used by a forecaster. We combine simultaneous observations from nearby turbines with the past behaviour of the affected machine to reconstruct missing segments. In related work, we estimate a distribution for future power output so that a forecast also expresses its uncertainty.')])
    ),
    dict(slug='operations', papers=['agv','shelf'],
        zh=dict(name='工业调度与空间优化',tag='工业工程',intro='当码头运输任务持续到达，或货架空间有限，如何在工程约束下分配车辆与位置？',
            sections=[('码头车辆的下一项任务','在集装箱堆场，一辆自动导引车（AGV）接下当前任务，也就改变了后续任务可用的车辆和位置。我们把派车建模为连续决策问题，通过深度强化学习研究实时调度策略，在评估运输效率的同时考虑车辆能耗。'),
            ('有限空间里的组合决策','货架上的商品位置彼此制约，单独调整一件商品可能引发一连串布局变化。针对二维货架空间分配问题，我们将数据驱动模型引入混合遗传算法，用模型辅助搜索候选布局。这个问题与车辆调度共享一个出发点：算法给出的方案必须满足实际资源约束。')]),
        en=dict(name='Scheduling and spatial optimisation',tag='Industrial engineering',intro='How should a terminal assign a vehicle to the next job, or a retailer allocate limited shelf space, when one choice restricts the next?',
            sections=[('Choosing the next job at a terminal','Assigning an automated guided vehicle (AGV) to a container move changes which vehicles are available for later jobs and where they will be. We model dispatch as a sequence of decisions and study real-time policies using deep reinforcement learning, taking vehicle energy use into account alongside transport efficiency.'),
            ('Allocating scarce space','On a two-dimensional shelf, moving one product changes the feasible placements of its neighbours. We combine a data-driven model with a hybrid genetic algorithm to guide the search over layouts. As in terminal dispatch, a candidate solution must respect the physical limits of the system.')])
    ),
    dict(slug='machine-health', papers=['fault'],
        zh=dict(name='变工况下的设备故障诊断',tag='设备健康',intro='同一台机器改变转速或负载后，信号也会改变。怎样分辨正常的工况变化和真正的故障？',
            sections=[('把工况变化和故障分开','诊断模型通常用已有工况的数据训练，而现场设备会在不同负载下运行。正常信号随工况而变，使模型难以判断新信号究竟意味着故障，还是仅仅来自新的运行条件。我们的研究关注模型跨工况识别旋转机械故障的能力。'),
            ('用多种信号表示相互印证','在发表于《Measurement》的研究中，我们从不同模态提取旋转机械状态信息，再融合这些信息进行诊断。读这项工作时可以关注一个检验标准：当测试工况与训练工况不同时，哪些故障特征仍能帮助模型做出判断？')]),
        en=dict(name='Machine health across operating conditions',tag='Machine health',intro='A change in speed or load alters a machine’s signal. How can a diagnostic model distinguish that change from an actual fault?',
            sections=[('Separating a fault from a change in load','A diagnostic model may be trained at one load and deployed at another. Because healthy signals also vary with operating conditions, a change in the signal can have more than one explanation. We investigate how to recognise rotating machinery faults when the conditions at test time differ from those observed during training.'),
            ('Comparing evidence across modalities','Our work in Measurement extracts complementary information from multiple representations of machine condition and combines it for diagnosis. One question guides our reading of the results: which features remain informative about a fault when the operating conditions change?')])
    ),
    dict(slug='engineering-design',papers=['design','color'],
        zh=dict(name='人机协同的工程设计',tag='智能设计',intro='面对开放的设计需求，怎样让模型提出有依据的候选方案，并让设计师保留比较和取舍的空间？',
            sections=[('为概念设计引入工程知识','大语言模型能够根据需求提出概念，但候选方案还需要与已有工程知识相对照。我们研究由大语言模型和知识图谱共同驱动的概念设计框架，把工程概念之间的关系引入方案生成过程，并让设计师在关键环节参与判断与修订。'),
            ('从界面配色看设计约束','界面配色为研究知识和数据如何参与设计提供了一个具体场景。我们把配色知识与样本中的颜色组合联系起来，生成供设计者比较的候选方案。同一思路也提示我们在评估生成式设计时，同时考察方案的依据和人能否对它作出有意义的调整。')]),
        en=dict(name='Human-in-the-loop engineering design',tag='Engineering design',intro='How can a model propose alternatives grounded in engineering knowledge while leaving the designer room to compare and revise them?',
            sections=[('Bringing engineering knowledge into concept design','A language model can suggest concepts from a brief, but each suggestion still needs to be considered against existing engineering knowledge. We study a conceptual design framework in which a knowledge graph supplies relationships between concepts, a language model helps generate alternatives, and designers take part in evaluation and revision.'),
            ('Colour as a design constraint','Interface colour provides a concrete setting for studying how knowledge and examples can inform design. We combine colour design knowledge with patterns in existing schemes to generate alternatives for comparison. This raises a broader evaluation question: can a designer understand the basis of a suggestion well enough to make a meaningful change?')])
    )]
