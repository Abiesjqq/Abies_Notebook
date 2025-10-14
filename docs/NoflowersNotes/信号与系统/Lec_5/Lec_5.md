
我们发现，指数信号经过 LTI 系统之后仍然为指数信号，仅系数发生变化。

例如，$\mathrm{e}^{j \omega t}$ 经过系统 $h(t)$, 结果为


$$
y(t) = \int_{-\infty}^{\infty} \mathrm{e}^{j \omega \tau}h(\tau) \mathrm{d}\tau = \mathrm{e}^{j \omega t} \int_{-\infty}^\infty h(\tau) \mathrm{e}^{-j \omega t}\mathrm{d}t = H(j \omega)\cdot \mathrm{e}^{j \omega t}
$$

我们把 $\displaystyle H(j \omega) = \int_{-\infty}^\infty h(\tau) \mathrm{e}^{-j \omega t}\mathrm{d}t$ 称为 $h(t)$ 的傅里叶变换 (一个与 $t$ 无关的常数)。  
在实际求解中，不用显式地求 $H(s)$, 而是用其它方法求得。

## 信号的频域分解

由上面的思路，将输入 $f$ 分解成指数信号的线性组合，即可更加方便地求得。

平稳的信号 (周期信号) 分解为虚指数信号 $\mathrm{e}^{j \omega t}$ 的组合 --> 傅里叶变换  
截断或者发散的信号 分解为复指数信号 $\mathrm{e}^{st}$ 的组合 --> 拉普拉斯变换

### 周期信号的傅里叶级数展开

周期为 $\displaystyle T = \frac{2\pi}{\omega}$ 的连续时间周期信号 $f$, 可以展开为指数函数集 $\{\exp(jn\omega t)\}, n = 0, \pm 1, \pm 2, \ldots$ 的线性组合，即**指数形式的傅里叶级数** 

$$
\sum_{n = -\infty}^{\infty}C_n \exp(jn\omega t)
$$

该指数函数集具有**正交性**：$\displaystyle \int_T \mathrm{e}^{jn\omega t} \mathrm{e}^{jm\omega t}\mathrm{d} t = \begin{cases}T ,& n = m \\ 0, & n \neq m\end{cases}$

为求 $C_n$, 计算积分

$$
\int_T f(t) \mathrm{e}^{-jn\omega t}\mathrm{d}t = \sum_kC_k \int_T \mathrm{e}^{-jn\omega t} \mathrm{e}^{jk\omega t}\mathrm{d} t = C_nT
$$

即可

!!! remarks "符号解释"
    $\displaystyle \int_T$ 为任意长度为 $T$ 区间上的积分

作为信号，我们称 $\omega$ 为**基波角频率**， $\displaystyle f = \frac{\omega}{2\pi}$ 为**基波频率**， $C_0$ 为**直流分量**  
$n = \pm N$ 的基波频率为 $Nf$, 两项合起来为信号的 $N$ 次谐波分量。

#### 实信号展开为三角形式傅里叶级数

若 $f$ 为实函数，有

$$
\begin{aligned}
f(t) &= C_0 + \sum_{n = 1}^{\infty}C_n \mathrm{e}^{jn\omega t} + \sum_{n = -\infty}^{-1}C_n \mathrm{e}^{jn\omega t} \\
&= C_0 + \sum_{n = 1}^{\infty}\left(C_n \mathrm{e}^{jn\omega t} + C_{-n}\mathrm{e}^{-jn\omega t}\right)
\end{aligned}
$$

令 $\displaystyle C_n = \frac{a_n - jb_n}{2}$，则 $\displaystyle C_{-n} = \frac{a_n + jb_n}{2}$，原式化为

$$
\begin{aligned}
f(t) &= \frac{a_0}{2} + \sum_{n = 1}^{\infty}\left( a_n \cos n \omega t + b_n \sin n \omega t\right) \\
&=\frac{a_0}{2} + \sum_{n = 1}^\infty A_n \cos (n\omega t + \varphi)
\end{aligned}
$$

后者被称为**带初始相位的纯余弦形式**

#### 周期信号可以展开为傅里叶级数的充分条件

**Dirichlet 条件**:  
- 在任何周期内绝对可积  
- 在一个周期内只有有限个有限的不连续点，且这些不连续点的值有限  
- 在一个周期内只有有限个极大值和极小值


