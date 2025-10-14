## 回溯概述

回溯算法主要应用于搜索。相比于暴力搜索，能排除一些不可能的情况，从而提高效率。

大致思路：

- 假设我们已经得到部分解 $(x_1, \dots, x_i)$，其中 $x_k \in S_k,\ 1 \le k \le i < n$（$S_k$ 表示第 $k$ 步下的选择集（S means Stage or (partial) Solution），而 $x_k$ 便是其中的一个选项）
- 首先将一种可能情况 $x_{i+1} \in S_{i+1}$ 加到这个部分解中，并检查新的部分解 $(x_1, \dots, x_i, x_{i+1})$ 是否满足限制条件
- 如果满足条件，继续添加下一种情况到部分解中（重复上一步）
- 但如果 $S_{i+1}$ 中没有满足要求的选择，那么表示沿 $x_i$ 往下走是走不通的，那么就删掉 $x_i$，并回溯到上一个部分解 $(x_1, \dots, x_{i-1})$，然后从 $S_i$ 中挑选另外的可能情况 $x_i'$，以此类推

博弈树中，应该尽可能将路径数少的放在靠近根节点的位置，这样一旦不合法排除的可能情况占比更大。

### N 皇后问题

在 N\*N 的棋盘上摆放 N 个皇后，任意两个皇后都不能处于同一行、同一列或同一斜线上。求摆放方式。

每个皇后占据的位置为当前位置和同一行、列、斜线中所有位置。  
从第一行开始，在空余位置上逐行摆放。如果某一行没有空位，说明之前的摆放有问题，回溯。

按课上所讲的，八皇后问题返回八维向量，第 i 位 $x_i$ 表示第 i 行的皇后的位置。  
这样的表示形式已经排除的同行的情况。进一步排除同列的情况，需要 $x_i\neq x_j \,(i\neq j)$；排除同一斜线的情况，需要 $\frac{x_i-x_j}{i-j}\neq \pm1\,(i\neq j)$。

回溯算法相当于用深度优先搜索检查博弈树的每一条路径。如果已经判定为不可能，则不用继续往下搜索、退回到上一步。

!!! examples "示例 N 皇后问题"

    **题目描述：**

    输入 N，输出 N 皇后问题解的个数。（或输出每种解的情况，这里代码中计算但不输出）

    **代码：**

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;

    class Solution {
    private:
        int n;
        vector<string> queen;
        vector<vector<int>> attack;
        vector<vector<string>> res;

        // (x,y)放置皇后后，更新attack
        void putQueen(int x, int y, vector<vector<int>>& atk) {
            static const int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
            static const int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
            atk[x][y] = 1;
            for (int i = 1; i < n; i++) {
                for (int j = 0; j < 8; j++) {
                    int nx = x + i * dx[j];
                    int ny = y + i * dy[j];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n)
                        atk[nx][ny] = 1;
                }
            }
        }

        // 回溯
        void backTrack(int r) {
            if (r == n) {
                res.push_back(queen);
                return;
            }
            for (int i = 0; i < n; i++) {
                if (attack[r][i] == 0) {
                    vector<vector<int>> tmp = attack;
                    queen[r][i] = 'Q';
                    putQueen(r, i, attack);
                    backTrack(r + 1);
                    attack = tmp;
                    queen[r][i] = '.';
                }
            }
        }

    public:
        vector<vector<string>> solveNQueens(int n) {
            this->n = n;
            attack.assign(n, vector<int>(n, 0));
            queen.assign(n, string(n, '.'));
            backTrack(0);
            return res;
        }
    };

    int main() {
        Solution solution;
        auto res = solution.solveNQueens(8);
        cout << "Number of solutions: " << res.size() << '\n';
        return 0;
    }
    ```

    注意：

    - `putQueen`需要传入参数 atk（attack），否则内部修改全部的 attack 而不是递归内部的副本，不同递归分支间相互污染。
    - `solveNQueens`中传入的参数 n 覆盖了成员 n，需要规定 `this->n = n`。

### 收费公路重建问题

给定 $N$ 个在 x 轴上的点，它们的坐标满足 $x_1 < x_2 < \ldots x_N$，并假设 $x_1 = 0$。在所有点中任取两点，一共有 $\frac{N(N - 1)}{2}$ 种取法，对应有 $\frac{N(N - 1)}{2}$ 不同的路径。  
给定 $\frac{N(N - 1)}{2}$ 条路径，如何重新构造（reconstruct）一个点集？

令输入的所有路径长度组成 $D$，起点 $x_1 = 0$，终点 $x_N=D_{max}$。将这两个距离从 $D$ 中删除。  
每次考虑 $D$ 中剩余距离的最大值，其对应的点只可能是到起点或终点的距离为这个最大值。分别考虑到起点、到终点的情况，检查和已有的所有点的距离是否包含在剩余的 $D$ 中。如果某个距离不包含在 $D$ 中，则说明这种排列有问题，回溯。

!!! examples "示例 收费公路重建问题"

    **题目描述：**

    第一行输入 n 表示点数，D 表示最大距离。第二行输入 N(N-1)/2 个点，表示两两距离。输出点排列数。

    **代码：**

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;

    class Solution {
    private:
        int n, D;
        vector<vector<int>> res;

        bool isValid(int nx, const vector<int>& x, multiset<int>& dist) {
            for (int u : x) {
                int d = abs(nx - u);
                auto it = dist.find(d);
                if (it == dist.end())
                    return false;
                dist.erase(it);
            }
            return true;
        }

        void backTrack(vector<int> x, multiset<int> dist) {
            if (x.size() == n) {
                sort(x.begin(), x.end());
                res.push_back(x);
                return;
            }

            int M = *dist.rbegin();  // 当前最大距离
            vector<int> candidates = {M, D - M};
            for (int cand : candidates) {
                if (cand < 0 || cand > D)
                    continue;
                auto tmp = dist;
                if (isValid(cand, x, tmp)) {
                    x.push_back(cand);
                    backTrack(x, tmp);
                    x.pop_back();
                }
            }
        }

    public:
        vector<vector<int>> solveTurnpike(int n, int D, multiset<int> dist) {
            this->n = n;
            this->D = D;

            if (n == 1)
                return {{0}};
            if (dist.find(D) == dist.end())
                return {};

            dist.erase(dist.find(D));
            vector<int> x = {0, D};
            backTrack(x, dist);
            sort(res.begin(), res.end());
            res.erase(unique(res.begin(), res.end()), res.end());
            return res;
        }
    };

    int main() {
        int n, D;
        multiset<int> dist;
        cin >> n >> D;
        for (int i = 0; i < n * (n - 1) / 2; i++) {
            int d;
            cin >> d;
            dist.insert(d);
        }
        Solution solution;
        auto res = solution.solveTurnpike(n, D, dist);
        cout << "Number of solutions: " << res.size() << '\n';
        for (auto& v : res) {
            for (int x : v)
                cout << x << ' ';
            cout << '\n';
        }
        return 0;
    }
    ```

### 博弈树

博弈树的每一个节点对应一个局面，每一条边对应一个动作。

#### 极小极大搜索

关于每个局面，定义评价函数。赢的评估值为 1，输的评估值为 -1，平局的评估值为 0。评价函数定义为：子树的叶节点中“赢的数量”-“输的数量”。

正、反方每走一步，都选择使自己赢得更多的节点。正方选择的节点称为 MAX 节点（评估值最大），反方选择的节点称为 MIN 节点（评估值最小）。  
由于正反方交替走步，MAX 层和 MIN 层 会交替出现。

步骤：

1. 构建博弈树；
2. 将评估函数应用于叶子节点（1 或 -1）；
3. 自底向上计算每个节点的 MINMAX 值；
4. 从根节点选择 MINMAX 值最大的分支，作为行动策略。

#### $\alpha-\beta$ 剪枝

对于 MAX 层节点，可以看作评估值的初试值为 $-\infty$，随着子节点的遍历向上增长；而对于 MIN 层节点，可以可以看作评估值的初试值为 $+\infty$，随着子节点的遍历向下减小。

对于 MIN 层节点，上一层 MAX 层会选择评估值小的节点。  
评估值的计算按中序遍历（并非二叉树时不存在“中序”，即第一个儿子、父亲、第二个儿子、父亲……的顺序）进行。对任意 MAX 层父亲节点，遍历完第一条路径后，父亲的 MINMAX 值从 $+\infty$ 降低为第一个儿子的 MINMAX 值。  
对于剩下的 MIN 子节点，当 MINMAX 值小于 MAX 父亲的 MINMAX 值时，肯定不会被父亲节点选择，因此不用继续遍历子节点。  
每次修改节点的 MINMAX 值时，都要检查还有没有可能被父亲选择。如果当前的 MINMAX 值小于 MAX 父亲的值、或大于 MIN 父亲的值，则不用继续搜索，即完成剪枝。

为什么叫 $\alpha-beta$ ？

- alpha：如果当前是 MAX 节点，能保证的最大值的最小值
- beta：如果当前是 MIN 节点，能保证的最小值的最大值

课上增加了 $\alpha$ 剪枝和 $\beta$ 剪枝的概念：

- $\alpha$ 剪枝：MIN 层子节点的值小于 MAX 层父节点的值
- $\beta$ 剪枝：MAX 层子节点的值大于 MIN 层父节点的值
