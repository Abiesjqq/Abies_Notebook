## 随机样本与统计量

### 随机样本的定义

**简单随机样本**：每个个体 $X_i$ 的分布与总体 $X$ 相同，且 $X_1\cdots X_n$ 相互独立。

后面出现的“样本”均指随机样本。

### 随机样本的统计量

统计量：

- **均值**：$\bar{X}=\frac{1}{n}\sum X_i$
- **方差**：$S^2=\frac{1}{n-1}\sum (X_i-\bar{X})^2$
- **k 阶（原点）矩**：$A_k=\frac{1}{n}\sum X_i^k$
- **k 阶中心矩**：$B_k=\frac{1}{n}\sum (X_i-\bar{X})^k$

统计量间的关系：

- $A_1=\bar{X}$
- $B_2=\frac{n-1}{n}S^2$

随机样本的特征依概率收敛于总体的特征。

!!! remarks "常用的结论"

    $$E(\bar{X})=E(X);$$

    $$Var(\bar{X})=\frac{Var(X)}{n};$$

    $$S^2=\frac{1}{n-1}\left(\sum X_i^2-n\bar{X}^2\right);$$

    $$E(X^2)=Var(X)+E(X)^2;$$

    $$E(S^2)=Var(X).$$

**标准正态分布的上侧 $\alpha$ 分位数**：设 $X\sim N(0,1)$，若 $z_{\alpha}$ 满足 $P(X>z_{\alpha}=\alpha)$，则称 $z_{\alpha}$ 为标准正态分布的上侧 $\alpha$ 分位数。

$z_{\alpha}$ 的性质：

1. $z_{1-\alpha}=z_{\alpha}$
2. $\Phi(z_{\alpha})=1-\alpha$

## 常用的分布

### 卡方分布

若随机变量 $\{X_1, X_2, \dots, X_n\}$ 相互独立，且每个 $X_i \sim N(0,1)$（标准正态分布），则定义 $X = \sum_{i=1}^{n} X_i^2$ 为服从自由度为 $n$ 的卡方分布，记作 $X \sim \chi^2(n)$.

**自由度**：指独立的标准正态随机变量的个数。

??? normal-comment "卡方分布的概率密度"

    定义 $\Gamma$ 函数：

    $$\Gamma(\alpha) = \int_0^{+\infty} t^{\alpha-1} e^{-t} dt \quad (\alpha > 0)$$

    $\Gamma$ 函数的性质：

    - $\Gamma(\alpha+1) = \alpha \cdot \Gamma(\alpha)$
    - 若 $\alpha$ 为正整数，则 $\Gamma(\alpha+1) = \alpha!$
    - $\Gamma(0.5) = \sqrt{\pi}$

    设 $Y \sim \chi^2(n)$，其概率密度函数为：

    $$
    f(x) =
    \begin{cases}
    \displaystyle \frac{1}{2^{\frac{n}{2}} \Gamma\left(\frac{n}{2}\right)} x^{\frac{n}{2}-1} e^{-\frac{x}{2}}, & x > 0 \\
    0, & x \leq 0
    \end{cases}
    $$

    图形特征：右偏分布，随着自由度 $n$ 增大，逐渐趋于对称（接近正态分布）。

卡方分布的性质：

- 可加性：若 $Y_1 \sim \chi^2(n_1)$，$Y_2 \sim \chi^2(n_2)$，且 $Y_1, Y_2$ 独立，则 $Y_1 + Y_2 \sim \chi^2(n_1 + n_2)$.（可推广至 $m$ 个独立卡方变量之和）

- 期望与方差：若 $Y \sim \chi^2(n)$，则 $E(Y) = n$,$\text{Var}(Y) = 2n$.

- 卡方分布的上侧 $\alpha$ 分位数：$\chi^2_{\alpha}(n)$ 表示 $\chi^2(n)$ 分布的上侧 $\alpha$ 分位数，可查阅卡方分布表获得。当 $n>40$ 时，可近似为：$\chi^2_{\alpha}(n) \approx \frac{1}{2} \left( z_{\alpha} + \sqrt{2n - 1} \right)^2$

注意：卡方分布满足可加性，但不满足线性性。缩放后的卡方变量不服从卡方分布。

### t 分布

设随机变量 $X \sim N(0,1)$，$Y \sim \chi^2(n)$，且 $X$ 与 $Y$ 相互独立，则称随机变量 $t = \frac{X}{\sqrt{\frac{Y}{n}}}$ 服从自由度为 $n$ 的 t 分布，记作 $t \sim t(n)$.

??? normal-comment "t 分布的概率密度函数"

    t 分布的概率密度函数为：

    $$
    f(t) = \frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n\pi} \, \Gamma\left(\frac{n}{2}\right)} \left(1 + \frac{t^2}{n}\right)^{-\frac{n+1}{2}}, \quad -\infty < t < +\infty
    $$

    图形特征：关于 $t=0$ 对称，形状类似正态分布，但尾部更厚；随着自由度 $n$ 增大，逐渐逼近标准正态分布。

$t(n)$ 分布的上侧 $\alpha$ 分位数记作 $t_{\alpha}(n)$，可查 t 分布表获得。

t 分布的性质：

- 极限性质：$\lim\limits_{n \to \infty} f(t) = \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}} = \varphi(t)$

- 期望与方差：若 $X \sim t(n)$，则 $E(X) = 0$，$Var(X) = \frac{n}{n-2}$.（当 $n \leq 2$ 时，方差不存在；当 $n \leq 1$ 时，期望也不存在）

- 对称性：$t_{1-\alpha}(n) = -t_{\alpha}(n)$

- 大样本近似：当 $n > 45$ 时，t 分布可近似为标准正态分布，$t_{\alpha}(n) \approx z_{\alpha}$.

### F 分布

设随机变量 $X \sim \chi^2(n_1)$，$Y \sim \chi^2(n_2)$，且 $X$ 与 $Y$ 相互独立，则称随机变量 $F = \frac{\frac{X}{n_1}}{\frac{Y}{n_2}}$ 服从自由度为 $(n_1, n_2)$ 的 F 分布，记作 $F \sim F(n_1, n_2)$.

第一自由度为 $n_1$，第二自由度为 $n_2$.

??? normal-comment "F 分布的概率密度函数"

    回顾 Gamma 函数：

    $$
    \Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1} e^{-x} dx \quad (\alpha > 0)
    $$

    定义 Beta 函数：

    $$
    B(a,b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}
    $$

    F 分布的概率密度函数：

    设 $F \sim F(n_1, n_2)$，其概率密度函数为：

    $$
    f(x) =
    \begin{cases}
    \displaystyle \frac{1}{B\left(\frac{n_1}{2}, \frac{n_2}{2}\right)} \cdot \left( \frac{n_1}{n_2} \right)^{\frac{n_1}{2}} \cdot x^{\frac{n_1}{2}-1} \cdot \left(1 + \frac{n_1}{n_2}x\right)^{-\frac{n_1+n_2}{2}}, & x > 0 \\
    0, & x \leq 0
    \end{cases}
    $$

    图形特征：右偏分布，随自由度增大逐渐趋于对称。

$F(n_1,n_2)$ 分布的上侧 $\alpha$ 分位数记作 $F_{\alpha}(n_1, n_2)$，可查 F 分布表获得。F 分布表中通常只提供特定 $\alpha$ 值，如 0.1, 0.05, 0.025, 0.01, 0.005.

F 分布的性质：

- 倒数性质：若 $F \sim F(n_1, n_2)$，则 $\frac{1}{F} \sim F(n_2, n_1)$.

- t 分布与 F 分布的关系：若 $t \sim t(n)$，则 $t^2 \sim F(1, n)$.

- t 分位数与 F 分位数的关系：$\left(t_{\frac{\alpha}{2}}(n)\right)^2 = F_{\alpha}(1, n)$.

- 分位数对称关系：$F_{1-\alpha}(n_1, n_2) = \frac{1}{F_{\alpha}(n_2, n_1)}$.

## 正态总体下的抽样分布

设 $X\sim N(\mu,\sigma^2)$，$\{X_1,X_2,\cdots X_n\}$ 是 $X$ 的样本，则符合正态总体下的抽样分布。

用 $\bar{X}$ 表示样本均值，用 $S^2$ 表示样本方差。

!!! remarks "常用的结论"

    $$\bar{X}\sim N(\mu,\frac{\sigma^2}{n}),\quad \frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{n}}}\sim N(0,1);$$

    $$\frac{(n-1)S^2}{\sigma^2}\sim \chi^2(n-1),\,\text{且}\,\bar{X},S^2\text{相互独立};$$

    $$\frac{\bar{X}-\mu}{\frac{S}{\sqrt{n}}}\sim t(n-1);$$

    $$F=\frac{S_1^2/\sigma_1^2}{S_2^2\sigma_2^2}=\frac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2}\sim F(n_1-1,n_2-1).$$

## 区间估计

定义：

- **置信区间**：设总体 $X$ 的 分布函数中有未知参数 $\theta$，给定值 $\alpha$，有 $P(\theta_1<\theta<\theta_2)\ge 1-\alpha$，则称随机区间 $(\theta_1,\theta_2)$ 为 $\theta$ 的双侧置信区间。其中 $\theta_1$ 为双侧置信下限，$\theta_2$ 为双侧置信上限。
- **置信度**：上述定义中，称 $1-\alpha$ 为置信度。
- **精确度**：置信区间的平均长度 $E(\hat{\theta_2}-\hat{\theta_1})$。
- **误差限**：二分之一区间的平均长度的置信区间。
- **单侧置信限**：$P(\theta_1<\theta)\ge 1-\alpha$，则 $\theta_1$ 为单侧置信下限，$P(\theta<\theta_2)\ge 1-\alpha$，则 $\theta_2$ 为单侧置信上限，$(\theta_1,+\infty)$ 或 $(-\infty,\theta_2)$ 为单侧置信区间。

**奈曼原则**：在置信度达到一定值的前提下，取精确度尽可能高的区间。

**枢轴量**：包含待估计参数 $\theta$、$\theta$ 的点估计等总体信息，但分布已知的函数。通过枢轴量分布的分位数，解不等式可得到 $\theta$ 的置信区间。

常用枢轴量：

1. 正态总体，单变量

| 条件 | 枢轴量 |
| ---- | ------ |
| $\sigma_2$ 已知，求 $\mu$ | $\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$ |

