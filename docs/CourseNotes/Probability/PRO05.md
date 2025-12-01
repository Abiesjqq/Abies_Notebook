## 大数定理

### 依概率收敛

设 $Y_1, \ldots, Y_n, \ldots$（或用 $\{Y_n, n \geq 1\}$ 记）为一个随机变量序列，$c$ 为常数量，若对于 $\forall \varepsilon > 0$，均有 $\lim_{n \to +\infty} P\left\{ |Y_n - c| \geq \varepsilon \right\} = 0$ 或 $\lim_{n \to +\infty} P\left\{ |Y_n - c| < \varepsilon \right\} = 1$ 成立，则称随机变量序列 $\{Y_n, n \geq 1\}$ 依概率收敛于 $c$，记为：

$$
Y_n \xrightarrow{P} c, \text{当 } n \to +\infty.
$$

若 $X_n \xrightarrow{P} a, Y_n \xrightarrow{P} b$，则有

- $X_n + Y_n \xrightarrow{P} a+b$
- $X_n \times Y_n \xrightarrow{P} ab$
- $X_n / Y_n \xrightarrow{P} \frac{a}{b}$
- $X_ne^{Y_n} \xrightarrow{P} ae^b$

<!-- !!! normal-comment ""

    依概率收敛的作用对象为随机变量序列，收敛条件为随机变量取值的概率趋向于 1。 -->

### 马尔可夫不等式

设随机变量 $Y$ 的 $k$ 阶矩 $E(Y^k)$ 存在 ($k \geq 1$)，则对于任意 $\varepsilon > 0$，都有：

$$
P\left\{ |Y| \geq \varepsilon \right\} \leq \frac{E(|Y|^k)}{\varepsilon^k}
$$

成立；

定理的等价形式为：

$$
P\left\{ |Y| < \varepsilon \right\} \geq 1 - \frac{E(|Y|^k)}{\varepsilon^k}.
$$

特别地，当 $Y$ 为取非负值的随机变量时，则有

$$
P\left\{ Y \geq \varepsilon \right\} \leq \frac{E(Y^k)}{\varepsilon^k}
$$

### 切比雪夫不等式

设随机变量 $X$ 具有数学期望 $E(X) = \mu$，方差 $Var(X) = \sigma^2$，则对于任意 $\varepsilon > 0$，都有：

$$
P\left\{ |X - \mu| \geq \varepsilon \right\} \leq \frac{\sigma^2}{\varepsilon^2};
$$

定理的等价形式为：

$$
P\left\{ |X - \mu| < \varepsilon \right\} \geq 1 - \frac{\sigma^2}{\varepsilon^2}.
$$

### 大数定律定义

设 $Y_1, \ldots, Y_n, \ldots$ 为一个随机变量序列，若存在常数序列 $\{c_n, n \geq 1\}$，使得对 $\forall \varepsilon > 0$，均有：

$$
\lim_{n \to +\infty} P\left\{ \left| \frac{1}{n} \sum_{i=1}^{n} Y_i - c_n \right| \geq \varepsilon \right\} = 0,
\quad \text{或} \quad
\lim_{n \to +\infty} P\left\{ \left| \frac{1}{n} \sum_{i=1}^{n} Y_i - c_n \right| < \varepsilon \right\} = 1
$$

成立，即有当 $n \to +\infty$，

$$
\frac{1}{n} \sum_{i=1}^{n} Y_i \xrightarrow{P} c_n
$$

则称随机变量序列 $\{Y_i, i \geq 1\}$ 服从（弱）大数定律。

说明： 若令 $Z_n = \frac{1}{n} \sum_{i=1}^{n} Y_i$，当 $n \to \infty$，$Z_n$ 依概率收敛于 $c$。

随机变量序列前 $n$ 个变量的算术平均依概率收敛于 $c$，则这个随机变量序列服从大数定律。

### 贝努里大数定律

设 $n_A$ 为 $n$ 重贝努里试验中事件 $A$ 发生的次数，并记事件 $A$ 在每次试验中发生的概率为 $p$，则对 $\forall \varepsilon > 0$，有：

$$
\lim_{n \to +\infty} P\left\{ \left| \frac{n_A}{n} - p \right| \geq \varepsilon \right\} = 0 \quad (n_A \text{ 为 } n \text{ 个 } 0\text{-}1 \text{ 分布变量之和})
$$

### 辛钦大数定律

设 $\{X_i, i \geq 1\}$ 为独立同分布的随机变量序列，且其期望存在，记为 $\mu$，则对 $\forall \varepsilon > 0$，有：

$$
\lim_{n \to \infty} P\left\{ \left| \frac{1}{n} \sum_{k=1}^{n} X_i - \mu \right| \geq \varepsilon \right\} = 0,
$$

即随机变量序列 $\{X_i, i \geq 1\}$ 服从大数定律，也即，当 $n \to +\infty$ 时，

$$
\frac{1}{n} \sum_{i=1}^{n} X_i \xrightarrow{P} \mu
$$

**推论：**

设 $\{X_i, i \geq 1\}$ 为独立同分布的随机变量序列，若 $h(x)$ 为连续函数，且 $E|h(X_1)| < +\infty$，则对 $\forall \varepsilon > 0$，有：

$$
\lim_{n \to \infty} P\left\{ \left| \frac{1}{n} \sum_{i=1}^{n} h(X_i) - E(h(X_1)) \right| \geq \varepsilon \right\} = 0,
$$

即随机变量 $\{h(X_i), i \geq 1\}$ 也服从大数定律，即

$$
\frac{1}{n} \sum_{i=1}^{n} h(X_i) \xrightarrow{P} E(h(X_1))
$$

若 $X_1, X_2, \cdots, X_n$ 为独立同分布的，$h(x)$ 为连续函数，则 $h(X_1), h(X_2), \cdots, h(X_n)$ 也为独立同分布的。

## 中心极限定理

### 独立同分布的中心极限定理

设随机变量 $X_1, X_2, \ldots, X_n, \ldots$ 相互独立同分布，当 $n$ 充分大时，$Y_n$ 近似服从 $N(0,1)$，即

$$\sum_{i=1}^nX_i\sim N(n\mu, n\sigma^2)$$

### 德莫弗-拉普拉斯定理

设 $n_A$ 为 $n$ 重贝努里试验中 $A$ 发生的次数，$P(A) = p$ ($0 < p < 1$)，则 $\forall x \in \mathbb{R}$，有：

$$
\lim_{n \to +\infty} P\left( \frac{n_A - np}{\sqrt{np(1-p)}} \leq x \right)
= \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}} dt = \Phi(x),
$$

即若 $n$ 足够大，$n_A \sim B(n, p)$，则

$$n_A \sim N(np, npq)$$
