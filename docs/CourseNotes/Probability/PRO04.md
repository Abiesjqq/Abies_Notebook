## 数学期望

### 定义

**一元随机变量的期望：**

离散型（前提为级数绝对收敛）：

$$E(X)=\sum_{i=1}^nx_ip_i$$

连续型（前提为积分绝对收敛）：

$$E(X)=\int_{-\infty}^{+\infty}xf(x)\mathrm{d}x$$

!!! examples "Y=g(X)，求 Y 的期望"

    离散型：求 Y 的分布律，或用 $E(X)$ 代入。

    连续型：$f_X(x)$ --> $F_X(x)$ --> $F_Y(y)$ --> $f_Y(y)$ --> $\int_{-\infty}^{+\infty} yf_Y(y)\mathrm{d}y$

常见一维随机变量分布的数学期望：

| 分布名称       | 概率分布类型 | 参数                        | 数学期望（期望值）  |
| -------------- | ------------ | --------------------------- | ------------------- |
| 伯努利分布 (B) | 离散         | $p$（成功概率）             | $p$                 |
| 二项分布 (B)   | 离散         | $n$（试验次数）, $p$        | $np$                |
| 几何分布 (G)   | 离散         | $p$（成功概率）             | $\frac{1}{p}$       |
| 泊松分布 (P)   | 离散         | $\lambda$（事件平均发生率） | $\lambda$           |
| 均匀分布 (U)   | 连续         | $a, b$（区间端点）          | $\frac{a + b}{2}$   |
| 指数分布 (E)   | 连续         | $\lambda$（速率参数）       | $\frac{1}{\lambda}$ |
| 正态分布 (N)   | 连续         | $\mu$, $\sigma^2$           | $\mu$               |

**二元随机变量的期望：**

设 $Z$ 是实函数 $Z=h(X,Y)$。

离散型：

$$E(Z)=\sum_{i=1}^n\sum_{j=1}^n h(x_i,y_j)p_{ij}$$

连续型：

$$E(Z)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}h(x,y)f(x,y)\mathrm{d}x\mathrm{d}y$$

二元变量下求某个变量的期望：类似边际分布，$E(X)=\int_{-\infty}^{+\infty}d\mathrm{d}x\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y$。

### 性质

1. $E(c)=c$
2. $E(c_1X_1\pm\cdots\pm c_nX_n)=c_1E(X_1)\pm\cdots\pm c_nE(X_n)$
3. 当 $X,Y$ 相互独立时，$E(XY)=E(X)E(Y)$

## 方差

### 定义

方差记为 $Var(X)$，标准差记为 $\sigma(X)$。

$$Var(X)=E([X-E(X)]^2)=E(X^2)-E(X)^2$$

设随机变量 $X$ 具有期望 $E(X)=\mu$，方差 $Var(X)=\sigma^2\neq 0$。  
记 $X^*=\frac{X-\mu}{\sigma}$，则有 $E(X^*)=0,Var(X^*)=1$，称 $X^*$ 为 $X$ 的标准化变量。

常见一维随机变量分布的方差：

| 分布名称       | 概率分布类型 | 参数                        | 方差                   |
| -------------- | ------------ | --------------------------- | ---------------------- |
| 伯努利分布 (B) | 离散         | $p$（成功概率）             | $p(1 - p)$             |
| 二项分布 (B)   | 离散         | $n$（试验次数）, $p$        | $np(1 - p)$            |
| 几何分布 (G)   | 离散         | $p$（成功概率）             | $\frac{1 - p}{p^2}$    |
| 泊松分布 (P)   | 离散         | $\lambda$（事件平均发生率） | $\lambda$              |
| 均匀分布 (U)   | 连续         | $a, b$（区间端点）          | $\frac{(b - a)^2}{12}$ |
| 指数分布 (E)   | 连续         | $\lambda$（速率参数）       | $\frac{1}{\lambda^2}$  |
| 正态分布 (N)   | 连续         | $\mu$, $\sigma^2$           | $\sigma^2$             |

### 性质

1. $Var(c)=0$
2. $Var(cX)=c^2Var(X)$
3. $Var(X\pm Y)=Var(X)+Var(Y)\pm 2E((X-E(X))(Y-E(Y)))$
4. $Var(X)\le E((X-c)^2)$，当且仅当 $E(X)=c$ 时等号成立

### 变异系数

变异系数表示离散程度，是标准差和期望的比值。

$$Cv(X)=\frac{\sqrt{Var(X)}}{E(X)}$$

## 协方差

### 定义

协方差表示两个随机变量之间的相互关系。

$$\begin{align*}Cov(X,Y)&=E((X-E(X))(Y-E(Y)))\\&=E(XY)-E(X)E(Y)\end{align*}$$

随机变量 $X,Y$ 的相关系数为：

$$\rho_{XY}=\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}$$

### 性质

1. $Cov(X,Y)=Cov(Y,X)$
2. $Cov(X,X)=Var(X)$
3. $Cov(c,Y)=0$
4. $Cov(aX,bY)=abCov(X,Y)$
5. $Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$
6. $Cov(X+Y,X-Y)=Var(X)-Var(Y)$
7. $Cov(X^*,Y^*)=Cov(\frac{X-E(X)}{\sqrt{Var(X)}},\frac{Y-E(Y)}{\sqrt{Var(Y)}})=\rho_{XY}$

方差与协方差的关系：

$$\begin{align*}Var(X_1+\cdots +X_n)&=\sum_{i=1}^nVar(X) +2\sum_{1\le i<j\le n}Cov(X_i,Y_j)\\&=\sum_{i=1}^n\sum_{j=1}^nCov(X_i,Y_j)\end{align*}$$

若 $X_1,\cdots ,X_n$ 两两独立，则 $Var(X_1\pm\cdots\pm X_n)=Var(X_1)+\cdots +Var(X_n)$。

协方差与相关系数、标准差的关系：

$Cov(X,Y)=\rho_{XY}\sigma_X\sigma_Y$，若 $X,Y$ 相互独立，则协方差和相关系数均为零。

### 相关系数

相关系数是用来表征随机变量间线性关系紧密程度的量，绝对值越大表示线性关系的程度越大。

$|\rho_{XY}|=1$ 时，表示 $X,Y$ 为线性关系。大于零时正相关，小于零时负相关。$|\rho_{XY}|=0$ 时，称两者不相关或零相关。

相互独立一定不相关，但不相关不一定独立。相关一定步独立。

!!! examples "已知 f(x,y) 求协方差"

    $f(x,y)$ --> $E(XY),\,f_X(x),\, f_Y(y)$ --> $E(X),\, E(Y)$ --> $Cov(X,Y)$

!!! examples "已知 f(x,y) 判断相关性和独立性"

    $f(x,y)$ 不能分解成两函数的乘积，则先用积分分别求 $E(XY)$ 和 $E(X),E(Y)$，再用 $Cov(X,Y)=E(XY)-E(X)E(Y)\neq 0$ 说明相关、且不独立。

    $f(x,y)$ 能分解成两函数的乘积，则求 $f_X(x)$ 和 $f_Y(y)$，再用 $f(x,y)=f_X(x)f_Y(y)$ 说明独立、且不相关。

## 其他数字特征

k 阶原点矩：

$$E[X^k]$$

k 阶中心矩：

$$E[(X - E[X])^k]$$

k+l 阶混合原点矩：

$$E[X^k Y^l]$$

k+l 阶混合中心矩：

$$E[(X - E[X])^k (Y - E[Y])^l]$$

上$\alpha$分位数：

$$\inf\{x \in \mathbb{R} \mid P(X \leq x) \geq 1 - \alpha\}$$

众数：

$$Mo(X)$$

## 多元随机变量的数字特征

数学期望向量、协方差矩阵。

略。
