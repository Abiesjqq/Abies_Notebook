
## 连续系统的频率响应

对于系统 $y_f(t) = T(f(t))$, 显然有

$$
Y_f(\mathrm{j}\omega) = H(\mathrm{j}\omega)F(\mathrm{j}\omega)
$$

我们把 $H(\mathrm{j}\omega)$ 称为 LTI 系统的频率响应。  
取 $H(\mathrm{j}\omega) = \vert H(\mathrm{j}\omega) \vert \cdot \mathrm{e}^{\mathrm{j}\theta(\omega)}$，两者分别称为 **幅度响应**和**相位响应**

显然有 $H(\mathrm{j}\omega) = F(H(t))$

### 频率响应与时域微分方程的关系

由系统的微分方程

$$
C_0 \frac{\mathrm{d}^n y(t)}{\mathrm{d}t^n}
+ \cdots
+ C_n y(t)
= E_0 \frac{\mathrm{d}^m f(t)}{\mathrm{d}t^m}
+ \cdots
+ E_m f(t)
$$

两边同时傅里叶变换，并利用傅里叶变换的时域微分特性

$$
\begin{aligned}
&\bigl[
C_0 (\mathrm{j}\omega)^n
+ C_1 (\mathrm{j}\omega)^{n-1}
+ \cdots
+ C_{n-1} \mathrm{j}\omega
+ C_n
\bigr] Y(\mathrm{j}\omega) \\
=
&\bigl[
E_0 (\mathrm{j}\omega)^m
+ E_1 (\mathrm{j}\omega)^{m-1}
+ \cdots
+ E_{m-1} \mathrm{j}\omega
+ E_m
\bigr] F(\mathrm{j}\omega)
\end{aligned}
$$

因此得到频率响应的表达式

$$
H(\mathrm{j}\omega)
= \frac{Y(\mathrm{j}\omega)}{F(\mathrm{j}\omega)}
= \frac{
E_0 (\mathrm{j}\omega)^m
+ E_1 (\mathrm{j}\omega)^{m-1}
+ \cdots
+ E_{m-1} \mathrm{j}\omega
+ E_m
}{
C_0 (\mathrm{j}\omega)^n
+ C_1 (\mathrm{j}\omega)^{n-1}
+ \cdots
+ C_{n-1} \mathrm{j}\omega
+ C_n
}
$$

可以直接写出频率响应！

!!! examples "例题"
    ![alt text](image.png)  

    ![alt text](image-1.png)

    此处 $X(\mathrm{j}\omega) = F(u(t) - u(t - \tau))$ 再展开就得到后面的傅里叶变换表达式

### 连续周期信号通过系统响应的频域分析

!!! remarks "连续周期信号通过实系统"

    计 $\phi(\omega)$ 为 $H(\mathrm{j}\omega)$ 的辐角.

    **正弦信号** $f(t) = \sin (\omega_0 t + \theta)$, 有 (实系统)

    $$
    y_f(t) = \vert H(\mathrm{j}\omega_0) \vert \sin (\omega_0 t + \phi(\omega_0) + \theta)
    $$

## 无失真传输系统和理想滤波器

### 信号的失真和无失真传输系统

包括两种：若输出波形发生变化，与输入波形不同，则产生失真 (信号的幅度减小与时间延迟不是失真，变形才是失真)

线性系统引起的信号失真包括：  
- 幅度失真：各频率分量幅度产生**不同程度**的衰减  
- 相位失真：各频率分量产生的相移不与频率成正比，使响应的各频率分量在时间轴上的相对位置产生变化

无失真传输系统的输出信号应为

$$
y(t) = K\cdot f(t - t_d)
$$

在频域的频率响应为

$$
H(\mathrm{j}\omega) = K\cdot \mathrm{e}^{-\mathrm{j}\omega t_d}
$$

幅度响应 $\vert H(\mathrm{j}\omega) = K$, 相位响应 $\phi(\omega) = -\omega t_d$ 是正比于 $\omega$ 的线性函数.

!!! examples "例题"
    ![alt text](image-2.png)

    注意这里相位的求法，使用图像法看夹角


通过系统改变信号中各频率分量的相对大小和相位，甚至完全去除某些频率分量的过程，称为**滤波**  
滤波器允许信号通过的频段称为滤波器的**通带** (pass band)，不允许信号通过的频段称为**阻带** (stop band)  
理想滤波器可分为**低通**、**高通**、**带通**、**带阻**

### 理想低通滤波器

$$
H(\mathrm{j}\omega) = \begin{cases}
    \mathrm{e}^{-\mathrm{j}\omega t_d}, &\quad \vert \omega \vert \leq \omega_c \\
    0, &\quad \vert \omega \vert > \omega_c
\end{cases} = p_{2\omega_c}\mathrm{e}^{-\mathrm{j}\omega t_d}
$$

$\omega_c$ 被称为**截止角频率**  
幅频响应 $\vert H(\mathrm{j}\omega)\vert$ 在通带 $0 - \omega_c$ 恒为 $1$ (或常数 $K$)，在通带之外为 $0$;  
相频响应 $\phi(\omega)$ 在通带内与 $\omega$ 成线性关系

**冲激响应**

$$
h(t) = \frac{1}{2\pi} \int_{-\omega_c}^{\omega_c}\mathrm{e}^{-\mathrm{j}\omega t_d}\mathrm{e}^{\mathrm{j}\omega t} \mathrm{d}t = \frac{\omega_c}{\pi}\mathrm{Sa}(\omega_c (t - t_d))
$$

$h(t)$ 的主瓣宽度为 $2\pi /\omega_c$, $\omega_c$ 越小，失真越大. 当 $\omega_c \to \infty$ 时，变为无失真传输系统，此时 $h(t)$ 变为冲激信号  
由于 $h(t)$ 存在 $t < 0$ 的成分，因此为非因果系统，物理不可实现

**阶跃响应**

$$
g(t) = \int_{-\infty}^{t}h(\tau) \mathrm{d}\tau = \frac{\omega_c}{\pi}\int_{-\infty}^{t}\mathrm{Sa}(\omega_c (\tau - t_d))\mathrm{d}\tau
$$

阶跃响应比输入阶跃信号延迟 $t_d$  
阶跃响应的建立需要一段时间。阶跃响应从最小值上升到最大值所需时间称为阶跃响应的**上升时间** $t_r = 2\pi / \omega_c$

!!! examples "例子: 滤波器，画图做"
    ![alt text](image-3.png)


!!! remarks "利用低通滤波器实现波形生成"

    方波信号经过低通滤波器，得到正弦波 (先滤掉高频, 只留下主瓣最内侧的两个峰, 再去掉直流分量, 就得到正弦信号)

由于理想滤波器是物理不可实现的，工程应用中就必须寻找一个物理可实现的频率特性去逼近理想特性，这种物理可实现的系统是**非理想滤波器**.

![alt text](image-4.png)

仅了解用

## 连续时间信号的时域抽样

### 信号抽样的理论分析

有 $\displaystyle f[k] = f(kT) = \int_{-\infty}^\infty f(t)\delta(t - kT)\mathrm{d}t$, 也即

$$
\displaystyle f_s(t) = f(t) \sum_n \delta(t - nT)
$$

为其抽样，其频域为

$$
\begin{aligned}
    F_s(\mathrm{j}\omega) &= \frac{1}{2\pi}F(\mathrm{j}\omega)\otimes \omega_0\sum_n \delta(\omega - n\omega_0) \\
    &= \frac{1}{T_s}\sum_n F(\omega - n\omega_0)
\end{aligned}
$$

其中 $\displaystyle \frac{1}{T} = f_s$ 为采样频率.  
可以理解为，采样之后的频谱是原频谱的周期性延拓，$n = 0$ 时，$\displaystyle F_s(\omega) = \frac{1}{T}F(\omega)$

![alt text](image-5.png)

如上图，使用低通滤波器可以取得最中间的频谱，即可以完全恢复原信号，前提是原信号的频谱不宽，不会发生重叠.  
也即，只有采样率足够高 ($\omega_s$ 足够宽) 的时候才能更好地恢复原信号

#### 时域取样定理

若带限信号 $f(t)$ 的最高角频率为 $\omega_0$, 则其可用等间隔的抽样值唯一地表示，而抽样间隔需不大于 $1 / (2 f_m)$, 或最低采样频率 $f_s$ 不小于 $2f_m$  
$f_s = 2f_m$ 为最小采样频率，称为**奈奎斯特采样率** (Nyquist Rate)

#### 冲激串采样后连续时间信号与离散序列的频谱

$$
\begin{aligned}
    F_s(\omega) &= \int_T \sum_k f(t)\delta(t - kT)\mathrm{e}^{-\mathrm{j}\omega t} \mathrm{d}t \\
    &= \sum_k \int_T f(kT)\delta(t - kT)\mathrm{e}^{-\mathrm{j}\omega t} \mathrm{d}t \\
    &= \sum_k f(kT)\mathrm{e}^{-\mathrm{j}\omega kT} = \sum_k f[k]\mathrm{e}^{-\mathrm{j}\omega kT} \\
    &= F(\mathrm{e}^{\mathrm{j}\omega T}) = X(\mathrm{e}^{\mathrm{j}\Omega})
\end{aligned}
$$

其中 $\displaystyle\Omega = \omega T = \frac{\omega}{f_s}$, $\vert \Omega \vert < \pi$ (1)
{ .annotate }

1. 离散信号频谱的周期性

### 信号重建

对于上述信号，使用一个低通滤波器

$$
H_r(\mathrm{j}\omega) = \begin{cases}
    T_s, &\quad \vert \omega \vert < \omega_s / 2 \\
    0, &\quad \vert \omega \vert < \omega_s / 2
\end{cases}, \quad h_r(t) = \mathrm{Sa}\frac{\omega_s t}{2}
$$

!!! remarks "有性质"

    由于

    $$
    F_s(\mathrm{j}\omega) \cdot H_r(\mathrm{j}\omega) = F(\mathrm{j}\omega)
    $$

    因此

    $$
    \begin{aligned}
        &f(t) = f_s(t) \otimes h_r(t) \\
        \Leftrightarrow &\sum_k f(kT_s)\cdot h_r(t - kT_s) = f(t)
    \end{aligned}
    $$

    也即 sinc 插值公式的变体

    $$
    f(t)
    = \sum_{k=-\infty}^{\infty} f(kT_s)
    \mathrm{Sa}\!\left(\frac{\pi}{T_s}(t - kT_s)\right)
    $$

!!! remarks "混叠误差与截断误差"

    ![alt text](image-6.png)

    一般截断误差可以接受，但是尽量避免混叠误差.

!!! normal-comment "矩形脉冲抽样"
    实际操作中难以实现冲激信号 (峰值功率为正无穷), 因此为矩形脉冲抽样.

    ![alt text](image-7.png)

    可见矩形脉冲也可以进行采样 ($0$ 附近频谱)

在实际应用中，我们还是采用 $f_s \geq (3 \sim 5)$, 是因为除了为了减少混叠，还会存在一些误差，在这些误差作用下虽然频域正确，在较长的时域中会有误差积累. (？)

!!! examples "欠采样技术"

    中心频率很高但是宽度很窄的信号 (例如 FM 信号, 只在指定频率附近有频率), 可以使用比其宽度宽的采样频率进行采样，能将信号搬移到 $0$ 附近，实现一样效果的采样

## 频域分析的应用

### 调制

以高频信号 $A\cos (\omega t +\varphi)$ 作为载波, 把低频信号搬移到高频信号上.

分为三类:  
AM 调幅, $A \to 1 + k \cdot f(t)$  
FM 调频, $\omega \to \omega_0 + k_f \cdot f(t)$  
PM 调相, $\varphi \to \varphi_0 + k_p \cdot f(t)$

#### 双边带调幅 (Amplitude Modulation)

$y(t) = f(t) \cos \omega_c t$, 有 

$$
Y(\mathrm{j}\omega) = \frac{1}{2}F(\omega + \omega_c) + \frac{1}{2}F(\omega - \omega_c)
$$

将 $F$ 的低频部分搬移到 $\omega_c$ 附近的高频部分.

### 解调

#### 同步解调

接收端有一个与发射端频率相同、相位也相同的振荡器，产生本地载波 $r(t) = y(t)\cos \omega_c t = f(t) \cos^2 \omega_c t$, 有

$$
R(\omega) = \frac{1}{2}F(\omega) + \frac{1}{4}\left(F(\omega - 2\omega_c) + F(\omega + 2\omega_c)\right)
$$

作用上低通滤波器即得 $f_r(t) = F^{-1}(R(\omega)\cdot H(\omega))$

![alt text](image-8.png)

同步解调需要精确锁定本地信号的相位!

!!! remarks "正交调制/解调"
    ![alt text](image-9.png)

    这样单个信道能传送两个独立信号，能提高信道的频谱利用率. 该方法依然需要相位锁定.

#### 检波器解调

发送端使用 $y(t) = \left[1 + kf(t)\right]\cos \omega_c t$, 确保 $1 + kf(t) > 0$, 再使用 RC 电路滤去高频部分，留下直流附近分量，即得原信号的频谱.  
但是其平均功率比较大.

### 频分复用

对信号 $f_i$, 使用

$$
y(t) = \sum f_i(t) \cos \omega_i t
$$

解调时在对应位置滤波并解调即可.

### 时分复用

(在时间轴中按延迟插入不同同周期信号，不做介绍)

## 离散信号通过系统的响应

$$
H(\mathrm{e}^{\mathrm{j}\Omega}) = \vert H(\mathrm{e}^{\mathrm{j}\Omega}) \vert \mathrm{e}^{\mathrm{j}\phi(\Omega)}
$$

补充地我们称 $\displaystyle \tau (Omega) = \frac{\mathrm{d}\phi(\Omega)}{\mathrm{d}\Omega}$ 为群时间响应

我们发现，

$$
y[k] = \mathrm{e}^{\mathrm{j}\Omega k} \otimes h[k] = \mathrm{e}^{\mathrm{j}\Omega k} \sum_n \mathrm{e}^{-\mathrm{j}\Omega n}h[n] = \mathrm{e}^{\mathrm{j}\Omega k} H(\mathrm{e}^{\mathrm{j}\Omega})
$$

离散系统的频率响应，等于系统单位样值响应的傅里叶变换

因此, 

$$
\begin{aligned}
    T[f[k]] &= \frac{1}{2\pi}\int_{2\pi}F(\mathrm{e}^{\mathrm{j}\Omega})T[\mathrm{e}^{\mathrm{j}\Omega k}] \mathrm{d}\Omega \\
    &= \frac{1}{2\pi}\int_{2\pi}F(\mathrm{e}^{\mathrm{j}\Omega})H(\mathrm{e}^{\mathrm{j}\Omega})\mathrm{e}^{\mathrm{j}\Omega k} \mathrm{d}\Omega
\end{aligned}
$$

### 理想低通数字滤波器

对于截止频率为 $\Omega_c$, 幅度为 $A$ 的低通滤波器，我们定义其相位响应为线性 (线性相位系统): $\phi(\Omega) = -\Omega k_0, \tau(\Omega) = k_0$, 也即

$$
H(\mathrm{j}\omega) = \begin{cases}
    \mathrm{e}^{-\mathrm{j}\omega k_0}, \quad & \omega < \omega_c \\
    0, \quad & \omega > \omega_c
\end{cases}
$$

此时对于 $f[k]$ (其频率为 $\Omega_m$), 其响应

$$
y[k] = \sum_{k = 0}^{n - 1}F[k]A\mathrm{e}^{\mathrm{j}\Omega_m (j - j_0)}
$$