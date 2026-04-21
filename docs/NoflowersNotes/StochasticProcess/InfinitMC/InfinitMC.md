
## Infinite State Markov Chain

Given a MC, $\mathcal{F}_t = \sigma(X_1, \ldots, X_t)$. Obviously $\mathcal{F}_t \subseteq \mathcal{F}_{t + 1}$. We call $\{\mathcal{F}_t\}_{t = 1}^\infty$ a **filtration**

We call $Y$ is $\mathcal{F}_t$-measurable: If we know $X_1, \ldots, X_t$, then we can get the value of $Y$

### Strong Markov Property

A random variable $\tau$ is called a **stopping-time** if for all $n \in \mathbb{Z}$, $[\tau = n]$ is $\mathcal{F}_n$-measurable. (The probability of $[\tau = n]$ can be decide only by the information before $n$)


Given a sequence $X_0, \ldots$ on a same probability space, if for all **stopping-time** $\tau < \infty$ (it can be a random variable) s.t.

$$
\mathbb{P}[X_{\tau + 1} = x_1, \ldots, X_{\tau + k} = x_k|X_\tau = x_0] = \mathbb{P}[X_1 = x_1, \ldots, X_k = x_k | X_0 = x_0] 
$$

holds on a probability of $1$, then we call the random process has **strong probability**

> Markov property is equivalent to Strong Markov property in discrete MC

!!! examples "Example"

    $\displaystyle t_A = \min\{t \geq 0|X_t \in A\}$ is a stopping time

Let $C_n = \{(X_0, \ldots, X_n) = (y_0, \ldots, y_{n - 1}, x_0)\}$, then

$$
\begin{aligned}
    \mathbb{P}[X_{\tau + 1} = x_1 | C_\tau, \tau < \infty] &= \frac{\mathbb{P}[X_{\tau + 1} = x_1 \land C_\tau, \tau < \infty]}{\mathbb{P}[C_\tau]} \\
    &= \frac{\sum_{n \geq 0}\mathbb{P}[X_{n + 1} = x_1 \land C_n \land \tau = n]}{\sum_{n \geq 0}\mathbb{P}[C_n \land \tau = n]} \\
    &= \frac{\sum_{n \geq 0}\mathbb{E}[\mathbf{1}[X_{n + 1} = x_1]\cdot \mathbf{1}[C_n \land \tau = n]]}{\sum_{n \geq 0}\mathbb{P}[C_n \land \tau = n]} \\
    &= \frac{\sum_{n \geq 0}\mathbb{E}[\mathbb{E}[\mathbf{1}[X_{n + 1} = x_1]\cdot \mathbf{1}[C_n \land \tau = n]|\mathcal{F}_n]]}{\sum_{n \geq 0}\mathbb{P}[C_n \land \tau = n]} \\
    &= \frac{\sum_{n \geq 0}\mathbb{P}[C_n \land [\tau = n]]\cdot \mathbb{E}[\mathbf{1}[X_{n + 1} = x_1|\mathcal{F}_n]]}{\sum_{n \geq 0}\mathbb{P}[C_n \land \tau = n]} \\
    &= \frac{\sum_{n \geq 0}\mathbb{P}[C_n \land [\tau = n]]\cdot \mathbb{P}[X_{n + 1} = x_1|X_n = x_0]}{\sum_{n \geq 0}\mathbb{P}[C_n \land \tau = n]} = P(x_0, x_1)
\end{aligned}
$$

### Infinite Markov Chain

Here we also define $P$ and $P(i, j) = \mathbb{P}[X_1 = j | X_0 = i]$ and $\mu_{t + 1}^T = \mu_t^T P$ (but not normal matrix multiply anymore)

And here **irreducible**: have a finite path from $i$ to $j$

We define $T_A = \min\{t \geq 0 | X_t \in A\}$. If $A = \{i\}$, we say $T_i = \min\{t \geq 0 | X_t = i\}$.  
We define $\mathbb{P}_i[A] = \mathbb{P}[A|X_0 = i]$ and $\mathbb{E}_i[X] = \mathbb{E}[X|X_0 = i]$  

$h_A(i) = \mathbb{P}_i[T_A < \infty]$，$e_A(i) = \mathbb{E}_i[T_A]$

!!! normal-comment "Another expression of Markov property"

    $$
    \forall A \in \sigma(X_t, X_{t + 1}, \ldots), \mathbb{P}[A|\mathcal{F}_t] = \mathbb{P}[A|X_t]
    $$

First step analysis:  

If $i \in A$, $h_A(i) = 1$  
If $i \notin A$, $h_A(i) = \sum_{j \in \Omega}P(i, j)h_A(j)$

!!! remarks "Proof"

    $$
    \begin{aligned}
        \mathbb{P}_i[T_A < \infty] &= \sum_j \mathbb{P}_i[T_A < \infty \land X_1 = j] \\
        &= \sum_j \mathbb{P}[X_1 = j] \cdot \mathbb{P}_i[T_A < \infty | X_1 = j] \\
        &= \sum_j P(i, j)\cdot \mathbb{P}[T_A < \infty | X_1 = j] \\
        &= \sum_j P(i, j) \cdot h_A(j)
    \end{aligned}
    $$

### Recurrent and Transient

We define $T_i^+ = \min\{t \geq 1 | X_t = i\}$. We say a state $i$ is **recurrent** when

$$
\mathbb{P}_i[T_i^+ < \infty] = 1
$$

If state $i$ is not recurrent, then we call it **transient**, i.e. $\mathbb{P}_i[T_i^+ < \infty] < 1$

The following are equivalent:  
- $i$ is recurrent  
- $\mathbb{P}_i[N_i = \infty] = 1$  
- $\mathbb{E}[N_i] = \infty$

here $\displaystyle N_i = \sum_{t = 0}^\infty \mathbf{1}[X_t = i]$

If $i$ is equivalent, and $P^t(j, i) \geq \alpha > 0$, we say $j$ is also recurrent.

!!! remarks "Proof"

    Firstly $\mathbb{P}_i[T_j < \infty] = 1$, and $\mathbb{P}_j[T_j^+ < \infty] \geq \mathbb{P}_j[T_i < \infty] \cdot \mathbb{P}[T_j < \infty] = 1$

    (??????)

### Recurrent in the Integer Chain

A integer chain: $P(i \to i + 1) = p, P(i + 1 \to i) = 1 - p$ and $P(0 \to 0) = 1 - p$.

We can prove that when $p \geq \dfrac{1}{2}$, the chain is transient; when $p < \dfrac{1}{2}$, the chain is recurrent.

In the recurrent cases, if $\mathbb{E}[T^+_{0}] = \infty$, then we call it **Null recurrent**; if $\mathbb{E}[T^+_{0}] < \infty$, then we call it **Positive recurrent**

When 



