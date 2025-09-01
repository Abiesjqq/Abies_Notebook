## 课程介绍

简单的假设：感知和运动是智能的标志

经验性质的 Engeneering，从工程实践中得出

答辩思路：问题，解决方法，发展趋势

参考期刊和会议论文：

- AI
  - NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, AAAI, IJCAI
  - TPAMI, JMLR, IJCV
  - Nature Machine Intelligence
- 机器人领域
  - ICRA, IROS, ACC, CDC
  - TRO, IJRR, Soft Robotics
  - Science Robotics
- 其他
  - SIGGraph, SIG CHI

## 概况

感知受到结构、能量、环境干扰限制，感知和运动控制的循环需要实时完成。

Motivation -> Action (behavior shaping) -> Reward -> Motivation

- 强化学习：从环境中输入，预测环境交互，反馈
- 监督学习：环境输入 + 标签

强化学习 Sim-to-Real：在仿真环境中训练，训练结果导入机器人

视觉语言模型：视觉模型和语言描述在向量空间中的矩阵相同。在统一的特征空间，用自然语言指令控制。

Counterfactuals：反事实推理，和决策的下一步相反的结果，帮助评估决策的反馈

机器人系统分为三大部分：机械部分，传感部分，控制部分  
传感（感知系统） -> 控制 （人机交互，控制） -> 机械（驱动，机械系统） -> 机器人-环境交互系统 -> 传感

（时间是单向的函数。Attention 是智能的一部分。）
