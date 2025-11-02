## 矩阵乘法

一系列不同大小的矩阵相乘，顺序不同则时间不同。

令两矩阵 $M_{m\times n}$、$M_{m\times k}$ 相乘的时间为 $mnk$，第 i 个矩阵的大小为 $r_{i-1}\times r_i$。

$t_{i,j}$ 表示第 i 个到第 j 个矩阵相乘的最小时间。

$$
t_{i,j}=\begin{cases}
\displaystyle 0, & i==j \\
\displaystyle \min\limits_{i\le m\le j}\{t_{i,m}+t_{m+1,j}+r_{i-1}r_mr_j\}, & i<j
\end{cases}
$$

时间复杂度：状态数 $O(n^2)$ x 每个状态的转移代价 $O(n)$ = $O(n^3)$

## Homework

### 最优二叉查找树（OBST）

定义查找长度：如果在树中，则长度为这个节点深度 +1（最后的 1 用于和当前节点比较）；如果不在树中，则长度为叶子节点的深度 +1（最后的 1 用于判断空节点）。
即平均搜索长度为：

$$E = \sum_i p_i \times (\text{depth}(k_i) + 1)$$

最优二叉搜索树：给定一组数和每个数的访问概率 $p_i$，求二叉搜索树，使平均查找长度最小。即希望常查的关键字放得浅，不常查的放得深。

状态转移：

$$\text{cost}[i][j] = \min_{r=i}^{j} (\text{cost}[i][r-1] + \text{cost}[r+1][j]) + \text{sum}(p_i \ldots p_j)$$

其中 \(r\) 表示选作根的关键字；\(\text{sum}(p_i \ldots p_j)\) 表示这些节点在子树中的总概率。

<!--
!!! examples "一道判断题"

    The root of an optimal binary search tree always contains the key with the highest search probability. T/F.

    F. 虽然直觉上“概率最高的键应该放在最上面”，但实际情况取决于 全局结构和搜索概率分布。放在根节点的关键字必须在保持 BST 有序性的前提下，同时平衡左、右子树的整体代价。有时为了平衡左右两边的概率和深度，最优解的根并不是概率最高的键。
 -->

### 旅行商问题（TSP）

给定 $n$ 个城市 \(V = {0, 1, 2, \dots, n-1}\)，两两城市间距离 \(\text{dist}[i] [j]\)。旅行商必须从某个城市出发，访问每个城市恰好一次，最后回到起点。希望使总路程最短，即 $\text{dist}[\pi_0][\pi_1] + \text{dist}[\pi_1][\pi_2] + \cdots + \text{dist}[\pi_{n-1}][\pi_0]$ 最小，其中 $\pi_i$ 表示第 i 个经过的城市。

令 $dp[S] [i]$ 表示从起点 0 出发，访问完集合 \(S\) 中的所有城市（包含 0 和 i），并以城市 \(i\) 结尾的最短路径长度。

初始化：$dp[{0}][0] = 0$

状态转移：若我们当前到达城市 \( i\)，上一步一定来自 \(S\setminus{i}\) 的某个城市 \(j\)。故：

$$dp[S][i] = \min_{j \in S, j \ne i} (dp[S \setminus {i}][j] + dist[j][i])$$

TSP 的时间复杂度：

对于集合 \(S\) 的每个子集 $S_k$，你可能以集合中的任意一个城市结尾。因此状态数 $m$ 等于大小为 $k$ 的集合个数乘 $k$ 再求和。

$$m = \sum_{k=1}^{n} \binom{n}{k} \cdot k= n \cdot 2^{n-1}= O(n \cdot 2^n)$$

对于每个状态 \(dp[S] [i]\)，要考虑从哪个城市 \(j\) 转移过来。内层要枚举所有 \(j\in S\setminus{i}\)，最多有 \(n\) 个候选城市。因此每个状态的转移代价 = \(O(n)\)。

总时间复杂度等于状态数乘每个状态的转移代价。

$$TC= O(m \times \text{cost per state})= O(n^2 2^n)$$

<!--
!!! examples "一道判断题"

    If a problem can be solved by dynamic programming, it must be solved in polynomial time. T/F.

    F. 因为 TSP 的时间复杂度为 $O(n^2 2^n)$。
 -->

### 最长公共子序列

给定两个序列（如两个字符串）A 与 B，最长公共子序列是同时作为两者子序列的序列中长度最大的那个，求长度。

令 $dp[i] [j]$ 表示取 A 字符串前 $i$ 个字符、B 字符串前 $j$ 个字符时，最长公共子序列的长度。

状态转移：

$$
dp[i][j]=\begin{cases}
dp[i-1][j-1]+1, & A[i-1]==B[i-1] \\
\max(dp[i-1][j],\, dp[i][j-1]), & A[i-1]\neq B[i-1]
\end{cases}
$$
