

!!! remarks "微分方程和特征根"
    对于 $\displaystyle \sum a_n \frac{\mathrm{d}^n y}{\mathrm{d}t^n} = C$, 对应特征方程 $\displaystyle \sum a_ns^n = 0$, 其解 $s_1, \cdots, s_n$, 得齐次解解 $\displaystyle y = \sum A_n \mathrm{e}^{s_n t}$, $A_n$ 由初始条件决定，再代入由 $C$ 确定特解，最后解为 **齐次解** + **特解**

## 利用 LTI 系统的特性

输出响应由两部分组成：  
- 初始状态为 0 时、完全由输入信号 $f(t)$ 决定的系统响应 — **零状态响应** $y_f(t)$ (强迫响应)  
- 输入信号为 0 时、完全由初始状态 $y^{n}(0-)$ 决定的系统响应 — **零输入响应** $y_x(t)$ (自由响应)  

其中**零输入响应**能直接通过齐次微分方程求得 (只与初始值有关)，但是**零状态响应**与变化的 $f(t)$ 有关，不易求得。因此可以先将 $f(t)$ 分解后求

在时域中，常用冲激信号作为基本单元信号 — **时域分析方法** (常用卷积，也称卷积法)
在频域/复频域中，使用指数信号作为基本带院信号 — **频域分析方法** (使用傅里叶变换)

## 利用单位冲激信号的线性组合分解

### 连续时间系统

先求零状态响应

冲激响应: 冲激信号激励系统时产生的零状态响应，记为 $h(t)$.

根据定义，$h(t)$ 满足：

$$
h^{(n)}(t) + a_{n - 1}h^{(n - 1)}(t) + \cdots + a_0h(t) = b_m\delta^{(m)}(t) + \cdots + b_0\delta(t)
$$

显然 $t > 0^+$ 时 $h(t)$ 是其次微分方程的解.

$$
h(t) = \left( \sum_{i=1}^n K_i \, \mathrm{e}^{s_i t} \right) u(t)
$$

$n \leq m$ 时, 为使方程两边平衡, $h(t)$ 应含有冲激及其高阶导数，即

$$
h(t) = \left( \sum_{i=1}^n K_i \, \mathrm{e}^{s_i t} \right) u(t) + \sum_{j=0}^{m-n} A_j \, \delta^{(j)}(t)
$$

$h(t)$ 代入配平即可.

由此得

$$
T(f(t)) = y_f(t) = \int_{-\infty}^{\infty}f(\tau)h(t - \tau)\mathrm{d} \tau = f(t) \otimes h(t)
$$

零输入响应仅需求解其次微分方程即可

**完全响应** = 零状态响应 + 零输入响应

!!! remarks "卷积积分的计算与性质"
    定义 $\displaystyle y(t) = f(t) \otimes h(t) = \int_{-\infty}^{\infty}f(\tau)h(t - \tau) \mathrm{d} \tau$
    
    两个方波信号卷积，得到结果为梯形，底边长为方波宽度的和，上边长为方波信号宽度的差
    
    理解： $\tau$ 作用时刻，$t$ 观察时刻，积分：所有作用时刻响应的叠加
    
    因果信号中，积分上下限可以换为 $[0, t]$
    
    !!! examples "几个例子"

        $$
        u(t) \otimes u(t) = r(t)
        $$  

        $$
        \displaystyle \mathrm{e}^{\alpha t}\otimes \mathrm{e}^{\beta t} = \begin{cases}\displaystyle \frac{\mathrm{e}^{\alpha t} - \mathrm{e}^{\beta t}}{\alpha - \beta}u(t) &\ \alpha \neq \beta \\ t\mathrm{e}^{\alpha t}u(t) &\ \alpha = \beta  \end{cases}
        $$
    
    有一些性质：  
    1. **交换律** $\displaystyle f(t) \otimes h(t) h(t) \otimes f(t)$
        可用系统作用 $f(t)$ 角度理解，同时表明 $h(t), f(t)$ 均能表示为冲激响应作为系统的描述； LTI 系统级联时可以交换先后顺序    
       2. **分配律** $x(t) \otimes (h_1(t) + h_2(t)) = x(t) \otimes h_1(t) + x(t)\otimes h_2(t)$  
           并联系统能分别计算并相加  
       3. **结合律** (公式略)
           级联系统的冲激响应等于格构成系统冲激响应的卷积  
       4. **与奇异信号的卷积** (最好用系统来理解)  
           - 直连系统 $x(t) \otimes \delta(t) = x(t)$  
           - 延时特性 $x(t )\otimes \delta (t - T) = x(t - T)$    
           - 微分特性 $x(t) \otimes \delta'(t) = x'(t)$  
           - 积分特性 $\displaystyle x(t) \otimes u(t) = \int_{-\infty}^{t}x(\tau) \mathrm{d}\tau$  
       5. 一些性质的组合
           - $x'(t) \otimes h(t) = x(t) \otimes h'(t) = y'(t)$，积分延时等相同.  
           - 可以先微分成冲激信号再积分方便求得  

### 离散时间系统

零输入响应直接求齐次差分返程即可。

!!! warning-box "初始条件"
    如果初始条件给的是 $y[0], y[1]$, 需要注意在此时激励信号已经作用了，不能直接用于计算零输入响应！  
    此时需要重新计算 $y[-1], y[-2]$ 用于求解零输入响应。

现求零状态响应，使用卷积法。  
同样仅需计算单位脉冲 (样值/样本) 响应即可。同样有

> 这里 $\delta$ 叫**单位样值序列**

$$
f[k] = \sum_{n = -\infty}^{\infty}f[n]\delta[k - n] \Rightarrow \sum_{n = -\infty}^{\infty}f[n]h[k - n] = f[k] \otimes h[k]
$$

$h[k]$ 满足:

$$
\sum_{i = 1}^{n}a_i \delta[k - i] = \sum_{i = 1}^{m}b_i h[k - i]
$$

先计算关于 $h$ 的齐次差分方程，再由 $h[k | k \leq -1] = 0$ 得到 $h[k]$ 的形式。

!!! remarks "卷积和的运算和性质"
    不过多赘述，和上面卷积积分类似  
    计算卷积 $f[k] \otimes h[k]$时，可以把 $f[k]$ 写成单位样值序列，在卷积之后把 $\delta$ 换成 $h$ 即可。

    例子：

    $$
    \alpha^k u[k] \otimes \beta^k u[k]
    $$

## 反馈系统的冲激响应和系统特性分析

反馈系统需要列方程求解，但是需要求含有卷积的方程！ --> **频域分析方法** (下次讲)

对一个系统 $y(t) = a + b \mathrm{e}^{\alpha t} + c \mathrm{e}^{\beta t}$, 有：  
- **固有响应**为 $b \mathrm{e}^{\alpha t} + c \mathrm{e}^{\beta t}$  
- **强迫响应**为 $a$  
- **稳态响应**为 $a$ (不随时间衰减到 $0$)  
- **暂态响应**为 $b \mathrm{e}^{\alpha t} + c \mathrm{e}^{\beta t}$ (与上面相反)



