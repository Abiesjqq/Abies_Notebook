## 数学基础

算符 nabla：

$$\vec{\nabla}=\frac{\partial}{\partial x}\vec{i}+\frac{\partial}{\partial y}\vec{j}+\frac{\partial}{\partial z}\vec{k}$$

### 梯度

标量函数$f=f(x,y,z)$的梯度，输入为标量、输出为矢量：

$$\vec{\nabla}f=\frac{\partial f}{\partial x}\vec{i}+\frac{\partial f}{\partial y}\vec{j}+\frac{\partial f}{\partial z}\vec{k}$$

设$\vec{\nabla}f$和$d\vec{l}$之间的夹角为$\theta$，则

$$df=|\vec{\nabla}f||d\vec{l}|\cos\theta,\quad|\vec{\nabla}f|=\frac{df_{max}}{|d\vec{l}|}$$

即梯度是导数下降最快的方向。

### 散度

矢量函数$f=(P(x,y,z), Q(x,y,z), R(x,y,z))$的散度，输入为矢量、输出为标量：

$$\vec{\nabla}\cdot \vec{f}=P_x'+Q_y'+R_z'$$

散度表示单位立方体中矢量场线的净流出量（假象立方体，$P_x'$表示 x 方向相对的两个面的净流出量，etc.）。散度大于零，表示源；散度小于零，表示汇；散度等于零，表示无源。

**散度定理（高斯定理）：**

$$\oint_{\tau}\vec{A}\cdot\mathrm{d}\vec{S}=\int_{\tau}(\vec{\nabla}\cdot\vec{A})\mathrm{d}\tau$$

??? normal-comment "证明"

    待补充。

### 旋度

矢量函数$f=(P(x,y,z), Q(x,y,z), R(x,y,z))$的旋度，输入为矢量、输出为矢量：

$$
\begin{align*}
\vec{\nabla}\times \vec{f}&=\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix} \\
&= \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\vec{i} + \left(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\right)\vec{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\vec{k}
\end{align*}
$$

??? normal-comment "旋度的几何含义"

    *什么是"有旋"？*

    首先理解"旋"的概念：
    - **有旋**：矢量场有"环绕"或"涡旋"的性质，就像漩涡中的水流
    - **无旋**：矢量场没有环绕性质，就像平行直流的水流
    - **旋度**：衡量矢量场在某点附近的"旋转强度"

    *旋度的物理本质*

    旋度实际上衡量的是：**单位面积内矢量场的环流强度**

    *数学推导：为什么旋度表示旋转强度*

    让我详细解释旋度公式中z分量的含义：

    z分量：

    $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$

    想象在xy平面上有一个小矩形，边长为$\Delta x$和$\Delta y$：

    **1. 沿着矩形边界的环流**

    沿矩形边界逆时针方向计算环流：
    - **底边**：从$(x, y)$到$(x+\Delta x, y)$，贡献$P(x,y) \cdot \Delta x$
    - **右边**：从$(x+\Delta x, y)$到$(x+\Delta x, y+\Delta y)$，贡献$Q(x+\Delta x,y) \cdot \Delta y$
    - **顶边**：从$(x+\Delta x, y+\Delta y)$到$(x, y+\Delta y)$，贡献$-P(x,y+\Delta y) \cdot \Delta x$
    - **左边**：从$(x, y+\Delta y)$到$(x, y)$，贡献$-Q(x,y) \cdot \Delta y$

    **2. 总环流**

    $$\Gamma = P(x,y)\Delta x + Q(x+\Delta x,y)\Delta y - P(x,y+\Delta y)\Delta x - Q(x,y)\Delta y$$

    **3. 利用泰勒展开**

    - $Q(x+\Delta x,y) \approx Q(x,y) + \frac{\partial Q}{\partial x}\Delta x$
    - $P(x,y+\Delta y) \approx P(x,y) + \frac{\partial P}{\partial y}\Delta y$

    代入得：

    $$ \Gamma \approx \frac{\partial Q}{\partial x}\Delta x \Delta y - \frac{\partial P}{\partial y}\Delta x \Delta y = \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\Delta x \Delta y$$

    **4. 单位面积的环流（旋度的z分量）**

    $$(\vec{\nabla}\times \vec{f})_z = \frac{\Gamma}{\Delta x \Delta y} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$

    *为什么旋度不为零表示有旋？*

    **核心理解**：旋度衡量的是**环流密度**

    - **旋度 ≠ 0**：净环流 ≠ 0 → 存在旋转趋势 → **有旋**
    - **旋度 = 0**：净环流 = 0 → 无旋转趋势 → **无旋**

    *具体例子*

    例子1：纯旋转场（有旋）

    $$\vec{f} = (-y, x, 0)$$

    计算z分量：

    $$(\vec{\nabla}\times \vec{f})_z = \frac{\partial x}{\partial x} - \frac{\partial(-y)}{\partial y} = 1 - (-1) = 2$$

    这表示绕z轴逆时针旋转，旋度不为零，所以有旋。

    例子2：径向场（无旋）

    $$\vec{f} = (x, y, 0)$$

    计算z分量：

    $$(\vec{\nabla}\times \vec{f})_z = \frac{\partial y}{\partial x} - \frac{\partial x}{\partial y} = 0 - 0 = 0$$

    这是从原点向外发散的场，虽然不是平行流，但没有旋转，所以无旋。

    例子3：剪切流（有旋）

    $$\vec{f} = (y, 0, 0)$$

    计算z分量：

    $$(\vec{\nabla}\times \vec{f})_z = \frac{\partial 0}{\partial x} - \frac{\partial y}{\partial y} = 0 - 1 = -1$$

**旋度定理（斯托克斯定理）：**

$$\oint_C\vec{A}\cdot\mathrm{d}\vec{l}=\int_S(\vec{\nabla}\times\vec{A})\cdot\mathrm{d}\vec{S}$$

??? normal-comment "证明"

    待补充。

### 拉普拉斯算子

标量函数$f=f(x,y,z)$作用给拉普拉斯算子：

$$
\begin{align*}
\Delta f&=\nabla\cdot\nabla f \\
&=(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z})\cdot(f_x',f_y',f_z') \\
&=f_{xx}''+f_{yy}''+f_{zz}''
\end{align*}
$$

## 电场强度计算

### 电偶极子

电偶极子电偶极距为 d，所求点距几何中心距离为 r，夹角为$\phi$，则电场：

$$\vec{E_p}=\frac{1}{4\pi\varepsilon_0 r^3}\left[-\vec{p}+\frac{3\vec{r}(\vec{r}\cdot\vec{p})}{r^2}\right]$$

??? normal-comment "证明"

    ![电偶极子](./PHYresources/电偶极子.jpg)

### 有限长带电直导线

导线长 2L，带电量 q，所求点距离导线中心距离为 z，在同一水平面上，则电场：

$$\vec{E}=\frac{q}{4\pi\varepsilon_0}\frac{1}{z\sqrt{z^2+L^2}}\hat{k}$$

??? normal-comment "证明"

    ![带电直导线](./PHYresources/带电直导线.jpg)

### 有限大带电平面

平面长 2L，宽 2b，所求点和几何中心在同一竖直面内，距离平面距离为 z（z << L），则电场：

$$\vec{E}=\frac{\sigma}{\pi\varepsilon_0}\cdot\arctan(\frac{b}{z})\hat{k}$$

??? normal-comment "证明"

    ![带电平面](./PHYresources/带电平面.jpg)

### 圆环、球壳、球体

**圆环**：按角度分成一段段圆弧

**均匀带电球壳**：纵向分成圆环，每个圆环的宽度按纵切面角度划分，最终为关于角度的积分。

$$\mathrm{d}q=2\pi R\sin\theta\text{(圆环周长)}\cdot R\mathrm{d}\theta\text{(圆环宽度)}\cdot\sigma\text{(电荷面密度)}$$

**球壳内**：对任意一点，取相对的两块球面，用立体角计算面积。相对球面在该点的电场强度抵消。

**均匀带电球体**：球外平方反比，球内正比。

## 几点注意

**几种倍率：**

| 前缀      | 符号  | 倍数       | 数值表示                                 |
| --------- | ----- | ---------- | ---------------------------------------- |
| **femto** | f     | $10^{-15}$ | $1 \, \text{fC} = 10^{-15} \, \text{C}$  |
| **micro** | $\mu$ | $10^{-6}$  | $1 \, \mu\text{C} = 10^{-6} \, \text{C}$ |
| **milli** | m     | $10^{-3}$  | $1 \, \text{mA} = 10^{-3} \, \text{A}$   |
| **centi** | c     | $10^{-2}$  | $1 \, \text{cm} = 10^{-2} \, \text{m}$   |
| **deci**  | d     | $10^{-1}$  | $1 \, \text{dm} = 10^{-1} \, \text{m}$   |
| **kilo**  | k     | $10^{3}$   | $1 \, \text{kJ} = 10^{3} \, \text{J}$    |
| **mega**  | M     | $10^{6}$   | $1 \, \text{MG} = 10^{6} \, \text{g}$    |
| **giga**  | G     | $10^{9}$   | $1 \, \text{GB} = 10^{9} \, \text{B}$    |
| **tera**  | T     | $10^{12}$  | $1 \, \text{TB} = 10^{12} \, \text{B}$   |


??? examples "相对运动下观察电场和磁场？"

    假设一无限长直导线，电荷以恒定速度 v 向右运动。

    case1：人静止。此时电荷产生电场，运动的电荷产生磁场。

    case2：人也以恒定速度 v 向右运动，此时电荷和人相对静止，在该参考系中磁场为零。

    case2 中观察者速度为$v$，根据相对论长度缩短，观察到的电荷密度为$\lambda'=\gamma\lambda$，其中$\gamma=\frac{1}{\sqrt{1+v^2 / c^2}}$为洛伦兹因子、$\lambda$为 case1 中的电荷密度。由于 case2 中电荷密度更大，电场更强，“补偿”了磁场的消失。

    这个例子说明了电场和磁场是同一物理实体在不同参考系中的表现。

??? examples "运动电荷不满足库伦定律？"

    *库伦定律的适用范围*

    库伦定律：

    $$\vec{F} = k\frac{q_1 q_2}{r^2}\hat{r}$$

    **仅适用于静止电荷**之间的相互作用。当电荷运动时，情况变得复杂得多。

    *为什么运动电荷不满足库伦定律？*

    1. **磁场的产生**

    运动电荷会产生磁场：

    $$\vec{B} = \frac{\mu_0}{4\pi}\frac{q\vec{v}\times\hat{r}}{r^2}$$

    这个磁场会对其他运动电荷产生洛伦兹力：

    $$\vec{F}_{magnetic} = q\vec{v}\times\vec{B}$$

    2. **电场的变化**

    运动电荷的电场不再是简单的库伦场，而是：

    $$\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\frac{(1-\beta^2)}{(1-\beta^2\sin^2\theta)^{3/2}}\hat{r}$$

    其中 $\beta = v/c$，$\theta$ 是速度方向与位置矢量的夹角。

    3. **相对论效应**

    高速运动时，还需要考虑：
    - 长度收缩
    - 时间膨胀
    - 质量-能量等效

    考虑一个静止电荷和一个运动电荷。前者对后者的力满足库伦定律，而后者对前者的力不满足库伦定律。此时牛顿第三定律不成立！

## 高斯定理

封闭曲面的电通量正比于曲面围成区域内的电荷总量。

$$\oiint\vec{E}\cdot\mathrm{d}\vec{S}=\frac{Q_{in}}{\varepsilon_0}$$

**高斯定理：**

假设封闭曲面 S，围成体积 V。  
则 S 的通量，即矢量对 S 的面积分，等于散度对 V 的体积分。  
通量为正，表示源；通量为负，表示汇。

**对于电场：**

对于任意的小立方体（dx, dy, dz），有

通量 = 总电荷量/介电常数 = 电荷密度/介电常数 _ 体积  
通量 = 散度 _ 体积

因此对每个小立方体，散度 = 电荷密度/介电常数

$$
\begin{align}
\vec{\nabla}\cdot\vec{E}=\frac{\rho}{\varepsilon_0}
\end{align}
$$

而任意封闭曲面围成的体积，可看作无数个小立方体的集合。通量等于散度的体积分，而每个散度用“电荷密度/介电常数”替换，得到任意体积满足(1)式。

**斯托克斯定理：**

假设封闭曲线为 l，围成曲面 S。  
则 l 的环流，即矢量对 l 的线积分，等于旋度对 S 的面积分。  
环流为正，表示逆时针；环流为负，表示顺时针；环流为零，表示无旋。

静电场是无旋场：

$$\vec{\nabla}\times\vec{E}=0$$

**常见电场强度：**

| **电荷分布**                         | **高斯面选择**                   | **电场强度表达式**                                   | **说明**                                                         |
| ------------------------------------ | -------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------- |
| **无限长直导线（线电荷密度）**       | 圆柱形高斯面（以导线为轴心）     | $E = \frac{\lambda}{2 \pi \varepsilon_0 r}$          | 其中 $\lambda$ 为线电荷密度，$r$ 为到导线的径向距离              |
| **无限大平板（面电荷密度）**         | 平行于平板的高斯面（与平板平行） | $E = \frac{\sigma}{2 \varepsilon_0}$                 | 其中 $\sigma$ 为面电荷密度，电场强度在平板两侧相等，且与距离无关 |
| **球壳（外部，面电荷密度）**         | 球形高斯面（半径大于球壳半径）   | $E = \frac{Q_{\text{enc}}}{4 \pi \varepsilon_0 r^2}$ | $Q_{\text{enc}}$ 是球壳内部的总电荷，$r$ 是距离球心的径向距离    |
| **球壳（内部，面电荷密度）**         | 球形高斯面（半径小于球壳半径）   | $E = 0$                                              | 由于对称性，球壳内部的电场为零                                   |
| **均匀带电球体（外部，体电荷密度）** | 球形高斯面（半径大于球体半径）   | $E = \frac{Q_{\text{enc}}}{4 \pi \varepsilon_0 r^2}$ | 外部电场与点电荷相同，遵循平方反比定律                           |
| **均匀带电球体（内部，体电荷密度）** | 球形高斯面（半径小于球体半径）   | $E = \frac{\rho r}{3 \varepsilon_0}$                 | 其中 $\rho$ 为体电荷密度，电场强度随 $r$ 增大而增大              |
