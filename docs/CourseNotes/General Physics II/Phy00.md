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

### 微分方程

#### y'+ay=0

将 $y'$ 化为 $\mathrm{d}y/\mathrm{d}x$，分离变量，通解为：

$$y=Ce^{-ax}$$

#### y''+ay=0

令 $a=\omega^2$，通解为 $y=C_1\sin(\omega x)+C_2\cos(\omega x)$.

#### ay''+by'+cy=0

令 $\Delta =b^2-4ac$，通解为：

1. $\Delta >0,\, \lambda_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$，则 $y=C_1e^{\lambda_1x}+C_2e^{\lambda_2x}$；
2. $\Delta=0,\, \lambda=-\frac{b}{2a}$，则 $y=(C_1+C_2x)e^{\lambda x}$；
3. $\Delta <0,\, \lambda_{1,2}=\alpha\pm i\beta$，则 $y=e^{\alpha x}(C_1\sin(\beta x)+C_2\cos(\beta x))$.

#### 特解

当微分方程等式右边非零时，需要化为通解+特解的形式。

| 非齐次项 $g(x)$ 的形式                         | 应猜测的特解 $y_p(x)$                           | 备注                      |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------- |
| 常数 $C$                                       | $A$                                             | $A$ 为常数                |
| 多项式：$a_0 + a_1 x + \cdots + a_n x^n$       | $A_0 + A_1 x + \cdots + A_n x^n$                | 同阶多项式                |
| $e^{kx}$                                       | $A e^{kx}$                                      | 若 $k$ 为特征根，需乘 $x$ |
| 多项式 × $e^{kx}$                              | (多项式) × $e^{kx}$                             | 同上，若共振需乘 $x$      |
| $\sin(\omega x)$, $\cos(\omega x$)             | $A \sin(\omega x) + B \cos(\omega x)$           | 一对一起猜                |
| $e^{kx} \sin(\omega x), e^{kx} \cos(\omega x)$ | $e^{kx} (A \sin(\omega x) + B \cos(\omega x))$  | 振荡指数型                |
| 多项式 × $\sin(\omega x)$ 或 $\cos(\omega x)$  | 多项式 × $(A \sin(\omega x) + B\cos(\omega x))$ | 同阶多项式                |


## 英语！

#### 基本物理量与场

| English Term          | 中文翻译     |
| --------------------- | -------- |
| electric field        | 电场       |
| magnetic field        | 磁场       |
| electric flux         | 电通量      |
| magnetic flux         | 磁通量      |
| electric potential    | 电势       |
| potential difference  | 电势差      |
| permittivity          | 介电常数、介电率 |
| relative permittivity | 相对介电常数   |
| permeability          | 磁导率      |
| relative permeability | 相对磁导率    |
| conductivity          | 电导率      |
| charge density        | 电荷密度     |
| current density       | 电流密度     |
| displacement current  | 位移电流     |
| polarization          | 极化       |
| magnetization         | 磁化       |

#### 麦克斯韦方程组相关

| English Term           | 中文翻译      |
| ---------------------- | --------- |
| Gauss's law (electric) | 电场高斯定律    |
| Gauss's law (magnetic) | 磁场高斯定律    |
| Faraday's law          | 法拉第电磁感应定律 |
| Ampère's law           | 安培环路定律    |
| Maxwell's equations    | 麦克斯韦方程组   |
| integral form          | 积分形式      |
| differential form      | 微分形式      |
| boundary conditions    | 边界条件      |
| tangential component   | 切向分量      |
| normal component       | 法向分量      |
| continuity condition   | 连续性条件     |

#### 材料与介质

| English Term           | 中文翻译  |
| ---------------------- | ----- |
| dielectric             | 电介质   |
| conductor              | 导体    |
| insulator              | 绝缘体   |
| perfect conductor      | 理想导体  |
| perfect dielectric     | 理想电介质 |
| ferromagnetic material | 铁磁材料  |
| paramagnetic material  | 顺磁材料  |
| diamagnetic material   | 抗磁材料  |

#### 波与传播

| English Term         | 中文翻译  |
| -------------------- | ----- |
| electromagnetic wave | 电磁波   |
| wave equation        | 波动方程  |
| plane wave           | 平面波   |
| transverse wave      | 横波    |
| phase velocity       | 相速度   |
| group velocity       | 群速度   |
| wavelength           | 波长    |
| frequency            | 频率    |
| reflection           | 反射    |
| refraction           | 折射    |
| transmission         | 透射    |
| Snell's law          | 斯涅尔定律 |

#### 能量与功率

| English Term           | 中文翻译  |
| ---------------------- | ----- |
| Poynting vector        | 波印廷矢量 |
| electromagnetic energy | 电磁能   |
| power flow             | 功率流   |
| energy density         | 能量密度  |

#### 电路与相关概念

| English Term       | 中文翻译 |
| ------------------ | ---- |
| capacitance        | 电容   |
| inductance         | 电感   |
| impedance          | 阻抗   |
| reactance          | 电抗   |
| resistance         | 电阻   |
| resonant frequency | 共振频率 |

#### 常见符号

| Symbol | English Term            | 中文翻译  |
| ------ | ----------------------- | ----- |
| **E**  | electric field          | 电场强度  |
| **D**  | electric displacement   | 电位移   |
| **B**  | magnetic flux density   | 磁感应强度 |
| **H**  | magnetic field strength | 磁场强度  |
| **ρ**  | charge density          | 电荷密度  |
| **J**  | current density         | 电流密度  |
| **ε**  | permittivity            | 介电常数  |
| **μ**  | permeability            | 磁导率   |
| **σ**  | conductivity            | 电导率   |


