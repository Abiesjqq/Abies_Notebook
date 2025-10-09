# Lec 04 Radiometric Calibration & HDR

## 辐射校准

### 像素值含义

- Radiance：单位面积、单位时间发射/接收的能量
- Irradiance：单位面积、单位时间、单位空间角的能量

**从 Radiance 到像素值：**

1. Radiance 经过镜头，在 sensors 上形成 Irradiance。
2. 曝光量 Exposure = Irradiance \* Time，得到光的能量大小
3. 胶片感光和输入能量有非线性的关系，而数码相机电流大小和输入光能量有线性关系。
4. 模拟得到数字的转换
5. Re-mapping：ISP（Image Signal Processor）将传感器 raw data 转化为 pixel，不同厂家做法不同

Re-mapping 的例子：

- 自动白平衡：人眼消除光源对白平衡的影响，相机模拟人眼。估算参数，RGB 列向量乘对角矩阵。
- Vignetting（暗角）：没有矫正时拍白墙，是中间白周围黑（角度不同，单位面积的能量不同）。相机自动修正 vignetting。
- 去噪：找到有重复性的部分，将所有重复部分平均

像素值数值不是 Radiance，而是非线性映射。数码相机更复杂。

## HDR

### 原理

HDR（High Dynamic Range，高动态范围成像）是一种提升图像亮度范围和细节表现的技术。它让图像同时保留明亮区域和阴暗区域的细节，避免过曝或死黑。

**传统拍摄 HDR：**

- 用闪光灯，使亮部和暗部的明亮度接近
- 用滤镜，过滤亮部的光线

**数码 HDR：**

假设：场景静态、相机静止、光线静止

1. 用不同的快门时间或光圈，同时拍多张图，把场景中不同部分的物体拍清楚。
2. 恢复相机响应曲线，即每个像素值实际对应多少辐射亮度，重建 HDR 图像
3. 将曝光值重新映射到 [0,255] 的整数范围内，和显示器适配

**怎么改变曝光度？**

快门时间、光圈大小、滤镜……

快门时间为$\frac{1}{2^n}$，即 1/8，1/16，1/32，1/64，1/128……  
但显示为邻近的整数，如 1/8，1/15，1/30，1/60，1/125……

### 算法

要求函数 f：

$$
\begin{align*}
\text{Pixel Value Z}=&f(\text{Exposure}) \\
\text{Exposure}=&\text{Irradiance}*\Delta t \\
\Rightarrow \log \text{Exposure}=&\log\text{Irradiance}+\log\Delta t
\end{align*}
$$

定义函数 g 为 log(f 的反函数)：

$$
\log \text{Exposure}=\log f^{-1}(\text{Z})=\log\text{Irradiance}+\log\Delta t\triangleq
g(Z)
$$

作图，横轴为 log Exposure，纵轴为 Pixel Value Z  
则横轴的步长为$\log\Delta t$（因为光源静止，Irradiance 不变），纵轴为 Pixel Value Z 变化量  
绘制图像的起点不确定（因为 Irradiance 的具体数值不确定）。左右移动各个照片的函数图像，拼接成光滑的曲线。

对于第 j 张图的第 i 个像素，一共 K 张图、N 个像素：

$$\ln E_i+\ln\Delta t_j-g(Z_{ij})=0$$

- 未知数：N+256（Ei 共 N 个；像素值是 [0,255] 的整数，g(Z)由 g(1),g(2)...决定，共 256 个）
- 方程数：NK

希望让以下式子尽可能小：

$$
\sum_{i=1}^{N}\sum_{j=1}^{P} \left[ \ln E_i + \ln \Delta t_j -g(Z_{ij}) \right]^2+\lambda \sum_{z=z_{\min}}^{z_{\max}} \left[ g(z) - \frac{g(z+1) + g(z-1)}{2} \right]^2
$$

- 第一项：fitting term（拟合项）
- 第二项：smoothness term（平滑项）

1. 偏导数为零

\[
\min \sum\_{i=1}^{n} (a_i x - b_i)^2 \; \rightarrow \;\text{linear equations of }
\begin{bmatrix}
a_1 \\ a_2 \\ \vdots \\ a_n
\end{bmatrix}
\mathbf{x} = \begin{bmatrix}
b_1 \\ b_2 \\ \vdots \\ b_n
\end{bmatrix}
\]

2. 解线性方程

\[\mathbf{A} \mathbf{x} = \mathbf{b}\;\rightarrow\; \mathbf{A}^T \mathbf{A}\mathbf{x}=\mathbf{A}^T \mathbf{b}\]

## 校准的研究

**Empirical Model of Response Functions**

标定不同相机的校准曲线，PCA 分析（主成分分析），减少定义曲线的参数

**Radiometric Calibration from a Single Image**

图像中的边界区域不同颜色混合，调整参数使边界颜色混合的曲线为线性
