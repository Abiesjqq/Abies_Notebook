
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

!!! example "例题"
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