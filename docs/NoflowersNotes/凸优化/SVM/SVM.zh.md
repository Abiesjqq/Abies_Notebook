## 支持向量机（Support Vector Machine, SVM）

给定一组样本点 $\boldsymbol{x}_i$ 以及二分类标签 $y_i \in \{0, 1\}, i = 1, \ldots, m$，希望找到一个超平面

$$
P: \boldsymbol{w}^T \boldsymbol{x} + b = 0
$$

把这两类样本尽可能“间隔最大”地分开。

!!! remarks "点到超平面的距离与间隔（margin）"

    **距离（distance）**：

    $$
    \mathrm{dist}(\boldsymbol{x}_i, P) = \frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert}.
    $$

    **间隔（margin）**：

    $$
    \min_{i} \mathrm{dist}(\boldsymbol{x}_i, P) = \min_i \frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert}.
    $$

硬间隔 SVM 的目标就是最大化这一最小间隔：

$$
\begin{aligned}
    &\max_{\boldsymbol{w}, b} \min_{1 \leq i \leq m}\frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert} \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) > 0.
\end{aligned}
$$

注意到，只要所有样本都被正确分类，$\boldsymbol{w}^T \boldsymbol{x}_i + b$ 的绝对尺度不会影响解。  
因此不妨假设

$$
\min_{1 \leq i \leq m} \vert \boldsymbol{w}^T \boldsymbol{x}_i + b\vert = 1,
$$

此时问题等价于

$$
\begin{aligned}
    &\max_{\boldsymbol{w}, b} \frac{1}{\Vert \boldsymbol{w} \Vert}
    \ \Longleftrightarrow\ 
    \min_{\boldsymbol{w}, b}\frac{1}{2}\Vert\boldsymbol{w}\Vert^2 \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) \geq 1.
\end{aligned}
$$

这是一个标准的凸优化问题。

## 软间隔 SVM（Soft Margin SVM）

当数据并非线性可分时，可以通过引入松弛变量（slack variables）$\boldsymbol{\xi} = (\xi_1, \ldots, \xi_m)$ 允许少量违约：

$$
\begin{aligned}
    &\min_{\boldsymbol{w}, b,\boldsymbol{\xi}}\ \frac{1}{2}\Vert\boldsymbol{w}\Vert^2 + C \sum_{i = 1}^m \xi_i \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) \geq 1 - \xi_i, \\
    &\qquad\qquad \boldsymbol{\xi} \geq \boldsymbol{0},\ C > 0.
\end{aligned}
$$

其中 $C$ 控制间隔最大化与误分类惩罚之间的权衡。

