## 电流

### 电流密度

电流密度 $\vec{j}$ 用于描述空间中任一点的电流强度，定义为：

$$\vec{j}=\frac{\mathrm{d}q}{\mathrm{d}t\mathrm{d}S_{\perp}}=\frac{\mathrm{d}i}{\mathrm{d}S_{\perp}}$$

通过封闭曲面的电流密度的通量，等于曲面内电荷变化量的负值（因为流出的通量为正）：

$$\oint_S\vec{j}\mathrm{d}\vec{S}=-\frac{\mathrm{d}q}{\mathrm{d}t}$$

对于稳恒电流（stationary current），电流密度的通量始终为零。电流密度线为闭合曲线。

### 漂移速度

外加电场后，电荷仍做无规则运动，但相比无电场时有沿电场方向的偏移。称偏移的速度为漂移速度 $v_d$，用漂移速度表示电荷运动的速度。

电流强度与漂移速度成正比（n 表示电荷的数密度）：

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

满足 $\vec{j}=\sigma\vec{E}$ 的材料称为欧姆材料。  
非欧姆材料有半导体。N 型半导体掺杂磷，多一个最外层电子；P 型半导体掺杂氮，少一个最外层电子。

### 电导率的微观表达

电荷速度：

$$
v_i = v_{0i} + \frac{eE}{m} t_i
$$

电流强度：

$$
J = \sum e v_i = \sum e v_{0i} + \sum e \cdot \frac{eE}{m} t_i = \sum \frac{e^2 E}{m} t_i
$$

定义平均碰撞时间 $ \tau = \frac{\sum t_i}{n} $，则

$$
J = \frac{n e^2 \tau}{m} E
$$

则电导率的微观表达：

$$
\sigma = \frac{1}{\rho} = \frac{n e^2 \tau}{m}, \quad \sigma \text{ 和 } \tau \text{ 有关}.
$$

$ v_d \ll v $，认为 $ \tau $ 只与材料有关，不受电场影响。

用麦克斯韦速度分布律得到平均碰撞时间：

$$
\tau = \frac{\lambda}{v} = \lambda \sqrt{\frac{2\pi m}{8kT}} \propto \frac{1}{\sqrt{T}}
$$

故

$$
\sigma \propto \frac{1}{\sqrt{T}}, \quad \rho \propto \sqrt{T}.
$$

### 几点注意

稳恒电流一般用大写I表示，瞬时电流一般用小写i表示。



## 电路

### 基尔霍夫定律

电动势等于将单位正电荷从负极移动到正极所做的功。

基尔霍夫第一定律（Junction Rule）：电流标量相加。  
基尔霍夫第二定律（Loop Rule）：回路电势差为零，$\sum\mathcal{E}_n+\sum iR_n=0$

求解电路中电流：设电流 --> 列方程组 --> 矩阵计算（或手工解方程组）

### 电场、能量分布

- 当电路中形成稳恒电流时，导体内电场强度非零。

根据高斯定律（积分形式）：

$$
\oint_S \vec{J} \cdot d\vec{S} = \oint_S \sigma \vec{E} \cdot d\vec{S} = 0 \quad \Rightarrow \quad \Sigma q = 0
$$

即导体内部处处净电荷为零。导体内的电场并非由内部电荷产生，而是来源于表面少量电荷的分布。

- 电源内做功与电动势

电源内部对电荷做功：

$$
dW = \mathcal{E} \, dq
$$

电源功率：

$$
P_{\text{EMF}} = \frac{dW}{dt} = \mathcal{E} \cdot \frac{dq}{dt} = \mathcal{E} I
$$

- 电阻两端的电势差与能量转化

电阻两端电势差：

$$
\Delta U_R = IR
$$

当电荷 $ dq $ 流过电阻时，电势能变化（转化为热能）：

$$
dW = dq \cdot \Delta U_R = I R \, dq
$$

电阻消耗的功率：

$$
P_R = \frac{dW}{dt} = I R \cdot \frac{dq}{dt} = I^2 R
$$

### RC 电路

- 充电：

根据基尔霍夫电压定律：

$$
\varepsilon - \frac{q}{C} - i R = 0  \\[0.5em]
\Rightarrow \varepsilon - \frac{q}{C} - R \cdot \frac{dq}{dt} = 0 \\[0.5em]
\Rightarrow \frac{dt}{RC} = \frac{dq}{C\varepsilon - q}
$$

积分求解得电荷随时间变化关系：

$$
q(t) = C\varepsilon \left(1 - e^{-\frac{t}{RC}}\right)
$$

- 放电：

$i = -\frac{dq}{dt}$，因为电荷减少。

$$
\frac{q}{C} - i R = 0 \Rightarrow q(t) = q_0 \, e^{-\frac{t}{RC}}
$$

- 定义时间常数 $\tau$：

电荷随时间衰减通式：

$$
\tau = RC \Rightarrow q = q_0 \, e^{-\frac{t}{\tau}}
$$


### 两电容器间充放电

初始时一个电容带电量 $q_0$，另一个不带电；通过电阻连接后发生电荷重分配。

根据基尔霍夫电压定律和电荷守恒：

$$
\left\{
\begin{aligned}
\frac{q}{C} - i R - \frac{q'}{C} &= 0 \\[0.5em]
q + q' &= q_0
\end{aligned}
\right.
$$

当系统达到稳态时，$t \to \infty$，电流为零，两电容电压相等：

$$
q = q' = \frac{q_0}{2}
$$

在过程中，电阻上消耗的能量微元：

$$
dW_R = dq \cdot \Delta U_R = i R \, dq = i R \cdot \frac{dq}{dt} \, dt
$$

对时间积分得总耗能：

$$
W_R = \int_0^{+\infty} i^2 R \, dt = \frac{1}{4} \cdot \frac{q_0^2}{C}
$$

初始电容储能为 $\frac{1}{2} \frac{q_0^2}{C}$，最终两个电容各存 $\frac{1}{2} \frac{(q_0/2)^2}{C} = \frac{1}{8} \frac{q_0^2}{C}$，总储能为 $\frac{1}{4} \frac{q_0^2}{C}$，损失的一半能量即为电阻上以热能形式耗散的部分。
