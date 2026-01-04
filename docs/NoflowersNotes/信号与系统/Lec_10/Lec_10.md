

## 系统函数

系统函数定义同 s 域，且 $H(z) = \mathcal{Z}(\delta[n])$. 通过差分方程，两边系数相除即可

$$
\begin{aligned}
    &\sum_{k = 0}^{s} a_ky[n - k] = \sum_{l = 0}^{t}b_lx[n - l] \\
    &H(z) = \frac{\displaystyle \sum_{l = 0}^s b_lz^{-l}}{\displaystyle \sum_{k = 0}^s a_kz^{-k}}
\end{aligned}
$$

一般保留负幂的形式，不需要化简.

## z 域零极点图和系统特性

其余和 s 域相同，这里讲一下微分方程的框图

### 离散时间系统的系统框图

给定微分方程

$$
\sum_{k = 0}^N a_ky[n - k] = \sum_{l = 0}^Mb_lx[n - l] = w[n]
$$

化简

$$
\begin{aligned}
    & w[n] = \sum_{l = 0}^Mb_lx[n - l] \\
    & y[n] = \frac{1}{a_0}\left(-\sum_{k = 1}^N a_ky[n - k] + w[n]\right)
\end{aligned}
$$

即可用反馈回路和级联实现

![alt text](image-1.png)

!!! examples "一个例子"

    ![alt text](image.png)

    这里合并延时器是因为延时器的开销是系统中最大的

    或者用 z 域的分析方法，处理方法类似于 s 域的分析
