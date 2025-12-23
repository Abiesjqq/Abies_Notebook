## Examples

### Vertex Cover

Given a graph $G = (V, E)$, find a subset of nodes $S$ of minimal cardinality such that for each $(u, v) \in E$, either $u$ or $v$ (or both) are in $S$.

Neighbor relation: $S'$ denotes neighbors of $S$ if $S'$ can be obtained from $S$ by adding or deleting a single node. Each vertex cover S has at most n neighbors.

!!! remarks "Sol.1 Gradient descent"

    Start with $S = V$. If there is a neighbor $S'$ that is a vertex cover and has lower cardinality, replace $S$ with $S'$. Otherwise, terminate the algorithm.

    Algorithm terminates after at most $n$ steps.

    Cons:

    - Small steps: local optimum, but not always global optimum.
    - Large steps: longer running time.

!!! remarks "Sol.2 Other strategies"

    - Greedy Algorithms
    - Randomized Algorithms
    - Local Search (k-exchange / hill climbing)
    - LP Relaxation + Rounding
    - Branch and Bound (Exact Search)

### Metropolis Algorithm

Simulate behavior of a physical system.

Gibbs-Boltzmann function: The probability of finding a physical system in a state with energy $E$ is proportional to $e^{-E/kT}$, where $T > 0$ is temperature and $k$ is a constant.

### Hopfield Neural Networks

**Problem**: Graph $G = (V, E)$ with integer (positive or negative) edge weights $w$. Assign weights $s_u=\pm 1$ to nodes. If $w_{uv} < 0$, then $u$ and $v$ want to have the same state; if $w_{uv} > 0$ then $u$ and $v$ want different states.

In general, no configuration respects all constraints.

Def. "good": With respect to a configuration $S$, edge $e = (u, v)$ is **good** if $w_e \times s_u \times s_v < 0$.

Def. "satisfied": With respect to a configuration $S$, a node $u$ is **satisfied** if the weight of incident good edges is greater than the weight of incident bad edges.

$$\sum_{v: e=(u,v) \in E} w_e s_u s_v \le 0$$

Def. "stable": A configuration is **stable** if all nodes are satisfied.

**Goal**: Find a stable configuration, if such a configuration exists.

!!! remarks "Sol. State-flipping algorithm"

    Repeated flip state of an unsatisfied node.

    ```c
    Arbitraryly config S;
    while (current configuration is not stable) {
        Pick one unsatisfied node u;
        Flip state of u;
    }
    return S;
    ```

    Thm.: The state-flipping algorithm terminates with a stable configuration after at most $W = \sum_e | w_e |$ iterations.

    ??? normal-comment "Proof"

        Def potential function $\Phi(S)=\sum_{e,good}|w_e|$. $\Phi(S)$ increases by at least 1 after each flip.

        When u flips state:

        - all good edges incident to u become bad
        - all bad edges incident to u become good
        - all other edges remain the same

        Since $\Phi(S)<W$, the algorithm terminates at most $W$ iterations.

### Maximum Cut

Given an undirected graph $G = (V, E)$ with positive integer edge weights $w_e$, find a cut $(A, B)$ such that the total weight of edges crossing the cut $w(A,B)$ is maximized.

$$w(A,B)\triangleq \sum_{u\in A,v\in B}w_{uv}$$

!!! remarks "Sol. Local search"

Given a cut $(A, B)$, move one node from $A$ to $B$, or one from $B$ to $A$ if it improves the solution.

Thm.: Let $(A, B)$ be a locally optimal cut and let $(A^*, B^*)$ be an optimal cut. Then $w(A, B) \ge 1/2 \sum_e w_e \ge 1/2 w(A^*, B^*)$.

## Homework

To be supplemented.

!!! examples "True or false"

    In local search, if the optimization function has a constant value in a neighborhood, there will be a problem.

    T.

    ---

    In Metropolis Algorithm, the probability of jumping up depends on T, the temperature. When the temperature is high, it'll be close to the original gradiant descent method.

    F. Not close to.

    ---

    For an optimization problem, given a neighborhood, if its local optimum is also a global optimum, one can reach an optimal solution with just one step of local improvements.

    F?

!!! examples "Choice"

    Consider the Minimum Degree Spanning Tree problem: Given a connected undirected graph $G(V, E)$, find a spanning tree $T$ whose maximum degree over its vertices is minimized over all spanning trees of $G$. The problem can be shown to be NP-hard by reduction from the Hamiltonian Path Problem. On the other hand, we can use local search to design approximating algorithms. Denote $d(u)$ as the degree of vertex $u$ on a tree $T$. Consider the following algorithm:

    1.  Find an arbitrary spanning tree $T$ of $G$.
    2.  If there's some edge $e \in E(G)\setminus E(T)$ with endpoints $u, v$, and there's some other vertex $w$ on the path between $u, v$ on $T$ such that $\max\{d(u), d(v)\} + 1 < d(w)$, then we replace an edge $e'$ incident to $w$ on $T$ with $e$, i.e. $T := T \cup \{e\}\setminus\{e'\}$.
    3.  Repeat Step (2) until there's no edge to replace.

    It can be shown that this algorithm will terminate at a solution with maximum vertex degree $OPT + O(\log |V|)$. To show the algorithm will terminate in finite steps, a useful technique is to define a nonnegative potential function $\phi(T)$ and to show $\phi(T)$ is strictly decreasing after each step. Which of the following potential functions below satisfies the above requirements?

    - A. $\phi(T) = \sum_{v \in V} d(v)$.
    - B. $\phi(T) = \sum_{(u,v) \in E(T)} \max\{d(u), d(v)\}$.
    - C. $\phi(T) = \sum_{u \in V} \sum_{v \in V, v \neq u} \sum_{w \in V, w \neq u,v} \max\{d(u), d(v), d(w)\}$.
    - D. $\phi(T) = \sum_{v \in V} 3^{d(v)}$.

    ---

    D. In B and C, $w$ may not directly contribute to the potential.

!!! examples "Choice"

    **Scheduling Job Problem:** There are $n$ jobs and $m$ identical machines (running in parallel) to which each job may be assigned. Each job $j = 1, \cdots, n$ must be processed on one of these machines for $t_j$ time units without interruption. Each machine can process at most one job at a time. The aim is to complete all jobs as soon as possible; that is, if job $j$ completes at a time $C_j$ (the schedule starts at time 0), then we wish to minimize $C_{max} = max_{j=1,\cdots,n} C_j$. The length of an optimal schedule is denoted as $OPT(C_{max})$.

    **Local Search Algorithm:** Start with any schedule; consider the job $l$ that finishes last; check whether or not there exists a machine to which it can be reassigned that would cause this job to finish earlier. If so, transfer job $l$ to this other machine. The local search algorithm repeats this procedure until the last job to complete cannot be transferred. An illustration of this local move is shown in following figure.

    Which of the following statement is false?

    - A. $OPT(C_{max}) \geq \sum_{j=1}^{n} t_j / m$
    - B. When transferring a job, if we always reassign that job to the machine that is currently finishing earlier, then no job is transferred twice.
    - C. Upon the termination of the algorithm, the algorithm may return a schedule that has length at least $2OPT(C_{max})$
    - D. Suppose that we first order the jobs in a list arbitrarily, then consequently assign each job to the machine that is currently of earliest completion time, the schedule obtained cannont be improved by the local search procedure.

    ---

    C. "At least" should be no more than.
