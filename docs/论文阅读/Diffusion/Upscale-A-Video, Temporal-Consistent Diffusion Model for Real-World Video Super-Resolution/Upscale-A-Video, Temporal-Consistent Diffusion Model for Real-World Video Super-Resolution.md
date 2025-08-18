
[文章连接 《Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution》](https://arxiv.org/abs/2312.06640)

!!! warning-box "注意"
    本文内容主要由 AI 生成

---

## **1. Introduction（引言）**
- **任务目标**：视频超分辨率（Video Super-Resolution, VSR） → 从低质量视频恢复高分辨率、高保真、时间一致的结果。  
- **挑战**：  
  1. **复杂退化**：真实世界中不仅有下采样，还包括噪声、模糊、压缩伪影、闪烁等。  
  2. **时间一致性**：扩散模型采样具有随机性，容易导致帧间不一致（flickering）。  
  3. **局部 vs 全局**：现有方法只能保证短序列内一致性，长视频仍有跨段不连贯。  

- **核心贡献**：  
  - 提出 **局部-全局（local-global）时间一致性策略**：  
    - 局部：在 **U-Net** 与 **VAE-Decoder** 中加入 3D 卷积、时间注意力。  
    - 全局：提出 **训练无关的光流引导潜空间递归传播（flow-guided recurrent latent propagation）**。  
  - 引入**文本引导（text prompt）**与**噪声调节（noise level control）**，在修复与生成之间实现平衡。  

---

## **2. Related Work（相关工作）**
- **Video Super-Resolution (VSR)**：  
  - CNN-based（如 EDVR、BasicVSR++）：在短期内表现好，但生成的纹理往往过于平滑。  
  - Real-world VSR：通常依赖数据增强或特殊采集数据，泛化性不足。  

- **Diffusion Models**：  
  - 基本思想：逐步加噪、逐步去噪。  
  - 在图像生成中已广泛应用（Stable Diffusion），但在视频中需要解决**跨帧一致性**。  

- **Diffusion for Restoration**：  
  - 从零训练（昂贵）或基于预训练模型（更高效）。  
  - 现有扩散方法仍难以保持长视频的一致性。  

**本工作定位**：在真实世界 VSR 中，首次系统性结合**扩散模型的生成先验**与**局部-全局时间一致性机制**。  

---

## **3. Methodology（方法）**

### **3.1 预备知识：扩散模型**
#### (1) 正向扩散（加噪过程）
给定真实样本 $z$，在时间步 $t$ 加入噪声：

$$
z_t = \alpha_t z + \sigma_t \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)
$$

- $\alpha_t, \sigma_t$：由噪声调度（noise schedule）控制。  

#### (2) 反向扩散（去噪过程）
模型学习在每一步估计干净样本：

$$
\mathcal{L}_{\text{LDM}} = \mathbb{E}_{z, x, c, t, \epsilon}\left[ \| v - f_\theta(z_t, x_\tau; c, t) \|^2_2 \right] \tag{1}
$$

其中：  
- $f_\theta$：U-Net 去噪器  
- $v \equiv \alpha_t \epsilon - \sigma_t x$ (v-prediction 参数化)  
- $c$：条件，包括文本 prompt 和噪声水平  

---

### **3.2 局部一致性（Local Consistency）**
- **动机**：单帧 VAE 解码器在视频中会产生**闪烁（flickering）**。  
- **方法**：  
  1. **Temporal U-Net**  
     - 在原始 2D 层中插入 3D 残差块和 temporal attention。  
     - 使用 RoPE（Rotary Position Embedding）提供时间位置信息。  
     - 训练时冻结空间层，仅优化时间层，减少计算量。  

  2. **Temporal VAE-Decoder**  
     - VAE 解码器原本是逐帧解码 → 容易产生颜色抖动。  
     - 改进：在解码器中加入 3D 残差块，并引入 **SFT（Spatial Feature Transform）** 层，以输入视频提供低频信息（颜色、光照），保证颜色稳定性。  
     - 损失函数：  

$$
\mathcal{L}_{\text{VAE}} = \lambda_1 \| y - \hat{y} \|_1 + \lambda_2 \text{LPIPS}(y, \hat{y}) + \lambda_3 \mathcal{L}_{\text{GAN}}
$$

---

### **3.3 全局一致性（Global Consistency）**
- **动机**：U-Net 和 VAE 只能保证局部序列（如 8 帧）的稳定性，长视频仍然会有跳变。  

- **方法**：提出 **训练无关的潜空间递归传播（Recurrent Latent Propagation）**  
  1. 使用 **RAFT 光流** 计算前后帧的像素流。  
  2. 检查**前向-后向一致性误差**：  

    $$
    E_{i-1 \to i}(p) = \| f_{i-1 \to i}(p) + f_{i \to i-1}(p + f_{i-1 \to i}(p)) \|^2_2 \tag{2}
    $$

    > 若误差小 → 说明光流有效，允许传播；否则丢弃。  

  3. **潜空间更新**：  

    $$
    \tilde{z}^i_0 = \Big[ W(\tilde{z}^{i-1}_0, f_{i \to i-1}) \cdot \beta + \hat{z}^i_0 \cdot (1 - \beta) \Big] \cdot M + \hat{z}^i_0 \cdot (1-M) \tag{3}
    $$

  - $W(\cdot)$：warp 操作  
  - $\beta$：融合权重  
  - $M$：由误差阈值 $\delta$ 得到的掩码  

---

### **3.4 推理时的可控条件**
1. **文本 Prompt**：可引导纹理生成（如“狮子鬃毛”、“油画风格”）。  
2. **噪声水平 $\tau$**：  
   - 小噪声 → 偏向恢复（restoration）。  
   - 大噪声 → 偏向生成（generation），细节更锐利。  
3. **Classifier-Free Guidance (CFG)**：增强 prompt 与噪声的控制效果。  

---

## **4. Experiments（实验）**

### **4.1 数据集与实现**
- **训练集**：  
  - WebVid10M 子集（33.5 万视频-文本对）  
  - 新采集的 **YouHQ** 数据集（3.7 万高清视频，1080×1920，包含街景、动物、人脸、水下、夜景等）  
- **测试集**：  
  - 合成：SPMCS, UDM10, REDS30, YouHQ40  
  - 真实：VideoLQ  
  - AIGC：AIGC30（来自 text-to-video 生成模型）  

### **4.2 对比结果**
- **指标**：  
  - 有 GT → PSNR, SSIM, LPIPS, E*warp（光流误差）  
  - 无 GT → CLIP-IQA, MUSIQ, DOVER  
- **结论**：  
  - Upscale-A-Video 在所有合成与真实数据集上取得最优或次优。  
  - 特别在**时间一致性（E*warp）**上优于 RealBasicVSR、StableSR 等强基线。  

### **4.3 消融实验**
- **VAE-Decoder finetune**：显著减少闪烁，提高一致性。  
- **Propagation 模块**：进一步改善长视频稳定性。  
- **Prompt / Noise level**：可控性强，能在 fidelity 与 realism 之间调节。  

---

## **5. Conclusion（结论）**
- 提出 **Upscale-A-Video**：结合 **扩散模型生成先验** 与 **局部-全局一致性策略**，实现真实世界视频超分辨率。  
- 创新点：  
  - **局部一致性**：Temporal U-Net + Temporal VAE-Decoder  
  - **全局一致性**：训练无关的光流引导潜空间传播  
  - **可控性**：Prompt + Noise level  
- 在真实与 AIGC 视频上均表现出 SOTA 的效果。  
