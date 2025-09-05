## Application of Texture

### Environmental Lighting

Environment map used to render realistic lighting.

**Spherical Environment Map:** Store the environment map in the surface of a sphere.  
缺点：靠近顶部和底部的图像扭曲

**Cube Map:** A vector maps to cube point along that direction. The cube is textured with 6 square texture maps.
优点：扭曲少  
缺点：给定方向，要先判断这个方向的光照信息记录在哪个面上

### Bump Mapping

Adding surface detail without adding more triangles.  
用纹理贴图定义物体表面上每个点的相对高度/法线, Perturb surface normal per pixel.

怎么扰动法线？（以 flatland 为例）  
二维：定义扰动后的函数，用差分求切线，与切线垂直的方向为法线。  
三维： u、v 方向的差分分别为 dp/du、dp/dv，则法线为(-dp/du, -dp/dv, 1)。

**Displacement mapping:**  
凹凸贴图只通过贴图信息改变法线，没有改变点的实际位置，在边缘处和阴影处不会随凹凸位移变化。  
而位移贴图改变点的实际位置，更真实。

位移贴图的代价：要求三角形本身划分得足够细，三角形顶点间的间隔大于纹理点的间隔

动态区间细分：检测是否需要将三角形细分

### 3D Texture

3D procedual noise + solid modeling

Can be used in volumn rendering.

## Examples of Geometry

- Implicit: algebaraic surface, level sets, distance functions...
- Explicit: point cloud, polygon mesh, subdivision...

**Implicit:**不给出点的具体坐标，而是描述哪些点在一个面上  
e.g. $x^2+y^2+z^2=1$. More generally, f(z,y,z)=0  
优点：判定给定点是否在面上简单  
缺点：确定图形困难

**Explicit:**直接给出点的坐标，或通过参数映射得到
e.g. $f:\mathbb{R}\to\mathbb{R}; (u,v)\mapsto(x,y,z)$  
优点：确定图形简单  
缺点：判定给定点是否在面上困难

### More Implicit Representation

1. Algebriac Surface: 用数学公式表示面。
2. Constructed Solid Geometry (CSG): 通过基本几何形体的布尔运算，得到复杂几何形体。
3. Distance Function: 定义空间中任何一点到表面的最小距离（距离函数，可正可负），距离函数为 0 的位置为表面。可用于图形的融合。
4. Level Set Methods: 将距离函数按格存储，用线性插值得到距离为 0 的点。
5. Fractals: 分形。

**Pros:**

- compact description
- certain queries easy
- good for ray-to-surface intersection
- for simple shapes, exact description / no sampling error
- easy to handle changes in topology
