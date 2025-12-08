## Terminology

**Approximation ratio:** an algorithm has an approximation ratio of $\rho(n)$ if cost $C$ (current algorithm) and $C^*$ (optimal algorithm) satisfies:

$$\max\left(\frac{C}{C^*},\frac{C^*}{C}\right)\le \rho(n)$$

The algorithm is called **$\rho(n)$-algorithm**.

**Approximation scheme:** an algorithm that takes as input both an instance and value $\varepsilon$, and is a 1-$\varepsilon$ algorithm.

**Polynomial-time approximation scheme (PTAS):** for any fixed $\varepsilon$, the algorithm runs in polynomial time. E.g., $O(n^{2/\varepsilon})$. Perturbation of $\varepsilon$ can greatly change time complexity. Therefore, PTAS is not an adequate discription.

**Fully polynomial-time approximation scheme (FPTAS):** for any fixed $\varepsilon$, the running time is both polynomial on $n$ and $1/\varepsilon$.

**Pseudo-polynomial approximation scheme (PPAS):** Consider the numeric value of the input parameters is N. PPAS's running time is polynomial in N, but not necessarily polynomial in the length of the input encoding ($\log N$).

## Examples

### Bin Packing

Given N items of sizes $S_1,\cdots,S_n$, such that $0 < S_i \le 1$ for all $1 \le i \le N$. Pack these items in the fewest number of bins, each of which has unit capacity.

!!! remarks "Next fit"

    **Next fit:** check if the previous bin can hold; create a new bin if not.

    Let M be the optimal number of bins. Next fit uses no more than 2M–1 bins. (Proof: $\text{size}(B_{2k-1})+\text{size}(B_{2k})>1$.)

!!! remarks "First fit"

    **First fit:** put in the first available bin; create a new bin if nif none of the existing bins can accommodate it.

    First fit uses no more than 17M/10 bins.

!!! remarks "Best fit"

    **Best fit:** put in a bin in the bin that leaves the minimum remaining space.

    Best fit does no better than first fit.

**On-line algorithm:** handle the current item before processing the next one. No on-line algorithm can always give an optimal solution.

**Off-line algorithm:** view the entire item list before producing an answer.

Thm.: There are inputs that force any on-line bin-packing algorithm to use at least 5/3 the optimal number of bins.

!!! remarks "First (or best) fit decreasing"

    **First (or best) fit decreasing:** sort the items into non-increasing sequence of sizes, then apply first (or best) fit.

    First (or best) fit decreasing uses no more than 11M/9+6/9 bins.

### Knapsack Problem

A knapsack with a capacity $M$ is to be packed. Given $N$ items. Each item $i$ has a weight $w_i$ and a profit $p_i$ . If $x_i$ is the percentage of the item $i$ being packed, then the packed profit will be $p_i x_i$. An optimal packing is a feasible one with maximum profit $\sum_{i=1}^n p_ix_i$ under the constrains $\sum_{i=1}^nw_ix_i\le M$ and $x_i\in [0,1]$.

**0-1 version of knapsack problem:** 0-1 knapsack is an NP-hard problem, because profits (and capacity) are exponential to the input length $\log_2 p_{max}$.

!!! remarks "Greedy solution"

    If we are greedy on profit, density or maximum profit density $p_i/w_i$, the approximation ratio is 2.

    ??? normal-comment "Proof"

        The item with maximum profit can always be include:

        $$p_{max}\le P_{greedy}\tag{1}$$

        The fractional version always do better than 0-1 version:

        $$p_{max}\le P_{opt}\le P_{frac}\tag{2}$$

        The remaining space in 0-1 version can't accomodate any item, whose profit is always less than max p:

        $$P_{frac}\le P_{greedy}+p_{max}\tag{3}$$

        Based on 1~3, $P_{opt}/P_{greedy}\le 2$.

!!! remarks "DP solution"

    **DP solution:** $W_{i,p}$ denotes the minimum weight of a collection from $\{1,\cdots, i \}$ with total profit being exactly $p$.

    $$
    W_{i,p} =
    \begin{cases}
    \infty & i = 0 \\
    W_{i-1,p} & p_i > p \\
    \min\{ W_{i-1,p},\, w_i + W_{i-1,p-p_i} \} & \text{otherwise}
    \end{cases}
    $$

    The running time is $O(np_{max})$, therefore it's a PPAS.

    What if $p_{max}$ is large? Round all profit values up to lie in smaller range.

### K-center Problem

Take a set of $n$ sites $s_1, \cdots, s_n$ as input. Select $K$ centers C so that the maximum distance from a site to the nearest center is minimized, i.e. the sum of covering radius is minimized.

The chosen do not need to lie within the set.(?)

!!! remarks "Greedy solution 1"

    **Greedy solution 1:** put the first center in the best possible location, and add centers to reduce covering radius. Bad if points are separated.

!!! remarks "Greedy solution 2"

    **Greedy solution 2:** If we know $r(C^*)$, then take s to be the center, radius $2r$ can cover all the sites covered by $C^*$.

    ```c
    Centers Greedy_2r(Sites S[], int n, int K, double r) {
        Sites S2[] = S[]; // S2 is the set of the remaining sites
        Centers C[] = EmptySet;
        while (S2[] != EmptySet ) {
            Select any s from S2 and add it to C;
            Delete all s2 from S2 that are at dist(s2, s) <= 2r;
        }
        if (|C| <= K)
            return C;
        else
            ERROR(No set of K centers with covering radius at most r);
    }
    ```

    Suppose the algorithm selects more than $K$ centers. Then for any set $C^*$ of size at most $K$, the covering radius is $r(C^*) > r$.

!!! remarks "Smarter solution: be far away"

    Always select a site with maximum distance from C.

    ```c
    Centers Greedy_2r(Sites S[], int n, int K, double r) {
        Sites S2[] = S[];
        Centers C[] = EmptySet;
        while (S2[] != EmptySet ) {
            Select s from S with maximum dist(s, C);
            Delete all s2 from S2 that are at dist(s2, s) <= 2r;
        }
        return C;
    }
    ```

    The algorithm returns a set C of K centers such that $r(C) \le 2r(C^*)$ where C* is an optimal set of K centers.

    Thm.: Unless P=NP, there's no $\alpha$-approximation for center selection problem for any $\alpha<2$.

    ??? normal-comment "Proof"

        **Dominating-Set problem:** A dominating set D of graph such that every vertex in the graph is either in D or adjacent to at least one vertex in D.

        If we can obtain a $(2-\varepsilon)$-approximation in polynomial time, then we can solve Dominating-Set (which is NP-complete) in polynomial time.

### Load Balancing

Input m identical machines and n jobs. Each job $j$ has a processing time $t_j$. Each job must be processed contiguously on exactly one machine and each machine can process only one job at a time.

Let $S[i]$ be the set of jobs assigned to machine $i$. The load of machine $i$ is $L[i] = \sum_{j \in S[i]} t_j$. The makespan of the schedule is the maximum load across all machines $L = \max_i L[i]$. Our goal is to assign every job to some machine so that the makespan $L$ is as small as possible.


!!! remarks "Listing scheduling"

    Listing scheduling is 2-approximation.

    ??? normal-coments "Proof"

        Let B denote the time for the last job, A denote the time for all other jobs, and OPT denote the optimal time.

        $OPT\ge A$ because the total time $T\ge mA+B$ and $OPT\le\frac{T}{m}$.

        $OPT\ge B$ because the last job must be allocated to a certain machine.

        Therefore, $OPT\ge \frac{A+B}{2}=T_{greedy}$.

!!! remarks "LPT rules"

**Longest processing time (LPT):** Sort n jobs in decreasing order of processing times; then run list scheduling algorithm.



## Homework

!!! examples "E.g.1"

    Given a 2-dimensional map indicating $N$ positions $p_i(x_i, y_i)$ of your post office and all the addresses you must visit, you'd like to find a shortest path starting and finishing both at your post office, and visit all the addresses at least once in the circuit. Fortunately, you have a magic item "Bamboo copter & Hopter" from "Doraemon", which makes sure that you can fly between two positions using the directed distance (or displacement).

    However, reviewing the knowledge in the ADS course, it is an NPC problem! Wasting too much time in finding the shortest path is unwise, so you decide to design a 2-approximation algorithm as follows, to achieve an acceptable solution.

    > Compute a minimum spanning tree T connecting all the addresses.
    > Regard the post office as the root of T.
    > Start at the post office.
    > Visit the addresses in order of a \_\_\_\_ of T.
    > Finish at the post office.

    There are several methods of traversal which can be filled in the blank of the above algorithm. Assume that $P \neq NP$, how many methods of traversal listed below can fulfill the requirement?

    - Level-Order Traversal
    - Pre-Order Traversal
    - Post-Order Traversal

    ---

    2.

!!! examples "E.g.2"

    You have 20 identical cores on which you want to schedule some $n$ jobs. Each job $j \in \{1, 2, \dots, n\}$ has a processing time $p_j > 0$. If $S_i$ is the set of jobs assigned to core $i$, let the load be $\sum_{j \in S_i} p_j$. Now, you want to partition the jobs among the cores to minimize the load of the most-loaded core.

    We design a greedy algorithm that picks any unassigned job, and assign it to the core with the least current load. What is the approximation ratio of the greedy algorithm? (Choose the smallest bound that applies.)

    A. 1
    B. 1.5
    C. 1.95
    D. 2

    ---

    C.

!!! examples "E.g.3"

    Consider the 0-1 knapsack problem with object weights $w$, profits $v$, and total weight limit $B$ (means that $w$ of any object is no larger than $B$.). In the class, we have learned that combining the greedy algorithm on maximum profit $v$ and maximum profit-weight ratio $v/w$ leads to an approximation algorithm which always produces a solution no less than $1/2$ of the optimal solution. Now let us consider the following simplified greedy algorithm. The algorithm first conducts the following sorting w.r.t. profit-weight ratio:

    > Sort all objects according to the profit-weight ratio $r_i = v_i / w_i$
    > so that $r_1 \ge r_2 \ge \dots \ge r_n$.

    Let the sorted order of objects be $a_1, \dots, a_n$. The next step is to find the lowest $k$ such that the total weight of the first $k$ objects exceeds $B$. Finally, we pick the more valuable of $\{a_1, \dots, a_{k-1}\}$ and $\{a_k\}$ as the final solution. Then which of the following arguments is correct:

    A. The algorithm always returns the optimal solution.
    B. The algorithm always returns a solution no less than $\alpha$ of the optimal solution, while $\alpha < 1/2$.
    C. The algorithm always returns a solution no less than $1/2$ of the optimal solution.
    D. The algorithm can generate a solution which is arbitrarily worse than the optimal solution.

    ---

!!! examples "E.g.4"

    For an approximation algorithm for a minimization problem, given that the algorithm does not guarantee to find the optimal solution, the best approximation ratio possible to achieve is a constant $\alpha>1$. (T/F)

    ---

    F. $\alpha$ is not always constant.
