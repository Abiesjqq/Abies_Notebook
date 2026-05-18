## 坐标系、点和刚体的描述

**坐标系**：这里统一采用空间笛卡尔直角右手坐标系，用大括号表示，如 $\{A\}$。通常用 $\{U\}$ 表示世界坐标系。

**点**：即列向量，用大写字母表示，左上标表示坐标系，如 $^A D$ 表示坐标系 $\{A\}$ 中的坐标点 $D$。长度、内积、外积定义略。

**刚体**：描述刚体，需要描述位置+姿态。通常在刚体上固定“联体坐标系”。

- 位置：设参考坐标系为 $\{A\}$，联体坐标系为 $\{B\}$，则刚体位置为 $\{B\}$ 的原点 $O_B$ 在 $\{A\}$ 中的位置，即 $^A O_B$。
- 姿态：用 $\{B\}$ 关于 $\{A\}$ 的旋转矩阵表示。即 $\{B\}$ 的姿态在 $\{A\}$ 中的表示。

## 两个坐标系之间的几何关系

**_Q：什么是相对姿态？_**

$\{B\}$ 关于 $\{A\}$ 的相对姿态，即 $\{B\}$ 相对于 $\{A\}$ 怎么旋转得到。

**_Q：什么是旋转矩阵？_**

旋转矩阵 $^A_B R$ 即用 $\{A\}$ 描述 $\{B\}$ 中三个轴的方向。

将 $\{B\}$ 的三个单位轴 $\hat{X_B}, \hat{Y_B}, \hat{Z_B}$ 用 $\{A\}$ 的向量表达，按列排列成矩阵，得到：

$$
^A_B R = \left(\hat{^A X_B}, \hat{^A Y_B}, \hat{^A Z_B}\right)
$$

旋转矩阵一定是正交矩阵，有：

$$
R^T R = I, \quad R^{-1} = R^T
$$

**_Q：同一个点，怎么在不同坐标系中表达？_**

即，对点 $P$，已知 $^B P$，怎么求 $^A P$？

1. 若两坐标系原点重合，则 $^A P = ^A_B R ^B P$。
2. 若原点不重合，引入齐次变换矩阵表示仿射变换（齐次坐标原理略）：

$$
^A_B T = \begin{pmatrix}
^A_B R & ^A O_B \\
0\, 0\, 0 & 1
\end{pmatrix}
$$

则 $^A P = ^A O_B + ^A_B R ^B P$，齐次坐标表示下即：

$$
\begin{pmatrix}
^A P \\ 1
\end{pmatrix}= ^A_B T \begin{pmatrix}
^B P \\ 1
\end{pmatrix}
$$

**_Q：齐次变换矩阵有什么性质？_**

1. 逆变换：旋转部分直接用逆矩阵，平移部分也要先旋转再平移：

$$
(^A_B T)^{-1} = \begin{pmatrix}
R^T & -R^T O \\
0 & 1
\end{pmatrix}
$$

2. 链乘法则：假设坐标系为 $\{A\}\to \{B\}\to \{C\}$，则：

$$
^A_C T = ^A_B T ^B_C T
$$

## 欧拉角与固定角表示

### 欧拉角

**_Q：为什么需要欧拉角？_**

旋转矩阵有9个参数，但三维刚体姿态实际只有三个自由度。下面用于讨论如何只用3个角度描述三维姿态。

**_Q：欧拉角怎么表示？_**

旋转角分为三类：

1. Roll：绕x轴旋转角，类似飞机左右翻滚
2. Pitch：绕y轴旋转角，类似飞机抬头低头
3. Yaw：绕z轴旋转角，类似飞机左右转向

对应矩阵：

$$
R_x(\phi) =
\begin{pmatrix}
1 & 0 & 0 \\
0 & \cos\phi & -\sin\phi \\
0 & \sin\phi & \cos\phi
\end{pmatrix}
$$

$$
R_y(\theta) =
\begin{pmatrix}
\cos\theta & 0 & \sin\theta \\
0 & 1 & 0 \\
-\sin\theta & 0 & \cos\theta
\end{pmatrix}
$$

$$
R_z(\psi) =
\begin{pmatrix}
\cos\psi & -\sin\psi & 0 \\
\sin\psi & \cos\psi & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

欧拉角即用连续三次旋转描述姿态，实际顺序为xyz：

$$
R = R_z(\alpha) R_y(\beta) R_x (\gamma)
$$

欧拉角属于内旋（Intrinsic Rotation），即每次旋转后后面的轴也跟着物体一起转，故后两次旋转不是绕世界坐标系的轴。

**_Q：欧拉角的顺序分为哪几类？_**

1. 对称型欧拉角：如zyz、xyx
2. 非对称型欧拉角：如zyx

略。

### 固定角

固定角属于外旋（Extrinsic Rotation），即三次旋转都绕世界坐标系固定轴，用统一旋转矩阵 $R_{xyz}(\gamma, \beta, \alpha)$ 表示。

固定角和欧拉角的关系：外旋x-y-z等价于内旋z-y-x

$$
R_{xyz}(\gamma, \beta, \alpha) = R_z(\alpha) R_y(\beta) R_x (\gamma)
$$

更新姿态矩阵时，旋转与旋转矩阵左右乘：右乘联体左乘基

- 右乘旋转矩阵表示绕联体坐标系轴旋转，即内旋
- 左乘旋转矩阵表示绕参考坐标系轴旋转，即外旋

### 欧拉角反解与万向锁问题

**_Q：已知旋转矩阵，怎么反求欧拉角？_**

即，已知旋转矩阵 $R$，将其反解为 $R_z(\alpha) R_y(\beta) R_x (\gamma)$ 的形式。

展开得到：

$$
\begin{pmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33}
\end{pmatrix} =
\begin{pmatrix}
\cos\alpha \cos\beta
&
\cos\alpha \sin\beta \sin\gamma - \sin\alpha \cos\gamma
&
\cos\alpha \sin\beta \cos\gamma + \sin\alpha \sin\gamma
\\
\sin\alpha \cos\beta
&
-\sin\alpha \sin\beta \sin\gamma + \cos\alpha \cos\gamma
&
-\sin\alpha \sin\beta \cos\gamma - \cos\alpha \sin\gamma
\\
-\sin\beta
&
\cos\beta \sin\gamma
&
\cos\beta \cos\gamma
\end{pmatrix}
$$

为了正确区分象限，引入反正切函数 $\arctan 2(y,x)$，其值域为 $(-\pi, \pi]$

结合展开式，可得：

$$
\beta =
\operatorname{atan2}
\left(
-r_{31},
\sqrt{r_{11}^2+r_{21}^2}
\right)
$$

$$
\alpha =
\operatorname{atan2}(r_{21},r_{11})
$$

$$
\gamma =
\operatorname{atan2}(r_{32},r_{33})
$$

当 $|r_{31}|\neq 1$，即 $\beta \neq \pm \frac{\pi}{2}$ 时，有唯一解。

**万向锁（Gimbal Lock）问题**：当 $\beta = \pm \frac{\pi}{2}$ 时，矩阵很多项为零，此时只能确定 $\alpha \mp \gamma$，不能确定 $\alpha$ 和 $\gamma$。类似原本独立的两个旋转轴“锁”在一起，导致系统失去一个自由度。

在接近万向锁时，微小旋转变化会导致欧拉角剧烈跳变，导致控制器难以正常工作。

### 等效轴角表示与罗德里格斯公式

**_Q：任意三维旋转，能不能等价成“绕某一根轴转一次”？_**

可以。欧拉定理给出，任意刚体定点转动都等价于绕某根固定轴旋转某个角度。这种表示方法即等效轴角表示（Axis-Angle Representation）。

下面令单位向量 $K$ 表示旋转轴，角度 $\theta$ 表示旋转角。

**_Q：已知旋转轴、旋转角，怎么得到旋转矩阵？_**

设向量 $Q$ 绕轴 $K$ 旋转角度 $\theta$，得到 $Q'$。

将 $Q$ 分解为沿轴方向的 $Q_{\parallel}$ 和垂直于轴方向的 $Q_{\perp}$，则 $Q_{\parallel}$ 不变、$Q_{\perp}$ 在平面内旋转，最终得到罗德里格斯公式（Rodrigues Formula）：

$$
Q' = Q\cos\theta + (K\times Q)\sin\theta + K(K\cdot Q)(1-\cos\theta)
$$

任意旋转矩阵都能写成 $R_K(\theta)$，右乘联体左乘基仍然成立。但轴角表示仍有特殊点，不方便连续积分。

## 单位四元数与欧拉参数

为表示三个独立方向，增加三个虚轴 $i,j,k$，满足：

$$
i^2 = j^2 = k^2 = -1,\quad ij=k, jk=i, ki=j
$$

四元数表示为：

$$
q = q_0 + q_1 i + q_2 j + q_3 k = (q_0, \mathbf{q})
$$

其中 $\mathbf{q} = (q_1, q_2, q_3)$ 为虚部向量。单位四元数满足 $q_0^2+q_1^2+q_2^2+q_3^2=1$。

**_Q：四元数有什么性质？_**

- 四元数的共轭为 $q^* = (q_0, -q_1, -q_2, -q_3)$
- 四元数的逆为其共轭，即 $q^{-1} = q^*$

一个真实旋转对应两个相反四元数，即 $q$ 和 $-q$ 表示同一个姿态。

**_Q：四元数怎么表示旋转？_**

即，已知四元数 $q$，怎么旋转向量 $P$？

先将向量 $P=(x,y,z)$ 写成纯四元数 $p=(0,x,y,z)$，四元数旋转为：

$$
p' = qpq^{-1}
$$

其中，左乘一次引入旋转，右乘逆消除额外的维度影响。

四元数本质上是四维单位球面上的点，能平滑覆盖整个旋转空间，所以没有万向锁问题。插值时，可以沿球面最短路径插值，即SLERP（球面线性插值）。

**_Q：单位四元数和轴角表示有什么关系？_**

假设绕单位轴 $K = (k_x, k_y, k_z)$，旋转角为 $\theta$，则对应的单位四元数为：

$$
q =
\left(
\cos\frac{\theta}{2},
\;
k_x \sin\frac{\theta}{2},
\;
k_y \sin\frac{\theta}{2},
\;
k_z \sin\frac{\theta}{2}
\right)
$$

单位四元数和旋转矩阵一一对应，具体表示略。

