# Greedy Algorithm

## Introduction

The Greedy Method: Make the best decision at each stage, under some greedy criterion. A decision made in one stage is not changed in a later stage, so each decision should assure feasibility.

Greedy algorithm works only if the local optimum is equal to the global optimum. It does not guarantee optimal solutions, but generally produces solutions that are very close in value (heuristics) to the optimal.

## Examples

### Activity Selection Problem

Given a set of activities $$S = \{ a_1, a_2, \cdots, a_n \}$ that wish to use a resource (e.g. a classroom). Each ai takes place during a time interval $[s_i, f_i)$. Activities $a_i$ and $a_j$ are compatible if $s_i \ge f_j$ or $s_j \ge f_i$ (i.e. their time intervals do not overlap).

Goal: Select a maximum-size subset of mutually compatible activities.

!!! remarks "DP Solution"

    Let $c_{ij}$ denote the maximum number of activities between $a_i$ and $a_j$. $S_{ij}$ denotes activities available between $a_i$ and $a_j$.

    $$
    c_{ij}=\begin{cases}
    0, &\text{if }S_{ij}\text{ is empty} \\
    c_{ik}+c_{kj}+1, &\text{if }a_k\in S_{ij}
    \end{cases}
    $$

!!! warning-box "Bad Greedy"

    1. Select the interval which starts earliest: Bad if a long activity starts early.
    2. Select the interval which is the shortest: Bad if it overlap with optimal ones.
    3. Select the interval with the fewest conflicts with other remaining intervals: Bad in overlapping cases.

!!! remarks "Greedy Solution"

    Select the interval which ends first (but not overlapping the already chosen intervals).

    **Thm.** Consider any nonempty subproblem $S_k$, and let $a_m$ be an activity in $S_k$ with the earliest finish time. Then $a_m$ is included in some maximum-size subset of mutually compatible activities of $S_k$.

    !!! normal-comment "Proof"

        Let $A_k$ be the optimal solution set, and $a_{ef}$ is the activity in $A_k$ with the earliest finish time.

        1. If $a_m=a_{ef}$, we are done.
        2. Else, $a_{ef}$ ends later than $a_m$. Replace $a_{ef}$ by $a_m$, and the result is better.

    Time complexity: sorting needs $O(\log N)$, selecting needs $O(N)$. Thus the total time complexity is $O(N\log N)$.

### Huffman Codes

Given a set of symbols and their corresponding frequencies (or probabilities), the Huffman coding problem asks for a prefix-free binary code that represents each symbol such that the expected (average) codeword length is minimized.

!!! remarks "Solution"

    Create a binary tree node for each character and insert all nodes into a min-heap.

    Repeat the following steps for (#nodes − 1) times:

    - Remove the node with the smallest frequency from the root of the min-heap and make it the left child of a new tree.
    - Remove the node with the second smallest frequency from the min-heap and make it the right child of the new tree.
    - Create a new root node whose frequency is the sum of the two children’s frequencies, and insert this new tree back into the min-heap.

    Time complexity: $O(N\log N)$.

    !!! normal-comment "Proof for Correctness"

        TO BE SUPPLEMENTED.

## Homework

!!! examples "T/F"

    - (F) All decidable problems are NP problems.
    - (T) All NP problems are decidable.
    - (T) All NP-complete problems are NP problems.
    - (T) All NP problems can be solved in polynomial time in a non-deterministic machine.
    - (F) If a problem can be solved by dynamic programming, it must be solved in polynomial time.
    - (T) If P = NP then the Shortest-Path (finding the shortest path between a pair of given vertices in a given graph) problem is NP-complete.
    - (F) Given that problem A is NP-complete. If problem B is in NP and can be polynomially reduced to problem A, then problem B is NP-complete.
    - (F) To prove problem B is NP-complete, we can use a NP-complete problem A and use a polynomial-time reduction algorithm to transform an instance of problem B to an instance of problem A.
