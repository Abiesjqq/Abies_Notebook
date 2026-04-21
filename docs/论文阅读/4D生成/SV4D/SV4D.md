
[文章链接 SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency](https://arxiv.org/abs/2407.17470)

这个更加恶心哈哈哈，diffusion的结果也比较恶心哈哈

> 这边相当于科研笔记吧:D (不理一下根本搞不清楚)

全称: Stable Video 4D，基于 SVD 和 SV3D

## Method

input 基本同 L4GM，讲一下主要的 pipeline 吧

输入视频 $\{I_t\}_{t = 1}^F$，resizing + normalizing，然后使用 VAE encoder 编码到 latent ($z_0$)，并加噪.

$$
z_t = \sqrt{\alpha_t}z_0 + \sqrt{1 - \alpha_t}\varepsilon
$$

其中 $\varepsilon \sim \mathcal{N}(0, 1) \in \mathbb{R}^{F \times V \times C \times H \times W}$ 为加上的噪声

然后，将第一帧 $I_1$ 进行 SV3D 生成，形成 $v$ 个视角的视频帧，anchor 住物体形状

数据预处理得到的 embedding ($\text{cond}$) 有 **原视频 latent**、**原视频 CLIP embedding**、**相机外参 embedding**、**第一帧的 multi-view latent**

然后是关键的 SV4D Diffusion UNet

我们输入的 latent 为 $(F, V, C, H, W)$ 的 tensor，然后在 UNet 的各个 block 阶段依次加入同一视角的 **Frame attention** 和同一时间的 **View attention**

最后训练时最小化 DDPM-style denoising loss （Diffusion 常用）

具体来说，训练时，我们根据输入的 $z_t$ 和 $\text{cond}$ 预测加上的噪声，然后计算 loss

$$
\mathcal{L} = \mathbb{E}_{t, \varepsilon}\Vert \varepsilon - \hat{\varepsilon}(z_t, \text{cond}) \Vert^2
$$

推理时，则用预测的 $\hat{\varepsilon}$ 来给初始噪声 $z_t$ 进行去噪得到生成的 4d latent，然后再用 VAE decoder 得到生成结果

## LoRA 训练

Suspended

## 基于 Causvid 思路的 DMD 蒸馏

### Causvid 的基本流程

Causvid 的基本目标是将双向、慢速的 diffusion 模型蒸馏成一个快速（一般是 autoregressive transformer）且 causal 的模型（适用于 rollout）

DMD (Diffusion Model Distillation): 将多步的 Diffusion 蒸馏到少步的 Diffusion，Causvid 可以理解成是将 DMD 的思路扩展到 video + AR 上

