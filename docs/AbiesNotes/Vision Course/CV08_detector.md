研究局部特征。  
Feature matching problem：在一张图中提取特征，另一张图中匹配。图片的角度、光照等不同。

## Harris 角点检测

移动 local window，看窗口中的点是否变化。角点处任意方向的移动都能使点改变。

用(u,v)表示 local window 的位移。位移前后窗口中的像素求 SSD（对应元素相减，求加权平方和）

当(u,v)很小时，对 I 泰勒展开：

$$
\begin{aligned}
E(u,v) &\approx \sum_{x,y} w(x,y) [I(x,y) + u I_x + v I_y - I(x,y)]^2 \\
&= \sum_{x,y} w(x,y) [u I_x + v I_y]^2 \\
&= \begin{pmatrix} u & v \end{pmatrix}
\begin{pmatrix} A & B \\ B & C \end{pmatrix}
\begin{pmatrix} u \\ v \end{pmatrix}
\end{aligned}
$$

其中：

$$
A = \sum_{x,y} w(x,y) I_x^2, \quad
B = \sum_{x,y} w(x,y) I_x I_y, \quad
C = \sum_{x,y} w(x,y) I_y^2
$$

能量函数是二次曲面，转换为判断矩阵 M。

令能量函数的值为常数，即用平面截二次曲面，得到椭圆。椭圆的长短轴的大小对应 M 的两个特征值$\lambda$（和倒数成正比），方向对应两个特征向量的方向，也是能量增长最快和最慢的方向。

由上述方法，通过求特征值和特征向量，找到能量增长最快和最慢的方向。若要找角点，希望对于任何(u,v)，即使是增长最慢的方向也有较大的增长速度，即特征值较大。

单独求特征值计算大，设计 Harris operator：

$$
f = \frac{\lambda_{\max} \lambda_{\min}}{\lambda_{\max} + \lambda_{\min}} = \frac{\det(M)}{\text{trace}(M)}
$$

找到的仍然不是单独的点，而是一片区域。需要通过 non-maximum suppression 确定中心点。

**流程：**

计算 f，用阈值二值化，non-maximum suppression

## 不变性

- 旋转不变性：旋转后椭圆长短轴的长度不变
- 光照强度改变：矩阵 M 由导数构成，不变
- 伸缩不变性：矩阵 M 改变，影响小
- 尺度（分辨率）变化？没有尺度不变性，通过改变 window 大小解决。

**评价 detectors：**

检测可重复性。同一物体不同的图，能检测到相同的特征点。
