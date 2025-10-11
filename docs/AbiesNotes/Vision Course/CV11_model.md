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
所有无穷远点排成一条直线，称为无穷远线。

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

五个点能拟合一条二次曲线：

