# Lec 05 Reflectance & Lighting

## 反射

!!! warning-box "提醒"

    和 GAMES101 部分重合，这里略写。

### BRDF

BRDF（Bi-direction Reflectance Distribution Function）：$\rho(\omega_o,\omega_i)$

一般在局部坐标系中计算反射，物体表面法向量和 Z 轴重合

$$L_o(\omega_o)=\sum_i \rho_{bd}(\omega_o,\omega_i)L_i(\omega_i)\cos\theta_i$$

其中$\cos\theta_i$表示光照倾斜时散开的效果

**采集 BRDF：**

用平面或球面作为 sample，采集后存储为四维数组，或按模型拟合

**散射（Diffuse）：**

常用假设：同一个点在不同视角的照片中相同，即假设为 diffuse。

### 朗伯模型（Lambert's Model）

表现散射，BRDF 是常数。常用模型。

### 冯氏模型（Phong's Model）

表现高光，光线集中在镜面反射方向，其他方向按 cos 指数级减弱。

### 其他模型

**微表面理论（Microfacet Theory）**：需要统计所有微表面的朝向

- Cook-Torrance 模型：假设每个微表面为完全镜面
- Oren-Nayar 模型：假设每个微表面为完全的朗伯模型

## 辐射学图像分析

### 基于朗伯模型的光度立体重建

#### 方法 I

**1. 求解法向量**

光源不同角度，拍摄多张照片,I 表示 Intensity。

已知：

\[
\begin{cases}
I_1 = \rho \, \mathbf{n} \cdot \mathbf{l}\_1 \\
I_2 = \rho \, \mathbf{n} \cdot \mathbf{l}\_2 \\
I_3 = \rho \, \mathbf{n} \cdot \mathbf{l}\_3
\end{cases}
\]

写成矩阵形式：

\[
\begin{pmatrix}
I_1 \\ I_2 \\ I_3
\end{pmatrix}=
\begin{pmatrix}
\mathbf{l}\_1^T \\ \mathbf{l}\_2^T \\ \mathbf{l}\_3^T
\end{pmatrix}
\rho \mathbf{n}
\]

记：

\[
\mathbf{I} =
\begin{pmatrix}
I_1 \\ I_2 \\ I_3
\end{pmatrix}, \quad
L =\begin{pmatrix}
\mathbf{l}\_1^T \\ \mathbf{l}\_2^T \\ \mathbf{l}\_3^T
\end{pmatrix}, \quad
\mathbf{b} = \rho \mathbf{n}
\]

则：

\[
\mathbf{I} = L \mathbf{b}
\]

由于 \( L,\mathbf{I}\) 已知，可得：

\[
\mathbf{b} = L^{-1} \mathbf{I}
\]

求得：

\[
\rho = \|\mathbf{b}\|\; , \;\mathbf{n} = \frac{1}{\rho} \mathbf{b}
\]

**2. 由法向量重建表面**

假设曲面为$(x, y, Z(x,y))$，则其法向量为：

\[
\mathbf{n}(x,y) = \frac{1}{\sqrt{Z_x^2 + Z_y^2 + 1}}
\begin{pmatrix}
-Z_x \\
-Z_y \\
1
\end{pmatrix}
\]

若记：

\[
\mathbf{n}(x,y) =
\begin{pmatrix}
n_1(x,y) \\
n_2(x,y) \\
n_3(x,y)
\end{pmatrix}
\]

则可得偏导关系：

\[
Z_x(x,y) = \frac{n_1(x,y)}{n_3(x,y)}, \quad
Z_y(x,y) = \frac{n_2(x,y)}{n_3(x,y)}
\]

我们可以通过沿路径积分来恢复任意点的表面高度，例如：

\[
Z(x, y) = \int_0^x Z_x(s, y) \, ds + \int_0^y Z_y(x, t) \, dt + c
\]

由于噪声，这种方法无法得到正确的结果！

我们必须有：

$$
\frac{\partial Z_x(x, y)}{\partial y} = \frac{\partial Z_y(x, y)}{\partial x}
$$

#### 方法 II

切向量 $ \boldsymbol{v}\_1 $ 与法向量 $ \boldsymbol{n} $ 垂直：

$$
\begin{aligned}
\boldsymbol{v}_1 &= \big(x+1, y, Z(x+1, y)\big) - \big(x, y, Z(x, y)\big) \\
&= \big(1, 0, Z(x+1, y) - Z(x, y)\big)
\end{aligned}
$$

$$
\begin{aligned}
0 &= n \cdot v_1 \\
&= (n_1, n_2, n_3) \cdot \big(1, 0, Z(x+1, y) - Z(x, y)\big) \\
&= n_1 + n_3 \big(Z(x+1, y) - Z(x, y)\big)
\end{aligned}
$$

$ v\_2 $ 得到一个类似的方程，每个法向量对 $ Z $ 给出两个线性约束，通过求解矩阵方程计算 $ Z $ 的值

稀疏矩阵，用 Conjugated Gradient algorithm 求解。

仍然存在低频失真（low-frequency distortion）的问题，整体形状可能倾斜、扭曲等。

### 捕捉光线

**方向光：**

镜面球体，用反射光角度推入射光

**环境光：**

环境光定义为照射到物体表面的球面函数。

类似光线追踪方法

## 相关研究

**Eyes for Relighting**

人像照片中，分析眼球用于捕捉环境光源  
还可用于估计人眼看到的场景

**Faces as Lighting Probes via Unsupervised Deep Highlight Extraction**

用人脸代替镜面球面，估计光线方向

用神经网络分离人脸的高光，捕捉到的图是 BRDF 和环境光卷积的效果。作用反卷积，得到估计结果

**Retrospective sensing for the measurement of surface texture and shape**

软胶上覆盖金属粉，用灯照亮软胶的另一面，物体压在软胶上时捕捉表面

可用于机器人皮肤的传感器
