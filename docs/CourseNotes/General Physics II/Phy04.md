## 电流

### 电流密度

电流密度 $\vec{j}$ 用于描述空间中任一点的电流强度，定义为：

$$\vec{j}=\frac{\mathrm{d}i}{\mathrm{d}S_{\perp}}=\frac{\mathrm{d}q}{\mathrm{d}t\mathrm{d}S_{\perp}}$$

通过封闭曲面的电流密度的通量，等于曲面内电荷变化量的负值（因为流出的通量为正）：

$$\oint_S\vec{j}\mathrm{d}\vec{S}=-\frac{\mathrm{d}q}{\mathrm{d}t}$$

对于稳恒电流（stationary current），电流密度的通量始终为零。电流密度线为闭合曲线。

### 漂移速度

外加电场后，电荷仍做无规则运动，但相比无电场时有沿电场方向的偏移。称偏移的速度为漂移速度 $v_d$，用漂移速度表示电荷运动的速度。  

电流强度与漂移速度成正比（n表示电荷的数密度）：

$$
\begin{align*}
I&=\frac{\Delta q}{\Delta t}=\frac{v_d\Delta t\Delta S\cdot n\cdot e}{\Delta t}=env_d\Delta S \\
j&=\frac{I}{\Delta S}=env_d
\end{align*}
$$

若载流子为电子，则电流密度与漂移速度方向相反，$\vec{j}=-en\vec{v_d}$。

### 欧姆定律的微观形式

考虑一小段圆柱，电势差为 $\mathrm{d}u$，截面积为 $\mathrm{d}s$。根据宏观欧姆定律，有：

$$\mathrm{d}I=\frac{\mathrm{d}U}{\mathrm{d}R}$$

将电流密度、电阻的表达式代入，得：

$$j\mathrm{d}S=\frac{1}{\rho}\frac{\mathrm{d}U}{\mathrm{d}l}\mathrm{d}S$$

将电场强度等于电势差比长度代入，得：

$$J=\frac{1}{\rho}E=\sigma E$$

即欧姆定律的微观形式。其中 $\rho$ 为电阻率，$\sigma$ 为电导率。