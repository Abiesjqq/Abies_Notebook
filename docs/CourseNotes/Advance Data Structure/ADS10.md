## 图灵机

图灵机可视为无穷长的纸带和读写头。纸带上有无穷多个方格能存储数据（0，1 或空）。读写头能读取方格中存储的信息，由当前状态和内部指令集决定进行的操作，操作包含不变、修改、左移右移等。

图灵机分为确定性图灵机和非确定性图灵机。前者跳转时有明确的下一步的状态；后者没有确定的状态，从动作集中选择下一步的状态，但每次都能找到正确的选项。  
两种图灵机在覆盖空间上不同。假设一共 n 步操作，每次操作有 k 种选择，确定性图灵机需要 $k^n$ 步，而非确定性图灵机只要 k 步。  
但两者在解决问题的能力上没有区别。

## P/NP/NPC/NPH 问题

P 问题：多项式时间内可解的问题。

NP（Nondeterministic polynomial-time）问题：非确定性图灵机在多项式时间内可解的问题。如果给定 NP 问题的正确答案，可在多项式时间内验证。示例：哈密尔顿回路。  
并非所有可判定的问题都是 NP 问题。示例：“图中不存在哈密尔顿回路”。

P 问题是 NP 问题的子集，但不知道是否是真子集。

NPC（NP-complete）问题是 NP 问题中最难的问题，构成 NP 问题的边界。任何 NP 问题能够在多项式时间内被归约到 NPC 问题。

NPH（NP-hard）问题是最难的问题，所有 NP 问题都能在多项式时间归约到它。  
NPC 问题既是 NP 问题，也是 NPH 问题。NPC 和 NPH 的区别为 NPH 不一定能检查答案，因此不一定是 NP 问题；而 NPC 问题一定是 NP 问题，能检查答案且最难。

多项式规约建立了 NPC 问题之间的等价关系。如果等价的 NPC 问题找到了多项式时间的算法，则所有 NPC 问题都找到了多项式时间的算法。  
多项式规约：如果用多项式时间的变换将问题 1 变为问题 2，且问题 2 在多项式时间内可解，则问题 1 在多项式时间内可解。关键在于多项式时间的转化程序。  
要讨论的问题分为优化问题和判定问题，两者等价。判定问题的答案空间只有 0 和 1，每个优化问题都有对应的判定问题（如遍历判定的条件）。可以用判定问题简化优化问题。

!!! examples "示例 多项式规约"

    假设已知哈密尔顿回路问题是 NPC 问题，证明旅行商问题是 NPC 问题。

    哈密尔顿回路问题：给定图，是否存在包含所有顶点的回路？

    旅行商问题：给定完全图（任意两点之间都有边）和常数 k，是否存在权值和小于 k 的简单回路？

    ---

    首先，TSP 问题是 NP 问题。

    假设哈密尔顿回路中边的权值都为 1，补全为完全图，补上的边权值都为 2。则存在哈密尔顿回路当且仅当取 k 为原来图中边数时，存在旅行商的回路。

第一个 NPC 问题：Cook 定理，电路的可满足性定理。

## 形式化语言框架

抽象问题：从问题实例到问题答案的二元映射

Formal-language Theory：略。

A language L is decided by an algorithm A if every binary string in L is accepted by A and every binary string not in L is rejected by A.

P problem: there exists an algorithm A that decides L in polynomial time.

NP 问题的封闭性：L 是 NP 问题，L 的补集是否是 NP 问题？

co-NP 定义为补集操作下封闭的 NP 问题的集合。

一共有四种情况：

1. P = NP = co-NP
2. NP = co-NP != P
3. P = NP&&co-NP
4. P != NP&&co-NP

多项式规约也可用于语言。用 no harder than 表示语言 1 对应的问题不难与语言 2 对应的问题。

!!! examples "示例 多项式规约 2"

    假设已知子团问题是 NPC 问题，证明顶点覆盖问题也是 NPC 问题。

    子团问题：给定图和常数 k，是否存在包含 k 个顶点的完全子图（任意两点间都有边）？

    顶点覆盖问题：给定图和常数 k，是否存在数量为 k 的顶点集，使图中任意一条边必有顶点包含在这个顶点集内？

    ---

    首先，顶点覆盖问题是 NP 问题。

    图有大小为 k 的子团，当且仅当它的补图有大小为顶点数-k 大小的顶点覆盖。

## Homework

（存疑）

!!! examples "NP-hard 问题"

    If P = NP then the Shortest-Path (finding the shortest path between a pair of given vertices in a given graph) problem is NP-complete.（T/F）

    ---

    F。P=NP 或 P!=NP 不会改变归约关系。假设问题 L 原本不是 NP-hard 问题，即不能被任意 NP 问题在多项式时间内归约，那即使 P=NP，L 也不是 NP-hard 问题。

!!! examples "NP-complete 问题归约"

    here exists an NP-complete problem such that not all the NP problems can be polynomially reduced to it.（T/F）

    ---

    F。NPC 问题的定义是在 NP 中，且所有 NP 问题都能多项式归约到它。
