**Why ray tracing?**

Rasterization couldn't handle global effects well.  
e.g. soft shadows, and especially when the light bounces more than once (glossy relection, indirect illumination).

Rasterization is fast, but quality is relatively low.  
Ray tracing is accurate, but is very slow.  
Rasterization: real-time; ray tracing: offline

Three ideas about light rays:

- Light travels in straight lines
- Light rays do not "collide" with each other if thay cross
- Light rays travel from the light sources to the eye (but the physics is invariant under path reversal - reviprocity)

基本方法：

对每一个像素，从相机出发连线穿过像素（eye ray），打到场景中最近的交点（closest scene），再将这个点和光源连线（shadow ray）。如果能连线，则这个点能被光源可见。

## Whitted-Style Ray Tracing

Whitted 风格：在任意点光线可继续传播（反射，折射...）

着色时，在每一个弹跳的点判断能否被光源照亮，考虑能量损失。最终像素的着色是所有弹跳点的着色之和。

从相机和像素连接的光线是primary ray，弹跳后形成的光线是secondary ray，和光源连接的光线是shadow ray。

![Whitted](../resources/Whitted.png){style="width:500px"}

### Ray-Surface Intersection

**Ray Equation:**

Ray is defined by its origin and a direction vector.

$$\mathbf{r}(t)=\mathbf{o}+t\mathbf{d}\qquad 0\le t<\infty$$

(ray(time) = origin + time * direction)

Ray intersection with sphere:

联立光线方程和球的方程，解二次方程。   
根据解的个数分为相离、相交和相切。相交时取更近的点。

#### Ray intersection with implicit surface:

$$
\begin{cases}
    \mathbf{r}(t)=\mathbf{o}+t\mathbf{d},\,\,0\le t<\infty \\
    \mathbf{p}: f(\mathbf{p})=0
\end{cases}
$$

Substitute ray equation:

$$f(\mathbf{o}+t\mathbf{d})=0$$

Solve for real, positive roots.

**How to compute?**

Simple idea: just intersect ray with each triangle.  
Ignore multiple intersections, each ray can have 0 or 1 intersections.

#### Ray Intersection with Triangle

1. ray-plane intersection  
2. test if hit point is inside triangle

Plane equation: 

plane is defined by normal vector (N) and a  point (P') on plane.

$$\mathbf{p}:(\mathbf{p}-\mathbf{p}')\cdot N=0$$

Solve for intersection:

$$
(\mathbf{p}-\mathbf{p}')\cdot N=(\mathbf{o}+t\mathbf{d}-\mathbf{p}')\cdot N=0 \\[0.5em]\\
t=\frac{(-\mathbf{p}'-\mathbf{o})\cdot N}{\mathbf{d}\cdot N}
$$

Then test if $\mathbf{o}+t\mathbf{d}$ is inside triangle.

**Faster: Moller Trunbore Algorithm**

Give barycentric coordinate directly.

$$\mathbf{O}+t\mathbf{D}=(1-b_1-b_2)\mathbf{P}_0-b_1\mathbf{P}_1+b_2\mathbf{P}_2$$

where $t$, $b_1$ and $b_2$ are variables.

$$
\begin{bmatrix}
t \\ b_1 \\ b_2
\end{bmatrix}=
\frac{1}{\mathbf{S}_1\cdot\mathbf{E}_1}
\begin{bmatrix}
\mathbf{S}_2\cdot\mathbf{E}_2 \\
\mathbf{S}_1\cdot\mathbf{S} \\
\mathbf{S}_2\cdot\mathbf{D}
\end{bmatrix}
$$

where

$$
\begin{align*}
\mathbf{E}_1&=\mathbf{P}_1-\mathbf{P}_0 \\
\mathbf{E}_2&=\mathbf{P}_2-\mathbf{P}_0 \\
\mathbf{S}&=\mathbf{O}-\mathbf{P}_0 \\
\mathbf{S}_1&=\mathbf{D}\times\mathbf{E}_2 \\
\mathbf{S}_2&=\mathbf{S}\times\mathbf{E}_1
\end{align*}
$$

#### Ray Intersection with Axis-Aligned Box
**Bounding Volumes** :  
Quick way to avoid intersections: bound complex object with a simple volume.

Box: the intersection of 3 pairs of slabs.  
esp. we often use an Axis-Aligned Bounding Box (AABB), any side of the BB is along either x, y, or z axis.

Key ideas:

- The ray enters the box only when it enters all pairs of s;abs.  
- The ray exits the box as long as it exits any pair of slabs.

For the 3D box, $t_{enter}=max\{t_{min}\}, t_{exit}=min\{t_{max}\}$

If $t_{exit}<0$, the box is "behind" the ray, no intersections.

Else if $t_{exit}\ge 0$ and $t_{enter}<0$, the ray's origin is inside the box, have intersections.

If $t_{enter}<t_{exit}$, the ray stays a while in the box, so they must intersect.

In Summary, ray and AABB intersect iff $t_{enter}<t_{exit}$ and $t_{exit} \ge 0$.

