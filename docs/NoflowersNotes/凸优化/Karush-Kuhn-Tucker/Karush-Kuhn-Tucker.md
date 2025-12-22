
Let $\boldsymbol{x} \in \mathbb{R}^n$ and $n \geq k$, consider

$$
\begin{aligned}
    &\min_{\boldsymbol{x}}f(\boldsymbol{x}) \qquad (\text{ICP})\\
    &\ \text{s.t.} \ \  h_i(\boldsymbol{x}) = 0,\ i = 1, \ldots, k \\
    & \quad \quad g_j(\boldsymbol{x}) \leq 0, \ j = 1, \ldots, m 
\end{aligned}
$$

and we assume the feasible set is $\Omega$  
Let $\boldsymbol{x}_0 \in \Omega$, the inequality constraint $g_j(\boldsymbol{x}_0) \leq 0$ is called **activate** if $g_j(\boldsymbol{x}_0) = 0$, or it's called **inactive**. Let

$$
\boldsymbol{J}(\boldsymbol{x}_0) = \{j: g_j(\boldsymbol{x}) = 0\}
$$

How to reduce to equality constrained problem?

A local minimum $\boldsymbol{x}^*$ of ICP is also a local minimum of the following:

$$
\begin{aligned}
    &\min_{\boldsymbol{x}}f(\boldsymbol{x}) \\
    &\ \text{s.t.} \ \  h_i(\boldsymbol{x}) = 0,\ i = 1, \ldots, k \\
    & \quad \quad g_j(\boldsymbol{x}) = 0, \ j \in \boldsymbol{J}(\boldsymbol{x}^*)
\end{aligned}
$$

since $\Omega_{\text{new}} \subseteq \Omega$!

![alt text](image.png){ style="width:40%" }

## Karush-Kuhn-Tucker (KKT) conditions

Let $\boldsymbol{x}^*$ be a local minimum of (ICP). If it is a regular point or all active constraints are affine, then there exist Lagrange multipliers $\lambda_1^*, \ldots, \lambda_k^*, \mu_1^*, \ldots, \mu_m^*$ s.t. the following KKT conditions hold:  
1. **stationarity** $\displaystyle \nabla f(\boldsymbol{x}^*) + \sum_{i = 1}^k \lambda_i^*\nabla h_i(\boldsymbol{x}^*) + \sum_{j = 1}^m \mu_j^*\nabla g(\boldsymbol{x}^*) = \boldsymbol{0}$   
2. **dual feasibility** $\mu_j^* \geq 0$  
3. **complementary slackness** $\mu_j^* g_j(\boldsymbol{x}^*) = 0$  

!!! normal-comment "Lagrangian"

    Condition 1 says $\nabla \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^*, \boldsymbol{\mu}^*) = \boldsymbol{0}$  
    Condition 3 says either $\mu_j^* = 0$ or $g_j(\boldsymbol{x}^*) = 0$

!!! remarks "Proof"

    For condition 1, just apply Lagrange condition and let $\mu_j^* = 0$ for all inactive $g_j$.

    For condition 2, assume there exists a $\mu_s < 0$. We will show we can move away from $\boldsymbol{x}^*$ so that feasibility is maintained but f decreases.  
    Due to $\nabla g_i$ are all linearly dependent, we can find a $\boldsymbol{v}$ that $\nabla g_i(\boldsymbol{x}^*)^T\boldsymbol{v} = 0 (i \neq s)$ (to ensure feasibility since it's tangent line) and $\nabla g_i(\boldsymbol{x}^*)^T\boldsymbol{v} < 0$ and lead to contradiction.

    Let $\boldsymbol{J}' = \boldsymbol{J}(\boldsymbol{x}^*) \setminus \{s\}$ and $S = \operatorname{span}\{\nabla h_i(\boldsymbol{x}^*), \nabla g_j(\boldsymbol{x}^*), j \in \boldsymbol{J}'\}$. $\nabla g_s(\boldsymbol{x}^8) \notin S$ since $\nabla g_j$ are linearly independent.

    So let $\boldsymbol{v} = -\nabla g_S(\boldsymbol{x}^*) - \mathcal{P}_S(-\nabla g_S(\boldsymbol{x}^*))$ then $\boldsymbol{v} \perp S$ and $\boldsymbol{v}^T \nabla g_s(\boldsymbol{x}^*) < 0$.  
    Then in KKT

    $$
    \begin{aligned}
    \boldsymbol{v}^T \nabla f(\boldsymbol{x}^*)
    &=
    \boldsymbol{v}^T
    \left(
    - \sum_{i=1}^{k} \lambda_i^* \nabla h_i(\boldsymbol{x}^*)
    - \sum_{j \in \boldsymbol{J}(\boldsymbol{x}^*)} \mu_j^* \nabla g_j(\boldsymbol{x}^*)
    - \sum_{j \notin \boldsymbol{J}(\boldsymbol{x}^*)} \underbrace{\mu_j^* \nabla g_j(\boldsymbol{x}^*)}_{=\,0}
    \right)
    \\[6pt]
    &=
    - \sum_{i=1}^{k} \lambda_i^*
    \underbrace{\boldsymbol{v}^T \nabla h_i(\boldsymbol{x}^*)}_{=\,0}
    \;-\;
    \sum_{j \in J'(\boldsymbol{x}^*)} \mu_j^*
    \underbrace{\boldsymbol{v}^T \nabla g_j(\boldsymbol{x}^*)}_{=\,0}
    \;-\;
    \mu_{j_0}^*
    \underbrace{\boldsymbol{v}^T \nabla g_{j_0}(\boldsymbol{x}^*)}_{<\,0}
    \\[6pt]
    &< 0.
    \end{aligned}
    $$

    so going through $\boldsymbol{v}$ will lead to a smaller $f$, contradiction!

!!! remarks "Normal cone"

    The normal cone of $F_{\boldsymbol{x}^*}\Omega$ is $N_{\boldsymbol{x}^*}\Omega$, the optimality condition says that 

    $$
    -\nabla f(\boldsymbol{x}^*) \in N_{\boldsymbol{x}^*}\Omega
    $$

    ![alt text](image-1.png){ style="width:60%" }

### Sufficiency of KKT conditions for convex problems

In ICP, assume $f, g_i$ are convex and $h_j$ are affine, if there exist $\lambda_1^*, \ldots, \lambda_k^*, \mu_1^*, \ldots, \mu_m^*$ s.t. the KKT condition is satisfied at a feasible $\boldsymbol{x}^* \in \Omega$, then $\boldsymbol{x}^*$ is a global **minimum**

!!! remarks "Proof"

It suffices to show $\nabla f(\boldsymbol{x}^*)(\boldsymbol{x} - \boldsymbol{x}^*) \geq 0$

$$
\begin{aligned}
    \nabla f(\boldsymbol{x}^*)(\boldsymbol{x} - \boldsymbol{x}^*) &= -\sum_{i} \lambda_i^* \nabla h_i(\boldsymbol{x}^*)^T(\boldsymbol{x} - \boldsymbol{x}^*) - \sum_{j \in \boldsymbol{J}(\boldsymbol{x}^*)}\mu_j^*\nabla g_j(\boldsymbol{x}^*)^T(\boldsymbol{x} - \boldsymbol{x}^*) \\
    &= -\sum_i \lambda_i^*(\underbrace{\boldsymbol{a}_i^T\boldsymbol{x} - \boldsymbol{a}_i^T\boldsymbol{x}^*}_{=0,\ h_i = \boldsymbol{a}_i^T\boldsymbol{x} - b_i}) - \sum_{j \in \boldsymbol{J}(\boldsymbol{x}^*)}\mu_j^*\nabla g_j(\boldsymbol{x}^*)^T(\boldsymbol{x} - \boldsymbol{x}^*) \\
    &\geq -\sum_{j \in \boldsymbol{J}(\boldsymbol{x}^*)}\mu_j^*(g_j(\boldsymbol{x}) - g_j(\boldsymbol{x}^*)), \quad g_j\text{ is convex} \\
    &\geq 0
\end{aligned}
$$

!!! examples "Power Location"

    $$
    \begin{aligned}
        \max_{P_1, \ldots, P_n}\ & \sum_{i = 1}^nW_i\log\left(1 + \frac{P_i}{N_i}\right) \\
        \text{s.t.}\ & \sum_{i = 1}^n P_i \leq P \\
        \ &P_i \geq 0 
    \end{aligned}
    $$

    The optimal solution should satisfy $\sum P_i = P$.

    The Lagrangian is 

    $$
    \mathcal{L}(\boldsymbol{P}, \lambda, \boldsymbol{\mu}) = - \sum_{i = 1}^nW_i\log\left(1 + \frac{P_i}{N_i}\right) + \lambda \left(\sum_{i = 1}^n P_i - P\right) - \sum_{i = 1}^n \mu_i P_i
    $$

    by the stationarity condition, 

    $$
    \partial_{P_i}\mathcal{L} = -\frac{W_i}{P_i + N_i} + \lambda - \mu_i = 0
    $$

    If $P_i = 0$, then $\displaystyle\mu_i = \lambda - \frac{W}{N_i} \geq 0$, so $\displaystyle\frac{W_i}{\lambda} - N_i \leq 0$  
    If $P_i < 0$, then $\mu_i = 0$, so $\displaystyle P_i = \frac{W_i}{\lambda} - N_i$.  
    So $\displaystyle P_i = \left(\frac{W_i}{\lambda} - N_i\right)^+$.

    It remains to solve $r$ from

    $$
    \sum_{i = 1}^n P_i = \sum_{i = 1}^n W_i\left(r - \frac{N_i}{W_i}\right) = P \quad r = \frac{1}{\lambda}
    $$

    and the LHS is a continuous, piecewise linear and strictly increasing, it has a unique solution and we can solve it easily.

    !!! remarks "It is the famous water filling solution!"

        ![alt text](image-2.png)

!!! examples "SVM"

The Lagrangian is

$$
\mathcal{L}(\boldsymbol{w}, b, \mu) = \frac{1}{2}\Vert \boldsymbol{w}\Vert^2 + \sum_{i = 1}^m \mu_i\left(1 - y_i(\boldsymbol{w}^T\boldsymbol{x}_i + b)\right)
$$

By the stationarity condition

$$
\boldsymbol{w}^* = \sum_{i = 1}^m\mu_i^* y_i\boldsymbol{x}_i
$$