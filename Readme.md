# AI工业流体仿真模型——东方·御风

## 概述

**“东方·御风”** 是基于昇腾AI打造的面向大型客机翼型流场高效高精度AI预测仿真模型， 并在昇思MindSpore流体仿真套件的支持下，有效提高了对复杂流动的仿真能力，仿真时间缩短至原来的二十四分之一，减小风洞实验的次数。同时，“东方·御风”对流场中变化剧烈的区域可进行精准预测，流场平均误差降低至万分之一量级，达到工业级标准。

![img-8.png](images/img_8.png)

本教程将对“东方·御风”的研究背景和技术路径进行介绍，并展示如何通过MindFlow实现该模型的训练和快速推理，以及流场可视化分析，从而快速获取流场物理信息。

## 背景介绍

民用飞机气动设计水平直接决定飞机的“四性”，即安全性，舒适性，经济性，环保性。飞机的气动设计作为飞机设计中最基础，最核心的技术之一，在飞机飞行包线（起飞-爬升-巡航-下降-降落等）的不同阶段有着不同的研究需求和重点。如起飞阶段工程师将更关注外部噪声和高升阻比，而巡航阶段则关注油耗效率和能耗效率。流体仿真技术在飞机的气动设计的应用广泛，其主要目的在于通过数值计算的方法 获取仿真目标的流场特性（速度、压力等），进而分析飞机的气动性能参数，实现飞行器的气动性能的优化设计。

![img-7.png](images/img_7.png)

目前，飞行器的气动仿真通常采用商业仿真软件对流体的控制方程进行求解，得到相应的气动性能参数（升阻力，压力，速度等）。无论基于何种CFD的仿真软件，都包含以下几个步骤：

1. 物理建模：将物理问题抽象简化，对相关几何体的2D/3D的流体和固体计算域进行建模。
2. 网格划分：将计算域划分为相应大小的面/体积单元，以便解析不同区域不同尺度的湍流。
3. 数值离散：将流体控制方程中的积分，微分项，偏导项通过不同阶的数值格式离散为代数形式，组成相应的代数方程组。
4. 流体控制方程求解：利用数值方法（常见的如`SIMPLE`算法，, `PISO` 算法等）对离散后的控制方程组进行迭代求解，计算离散的时间/空间点上的数值解。
5. 流场后处理：求解完成后，使用流场后处理软件对仿真结果进行定性和定量的分析和可视化绘图，验证结果的准确性。

![img.png](images/img.png)

然而，随着飞机设计研制周期的不断缩短，现有的气动设计方法存在诸多局限。为使大型客机的气动设计水平赶超波音和空客两大航空巨头，必须发展先进的气动设计手段，结合人工智能等先进技术，建立适合型号设计的快速气动设计工具，进而提高其对复杂流动的仿真能力，减少风洞试验的次数，降低设计研发成本。

![img-11.png](images/img_11.png)

在飞行器的设计中，机翼的阻力分布约占整体飞行阻力的52%，因此，机翼形状设计对飞机整体的飞行性能而言至关重要。然而，三维翼型高精度CFD仿真需划分成百上千万量级的计算网格，计算资源消耗大，计算周期长。为了提高仿真设计效率，通常会先针对三维翼型的二维剖面进行设计优化，而这个过程往往需要对成千上万副的翼型及其对应工况进行CFD的重复迭代计算。其中，超临界翼型在高速巡航阶段的有着重要的应用。因为相较于普通翼型，超临界翼型的头部比较丰满，降低了前缘的负压峰值，使气流较晚到达声速，即提高了临界马赫数；同时，超临界翼型上表面中部比较平坦，有效控制了上翼面气流的进一步加速，降低了激波的强度和影响范围，并且推迟了上表面的激波诱导边界层分离。因此，超临界翼型有着更高的临界马赫数，可大幅改善在跨音速范围内的气动性能，降低阻力并提高姿态可控性，是机翼形状中必须考虑的设计。

![img-10.png](images/img_10.png)

然而，二维超临界翼型的气动设计需要针对不同的形状参数和来流参数进行仿真，依然存在大量的重复迭代计算工作，设计周期长。因此，利用AI天然并行推理能力，缩短设计研发周期显得尤为重要。基于此，商飞和华为联合发布了业界首个AI工业流体仿真模型-- **“东方·御风”** ，该模型能在超临界翼型的几何形状、来流参数（攻角/马赫数）发生变化时，实现大型客机翼型流场的高效高精度推理，快速精准预测翼型周围的流场及升阻力。

## 技术难点

为了实现超临界翼型的的AI高效高精度流场预测，需要克服如下的技术难点：

* **翼型网格疏密不均，流动特征提取困难。** 二维翼型计算域的流体仿真网格常采用O型或C型网格。如图所示，为典型的O型网格剖分。为了精准地计算流动边界层，对翼型近壁面进行了网格加密，而来流远场的网格则相对稀疏。这种非标的网格数据结构增加了提取流动特征的困难程度。

![img-12.png](images/img_12.png) ![img-13.png](images/img_13.png)

* **不同气动参数或翼型形状发生改变时，流动特征变化明显。** 如图所示，当翼型的攻角发生变化时，流场会发生剧烈的变化，尤其当攻角增大到一定程度时，会产生激波现象：即流场中存在明显的间断现象，流体在波阵面上的压力、速度和密度形成明显的突跃变化。

![img-13.png](images/diff_aoa.png)

* **激波区域流场变化剧烈，预测困难。** 由于激波的存在对其附近的流场影响显著，激波前后的流场变化剧烈，流场变化复杂，导致AI预测困难。激波的位置直接影响着翼型的气动性能设计和载荷分布。因此，对激波信号的精准捕捉是十分重要但充满挑战的。

## 技术路径

针对如上所述的技术难点，我们设计了基于AI模型的技术路径图，构建不同流动状态下翼型几何及其对应流场的端到端映射， 主要包含以下几个核心步骤：

* 首先，设计AI数据高效转换工具，实现翼型流场复杂边界和非标数据的特征提取，如图数据预处理模块。先通过曲线坐标系网格转换程序实现规则化AI张量数据生成，再利用几何编码方式加强复杂几何边界特征的提取。

* 其次，利用神经网络模型，实现不同流动状态下翼型构型和流场物理量的映射，如图ViT-based encoder-decoder所示；模型的输入为坐标转换后所生成的翼型几何信息和气动参数；模型的输出为转换后生成的流场物理量信息，如速度和压力。

* 最后，利用多级小波变换损失函数训练网络的权重。对流场中突变高频信号进行进一步地分解学习，进而提升流场剧烈变化区域（如激波）的预测精度，如图loss function对应的模块；

![img-1.png](images/img_1.png)

翼型几何形状发生改变时，AI和CFD预测的表面压力分布，流场分布及其误差统计如下：

![airfoil.gif](images/airfoil.gif)

来流攻角发生改变时，AI和CFD预测的表面压力分布，流场分布及其误差统计如下：

![aoa_var.gif](images/aoa_var.gif)

来流马赫数发生改变时，AI和CFD预测的表面压力分布，流场分布及其误差统计如下：

![Ma_var.gif](images/Ma_var.gif)