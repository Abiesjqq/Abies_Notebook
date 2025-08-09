
[文章连接 《Denoising Diffusion Probabilistic Models》](https://arxiv.org/abs/2006.11239)

!!! warning-box "注意"
    本文内容主要由 AI 生成

## 1. 生成模型的共同目标

生成模型的核心目标是通过学习数据的分布，生成与真实数据相似的新样本。具体来说，我们希望模型能够：  
- **高效采样**：快速生成新的样本。  
- **高保真**：生成的样本与真实数据在视觉上难以区分。  
- **可评估密度**：能够计算生成样本的概率密度，用于进一步的分析和应用。  

Diffusion 模型通过“去噪”的过程，将这些目标统一到一个框架中。

---

## 2. Diffusion 模型的“两阶段”直觉

Diffusion 模型的核心思想是通过两个阶段实现生成任务：
1. **前向过程（Forward Process）**：将清晰的图像逐渐加噪，直到变成纯噪声。
2. **反向过程（Reverse Process）**：从纯噪声开始，逐步去噪，恢复出清晰的图像。

这两个过程共同构成了 Diffusion 模型的生成机制。

---

## 3. 前向过程（Forward Process）

### 3.1 定义
前向过程是一个固定的马尔可夫链，逐步将图像加噪。每一步加的噪声是高斯分布：


$$
q(x_t \mid x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t}\,x_{t-1}, \beta_t I)
$$ 

其中，$\beta_t$ 是预设的超参数，控制每一步加的噪声量。随着 $t$ 的增加，图像逐渐变得模糊，最终变成纯噪声。

### 3.2 任意步闭式采样
利用高斯分布的性质，可以直接从任意步 $t$ 采样，而不需要逐步递归。具体公式为：


$$
x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon, \quad \epsilon \sim \mathcal{N}(0,I)
$$ 

其中，$\bar{\alpha}_t = \prod_{s=1}^{t}(1-\beta_s)$。这个公式使得我们可以在训练时直接跳到任意步 $t$，大大提高了效率。

---

## 4. 反向过程（Reverse Process）

### 4.1 目标
反向过程的目标是从纯噪声 $x_T \sim \mathcal{N}(0,I)$ 开始，逐步恢复出清晰的图像 $x_0$。这个过程是通过学习一个参数化的马尔可夫链实现的：


$$
p_\theta(x_{t-1} \mid x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \sigma_t^2 I)
$$ 

其中，$\mu_\theta(x_t, t)$ 是神经网络的输出，$\sigma_t$ 是固定的方差。

### 4.2 参数化
为了简化实现，$\sigma_t$ 被固定为 $\beta_t$ 或 $\tilde{\beta}_t$。因此，我们只需要学习均值函数 $\mu_\theta(x_t, t)$。

---

## 5. 变分下界 ELBO 的完整推导

### 5.1 生成模型与证据
为了评估生成模型的性能，我们最大化训练数据的对数似然：


$$
\log p_\theta(x_0) = \log \int p_\theta(x_{0:T})\,dx_{1:T}
$$ 

由于直接计算这个积分非常困难，我们引入一个近似后验分布 $q(x_{1:T} \mid x_0)$，并使用变分推断得到一个下界（ELBO）：


$$
\log p_\theta(x_0) \ge \mathbb{E}_{q(x_{1:T} \mid x_0)}\!\left[\log\frac{p_\theta(x_{0:T})}{q(x_{1:T} \mid x_0)}\right] =: -\mathcal{L}_{\text{VLB}}
$$ 

### 5.2 展开 ELBO
将联合概率分解为：


$$
p_\theta(x_{0:T}) = p(x_T)\prod_{t=1}^{T} p_\theta(x_{t-1} \mid x_t)
$$ 

代入 ELBO，得到：


$$
\mathcal{L}_{\text{VLB}} = D_{\text{KL}}(q(x_T \mid x_0) \| p(x_T)) + \sum_{t=2}^{T} D_{\text{KL}}(q(x_{t-1} \mid x_t, x_0) \| p_\theta(x_{t-1} \mid x_t)) - \mathbb{E}_q[\log p_\theta(x_0 \mid x_1)]
$$ 

这个公式包含了三个部分：  
1. **初始噪声的 KL 散度**：衡量初始噪声分布与先验分布的差异。  
2. **中间步骤的 KL 散度**：衡量每一步的去噪过程与目标分布的差异。  
3. **最终步骤的对数似然**：衡量最终生成的图像与真实图像的相似度。  

---

## 6. 从 ELBO 到可训练的 MSE Loss

### 6.1 重新参数化均值
为了简化训练过程，我们将均值函数 $\mu_\theta(x_t, t)$ 重新参数化为：


$$
\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}}\!\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t, t)\right)
$$ 

其中，$\epsilon_\theta(x_t, t)$ 是神经网络的输出，表示预测的噪声。

### 6.2 代入 KL，化简为 MSE
将上述均值函数代入 KL 散度，最终得到一个简化的损失函数：


$$
\mathcal{L}_{\text{simple}} = \mathbb{E}_{x_0, \epsilon, t}\!\big[\|\epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon, t)\|^2\big]
$$ 

这个损失函数是一个均方误差（MSE），表示预测的噪声与真实噪声之间的差异。通过最小化这个损失函数，我们可以训练出一个有效的去噪模型。

---

## 7. 采样（Sampling）算法

在训练完成后，我们可以通过以下步骤从纯噪声生成清晰的图像：

1. 从纯噪声开始：$x_T \sim \mathcal{N}(0, I)$。
2. 逐步去噪：对于 $t = T, T-1, \dots, 1$，使用以下公式更新图像：

    $$
    x_{t-1} = \frac{1}{\sqrt{\alpha_t}}\!\left(x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t, t)\right) + \sigma_t z, \quad z \sim \mathcal{N}(0, I)
    $$ 

3. 最终得到 $x_0$，即生成的图像。

---

## 8. 代码实现视角的公式映射

在实际代码实现中，上述公式可以直接映射为以下 PyTorch 代码片段：

| **数学符号** | **PyTorch 代码片段** | **说明** |
|---|---|---|
| $x_0$ | `x0: Tensor` | 原始图像，范围 `[-1, 1]` |
| $\beta_t$ | `betas: Tensor[T]` | 预定义噪声调度，长度 `T` |
| $\alpha_t = 1 - \beta_t$ | `alphas = 1 - betas` | 每一步的保留系数 |
| $\bar{\alpha}_t = \prod_{s=1}^{t}\alpha_s$ | `alphas_cumprod = alphas.cumprod(0)` | 累积乘积 |
| $\sqrt{\bar{\alpha}_t}$ | `sqrt_alphas_cumprod = alphas_cumprod.sqrt()` | 用于加噪 |
| $\sqrt{1 - \bar{\alpha}_t}$ | `sqrt_one_minus_alphas_cumprod = (1 - alphas_cumprod).sqrt()` | 用于加噪 |
| **加噪公式** $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon$ | `x_t = sqrt_alphas_cumprod[t] * x0 + sqrt_one_minus_alphas_cumprod[t] * eps` | 训练时一步得到任意步噪声图 |
| $\epsilon_\theta(x_t, t)$ | `eps_pred = model(x_t, t)` | U-Net 输出预测噪声 |
| **训练损失** $\|\epsilon - \epsilon_\theta\|_2^2$ | `loss = F.mse_loss(eps, eps_pred)` | 简化损失 |
| **采样更新** $x_{t-1}$ 公式 | `x_prev = (x_t - (1 - alphas[t]) / sqrt_one_minus_alphas_cumprod[t] * eps_pred) / alphas[t].sqrt() + sigma_t * torch.randn_like(x_t)` | DDPM 采样一步 |
| `sigma_t` 选择 | `sigma_t = betas[t].sqrt()` | 对应 DDPM 随机采样；若为 0 → DDIM |

---


### 训练循环伪代码（极简版）

```python
# 预计算张量
alphas_cumprod = torch.cumprod(1 - betas, dim=0)
sqrt_alphas_cumprod = alphas_cumprod.sqrt()
sqrt_one_minus_alphas_cumprod = (1 - alphas_cumprod).sqrt()

for x0 in dataloader:
    t = torch.randint(0, T, (x0.size(0),), device=x0.device)
    noise = torch.randn_like(x0)
    x_t = sqrt_alphas_cumprod[t, None, None, None] * x0 \
          + sqrt_one_minus_alphas_cumprod[t, None, None, None] * noise
    eps_pred = model(x_t, t)
    loss = F.mse_loss(noise, eps_pred)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    x_t = torch.randn_like(x0)  # 从纯噪声开始
    for t in reversed(range(T)):
        eps_pred = model(x_t, torch.full((x_t.size(0),), t, device=x_t.device))
        sigma_t = betas[t].sqrt()
        z = torch.randn_like(x_t) if t > 0 else 0
        x_t = (x_t - (1 - alphas[t]) / sqrt_one_minus_alphas_cumprod[t] * eps_pred) \
              / alphas[t].sqrt() + sigma_t * z
    return x_t  # 最终生成图
```
