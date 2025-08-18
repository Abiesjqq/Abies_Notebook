
[文章连接 《Unleashing the Power of One-Step Diffusion based Image Super-Resolution via a Large-Scale Diffusion Discriminator》](https://arxiv.org/abs/2410.04224)

!!! warning-box "注意"
    本文内容主要由 AI 生成
---

## **1. Introduction（引言）**
- **问题背景**：图像超分辨率（Image Super-Resolution, SR）希望从低分辨率 (LR) 图像恢复高分辨率 (HR) 图像。  
- **现有挑战**：  
  1. **多步扩散模型 (multi-step diffusion)** 在 SR 中表现强，但推理开销大（几十到上百步采样）。  
  2. **单步扩散模型 (one-step diffusion)** 提升速度，却在质量上明显落后。  
  3. GAN 方法训练稳定性差，缺乏大规模稳定替代方案。  

- **论文贡献**：  
  - 提出 **One-Step Diffusion GAN (OSDG)** 框架。  
  - 引入 **大规模扩散判别器 (Diffusion Discriminator, DD)**，作为训练的核心监督。  
  - 在 **训练阶段**使用多步扩散判别器约束 → 在**推理阶段**只需单步扩散生成。  
  - 在多个数据集上实现 **接近多步扩散的质量 + 远快于其的速度**。  

---

## **2. Related Work（相关工作）**
- **超分辨率方法**：  
  - CNN-based (EDSR, RCAN)：提升 PSNR，但缺乏感知质量。  
  - GAN-based (SRGAN, ESRGAN)：增强感知细节，但训练不稳定，容易过拟合或引入伪影。  

- **扩散模型 (Diffusion Models)**：  
  - 优点：逐步去噪的方式，生成质量极高。  
  - 缺点：需要 **多步采样**，推理速度慢。  

- **单步扩散 (One-Step Diffusion)**：  
  - 最近研究试图压缩扩散过程到一步，但导致感知质量急剧下降。  
  - 现有方法缺乏有效的 **训练信号** 来指导单步生成器。  

**本文定位**：提出 **Diffusion Discriminator**，作为 **GAN 判别器的替代品**，利用多步扩散的强分布对齐能力，指导单步扩散模型。  

---

## **3. Methodology（方法）**

### **3.1 扩散模型回顾**
#### (1) 正向加噪过程：

$$
q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t}x_{t-1}, \beta_t I)
$$

- $x_t$：第 $t$ 步带噪样本  
- $\beta_t$：噪声调度  

重参数化公式：  

$$
x_t = \alpha_t x_0 + \sigma_t \epsilon, \quad \epsilon \sim \mathcal{N}(0,I)
$$

#### (2) 反向去噪过程：

$$
p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))
$$

---

### **3.2 单步扩散生成器 (One-Step Generator)**
- 将扩散过程压缩为一步：  
  - 输入：低分辨率图像 $x_{LR}$  
  - 输出：一步生成的超分辨率图像 $\hat{x}_{HR}$。  

- 损失函数：  
  - 基础重建损失 (L1, L2)。  
  - 感知损失 (LPIPS)。  
  - 最重要：来自 **扩散判别器**的对抗性损失。  

---

### **3.3 大规模扩散判别器 (Diffusion Discriminator, DD)**
- **思想**：传统 GAN 判别器 $D(x)$ 判断真/假；而本工作使用 **多步扩散模型** 作为判别器，提供更强监督。  

- **训练机制**：  
  1. 真实 HR 图像 → 经过正向扩散得到 $x_t$。  
  2. 单步生成的 $\hat{x}$ 也经过相同扩散过程得到 $\hat{x}_t$。  
  3. 多步扩散判别器学习区分 $(x_t)$ 与 $(\hat{x}_t)$。  

- 判别损失：  

$$
\mathcal{L}_{DD} = \mathbb{E}_{x} \left[ \log D(x_t, t) \right] + \mathbb{E}_{\hat{x}} \left[ \log(1 - D(\hat{x}_t, t)) \right]
$$

- 最终训练目标：  

$$
\mathcal{L} = \mathcal{L}_{rec} + \lambda_1 \mathcal{L}_{perc} + \lambda_2 \mathcal{L}_{DD}
$$

---

## **4. Experiments（实验）**

### **4.1 数据集**
- DIV2K  
- Flickr2K  
- RealSR  
- 宽泛的高分辨率自然图像集合  

### **4.2 评价指标**
- **传统指标**：PSNR, SSIM  
- **感知指标**：LPIPS, DISTS  
- **用户研究**：人类偏好测试  

### **4.3 对比实验**
- Baselines：EDSR, RCAN, ESRGAN, Real-ESRGAN, DiffusionSR 等。  
- 结果：  
  - 单步扩散在速度上比多步扩散快 $10\sim 50\times$。  
  - 在质量指标上接近多步扩散，优于现有单步扩散和 GAN-based 方法。  

### **4.4 消融实验**
- 仅使用 L1 → 图像过于平滑。  
- 使用 GAN 判别器 → 不稳定，存在伪影。  
- 使用 Diffusion Discriminator → 稳定收敛，质量最佳。  

---

## **5. Conclusion（结论）**
- 提出 **OSDG 框架**，实现单步扩散图像超分辨率。  
- 创新点：  
  - 提出 **大规模扩散判别器 (Diffusion Discriminator)**，替代传统 GAN 判别器。  
  - 在推理阶段只需一步采样，但质量接近多步扩散。  
- **优势**：兼顾 **高效性（速度）** 与 **高质量（感知指标、用户偏好）**。  
