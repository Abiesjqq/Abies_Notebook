## Explicit Representations

**1. Point Cloud**  
list of points (x,y,z)  
直接扫描得到点云，需要通过算法转化为三角形面  
如果点云密度过低，则不能画出图像

**2. Polygon Mesh**  
三角形面表示
Wavefront Object File (.obj) Format: v 表示点的坐标，vn 表示法线，vt 表示纹理坐标，f 表示面的顶点的编号

## Curves

### Bezier Curves

贝塞尔曲线：用一系列控制点定义曲线

e.g.满足条件：

1. 从 P0 开始，且切线方向为 P0P1
2. 从 P3 结束，且切线方向为 P2P3

![Bezier](../resources/Bezier.png){style="width:250px"}

#### de Casteljiau Algorithm

Consider three points (quadratic Bezier):

将起点到终点视为 0~1，对其中任一个比例为 t 的点，按下图方法确定：

![Bezier 3](../resources/Bezier%203.png){style="width:600px"}

四点：

![Bezier 4](../resources/Bezier%204.png){style="width:250px"}

**Bernstein form of a Bezier curve of order n:**

$$b^n(t)=\sum_{j=0}^nb_jB_j^n(t)$$

Bernstein polynomials:

$$B_i^n(t)=\begin{pmatrix}n \\ i\end{pmatrix}t^i (1-t)^{n-i}$$

e.g.

2D:

$$b^2(t)=b_0(1-t)^2+b_1 2t(1-t)+b_2 t^2$$

3D:

$$b^3(t)=b_0 (1-t)^3+b_1 3t(1-t)^2+b_2 3t^2(1-t)+b_3 t^3$$

#### Properties of Bezier Curves

1. Affine transformation property: transform curve by transforming control points.  
   在仿射变换下，变换控制点再用变换后的点画曲线，和直接对曲线上点变换，两者结果相同。  
   但仅对仿射变换成立，投影等变换不成立。

2. Convec hull property: curve is within convex hull of control points.  
   绘制的贝塞尔曲线一定在所有控制点形成的凸包内。  
   e.g. 若控制点共线，则贝塞尔曲线是这条线本身

#### Piecewise Bezier Curves

用多个控制点同时控制一条曲线，中间部分不能反映趋势。用多组点逐段控制，一般每四个点控制一段，再将所有曲线连接。

若控制杆和中间点共线，且控=控制杆大小相同，则认为连接点处曲线连续。

**Continuity:**

$C^0$ continuity: $a_n=b_n$，几何上不间断

$C^1$ continuity: $a_n=b_0=\frac{1}{2}(a_{n-1}+b_1)$，前后控制杆长度相同，切线连续

### Other Types of Splines

Spline（样条）：由一系列控制点控制的曲线，满足特定的连续性

B-Spline（基样条）: 对贝塞尔曲线的增强，增加了局部性，改动一个点影响曲线的一个范围内而不是影响整个曲线

## Surfaces

### Bezier Surfaces

1. 沿 x 方向的控制点，绘制沿 x 方向的贝塞尔曲线；
2. 在上述曲线沿 y 方向取点作为控制点，绘制沿 y 方向的贝塞尔曲线；
3. y 方向曲线扫过的面为贝塞尔曲面

### Mesh Operations

- Mesh subdivision  
- Mesh simplification  
- Mesh regularization  



