## AVL 树

AVL 树的要求：二叉搜索树 + 左右子树的高度差的绝对值小于等于 1。

操作：LL，RR，LR，RL

**树高怎么定义？**

这里的树高相当于叶节点深度的最大值。空树的树高定义为-1，只有根节点的树的树高定义为 0。

**平衡因子怎么定义？**

平衡因子 BF 等于左子树的高度减右子树的高度。

**AVL 树中节点数和树高的关系？**

设 AVL 树的节点数量为 n，则树高为 $O(\log n)$。

为什么？给定树高，最大和最小节点数都为指数级。

最小节点数：各个节点的平衡因子尽量为 1 或 -1，$N_h=N_{h-1}+N_{h-2}+1$。定义斐波那契数列 $F_0=0, F_1=1$，则最小节点数 $N_h=F_{h+2}-1$。
最大节点数：树尽可能饱满，各节点的平衡因子为 0，$N(h)=2N(h-1)+1$

**插入时可能多个节点的平衡条件被破坏？**

可能插入节点到根节点的路径上，平衡全部被破坏。

**此时仍可以通过一次旋转恢复平衡？**

只需要调整距离最近的一个节点。因为旋转后调整了失衡的局部特征，使失衡不会向上传递。

**AVL 树的删除？**

按普通 BST 删除 --> 从下到上更新节点的高度 --> 沿着路径向上检测失衡并旋转恢复。

如果出现多个节点失衡，为什么在插入时只要调整一次，但删除时需要调整多次？删除中不能通过旋转使局部恢复平衡。

一次删除中，旋转次数最多为 $O(\log n)$ 次（因为向上传递，树高为 $O(\log n)$）。

**AVL 树相比于 Splay 树有什么缺点？**

1. 插入和删除至少 $O(\log n)$，旋转需要额外时间，摊还时间不能保证；
2. 多次访问同一个点没有优势。

## Splay 树

Splay 树的要求：每次访问后将访问的节点 splay 到根上。

操作：zig，zig-zag，zig-zig

**什么时候进行 splay 操作？**

1. 插入：插入后将插入的节点 splay 到根。
2. 查询：若成功查找到节点 x，则将 x 伸展到根；若查找失败，则将搜索路径的最后一个节点伸展到根。
3. 删除：找到删除的节点 x，将 x 伸展到根 --> 删除根节点后，得到两棵子树 L 和 R --> 若 L 非空，查找 L 中最大节点（这一步将最大节点伸展到根，得到的结果没有右子树） --> 将 R 作为右子树接上。

**zig，zig-zag，zig-zig 操作相比于普通旋转有什么区别？**

普通旋转指每次只调整访问的节点和其父亲节点。在顺序插入时，这种旋转后的树仍为链表。zig，zig-zag 操作和普通旋转相同，但 zig-zig 操作先转祖父节点、再转父节点。顺序插入再依次查找时，查找过程顺便将树高减半。

**摊还分析的三种方法？**

1. 聚合分析(aggregate analysis)：计算总成本除以操作次数。
2. 核分析（accounting method）：给每个操作分配摊还费用，多余的费用作为 credit。每个操作对 credit 的影响等于摊还费用减实际成本。需要保证 credit 大于零。
3. 势能分析（potential method）：对状态定义势能函数，总摊还成本等于实际成本加势能的变化量。

esp. Multipop stack 的分析：

1. 聚合分析：分析得到总时间为 $O(n)$。
2. 核分析：定义 push 的费用为 2，pop 和 multipop 的费用为 0。
3. 势能分析：定义势能函数为栈中元素个数。

**Splay 树的势能分析？**

定义势能函数为 $\Phi(T)=\sum_{i\in T}\log S(i)=\sum_{i\in T}Rank(i)$，其中 $S(i)$ 表示以 i 为根（包括 i）的子树中节点个数，$Rank(i)=\log S(i)$。

结论：将节点 x 伸展到根的最大摊还代价是 $3(Rank_2(x)-Rank_1(x))+1$。

**为什么不能用树高作为 Splay 树的势能函数？**

Splay 操作会导致树高剧烈变化，树高变化与单次操作的复杂度没有互补关系，每次操作的树高变化没有上界。

**例题**

势能函数需要使实际成本最大的那一步，势能变化为负值且变化大，两者相加后将这一步的摊还成本控制在一定范围内。

!!! examples "势能函数的选择 1"

    A queue can be implemented by using two stacks SA and SB as follows:

    - To enqueue x, we push a onto SA.
    - To dequeue from the queue, we pop and return the top item from SB. However, if SB is empty, we first fill it (and empty SA) by popping the top item from SA, pushing this item onto SB, and repeat until SA is empty.

    Assuming that push and pop operations take $O(1)$ worst-case time, please select a potential function $\Phi$ which can help us prove that enqueue and dequeue operations take $O(1)$ amortized time(when starting from an empty queue).

    A. $\Phi= 2|SA|$
    B. $\Phi= |SA|$
    C. $\Phi= 2|SB|$
    D. $\Phi= |SB|$

    ---

    实际成本最大的步骤为 SB 为空时的 pop，此时实际成本为 $2|SA|$，因此这一步的势能变化应为 $-2|SA|+C$。选A。

!!! examples "势能函数的选择 2"

    You are to maintain a collection of lists and to support the following operations.

    1. insert(item, list): insert item into list (cost = 1).
    2. sum(list): sum the items in list, and replace the list with a list containing one item that is the sum (cost = length of list).

    We show that the amortized cost of an insert operation is $O(1)$ and the amortized cost of a sum operation is $O(1)$. If we assume the potential function to be the number of elements in the list, which of the following is FALSE?

    A. For insert, the actual cost is 1.
    B. For insert, the change in potential is 1. The amortized cost is 2.
    C. For sum, the actual cost is k.
    D. For sum, the change cost is 2 − k. The amortized cost is 2.

    ---

    actual cost 表示实际成本，amortized cost 表示摊还成本。

    AB：插入的实际成本为 1，势能变化为 1，摊还成本为 2。
    CD：设 list 的长度为 k。sum 的实际成本为 k，势能变化为 -(k-1)，摊还成本为 1。

    选 D。

## 红黑树

红黑树的要求：节点红或黑，根节点黑，NIL 黑，红色节点不相邻，每个节点到任意 NIL 的路径上黑色节点数相同。

**红色节点的子节点一定都是 NIL 或都不是 NIL？**

假设只有一个是 NIL，则根节点到这个 NIL 的距离和经过另一个黑色孩子到 NIL 的距离不相等，违反黑高特性。

**红黑树中节点数和树高的关系？**

设红黑树的节点数量为 n，则树高最大为 $2\log_2 (n+1)$。

为什么？设 $bh$ 表示黑高，$bh\le \frac{h}{2}$，根节点到所有 NIL 的长度至少为 $bh$，故 $N\ge 2^{bh}-1$，化简得到上式。

课件中的证明：归纳法。首先，只有 NIL 节点时 $bh$ 为零，总节点数为零。归纳对于任意高度为 $k+1$ 的节点 x，它孩子的黑高为 $bh(x)$ 或 $bh(x)-1$，故子树节点数 $size(child) \ge 2^{bh(child)}-1\ge 2^{bh(x)-1}-1$，以当前节点为根的子树总节点数 $size(x)\ge 1+2size(child)=2^{bh(x)}-1$。

另外，从某节点到其后代叶节点的所有简单路径中，最长的一条路径的长度至少是最短一条的 2 倍。

**红黑树的插入？**

插入节点默认红色节点，按二叉搜索树特性找到插入位置。只可能违反红色节点不相邻的条件，即父亲为红色。

1. 叔叔也为红色：父亲、叔叔这一层变为黑色，爷爷变为红色，上移判断。
2. 叔叔为黑色，且爷爷-父亲-插入节点为 LR 或 RL：一次旋转，转为第三种。
3. 叔叔为黑色，且爷爷-父亲-插入节点为 LL 或 RR：上面的红色节点和爷爷颜色互换，再将父亲转到根。

**红黑树中，从空树开始连续插入 n 个节点（n>1），一定会出现红色节点吗？**

会。n=2 时有红色节点。再继续插入，插入为红色节点，调整过程中红色节点保留。

**红黑树的删除？**

只考虑删除节点有一个孩子的情况。此时问题为删除节点为黑色，且子节点为黑色或 NIL。

将删除后接替的节点定义为双黑节点。

1. 兄弟是红色：兄弟和父亲颜色互换，将兄弟转到父亲的位置，转为 234 中的一种。
2. 兄弟是黑色，且兄弟的孩子都是黑色：双黑和兄弟这一层黑度减一（兄弟变红），双黑的一个黑度上移到父亲。
3. 兄弟是黑色，兄弟有孩子是红色，且父亲-兄弟-红孩子为 LR 或 RL：红孩子和兄弟的颜色互换，红孩子向上转到兄弟的位置，转为情况 4。
4. 兄弟是黑色，兄弟有孩子是红色，且父亲-兄弟-红孩子为 LL 或 RR：将兄弟和父亲颜色互换，兄弟转到根，红孩子染黑（补偿原来兄弟的黑色），双黑变单黑（路径上增加了原来兄弟的黑色）。

情况 34 中 4 优先。

如果要删除节点为 x 且 x 的孩子均为黑，则双黑标记在 x 的位置。

红黑树删除的时间复杂度：最多 3 次旋转（1->3->4），情况 2 中向上推进的次数最多为树高 $O(\log n)$，故删除的 TC 为 $O(\log n)$。

**红黑树中旋转次数？**

插入最多 2 次，删除最多 3 次。

## B+ 树

B+ 树的要求：对 M 阶 B+ 树，根节点有 2~M 个孩子，非叶节点有 $\lceil\frac{M}{2} \rceil$~M 个孩子，所有叶节点在同一层。

**B+ 树中节点的含义？**

所有非叶节点中的元素仅用于查找。所有实际值都按从小到大的顺序存储在叶节点中。

如果某节点有 n 个孩子，则该节点内部有 M 个指针和 M-1 个数值。指针的前 n 个分别指向 n 个孩子，数值的前 n-1 个中第 i 个元素表示第 i+1 个孩子的最小值（第一个值）。

**B+ 树的查找？**

检查非叶节点中的数值，如果大于等于当前值、小于下一个值，就移动到对应的孩子。

**B+ 树的插入？**

先找到插入的位置，判断是否需要分裂。

叶节点的分裂：如果叶节点中元素为 M+1 个，则在 $\lceil\frac{M}{2} \rceil$ 个元素右边分割，将右叶子第一个元素上移到父节点，并在父节点中增加指向右叶子的指针。

中间节点的分裂：第 $\lceil\frac{M}{2} \rceil$ 个元素上移到父节点作为索引。

根节点的分裂：第 $\lceil\frac{M}{2} \rceil$ 个元素上移作为新的根，其余分裂为两个节点（左子树和右子树）。

<span style="color:red">（存疑？）插入时即使不分裂也可能需要更新上层节点。</span>

**B+ 树插入和查询的时间复杂度？**

M 阶 B+ 树共 $O(\log_{\lceil M/2 \rceil}N)$ 层，每次操作最多改变一组叶节点，数量为 $O(M)$，故整体时间复杂度为 $O(\frac{M}{\log M}\log N)$。

查询的时间复杂度等于树高，即 $O(\log_MN)$，课件中写的是 $O(\log N)$。

## 倒排索引

倒排索引的结构：对每个关键词，包含一系列指向它出现在文档中位置的指针，表示为 <次数; (文档 1, 位置 1); (文档 2, 位置 2); …>，成为 posting list。

“倒排”的含义为是针对每个 term，而不是针对 document。

**倒排索引之前的想法？**

Term-Document Incidence Matrix：每个单词分配二进制序列，1 表示在文档中。多关键词搜索时，对二进制序列做与运算。

缺点：矩阵太稀疏，浪费空间。

**为什么需要记录出现的总次数？**

多关键词搜索时，优先用出现次数少的。

**添加索引的流程？**

Token Analyzer, Stop Filter --> Vocabulary Scanner -> Vocabulary Inserter --> Memory Management.

读到一个词后：Word Stemming --> Stop Words

**在索引中搜索一个词？**

1. Search trees：B 树、B+ 树、Tries
2. hashing：优点为查询、插入、删除速度快，缺点为不支持范围查询、最坏情况退化为 O(n)、动态扩容代价大，随机访问不适合磁盘。

**内存满了怎么办？**

文档分批处理，内存分块。内存满时将这块内存写到磁盘，清空并处理下一个块。最后将所有块外部合并（归并），得到最终的倒排索引。

内存块指当内存中的倒排索引达到预设容量时，这一批处理过的倒排列表就成为一个块，写到磁盘去。

**索引的分配？**

每个 node（计算机）存储整个倒排索引的一部分。

1. Term-partitioned index：按词汇的编号划分
2. Document-partitioned index：按文档的编号划分

**动态索引？**

主索引极大，通常已经写死在磁盘上，顺序存储、压缩优化、不可修改。

在 main index 之外新增 auxiliary index，搜索时同时在两边搜。

什么时候合并主索引和辅助索引？辅助索引达到一定大小，或定时合并，或 LSM Tree 原理分层合并（略）。

怎么删除文档？使用 delete-bit（删除标记），将删除的文档也写入辅助索引。合并时在磁盘中删除。

**压缩存储空间？**

先去除停用词，将所有的词汇放在同一个存储块内，词汇之间没有任何间隔（类似字符串）。为了从字符串中分离出词汇，需要另一张小的表记录每个词汇开头的位置。每个词汇的索引记录相邻词汇开头的差分。

**设置阈值？**

文档截断阈值、查询词阈值

**评价检测性能？**

1. 精确度（precision）：检索到的有意义的文档占所有检索到文档的比例。
2. 召回率（recall）：检索到的有意义的文档占所有有意义的文档的比例。

## 左偏堆

定义零路径长（Npl）：节点到一个没有两个儿子的节点的最短路径的长。具有 0 个或 1 个儿子的节点的 Npl 为 0，null 的 Npl 为-1。每个节点的 Npl 等于它的两个孩子的 Npl 的最小值 +1。

左偏堆的要求：每个节点的左孩子的 Npl 都要大于等于其右孩子的 Npl

**最右路径节点数和总节点数的关系？**

最右路径上 $r$ 个节点，则总节点数至少为 $2^r-1$。

反过来，总节点数为 $N$，最右路径最多有 $\lfloor \log(N+1)\rfloor$ 个节点。

**普通堆合并的时间复杂度？**

$O(n)$（先合并两数组，再从后往前调整）。

和搜索树不同，堆不需要查询操作。左偏堆中最右路径尽可能短，所有合并只要在右路径上进行，左边的节点不会被访问到。

**左偏堆的合并？**

（详见“左偏堆，斜堆”部分。）

1. 递归合并：从根较小的堆（o）开始，每次有两个待合并的堆，分别为 o 的右儿子和另一个左偏堆。将这两者中根较小的作为 o 的右儿子。从下往上（递归顺序）检查是否违反左偏性质，调整并更新 Npl。
2. 迭代合并：用栈存储合并的父节点，合并完后弹栈调整。

递归深度为两个堆最右路径长度之和，而每一层操作为常数。总 TC 为 $O(\log N_1+\log N_2)=O(\log\sqrt{N_1N_2})=O(\log(N_1+N_2))$。

## 斜堆

斜堆的要求：每次合并后交换左右孩子。不考虑 Npl。

**斜堆的合并？**

从根较小的堆（o）开始，每次有两个待合并的堆，分别为 o 的右儿子和另一个左偏堆。将这两者中根较小的作为 o 的右儿子。从下往上交换左右孩子。

也可理解为先左右交换，再在左边合并。

**斜堆的摊还分析？**

定义重节点（heavy node）：该节点右子树的节点个数大于等于所有后代（包括自身）的一半。否则为轻节点（light node）。

可证明，若最右路径上有 l 个轻节点，则整个斜堆至少有 $2^l-1$ 个节点。即最右路径上轻节点的个数为 $O(\log N)$。（归纳法证明）

定义势能函数：$\Phi(T)$ 为 T 中重节点的个数。

合并后只有最右路径上轻重会变，且重节点一定变化轻节点、轻节点不一定变为重节点。故一侧操作的均摊成本至多为原先两个堆的最右路径上轻节点的个数，即 $O(\log N)$。

## 二项队列

二项树：首先需要满足堆序性（这里默认最小堆）。定义单个节点的高度为 0，k 阶二项树由一个 k-1 阶二项树连接到另一 k-1 阶二项树的根节点构成。

二项队列：一系列阶数不同的二项树构成的森林。

**查询最小值的时间复杂度？**

最小值一定是某个二项树的根，一共 $O(\log N)$ 个二项树，故 TC 为 $O(\log N)$。

如果额外记录全局最小值，则查询的 TC 为 $O(1)$，但需要另外维护这个值。

**插入的时间复杂度？**

插入相当于二进制下加一。

设最小的不存在该阶数的二项树的数值为 i，则这次插入的时间为 $const.\times (i+1)$，最坏时间为 $O(\log N)$。  
但对于 k 阶二项树，只可能被创建 $\frac{N}{K}$ 次，总代价为 $O(N)$，故摊还代价为 $O(1)$。

或势能分析：定义势能函数 $\Phi$ 为合并后二项树的数量。

**二项队列的删除？**

遍历根节点，找到最小值 --> 删除这个根节点，将剩余二项树和删除后子树合并。

**二项树怎么合并？**

第 i 个二项树是 i-1 叉树，用 LeftChild-NextSibling 方式表示。

T2 连接到 T1 上（相当于从左边连接）：

```c
T2 -> NextSibling = T1 -> LeftChild;
T1 -> LeftChild = T2;
```

## 回溯法

**回溯法过程的表示？**

令 $S_k$ 表示第 $k$ 步下所有可能的选择，用 $(x_1, x_2,\cdots,x_i)$ 表示当前的部分解，其中 $x_k\in S_k$。选择 $x_{i+1}\in S_{i+1}$ 加入部分解，检查是否符合条件。符合则继续，不符合则回到 $(x_1, x_2,\cdots,x_i)$，选择新的 $x_{i+1}'$。

??? normal-comment "回溯法 template"

    ```c
    bool Backtracking(int i) {
        Found = false;
        if (i > N)
            return true; // (x1, …, xN) 为成功解
        for (each xi in Si) {
            OK = Check((x1, …, xi), R);  // 检查条件，不满足则剪枝
            if (OK) {  // 满足则继续构造
                Count xi in;
                Found = Backtracking(i + 1);
                if (!Found)
                    Undo(i); // 下一步不满足则回到 (x1, …, xi-1)
            }
            if (Found)
                break;
        }
        return Found;
    }
    ```

## 八皇后问题

**解的表示？**

$Q_i$ 表示第 i 行的皇后，$x_i$ 表示 $Q_i$ 所在的列。Solution 表示为 $(x_1, x_2,\cdots,x_8)$。

Solution space 指 solution 的所有可能情况的数量（不一定满足所有条件）。

课件中画出博弈树便于理解。实际不用构造树。

## 博弈树

**树、剪枝的表示？**

边表示操作，节点表示状态。所有从根到叶节点的路径即 solution space。

黑色节点表示剪枝。如果一个节点标黑，则它所有的孩子都不用遍历，直接跳到同一层的下一个节点。如果一个节点的所有孩子都被标黑，则这个节点也标黑。

博弈树中深度优先搜索等价于后序遍历。

**遍历的顺序？**

如果不同步骤 ​$S_i$ 的可选项数量不同，应优先处理可选项数量较少的步骤，因为这样能更快发现冲突并进行剪枝、减少搜索空间。

## 收费公路问题

已知 $N$ 个收费站排列在 x 轴，且第一个位于 x=0，给出两两间距离（共 $N(N-1)/2$ 个），求各个收费站的位置。

每次取剩余的最大距离，对应的收费站到第一个或最后一个的距离为这个最大值。假设一种情况，计算和已知所有收费站的距离，当距离超出时回溯。

??? normal-comment "示例代码"

    ```c
    bool Reconstruct(DistType X[], DistSet D, int N, int left, int right) {
        bool Found = false;
        if (Is_Empty(D))
            return true;
        D_max = Find_Max(D);                // 假设到第一个点的距离为剩余最大值
        OK = Check(D_max, N, left, right);  // 检查这个点是否符合
        if (OK) {
            X[right] = D_max;
            // 删除用到的距离
            for (i = 1; i < left; i++)
                Delete(| X[right] - X[i] |, D);
            for (i = right + 1; i <= N; i++)
                Delete(| X[right] - X[i] |, D);
            // 继续构建
            Found = Reconstruct(X, D, N, left, right - 1);
            if (!Found) {  // 情况不满足，回溯
                // 重新插入用到的距离
                for (i = 1; i < left; i++)
                    Insert(| X[right] - X[i] |, D);
                for (i = right + 1; i <= N; i++)
                    Insert(| X[right] - X[i] |, D);
            }
        }
        if (!Found) {  // 假设不成立，换成到最后一个点的距离为剩余最大值
            OK = Check(X[N] - D_max, N, left, right);
            if (OK) {
                X[left] = X[N] – D_max;
                // 删除用到的距离
                for (i = 1; i < left; i++)
                    Delete(| X[left] - X[i] |, D);
                for (i = right + 1; i <= N; i++)
                    Delete(| X[left] - X[i] |, D);
                // 继续构建
                Found = Reconstruct(X, D, N, left + 1, right);
                if (!Found) { // 回溯
                    // 重新插入用到的距离
                    for (i = 1; i < left; i++)
                        Insert(| X[left] - X[i] |, D);
                    for (i = right + 1; i <= N; i++)
                        Insert(| X[left] - X[i] |, D);
                }
            }
        }
        return Found;
    }
    ```

## 井字棋

**策略的表示？**

课件中叉表示电脑，圆表示人，从电脑角度考虑。

$P$ 表示下棋位置，$W$ 表示当前位置下可能赢的种类数，“可能赢”指路径上没有对方的棋。$f(P)$ 表示这个位置对电脑而言的 goodness，$f(P)=W_{computer}-W_{human}$。

电脑下棋，选择 $f(P)$ 最大的位置；人下棋，选择 $f(P)$ 最小的位置。

**alpha-beta 剪枝？**

选择 max 时的剪枝称为 $\alpha$ 剪枝，选择 min 时的剪枝称为 $\beta$ 剪枝。

<span style="color:red">（为什么？）$\alpha-\beta$ 剪枝能将搜索节点的数量从 $O(N)$ 降低到 $O(\sqrt{N})$。</span>

## 主定理

公式：$T(n)=aT(n/b)+f(n)$

**怎么求 T(n)？**

1. Substitude method（代入法）：猜想 $T(n)=g(n)$，即要证 $T(n)<c\cdot g(n)$。假设 $n/b$ 满足，由递推式退出 $n$ 满足。

如果递推式不满足上述公式，可通过换元转化。先将 $f(n)$ 换为幂次，再换成 $n/b$ 的形式。如果含 n 的表达式中同时含有常数项，可直接将常数忽略。

esp. 当证明 $T(n)$ 时发现结果多了低阶项，可尝试在假设中减去这个低阶项（加强假设）来证明。

2. Recursion-tree method（递归树法）：对于上面公式的类型，每个节点变成 $f(n)$，递归树共 $\log_b(N)$ 层。非叶节点总和为等比数列，叶节点总和为 $a^{\log_b(N)}$。

**主定理结论？**

令 $\frac{af(N/b)}{f(N)}\to c$，则

$$
T(n) =
\begin{cases}
\Theta(f(N)), &\quad c<1 \\
\Theta(f(N)\log N), &\quad c=1 \\
\Theta(N^{\log_b a}), &\quad c>1
\end{cases}
$$

上述只对 $f(N)$ 为多项式或多项式乘对数时适用。

进一步可加上对数项 $T(n)=aT(\frac{n}{b})+\Theta\big(n^{c}(\log n)^{k}\big)$，有：

$$
T(n) =
\begin{cases}
\displaystyle \Theta\big(n^{c}(\log n)^{k}\big), &\quad a < b^c \\
\displaystyle \Theta\big(n^{c}(\log n)^{k+1}\big), &\quad a = b^c \\
\displaystyle \Theta\big(n^{\log_b a}\big), &\quad a > b^c
\end{cases}
$$

??? examples "分治时间的计算"

    $$T(n)=2T(n/2)+n/\log n$$

    不能使用主定理，因此用递归树，递归树我们有 $\log_2 n$ 层，第 $i$ 层时间复杂度 $n / \log(n/2^i)$，叶子有 $n$ 个，故整体复杂度为

    $$
    \sum_{i=0}^{\log_2 n - 1} \frac{n}{\log(n/2^i)} + \Theta(n) = \sum_{i=0}^{\log n - 1} \frac{n}{\log_2 n - i} + \Theta(n) = \sum_{j=1}^{\log_2 n} \frac{n}{j} + \Theta(n) = O(n \log \log n)
    $$

## 最近点对问题

**怎么找跨越中间的点对？**

令 $\overline{x}$ 为所有 x 的中值，$\delta$ 为左右的最近点距离，只需考虑 $[\overline{x}-\delta, \overline{x}+\delta]$ 的 strip。将 strip 中点按 y 排序，对于 strip 中点 $q_i$，进一步只需考虑 $[y_i, y_i+\delta]$ 区域中的点。划分成 4x2 的方格，每格中只可能有一个点，因此最多检查 7 个点。

## 背包问题

**0-1 背包？**

$v_i$ 表示物品体积，$w_i$ 表示物品价值。$dp_{i,j}$ 表示前 i 个物品、占用 j 体积时的最大价值。

$$dp_{i,j}=\max(dp_{i-1,j},\,dp_{i-1,j-v_i}+w_i)$$

滚动数组中`y=i&1`，用`y^1`切换。  
也可用一维数组表示，略。

**完全背包？**

$dp_{i,j}$ 表示前 i 个物品、占用 j 体积时的最大价值。

完全背包中同一物品可选择无穷多次，考虑选择第 i 件物品时不用由 i-1 转移。

$$dp_{i,j}=\max(dp_{i-1,j},\,dp_{i,j-v_i}+w_i)$$

**多重背包？**

可展开（或用二进制展开）为 0-1 背包。

## 矩阵乘法的顺序

矩阵 $M_{m\times n}$、$M_{n\times k}$ 相乘的时间为 $mnk$。

**不同乘法顺序的种数？**

令 $b_n$ 表示 n 个矩阵相乘的不同顺序的数量，则 $b_n=\sum_{i=1}^{n-1}b_ib_{n-i}$。

$b_n$ 为卡特兰数，表达式为 $b_n= \frac{1}{n}\binom{2(n-1)}{n-1}$。

**线性规划求解？**

令第 i 个矩阵的大小为 $r_{i-1}\times r_i$。$t_{i,j}$ 表示第 i 个到第 j 个矩阵相乘的最小时间。

$$t_{i,j}=\min\limits_{i\le m\le j}\{t_{i,m}+t_{m+1,j}+r_{i-1}r_mr_j\}$$

时间复杂度为 $O(n^3)$。

## 最优二叉搜索树

给定一列单词 $w_1, w_2,\cdots,w_n$ 和对应的访问频率 $p_1,p_2,\cdots,p_n$。如果单词深度为 $d$，则访问的比较次数为 $d+1$/需要在一棵二叉查找树中放置这些单词，使得总访问次数的期望时间最小，即 $\sum p_i(d_i+1)$ 最小。

符号表示：$T_{ij}$ 表示 $w_i,\cdots,w_j$ 的最优二叉搜索树，$c_{ij}$ 表示 $T_{ij}$ 的搜索次数期望，$r_{ij}$ 表示 $T_{ij}$ 的根，$w_{ij}$ 表示 $T_{ij}$ 中所有节点频率求和。

不考虑和自己的比较，访问次数为左子树的次数加右子树的次数；在考虑和自身的一次比较，需要再加上区间内所有单词的频率。

$$c_{i,j}=\sum_{k=i}^jp_{k}+\max_{i\le k\le j}(c_{i,k-1}+c_{k+1,j})$$

## 全源最短路径

**Floyd-Warshall 算法？**

令 $D^k[i][j]$ 表示从 i 到 j、中间点只允许 $\{0, 1,\cdots,k-1\}$ 的路径的最短长度。$D^{-1}[i][j]$ 表示不允许任何中间点，即原有的边；$D^0[i][j]$ 表示允许点 0 作为中间点……$D^{N-1}[i][j]$ 表示允许所有点作为中间点。

如果路径不经过 k-1，则 $D^k[i][j]=D^{k-1}[i][j]$；如果经过点 k-1，则 $D^{k-1}[i][k]=D^{k-1}[k][j]$。

$$D^k[i][j]=\min(D^{k-1}[i][j],D^{k-1}[i][k] + D^{k-1}[k][j])$$

因为需要逐步加入中间点，循环最外层应为遍历中转点。

!!! examples "完全平方数的和"

    给你一个整数 n，返回和为 n 的完全平方数的最少数量。例如 n = 13，则 n 至少需要写成两个完全平方数相加的形式，即 n = 4 + 9。

    ---
