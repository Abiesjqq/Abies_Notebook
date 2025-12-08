
We encounter AEC problems:

$$
\begin{aligned}
    &\min_{\boldsymbol{x}} f(\boldsymbol{x}) \\
    &\text{s.t.}\ \ \   h_i(\boldsymbol{x}) = \boldsymbol{a}_i^T\boldsymbol{x} - b_i = 0, \quad i = 1, \ldots, k
\end{aligned}
$$

i.e.

$$
\begin{aligned}
    &\min_{\boldsymbol{x}} f(\boldsymbol{x}) \\
    &\text{s.t.}\ \ \   \boldsymbol{Ax} = \boldsymbol{b}
\end{aligned}
$$

where $f$ is differentiable with $\operatorname{dom}f = \mathbb{R}^n, \boldsymbol{A}^T = (\boldsymbol{a}_1, \ldots, \boldsymbol{a}_k) \in \mathbb{R}^{n \times k}$, the feasible set is $\Omega = \boldsymbol{x}_0 + \operatorname{Null}(\boldsymbol{A})$.  
We assume the problem is feasible.

By observation, if $\boldsymbol{x}^*$ is a minimum of AEC, then

$$
\nabla f (\boldsymbol{x}^*)^T \boldsymbol{v}\geq 0 \Longrightarrow \nabla f (\boldsymbol{x}^*)^T \boldsymbol{v} = 0
$$

for all feasible direction $\boldsymbol{v}$, i.e. for $\boldsymbol{v} \in \operatorname{Null}(\boldsymbol{A})$ i.e. $\nabla f (\boldsymbol{x}^*) \perp \operatorname{Null}(\boldsymbol{A})$

!!! remarks "Proof"

    $$
    \nabla f (\boldsymbol{x}^*)^T \boldsymbol{v} = \lim_{t \to 0^+}\frac{f(\boldsymbol{x}^* + t\boldsymbol{v}) - f(\boldsymbol{x}^*)}{t} \geq 0
    $$

    And $\boldsymbol{v} \in \operatorname{Null}(\boldsymbol{A}) \Rightarrow - \boldsymbol{v} \in \operatorname{Null}(\boldsymbol{A})$, So $\nabla f (\boldsymbol{x}^*)^T \boldsymbol{v} = 0$

## Lagrange condition

If $\boldsymbol{x}^*$ is a local minimum of AEC, then there exists $\boldsymbol{\lambda}^* = (\lambda_1^*, \lambda_2^*, \ldots, \lambda_k^*)^T \in \mathbb{R}^k$ such that

$$
\nabla f(\boldsymbol{x}^*) + \boldsymbol{A}^T \boldsymbol{\lambda}^* = \nabla f(\boldsymbol{x}^*) + \sum_{i = 1}^{k}\lambda_i^* \nabla h_i(\boldsymbol{x}^*) = \boldsymbol{0}
$$

The constrains $\lambda_1^*, \lambda_2^*, \ldots, \lambda_k^*$ are called **Lagrange multipliers**

!!! remarks "Proof"

$\nabla f(\boldsymbol{x}^*) \in \operatorname{Null}(\boldsymbol{A})^\perp = \operatorname{Range}(\boldsymbol{A}^T)$, so there exists a $-\boldsymbol{\lambda}^*$ s.t. $\nabla f(\boldsymbol{x}^*) = -\boldsymbol{A}^T \boldsymbol{\lambda}^*$

### Lagrangian (Lagrange function)

We define Lagrangian By

$$
\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = f(\boldsymbol{x}) + \boldsymbol{\lambda}^T(\boldsymbol{Ax} - \boldsymbol{b}) = f(\boldsymbol{x}) + \sum_{i = 1}^k \lambda_i (\boldsymbol{a}_t^T \boldsymbol{x} - b_i)
$$

The optimality condition becomes the following **Lagrange condition** (**KKT equations**)

$$
\nabla \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^*) = \boldsymbol{0} \Longleftrightarrow \begin{cases}
    \nabla_{\boldsymbol{x}} \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^*) = \nabla f(\boldsymbol{x}^*) + \boldsymbol{A}^T\boldsymbol{\lambda}^* = \boldsymbol{0} \\
    \nabla_{\boldsymbol{\lambda}} \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^*) = \boldsymbol{Ax}^* - \boldsymbol{b} = \boldsymbol{0}
\end{cases}
$$

i.e. $(\boldsymbol{x}^*, \boldsymbol{\lambda}^*)$ is the stationary point of $\mathcal{L}$.

### Lagrangian and Convex Optimization

Suppose AEC is convex, i.e. $f$ is convex, then if there exists $\boldsymbol{\lambda}^*$ such that $(\boldsymbol{x}^*, \boldsymbol{\lambda}^*)$ satisfies the lagrange condition $\nabla \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^*) = \boldsymbol{0}$, then $\boldsymbol{x}^*$ is the global minimum of AEC

!!! remarks "Proof"

    For all $\boldsymbol{x} \in \Omega$,

    $$
    \nabla f(\boldsymbol{x}^*)^T (\boldsymbol{x} - \boldsymbol{x}^*) = -(\boldsymbol{\lambda}^*)^T\boldsymbol{A}(\boldsymbol{x} - \boldsymbol{x}^*) = -(\boldsymbol{\lambda}^*)^T (\boldsymbol{Ax} - \boldsymbol{Ax}^*) = \boldsymbol{0}
    $$

    So $\boldsymbol{x}^*$ is the global minimum

## Problems with general equality constrains

Consider the general equality constrained problem in $\mathbb{R}^n$ (GEC)

$$
\begin{aligned}
    &\min_{\boldsymbol{x}} f(\boldsymbol{x}) \\
    &\text{s.t.}\ \ \   h_i(\boldsymbol{x}) = 0, \quad i = 1, \ldots, k
\end{aligned}
$$

where $f$ and $h_i$ are all differentiable. ($h_i$ is not yet affine!) 

Suppose $\boldsymbol{x}^*$ is the local minimum. What if we linearize the constrains locally in the neighborhood of $\boldsymbol{x}^*$?

$$
\begin{aligned}
    &\min_{\boldsymbol{x}} f(\boldsymbol{x}) \\
    &\text{s.t.}\ \ \   \nabla h_i(\boldsymbol{x}^*)^T(\boldsymbol{x} - \boldsymbol{x}^*) = 0, \quad i = 1, \ldots, k
\end{aligned}
$$

We would expect that there exists $\boldsymbol{\lambda} \in \mathbb{R}^k$ s.t.

$$
\nabla f(\boldsymbol{x}^*) + \sum_{i = 1}^{k}\lambda_i^* \nabla h_i(\boldsymbol{x}^*) = \boldsymbol{0}
$$

### Optimization on 2D cycle

i.e. $h(\boldsymbol{x}) = \Vert \boldsymbol{x}\Vert^2 - 1 = 0$, by some calculation we can also get $\boldsymbol{x}^*$ is the minimum iff $\nabla \mathcal{L}(\boldsymbol{x}^*, \lambda^*) = \boldsymbol{0}$

### General equality constrains

Consider the general equality constraints in $\mathbb{R}^n$

$$
\boldsymbol{h}(\boldsymbol{x}) = \boldsymbol{O}
$$

where $\boldsymbol{h}(\boldsymbol{x}) = (h_1(\boldsymbol{x}), \ldots, h_k(\boldsymbol{x}))$.

Let $\boldsymbol{x}(t): [0, \varepsilon) \to \Omega$ be a feasible path starting at $\boldsymbol{x}_0$. We only observe around $\boldsymbol{x}_0$, a **tangent line $\tilde{T}_{\boldsymbol{x}_0}\Omega$** is 

$$
\boldsymbol{h}(\boldsymbol{x}_0) + \nabla \boldsymbol{h}(\boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) = \boldsymbol{0}
$$

, a **feasible direction** $\boldsymbol{x}'(0^+)$ and a **tangent space** $T_{\boldsymbol{x}_0}\Omega = \operatorname{Null}(\boldsymbol{h}'(\boldsymbol{x}_0))$ and **normal space** $N_{\boldsymbol{x}_0}\Omega = [T_{\boldsymbol{x}_0}\Omega]^\perp$  
Noting that for all path $\boldsymbol{x}(t)$ with $\boldsymbol{x}(0) = \boldsymbol{x}_0$, we have $\boldsymbol{h}(\boldsymbol{x}) \equiv \boldsymbol{0}$, then

$$
\boldsymbol{h}'(\boldsymbol{x}(0))\boldsymbol{x}'(0) = \boldsymbol{0}
$$

Let $F_{\boldsymbol{x}_0}\Omega$ be the set of feasible directions, then we know that

$$
F_{\boldsymbol{x}_0}\Omega \subseteq \operatorname{Null}(\boldsymbol{h}'(\boldsymbol{x}_0))
$$

such condition is not sufficient. We need a constraint qualification to ensure $F_{\boldsymbol{x}_0}\Omega = \operatorname{Null}(\boldsymbol{h}'(\boldsymbol{x}_0))$

#### Regular point and Critical point

A point $\boldsymbol{x}_0$ is a **regular point** of $\boldsymbol{h}$ if

$$
\boldsymbol{h}'(\boldsymbol{x}_0) = \begin{pmatrix}
    \nabla h_1(\boldsymbol{x}_0)^T \\
    \vdots \\
    \nabla h_k(\boldsymbol{x}_0)^T \\
\end{pmatrix}
$$

has full rank ($\nabla h_i(\boldsymbol{x}_0)^T$ are linearly independent).  
It is called **critical point** if it is not regular.

At a regular point $\boldsymbol{x}_0 \in \Omega$, 

$$
F_{\boldsymbol{x}_0}\Omega = \operatorname{Null}(\boldsymbol{h}'(\boldsymbol{x}_0))
$$

In this case $N_{\boldsymbol{x}_0}\Omega = \operatorname{span}\{\nabla h_1(\boldsymbol{x}_0), \ldots, \nabla h_1(\boldsymbol{x}_0)\}$

!!! normal-comment "Geometry"
    ![alt text](image.png){ style="width:50%; float:left" }
    ![alt text](image-1.png){ style="width:50%; float:right" }

    The left one is regular point and the right one is critical point.

**Lemma** If $\boldsymbol{x}_0$ is a regular point, then for any $\boldsymbol{v}$ s.t. $\boldsymbol{h}'(\boldsymbol{x}_0)\boldsymbol{v} = \boldsymbol{0}$, there exists a local path $\boldsymbol{x}(t)$ start from $\boldsymbol{x}_0$ s.t. $\boldsymbol{h}(\boldsymbol{x}(t)) = \boldsymbol{0}, \boldsymbol{x}_0'(0) = \boldsymbol{v}$.

!!! remarks "Proof of the lemma"

    Let

    $$
    \begin{aligned}
        \tilde{\boldsymbol{x}}(t, \boldsymbol{\alpha}) &= \boldsymbol{x}_0 + t\boldsymbol{v} + \boldsymbol{h}'(\boldsymbol{x}_0)^T \boldsymbol{\alpha} \\
        &= \boldsymbol{x}_0 + t\boldsymbol{v} + \sum_{i = 1}^k \alpha_i \nabla h_i(\boldsymbol{x}_0) \\
        \boldsymbol{F}(t, \boldsymbol{\alpha}) &= \boldsymbol{h}(\boldsymbol{x}(t, \boldsymbol{\alpha}))
    \end{aligned}
    $$

    we have

    $$
    \boldsymbol{F}(0, \boldsymbol{0}) = \boldsymbol{0}, \quad \frac{\partial \boldsymbol{F}(0, \boldsymbol{0})}{\partial \boldsymbol{\alpha}} = \boldsymbol{h}'(\boldsymbol{x}_0)\boldsymbol{h}'(\boldsymbol{x}_0)^T \succ \boldsymbol{O}
    $$

    (Since $\boldsymbol{h}'(\boldsymbol{x}_0)$ is full rank).  
    By the implicit function theorem, there exists $\boldsymbol{\alpha} = \boldsymbol{\phi}(t)$ for small $t$ s.t. $\boldsymbol{\phi}(0) = \boldsymbol{0}, \boldsymbol{F}(t, \boldsymbol{\phi}(t)) = \boldsymbol{0}$ and 

    $$
    \boldsymbol{\phi}'(0) = - \left[ \frac{\partial \boldsymbol{F}(0,0)}{\partial \boldsymbol{\alpha}} \right]^{-1}
    \frac{\partial \boldsymbol{F}(0,0)}{\partial t}
    =
    - \left[ \frac{\partial \boldsymbol{F}(0,0)}{\partial \boldsymbol{\alpha}} \right]^{-1}
    \boldsymbol{h}'(\boldsymbol{x}_0)\boldsymbol{v}
    = 0
    $$

    ($\boldsymbol{\phi}$ is the implicit function of $\boldsymbol{\alpha}$ in $\boldsymbol{F} = \boldsymbol{0}$) then

    $$
    \boldsymbol{x}(t)=\tilde{\boldsymbol{x}}\bigl(t,\boldsymbol{\phi}(t)\bigr)
    =\boldsymbol{x}_0+t\boldsymbol{v}+\boldsymbol{h}'(\boldsymbol{x}_0)^{T}\boldsymbol{\phi}(t)
    =\boldsymbol{x}_0+t\boldsymbol{v}+\sum_{i=1}^{k}\boldsymbol{\phi}_{i}(t)\nabla h_{i}(\boldsymbol{x}_0)
    $$

    satisfies the requirement.

!!! remarks "Proof of the theorem"

    According to the lemma, $\operatorname{Null}(\boldsymbol{h}'(\boldsymbol{x}_0)) \subseteq F_{\boldsymbol{x}_0}\Omega$.

!!! normal-comment "Implicit function theorem"

    If $\boldsymbol{F}:\mathbb{R}^{n+k}\to\mathbb{R}^{k}$ is continuously differentiable in a neighborhood of $(\boldsymbol{x}_{0},\boldsymbol{y}_{0})$ and satisfies

    $$
    \boldsymbol{F}(\boldsymbol{x}_{0},\boldsymbol{y}_{0})=\boldsymbol{0},\quad
    \det\frac{\partial\boldsymbol{F}(\boldsymbol{x}_{0},\boldsymbol{y}_{0})}{\partial\boldsymbol{y}}\neq 0
    $$

    then there exists a continuously differentiable function $\boldsymbol{y}=\boldsymbol{\phi}(\boldsymbol{x})$ defined in a neighborhood of $\boldsymbol{x}_{0}$ such that

    $$
    \begin{aligned}
        &\boldsymbol{F}\bigl(\boldsymbol{x},\boldsymbol{\phi}(\boldsymbol{x})\bigr)=\boldsymbol{0} \\
        &\frac{\partial\boldsymbol{\phi}(\boldsymbol{x})}{\partial\boldsymbol{x}}
        =-\left[\frac{\partial\boldsymbol{F}\bigl(\boldsymbol{x},\boldsymbol{\phi}(\boldsymbol{x})\bigr)}{\partial\boldsymbol{y}}\right]^{-1}
        \frac{\partial\boldsymbol{F}\bigl(\boldsymbol{x},\boldsymbol{\phi}(\boldsymbol{x})\bigr)}{\partial\boldsymbol{x}}
    \end{aligned}
    $$

### Lagrange condition in GEC

If $\boldsymbol{x}^*$ is a local minimum of $f$ (GEC) and it is a regular point of $\boldsymbol{h}$, then there exists Lagrange multipliers $\lambda_1^*, \ldots, \lambda_k^*$ s.t.

$$
\nabla f(\boldsymbol{x}^*) + \sum_{i = 1}^k \lambda_i^*\nabla h_i(\boldsymbol{x}_0) = \boldsymbol{0}
$$

!!! normal-comment "Note"

    This simply says $\nabla f(\boldsymbol{x}^*) \in N_{\boldsymbol{x}_0}\Omega = \operatorname{span}\{\nabla h_1(\boldsymbol{x}_0), \ldots, \nabla h_1(\boldsymbol{x}_0)\}$

And define the Lagrangian of GEC by

$$
\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = f(\boldsymbol{x}) + \lambda^T\boldsymbol{h}(\boldsymbol{x}) = \boldsymbol{f}(\boldsymbol{x}) + \sum_{i = 1}^k \lambda_i h_i(\boldsymbol{x})
$$

and the Lagrange condition $\nabla \mathcal{L}(\boldsymbol{x}^*, \boldsymbol{\lambda}^* = \boldsymbol{0})$

!!! warning-box "The condition is not sufficient!"