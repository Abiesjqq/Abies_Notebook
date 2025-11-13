## 二维随机变量

E 是随机试验，样本空间为 S={e}。设 X=X(e), Y=Y(e) 为 S 上的随机变量，则 (X,Y) 称为二维随机变量。

二维随机变量分为离散型二维随机变量和连续型二维随机变量

## 离散型的分布

### 联合分布

用二维表表示离散型二维随机变量的联合分布，其中第 i 行第 j 列表示 $P\{X=x_i,Y=y_i\}$。

$$
\begin{array}{c|ccc}
 & y_1=0 & y_2=1 & y_3=2 \\
\hline
x_1=0 & 0.1 & 0.2 & 0.1 \\
x_2=1 & 0.2 & 0.3 & 0.1 \\
\end{array}
$$

### 边际分布

边际分布即二维变量中其中一维固定的概率，相当于全概率公式。

固定 X 变量，即联合分布中一行的概率相加；固定 Y 变量，即联合分布中一列的概率相加。

$$P\{X=x_i\}=P\{X=x_i,\bigcup_{j=1}^{\infty}(Y=y_i)\}=\sum_{j=1}^{\infty}p_{ij}\triangleq p_{i\cdot}$$

二维表表示时，在最下面和最右边各加一行、一列，表示边际分布。

### 条件分布

条件分布即 X 和 Y 满足一定条件下，X 或 Y 取某个值的概率。

将 X 和 Y 的条件转化为 X 和 Y 分别的取值，在联合分布中查找相加。

## 联合分布函数

记二维分布函数为 $F(x,y)$：

$$F(x,y)=P\{(X\le x)\cap (Y\le y)\}\triangleq P\{X\le x,Y\le y\}$$

类似二维前缀和，可用分布函数计算 X 和 Y 在某个区间的概率：

$$P\{x_1\le X\le x_2,y_1\le Y \le y_2\}=F(x_2,y_2)-F(x_1,y_2)-F(x_2,y_1)+F(x_1,y_1)$$

边际分布函数：

$$F_X(x)=P\{X\le x,Y\le +\infty\}\triangleq F(x,+\infty)$$

$$F_Y(y)=P\{X\le +\infty,Y\le y\}\triangleq F(+\infty,y)$$

条件分布函数：

$$F_{X|Y}(x|y)=P(X\le x|Y=y)$$

$$F_{Y|X}(y|x)=P(Y\le y|X=x)$$

因为分母中含 $P\{Y=y\}$，只能对离散型的 Y 才能直接计算。  
对于连续型变量 Y，分母定义为长度为 $\varepsilon$ 的邻域的概率。

## 连续型的联合密度函数

若存在二元非负函数 $f(x,y)$ ，使得对任意实数 $x,y$ 有 $F(x,y)=\int_{-\infty}^x\int_{-\infty}^y f(u,v)\mathrm{d}u\mathrm{d}v$，则称 $f(x,y)$ 为二维连续型随机变量的的联合概率密度函数。

联合密度函数的性质：

- $f(x, y) \geq 0$;
- $\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x, y) \mathrm{d}x \mathrm{d}y = F(+\infty, +\infty) = 1$;
- 在 $f(x, y)$ 的连续点处有

$$
\frac{\partial^2 F(x, y)}{\partial x \partial y} = f(x, y);
$$

- $(X, Y)$ 落入 $xOy$ 平面任一区域 $D$ 的概率为

$$
P\{(X, Y) \in D\} = \iint_D f(x, y) \mathrm{d}x \mathrm{d}y.
$$

边际概率密度函数：

可理解成平行于坐标轴的箭头，看穿过非零区域的部分。

$$f_X(x)=\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y$$

$$f_Y(y)=\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}x$$

条件概率密度函数：

$$f_{Y|X}(y|x)=\frac{f(x,y)}{f_X(x)},\quad -\infty<y<+\infty$$

## 几种连续型的概率分布

### 二元均匀分布

设二维随机变量 $(X,Y)$ 在二维有界区域 $D$ 上取值，且具有联合密度函数如下，则称 $(X,Y)$ 服从 $D$ 上均匀分布。（其中 $S$ 表示面积。）

$$
f(x,y)=\begin{cases}
\frac{1}{S(D)}, &(x,y)\in D \\
0, &\text{other}
\end{cases}
$$

若 $D_1$ 是 $D$ 的一个子集，则概率为：

$$P\{(X,Y)\in D_1\}=\iint_{D_1}f(x,y)\mathrm{d}x\mathrm{d}y=\frac{S(D_1)}{S(D)}$$

$(X,Y)$ 是二维均匀分布，$X$、$Y$ 的边际密度函数不一定均为均匀分布。（可能沿 x 或 y 方向的长度不同。）

给定均匀分布的区间，求联合分布函数：$F(x_0,y_0)$ 表示的是以当前点 $(x_0, y_0)$ 为右上角、向左下方无限延伸的矩形覆盖的联合密度函数的面积分。用直线 $x=x_0$ 和 $y=y_0$ 确定矩形和均匀分布区间的交点，按交点在不同位置分类讨论。

!!! examples "示例 求联合分布函数"

    $D$ 是 x=0, y=0, y=x+1 围成的区域，在 $D$ 上均匀分布，求 $F(x,y)$。

    按如下分类：

    $$
    \begin{cases}
    x\le-1, y\le 0; \\
    -1\le x \le 0,0<y<x+1; \\
    -1\le x<0, 0<y<1; \\
    x>0, 0<y<1; \\
    x>0, y>1
    \end{cases}
    $$

### 二元正态分布

设二维随机变量 $(X,Y)$ 具有联合密度函数如下，则称 $(X,Y)$ 服从 $D$ 上二维正态分布，记为 $(X,Y)\sim N(\mu_1, \mu_2; \sigma_1^2, \sigma_2^2; \rho)$。

$$
f(x, y) = \frac{1}{2\pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}}
\exp\left\{ -\frac{1}{2(1 - \rho^2)} \left[ \frac{(x - \mu_1)^2}{\sigma_1^2} -2\rho \frac{(x - \mu_1)(y - \mu_2)}{\sigma_1 \sigma_2} +\frac{(y - \mu_2)^2}{\sigma_2^2} \right] \right\}
$$

二元正态分布的边际分布函数、条件分布函数也是正态分布（正态分布的封闭性）。

## 连续型的独立性

若满足以下条件，称 $X$、$Y$ 相互独立：

$$
\begin{align*}\forall (x,y),\quad &P\{X\le x, Y\le y\}=P\{X\le x\}\cdot P\{Y\le y\},\,\\[0.5em]
&\text{i.e.}\,F(x,y)=F_X(x)F_Y(y)\end{align*}$$

或用密度函数表示（“几乎处处成立”表示除面积为零的区域外处处成立）：

$$f(x,y)=f_X(x)\cdot f_Y(y)\quad \text{(holds a.e.)}$$


若 $(X,Y)$ 为二维正态变量， $X$、$Y$ 相互独立的充要条件为 $\rho=0$。

二维连续型随机变量 $X, Y$ 相互独立的充要条件是 $X, Y$ 的联合密度函数 $f(x, y)$ 几乎处处可写成 $x$ 的函数 $m(x)$ 与 $y$ 的函数 $n(y)$ 的乘积，即 $f(x, y) = m(x) \cdot n(y)$。

## 多元随机变量函数的分布

### Z=X+Y

离散型：

$$P\{Z=z_k\}=\sum_{i=1}^{+\infty}P\{X=x_i, Y=z_k-x_i\}$$

连续型：

$$F_Z(z)=\iint_{x+y\le z}f(x, y)\mathrm{d}x\mathrm{d}y=\int_{-\infty}^{+\infty}\mathrm{d}x\int_{-\infty}^{z-x}f(x, y)\mathrm{d}y$$

作积分变量变换 $u = x, \, v = x + y$ 可得

$$
F_Z(z) = \int_{-\infty}^{z} \mathrm{d}v \int_{-\infty}^{+\infty} f(u, v - u) \mathrm{d}u,
$$

从而

$$
f_Z(z) = F'_Z(z) = \int_{-\infty}^{+\infty} f(u, z - u) \mathrm{d}u = \int_{-\infty}^{+\infty} f(x, z - x) \mathrm{d}x. \tag{3.5.5}
$$

### Z=max{X,Y}

### Z=min{X,Y}