## Z-Buffer

Painter's Algorithm: paint from back to front, overwrite in the framebuffer.

对三角形排序，在相互遮挡的情况下无法排序。因此对像素排序（每个像素记录最近的距离）。

Z-Buffer: store current min. z-value for each sample (pixel).  
Needs an additional buffer for depth values. Frame buffer stores color values, depth buffer (z-buffer) stores depth.  
NOTE: For simplicity we suppose z is always positive.

## Shading

### Definition

Shading: The darkening or coloring of an illustration or diagram with parallel lines or a block of color.  
In this course: The process of applying a material to an object.

### Blinn-Phong Reflectance Model

Shading: specular highlight + diffuse reflection + ambient lighting

Input:

1. viewer direction: v
2. surface normal: n
3. light direction: l
4. surface parameters

**Diffuse Reflection**

How much light (energy) is received?  
Lambert’s cosine law: $\cos\theta=\mathbb{i}\cdot\mathbb{n}$

**Light Falloff**

点光源，能量集中在靠近中心的球壳，但是远近球壳能量守恒。  
distance: r, intensity: I  
平方反比，计算有多少光到达 shading point

**Lambertian (Diffuse) Shading. **

$$L_d=k_d(I/r^2)max(0, \mathbb{n}\cdot\mathbb{l})$$

$L_d$: diffusely reflected light  
$I/r^2$: energy arrived at the shading point  
$k_d$: diffuse coefficient
$max(0, \mathbb{n}\cdot\mathbb{l})$: energy received by the shading point
kd 定义不同材质对光的吸收，kd 越大物体越亮

公式中不含 v：漫反射的反射光线均匀分布在各个方向上，和观察方向无关。
如果区分 rgb，则给不同区域赋予不同颜色。
