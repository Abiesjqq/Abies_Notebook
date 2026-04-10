文章：From Slow Bidirectional to Fast Autoregressive Video Diffusion Models [![arXiv](https://img.shields.io/badge/arXiv-2412.07772-b31b1b.svg)](https://arxiv.org/pdf/2412.07772)

Causal Vid: 用作快速和交互性的因果性视频生成的模型

这边主要看方法

### 相关工作

**自回归 (Autoregressive) 视频生成** 这里提到自回归的基于扩散模型的视频生成，大概就是用前一部分（可能是固定窗口）自身的去噪结果（可能是 latent）去生成下一帧，而不是基于全部视频帧（T 帧）去去噪，这样能大大降低模型计算压力

同时自回归的实现形式可以实现变长度的视频生成，而不是一般 diffusion 固定视频长度

**Diffusion Distillation**

训练一个少不是 student model，让它去模仿原长步数的 teacher model 的行为，