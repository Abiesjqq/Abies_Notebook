# Lec 06 Filters

## 滤波器

用领域中所有像素的加权平均替换中心像素的颜色值。  
一般使用空域不变（spatially-invariant）的核

- Box filter: 简单平均
- Gaussian filter：中心的权值大

图像边界的平均：像素值拓展，外围加零（zero packing）或特定颜色值

字体的软阴影效果：原图像做高斯模糊，模糊后的图像向旁边平移，与原图像叠加

## 边缘检测

边缘处图像信号不连续。  
用差分代替导数（-1 0 1 的 1\*3 filter），导数值大于阈值则认为是边缘

**问题**：图像有噪声，噪声处导数大  
解决：先 Gaussian，再 derivative。两者合并为 DoG

**Sobel Filter：**

Blurring \* 1D derivative filter

水平 Sobel filter：

$$\begin{bmatrix}1&0&-1\\2&0&-2\\1&0&-1\end{bmatrix}$$

竖直 Sobel filter：

$$\begin{bmatrix}1&2&-1\\0&0&0\\-1&-2&-1\end{bmatrix}$$

**计算图像梯度：**

选择 derivative filter，与图像做卷积，计算 gradient, direction, amplitude，只要有一个方向变化大就认为是边缘

得到的边缘可能宽度大。每次检测上下的像素对边缘的响应是否比当前像素更大，保留响应最大的点。

## 双边滤波（Bilateral Filter）

高斯滤波时去除噪声，但边界变模糊。

双边滤波：空间上接近且颜色值接近，则权值大。包含 spatial Gauss 和 range domain Gauss  
不同像素的核不同，是 spatially-varient  
实现去噪的同时保留明显的边界

$$J(x)=\frac{1}{k(x)}\sum_{\xi}f(x,\xi)g(I(\xi)-I(x))I(\xi)$$

其中 k(x)为归一化参数，保证权值之和为 1

**增强细节**：滤波前后图像做差为细节的像素值，将细节像素值乘 2 加到原图像

## 滤波的研究

**HDR 图像的显示**

HDR 范围可能过大，需要重新映射到 0-255 的 LDR。

1. **gamma 映射**：将 x 映射为 $x^{\gamma}$。亮度高的部分压缩到小范围，亮度低的部分展开
2. **intensity 的 gamma 映射**：将 intensity 和 color 分开，如转换为 YUV 格式，在 Y 通道（亮度）压缩、UV 通道（颜色）保持。细节处小的起伏被去掉，细节丢失。
3. **用 Gaussian 滤波分离细节**：分离不完全，物体边缘空缺。
4. **用双边滤波代替高斯滤波**

**Digital Photography with Flash and No-flash Image Pairs**

相机不动，打闪光灯和不用闪光灯拍两张。闪光灯图噪声更低，但有色差。  
Joint bilateral filter：对不用闪光灯的图作双边滤波，其中 range domain Gaussian 用闪光灯的图。

闪光灯可能导致额外的高光：检测高光，做成 mask。

**Guided Image Filtering**

公式略。

实现双边滤波的效果，但时间复杂度低。
