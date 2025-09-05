Shading:

- Barycentric Coordinates
- Texture queries
- Application of textures

**Barycentric Coordinates**: 三角形中任何一点都可表示为三个顶点坐标的线性组合

A coordinate system for triangle $(\alpha, \beta,\gamma)$:

$$(x,y)=\alpha A+\beta B+\gamma C$$

其中$\alpha+\beta+\gamma=1$，且都是非负的
满足这三个条件则点在三角形内，是重心坐标

**怎么求重心坐标？**
奔驰定理：用面积求重心坐标  
$A_A$表示 A 相对的小三角形的面积

$$\alpha=\frac{A_A}{A_A+A_B+A_C}$$

或：基于点坐标的公式。推导可参考渲染器 Tinyrenderer 内容。

![Barycentric Coordinates](../resources/Barycentric%20Coordinates.png){style="width:500px"}

Linearly interpolate values at vertices:

$$V=\alpha V_A+\beta V_B+\gamma V_C$$

问题：投影不能保证重心坐标不变  
解决：取三维坐标计算，运算后再投影到二维平面

## Applying texture

for each rasterized screen sample (x,y):

1. (u,v) = evaluate texture coordinate at (x,y)
2. texcolor = texture.sample(u,v)
3. set sample’s color to texcolor

**纹理分辨率低于图片分辨率?**
需要纹理放大  
（A pixel on a texture: texel）

1. 非整数的坐标 round 成整数
2. 双线性插值：找相邻的四个像素，和左下角的水平竖直方向距离为 s 和 t，线性插值（先水平得到两个中间点，再对竖直中间点插值）
3. Bicubic：取周围 16 个

**纹理图片太大？**  
像素在纹理上覆盖很大一片区域  
网格平面透视：近处锯齿，远处摩尔纹

1. 超采样：在一个像素内部有多个采样点平均
2. 范围查询求平均值：取像素覆盖的一片区域的平均值

### Mipmap

mipmap: Allowing (fast, approx., square) range queries  
给定一块正方形区域，快速查询到覆盖的像素的 rgb 平均值。

**1. 生成：**

每次将长、宽的分辨率都减半，直到减为 1\*1，生成一系列 mipmap(mip hierarchy)。  
每次的存储空间是上一次的 1/4，额外引入的存储量为原图的 1/3。

**2. 查询：**

对任意像素，假设在原图中向上、向右移动 1 个像素时，在纹理图中移动距离是`l1`、`l2`。  
令像素在纹理图上覆盖的区域为正方形，边长为`max(l1,l2)`。  
用 mipmap 查询这个正方形覆盖的像素的 rgb 平均值。

距离近时，一个像素覆盖的区域小，在低层的 mipmap（接近原图）上查询；  
距离远时，一个像素覆盖的区域大，在高层的 mipmap（分辨率低）上查询。

**变化不连续？**

**Trilinear Interpolation:**  
先在相邻的两个 mipmap 上关于行、列进行 bilinear interpolation，再在两个层之间线性插值。

**缺点：**Overblur，远处抹去细节  
部分因为 mipmap 只支持正方形查询，非正方形误差大  
解决：Anisotropic Filtering

### Anisotropic Filtering

每次变换仅长或宽减小一半，保留生成的所有图（不一定是正方形）。  
额外开销是原图的 3 倍。

![Anisotropic](../resources/Anisotropic.png){style="width:400px"}

**为什么？**  
原图中一个像素映射到纹理上不一定是正方形，即原图中水平、竖直方向移动 1 个像素，纹理图中移动距离可能不同。

Can look up axis-aligned rectangular zones.

But diagonal footprint still a problem.

### EWA Filtering

Use multiple lookups, weighted average.

对于不规则形状，将图形分割成不同个圆形，多次查询圆形。
