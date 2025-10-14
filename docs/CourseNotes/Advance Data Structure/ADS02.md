# ADS Lec 02 红黑树和 B+树

## 红黑树

### 红黑树性质

1. 节点为红色或黑色
2. 根节点为黑色，NIL 节点（空叶子节点）为黑色
3. 红色节点的子节点为黑色
4. 从根节点到 NIL 节点的每条路径上的黑色节点数量相同

合法红黑树的红色节点的两个子节点一定都是叶子或都不是叶子。

从根到叶节点的路径，最长路径最多是最短路径的两倍。

有 N 个内部节点的红黑树，树高最大为$2\log_2(N+1)$
（bh 表示黑高，h 表示树高，$N\ge 2^{bh}-1$, 即 $bh\le\log_2(N+1)$，$h\le 2\, bh=2\log_2(N+1)$）

### 插入

插入节点默认为红色。

1. 插入节点是根节点：直接变黑
2. father 为红色，uncle 为红色：uncle, father, grandfather 变色，将 grandfather 作为插入节点重新判断
3. father 为红色，uncle 为黑色：（LL, RR, LR, RL）旋转，再变色

### 删除

**回忆二叉树的删除：**

1. 叶节点：直接删除
2. 只有一个孩子：直接用孩子代替
3. 有两个孩子：找到左子树中最大的或右子树中最小的，代替删除节点，继续删除这个节点

红黑树删除：先按二叉搜索树方法删除，再调整。  
第三种一定会转化为前两种，只讨论前两种情况。

只有一个孩子：一定是当前黑，唯一的孩子红，且孩子为叶节点。  
直接用孩子红节点代替，再将代替后的节点变黑

没有孩子，且删除红节点：直接删除

没有孩子，且删除黑节点：  
认为删除后替换的 NIL 为“双黑节点”

1. 兄弟是黑色：
   1. 兄弟至少有一个红色孩子：根据父亲 p、兄弟 s、兄弟红孩子 r 关系（LL,RR,LR,RL）变色+旋转，双黑恢复为单黑
      1. LL 型和 RR 型：r 变 s，s 变 p，p 变黑
      2. LR 型和 RL 型：r 变 p，p 变黑
   2. 兄弟的孩子都是黑色：兄弟变红，双黑上移到父节点
      1. 父节点为红：直接将父节点变黑
      2. 父节点为黑：双黑上移到父节点，对父节点重复操作
      3. 父节点为根节点：双黑上移后碰到根节点，直接变成单黑
2. 兄弟是红色：
   兄父变色，父亲朝双黑节点旋转，保持双黑继续调整

![RBTree insertion](./ADSresources/RBTree%20insertion.png)

<!-- ![RBTree deletion](./ADSresources/RBTree%20deletion.png) -->

??? examples "红黑树代码示例"

      ```cpp
      #include <bits/stdc++.h>
      using namespace std;

      enum Color { RED, BLACK };

      struct Node {
         int val;
         Color color;
         Node *l, *r, *p;

         Node(int val) : val(val), color(RED), l(nullptr), r(nullptr), p(nullptr) {}
      };

      class RBTree {
         private:
         Node* root;

         // 左旋
         void rotLeft(Node* x) {
            Node* y = x->r;
            x->r = y->l;
            if (y->l)
                  y->l->p = x;

            y->p = x->p;
            if (!x->p)
                  root = y;
            else if (x == x->p->l)
                  x->p->l = y;
            else
                  x->p->r = y;

            y->l = x;
            x->p = y;
         }

         // 右旋
         void rotRight(Node* x) {
            Node* y = x->l;
            x->l = y->r;
            if (y->r)
                  y->r->p = x;

            y->p = x->p;
            if (!x->p)
                  root = y;
            else if (x == x->p->l)
                  x->p->l = y;
            else
                  x->p->r = y;

            y->r = x;
            x->p = y;
         }

         // 插入后调整
         // case 1：父红、叔红，父叔变黑、爷变红，递归向上
         // case 2：父红、叔黑、LL/RR，父变黑、爷变红，旋转爷爷
         // case 3：父红、叔黑、LR/RL，先旋转父亲转为case2，再处理
         void insertFix(Node* z) {
            while (z->p && z->p->color == RED) {
                  if (z->p == z->p->p->l) {  // 父亲是左节点
                     Node* y = z->p->p->r;  // y表示叔叔节点
                     // case 1: 叔叔是红色
                     if (y && y->color == RED) {
                        z->p->color = BLACK;
                        y->color = BLACK;
                        z->p->p->color = RED;
                        z = z->p->p;  // 继续向上调整
                     } else {
                        // case 3 LR: z是右孩子，先转为LL
                        if (z == z->p->r) {
                              z = z->p;    // 先更新z指向父亲
                              rotLeft(z);  // 左旋父亲，变成LL情况
                        }
                        // case 2 LL: z是左孩子
                        z->p->color = BLACK;
                        z->p->p->color = RED;
                        rotRight(z->p->p);  // 右旋爷爷
                     }
                  } else {                   // 父亲是右节点（镜像操作）
                     Node* y = z->p->p->l;  // 叔叔节点
                     // case 1: 叔叔是红色
                     if (y && y->color == RED) {
                        z->p->color = BLACK;
                        y->color = BLACK;
                        z->p->p->color = RED;
                        z = z->p->p;
                     } else {
                        // case 3 RL: z是左孩子，先转为RR
                        if (z == z->p->l) {
                              z = z->p;     // 先更新z指向父亲
                              rotRight(z);  // 右旋父亲，变成RR情况
                        }
                        // case 2 RR: z是右孩子
                        z->p->color = BLACK;
                        z->p->p->color = RED;
                        rotLeft(z->p->p);  // 左旋爷爷
                     }
                  }
            }
            root->color = BLACK;  // 根节点必须是黑色
         }

         // 用子树v替换u
         void transplant(Node* u, Node* v) {
            if (!u->p)
                  root = v;
            else if (u == u->p->l)
                  u->p->l = v;
            else
                  u->p->r = v;

            if (v)
                  v->p = u->p;
         }

         // 找最小节点
         Node* minNode(Node* x) {
            while (x->l)
                  x = x->l;
            return x;
         }

         // 删除后调整
         // case 1：兄红，兄父变色，父向双黑转，转化为其他情况
         // case 2：兄黑、兄弟儿子都黑，兄变红，双黑上移到父，递归
         // case 3：兄黑、兄一个儿子红、LL/RR，红儿子变父、父变黑，父转
         // case 4：兄黑、兄一个儿子红、LR/RL，红儿子、兄变色，兄转，转化为case 3
         void deleteFix(Node* x, Node* xp) {
            while (x != root && (!x || x->color == BLACK)) {
                  if (x == xp->l) {     // 要删除的节点是左儿子
                     Node* s = xp->r;  // s表示兄弟
                     // case 1
                     if (s && s->color == RED) {
                        x->color = BLACK;
                        xp->color = RED;
                        rotLeft(xp);
                        s = xp->r;
                     }
                     // case 2
                     if ((!s->l || s->l->color == BLACK) &&
                        (!s->r || s->r->color == BLACK)) {
                        if (s)
                              s->color = RED;
                        x = xp;
                        xp = xp->p;
                     }
                     // case 3 RL
                     else {
                        if (!s->r || s->r->color == BLACK) {
                              if (s->l)
                                 s->l->color = BLACK;
                              s->color = RED;
                              rotRight(s);
                              s = xp->r;
                        }
                        // case 4 RR
                        s->color = xp->color;
                        xp->color = BLACK;
                        if (s->r)
                              s->r->color = BLACK;
                        rotLeft(xp);
                        x = root;
                        break;
                     }
                  } else {
                     Node* s = xp->l;
                     if (s && s->color == RED) {
                        s->color = BLACK;
                        xp->color = RED;
                        rotRight(xp);
                        s = xp->l;
                     }
                     if ((!s->l || s->l->color == BLACK) &&
                        (!s->r || s->r->color == BLACK)) {
                        if (s)
                              s->color = RED;
                        x = xp;
                        xp = xp->p;
                     } else {
                        if (!s->l || s->l->color == BLACK) {
                              if (s->r)
                                 s->r->color = BLACK;
                              s->color = RED;
                              rotLeft(s);
                              s = xp->l;
                        }
                        if (s->l)
                              s->l->color = BLACK;
                        rotRight(xp);
                        x = root;
                        break;
                     }
                  }
            }
            if (x)
                  x->color = BLACK;
         }

         public:
         RBTree() : root(nullptr) {}

         // 插入
         void insert(int val) {
            Node* z = new Node(val);
            Node* y = nullptr;
            Node* x = root;

            while (x) {
                  y = x;
                  if (z->val < x->val)
                     x = x->l;
                  else
                     x = x->r;
            }

            z->p = y;
            if (!y)
                  root = z;
            else if (z->val < y->val)
                  y->l = z;
            else
                  y->r = z;

            insertFix(z);
         }

         // 删除
         void remove(int val) {
            Node* z = root;
            while (z && z->val != val)
                  z = (val < z->val ? z->l : z->r);
            if (!z)
                  return;

            Node* y = z;
            Node* x = nullptr;
            Node* xp = nullptr;
            Color yc = y->color;

            if (!z->l) {
                  x = z->r;
                  xp = z->p;
                  transplant(z, z->r);
            } else if (!z->r) {
                  x = z->l;
                  xp = z->p;
                  transplant(z, z->l);
            } else {
                  y = minNode(z->r);
                  yc = y->color;
                  x = y->r;
                  if (y->p == z) {
                     if (x)
                        x->p = y;
                     xp = y;
                  } else {
                     transplant(y, y->r);
                     y->r = z->r;
                     y->r->p = y;
                     xp = y->p;
                  }
                  transplant(z, y);
                  y->l = z->l;
                  y->l->p = y;
                  y->color = z->color;
            }
            delete z;
            if (yc == BLACK)
                  deleteFix(x, xp);
         }

         // 中序遍历
         void inorder(Node* t) {
            if (!t)
                  return;
            inorder(t->l);
            cout << t->val << (t->color == RED ? "(R) " : "(B) ");
            inorder(t->r);
         }

         // 输出树结构
         void printTree(Node* t, string prefix = "", bool isLeft = true) {
            if (!t)
                  return;

            cout << prefix;
            cout << (isLeft ? "|-- " : "\\-- ");
            cout << t->val << (t->color == RED ? "(R)" : "(B)") << endl;

            if (t->l || t->r) {
                  if (t->l)
                     printTree(t->l, prefix + (isLeft ? "|   " : "    "), true);
                  else
                     cout << prefix << (isLeft ? "|   " : "    ") << "|-- null\n";

                  if (t->r)
                     printTree(t->r, prefix + (isLeft ? "|   " : "    "), false);
                  else
                     cout << prefix << (isLeft ? "|   " : "    ") << "`-- null\n";
            }
         }

         // 输出
         void print() {
            cout << "Inorder: ";
            inorder(root);
            cout << '\n';
         }

         void printStructure() {
            cout << "Tree structure:\n";
            if (root)
                  printTree(root);
            else
                  cout << "Empty tree\n";
            cout << '\n';
         }

         Node* getRoot() { return root; }
      };

      int main() {
         RBTree tree;
         int arr[] = {10, 20, 30, 15, 25, 40, 50};

         for (int v : arr) {
            cout << "========== Insert " << v << " ==========\n";
            tree.insert(v);
            tree.print();
            tree.printStructure();
         }

         cout << "\n========== Delete 20 ==========\n";
         tree.remove(20);
         tree.print();
         tree.printStructure();

         cout << "\n========== Delete 40 ==========\n";
         tree.remove(40);
         tree.print();
         tree.printStructure();
      }
      ```

## B 树

### B 树性质

AVL 树、红黑树都将数据存到内存。当数据量大到内存存不下时，需要将数据存到硬盘，再分批从硬盘读到内存。  
（硬盘：CPU 不能直接和硬盘交互，硬盘读取物理地址连续的多个字节和读取单个字节的耗时几乎没有区别。）

硬盘访问时间长，尽可能减少硬盘的访问次数。而对于 AVL 树和红黑树，每往下找一层都要访问硬盘，硬盘访问次数和树高正相关。  
B 树是多叉平衡搜索树，降低树高。

- 内部节点：包含数据的节点
- 外部节点：表示查找失败，这里省略
- 叶节点：这里将最后一层内部节点称为叶节点

1. 平衡：叶节点都在同一层
2. 有序：任何节点内都从小到大，左子树<元素<右子树
3. 多路：对于 m 阶 B 树，每个节点最多有 m 个分支、m-1 个元素

根节点最少 2 个分支、1 个元素（除非只有根节点）  
其他节点最少$\lceil\frac{m}{2}\rceil$个节点，$\lceil\frac{m}{2}\rceil-1$个元素

### 查找、插入

**查找**：在节点内依次比较（顺序查找为例，更大就向右比较，更小就向下到子树）

**插入**：插入在叶节点。如果上溢出（节点内的元素超出），以第$\lceil\frac{m}{2}\rceil$个元素分割，将这个元素上移到父节点，两边分裂。如果父节点上溢出，递归调整。

### 删除

插入会上溢出，而删除会下溢出（节点内的元素个数过少）

查找要删除的节点，如果非叶节点，转化为直接前驱或直接后继替换，再删除替换的节点。

如果出现下溢出，首先用左右兄弟补全。先将父亲节点对应元素下移，再将兄弟节点中的元素上移。如果兄弟有子树，要将子树也移动到补全的节点。

如果左右兄弟都不够补全，将节点和其中一个兄弟合并。先将父亲节点对应元素下移，再将要合并的元素合并，删除父亲中空节点和空子树。  
要检查父亲节点是否也下溢出，递归调整。

## B+树

### B+树性质

在 B 树中按顺序遍历节点，需要中序遍历来回移动。而 B+树中可以直接遍历叶节点。

B+树的叶节点层包含所有元素，从小到大链接起来。  
B+树常用于数据库中的索引结构，每个元素都包含指向记录存储地址的指针，此时节点内的元素又被称为关键字。通过关键字中的指针，可以索引到数据库中的某一条记录。  
B+树本身也作为索引文件存储在硬盘中。

- B+树节点内元素个数和分支数相同，每个元素对应子节点的最大值。非叶节点是对下一层节点的索引。
- 其他性质与 B 树相同。节点最少 2 个分支、1 个元素（除非只有根节点）；其他节点最少$\lceil\frac{m}{2}\rceil$个节点，$\lceil\frac{m}{2}\rceil-1$个元素

阶为 3 的 B+树称为 2-3 树；阶为 4 的 B+树称为 2-3-4 树。

!!! normal-comment "B+树和 B 树的区别"

    B 树中 m 个分支的节点内有 m-1 个元素，而 B+树中 m 个分支的节点内有 m 个元素

    B 树中每个节点都包含指向相应记录的指针，而 B+树中只有叶节点包含指向相应记录的指针，非叶节点只作为查找叶节点的多级索引。

    B 树只有根节点一个头指针。B+树有两个头指针，即能通过叶节点链表的头指针顺序查找，也能通过根节点的指针随机查找。

!!! warning-box "注意！"

    <span style="color:red">课上讲的 B+树结构与上面不同！</span>

    课堂中的 B+树：

    - B+树中，有 m 个分支的节点内部有 m-1 个元素，其中第 k 个元素为第 k+1 个分支所有叶节点的最小值。每次走到下一层子树的条件为，节点内部的元素中大于等于前一个且小于后一个。
    - 节点内部元素个数固定为 M-1 个，空位用 - 填充。
    - 插入导致上溢出时，优先考虑用兄弟弥补。兄弟无法解决时再分裂。
    - 上溢出分裂时，在第$\lceil\frac{m}{2}\rceil$右侧分裂，父亲中增加第$\lceil\frac{m}{2}\rceil+1$个元素。

### 查找

顺序查找：直接在叶节点链表上查找

随机查找：从根节点开始查找，直到叶节点。在节点内依次比较（顺序查找为例，大于就向右比较，小于等于就向下到子树）

范围查找：e.g. 查找范围为[A,B]的节点。先随机查找到左边界，在顺序遍历直到右边界。
