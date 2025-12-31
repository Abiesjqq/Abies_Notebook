# Parallel Algorithms

## Introduction

### PRAM Model

PRAM is for designing algorithm.

In Parallel Random Access Machine (PRAM) model, there are $n$ processors sharing same memories. Each processor can interact with the memory (read/write/computation).

_How to resolve access conflicts?_

- EREW (Exclusive-Read Exclusive-Write): No two processors may read from or write to the same memory location.
- CREW (Concurrent-Read Exclusive-Write): Multiple processors may read the same memory simultaneously, but only one processor may write.
- CRCW (Concurrent-Read Concurrent-Write): Multiple processors may read from and write to the same memory location simultaneously, with arbitrary rule, priority rule or common rule.

### WD Model

WD is for analyzing complexity.

In the Work–Depth (WD) model, a parallel algorithm is characterized by two measures: work $W$ (the total number of operations performed), and depth $D$ (the length of the longest chain of dependent operations).

In parallel algorithm, all operations form a DAG (directed acyclic graph). Unconnected nodes can parallel, and connected nodes must operate in the direction of edge.

Work $W$ is the total numbers of nodes in DAG, and depth $D$ is the length of the longest directed path. WD does not care about exact number of working processors in each layer. Instead, it emphesis the overall $W$ and $D$. (If we consider the work of each layer in WD, there are no emplicit rule.)

_Use WD model to measure the performance?_

Two parameters:

- Work load $W(n)$: total number of operations;
- Worst-case running time $T(n)$: i.e. the depth in WD model.

Number of processors $p$ vs. total time:

- If $p=W(n)/T(n)$, then in PRAM model, $W(n)$ operations can be finished in $T(n)$ time.
- If $p\le W(n)/T(n)$, the total time is $W(n)/p$.

In general, **Brent's Theorem**:

$$T_p=O\left(\frac{W(n)}{p}+T(n)\right)$$

## Examples

### Summation Problem

Input $A(1)$ to $A(n)$, and output $A(1)+\cdots A(n)$.

!!! remarks "Summation Problem"

    **1. PRAM model**:

    Summing in the form of a binary tree. Each node sums its two children.

    ```c
    int parallel_sum_PRAM(int n) {
        // B[h][j] = value held by processor j at step h
        parallel_for (int i = 1; i <= n; i++)
            B[0][i] = A[i];

        for (int h = 1; h <= log2(n); h++) {
            parallel_for (int j = 1; j <= n / (1 << h); j++) {
                B[h][j] = B[h - 1][2 * j - 1] + B[h - 1][2 * j];
            }
        }

        return B[log2(n)][1];
    }
    ```

    Disadvantage: More processors are not in use in higher layers.

    ---

    **2. WD model**:

    ```c
    // returns sum of A[l..r], assume r-l+1 is power of 2 for simplicity
    int parallel_sum(int A[], int l, int r) {
        if (l == r)
            return A[l];
        int m = (l + r) / 2;

        int left, right;
        spawn left = parallel_sum(A, l, m);  // run in parallel
        right = parallel_sum(A, m + 1, r);   // run concurrently
        sync;                                // wait for spawned task

        return left + right;
    }
    ```

    _Seemingly no difference with PRAM...? Maybe the two models just care about different aspects x_x_

    - $T(n)=\log n+2$ (2 is initilization and output);
    - $W(n)=n+n/2+n/2^2+\cdots+n/2^k+1=2n$.

### Prefix-Sums

Input $A(1)$ to $A(n)$, and output $\sum_{i=1}^1 A(i), \sum_{i=1}^2 A(i),\cdots,\sum_{i=1}^n A(i)$.

!!! remarks "Prefix-Sums"

    **1. PRAM Model**:

    Def. $C(h,i)=\sum_{k=1}^{\alpha}A(k)$, where $(0,\alpha)$ is the rightmost descendant leaf of node $(h, i)$.

    Generate $C$ from $B$ (where $B(h,j)$ is the value held by processor $j$ at step $h$), from top to bottom:

    - First node in each step: $C(h,1)=B(h,1)$;
    - Even nodes in each step: $C(h,2k)=C(h+1,k)$;
    - Odd nodes except the first one in each step: $C(h,2k+1)=C(h+1,k)+B(h,2k+1)$.

    ---

    **2. WD Model**:

    - $T(n)=O(\log n)$;
    - $W(n)=O(n)$.

### Merging

Merge two non-decreasing arrays $A(1), A(2), \cdots , A(n)$ and $B(1), B(2), \cdots , B(m)$ into another non-decreasing array $C(1), C(2), \cdots , C(n+m)$.

To simplify, assume:

1. the elements of A and B are pairwise distinct;
2. $n = m$;
3. both $\log n$ and $n/\log n$ are integers.

!!! remarks "Partition"

    Partition the input into $p$ (a large number) independent small jobs, so that the size of the largest small job is roughly $n/p$. Do the small jobs concurrently, using a separate (possibly serial) algorithm for each.

    Specifically, in the merging problem, it's transferred into ranking problem: the rank of $j$-th element of array $B$ in array $A$ is

    $$
    RANK(j,A)=\begin{cases}
    0, &\text{if }B(j)<A(1) \\
    i, &\text{if }A(i)<B(j)<A(i+1) \\
    n, &\text{if }B(j)>A(n)
    \end{cases}
    $$

    Computation of $RANK(i,A)$ and $RANK(i,B)$ can be concurrent.

    The index in the final array is the sum of ranks in two arrays. Therefore the result $C$ can be represented as:

    ```c
    for (int i = 1; i <= n; i++) {
        C[i + RANK(i, B)] = A[i];
        C[i + RANK(i, A)] = B[i];
    }
    ```

    Given a solution to the ranking problem, the merging problem can be solved in $O(1)$ time and $O(n+m)$ work.

    ---

    _How to do the ranking?_

    ??? remarks "Binary Search"

        - $T(n)=O(\log n)$;
        - $W(n)=O(n\log n)$.

    ??? remarks "Serial Ranking"

        ```c
        i = j = 0;
        while (i <= n || j <= m) {
            if (A[i + 1] < B[j + 1])
                RANK(++i, B) = j;
            else
                RANK(++j, A) = i;
        }
        ```

        - $T(n)=W(n)=O(n+m)$.

    !!! remarks "Parallel Ranking"

        Assume $n=m$. Parallel ranking operates as below:

        Let $p=n/\log n$, divide into $p$ subproblems (If $p$ is too small, size of subproblems becomes too large; if $p$ is too big, cost of sampling becomes too large).

        1. Select a sample in every $\log n$ elements

        ```c
        A_Select[i] = A[1 + (i - 1) * log(n)]
        B_Select[i] = B[1 + (i - 1) * log(n)]
        ```

        2. Compute RANK for each selected element (using binary search).
        3. RANK for every element is determined by selected samples in both arrays. Combine subproblems.

        Let $p=n/\log n$. The first two steps divide the problem into at most $2p$ smaller sized $O(logn)$ subproblems.

        - For step 1, $T_1=O(\log n)$, $W_1=pT_1=O(n)$;
        - For step 2, $T_2=T_1=O(\log n)$, $W_2=2pT_2=O(n)$.

        Therefore, total depth and work is:

        - $T=O(\log n)$;
        - $W=O(n)$.

### Maximum Finding

Input $A(1)$ to $A(n)$, and output $\max\{A(1),\cdots ,A(n)\}$.

!!! remarks "Similar to Summation Problem"

    - $T=O(\log n)$;
    - $W=O(n)$.

!!! remarks "Compare all pairs"

    - $T=O(1)$;
    - $W=O(n^2)$.

!!! remarks "Doubly-logarithmic Paradigm"

    Operate in the follwoing three steps:

    1. Divide the array into $\sqrt{n}$ blocks, each of size $\sqrt{n}$.
    2. Concurrently compute the maximum of each block.
    3. Concurrently compute the maximum of $\sqrt{n}$ local maximums.

    $$T(n)\le T(\sqrt{n})+c_1,\quad W(n)\le \sqrt{n}W(\sqrt{n})+c_2 n.$$

    - $T(n)=O(\log\log n)$;
    - $W(n)=O(n\log\log n)$.

    The $W$ is not optimum.

    ---

    Improvement: Let $h=\log\log n$. Divide the array into $n/h$ blocks, each of size $h$.

    - $T(n)=O(\log\log n)$;
    - $W(n)=O(n)$.

### Random Sampling

weishenmezhemeduoliziaaabuxiangdazile

## Homework

!!! examples "E.g. T/F"

    When we solve the ranking problem via designing the parallel algorithms based on binary search, we shorten the worst-case running time but take more work loads comparing with the sequential algorithms.

    (T)

    ---

    In general, for a 3-way merge we need 6 input buffers and 2 output buffers for parallel operations.

    (T)
