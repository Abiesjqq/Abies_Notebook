

傅里叶变换是以 $\mathrm{e}^{\mathrm{j}\omega t}$ 为基底分解信号。以更一般的 $\mathrm{e}^{st}$ 作为基底对信号进行分解，即为拉普拉斯变换.

## 拉普拉斯变换

对于发散的信号，对其作用一个衰减的指数信号，即可做傅里叶变换. 

即令 $s = \sigma + \mathrm{j}\omega$, 

$$
f(t)\mathrm{e}^{-\sigma t} \overset{F}{\longleftrightarrow} \int f(t)\mathrm{e}^{-\sigma t}\mathrm{e}^{-\mathrm{j}\omega t}\mathrm{d}t = \int f(t)\mathrm{e}^{-s t}\mathrm{d}t = F(s)
$$

称 $F(s)$ 为 $f(t)$ 的拉普拉斯变换，记作 $\displaystyle f(t) \overset{L}{\longleftrightarrow} F(s)$

!!! normal-comment "注释"
    相当于给傅里叶变换增加了一个维度，$\mathrm{j}\omega \to \sigma + \mathrm{j}\omega$，也相当于 $t \to (\sigma, \omega)$  
    我们把 $f(t)$ 称为**原函数**，把 $F(s)$ 称为**像函数**  
    $s$ 被称为**复频率**, $F(s)$ 为**复频谱**.

同样有反变换 ($s = \sigma + \mathrm{j}\omega$)

$$
\begin{aligned}
    &f(t)\mathrm{e}^{-\sigma t} = \frac{1}{2\pi}\int F(s)\mathrm{e}^{\mathrm{j}\omega t} \mathrm{d}\omega \\
    \Leftrightarrow\  & f(t) = \frac{1}{2\pi}\int F(s)\mathrm{e}^{st}\mathrm{d}\omega = \frac{1}{2\pi \mathrm{j}}\int_{\sigma - \mathrm{j}\infty}^{\sigma + \mathrm{j}\infty} F(s)\mathrm{e}^{st}\mathrm{d}s
\end{aligned}
$$

!!! normal-comment "注意"
    这是一个线积分！平时不怎么会用做这个方法求该积分.

### 单边拉普拉斯变换

对于因果信号和因果系统，使用单边拉普拉斯变换更为方便. 对于一般的实指数信号，其傅里叶变换不能在整个实轴上发生, 因此取单边 (?)

$$
F(s) = \int_{0^-}^{\infty}f(t)\mathrm{e}^{-st}\mathrm{d}t
$$

$$
f(t) = \frac{1}{2\pi \mathrm{j}}\int_{\sigma - \mathrm{j}\infty}^{\sigma + \mathrm{j}\infty} F(s)\mathrm{e}^{st}\mathrm{d}s
$$

这里取 $0$ 是为了考虑到初始条件

### 拉普拉斯变换的收敛条件和收敛域

单边拉普拉斯变换存在的充要条件: 存在 $\sigma$ 满足

$$
\int_{0^-}^\infty\vert f(t)\vert \mathrm{e}^{-\sigma t}\mathrm{d}t < \infty \Rightarrow \lim_{t \to \infty}f(t)\mathrm{e}^{-\sigma t} = 0,\ \sigma > \sigma_0
$$

$\sigma_0$ 为所有 $\sigma$ 的下界, $\sigma > \sigma_0$ 称为收敛条件, $\sigma_0$ 称为绝对收敛坐标. 所有满足收敛条件的 $s$ 构成**收敛域** (ROC)

!!! examples "例题"

    求 $f(t) = \mathrm{e}^{-t}u(t)$, $g(t) = -\mathrm{e}^{-t}u(-t)$ 的 L 变换

    $$
    \begin{aligned}
        f(t) &\overset{L}{\longleftrightarrow} F(s) = \int_0^\infty\mathrm{e}^{-(1 + s)t}\mathrm{d}t = \frac{1}{s + 1}, &\quad \mathrm{Re}(s) > -1 \\
        g(t) &\overset{L}{\longleftrightarrow} X(s) = -\int_{-\infty}^0\mathrm{e}^{-(1 + s)t}\mathrm{d}t = \frac{1}{s + 1}, &\quad \mathrm{Re}(s) < -1
    \end{aligned}
    $$

    由此可见，拉普拉斯变换表达式和原信号并非一一对应. 但是**包含收敛域**的拉普拉斯变换和信号一一对应

    若收敛域包含虚轴，则原信号具有傅里叶变换.

!!! remarks "有理像函数的零极点图"

    若 $\displaystyle X(s) = M\frac{\prod(s - \beta_i)}{\prod(s - \alpha_i)}$, 分子多项式的根称为**零点**，分母多项式的根称为**极点**.  
    将 $X(s)$ 的全部零点和极点标注在 $s$ 平面上构成零极点图，零极点图及其收敛域可以表示一个 $X(s)$, 与其本身仅相差一个 $M$. (类似于傅里叶变换的 $\vert H(\mathrm{j}\omega) \vert$ 的图像)

    !!! examples "例子"

        $$
        x(t) = \mathrm{e}^{-t}u(t) + \mathrm{e}^{-2t}u(t) \overset{L}{\longleftrightarrow} \frac{1}{s + 1} + \frac{1}{s + 2} = \frac{2s + 3}{(s + 1)(s + 2)}
        $$

        有零极点图

        ![alt text](image.png)

    有性质:  
    - L 变换为有理函数时，收敛域内不包含任何极点  
    - 因果信号的收敛于在收敛轴的右边且不包含  
    - 对于有限持续时间的信号，若存在 L 变换，则其收敛域为整个 $s$ 平面

!!! remarks "常用信号的拉普拉斯变换"

**指数函数**