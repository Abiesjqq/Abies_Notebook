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
