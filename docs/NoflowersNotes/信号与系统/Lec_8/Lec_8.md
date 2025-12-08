
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
    \phi(\mathrm{j}\omega) &= K\frac{ \prod_{i = 1}^m\operatorname{Arg}(\mathrm{j}\omega - z_i)}{ \prod_{i = 1}^n\operatorname{Arg}(\mathrm{j}\omega - p_i)}
\end{aligned}
$$

可以在零极点图中通过观察在 $\omega$ 变化时各个差矢量的模长之积/商来判断频响变化

!!! examples "例子"

    ![alt text](image-1.png)

!!! examples "超级例题"

    ![alt text](image-2.png)

## L 变换与微分方程

!!! examples "一个例题"

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
    R_{\mathrm{zs}}(s)& = \frac{(s + 3)U(s)}{s^2 + 3s + 2} = \frac{3}{2s} - \frac{2}{s + 1} + \frac{1}{2(s + 2)} \\
    r_{\mathrm{zs}}(t) &= \left(\frac{1}{2}\mathrm{e}^{-2t} - 2\mathrm{e}^{-t} + \frac{3}{2}\right)u(t)
\end{aligned}
$$