## 回溯概述

### 最大子序列和

??? normal-comment "线性规划、前缀和？"

    **1. 线性规划**

    `cur` 记录以当前位置结束的最大子序列和， `res` 存储结果。

    代码：

    ```cpp
    void findMaxSum(vector<int>& a) {
        int res = a[0];
        int cur = a[0];
        for (int i = 1; i < a.size(); i++) {
            cur = max(a[i], cur + a[i]);
            res = max(res, cur);
        }
        cout << res << '\n';
    }
    ```

    ---

    **2. 前缀和**

    当前的最大前缀和 = 当前前缀和 - 前半部分的最小前缀和

    ```cpp
    void findMaxSum2(vector<int>& a) {
        int pre = 0, minpre = INT_MAX, res = -INT_MAX;
        for (int x : a) {
            pre += x;
            res = max(res, pre - minpre);
            minpre = min(minpre, pre);
        }
        cout << res << '\n';
    }
    ```

分治法：先递归求解左右两部分的最大子序列和，再单独求解跨过中点的子序列和，三者取最大值。

