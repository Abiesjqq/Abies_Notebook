## 射影几何

- **欧氏几何中的平面直线**：$ax + by + c = 0$

  - 多个方程对应同一条直线：
    $(ka)x + (kb)y + kc = 0, \forall k \neq 0$

- **平面直线的齐次表示**：$(a, b, c)^T \sim k(a, b, c)^T$

- **欧氏几何中的平面点**：$\mathbf{x} = (x, y)^T$

- **点的齐次表示**：

$$
\mathbf{x} = (x, y, 1)^T \quad (x, y, 1)^T \sim k(x, y, 1)^T, \forall k \neq 0
$$

- **齐次坐标**$(x_1, x_2, x_3)^T$，但只有 2 个自由度 (2DOF)

- **点在直线上**：$\mathbf{x}$在直线$l$上当且仅当：

$$
\mathbf{x}^T l = (x, y, 1)(a, b, c)^T = ax + by + c = 0
$$

- **两条直线$l$和$l'$的交点**：

$$
\mathbf{x} = l \times l'
$$

平行直线叉乘，最后一位为 0，表示无穷远点。  
所有无穷远点排成一条直线，称为**无穷远线**。

- **过两点$\mathbf{x}$和$\mathbf{x}'$的直线**：

$$
l = \mathbf{x} \times \mathbf{x}'
$$

- **二次曲线 (Conics)**

平面上由二阶方程描述的曲线：

$$
ax^2 + bxy + cy^2 + dx + ey + f = 0
$$

或齐次化形式：

$$
x \mapsto \frac{x_1}{x_3}, \quad y \mapsto \frac{x_2}{x_3}
$$

$$
ax_1^2 + bx_1x_2 + cx_2^2 + dx_1x_3 + ex_2x_3 + fx_3^2 = 0
$$

或矩阵形式：

$$
\mathbf{x}^T \mathbf{C} \mathbf{x} = 0 \quad \text{其中} \quad
\mathbf{C} =
\begin{bmatrix}
a & b/2 & d/2 \\
b/2 & c & e/2 \\
d/2 & e/2 & f
\end{bmatrix}
$$

系数构成六维向量${a,b,c,d,e,f}$，由于只考虑比值，自由度为 5。

- **五点定义一个圆锥曲线**

对于每个点，圆锥曲线经过：

$$
ax_i^2 + bx_iy_i + cy_i^2 + dx_i + ey_i + f = 0
$$

或

$$
\begin{pmatrix}
x_i^2 & x_iy_i & y_i^2 & x_i & y_i & 1
\end{pmatrix}
\mathbf{c} = 0, \quad \mathbf{c} = (a, b, c, d, e, f)^\top
$$

堆叠约束条件得到：

$$
\begin{bmatrix}
x_1^2 & x_1y_1 & y_1^2 & x_1 & y_1 & 1 \\
x_2^2 & x_2y_2 & y_2^2 & x_2 & y_2 & 1 \\
x_3^2 & x_3y_3 & y_3^2 & x_3 & y_3 & 1 \\
x_4^2 & x_4y_4 & y_4^2 & x_4 & y_4 & 1 \\
x_5^2 & x_5y_5 & y_5^2 & x_5 & y_5 & 1 \\
\end{bmatrix}
\mathbf{c} = 0
$$

## 射影变换

### 射影变换定义

射影变换是从 $P^2$ 到其自身的可逆映射 $h$，满足：三个点 $x_1, x_2, x_3$ 共线当且仅当 $h(x_1), h(x_2), h(x_3)$ 也共线。

一个映射 $h: P^2 \to P^2$ 是射影变换，当且仅当存在一个非奇异的 $3 \times 3$ 矩阵 $H$，使得对于任何由向量 $x$ 表示的 $P^2$ 中的点，都有 $h(x) = Hx$ 成立。

射影变换 (Projective transformation)

$$
\begin{pmatrix}
x'_1 \\
x'_2 \\
x'_3
\end{pmatrix}
=\begin{bmatrix}
h_{11} & h_{12} & h_{13} \\
h_{21} & h_{22} & h_{23} \\
h_{31} & h_{32} & h_{33}
\end{bmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
x_3
\end{pmatrix}
\quad \text{或} \quad
\mathbf{x'} = \mathbf{H} \mathbf{x}
$$

变换的层次结构：

1. 射影线性群 (Projective linear group)  
2. 仿射群 (Affine group) —— 最后一行是 `[0, 0, 1]`  
3. 欧几里得群 (Euclidean group) —— 左上角 2x2 子矩阵为正交矩阵  
4. 定向欧几里得群 (Oriented Euclidean group) —— 左上角 2x2 子矩阵行列式为 1

射影变换只保留直线，仿射中还保留平行、欧几里得变换还保留角度

相似形：经过相似变换（放缩、旋转、平移）后得到的图形  
射影变换可以分解为相似变换和切变的组合

### 无穷远线

$$
l_\infty' = \mathbf{H}^{-T} l_\infty = 
\begin{bmatrix}
\mathbf{A}^T & \mathbf{0} \\
-\mathbf{A}^T \mathbf{t} & 1
\end{bmatrix}
\begin{pmatrix}
0 \\ 0 \\ 1
\end{pmatrix}
= l_\infty
$$

无穷远线 $l_\infty$ 在射影变换 $\mathbf{H}$ 下保持不变，当且仅当 $\mathbf{H}$ 是一个仿射变换。
