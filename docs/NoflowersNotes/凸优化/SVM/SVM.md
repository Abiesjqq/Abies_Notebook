
## Support vector machine (SVM)

Given a sets of points $\boldsymbol{x}_i$, and a classifier $y_i \in \{0, 1\}, i \in \{1, \ldots, m\}$, find a hyperplane $P: \boldsymbol{w}^T \boldsymbol{x} + b = 0$ which divide the points into two parts with the largest margin. 

!!! remarks "Distant and margin from a hyperplane"

    **Distance**: 

    $$
    \mathrm{dist}(\boldsymbol{x}_i, P) = \frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert}
    $$

    **margin**:

    $$
    \min_{i} \mathrm{dist}(\boldsymbol{x}_i, P) = \min_i \frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert}
    $$

The SVM maximizes the margin:

$$
\begin{aligned}
    &\max_{\boldsymbol{w}, b} \min_{1 \leq i \leq m}\frac{\vert\boldsymbol{w}^T \boldsymbol{x}_i + b \vert}{\lVert \boldsymbol{w}\rVert} \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) > 0
\end{aligned}
$$

Noting that the absolute value of $\boldsymbol{w}^T \boldsymbol{x}_i + b$ won't affect the solution. WLOG let $\displaystyle \min_{1 \leq i \leq m} \vert \boldsymbol{w}^T \boldsymbol{x}_i + b\vert = 1$. Then the problem turned to:

$$
\begin{aligned}
    &\max_{\boldsymbol{w}, b} \frac{1}{\Vert \boldsymbol{w} \Vert} \Leftrightarrow \min_{\boldsymbol{w}, b}\frac{1}{2}\Vert\boldsymbol{w}\Vert^2 \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) \geq 1
\end{aligned}
$$

Which is a convex problem!

## Soft margin SVM

For some datasets which are not linearly separable, we introduce a slack variables (松弛变量) $\boldsymbol{\xi} = (\xi_1, \ldots, \xi_m)$, 

$$
\begin{aligned}
    &\min_{\boldsymbol{w}, b}\frac{1}{2}\Vert\boldsymbol{w}\Vert^2 + C \sum_{i = 1}^m \xi_i \\
    &\ \mathrm{s.t.}\quad y_i(\boldsymbol{w}^T \boldsymbol{x}_i + b) \geq 1 - \xi_i\\
    &\qquad \ \ \boldsymbol{\xi} \geq \boldsymbol{0}, C > 0
\end{aligned}
$$
