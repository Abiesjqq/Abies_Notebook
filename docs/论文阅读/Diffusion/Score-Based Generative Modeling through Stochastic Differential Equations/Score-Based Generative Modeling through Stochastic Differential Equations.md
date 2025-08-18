
[文章链接 《Score-Based Generative Modeling through Stochastic Differential Equations》](https://arxiv.org/abs/2011.13456)

一种基于 **随机微分方程 (SDE)** 的统一生成建模框架。 

## 引言（Introduction）

**背景**  
- 生成建模中有两大类很成功的基于噪声扰动的概率生成方法：  
  1. **SMLD（Score Matching with Langevin Dynamics）**  
     - 先对数据加入不同强度的噪声  
     - 学习每个噪声尺度下的 score function $\nabla_x \log p_\sigma(x)$  
     - 采样时用 Langevin 动力学逐步去噪  
  2. **DDPM（Denoising Diffusion Probabilistic Model）**  
     - 构造一条噪声逐渐增强的马尔可夫链（前向过程）  
     - 学习逆马尔可夫链（反向过程）的参数  
     - 本质上也在学习每个噪声尺度下的 score function  

两者共同点：  
- 都是 score-based generative models  
- 都是从“多尺度噪声”出发：前向过程加噪，反向过程去噪  

**主要贡献**  
- 提出一个基于随机微分方程（SDE）的统一框架，把 SMLD 和 DDPM 视为离散化的特殊 SDE  
- 正向 SDE：数据 $\to$ 高斯先验  
- 反向 SDE：先验 $\to$ 数据（需已知各时刻的 score）  
- 训练方法：用时间依赖的神经网络估计 score function  
- 新特性：灵活采样器、Predictor–Corrector、Probability Flow ODE、条件生成  
- 实验：在 CIFAR-10 上达到当时最佳无条件生成指标（FID 2.20, IS 9.89）、似然最高记录（2.99 bits/dim）、首次生成 1024×1024 高保真图像  

---

## 背景（Background）

**SMLD（Denoising Score Matching with Langevin Dynamics）**  
- 对数据加噪：$p_\sigma(\tilde{x} | x) = \mathcal{N}(\tilde{x}; x, \sigma^2 I)$  
- 多个噪声尺度：$\sigma_{\min} = \sigma_1 < \dots < \sigma_N = \sigma_{\max}$  
- 训练目标：  

$$
\min_\theta \sum_{i=1}^N \sigma_i^2 \, \mathbb{E}\big[ \| s_\theta(\tilde{x},\sigma_i) - \nabla_{\tilde{x}} \log p_\sigma(\tilde{x} | x) \|^2 \big]
$$

- 采样：从最大噪声 $\sigma_N$ 的高斯开始，依次用 Langevin MCMC 去噪，到 $\sigma_{\min}$ 得到样本  

**DDPM（Denoising Diffusion Probabilistic Models）**  
- 前向马尔可夫链：  
  $q(x_i | x_{i-1}) = \mathcal{N}(\sqrt{1 - \beta_i} x_{i-1}, \beta_i I)$  
- 训练：反向链 $p_\theta(x_{i-1} | x_i)$，ELBO 等价于多尺度 score matching  
- 采样：从高斯噪声 $x_N$ 开始，逐步还原到 $x_0$  

**两者关系**  
- 都是不同噪声尺度下的 score matching  
- 差异在加噪方式：SMLD → variance exploding，DDPM → variance preserving  

---

## 基于 SDE 的 Score-Based 生成建模

**正向 SDE（加噪过程）**  

$$
dx = f(x,t) \, dt + g(t) \, dw
$$

- $f(x,t)$：漂移系数  
- $g(t)$：扩散系数  
- $w$：标准 Wiener 过程  
- 目标：把 $p_0$ 平滑转成易采样的 $p_T$  

**反向 SDE（生成过程）**  

$$
dx = \big[ f(x,t) - g(t)^2 \, \nabla_x \log p_t(x) \big] \, dt + g(t) \, d\bar{w}
$$

- $d\bar{w}$ 是反向时间的 Wiener 过程  
- 需已知 $\nabla_x \log p_t(x)$ 才能生成  

**score 估计**  

$$
\min_\theta \mathbb{E}_{t \sim U(0,T)} \big[ \lambda(t) \, \mathbb{E}_{x_0 \sim p_0, x_t \sim p_{0t}(\cdot|x_0)} \| s_\theta(x_t, t) - \nabla_{x_t} \log p_{0t}(x_t | x_0) \|^2 \big]
$$

- $\lambda(t)$：权重函数  
- 如果 $f$ 是仿射的，条件分布是高斯，训练方便  

**三种 SDE**  
- VE SDE（variance exploding）  
- VP SDE（variance preserving）  
- Sub-VP SDE（VP 改进版）  

SMLD ⇔ VE SDE 离散化  
DDPM ⇔ VP SDE 离散化  

---

## 求解反向 SDE

**通用数值解法**  
- Euler–Maruyama、随机 Runge–Kutta 等  
- Reverse Diffusion Sampler：通用，优于原生采样  

**Predictor–Corrector (PC) 采样器**  
1. Predictor：数值 SDE 更新一步  
2. Corrector：基于 score 的 MCMC（如 Langevin 动力学）修正  
- SMLD 原法：Predictor=恒等，Corrector=Langevin  
- DDPM 原法：Predictor=祖先采样，Corrector=恒等  
- PC 方法比单纯增加预测步效果更好  

**Probability Flow ODE**  

$$
dx = \left[ f(x,t) - \frac{1}{2} g(t)^2 \, \nabla_x \log p_t(x) \right] dt
$$

- 与 SDE 边际分布一致，但确定性  
- 用途：精确似然计算、潜空间操作、自适应采样  

**网络结构改进**  
- NCSN++（VE SDE）、DDPM++（VP/Sub-VP SDE）  
- 更深网络 + 连续目标 → CIFAR-10 FID 2.20, IS 9.89；bits/dim 2.99；首次生成 CelebA-HQ 1024×1024 高保真图像  

---

## 条件与可控生成

在反向 SDE 中替换为条件 score：  

$$
\nabla_x \log p_t(x|y) = \nabla_x \log p_t(x) + \nabla_x \log p_t(y|x)
$$

- $\nabla_x \log p_t(x)$：无条件 score  
- $\nabla_x \log p_t(y|x)$：条件梯度  

**如何加条件**  
- 无需重新训练模型  
- 条件梯度可来自分类器或观测数据似然  

**应用示例**  
- 类别条件生成：用分类器梯度提升类别一致性  
- 图像修补（inpainting）：强制已知像素匹配条件分布  
- 图像上色（colorization）：条件是灰度像素值  

**优势**  
- 同一模型支持多任务  
- 灵活替换条件来源  
- CIFAR-10 类别条件生成、修补、上色效果显著提升  
