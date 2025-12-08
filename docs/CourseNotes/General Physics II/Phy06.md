## 电磁感应

### 感生电动势

定义磁通量 $\Phi_B$：

$$\Phi_B=\iint_B\vec{B}\cdot\mathrm{d}\vec{S}$$

感生电动势等于磁通量的变化率：

!!! pure ""

    $$\mathcal{E}=-\frac{\mathrm{d}\Phi_b}{\mathrm{d}t}$$

楞次定律：感应电流的方向阻止磁通量的变化，即上面公式中负号。

电磁感应的本质是能量守恒。

### 动生电动势

洛伦兹力 $\vec{F_B}=-e(\vec{v}\times\vec{B})$，电场 $\vec{E}=\frac{\vec{F_B}}{-e}=\vec{v}\times\vec{B}$，由电场得到动生电动势：

!!! pure ""

    $$\mathcal{E}=\int_a^b (\vec{v}\times\vec{B})\cdot\mathrm{d}\vec{s}$$

洛伦兹力不做功，这里洛伦兹力方向仍与叠加后速度垂直。

### 感生电场

磁场变化产生涡旋电场，使导体中电子定向运动，产生电动势。

需要对麦克斯韦方程组修正：

!!! pure ""

    $$\oint\vec{E}\cdot\mathrm{d}\vec{l}=\mathcal{E}=\frac{\mathrm{d}\Phi_B}{\mathrm{d}t}$$

## 电感

定义自感系数 $L$，单位为 $\mathrm{H}$：

!!! pure ""

    $$L=\frac{N\Phi_B}{I}$$

电动势与电感的关系：

!!! pure ""

    $$\mathcal{E}=-L\frac{\mathrm{d}i}{\mathrm{d}t}$$

### LR 电路

充电时，回路总电势差为零，即 $\mathcal{E}-iR-L\frac{\mathrm{d}i}{\mathrm{d}t}=0$，化简得到 $i=\frac{\mathcal{E}}{R}(1-e^{-\frac{t}{\tau}})$，其中 $\tau$ 表示 $\frac{L}{R}$。

同理，放电时，$i=\frac{\mathcal{E}}{R}e^{-\frac{t}{\tau}}$。

### 自感磁能

电流从 0 增大到 $i$ 时，电感中能量为

!!! pure ""

    $$U_B=\frac{1}{2}Li^2$$

能量密度 $u_B=\frac{U_B}{V}$。

### 互感

线圈 1 对线圈 2 产生的磁通量正比于线圈 1 的电流，比例稀疏记为 $M_{12}$，同理定义 $M_{21}$。

可证明 $M_{12}=M_{21}=M$，记为互感系数。

互感系数与自感系数的关系：

$$M=k\sqrt{L_1L_2}$$

若 k=1 表示同轴，若 k=0 表示垂直，若 0 < k < 1 表示部分漏磁。

### 互感磁能

两个线圈的系统中，除了各自存储自感磁能，电源还要抵抗互感电动势作功，形成互感磁能，大小为：

!!! pure ""

    $$U_B=MI_1I_2$$

在 k 个线圈的系统中，总能量等于自感磁能之和加互感磁能之和：

$$W_B=\frac{1}{2}\sum_iL_iI_i^2+\frac{1}{2}\sum_{i,j}M_{ij}I_iI_j$$

### LC 电路

回路总电势差为零建立等式 $-L\frac{\mathrm{d}i}{\mathrm{d}t}=\frac{q}{C}$，得到二阶微分方程，解为 $q=q_0\cos(\omega t+\phi)$，其中 $\omega=\frac{1}{\sqrt{LC}}$。

能量在电容和电感间相互转化，两者能量之和为定值。

### RCL 电路

建立等式 $-L\frac{\mathrm{d}i}{\mathrm{d}t}+\frac{q}{C}+iR=0$。

如果外加周期性电源 $\mathcal{E}=\mathcal{E}_m\cos \omega''t$，则变为受迫振动。当 $\omega''=\omega$ 时得到共振，电流峰值最大。

任意时刻下，电路最大储能等于电容或电感可能的储能的峰值。

## 磁介质

磁化强度 $\vec{M}$，表示磁化后的宏观效果：

!!! pure ""

    $$\vec{M} =\frac{\sum\mu_i}{\Delta V}$$

定义磁场强度 $H$：

!!! pure ""

    $$H=\frac{\vec{B}}{\mu_0}-\vec{M}$$

## 边界条件

| 物理量              | 法向分量边界条件                                                 | 切向分量边界条件                                                         | 说明                      |
| ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------- |
| 电场 $\vec E$       | $E_2^\perp-E_1^\perp=\frac{\sigma_{\text{free}}}{\varepsilon_0}$ | $\vec E_1^\parallel=\vec E_2^\parallel$                                  | 法拉第定律（无环电压）    |
| 电位移 $\vec D$     | $D_2^\perp-D_1^\perp=\sigma_{\text{free}}$                       | $\vec D_1^\parallel=\vec D_2^\parallel$                                  | $\vec D$ 只对自由电荷敏感 |
| 磁感应强度 $\vec B$ | $B_1^\perp=B_2^\perp$                                            | $B_2^\parallel-B_1^\parallel=0$                                          | 无磁单极子                |
| 磁场强度 $\vec H$   | $H_1^\perp=H_2^\perp$                                            | $\vec H_2^\parallel-\vec H_1^\parallel=\vec K_{\text{free}}\times\hat n$ | 安培环路定律              |
