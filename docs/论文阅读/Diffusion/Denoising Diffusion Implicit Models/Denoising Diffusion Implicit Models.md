
[文章连接 《Denoising Diffusion Implicit Models》](https://arxiv.org/abs/2010.02502)

!!! warning-box "注意"
    本文内容主要由 AI 生成

DDIM 的核心目标只有一个：在“不重新训练网络”的前提下，让已经训练好的 DDPM 模型更快地生成高质量样本，同时还能像 GAN 一样做语义插值和精确重建。为此，作者把 DDPM 的生成流程重新梳理成“非马尔可夫”的视角，然后用一种更短、更确定性的路径完成从噪声到图像的反向过程。下面按时间顺序把整个流程拆开，说明每一步为什么要这样做、它解决了什么问题、以及最终带来了什么好处。

## 1. 先回顾一下 DDPM 的原始套路

DDPM 把数据 $x_0$ 通过 $T$ 步马尔可夫链逐步加噪变成近似高斯分布的 $x_T$，再训练一个网络 $\varepsilon_\theta(x_t , t)$ 学会“预测每一步加进去的噪声”。生成时，从纯高斯噪声 $x_T$ 出发，按 $T$ 步反向去噪，最终得到一张图片。

公式上，训练时只用到边缘分布

$$
q(x_t \mid x_0) = \mathcal{N}(\sqrt{\alpha_t} x_0, (1-\alpha_t) I)
$$

和对应的噪声预测损失

$$
L_1 = \sum_t \|\varepsilon_\theta(x_t , t) - \varepsilon\|^2
$$

而实际反向链

$$
p_\theta(x_{t-1}\mid x_t) = \mathcal{N}(\mu_\theta(x_t , t), \Sigma_t)
$$

必须一步一步走，且步数 $T$ 很大(1000)，所以慢。

## 2. 为什么可以改流程？——关键观察

训练目标 $L_1$ 只依赖“$x_t$ 的边缘分布”和“噪声预测网络”，而不关心“整条链是不是马尔可夫”。也就是说：只要保证 $q(x_t \mid x_0)$ 不变，链中间怎么跳步、是否随机，都不影响训练好的 $\varepsilon_\theta$ 依然是最优解。

于是作者提出一族新的“非马尔可夫前向过程” $q_\sigma(x_{1:T}\mid x_0)$，用一个额外的方差向量 $\sigma$ 来控制每一步的随机程度。当 $\sigma_t \to 0$，过程几乎确定；当 $\sigma_t$ 取特定值，就退回原始 DDPM。

## 3. 构造非马尔可夫链——公式层面

新的前向链写作

$$
q_\sigma(x_{t-1}\mid x_t , x_0) = \mathcal{N}\!\bigl(\mu(x_t , x_0),\, \sigma_t^2 I\bigr)
$$

其中均值 $\mu$ 被精心选成：

$$
\mu = \sqrt{\alpha_{t-1}} x_0 + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\, \frac{x_t - \sqrt{\alpha_t} x_0}{\sqrt{1-\alpha_t}}
$$

这样设计是为了“边缘一致性”——无论 $\sigma$ 怎么变，$q(x_t \mid x_0)$ 始终是 $\mathcal{N}(\sqrt{\alpha_t} x_0, (1-\alpha_t) I)$。

有了这个性质，训练目标 $J_\sigma$ 与原来的 $L_1$ 只差一个不依赖 $\theta$ 的常数，因此 **完全不需要重训网络**。

## 4. 反向生成时把 $\sigma$ 当旋钮

生成时，我们反过来用 $x_t$ 预测 $x_0$，再用上面的 $q_\sigma$ 采样 $x_{t-1}$。公式变成

$$
x_{t-1} = \sqrt{\alpha_{t-1}} f_\theta(x_t) + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\, \varepsilon_\theta(x_t) + \sigma_t \varepsilon
$$

其中

$$
f_\theta(x_t)=\frac{x_t - \sqrt{1-\alpha_t}\,\varepsilon_\theta(x_t,t)}{\sqrt{\alpha_t}}
$$

是网络对 $x_0$ 的点估计。

- 把 $\sigma_t$ 全设为 0，就得到 **DDIM**——一条确定性的、由 $x_T$ 唯一决定 $x_0$ 的隐式模型。  
- 把 $\sigma_t$ 设为原 DDPM 值，就回到随机 DDPM。  
- 把 $\tau$ 选成 $[1,\dots,T]$ 的子序列（比如 20 步），就能在 20 次迭代内完成采样。

## 5. 细节优化 1：选 $\tau$ 的策略

$\tau$ 的选取直接影响“跳步”后信息的丢失程度。作者试了两种简单规则：

- 线性：$\tau_i = \lfloor c \cdot i \rfloor$  
- 二次：$\tau_i = \lfloor c \cdot i^2 \rfloor$

实验里发现对 32×32 的 CIFAR-10 用二次更好，对 64×64 以上用线性即可。这一步纯粹是为了在极少步数下仍保持高质量，没有理论门槛，实践中按验证集 FID 挑即可。

## 6. 细节优化 2：ODE 视角与编码能力

把迭代改写成连续 ODE 后，DDIM 的更新式与 Euler 法解 ODE 完全一致：

$$
\frac{\mathrm{d}\bar{x}(\sigma)}{\mathrm{d}\sigma} = \varepsilon_\theta\!\left(\frac{\bar{x}(\sigma)}{\sqrt{\sigma^2+1}}\right)
$$

这意味着：

- 可以用更精确的 ODE 积分器（多步 Adams、RK45 等）进一步减少步数；  
- 可以从 $x_0$ 逆向积分到 $x_T$，把真实图像“编码”成隐变量，再正向积分回来，实现近乎无损的重建（见表 2 的 MSE 结果）。

DDPM 由于反向链是随机的，几乎不可能做这种确定性的编解码。

## 7. 语义插值——$x_T$ 就是高层语义码

在 DDIM 里，$x_T$ 完全决定最终图像的“长相”。于是，把两张图的 $x_T$ 做球面线性插值（slerp），再跑一次短链，就能生成一条平滑、语义连贯的过渡序列；而 DDPM 因为每一步都注入随机噪声，插值结果几乎不可用。

## 8. 实验验证：省了多少时间？

用同一组预训练权重，仅改变 $(\tau,\sigma)$ 组合：

- **CIFAR-10**：20 步 DDIM 的 FID ≈ 4.67，与 1000 步 DDPM 的 4.04 几乎持平，但时间 ×50 倍减少。  
- **CelebA-HQ 256×256**：50 步 DDIM 得到 FID ≈ 6.5，而 50 步 DDPM 已掉到 45 以上。

此外，把 $\sigma$ 调到 0.2~0.5 还能在速度与质量之间做平滑折中。

## 9. 结论一句话

DDIM 用“同训练、不同采样”的思路，把原本需要一千步的扩散采样压缩到几十步甚至十步以内，同时额外赋予模型确定性的隐空间，使得插值、编码、重建都变成顺手功能，而所有这些只需在生成阶段改几行代码即可。
