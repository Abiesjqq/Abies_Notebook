## 磁力

### 静磁场

静磁场散度为零。对于任意封闭曲面，磁通量为零。

静磁场是无源场，不是保守场。

电流形成的磁场：视为电荷运动产生磁场的叠加。

### 洛伦兹力、安培力

洛伦兹力的计算：

$$F_B=q\vec{v}\times\vec{B}$$

洛伦兹力叠加得到安培力：

$$\mathrm{d}F_B=i\mathrm{d}\vec{l}\times\vec{B}\quad\Rightarrow\quad F_B=iBl\sin\phi$$

磁场中圆周运动，速度选择器，托卡马克磁约束，测量荷质比：略。

### 霍尔效应

载流子在电场与磁场中受力平衡：

$$
Eq = qvB \quad \Rightarrow \quad E = vB
$$

设导体宽度为 \( l \)，则横向电势差为：

$$
\Delta V = lE = lvB
$$

设材料厚度为 \( t \)，载流子体密度为 \( n \)，电荷量为 \( q \)，则可用电流表示 $v$：

$$
I = nq v \cdot (t l) \quad \Rightarrow \quad v = \frac{I}{nq t l} \\[0.5em]
\Rightarrow \Delta V = l \cdot \left( \frac{I}{nq t l} \right) \cdot B = \frac{IB}{nq t}
$$

定义霍尔系数 \( R_H = \frac{1}{nq} \)，则

!!! pure ""

    $$
    \Delta V =\frac{IB}{nq t}= R_H\cdot \frac{IB}{t}
    $$

其中霍尔系数是宏观可测量量。

### 磁偶极子

#### 磁偶极子定义

单根导线受力与力矩：设导线长度为 \( l \)，电流为 \( I \)，磁场为 \( \vec{B} \)，夹角为 \( \theta \)：

$$
F = I l B, \quad \tau = F \cdot \frac{l}{2} \sin\theta = I l^2 B \sin\theta
$$

推广到闭合线圈（面积 \( A \)）：

$$
\vec{\tau} = I \vec{A} \times \vec{B}
$$

若磁场方向与线圈平面垂直，则线圈各边所受安培力合力为零，但存在力矩（除非磁场平行于法向量）。  
在均匀磁场中，任意闭合载流线圈所受合力为零，但可能有力矩。

磁偶极子是封闭的载流线圈，其磁偶极矩为：

$$
\vec{\mu} = I \vec{A} \hat{n}
$$

其中 \( \hat{n} \) 是由右手定则确定的法向量。

#### 磁偶极子受力

在均匀磁场中，磁偶极子所受合力为零，但力矩 $\vec{\tau} = \vec{\mu} \times \vec{B}$ 不为零。力矩方向使 \( \vec{\mu} \) 趋向于与 \( \vec{B} \) 同向。  
（对比电偶极子：\( \vec{\tau} = \vec{p} \times \vec{E} \)）

磁偶极子势能表达式：

$$
U(\theta) = -\vec{\mu} \cdot \vec{B}
$$

当 \( \vec{\mu} \) 与 \( \vec{B} \) 方向一致时，能量最低（稳定平衡）。

#### 非均匀磁场中磁偶极子

在非均匀磁场中，磁偶极子会受到净力：

$$
\begin{align*}
\vec{F} &= -\nabla U = \nabla (\vec{\mu} \cdot \vec{B}) \\
&= \left( \mu_x \frac{\partial B_x}{\partial x}, \mu_y \frac{\partial B_y}{\partial y}, \mu_z \frac{\partial B_z}{\partial z} \right)
\end{align*}
$$

更准确形式（矢量梯度）：

$$
\vec{F} = (\vec{\mu} \cdot \nabla) \vec{B}
$$
