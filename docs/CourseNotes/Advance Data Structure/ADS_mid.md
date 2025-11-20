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

!!! examples "判断 平衡因子"

    In an AVL tree, it is impossible to have this situation that the balance factors of a node and both of its children are all $-1$.（T/F）

    ---

    T。构造，可行。

!!! examples "判断 AVL 树高度"

    The maximum/minimum height for an AVL tree of 30 nodes is $6/4$. (The height of an empty tree is defined to be $-1$)（T/F）

    ---

    F。分别计算高度为 h 时的最少节点和最多节点数。最大高度为 5 而非 6。

    注意只有根节点时树高为 0。

!!! examples "AVL 树和 Splay 树辨析"

    Among the following 3 statements about AVL trees and splay trees, how many of them are correct?

    (1) In a splay tree, if we only have to find a node without any more operation, it is acceptable that we don't push it to root and hence reduce the operation cost. Otherwise, we must push this node to the root position.

    (2) In a splay tree, for any non-root node $X$, its parent $P$ and grandparent $G$ (guaranteed to exist), the correct operation to splay $X$ to $G$ is to rotate $X$ upward twice.

    (3) Splaying roughly halves the depth of most nodes on the access path.

    ---

    （1）错，只是访问也需要伸展到根。

    （2）错，第一次是 $P$ 转，第二次才是 $X$ 转。

    （3）对。注意是路径上的节点，而不是所有节点。

!!! examples "AVL 树删除再插入"

    Delete a node $v$ from an AVL tree $T_1$, we can obtain another AVL tree $T_2$. Then insert $v$ into $T_2$, we can obtain another AVL tree $T_3$. Which one(s) of the following statements about $T_1$ and $T_3$ is(are) true?

    - Ⅰ、If $v$ is a leaf node in $T_1$, then $T_1$ and $T_3$ might be different.
    - Ⅱ、If $v$ is not a leaf node in $T_1$, then $T_1$ and $T_3$ must be different.
    - Ⅲ、If $v$ is not a leaf node in $T_1$, then $T_1$ and $T_3$ must be the same.

    ---

    I 正确。删除叶节点可能导致旋转，再插入节点时，如果插入路径可能与原路径不同，从而触发不同的旋转。

    II、III 错误。must 都不能确定。

## Splay 树

Splay 树的要求：每次访问后将访问的节点 splay 到根上。

操作：zig，zig-zag，zig-zig

**什么时候进行 splay 操作？**

1. 插入：插入后将插入的节点 splay 到根。
2. 查询：若成功查找到节点 x，则将 x 伸展到根；若查找失败，则将搜索路径的最后一个节点伸展到根。
3. 删除：找到删除的节点 x，将 x 伸展到根 --> 删除根节点后，得到两棵子树 L 和 R --> 若 L 非空，查找 L 中最大节点（这一步将最大节点伸展到根，得到的结果没有右子树） --> 将 R 作为右子树接上。

Splay 树的删除中，将 x 伸展到根并删除根节点后，可选择 L 中最大的节点，也可选择 R 中最小的节点。

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

!!! examples "判断 Splay 树的高度"

    All of the Zig, Zig-zig, and Zig-zag rotations in a splay tree not only move the accessed node to the root, but also roughly half the depth of most nodes in the tree. （T/F）

    ---

    F。伸展操作只保证把被访问的节点移动到根，将根到访问节点的路径上的节点的 Rank 近似减少一半（也可说成路径上的深度大致减半），不保证所有其他节点的深度都减少一半

## 红黑树

红黑树的要求：节点红或黑，根节点黑，NIL 黑，红色节点不相邻，每个节点到任意 NIL 的路径上黑色节点数相同。

**黑高怎么定义？**

对于任意节点 x，其黑高为 x 到任意 NIL 的路径上黑色节点的个数（不包括 x，但包括 NIL）。

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

!!! examples "判断 红色节点数"

    In a red-black tree with 3 nodes, there must be a red node.（T/F）

    ---

    F。虽然空树插入三个节点为黑红红，但可能通过后续操作使其变成黑黑黑。如：插入一个数、再删除插入的数。

!!! examples "红黑树判断"

    If we insert $N$ ($N \geq 2$) nodes (with different integer elements) consecutively to build a red-black tree $T$ from an empty tree, which of the following situations is possible:

    - A. All nodes in $T$ are black
    - B. The number of leaf nodes (NIL) in $T$ is $2N - 1$
    - C. $2N$ rotations occurred during the construction of $T$
    - D. The height of $T$ is $\lceil 3\log_2(N + 1)\rceil$ (assume the height of the empty tree is 0)

    ---

    A 错。从空树连续插入，两个节点以上的红黑树中一定有红色节点。

    B 对。NIL 数等于内部节点数加一，N=2 时满足。

    C 错。红黑树中一次插入最多旋转 2 次，因为每组旋转后局部已满足性质，不会向上传播。

    D 错。由于黑高的限制，红黑树高度最大为 $2\log_2(N + 1)$

!!! examples "红黑树的势能分析"

    There are four basic operations on red-black trees that perform structural modifications: node insertions, node deletions, rotations, and color changes. We shall prove that any sequence of $m$ RB-INSERT and RB-DELETE operations on an initially empty red-black tree causes $O(m)$ structural modifications in the worst case. We count the structural modifications in each step (e.g. Case 1 in RB-DELETION) as one unit operation (cost = 1).

    We define the weight of each node based on its state, and the potential of the Red-Black Tree $T$ is represented by the following function:

    $\Phi(T) = \sum_{x \in T} g(x)$

    where $g(x)$ is calculated for all nodes $x \in T$ of the Red-Black Tree.

    We define the weight of a red node $x$ as $g(x) = 0$.

    For black nodes, which of the following definitions work?

    A.

    - $g(x) = 1$: If the black node has no red children.
    - $g(x) = 0$: If the black node has one red child.
    - $g(x) = 2$: If the black node has two red children.

    B.

    - $g(x) = 1$: If the black node has no red children or one red child.
    - $g(x) = 2$: If the black node has two red children.

    C.

    - $g(x) = 0$: If the black node has no red children.
    - $g(x) = 1$: If the black node has one red child.
    - $g(x) = 2$: If the black node has two red children.

    D.

    - $g(x) = 1$: If the black node has no red children.
    - $g(x) = 2$: If the black node has one red child.
    - $g(x) = 0$: If the black node has two red children.

    ---

    C。

    摊还分析要求代价小的操作势能差大、代价大的操作势能差小。势能对于状态定义，需要反映状态“坏”的程度，当树被修复（旋转、变色）时势能下降。红黑树中的“坏结构”为黑色节点有红孩子，因为红黑树的修复机制都是围绕着“红色太多”展开的，红色节点后插入可能导致红色节点相邻，引发修复。删除黑节点会造成 double-black，但删除触发修复的关键在兄弟节点有没有红孩子、兄弟节点是否是红色、叔侄子是否红色等，仍由红色结构决定。因此，结构越“坏”， $g(x)$ 也要越大。

## B+ 树

B+ 树的要求：对 M 阶 B+ 树，根节点有 2~M 个孩子，非叶节点有 $\lceil\frac{M}{2} \rceil$~M 个孩子，所有叶节点在同一层。

**B+ 树中节点的含义？**

所有非叶节点中的元素仅用于查找。所有实际值都按从小到大的顺序存储在叶节点中。

如果某节点有 n 个孩子，则该节点内部有 M 个指针和 M-1 个数值。指针的前 n 个分别指向 n 个孩子，数值的前 n-1 个中第 i 个元素表示第 i+1 个孩子的最小值（第一个值）。

**B+ 树的查找？**

检查非叶节点中的数值，如果大于等于当前值、小于下一个值，就移动到对应的孩子。

**B+ 树的插入？**

空树中插入一个节点，给节点既是叶节点也是根节点。当插入节点是 $M+1$ 个时，分裂产生表示索引的根节点。

先找到插入的位置，判断是否需要分裂。

叶节点的分裂：如果叶节点中元素为 $M+1$ 个，则在 $\lceil\frac{M}{2} \rceil$ 个元素右边分割，将右叶子第一个元素上移到父节点，并在父节点中增加指向右叶子的指针。

中间节点的分裂：第 $\lceil\frac{M}{2} \rceil$ 个元素上移到父节点作为索引。

根节点的分裂：第 $\lceil\frac{M}{2} \rceil$ 个元素上移作为新的根，其余分裂为两个节点（左子树和右子树）。

（插入时即使不分裂也可能需要更新上层节点？）永远插入到搜索到的叶节点中，如果插入数值小于搜索到叶节点的最小值，则放在最左边。

**B+ 树插入和查询的时间复杂度？**

M 阶 B+ 树共 $O(\log_{\lceil M/2 \rceil}N)$ 层，每次操作最多改变一组叶节点，数量为 $O(M)$，故整体时间复杂度为 $O(\frac{M}{\log M}\log N)$。

查询的时间复杂度等于树高乘每层的操作数，树高为 $O(\log_MN)$，每层需比较 $O(\log M)$ 次，总时间复杂度为 $O(\log_MN\cdot \log M)=O(\log N)$。课件中写的是 $O(\log N)$（$M$ 固定）。

!!! examples "插入的分裂次数"

    To perform Insert on a B+ tree of order $M$, a node with $M+1$ keys will be split into 2 nodes. After inserting $1, 2, 3, \dots, 9, 10$ consecutively into an initially empty B+ tree of order 3, how many split operations have occurred in total?

    ---

    5 次。分裂次数为叶节点分裂和中间节点分裂之和。

!!! examples "B+ 树节点个数"

    A 2-3 tree with 3 nonleaf nodes must have 18 keys at most.（T/F）

    ---

    T。这里的 key 指叶节点中存储的数值。

!!! examples "B+ 树节点个数 2"

    A B+ tree of order 3 with 21 numbers has at least \_\_ nodes of degree 2.

    ---

    0。尝试构造 B+ 树，使得所有中间节点都有 3 个孩子，能构造出。

!!! examples "B+ 树判定"

    The teacher wants to write the `IsBpT` function to check if the trees submitted by students satisfy the definition of the B+ tree of a given order (e.g., order 4) learned in our class. The B+ tree structure is defined as follows:

    ```c
    typedef struct BpTNode BpTNode;
    struct BpTNode {
        bool isLeaf; /* 1 if this node is a leaf, or 0 if not */
        bool isRoot; /* 1 if this node is the root, or 0 if not */
        BpTNode** children; /* Pointers to children. This field is not used by leaf nodes. */
        ElementType* keys;
        int num_children; /* Number of valid children (not NULL) */
        int num_keys; /* Number of valid keys */
    };
    ```

    Fortunately, the students are all brilliant, so the B+ trees they submit guarantee to meet the following properties:

    - There is a root node, and all leaf nodes are at the same depth;
    - The key values stored in all leaf nodes are arranged in strictly ascending order from left to right.

    Your task is to complete the function `IsBpT` as follows so that the teacher can determine whether a tree submitted by a student meets the other properties required by the definition of the B+ tree of a given order. Return true if the tree is a B+ tree, or false if not.

    ```c
    bool IsBpT(BpTNode* node, int order) {
        if (node->isLeaf == 1) {     /* this is a leaf node */
            if (node->isRoot == 1) { /* this tree has only one node */
                if (node->num_keys < 1 || node->num_keys > order)
                    return false;
            } else {
                if (node->num_keys < (order + 1) / 2 || node->num_keys > order)
                    return false;
            }
        } else {
            /* check the property of the tree structure */
            if (node->num_keys != node->num_children - 1)
                return false;
            if (node->isRoot == 1) { /* this is the root node */
                if (node->num_keys < 1 || node->num_keys > order - 1)
                    return false;
                else if (node->num_children < 2 || node->num_children > order)
                    return false;
            } else {
                if ( __________________ || node->num_keys > order - 1)
                    return false;
                else if (node->num_children < (order + 1) / 2 ||
                        node->num_children > order)
                    return false;
            }

            /* check the property of the value of key */
            for (int i = 0; i < node->num_keys; i++) {
                BpTNode* key_node = __________________ ;
                while (key_node->isLeaf == 0) {
                    key_node = key_node->children[0];
                }
                if (node->keys[i] != key_node->keys[0])
                    return false;
            }
            for (int i = 0; i < node->num_children; i++) {
                if (IsBpT(node->children[i], order) == false)
                    return false;
            }
        }
        return true;
    }
    ```

    ---

    第一空：`node->num_children < (order + 1) / 2 - 1`，因为中间节点的元素数

    第二空：`node->children[i + 1]`，因为中间节点的第 i 个元素为第 i+1 个子树中的最小值。

---

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

---

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

从根较小的堆（o）开始，每次有两个待合并的堆，分别为 o 的右儿子和另一个左偏堆。将这两者中根较小的作为 o 的右儿子。从下往上交换左右孩子。也可理解为先左右交换，再在左边合并。

注意！Always swap the left and right children except that the largest of all the nodes on the right paths does not have its children swapped. 除了最右路径上最后一个节点，所有最右路径上节点都要交换左右孩子！即使是空节点和某个节点 x 合并，只要 x 有右孩子，则 x 的左右孩子仍要交换。

**斜堆的摊还分析？**

定义重节点（heavy node）：该节点右子树的节点个数大于等于所有后代（包括自身）的一半。否则为轻节点（light node）。

可证明，若最右路径上有 l 个轻节点，则整个斜堆至少有 $2^l-1$ 个节点。即最右路径上轻节点的个数为 $O(\log N)$。（归纳法证明）

定义势能函数：$\Phi(T)$ 为 T 中重节点的个数。

合并后只有最右路径上轻重会变，且重节点一定变化轻节点、轻节点不一定变为重节点。故一侧操作的均摊成本至多为原先两个堆的最右路径上轻节点的个数，即 $O(\log N)$。

最坏情况下两个堆都退化为链状，合并时间为 $O(N)$。插入、删除的本质都是合并，也都是最坏 $O(N)$、摊还 $O(\log N)$。

!!! examples "斜堆最右路径长度"

    The right path of a skew heap can be arbitrarily long.（T/F）

    ---

    T。斜堆中，最右路径上轻节点的数量有限制，但最右路径总长任意。

## 二项队列

二项树：首先需要满足堆序性（这里默认最小堆）。定义单个节点的高度为 0，k 阶二项树由一个 k-1 阶二项树连接到另一 k-1 阶二项树的根节点构成。（二项树的阶数与二进制对应。）

二项队列：一系列阶数不同的二项树构成的森林。

**查询最小值的时间复杂度？**

最小值一定是某个二项树的根，一共 $O(\log N)$ 个二项树，故 TC 为 $O(\log N)$。

如果额外记录全局最小值，则查询的 TC 为 $O(1)$，但需要另外维护这个值。

**插入的时间复杂度？**

插入相当于二进制下加一。将插入的节点视为 0 阶二项树，和原有的二项队列合并。同阶二叉树合并时，用较小的根作为新的根，从而保证二项树的堆序性。

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

**根据节点数判断二项树个数？**

将节点数转化为二进制，其中 1 的个数即二项树的个数。

!!! examples "二项树连接"

    To implement a binomial queue, the subtrees of a binomial tree are linked in increasing sizes.（T/F）

    ---

    F。由上面连接的代码可知，同阶二项树连接时作为 LeftChild，即子树按大小（节点数）递减的方式串成链。题目描述中“linked in increasing sizes”错误。

!!! examples "二项队列判断"

    Making N insertions into an initally empty binomial queue takes $O(N)$ time in the worst case.

    T。单次插入的最坏时间为 $O(\log N)$，但考虑二项树的创建为 $O(N)$。

    ---

    To implement a binomial queue, left-child-next-sibling structure is used to represent each binomial tree.

    T。

    ---

    For a binomial queue, delete-min takes a constant time on average.

    F。要查找所有二项树，时间为 $O(\log N)$。

    ---

    For a binomial queue, merging takes a constant time on average.

    F。可能产生 $O(\log N)$ 次进位，时间为 $O(\log N)$。

    ---

    Inserting a number into a binomial heap with 15 nodes costs less time than inserting a number into a binomial heap with 19 nodes.

    F。插入第 16 个节点后进位多。

!!! examples "二项队列操作时间"

    For a binomial queue, \_\_ takes a constant time on average.

    A. merging
    B. find-max
    C. delete-min
    D. insertion

    ---

    D。其他三项均为 $O(\log N)$。

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

!!! examples "暴力搜索"

    It is guaranteed that an exhaustive search can always find the solution in finite time.（T/F）

    ---

    F。解空间可能是无限的。

!!! examples "回溯顺序"

    In backtracking, if different solution spaces have different sizes, start testing from the partial solution with the largest space size would have a better chance to reduce the time cost. （T/F）

    ---

    F。这里的 size of solution spaces 指的是在某种情况下可能的选择的个数，可选择数少，剪枝剪掉的多。

!!! examples "回溯的时间复杂度"

    What makes the time complexity analysis of a backtracking algorithm very difficult is that the time taken to backtrack -- that is, to recover the previous state of a solution -- is hard to estimate.（T/F）

    ---

    F。不是因为“回溯”这个过程的时间难以分析，而是不同分支的搜索空间大小差别大、不确定什么时候回溯。

!!! examples "回溯的时间和解空间"

    The time complexity of a backtracking algorithm is $\Omega(S)$ where $S$ is the total size of the solution space.（T/F）

    ---

    F。Solution space 指所有可能的解，但回溯中通过剪枝，不用访问所有的解空间。

## 八皇后问题

**解的表示？**

$Q_i$ 表示第 i 行的皇后，$x_i$ 表示 $Q_i$ 所在的列。Solution 表示为 $(x_1, x_2,\cdots,x_8)$。

Solution space 指 solution 的所有可能情况的数量（不一定满足所有条件）。

课件中画出博弈树便于理解。实际不用构造树。

**解的个数？**

N 皇后问题解的个数是指数级，但找到一个解只需多项式时间。

!!! examples "回溯边数"

    The problem of “N queens” is to place N queens on an N\*N chessboard such that no two queens attack. If the problem is to be solved by backtracking method, we need to check \_\_ edges of the game tree with N=3 to see that there is no solution.

    ---

    11。边指放棋子的操作，同一列上放棋子直接跳过、不需要尝试。

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

## 分治法

!!! examples "排序与分治"

    How many of the following sorting methods use(s) Divide and Conquer algorithm?

    - Heap Sort
    - Insertion Sort
    - Merge Sort
    - Quick Sort
    - Selection Sort
    - Shell Sort

    ---

    2 个。Merge sort 是经典分治算法。Quick sort 用 pivot 将数组分成两部分，再分别处理两边，也是分治。

    堆排序、插入排序、选择排序、希尔排序不是分治。

!!! examples "时间分析"

    Recall that in the merge sort, we divide the input list into two groups of equal size, sort them recursively, and merge them into one sorted list. Now consider a variant of the merge sort. In this variant, we divide the input list into $\sqrt{n}$ groups of equal size, where n is the input size. What is the worst case running time of this variant? (You may use the fact that merging k sorted lists takes $O(m\log k)$ where m is the total number of elements in these lists.)

    ---

    $O(N\log N)$。递推式为 $T(N)=\sqrt{N}T(\sqrt{N})+O(N\log N)$，猜想时间复杂度为 $O(N\log N)$（根据选项猜测），代入发现符合。

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

!!! examples "f(N)的表示"

    $f(N)$ 由以下构成：

    ```c
    for(int k=1;k<=r-l+1;k++)
        for(int i=1;i<=r-l+1;i++)
            for(int j=l;j<=r;j+=i)
                calc(j, i);
    ```

    ---

    $\sum_{i=1}^N\frac{N}{i}=N\log N$，故 $f(N)=O(N^2\log N)$。

!!! examples "分治时间的计算"

    $$T(n)=2T(n/2)+n/\log n$$

    不能使用主定理，因此用递归树，递归树我们有 $\log_2 n$ 层，第 $i$ 层时间复杂度 $n / \log(n/2^i)$，叶子有 $n$ 个，故整体复杂度为

    $$
    \sum_{i=0}^{\log_2 n - 1} \frac{n}{\log(n/2^i)} + \Theta(n) = \sum_{i=0}^{\log n - 1} \frac{n}{\log_2 n - i} + \Theta(n) = \sum_{j=1}^{\log_2 n} \frac{n}{j} + \Theta(n) = O(n \log \log n)
    $$

!!! examples "主定理计算"

    For the recurrence equation $T(N)=8T(N/2)+N^3\log N$, we obtain $T(N)=O(N^3\log N)$ according to the Master Theorem.

    F。$T(N)=O(N^3\log^2 N)$。

    ---

    For the recurrence equation $T(N)=aT(N/b)+f(N)$, if $af(N/b)=f(N)$, then $T(N)=\Theta(N\log_b N)$.

    F。$T(N)=\Theta(f(N)\log_b N)$。

    ---

    For the recurrence equation $T(N)=aT(N/b)+f(N)$, if $af(N/b)=Kf(N)$ for some constant $K>1$, then $T(N)=\Theta(f(N))$.

    F。$\Theta(N^{\log_b a})$。

    ---

    For the recurrence equation $T(N)=aT(N/b)+f(N)$, if $af(N/b)=f(N)$, then $T(N)=\Theta(f(N)\log_b N)$.

    T。

!!! examples "时间计算"

    3-way-mergesort : Suppose instead of dividing in two halves at each step of the mergesort, we divide into three one thirds, sort each part, and finally combine all of them using a three-way-merge. What is the overall time complexity of this algorithm ?

    ---

    $O(N\log N)$。combine all of them using a three-way-merge 指每次取三组中最小值、合并成一组的方法。$T(N)=3T(N/3)+O(N)$，故 $T(N)=O(N\log N)$。

---

## 最近点对问题

**怎么找跨越中间的点对？**

令 $\overline{x}$ 为所有 x 的中值，$\delta$ 为左右的最近点距离，只需考虑 $[\overline{x}-\delta, \overline{x}+\delta]$ 的 strip。将 strip 中点按 y 排序，对于 strip 中点 $q_i$，进一步只需考虑 $[y_i, y_i+\delta]$ 区域中的点。划分成 4x2 的方格，每格中只可能有一个点，因此最多检查 7 个点。

!!! examples "最近点对时间"

    If devide-and-conquer strategy is used to find the closest pair of points in a plane, unless the points are sorted not only by their x coordinates but also by their y coordinates, it would be impossible to solve it in a time of $O(N\log N)$, where $N$ is the number of points.（T/F）

    ---

    T。如果没有对 Y 排序，strip 内部的排序需要时间 $O(N\log N)$，总时间复杂度大于 $O(N\log N)$。

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

给定一列单词 $w_1, w_2,\cdots,w_n$ 和对应的访问频率 $p_1,p_2,\cdots,p_n$。如果单词深度为 $d$，则访问的比较次数为 $d+1$，需要在一棵二叉查找树中放置这些单词，使得总访问次数的期望时间最小，即 $\sum p_i(d_i+1)$ 最小。

符号表示：$T_{ij}$ 表示 $w_i,\cdots,w_j$ 的最优二叉搜索树，$c_{ij}$ 表示 $T_{ij}$ 的搜索次数期望，$r_{ij}$ 表示 $T_{ij}$ 的根，$w_{ij}$ 表示 $T_{ij}$ 中所有节点频率求和。

不考虑和自己的比较，访问次数为左子树的次数加右子树的次数；在考虑和自身的一次比较，需要再加上区间内所有单词的频率。

$$c_{i,j}=\sum_{k=i}^jp_{k}+\max_{i\le k\le j}(c_{i,k-1}+c_{k+1,j})$$

## 全源最短路径

**Bellman-Ford 算法？**

Bellman–Ford 是一种单源最短路径算法，边权可以为负。

对每个点定义 $dist$ 为到源点的最小距离，初始化为正无穷。对每条边松弛 $dist[v]=\min(dist[v], dist[u]+l_{uv})$，最多松弛 $N-1$ 次。再检查所有边，如果仍存在 $dist[v] > dist[u] + l_{uv}$，说明存在负环。

令 $D^k[v]$ 表示从源点 s 到当前点 v，最多使用 k 条边的最短路径长度，则 $D^{n-1}[v]$ 表示所求的最短路。如果仍只使用 k-1 条边，则 $D^k[v]=D^{k-1}[v]$；如果使用 k 条边，且令 $(w,v)$ 是最后的边，则 $D^k[v]=\min_{(w,v)\in E}(D^{k-1}[w]+l_{wv})$。

不包含负环等价于对任意顶点 $v$，有 $D^n[v]=D^{n+1}[v]$。

**Floyd-Warshall 算法？**

令 $D^k[i][j]$ 表示从 i 到 j、中间点只允许 $\{0, 1,\cdots,k\}$ 的路径的最短长度。$D^{-1}[i][j]$ 表示不允许任何中间点，即原有的边；$D^0[i][j]$ 表示允许点 0 作为中间点……$D^{N-1}[i][j]$ 表示允许所有点作为中间点。

如果路径不经过 k-1，则 $D^k[i][j]=D^{k-1}[i][j]$；如果经过点 k-1，则 $D^{k-1}[i][k]=D^{k-1}[k][j]$。

$$D^k[i][j]=\min(D^{k-1}[i][j],D^{k-1}[i][k] + D^{k-1}[k][j])$$

因为需要逐步加入中间点，循环最外层应为遍历中转点。

包含负环等价于存在一个顶点 $v$，使得 $D^n[v][v]<0$。Floyd-Warshall 算法允许负边，但不能出现负环。

## 产品装配问题

汽车可以在两条装配线中组装，不同装配线在同一个工站的加工时间不同。在进入下一个工站时，可以留在当前线、也可以从另一条线切换过来。求最短时间。

共有 $N$ 个工站，0、1 两条装配线。令 $t_{0,j}$、$t_{1,j}$ 分别表示 0、1 线从工站 $j-1$ 到 $j$ 的时间，$t_{0\to 1,j}$、$t_{1\to 0,j}$ 分别表示切换所需的时间。

暴力搜索需要 $O(2^N)$ 的时间、$O(N)$ 的空间。

令 $f[0][i]$、$f[1][i]$ 分别表示进行到 0、1 条线的第 i 个工站的最短时间。状态转移：$f[0][i]=\min{f[0][i-1]+t_{0,i},f[1][i-1]+t_{1\to 0,j}}$（前者记为 $f_{stay}$，后者记为 $f_{move}$。）

## 动态规划

**子序列和子数组？**

子序列（subsequence）可以有间隔，而子数组/子串/子区间（subarray/substring/interval）要求连续。

**什么时候不能用动态规划？**

1. 出现 history-dependency，当前决策不仅取决于当前状态，还取决于“过去发生过什么”，而过去的信息不能被压缩成有限维的状态。
2. 子问题没有 overlapping
3. 子问题数量太大，问题是在线的……

!!! examples "完全平方数的和"

    给你一个整数 n，返回和为 n 的完全平方数的最少数量。例如 n = 13，则 n 至少需要写成两个完全平方数相加的形式，即 n = 4 + 9。

    ---

    令 $dp[i]$ 表示和为 i 时，所需完全平方数的最少个数。状态转移：$dp[i]=\min_{1\le j^2\le i}(dp[i-j^2]+1)$。

    ```cpp
    int numSquares(int n) {
        const int INF = 1e9;
        vector<int> dp(n + 1, INF);
        dp[0] = 0;

        vector<int> squares;
        for (int i = 1; i * i <= n; ++i) {
            squares.push_back(i * i);
        }

        for (int i = 1; i <= n; ++i) {
            for (int sq : squares) {
                if (sq > i) break;
                dp[i] = min(dp[i], dp[i - sq] + 1);
            }
        }
        return dp[n];
    }
    ```

!!! examples "切割最大利益问题"

    Rod-cutting Problem: Given a rod of total length $N$ inches and a table of selling prices $P_L$ for lengths $L = 1, 2, \cdots, M$. You are asked to find the maximum revenue $R_N$ obtainable by cutting up the rod and selling the pieces. For example, based on the following table of prices, if we are to sell an 8-inch rod, the opti   mal solution is to cut it into two pieces of lengths 2 and 6, which produces revenue $R_8 = P_2 + P_6 = 5 + 17 = 22$. And if we are to sell a 3-inch rod, the best way is not to cut it at all.

    | Length $L$  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
    | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | Price $P_L$ | 1   | 5   | 8   | 9   | 10  | 17  | 17  | 20  | 23  | 28  |

    ---

    先剪一段得到收益 $P_i$，再将剩下的视为子问题。$R_N=\max\limits_{1\le i\le N}(P_i+R_{N-i})$。

!!! examples "字符串匹配"

    Given two words `word1` and `word2`, the minimum number of operations required to transform `word1` into `word2` is defined as the edit distance between the two words.
    The operations include:

    - Inserting a character
    - Deleting a character
    - Replacing a character

    Example:

    Input: `word1 = "horse"`, `word2 = "ros"`
    Edit Distance: 3

    Explanation:

    1. horse → rorse (replace 'h' with 'r')
    2. rorse → rose (remove 'r')
    3. rose → ros (remove 'e')

    We can use dynamic programming to solve it.

    Definition:

    - `dp[i][j]` represents the minimum edit distance between the substring of word1 ending at index i-1, and the substring of word2 ending at index j-1.
    - `word[i]` represents the i-th character of the word

    ---

    初始化：$dp[0][i]=dp[i][0]=0$

    若最后一个字母相同，则 $dp[i][j]=dp[i-1][j-1]$。
    若最后一个字母不同，可以选择删除 word1 最后一个字符、在 word1 末尾插入字符、将 word1 最后的字符替换为 word2 最后的字符。删除的代价为 $dp[i-1][j]+1$，插入的代价为 $dp[i][j-1]+1$，替换的代价为 $dp[i-1][j-1]+1$，最终代价为三者取 min。

!!! examples "判断 时间复杂度"

    If a problem can be solved by dynamic programming, it must be solved in polynomial time. T/F.

    ---

    F. 因为 TSP 的时间复杂度为 $O(n^2 2^n)$。

!!! examples "动态规划的循环顺序"

    In dynamic programming, we derive a recurrence relation for the solution to one subproblem in terms of solutions to other subproblems. To turn this relation into a bottom up dynamic programming algorithm, we need an order to fill in the solution cells in a table, such that all needed subproblems are solved before solving a subproblem. Among the following relations, which one is impossible to be computed?

    - A. $A(i,j) = \min(A(i-1,j), A(i,j-1), A(i-1,j-1))$
    - B. $A(i,j) = F(A(\min\{i,j\}-1,\min\{i,j\}-1), A(\max\{i,j\}-1,\max\{i,j\}-1))$
    - C. $A(i,j) = F(A(i,j-1), A(i-1,j-1), A(i-1,j+1))$
    - D. $A(i,j) = F(A(i-2,j-2), A(i+2,j+2))$

    ---

    A 可以。

    B 可以。$A(i,j)$ 的值都依赖于 $A(i-1,i-1)$ 和 $A(j-1,j-1)$，而这两个值严格更小。可按照对角线顺序填表。

    C 可以。$A(i,j-1)$ 为左、$A(i-1,j-1)$ 为左上、$A(i-1,j+1)$ 为右上，可以按行（i）逐个填表。

    D 不可以。循环依赖。

!!! examples "动态规划顺序 2"

    Given a recurrence equation $f_{i,j,k} = f_{i,j+1,k} + \min\limits_{0 \le l \le k}\{f_{i-1,j,l} + w_{j,l}\}$. To solve this equation in an iterative way, we cannot fill up a table as follows:

    - A. `for k in 0 to n: for i in 0 to n: for j in n to 0`
    - B. `for i in 0 to n: for j in 0 to n: for k in 0 to n`
    - C. `for i in 0 to n: for j in n to 0: for k in n to 0`
    - D. `for i in 0 to n: for j in n to 0: for k in 0 to n`

    ---

    B。$f_{i,j+1,k}$ 需要同一层 i、同一 k、j+1 列的值，说明 j 从 n 到 0 遍历。$f_{i-1,j,l}$ 需要上一层 i、同一 j、所有 l 的值，说明 i 从 0 到 n 遍历，而 k 的遍历顺序无关，因为 i-1 层全部 k 都计算完。

    循环的方向取决于其他量固定时，这个量依赖于更小的值还是更大的值。但如果状态转移的依赖的所有值都是某变量的上一个值，这个变量必须优先循环。

    因此要求为：`i++`, `j--`。B 中 j 递增，不符。

!!! examples "动态规划顺序 3"

    To solve the optimal binary search tree problem, we have the recursive equation $c_{ij} = \min_{i \le l \le j}\{w_{ij} + c_{i,l-1} + c_{l+1,j}\}$. To solve this equation in an iterative way, we must fill up a table as follows:

    A. `for i = 1 to n-1 do; for j = i to n do; for l = i to j do`
    B. `for k = 1 to n-1 do; for i = 1 to n-k do; set j = i+k; for l = i to j do`
    C. `for j = 1 to n-1 do; for i = 1 to j do; for l = i to j do`
    D. `for k = 1 to n-1 do; for i = 1 to n do; set j = i+k; for l = i to j do`

    ---

    B。状态转移依赖的 $c_{i,l-1}$ 和 $c_{l+1,j}$ 都长度小于 $c_{i,j}$，因此最外层按区间长度遍历。

    其他选项可通过列举前几项排除。

## 贪心算法

只有当局部最优解（local optimum）和全局最优解（global optimum）相同时，贪心算法才有效。

贪心算法不能保证找到最优解，但通常会产生数值非常接近的解（启发式算法）。

## 活动选择问题

给定一个活动集合 $S = \{a_1, a_2, \ldots, a_n\}$，其中活动 $a_i$ 占用时间 $[s_i,f_i)$ ，且 $0 \leq s_i < f_i < \infty$。如果活动 $a_i$ 和 $a_j$ 满足 $f_i \leq s_j$ 或者 $f_j \leq s_i$，则称活动 $a_i$ 和 $a_j$ 是兼容的（compatible）。要求找到一个最大的彼此兼容的子集。

**线性规划求解？**

方法一：

令 $S_{ij}$ 表示活动 $a_i$ 与 $a_j$ 之间（不包括 $a_i$、$a_j$）的最大彼此兼容的集合，记大小为 $c_{ij}$。则 $c_{ij}=\max(c_{ik}+c_{kj}+1\mid f_i\le s_k<f_k\le s_j)$，即遍历所有 $a_i$、$a_j$ 之间的活动 $a_k$。

方法二：

令 $S_{ij}$ 表示第 i 到第 j 个活动的最大兼容活动集合，记大小为 $c_{i,j}$。令 $k(i)$ 表示前 i 个活动中，结束时间在 $s_i$ 之前、且 $c_k$ 最大的 k 值，则 $c_i=\max(c_{i-1},c_{k(i)}+1)$。如果活动有权值 $w_i$，将这里的 1 替换为 $w_j$。

**贪心算法求解？**

按各个活动的结束时间排序，每次取不冲突且结束时间最早的活动。（也可以从后往前选择最晚开始的活动。）

证明：交换参数法。假设不取结束时间最早的，证明替换后更优或等价。  
需要用到以下步骤：1. 考虑任意非空子问题 $S_k$，令 $a_m$ 是 $S_k$ 中结束时间最早的活动，则 $a_m$ 在 $S_k$ 的某个最大兼容的活动子集中。2. 用贪心策略选择 $a_1$ 之后得到子问题 $S_1$，那么 $a_1$ 和子问题 $S_1$ 的最优解合并，一定可以得到原问题的一个最优解。

动态规划求解的时间复杂度为 $O(N\log N)$，而贪心算法的时间为 $O(N)$。

!!! examples "活动选择判断"

    Let S be the set of activities in Activity Selection Problem. Then the earliest finish activity $a_m$ must be included in all the maximum-size subset of mutually compatible activities of S.

    F。可能有多个子集大小都为 maximum-size，而 $a_m$ 不一定在每个这样的子集中都出现。

    ---

    Let S be the set of activities in Activity Selection Problem. Then there must be some maximum-size subset of mutually compatible activities of S that includes the earliest finish activity.

    T。即贪心算法能找到最优解，但不一定是唯一的最优解。

!!! examples "动态规划判断"

    Let $c_{1,j}$ be the optimal solution for $a_1$ to $a_j$, and $a_{k(j)}$ is the nearest compatible activity to $a_j$ that is finished before $a_j$. If each activity has a weight $w$, then

    $$
    c_{1,j} =
    \begin{cases}
    1 & \text{if } j=1 \\
    \max\{ c_{1,j-1}, c_{1,k(j)} + w_j \} & \text{if } j>1
    \end{cases}
    $$

    （T/F）

    ---

    F。考虑第 j 个活动选或者不选，状态转移为 $c_{i,j}=\max\{ c_{1,j-1}, c_{1,k(j)} + w_j \}$。但由于活动有权值，当 j=1 时应初始化为 $w_1$ 而不是 1。

!!! examples "空间调度问题比较"

    Let us consider the following problem: given the set of activities $S$, we must schedule them all using the minimum number of rooms.

    Greedy1: Use the optimal algorithm for the Activity Selection Problem to find the max number of activities that can be scheduled in one room. Delete and repeat on the rest, until no activities left.

    Greedy2:

    - Sort activities by start time. Open room 1 for $a_1$.
    - for i=2 to n if $a_i$ can fit in any open room, schedule it in that room; otherwise open a new room for $a_i$.

    Which of the following statements is correct?

    A. None of the above two greedy algorithms are optimal.
    B. Greedy1 is an optimal algorithm and Greedy2 is not.
    C. Greedy2 is an optimal algorithm and Greedy1 is not.
    D. Both of the above two greedy algorithms are optimal.

    ---

    C。Greedy2 是正确的贪心做法，假设某个活动要新开房间，则前面所有房间在某个时间都重叠，不可能用更少的房间。而 Greedy1 可能选择结束时间早但重叠多的活动，导致房间数更多（可举反例）。

## 哈夫曼编码

给定字母表 $C$，$C_i$ 表示第 i 个字符，$f_i$ 表示 $C_i$ 的频率。为每个字符分配一个前缀码，用字典树表示每个字符的编码，令 $d_i$ 表示 $C_i$ 在字典树中的深度，即编码的长度。加权编码总长度 $cost=\sum f_id_i$，要求这个值最小。

**无歧义解码的要求？**

前缀码的要求：不存在一个编码是另一个编码的前缀。

编码对应的哈夫曼树需要为前缀树，每个字符对应树中的一个叶节点。为了使总编码长度最小，每个内部节点必须有两个孩子（是满二叉树）。

**哈夫曼编码的方法？**

每次取频率最低的两个节点合成一个节点。重复 $C-1$ 次，构造哈夫曼树。

```c
void Huffman(PriorityQueue heap[], int C) {
    Consider the C characters as C single node binary trees, and initialize them into a min heap;
    for ( i = 1; i < C; i++ ) {
        Create a new node;
        Delete root from min heap and attach it to left_child of node;
        Delete root from min heap and attach it to right_child of node;
        weight of node = sum of weights of its children;
        // 树的 cost 等于所有叶节点的代价之和
        Insert node into min heap;
    }
}
```

**贪心策略的证明？**

引理 1：$C$ 为一个字母表，其中每个字符 $c \in C$ 频率为 $c.freq$。令 $x$ 和 $y$ 是 $C$ 中频率最低的两个字符。那么存在 $C$ 的一个最优前缀码，$x$ 和 $y$ 的码字长度相同，且只有最后一个二进制位不同，即在哈夫曼树中为兄弟叶节点。

引理 1 证明：由于最优前缀码树是满二叉树，必然存在一对兄弟叶子，它们所在的深度是树中最大。分别将 $x$ 和 $y$ 换到这两个位置，交换之后总代价只会变小、不会变大。

引理 2：令 $x$ 和 $y$ 是 $C$ 中频率最低的两个字符。令 $C'$ 为 $C$ 去掉字符 $x$ 和 $y$、加入新字符 $z$ 且 $z.freq = x.freq + y.freq$ 后的新字母表，令 $T'$ 为 $C'$ 的任意一个最优前缀码树。将 $T'$ 中的叶节点 $z$ 替换为一个以 $x$ 和 $y$ 为孩子的内部节点，则得到一个 $C$ 的一个最优前缀码树 $T$。

!!! examples "前缀树判断"

    A binary tree that is not full cannot correspond to an optimal prefix code.（T/F）

    ---

    T。这里的 full binary tree（满二叉树）指所有非叶节点都有两个孩子。最优前缀树必须为满二叉树。

!!! examples "哈夫曼编码长度分析"

    Given 4 cases of frequences of four characters. In which case(s) that the total bits taken by Huffman codes are the same as that of the ordinary equal length codes?

    (1) 4 2 11 6
    (2) 6 5 7 12
    (3) 3 2 3 4
    (4) 8 3 10 7

    ---

    （3）和（4）。哈夫曼编码长度为每个字符的编码长度乘出现次数求和，ordinary equal length codes 长度指编码长度乘所有字符的出现次数。

!!! examples "最优前缀码判断"

    Given four characters (a, b, c, d) with distinct frequencies in a text. Suppose that a and b are the two characters having the lowest frequencies. Which of the following sets of code is a possible Huffman code for this text?

    A. a: 000, b: 001, c: 01, d: 1
    B. a: 000, b: 001, c: 01, d: 11
    C. a: 000, b: 001, c: 10, d: 1
    D. a: 010, b: 001, c: 01, d: 1

    ---

    A。B 中前缀树不是满二叉树，d 可以上移一层。C 中 d 是 c 的前缀。D 中 a 和 b 不是兄弟节点。
