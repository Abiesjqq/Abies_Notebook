## AVL 树

平衡因子 bf = 左子树高度 - 右子树高度  
AVL Tree：所有节点的|bf|<=1

- LL: 右旋
- RR：左旋
- LR：子节点左旋，右旋
- RL：子节点右旋，左旋

??? normal-comment "代码示例"

    节点定义：
    ```c
    typedef struct AVLTree {
        int val;
        struct AVLTree* left;
        struct AVLTree* right;
        int height;
    } AVLTree;

    typedef AVLTree* node;
    ```

    左旋、右旋：
    ```c
    node left_rotate(node x) {
        node y = x->right;
        node yl = y->left;

        y->left = x;
        x->right = yl;

        x->height = max(height(x->left), height(x->right)) + 1;
        y->height = max(height(y->left), height(y->right)) + 1;

        return y;
    }

    node right_rotate(node x) {
        node y = x->left;
        node yr = y->right;

        y->right = x;
        x->left = yr;

        x->height = max(height(x->left), height(x->right)) + 1;
        y->height = max(height(y->left), height(y->right)) + 1;

        return y;
    }
    ```

    删除：
    ```c
    待补充
    ```

删除：用左子树或右子树最接近的节点替换，检查平衡

## 红黑树

性质：

1. 节点为红色或黑色
2. 根节点为黑色，NIL 节点（空叶子节点）为黑色
3. 红色节点的子节点为黑色
4. 从根节点到 NIL 节点的每条路径上的黑色节点数量相同

合法红黑树的红色节点的两个子节点一定都是叶子或都不是叶子。

从根到叶节点的路径，最长路径最多是最短路径的两倍。

有 N 个内部节点的红黑树，树高最大为$2\log_2(N+1)$

??? remarks "证明"

    bh表示黑高，h表示树高

    $N\ge 2^{bh}-1$, 即 $bh\le\log_2(N+1)$

    $h\le 2\, bh=2\log_2(N+1)$

**插入**

插入节点默认为红色。

1. 插入节点是根节点：直接变黑
2. father 为红色，uncle 为红色：uncle, father, grandfather 变色，将 grandfather 作为插入节点重新判断
3. father 为红色，uncle 为黑色：（LL, RR, LR, RL）旋转，再变色
