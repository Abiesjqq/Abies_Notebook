# CV Lec 10 Homography

透视变换主要用于图像拼接。

## 齐次坐标

!!! warning-box "注意"

    齐次坐标部分和 GAMES101 重复，这里略写。

齐次坐标，仿射变换下最下面一行一定是 001（二维）。

仿射变换一定由放缩、旋转、剪切、平移组成。  
仿射后原点可能移动，但直线仍然是直线，平行关系、长度比值保持。

如果允许最后一行非 001，则是 homography，视觉上为图像在平面外旋转。

- homography 前后直线仍然是直线，但平行、长度比值、原点位置不保留
- homography 对矩阵乘法封闭，构成群

图像中所有平面，都可以通过 homography 转化为正视的平面。

## 图像拼接

### 原理

在图像拼接中，我们希望找到一个**单应矩阵（Homography Matrix）**
\( \mathbf{H} \in \mathbb{R}^{3\times3} \)，使得一张图片中的特征点经过透视变换后，与另一张图片中的对应特征点对齐。

拍照时相机位置不能动。否则同一个点在不同图像中不同，拼接后有重影。  
实际拍摄全景照片时，相机位置的距离相对于物体尺度能忽略。

### Mosaic 算法

- **基本关系**

两幅图像中对应点满足透视关系：

$$
x' = Hx
\quad \leftrightarrow \quad
\begin{bmatrix}
x' \ y' \ 1
\end{bmatrix}
\begin{bmatrix}
a & b & c \
d & e & f \
g & h & i
\end{bmatrix}
\begin{bmatrix}
x \ y \ 1
\end{bmatrix}
$$

由于齐次坐标中比例无关，我们实际上有：

\[
\begin{bmatrix} x' \ y' \ 1 \end{bmatrix} \propto H \begin{bmatrix} x \ y \ 1 \end{bmatrix}
\]

即两边仅相差一个**比例常数**。

- **方程构建思路**

设原图像与目标图像中的对应点分别为：

\[
\mathbf{x}\_i = (x_i, y_i)^T, \quad \mathbf{x}'\_i = (x'\_i, y'\_i)^T
\]

则有：

\[
\mathbf{x}'\_i \propto \mathbf{H} \mathbf{x}\_i
\]

这等价于：

\[
\mathbf{x}'\_i \times (\mathbf{H}\mathbf{x}\_i) = 0
\]

其中“×”表示向量叉积。
这一式保证了两向量共线（即仅相差比例常数）。

- **展开矩阵形式**

令单应矩阵：

\[
\mathbf{H} =
\begin{pmatrix}
\mathbf{h}^{1T} \
\mathbf{h}^{2T} \
\mathbf{h}^{3T}
\end{pmatrix}
\]

则：

\[
\mathbf{H}\mathbf{x}\_i =
\begin{pmatrix}
\mathbf{h}^{1T} \mathbf{x}\_i \
\mathbf{h}^{2T} \mathbf{x}\_i \
\mathbf{h}^{3T} \mathbf{x}\_i
\end{pmatrix}
\]

代入叉积公式：

\[
\mathbf{x}'\_i \times \mathbf{H}\mathbf{x}\_i =
\begin{pmatrix}
y'\_i \mathbf{h}^{1T} \mathbf{x}\_i - x'\_i \mathbf{h}^{2T} \mathbf{x}\_i \
\mathbf{h}^{3T} \mathbf{x}\_i - x'\_i \mathbf{h}^{1T} \mathbf{x}\_i \
x'\_i \mathbf{h}^{2T} \mathbf{x}\_i - y'\_i \mathbf{h}^{3T} \mathbf{x}\_i
\end{pmatrix}
\]

- **化为线性方程形式**

通过矩阵排列，可将每对匹配点对应的方程写成标准形式：

\[
\mathbf{x}'\_i \times \mathbf{H}\mathbf{x}\_i =
\begin{bmatrix}
0^T & -x'\_i & y'\_i x_i^T \
x'\_i & 0^T & -x'\_i x_i^T \
-y'\_i x_i^T & x'\_i x_i^T & 0^T
\end{bmatrix}
\begin{bmatrix}
\mathbf{h}^1 \
\mathbf{h}^2 \
\mathbf{h}^3
\end{bmatrix}
= 0
\]

- **方程组表达**

因此，对于每一对匹配点 \((\mathbf{x}\_i, \mathbf{x}'\_i)\)，我们可以得到一个线性约束：

\[
\mathbf{A}\_i \mathbf{h} = 0
\]

将所有匹配点的方程堆叠起来：

\[
\mathbf{A}\mathbf{h} = 0
\]

其中\(\mathbf{h} = [h_1, h_2, \dots, h_9]^T\)
表示单应矩阵的展开向量形式。

通常使用 SVD（奇异值分解）求解该齐次方程，取最小奇异值对应的特征向量作为解。

- **求解方程**

在上一步中，我们得到了齐次线性方程组：

$$
\mathbf{A}\mathbf{h} = 0
$$

其中 \(\mathbf{A}\) 是由所有匹配点构造的矩阵，\(\mathbf{h}\) 是单应矩阵 \(\mathbf{H}\) 展开的 9 维向量。

- （1）避免平凡解

显然，\(\mathbf{h} = 0\) 是一个平凡解，但它没有实际意义。
因此，我们约束 \(\mathbf{h}\) 的长度为 1：

$$
|\mathbf{h}| = 1
$$

这使得问题变为：

$$
\min_{|\mathbf{h}|=1} |\mathbf{A}\mathbf{h}|
$$

即找到一个非零的 \(\mathbf{h}\)，使得 \(\mathbf{A}\mathbf{h}\) 尽可能接近零。

- （2）考虑噪声和误差

由于特征检测存在偏差、镜头畸变或透视投影误差，
\(\mathbf{A}\mathbf{h}\) 无法严格等于零。
因此，我们在最小二乘意义下寻找最优解：

$$
\min_{|\mathbf{h}|=1} |\mathbf{A}\mathbf{h}|^2
$$

- （3）通过 SVD 求解

对矩阵 \(\mathbf{A}\) 进行奇异值分解（SVD）：

$$
\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T
$$

其中：

- \(\mathbf{U}\)：左奇异向量矩阵（正交）
- \(\mathbf{\Sigma}\)：奇异值对角矩阵，元素按从大到小排列
- \(\mathbf{V}\)：右奇异向量矩阵（正交）

- （4）取最小奇异值对应向量

在最小化 \(|\mathbf{A}\mathbf{h}|\) 的约束问题中，
最优解 \(\mathbf{h}\) 是矩阵 \(\mathbf{A}^T\mathbf{A}\) 的最小特征值对应的特征向量。
由 SVD 性质可知，这等价于取 \(\mathbf{V}\) 中对应最小奇异值的列向量作为 \(\mathbf{h}\)。

即：

$$
\mathbf{h} = \mathbf{v}_{\text{min}}
$$

- （5）恢复单应矩阵

将 \(\mathbf{h}\) 重新 reshape 为 \(3 \times 3\) 矩阵：

$$
\mathbf{H} =
\begin{bmatrix}
h_1 & h_2 & h_3 \
h_4 & h_5 & h_6 \
h_7 & h_8 & h_9
\end{bmatrix}
$$

由于 \(\mathbf{H}\) 仅确定到一个比例常数（齐次坐标不变），
通常将其归一化，例如令 \(h_9 = 1\)

## 实际问题

匹配时有 outlier，特征点匹配到不相关的点。  
outlier 会影响拟合，导致拟合结果与实际的偏离大。

### M-estimators

通常拟合为最小二乘，对惩罚计算平方。为什么是二乘？求偏导后为线性，计算方便。  
但平方的惩罚增长快，会为了适配 outlier 而牺牲正常的数据点。

M-estimators 中需要新的惩罚函数$\rho$（如绝对值函数），要求不能随偏离的增加而快速增长。

### RANSAC

用 RANSEC 选择最大的 inlier 的集合，再用这个集合做最终的拟合。

流程：

1. 随机挑选 s 个样本点拟合，重复 n 次。
2. 对每个拟合结果，判断和多少个点吻合，作为模型的评价。
3. 选取吻合点最多的模型，所有吻合的点作为 inlier，所有不吻合的点作为 outlier。要求 inlier 至少多于一半。
4. 用所有 inlier 点做拟合，得到最终结果。

优点：

- 简单且通用
- 适用于许多不同的问题
- 在实践中通常效果良好

缺点：

- 需要调整参数
- 有时需要过多的迭代次数
- 在内点比例极低时可能失效

**怎么设计迭代次数 n？**

假设 outlier 的比例为 e。希望在 n 次迭代中，至少有一次选取的 s 个样本点全部为 inlier。

一次选取中全部是 inlier 的概率$q=(1-e)^s$。  
希望$1-(1-q)^n>p$，则：

$$n=\frac{\log (1-p)}{\log (1-(1-e)^s)}$$

**怎么设计选取点数 s？**

希望选取最少的点。

s 跟要拟合的映射的自由度有关。

**怎么计算 outlier 的比例 e？**

在迭代的过程中动态估计 outlier 的比例。一开始假设为 1，迭代时不断减小。

## 几个概念

### Algebraic Distance

DLT（直接线性变换）算法的目标是最小化代数距离，即使 \(\mathbf{A}\mathbf{h}\) 尽可能接近零。
这里 \(\mathbf{e} = \mathbf{A}\mathbf{h}\) 表示残差向量，每个匹配点贡献两个独立方程。

$$
\mathbf{e} = \mathbf{A}\mathbf{h} \quad \text{残差向量}
$$

$$
\mathbf{e}_i \quad \text{为对应点的前两个残差分量}
$$

代数距离定义为：

$$
d_{a_i}(\mathbf{x}'_i, \mathbf{H}\mathbf{x}_i)^2 = |\mathbf{e}_i|^2 =
\left|
\begin{bmatrix}
0^T & -x'_i & y'_i x_i^T \
x'_i & 0^T & -x'_i x_i^T
\end{bmatrix}
\mathbf{h}
\right|^2
$$

对于两点 \(\mathbf{x}\_1, \mathbf{x}\_2\)，它们的代数距离为：

$$
d_{a_i}(\mathbf{x}_1, \mathbf{x}_2)^2 = a_1^2 + a_2^2 \quad \text{其中} \quad \mathbf{a} = (a_1, a_2, a_3)^T = \mathbf{x}_1 \times \mathbf{x}_2
$$

综合所有点对，总的代数距离为：

$$
\sum_i d_{a_i}(\mathbf{x}'_i, \mathbf{H}\mathbf{x}_i)^2 = \sum_i |\mathbf{e}_i|^2 = |\mathbf{A}\mathbf{h}|^2 = |\mathbf{e}|^2
$$

因此，DLT 实际上是在最小化所有点对的代数误差平方和，以估计最优单应矩阵 \(\mathbf{H}\)。

### Geometric Distance

把 x 映射到 x'，希望映射后的 x 和 x'在图像平面上的欧式距离尽可能小。  
如果反向将 x'映射到 x，得到双向的距离。

几何距离（Geometric Distance）用于衡量点与其投影在图像空间中的真实几何误差，与代数距离不同，它直接反映了像素级误差，因此更符合视觉意义下的“匹配精度”。

- \(\mathbf{x}\)：原始观测到的特征点坐标
- \(\hat{\mathbf{x}}\)：估计或投影得到的特征点坐标
- \(d(\cdot, \cdot)\)：图像平面上的欧式距离

**单向重投影误差（Error in one image）**
只考虑一幅图像中的投影误差：

$$
\hat{\mathbf{H}} = \underset{\mathbf{H}}{\operatorname{argmin}} \sum_i d\left(\mathbf{x}'_i, \mathbf{H} \mathbf{x}_i\right)^2
$$

表示找到一个 \(\mathbf{H}\)，使得变换后的点 \(\mathbf{H}\mathbf{x}\_i\) 与目标点 \(\mathbf{x}'\_i\) 尽可能接近。

**对称传递误差（Symmetric Transfer Error）**
考虑双向投影误差，使误差在两幅图像间对称：

$$
\hat{\mathbf{H}} = \underset{\mathbf{H}}{\operatorname{argmin}} \sum_i
d\left(\mathbf{x}_i, \mathbf{H}^{-1} \mathbf{x}'_i\right)^2 +
d\left(\mathbf{x}'_i, \mathbf{H} \mathbf{x}_i\right)^2
$$

即既要求 \(\mathbf{H}\mathbf{x}\_i\) 接近 \(\mathbf{x}'\_i\)，
也要求 \(\mathbf{H}^{-1}\mathbf{x}'\_i\) 接近 \(\mathbf{x}\_i\)。

**重投影误差（Reprojection Error）**
几何意义最准确但计算最复杂的形式，
它同时优化变换矩阵和最优的估计点位置：

$$
\left(\hat{\mathbf{H}}, \hat{\mathbf{x}}_i, \hat{\mathbf{x}}'_i\right)
= \underset{\mathbf{H}, \hat{\mathbf{x}}_i, \hat{\mathbf{x}}'_i}{\operatorname{argmin}}
\sum_i d\left(\mathbf{x}_i, \hat{\mathbf{x}}_i\right)^2 + d\left(\mathbf{x}'_i, \hat{\mathbf{x}}'_i\right)^2
\quad \text{subject to} \quad
\hat{\mathbf{x}}'_i = \hat{\mathbf{H}} \hat{\mathbf{x}}_i
$$

这相当于在两幅图像中寻找最接近观测点的真实投影点，使得它们严格满足单应约束。
实际中通常通过非线性最小二乘优化（如 Levenberg–Marquardt）进行求解。
