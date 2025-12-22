
类似 L 变换，我们可以将发散的离散时间信号乘以一个缩放的指数因子，再进行离散的傅里叶变换；  
或者，对连续信号的 L 变换，对其进行采样，即可得到离散信号的 z 变换。

## z 变换的定义

我们希望把 $f[n]$ 分解为 $f[n] = \sum_n a_n z^n$, 即有 $z$ 变换的表达式

$$
X(z) = \sum_{n} x[n]z^{-n}
$$

其中 $z$ 是一个复数变量，常写为 $z = r\mathrm{e}^{\mathrm{j}\omega}$  
分为单边和双边:

$$
\begin{aligned}
    X(z) = \sum_{n = -\infty}^\infty x[n]z^{-n} \\
    X(z) = \sum_{n = 0}^\infty x[n]z^{-n}
\end{aligned}
$$

!!! remarks "转换成傅里叶变换"

    $$
    X(r\mathrm{e}^{\mathrm{j}\omega}) = \sum_n (x[n]r^{-n})\mathrm{e}^{-\mathrm{j}\omega n} = \operatorname{DTFT}(x[n]r^{-n})
    $$

### z 变换和 L 变换的关系

采样 

$$
x_s(t) = x(t)\delta_T(t) = \sum x(nT)\delta(t - nT), \quad x[n] = x(nT)
$$

对 $x_S(t)$ 进行单边 L 变换，

$$
\begin{aligned}
    X_s(s) = \sum_{n = 0}^\infty x(nT)\mathrm{e}^{-nTs}
\end{aligned}
$$

这里取 $z = \mathrm{e}^{sT} = \mathrm{e}^\sigma \cdot \mathrm{e}^{\mathrm{j}\omega}$ 即得 $z$ 变换表达式

L 变换中 $s$ 平面上的虚轴映射为 z 平面的单位圆，负无穷映射为 z 平面的原点。

### z 变换的收敛域

一个显然的充分条件：存在 $r$, 

$$
\sum_n \lvert x[n]r^{-n}\rvert \leq \infty
$$

由上面的对应关系，可以知道变换后为有理分式的收敛域为以原点为圆心的圆环构成的环带结构，且收敛域中不会包含任何极点。  
因果序列的收敛域在极点所在圆的外侧，非因果序列的收敛域在极点所在圆的内侧。

!!! examples "例子"

$x[n] = a^n u[n]$ z 变换收敛要求 $|z| > |a|$，为半径为 $|a|$ 的圆的外围，$\displaystyle X(z) = \frac{z}{z - a}$

$x[n] = -a^n x[-n - 1]$:

$$
X(z) = -\sum_{n = -\infty}^{-1}a^nz^{-n} = -\sum_{n = 1}^\infty \left(\frac{z}{a}\right)^n = \frac{z}{z - a}, \quad |z| < |a|
$$

| 序列类型        | 序列范围                      | 收敛域                              |
| ----------- | ------------------------- | -------------------------------- |
| 有限长度序列      | $N_1<0,N_2>0$            | $0<\lvert z\rvert<\infty$        |
| 有限长度序列（因果）  | $N_1\ge0,N_2>0$          | $0<\lvert z\rvert\le\infty$      |
| 有限长度序列（非因果） | $N_1<0,N_2\le0$          | $0\le\lvert z\rvert<\infty$      |
| 右边序列        | $N_1<0,N_2=\infty$       | $R_{x1}<\lvert z\rvert<\infty$   |
| 右边序列（因果）    | $N_1\ge0,N_2=\infty$     | $R_{x1}<\lvert z\rvert\le\infty$ |
| 左边序列        | $N_1=-\infty,N_2>0$      | $0<\lvert z\rvert<R_{x2}$        |
| 左边序列（非因果）   | $N_1=-\infty,N_2\le0$    | $0\le\lvert z\rvert<R_{x2}$      |
| 双边序列        | $N_1=-\infty,N_2=\infty$ | $R_{x1}<\lvert z\rvert<R_{x2}$   |

!!! remarks "常用信号的 z 变换"

    **单位取样序列** $\mathcal{Z}(\delta[n]) = 1$, $0 \leq |z| \leq +\infty$  
    **单位阶跃序列** $\displaystyle \mathcal{Z}(u[n]) = \frac{z}{z - 1}$, $|z| > 1$ （因果）; $\mathcal{Z}(u[-1 - n]) = \frac{z}{z - 1}$, $|z| < 1$ （非因果）  
    **斜变序列** $\displaystyle \mathcal{Z}(n\cdot u[n]) = \frac{z}{(z - 1)^2}$, $|z| > 1$ （计算时对单位阶跃信号表达式求导进行计算）  
    **单边指数序列** $\displaystyle \mathcal{Z}(a^nu[n]) = \frac{z}{z - a}$, $|z| > |a|$  
    **双边指数序列** $\displaystyle \mathcal{Z}(b^{|n|}) = \frac{z(b - b^{-1})}{(z - b)(z - b^{-1})}$, $|b| < |z| < |b^{-1}|, |b| < 1$  
    **正余弦序列** $\displaystyle \mathcal{Z}(\cos (\omega_0 n)u[n]) = \frac{1}{2}\left(\frac{z}{z - \mathrm{e}^{\mathrm{j}\omega_0}} + \frac{z}{z - \mathrm{e}^{-\mathrm{j}\omega_0}}\right) = \frac{z(z - \cos \omega_0)}{z^2 -2z \cos \omega_0 + 1}$, $|z| > 1$, $\mathcal{Z}(\sin (\omega_0 n)u[n]) = \dfrac{z \sin \omega_0}{z^2 - 2z \cos \omega_0 + 1}$

## z 变换的性质

### 线性性

类似 L 变换，但是零极点如果抵消，收敛域会变大

### 位移性质

离散时间系统的位移相当于连续时间系统的时移 + 微积分

对于双边 z 变换，$\mathcal{Z}(x[n - m]) = z^{-m}X(z)$, 证明按定义展开即可；在 $z = 0$ 和无穷处零极点情况可能会发生变化

对于单边 z 变换，根据定义，_向右平移时_

$$
\mathcal{Z}(x[n - m]u[n]) = z^{-m}X(z) + \sum_{k = 1}^m x[-k]z^{k - m}
$$

也即会有新参与 z 变换的项的加入；在 $z = 0$ 处增加了 $m$ 重极点

_向左平移时_

$$
\mathcal{Z}(x[n + m]u(n)) = z^m\left(X(z) - \sum_{k = 0}^{m - 1}x[k]z^{-k}\right)
$$

也即有部分项不再参与 z 变换；在 $z = 0$ 处增加了 $m$ 重零点。

证明同样将单边 z 变换定义即可求得。

### 频移性质

$$
\mathcal{Z}(z_0^nx[n]) = \sum_n x \left(\frac{z}{z_0}\right)^n = X\left(\frac{z}{z_0}\right), \quad R_{x_1} < \left|\frac{z}{z_0}\right| < R_{x_2}
$$

!!! examples "一些例子"

    $z_0 = \mathrm{e}^{\mathrm{j}\omega_0}$ 时，变成 $X(\mathrm{e}^{-\mathrm{j}\omega_0}z)$, 特别的, $z_0 = -1$ 时，$X(z)$ 绕原点旋转了 $180^\circ$  
    $z_0$ 是正实数时，收敛域以系数 $a$ 缩放。（注意不是 $\dfrac{1}{a}$！！因为是函数 $X$ 括号内的东西进行对应）

### 时间反转

对于双边 z 变换，$\mathcal{Z}(x[-n]) = X\left(\dfrac{1}{z}\right)$

### z 域微分

$$
\frac{\mathrm{d}X(z)}{\mathrm{d}z} = -z^{-1}\sum_n nx[n]z^{-n} = -z^{-1}\mathcal{Z}(nx[n])
$$

因此

$$
\mathcal{Z}(nx[n]) = -z \frac{\mathrm{d}X(z)}{\mathrm{d}z}
$$

收敛域不变，在可能原点引入一个极点（因为可能会和零点抵消）

### 卷积定理

与 L 变换相同，不做描述

!!! examples "一个例题"

    求 $x_1[n] = a^nu[n], x_2[n] = b^nu[n]$, 求二者卷积.

    进行 z 变换并相乘，有 

    $$
    X(z) = \dfrac{z^2}{(z - a) (z - b)} = \dfrac{1}{a - b}\left(\frac{az}{z - a} - \frac{bz}{z - b}\right)
    $$

    因此卷积结果为 $\dfrac{1}{a - b}(a^{n + 1} - b^{n + 1}) u[n]$

### 共轭性质

$\mathcal{Z}(\overline{x[n]}) = \overline{X(\overline{z})}$ 零极点共轭。  
因此实信号的零极点一定是共轭的。

!!! warning-box "零极点共轭的信号不一定是实信号！"



### 初值定理

