
## 连续时间系统的系统函数

系统在零状态条件下，输出信号的拉氏变换式与输入信号的拉式变换式之比，称为**系统函数**，记为 $H(s)$

$$
H(s) = \frac{Y(s)}{X(s)}
$$

类似傅里叶变换，可以通过微分方程直接写出系统函数，这里不再重复

## 系统函数与系统特性

### 零极点图与系统特性

**$\sigma$ 轴的单极点** $\displaystyle H(s) = \frac{1}{s - \alpha } \overset{L^{-1}}{\longleftrightarrow}\mathrm{e}^{\alpha t}u(t)$ 为实指数信号  

**共轭单极点** 看图 ![alt text](image.png){ style="width:50%" }  
$\displaystyle H(s) = \frac{\omega}{(s - \alpha )^2 + \omega^2}\overset{L^{-1}}{\longleftrightarrow} \sin \omega t\ \mathrm{e}^{\alpha t}u(t)$, 极点 $p_{1, 2} = \alpha \pm \mathrm{j}\omega$

#### 零极点和系统因果性

如果 $H(s)$ 是**有理函数**，则系统为因果系统的充分必要条件是 $H(s)$ 的收敛域是 s 域的某个右半平面。

#### 零极点和系统稳定性

连续时间线性时不变系统稳定的充要条件是其在实数域上绝对可积，因此  
因果系统在 s 域稳定的充要条件是系统函数 $H(s)$ 的全部极点位于 s 平面的左半平面。

#### 零极点与系统频响特性

由于

$$
H(\mathrm{j}\omega) = K\frac{ \prod_{i = 1}^m(\mathrm{j}\omega - z_i)}{ \prod_{i = 1}^n(\mathrm{j}\omega - p_i)}
$$

有

$$
\begin{aligned}
    \vert H(\mathrm{j}\omega)\vert &= K\frac{ \prod_{i = 1}^m|\mathrm{j}\omega - z_i|}{ \prod_{i = 1}^n|\mathrm{j}\omega - p_i|} \\
    \phi(\mathrm{j}\omega) &= K\left( \sum_{i = 1}^m\operatorname{Arg}(\mathrm{j}\omega - z_i)- \sum_{i = 1}^n\operatorname{Arg}(\mathrm{j}\omega - p_i)\right)
\end{aligned}
$$

可以在零极点图中通过观察在 $\omega$ 变化时各个差矢量的模长之积/商来判断频响变化

!!! examples "例子"

    ![alt text](image-1.png)

!!! examples "超级例题"

    ![alt text](image-2.png)

## L 变换与微分方程

给定系统微分方程

$$
\frac{\mathrm{d}^2 r(t)}{\mathrm{d}t^2} + 3\frac{\mathrm{d}r(t)}{\mathrm{d}t} + 2r(t) = \frac{\mathrm{d}u(t)}{\mathrm{d}t} + 3u(t)
$$

进行分析 (初始条件 $r(0^-) = 1, r'(0^-) = 2$)

两边进行拉普拉斯变换，有

$$
s^2R(s) - sr(0^-) - r'(0^-) + 3(sR(s) - r(0^-)) + 2R(s) = sU(s) - u(0^-) + 3U(s)
$$

解得

$$
R(s) = \frac{(s + 3)U(s)}{s^2 + 3s + 2} + \frac{(s + 3)r(0^-) + r'(0^-)}{s^2 + 3s + 2}
$$

**零输入响应**

$$
\begin{aligned}
    R_{\mathrm{zi}}(s)& = \frac{(s + 3)r(0^-) + r'(0^-)}{s^2 + 3s + 2} = \frac{4}{s + 1} - \frac{3}{s + 2} \\
    r_{\mathrm{zi}}(t) &= \left(4\mathrm{e}^{-t} - 3\mathrm{e}^{-2t}\right)u(t)
\end{aligned}
$$

**零状态响应**

$$
\begin{aligned}
    R_{\mathrm{zs}}(s)& = \frac{(s + 3)U(s)}{s^2 + 3s + 2} = \frac{3}{2s} - \frac{2}{s + 1} + \frac{1}{2(s + 2)}, \quad U(s) = \frac{1}{s} \\
    r_{\mathrm{zs}}(t) &= \left(\frac{1}{2}\mathrm{e}^{-2t} - 2\mathrm{e}^{-t} + \frac{3}{2}\right)u(t)
\end{aligned}
$$

**完全响应**

$$
\begin{aligned}
    R(s) &= \frac{(s + 3)U(s)}{s^2 + 3s + 2} + \frac{(s + 3)r(0^-) + r'(0^-)}{s^2 + 3s + 2} = \frac{3}{2s} + \frac{2}{s + 1} - \frac{5}{2(s + 2)} \\
    r_{\mathrm{zs}}(t) &= \left(-\frac{5}{2}\mathrm{e}^{-2t} + 2\mathrm{e}^{-t} + \frac{3}{2}\right)u(t)
\end{aligned}
$$

**瞬(暂)态响应和稳态响应** 会随时间增长消失的部分为瞬态响应

虚轴左边的极点产生的函数项，对应于瞬态响应；虚轴及虚轴右边的极点产生的函数项，对应于稳态响应

**自由响应和强迫响应** 自由响应只由系统本身决定

系统函数的极点 --> 自由响应分量；激励函数的极点 --> 强迫响应的分量  
当激励信号的极点和系统函数的极点重合，即会发生**谐振** $\left(\displaystyle \frac{1}{s^2} \overset{L^{-1}}{\longleftrightarrow} t\cdot u(t)\right)$  
$H(s)$ 零、极点相消时，某些频率分量将丢失

!!! examples "几个例题"

    ![alt text](image-3.png)  
    ![alt text](image-4.png)

## 连续线性时间系统的框图描述

### 基本构成单元

**加法器** $y(t) = x_1(t) + x_2(t); Y(s) = X_1(s) + X_2(s)$  
![alt text](image-5.png)

**标量乘法器** $y(s) = a\cdot x(t); Y(s) = a\cdot X(s)$  
![alt text](image-6.png)

**积分器** $\displaystyle y(t) = \int_{-\infty}^t x(\tau) \mathrm{d}\tau$ 或 $\displaystyle y(t) = \int_{0^-}^t x(\tau) \mathrm{d}\tau; Y(s) \frac{X(s)}{s}$ (不用考虑初值)  
![alt text](image-7.png)

上述元件为构成 LTI 的所有常用基本单元

### 基本组合方式

系统的基本组合连接方式有串联、并联和反馈环路

**串联并联**  

![alt text](image-8.png){ style="width:50%;" }
![alt text](image-9.png){ style="width:50%;" }

**反馈环路**

![alt text](image-10.png){ style="width:50%;" }

$$
\begin{cases}
    E(s) = F(s) - \beta(s)Y(s) \\
    Y(s) = E(s)K(s)
\end{cases}
$$

怎样计算系统函数？得到 $\displaystyle Y = \frac{K}{1 + \beta K}F$, 因此

$$
H(s) = \frac{K(s)}{1 + \beta(s)K(s)}
$$

!!! examples "例子"

    求 $\displaystyle H(s) = \frac{1}{s + a_0}$ 的系统框图

    先将 $s$ 化为 $s^{-1}$, 得 $\displaystyle H(s) = \frac{s^{-1}}{1 + a_0\cdot s^{-1}}$  
    对比反馈环路表达式，得 $K(s) = s^{-1}, \beta(s) = a_0$

    !!! normal-comment "注意"
        用积分器而不是微分器，因为微分器受噪声影响比较大、不稳定，实际中应用比较少

### 高阶 LTI 系统的框图模拟

系统函数形为

$$
H(s) = \frac{b_ms^m + \ldots + b_0}{s^n + a_{n - 1}s^{n - 1} + \ldots + a_0}, \quad n \geq m
$$

**直接法** 变成 $s^{-1}$ 积分器形式，然后分成分子分母

$$
\begin{aligned}
    &H(s) = \frac{Y(s)}{X(s)} = \frac{Y(s)}{E(s)}\cdot \frac{E(s)}{X(s)}, \quad E(s) = 1 \\
    & H(s) = \frac{b_ms^{-(n - m)} + \ldots + b_0s^{-n}}{1 + a_{n - 1}s^{-1} + \ldots + a_0s^{-n}}
\end{aligned}
$$

表示为

$$
\begin{cases}
    \displaystyle Y(s) = \left(b_ms^{-(n - m)} + \ldots + b_0s^{-n}\right)E(s) \\
    \displaystyle E(s) = X(s) - \left(a_{n - 1}s^{-1} + \ldots + a_0s^{-n}\right)E(s)
\end{cases}
$$

第一个式子为正项的积分器和加法器叠加；第二个式子为反馈回路。

!!! examples "例子"

    ![alt text](image-11.png)

**串联法** 将 $H(s)$ 分级为若干个一阶或二阶相乘的形式

$$
H(s) = K \prod_{i}(s - p_i)\left(k + \frac{l}{s}\right)\left[\prod_i (s - q_i)\right]^{-1}
$$

即化为 一阶微分 + 积分器 + 反馈回路的串联 

**并联法** 将 $H(s)$ 分为若干一阶（积分器）二阶（反馈）相加的形式

$$
H(s) = \sum \frac{a_i}{s^{-1}} + \sum \frac{b_i s^{-1}}{1 + c_i s^{-1}}
$$