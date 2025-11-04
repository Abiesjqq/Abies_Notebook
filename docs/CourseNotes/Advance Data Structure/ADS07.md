!!! warning-box "提醒"

    和 Noflower/算法设计分析/分治 高度重合，点击 [此处](/Abies_Notebook/NoflowersNotes/算法设计分析/分治/分治) 可移步。

## 最近点对问题

在平面上给定 \( n \) 个点，希望找出其中距离最近的两个点。  
输入：平面上 \( n \) 个点 \( P = \{p_1, p_2, \dots, p_n\} \)，每个点 \( p_i = (x_i, y_i) \)。
输出：一对点 \( (p_i, p_j) \)（\( i \ne j \)），使得它们之间的欧几里得距离最小。

分治法步骤：

1. 将点集分别按 x 坐标和 y 坐标排序，得到数组 \( P_x \) 和 \( P_y \)。
2. 用一条垂直线将点集分为左右两半，每边约 \( n/2 \) 个点，递归求解左半的最近距离 \( d_L \)，右半的最近距离 \( d_R \)。令 \( d = \min(d_L, d_R) \)。
3. 合并时要考虑跨越分割线的点对，只需取半宽为 $d$ 的带状区域（strip）即可。对 strip 中的点按 y 坐标排序，检查邻近的点，计算这些候选点对的距离，更新最小距离。

![strip point](./ADSresources/strip%20point.png){style="width:300px"}

理解：将 strip 划分为边长的 $d/2$ 的方格，将要考虑的点放在一条底边。希望距离小于 $d$，故一个方格以外的点不用考虑；而因为两边的最小距离都小于 $d$，一个方格内最多只有一个点。所以对于 strip 中的点，只需要检查相邻的 7 个方格，最多有 7 个邻居点，为常数时间。  
实际操作中，因为提前将点集按 y 坐标排序，只需比较后面至多 7 个点。

??? examples "代码示例 分治法最近点对"

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;

    struct Point {
        double x, y;
    };

    // 计算两点欧几里得距离
    double dist(const Point& a, const Point& b) {
        double dx = a.x - b.x;
        double dy = a.y - b.y;
        return sqrt(dx * dx + dy * dy);
    }

    // 合并阶段：仅比较带区中的点
    double stripClosest(vector<Point>& strip, double d) {
        double min_d = d;
        int n = strip.size();  // strip 中点数

        // strip 已按 y 排序，只需比较后面至多 7 个点
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n && (strip[j].y - strip[i].y) < min_d; ++j)
                min_d = min(min_d, dist(strip[i], strip[j]));
        return min_d;
    }

    // 分治核心
    double closestUtil(vector<Point>& Px, vector<Point>& Py) {
        int n = Px.size();  // 点的总数
        int mid = n / 2;
        double midx = Px[mid].x;  // 划分竖线的 x 值

        // 按 x 分成左右部分
        vector<Point> Qx(Px.begin(), Px.begin() + mid);
        vector<Point> Rx(Px.begin() + mid, Px.end());

        // 按 y 坐标划分成 Qy、Ry
        vector<Point> Qy, Ry;
        Qy.reserve(mid);  // 优先分配空间，后续 push_back 时不会扩容
        Ry.reserve(n - mid);
        for (auto& p : Py) {
            if (p.x <= midx)
                Qy.push_back(p);
            else
                Ry.push_back(p);
        }

        // 递归求解左右两侧的最小距离
        double dl = closestUtil(Qx, Qy);
        double dr = closestUtil(Rx, Ry);
        double d = min(dl, dr);

        // 构造带区 strip：距离分割线 <= d 的点
        vector<Point> strip;
        for (auto& p : Py)
            if (fabs(p.x - midx) < d)
                strip.push_back(p);

        // 带区扫描更新最小值
        return min(d, stripClosest(strip, d));
    }

    // 主函数：输入点集，返回最小距离
    double closestPair(vector<Point>& points) {
        vector<Point> Px = points, Py = points;
        sort(Px.begin(), Px.end(),
            [](auto& a, auto& b) { return a.x < b.x; });  // 按 x 排序
        sort(Py.begin(), Py.end(),
            [](auto& a, auto& b) { return a.y < b.y; });  // 按 y 排序
        return closestUtil(Px, Py);  // 调用函数传入排序后 Px、Py
    }

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);

        int n;
        cout << "Enter number of points: ";
        cin >> n;

        vector<Point> pts(n);
        cout << "Enter points (x y):\n";
        for (int i = 0; i < n; ++i)
            cin >> pts[i].x >> pts[i].y;

        double ans = closestPair(pts);
        cout << fixed << setprecision(6);
        cout << "Minimum distance = " << ans << "\n";
        return 0;
    }
    ```

## 时间复杂度：主定理

!!! normal-comment "几种时间复杂度"

      - $O$：上界，最坏情况
      - $o$：非紧上界
      - $\Omega$：下界，最好情况
      - $\omega$：非紧下界
      - $\Theta$：紧确界（即是上界又是下界），增长同阶

一般，分治 TC 的递推式为：

$$T(n)=aT(\frac{n}{b})+f(n)$$

认为 $f(n)=n^c$，得到主定理（Master Theorem）表达式：

$$
T(n) =
\begin{cases}
\displaystyle O(n^c), &\quad a < b^c \\
\displaystyle O(n^c\log n), &\quad a = b^c \\
\displaystyle O(n^{\log_ba}), &\quad a > b^d
\end{cases}
$$

??? normal-comment "主定理推导"

    **第一步：展开递推式（可选，用于理解）**

    我们也可以通过递归树或展开来直观理解：

    $$
    \begin{aligned}
    T(n) &= aT\left(\frac{n}{b}\right) + n^c \\
    &= a\left[ aT\left(\frac{n}{b^2}\right) + \left(\frac{n}{b}\right)^c \right] + n^c \\
    &= a^2 T\left(\frac{n}{b^2}\right) + a \cdot \frac{n^c}{b^c} + n^c \\
    &= a^2 \left[ aT\left(\frac{n}{b^3}\right) + \left(\frac{n}{b^2}\right)^c \right] + a \cdot \frac{n^c}{b^c} + n^c \\
    &= a^3 T\left(\frac{n}{b^3}\right) + a^2 \cdot \frac{n^c}{b^{2c}} + a \cdot \frac{n^c}{b^c} + n^c \\
    &\;\;\vdots \\
    &= a^k T\left(\frac{n}{b^k}\right) + n^c \sum_{i=0}^{k-1} \left( \frac{a}{b^c} \right)^i
    \end{aligned}
    $$

    当递归到底层时，\( \frac{n}{b^k} = 1 \Rightarrow k = \log_b n \)。

    所以总时间复杂度为：

    $$
    T(n) = a^{\log_b n} T(1) + n^c \sum_{i=0}^{\log_b n - 1} \left( \frac{a}{b^c} \right)^i
    $$

    注意到 \( a^{\log_b n} = n^{\log_b a} \)，因此：

    $$
    T(n) = \Theta\left( n^{\log_b a} \right) + n^c \cdot \sum_{i=0}^{\log_b n - 1} \left( \frac{a}{b^c} \right)^i
    $$

    现在关键看比值 \( \frac{a}{b^c} \)：

    ---

    **第二步：分情况讨论（即主定理的三种情形）**

    令 \( \alpha = \log_b a \)，即 \( a = b^\alpha \)。比较 \( \alpha \) 与 \( c \)：

    情况 1：\( c < \log_b a \)（即 \( f(n) = n^c \) 多项式小于 \( n^{\log_b a} \)）

    此时 \( \frac{a}{b^c} = b^{\log_b a - c} > 1 \)，几何级数主导项是最后一项：

    $$
    \sum_{i=0}^{\log_b n - 1} \left( \frac{a}{b^c} \right)^i = \Theta\left( \left( \frac{a}{b^c} \right)^{\log_b n} \right) = \Theta\left( n^{\log_b a - c} \right)
    $$

    所以：

    $$
    T(n) = \Theta(n^{\log_b a}) + n^c \cdot \Theta(n^{\log_b a - c}) = \Theta(n^{\log_b a})
    $$

    **结论**：若 \( f(n) = O(n^c) \) 且 \( c < \log_b a \)，则

    $$
    T(n) = \Theta(n^{\log_b a})
    $$

    ---

    情况 2：\( c = \log_b a \)

    此时 \( \frac{a}{b^c} = 1 \)，几何级数变成：

    $$
    \sum_{i=0}^{\log_b n - 1} 1 = \log_b n = \Theta(\log n)
    $$

    所以：

    $$
    T(n) = \Theta(n^c) + n^c \cdot \Theta(\log n) = \Theta(n^c \log n)
    $$

    **结论**：若 \( f(n) = \Theta(n^{\log_b a}) \)，则

    $$
    T(n) = \Theta(n^{\log_b a} \log n)
    $$

    ---

    情况 3：\( c > \log_b a \)

    此时 \( \frac{a}{b^c} < 1 \)，几何级数收敛到常数：

    $$
    \sum_{i=0}^{\log_b n - 1} \left( \frac{a}{b^c} \right)^i = \Theta(1)
    $$

    所以：

    $$
    T(n) = \Theta(n^{\log_b a}) + n^c \cdot \Theta(1) = \Theta(n^c)
    $$

    但注意：主定理的第三种情况还需要满足**正则条件（regularity condition）**：
    存在 \( \varepsilon > 0 \)，使得 \( a f(n/b) \leq k f(n) \) 对某个 \( k < 1 \) 成立（通常对多项式 \( f(n) = n^c \) 自动满足）。

    **结论**：若 \( f(n) = \Omega(n^c) \) 且 \( c > \log_b a \)，且满足正则条件，则

    $$
    T(n) = \Theta(f(n)) = \Theta(n^c)
    $$

    ---

    **总结（主定理，当 \( f(n) = n^c \) 时）**

    设 \( T(n) = aT(n/b) + n^c \)，其中 \( a \geq 1, b > 1, c \geq 0 \)，则：

    - 若 \( c < \log_b a \)，则 \( T(n) = \Theta(n^{\log_b a}) \)
    - 若 \( c = \log_b a \)，则 \( T(n) = \Theta(n^c \log n) \)
    - 若 \( c > \log_b a \)，则 \( T(n) = \Theta(n^c) \)

主定理不适用的情况：

- $a$ 不是常数
- $a<1$
- $f(n)$ 不是 $\Theta(n^c)$

**扩展主定理**：

它进一步允许 \(f(n)\) 在渐进意义上带有对数幂项，即：

\[
f(n)=\Theta!\big(n^{c}(\log n)^{k}\big),
\]

其中 \(c\ge0,\ k\ge 0\)。

则递推式：

\[
T(n)=a,T!\left(\frac{n}{b}\right)+\Theta!\big(n^{c}(\log n)^{k}\big)
\]

的解为：

$$
T(n) =
\begin{cases}
\displaystyle \Theta\big(n^{c}(\log n)^{k}\big), &\quad a < b^c \\
\displaystyle \Theta\big(n^{c}(\log n)^{k+1}\big), &\quad a = b^c \\
\displaystyle \Theta\big(n^{\log_b a}\big), &\quad a > b^d
\end{cases}
$$

??? normal-comment "扩展主定理推导"

    设 \(f(n)=\Theta(n^{c}(\log n)^k)\)，且 \(aT(n/b)\) 把问题划分为 \(a\) 个规模 \(n/b\) 的子问题。

    第 1 层（根），代价：\(f(n)\)。

    第 2 层，个子问题规模 \(n/b\)，共有 \(a\) 个，总代价：

    \[
    a,f(n/b) = a,(n/b)^c(\log (n/b))^k
    = n^c,a,b^{-c}(\log n - \log b)^k.
    \]

    第 \(i\) 层，共有 \(a^i\) 个子问题，规模 \(n/b^i\)，总代价：

    \[
    a^i f(n/b^i)
    = n^c (a/b^c)^i (\log (n/b^i))^k
    = n^c (a/b^c)^i (\log n - i\log b)^k.
    \]

    层数 \(L=\log_b n\)。

    ---

    分三种情况

    **(1) 当 \(a/b^c < 1\)**（即 \(c>\log_b a\)）

    上层代价逐层衰减，主导项在根层。

    \[
    T(n)=\Theta(n^c(\log n)^k).
    \]

    **(2) 当 \(a/b^c > 1\)**（即 \(c<\log_b a\)）

    每层代价增长，最后一层最大：

    \[
    T(n)=\Theta(n^{\log_b a}).
    \]

    **(3) 当 \(a/b^c = 1\)**（即 \(c=\log_b a\)）

    每层代价大约相等：

    \[
    \text{第 } i \text{ 层代价} \approx n^c(\log n - i\log b)^k,
    \]

    层数 \(\log*b n\)，把这些相加：

    \[
    T(n)\approx n^c\sum_{i=0}^{\log_b n} (\log n - i\log b)^k
    \approx n^c \int_0^{\log n} t^k,dt
    = \Theta(n^c(\log n)^{k+1}).
    \]

    这就是扩展主定理第 2 种情况的来源。

## 二进制整数乘法

将整数按二进制位划分，拆成高位和低位两部分：

$$
x = 2^m a + b,\quad y = 2^m c + d,
$$

于是：

$$
xy = 2^{2m}ac + 2^m(ad + bc) + bd.
$$

若递归地计算四个 \( \tfrac{n}{2} \)-位数的乘积（(ac, ad, bc, bd)），得到递推：$T(n) = 4T(n/2) + \Theta(n)$，解得 \( T(n) = \Theta(n^2) \)，并没有改进。

Karatsuba 改进：

$$
ad + bc = (a + b)(c + d) - ac - bd.
$$

因此只需计算 $ac,\ bd,\ (a+b)(c+d)$ 三个乘法。

$T(n) = 3T(n/2) + \Theta(n)= \Theta(n^{\log_2 3}) = O(n^{1.585})$，显著优于\( T(n) = \Theta(n^2) \) 的方法。

## 矩阵乘法

对两个 \( n \times n \) 矩阵 \( A, B \)：

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

传统方法需要 \( n^3 \) 次标量乘法和 \( n^3 - n^2 \) 次加法，时间复杂度为 $\Theta(n^3)$。

将矩阵分为四个 \( \frac{n}{2} \times \frac{n}{2} \) 的子块：

$$
A =
\begin{pmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{pmatrix}, \quad
B =
\begin{pmatrix}
B_{11} & B_{12} \\
B_{21} & B_{22}
\end{pmatrix}.
$$

则：

$$
C_{11} = A_{11}B_{11} + A_{12}B_{21} \\
C_{12} = A_{11}B_{12} + A_{12}B_{22} \\
C_{21} = A_{21}B_{11} + A_{22}B_{21} \\
C_{22} = A_{21}B_{12} + A_{22}B_{22}
$$

这样仍需要 8 次乘法，时间复杂度上无改进。

Strassen 注意到：通过巧妙的线性组合只用 7 次矩阵乘法（外加 18 次加减法），减少一次乘法：

$$
\begin{cases}
P_1 = A_{11}(B_{12} - B_{22}) \\
P_2 = (A_{11} + A_{12})B_{22} \\
P_3 = (A_{21} + A_{22})B_{11} \\
P_4 = A_{22}(B_{21} - B_{11}) \\
P_5 = (A_{11} + A_{22})(B_{11} + B_{22}) \\
P_6 = (A_{12} - A_{22})(B_{21} + B_{22}) \\
P_7 = (A_{11} - A_{21})(B_{11} + B\_{12})
\end{cases}
$$

然后组合成：

$$
\begin{cases}
C_{11} = P_5 + P_4 - P_2 + P_6 \\
C_{12} = P_1 + P_2 \\
C_{21} = P_3 + P_4 \\
C_{22} = P_1 + P_5 - P_3 - P_7
\end{cases}
$$

递推式：

$$
T(n) = 7T(n/2) + Θ(n^2),
$$

主定理解得：

$$
T(n) = Θ(n^{\log_2 7}) ≈ Θ(n^{2.81}).
$$

这是第一个低于 \( n^3 \) 的矩阵乘法算法。

采用更巧妙的分割方式（可利用机器学习），能得到更低的时间复杂度。但在实际应用中仍使用 $O(n^3)$ 的方法。

## 快速傅里叶变换 FFT

一个 n 次的复系数单变量多项式恰好有 n 个复根。一个 n-1 次的单变量多项式 A(x)由其在 n 个不同 x 值处的取值唯一确定。  
表示 n-1 次多项式：n 个系数，或 n 个点的取值。使用 point-value 表示能快速表示多项式乘法，但判断单个点是否在曲线上的代价更大。

多项式乘法：系数表示 - FFT -> point-value 表示 -> point-value 相乘 - inverse FFT -> 系数表示
FFT 在时域和频域间快速转化

将 n 次多项式按奇偶分为两个 n/2 次多项式，互为相反数的点的取值可转化为 n/2 次多项式取值的线性组合。  
递归计算奇数和偶数部分，时间复杂度为 $O(n\log n)$。





























## 其他

### 矩阵幂求斐波那契

斐波那契数列中，$F_1=1$，$F_2=1$。

定义矩阵 $M$:

$$M=\begin{pmatrix}0& 1 \\ 1 & 1 \end{pmatrix}$$

则：

$$M^n=\begin{pmatrix}F_{n-1} & F_{n} \\ F_n & F_{n+1} \end{pmatrix}$$

故可用矩阵的幂 $M^n$ 求 $F_n$。

用快速幂方法求幂的时间复杂度为 $O(\log n)$，故计算第 $n^2$、第 $n^3$ 项斐波那契数列的时间复杂度均为 $O(\log (n^k))=O(\log n)$。

### 两个数组找第 k 小值

给定两个有序数组 A、B，长度分别为 m、n。给定 k（$k<min\{m,n\}$），要在两数组的合并数组中找第 k 小的值，求最小时间复杂度？

最终情况为将 A、B 分别划分为两部分，且两者左边部分的最大值小于两者右边部分的最小值，左边部分个数和为 k。只需要找到两个数组中这个划分的位置。

假设 A 中划分位置 i 初始为 k，B 中划分位置 j 初始为 0。每次二分调整，保证 i+j=k，直到满足上述条件。时间复杂度约为 $O(\log k)$。

??? examples "代码示例 返回两有序数组合并后的中点"

    来自LeetCode 4. Median of Two Sorted Arrays.

    ```cpp
    class Solution {
    public:
        double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
            int n1 = nums1.size();
            int n2 = nums2.size();
            if (n1 > n2) {
                return findMedianSortedArrays(nums2, nums1);
            }

            int left = (n1 + n2 + 1) >> 1;
            int low = 0, high = n1;
            while (low <= high) {
                int mid1 = (low + high) >> 1;
                int mid2 = left - mid1;
                int l1 = INT_MIN, l2 = INT_MIN, r1 = INT_MAX, r2 = INT_MAX;
                if (mid1 < n1)
                    r1 = nums1[mid1];
                if (mid1 - 1 >= 0)
                    l1 = nums1[mid1 - 1];
                if (mid2 < n2)
                    r2 = nums2[mid2];
                if (mid2 - 1 >= 0)
                    l2 = nums2[mid2 - 1];

                if (l1 <= r2 && l2 <= r1) {
                    if ((n1 + n2) % 2) {
                        return (double)max(l1, l2);
                    } else {
                        return (double)(max(l1, l2) + min(r1, r2)) / 2.0;
                    }
                } else if (l1 > r2) {
                    high = mid1 - 1;
                } else {
                    low = mid1 + 1;
                }
            }
            return 0;
        }
    };
    ```

### 合并有序数组的时间复杂度

给定 k 个有序数组，k 个数组中元素总数为 n。求合并这 k 个数组的最小时间复杂度？

每次在 k 个数组的头部选出最小的元素，即将头部元素都放到最小堆中，取堆顶。时间复杂度为 $O(\log k)$。

一共需要取 n 个，故总时间复杂度为 $O(n\log k)$。
