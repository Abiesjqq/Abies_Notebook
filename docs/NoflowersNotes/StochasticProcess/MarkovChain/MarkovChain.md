
## Discrete Markov Chain

Given a sequence of variables $X_1, X_2, \ldots$, $X_i \in \Omega$ where $\Omega$ is a countable set. inference

$$
\forall a_0, \ldots a_t \in \Omega, \mathbb{P}[X_t = a_t | X_{t - 1} = a_{t - 1}, \ldots, X_0 = a_0] = \mathbb{P}[X_t = a_t | X_{t - 1} = a_{t - 1}]
$$

Then we call $\{X_t\}$ a Markov chain.

In a Markov chain, law of $X_{t + 1}$ is determined by $X_t$. Assume $X_t \in \Omega = [N]$, let matrix

$$
\boldsymbol{P}^{(t)}(i, j) \overset{\triangle}{=} \mathbb{P}[X_{t + 1} = j|X_t = i] = \boldsymbol{P}^{(t)}(j \to i)
$$

If $\boldsymbol{P}^{(t)}$ does not change with time $t$, then the Markov chain is called a **time-homogeneous** Markov chain.

$\boldsymbol{P}$ is called the transition matrix of the (time-homogeneous) Markov chain.  
So we can describe a (time-homogeneous) Markov chain by a **weighted directed graph** with $N$ vertices. The state change on the chain can be view as the random walk on the graph.

!!! normal-comment "By default we only consider time-homogeneous Markov chain."

At time $t$, we denote $X_t$'s law by $\boldsymbol{\mu}_t$, i.e.

$$
\forall i \in [N], \boldsymbol{\mu}_t(i) = \mathbb{P}[X_t = i]
$$

The according to the law of total probability, 

$$
\boldsymbol{\mu}_{t + 1}^T = \boldsymbol{\mu}_{t}^T\boldsymbol{P}
$$

and

$$
\boldsymbol{\mu}_t^T = \boldsymbol{\mu}_0^T\boldsymbol{P}^t
$$

!!! remarks "By observation"

    $$
    \boldsymbol{P}^t(i, j) = \mathbb{P}[X_t = j|X_0 = i]
    $$

    And

    $$
    \boldsymbol{P}^{s + t} = \boldsymbol{P}^s \boldsymbol{P}^t
    $$

    it is called Chapman-Kolmogorov Equation

### Stationary Distribution

If a distribution $\pi$ does not change under a Markov chain, i.e.

$$
\boldsymbol{\pi}^T = \boldsymbol{\pi}^T \boldsymbol{P}
$$

Then we call the distribution $\pi$ is $P$'s **stationary distribution** (S.D.).

!!! remarks "View a discrete distribution as a vector"

    Now if we introduce a distribution $\pi$, then

    $$
    \boldsymbol{\pi} = \begin{pmatrix}
        \mathbb{P}[X = 0] \\ \vdots \\ \mathbb{P}[X = N]
    \end{pmatrix}
    $$

**Markov Chain Monte Carlo (MCMC) Algorithm**:  
Design a Markov chain and let its stationary distribution be $\pi$.  
Begin with a distribution and simulate the chain for a few steps to get the final distribution $\mu_t$.  
We hope when $t$ is big enough, $\mu_t$ approaches $\pi$

### Existence of S.D.

If a S.D. $\pi$ exists, then $\boldsymbol{P}^T \boldsymbol{\pi} = \boldsymbol{\pi}$, i.e. $\boldsymbol{P}$ has a eigenvalue $1$.

Noting that $\boldsymbol{P}^T \boldsymbol{1} = \boldsymbol{1}$ by $\boldsymbol{P}$'s definition, so $\boldsymbol{P}^T$ has a eigenvector $\boldsymbol{v}$. Let $\boldsymbol{\pi} = |\boldsymbol{v}|/\Vert \boldsymbol{v}\Vert$.

Noting that 

$$
\pi(i) = \frac{1}{\Vert \boldsymbol{v}\Vert}\left|\sum_{j \in [N]}\boldsymbol{v}(j)\cdot \boldsymbol{P}(j \to i)\right| \leq \frac{1}{\Vert \boldsymbol{v}\Vert}\sum_{j \in [N]}|\boldsymbol{v}(j)|\cdot \boldsymbol{P}(j \to i) = \sum_{j \in [N]}\pi(i)\cdot \boldsymbol{P}(j \to i)
$$

### Uniqueness and Convergence