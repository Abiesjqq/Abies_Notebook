
[文章连接 《DOVE: Efficient One-Step Diffusion Model for Real-World Video Super-Resolution》](https://arxiv.org/abs/2505.16239)

!!! warning-box "注意"
    本文内容主要由 AI 生成

---

## **1. Introduction（引言）**
本文研究视频超分辨率（VSR），目标是从低分辨率视频恢复出高分辨率结果。现有的多步扩散方法能够生成高质量结果，但推理速度慢；而单步扩散方法虽然高效，却在生成质量上有明显退化，并且往往缺乏跨帧的一致性，导致结果出现闪烁。为此，作者提出了 **DOVE (Diffusion One-step Video Enhancer)**，它在保证高效推理的同时，兼顾了画质和时间一致性。核心贡献包括：提出 **条件感知的噪声蒸馏（Condition-aware Noise Distillation, CND）**，以增强单步扩散生成质量；引入 **时序一致性正则化（Temporal Consistency Regularization, TCR）**，确保跨帧稳定性。最终，DOVE 在真实世界视频超分辨率中取得接近多步扩散模型的表现，但推理速度大幅提升。

---

## **2. Related Work（相关工作）**
早期视频超分辨率方法主要基于 CNN 或 RNN，如 EDVR、BasicVSR++，能够提升 PSNR，但重建细节不足。GAN 类方法（如 Real-ESRGAN, VSRGAN）能恢复更多细节，但训练往往不稳定，并可能引入伪影。扩散模型因逐步去噪而展现了强大的生成能力，多步扩散在图像和视频超分辨率上均取得了优异表现，但推理效率过低。单步扩散虽然尝试将多步压缩为一步以提升速度，但缺乏有效监督，导致结果质量下降。此外，现有方法在跨帧一致性建模方面依赖光流对齐或递归传播，而扩散 VSR 中缺少系统的时间一致性约束。本文的定位正是在高效单步扩散的基础上，引入蒸馏与一致性正则化，从而在真实视频超分任务中兼顾效率与质量。

---

## **3. Methodology（方法）**
在标准扩散模型中，正向加噪过程为  

$$
z_t = \alpha_t z_0 + \sigma_t \epsilon, \quad \epsilon \sim \mathcal{N}(0,I),
$$

而反向去噪的目标是通过 U-Net 预测干净样本的残差信息，其训练损失定义为  

$$
\mathcal{L}_{\text{diff}} = \mathbb{E}_{z, t, \epsilon}\left[ \| v - f_\theta(z_t, t, c) \|_2^2 \right],
$$

其中 $c$ 表示低分辨率帧作为条件输入。  

为增强单步扩散的生成能力，作者提出了 **条件感知的噪声蒸馏 (CND)**。其思路是以多步扩散模型作为教师，提供丰富的生成信号，指导一步扩散生成器学习接近教师的结果。其蒸馏损失为  

$$
\mathcal{L}_{\text{CND}} = \mathbb{E}\left[ \| G_{1}(x_{LR}) - G_{T}(x_{LR}) \|_1 \right],
$$

其中 $G_{1}$ 表示单步扩散学生模型，$G_{T}$ 表示多步扩散教师模型。  

另一方面，为解决跨帧抖动问题，提出了 **时序一致性正则化 (TCR)**。具体做法是利用光流 $f_{i \to i+1}$ 将第 $i$ 帧 warp 到第 $i+1$ 帧，在潜空间中约束相邻帧的一致性：  

$$
\mathcal{L}_{\text{TCR}} = \mathbb{E}\left[ \| W(z^i, f_{i \to i+1}) - z^{i+1} \|_1 \right],
$$

其中 $W(\cdot)$ 表示基于光流的变换操作。  

综合起来，最终的训练目标为  

$$
\mathcal{L} = \lambda_1 \mathcal{L}_{\text{diff}} + \lambda_2 \mathcal{L}_{\text{CND}} + \lambda_3 \mathcal{L}_{\text{TCR}}.
$$

---

## **4. Experiments（实验）**
实验部分使用 WebVid 与 YouHQ 等高质量视频作为训练集，测试集包括合成数据集（REDS, UDM10, SPMCS）和真实数据集（VideoLQ, AIGC-Video）。在有 GT 的场景中，采用 PSNR、SSIM、LPIPS 与 tOF（一致性指标）；在无 GT 的场景下，使用 NIQE、CLIP-IQA 与 MUSIQ 进行评估。实验结果表明，DOVE 在质量上接近多步扩散方法 Upscale-A-Video，而在推理速度上快 $20 \sim 50$ 倍，并在时间一致性指标上显著优于其他单步方法。消融实验进一步验证了各模块的重要性：若去掉 CND，图像会过于平滑；去掉 TCR，则出现明显闪烁；而两者结合能够获得最优的结果。

---

## **5. Conclusion（结论）**
本文提出了 **DOVE**，一种高效的一步扩散视频超分方法，兼顾了速度与生成质量。其创新之处在于引入了条件感知的噪声蒸馏（CND），以增强单步扩散模型的生成能力，并提出时序一致性正则化（TCR），有效解决了跨帧不稳定的问题。实验表明，DOVE 在真实世界视频超分任务中实现了高质量、时间一致且接近实时的推理，具有很强的实用价值。
