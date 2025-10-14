# ADS Lec 04 左偏堆和斜堆

## 左偏堆

### 概念

**dist（或 Npl）**：对于任意一个节点，它的 dist 为这个节点到没有两个孩子的节点的最短距离。  
对叶节点、只有一个孩子的节点，dist 都为 0。

**左偏堆：**

- 是二叉堆
- 对任意节点，其左孩子的 dist 一定大于等于右孩子的 dist

左偏堆的性质：

- 任意节点的 dist = 其右孩子的 dist + 1（如果没有右孩子，则为 0）。
- 若根节点的 dist 为 N，则前 N+1 层为满二叉树，整个左偏堆至少有$2^{N+1}-1$个节点。
- 若整个左偏堆共 N 个节点，则右侧路径最多有$\lfloor \log(N+1) \rfloor$个节点。

左偏堆最右侧的路径尽可能短，合并时只沿右侧路径合并，时间复杂度低。

### 操作

节点的定义为：

```cpp
struct node {
    int val, d;   // 存储的值，dist
    node *l, *r;  // 左右儿子
};
```

#### 递归合并

1. 将已经合并的顶点（记为 o）从根较小的堆开始，沿最右侧不断下移。
2. 每次有两个待合并的堆，分别为 o 的右儿子和另一个左偏堆。将这两者中根较小的作为 o 的右儿子。
3. 检查“放在 o 的右儿子”这一步是否违反左偏性质，调整并更新 o 的 dist。
4. 将 o 下移，递归进行。

代码：

```cpp
node* merge1(node* a, node* b) {
    if (!a)
        return b;
    if (!b)
        return a;

    if (a->val > b->val)     // o从根较小的堆开始
        swap(a, b);
    a->r = merge1(a->r, b);  // 递归合并o的右儿子和另一个堆

    if (!a->l || a->l->d < a->r->d)  // 维护左偏性质
        swap(a->l, a->r);
    a->d = a->r ? a->r->d + 1 : 0;   // 更新o的dist
    return a;
}
```

#### 迭代合并

迭代合并中，用栈存储合并路径上的所有父节点。合并完后，回溯存储的父节点，依次调整左右儿子，使其保持左偏。

- 递归合并是自底向上进行，先产生最底部的合并结果，每次产生后维护左偏
- 迭代合并是自顶向下进行，先合并完所有节点，再从下开始依次调整、维护左偏

1. 将已经合并的顶点（记为 o）从根较小的堆开始，沿最右侧不断下移。
2. 若另一个堆小于 o 的右儿子，则交换到 o 右儿子的位置。
3. 在栈中存储合并的父节点 o。
4. 将 o 下移，递归进行。
5. 依次弹栈，维护左偏性质。

代码：

```cpp
node* merge2(node* a, node* b) {
    if (!a)
        return b;
    if (!b)
        return a;
    if (a->val > b->val)
        swap(a, b);

    node* root = a;    // 合并后根节点
    stack<node*> stk;  // 栈用于存储合并路径的父节点

    while (a->r && b) {   // 合并
        if (a->r->val > b->val)
            swap(a->r, b);
        stk.push(a);
        a = a->r;
    }
    a->r = b;

    while (stk.size()) {  // 调整合并路径上的点，维护左偏性质
        a = stk.top();
        stk.pop();
        if (!a->l || a->l->d < a->r->d)
            swap(a->l, a->r);
        a->d = a->r ? a->r->d + 1 : 0;
    }
    return root;
}
```

#### 插入

单点插入可看作原先的左偏堆和只有一个节点的新堆的合并。

代码：

```cpp
node* newNode(int x) {
    node* t = new node;
    t->val = x;
    t->d = 0;
    t->l = t->r = nullptr;
    return t;
}

node* insert(node* a, int x) {
    node* t = newNode(x);
    a = merge1(a, t);
    return a;
}
```

#### 删除

删除一个节点时，需要考虑它的父节点和子节点。  
先将子节点对应的子树合并，再用合并后的树代替要删除的节点。

代码：

```cpp
node* delNode(node* a, int x) {
    if (!a)
        return nullptr;
    if (a->val == x) {
        node* merged = merge1(a->l, a->r);
        delete a;
        return merged;
    }

    a->l = delNode(a->l, x);
    a->r = delNode(a->r, x);
    if (!a->l || a->l->d < a->r->d)
        swap(a->l, a->r);
    a->d = a->r ? a->r->d + 1 : 0;
    return a;
}
```

## 斜堆

### 概念

左偏堆和斜堆的关系类似于 AVL 树和 Splay 树。

斜堆满足任何节点小于（或大于）其左右儿子，但不需要像左偏堆一样维护 dist。

斜堆更看重合并的效率，而不是堆的平衡，它的目的是使 M 次操作的最大时间复杂度为$O(M\log N)$。

### 操作

**节点定义：**

```cpp
struct node {
    int val;     // 不含dist
    node *l, *r;
};

```

**递归合并：**

顶小的堆原先的右子树、另一个堆作为待合并的两个堆，合并后作为顶小的堆的右子树。再将顶小的堆的左右子树交换。  
如果一个堆和空节点合并，则这个堆的左右子树不交换。

??? examples "递归合并代码"

    ```cpp
    node* merge1(node* a,node* b) {
        if (!a)
            return b;
        if (!b)
            return a;

        if (a->val>b->val)
            swap(a, b);
        a->r = merge1(a->r, b);
        swap(a->l, a->r);
        return a;
    }
    ```

**迭代合并：**

用栈记录每次操作的父节点。所有合并完成后，从下到上依次交换栈中节点的左右节点。

??? examples "迭代合并代码"

    ```cpp
    node* merge2(node* a, node* b) {
        if (!a)
            return b;
        if (!b)
            return a;
        if (a->val > b->val)
            swap(a, b);

        node* rt = a;
        stack<node*> stk;

        while (a->r && b) {
            if (a->r->val > b->val)
                swap(a->r, b);
            stk.push(a);
            a = a->r;
        }
        a->r = b;

        while (stk.size()) {
            a = stk.top();
            stk.pop();
            swap(a->l, a->r);
        }
        return rt;
    }
    ```

**插入：**

看作和只有一个节点的堆的合并。

**删除：**

合并左右儿子，用合并后的堆代替要删除的节点。

### 摊还分析

**回顾势能分析：**

对于状态$D_i$，需要构造势能函数$\Phi(D_i)$，满足$\Phi(D_k)\ge \Phi(D_0)$。  
每一步的摊还成本$\hat{c_i}$ $=$ 实际成本$c_i + \Phi(D_i)-\Phi(D_{i-1})$。  
总的摊还成本$\displaystyle\sum_{i=1}^n\hat{c_i}$ $=$ 总的实际成本$\displaystyle\sum_{i=1}^n c_i+ \Phi(D_n)-\Phi(D_0)\ge \displaystyle\sum_{i=1}^n c_i$

整个操作中单调递增的函数不适合作为势能函数。因为势能函数反映实际成本和均摊成本之间的差距，一定有正有负。

**斜堆合并的分析：**

每次斜堆合并的操作步数，即实际成本，取决于最右侧路径节点数之和。但斜堆不保证左偏，右路径长度可能为$O(N)$。

定义**重节点**：对于一个节点，在以这个节点为根（包含该节点）的子树中，如果右子树的节点数大于等于总节点数的一半，则该节点为重节点；反之为轻节点。

定义**势能函数**：势能为整棵树中重节点的个数。

斜堆合并时，只有最右路径上节点的轻重情况会改变。其他节点的轻重情况一定不变（因为直接从左子树移动到右子树，局部结构不变）。所以考虑势能变化，只要考虑最右路径的轻重节点数。

最右路径上，重节点一定变为轻节点，而轻节点不一定变为重节点（本身交换后就不一定，左儿子还可能加其他节点）。

对于右路径上的轻节点，左子树的节点较多，类似左偏堆，轻节点最多有$\log(N)$个。

记$l_1$、$h_1$，$l_2$、$h_2$为第一、二个堆最右路径上轻、重节点数，$h$表示其他位置的重节点数。  
一次操作前：$\Phi_{i-1}=h_1+h_2+h$  
一次操作后：$\Phi_{i}\le l_1+l_2+h$

一次操作的均摊成本：

$$
\begin{align*}
\hat{c_i}&=c_i+\Phi_i-\Phi_{i-1} \\
&=c_i+l_1+l_2-(h_1+h_2) \\
&\le 2(l_1+l_2) \\
&=O(\log N)
\end{align*}
$$

由此得到，斜堆合并的均摊成本为$O(\log N)$。
