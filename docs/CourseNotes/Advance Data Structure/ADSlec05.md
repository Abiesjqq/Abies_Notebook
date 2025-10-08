## 概念

**二项队列**是一系列满足堆性质的树组成的森林。其中的每个树是二项树，每种阶数的二项树最多只有一棵。

**二项树**：定义单个节点的高度为 0。k 阶二项树由一个 k-1 阶二项树连接到另一 k-1 阶二项树的根节点构成。即，阶数为 k 的二项树由两棵阶数为 k−1 的二项树合并而成。

二项树的性质：

- 高度为 k 的二项树一定有$2^k$个节点。
- 第 i 个二项树是 i-1 叉树。
- 二项树的子树也是二项树。
- k 阶二项树，深度为 d 的层共$\binom{k}{d}$个节点。

要表示 n 个数（n 个节点），将 n 转化为二进制，若第 i 位为 1 则需要二项树$B_i$。

## 操作

由于二项树不是二叉树，不能用左右儿子表示，改为 LeftChild-NextSibling 表示。

整个二项队列用二项树根节点的 vector 表示。

**定义：**

```cpp
struct Node {
    int val;
    Node* leftChild = nullptr;
    Node* nextSibling = nullptr;
    Node(int v) : val(v) {}
};

using BinTree = Node*;

struct BinomialQueue {
    vector<BinTree> trees;
    int size = 0;

    // 一些成员函数定义在这里
};
```

### 合并

合并两个二项队列时，如果都有 k 阶二项树，则将其合并为一棵 k+1 阶二项树。

由于二项队列中的二项树与二进制对应，二项队列的合并与二进制加法对应。  
二项树 BinTree 为 nullptr 表示二进制中 0，否则表示二进制中 1。

`trees[i]`、`other.trees[i]`、`carry`看作 3 个二进制位，三位能 0~7 共 8 中情况，用`state`表示这 8 种情况的编号。

将 state 表示为(carry, other, this)，不同的 state 值对应不同的操作：

- state=0：三者都为 nullptr，不操作
- state=1：只有 this，保留 this
- state=2：只有 other，将 other 移到 this，相当于加入队列
- state=3：只有 this 和 other 有，将两者合并成新的阶数加一的树，记为 carry，清空 this 和 other
- state=4：只有 carry 有，把 carry 移到 this
- state=5：只有 this 和 carry 有，将两者合并成新的 carry
- state=6：只有 other 和 carry 有，将两者合并成新的 carry
- state=7：三者都有，对应二进制本位为 1 且有进位
  - 把原来的 carry 放入 this（因为本位和为 1）
  - 将 this 和 other 合并成新的 carry（对应进位）
  - 清空 other

**代码示例：**

1. 合并二项树

```cpp
static BinTree combine(BinTree a, BinTree b) {
    if (a->val > b->val)
        swap(a, b);
    b->nextSibling = a->leftChild;
    a->leftChild = b;
    return a;
}
```

2. 合并二项队列

```cpp
void merge(BinomialQueue& other) {
    BinTree carry = nullptr;
    size += other.size;
    for (int i = 0; i < (int)trees.size(); i++) {
        int state = (trees[i] != nullptr) +
                    2 * (other.trees[i] != nullptr) +
                    4 * (carry != nullptr);
        switch (state) {
            case 0:
                break;
            case 1:
                break;
            case 2:
                trees[i] = other.trees[i];
                other.trees[i] = nullptr;
                break;
            case 3:
                carry = combine(trees[i], other.trees[i]);
                trees[i] = other.trees[i] = nullptr;
                break;
            case 4:
                trees[i] = carry;
                carry = nullptr;
                break;
            case 5:
                carry = combine(trees[i], carry);
                trees[i] = nullptr;
                break;
            case 6:
                carry = combine(other.trees[i], carry);
                other.trees[i] = nullptr;
                break;
            case 7:
                carry = combine(trees[i], other.trees[i]);
                trees[i] = other.trees[i] = nullptr;
                break;
        }
    }
    other.size = 0;
}

```

### 插入

将新插入的节点视为单个节点的二项树，再与原有的二项队列合并。

代码示例：

```cpp
void insert(int x) {
    BinomialQueue single;
    single.trees[0] = new Node(x);
    single.size = 1;
    merge(single);
}
```

### 查找最小值

查找最小值，只需要搜索所有二项树的根节点，这样时间复杂度为$O(\log n)$。  
另外，可以额外记录最小值、插入时更新最小值，这样时间复杂度为$O(1)$。

代码示例：

```cpp
int findMin() {
    int minVal = INT_MAX;
    for (auto t : trees) {
        if (t && t->val < minVal)
            minVal = t->val;
    }
    return minVal;
}
```

### 删除最小值

搜索所有二项树的根节点，删除最小值。剩余节点重新组合成二项队列。

代码示例：

```cpp
void deleteMin() {
    int minIdx = -1, minVal = INT_MAX;
    for (int i = 0; i < (int)trees.size(); i++) {
        if (trees[i] && trees[i]->val < minVal) {
            minVal = trees[i]->val;
            minIdx = i;
        }
    }
    if (minIdx == -1)
        return;

    // 取出最小树
    BinTree minTree = trees[minIdx];
    trees[minIdx] = nullptr;
    size -= (1 << minIdx);

    // 拆分它的孩子链，反向构建新队列
    BinomialQueue childQ;
    BinTree child = minTree->leftChild;
    for (int j = minIdx - 1; j >= 0; j--) {
        BinTree next = child->nextSibling;
        child->nextSibling = nullptr;
        childQ.trees[j] = child;
        child = next;
    }
    childQ.size = (1 << minIdx) - 1;

    merge(childQ);
    delete minTree;
}
```

??? examples "二项队列代码示例"

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;

    struct Node {
        int val;
        Node* leftChild = nullptr;    // 第一个孩子
        Node* nextSibling = nullptr;  // 下一个兄弟
        Node(int v) : val(v) {}
    };

    using BinTree = Node*;

    struct BinomialQueue {
        vector<BinTree> trees;  // 每个阶的二项树
        int size = 0;

        BinomialQueue(int maxTrees = 20) { trees.assign(maxTrees, nullptr); }

        // 合并两棵同阶二项树（小根堆）
        static BinTree combine(BinTree a, BinTree b) {
            if (a->val > b->val)
                swap(a, b);
            b->nextSibling = a->leftChild;
            a->leftChild = b;
            return a;
        }

        // 合并两个二项队列
        void merge(BinomialQueue& other) {
            BinTree carry = nullptr;
            size += other.size;
            for (int i = 0; i < (int)trees.size(); i++) {
                int state = (trees[i] != nullptr) +
                            2 * (other.trees[i] != nullptr) +
                            4 * (carry != nullptr);
                switch (state) {
                    case 0:
                        break;
                    case 1:
                        break;
                    case 2:
                        trees[i] = other.trees[i];
                        other.trees[i] = nullptr;
                        break;
                    case 3:
                        carry = combine(trees[i], other.trees[i]);
                        trees[i] = other.trees[i] = nullptr;
                        break;
                    case 4:
                        trees[i] = carry;
                        carry = nullptr;
                        break;
                    case 5:
                        carry = combine(trees[i], carry);
                        trees[i] = nullptr;
                        break;
                    case 6:
                        carry = combine(other.trees[i], carry);
                        other.trees[i] = nullptr;
                        break;
                    case 7:
                        carry = combine(trees[i], other.trees[i]);
                        trees[i] = other.trees[i] = nullptr;
                        break;
                }
            }
            other.size = 0;
        }

        // 插入一个元素
        void insert(int x) {
            BinomialQueue single;
            single.trees[0] = new Node(x);
            single.size = 1;
            merge(single);
        }

        // 查找最小值
        int findMin() {
            int minVal = INT_MAX;
            for (auto t : trees)
                if (t && t->val < minVal)
                    minVal = t->val;
            return minVal;
        }

        // 删除最小值
        void deleteMin() {
            int minIdx = -1, minVal = INT_MAX;
            for (int i = 0; i < (int)trees.size(); i++) {
                if (trees[i] && trees[i]->val < minVal) {
                    minVal = trees[i]->val;
                    minIdx = i;
                }
            }
            if (minIdx == -1)
                return;  // 空队列

            // 拿出最小树
            BinTree minTree = trees[minIdx];
            trees[minIdx] = nullptr;
            size -= (1 << minIdx);

            // 拆分它的孩子链，反向构建新队列
            BinomialQueue childQ;
            BinTree child = minTree->leftChild;
            for (int j = minIdx - 1; j >= 0; j--) {
                BinTree next = child->nextSibling;
                child->nextSibling = nullptr;
                childQ.trees[j] = child;
                child = next;
            }
            childQ.size = (1 << minIdx) - 1;

            merge(childQ);
            delete minTree;
        }
    };

    int main() {
        BinomialQueue H;
        for (int x : {5, 2, 8, 1, 3})
            H.insert(x);

        cout << "Min = " << H.findMin() << "\n";  // 输出 Min = 1
        H.deleteMin();
        cout << "Min after delete = " << H.findMin() << "\n";  // 输出 2
    }

    ```
