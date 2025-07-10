# Lecture 01 / Overview of Computer Graphics

!!! remarks "Menu of this lecture"

    - [Concepts of raterization, ray tracing etc.](#basic-concepts)

### Basic Concepts

**Rasterization**

1. Project geometry primitives (3D triangles / polygons) onto the screen.
2. Break projected primitives into fragments (pixels)
3. Real-time applications is the gold standard in Video Games

??? normal-comment "translation"

    1. 将几何形状（3D 三角形/多边形）投影到屏幕上
    2. 将投影后的图元划分为片段（像素）
    3. 在视频游戏中，实时应用是黄金标准

**Curves and Meshes**

**Ray Tracing**

Shoot rays from camera through each pixel
Offline application is the gold standard in Animation / Movies

**Animation / Simulation**

**Difference between Computer Graphics and Computer Vision?**

![Diagram](../../images/computer graphics and vision.png){style="width:600px"}

[Click here to jump to the course website](http://www.cs.ucsb.edu/~lingqi/teaching/games101.html)

# Lecture 02 / Review of Linear Algebra

!!! remarks "Menu of this lecture"

    - [Functions of dot product and cross product](#functions-of-dot-product-and-cross-product)
    - [Dot product and cross product in matrix](#dot-product-and-cross-product-in-matrix)

**Unit vector**: $\hat{a}=\vec{a}/|\vec{a}|$  
Usually use unit vectors to present directions.

Vectors are represented as column vectors by default.

### Functions of dot product and cross product

**Dot product:**

1. Find the angle between two vectors.  
   e.g cosine of angle bwtween light source and surface.
2. Find projection of one vector on another.

More specifically:

1. Measure how close two directions are.
2. Decompose a vector.
3. Determine forward / backward.

**Cross product:**

1. Construction coordinate systems.

Functions:

1. Determine left / right. Given a plane and two vectors on this plane, determine the relative position of the two vectors.
2. Determine in / out. Several vectors are connected head-to-tail to form a closed shape. Given another point, determine whether this point lies inside the closed shape.

e.g.  
![example](../../images/cross product eg.png){style="width:100px"}  
Check: $\vec{AB}\times\vec{AP}, \vec{BC}\times\vec{BP}, \vec{CA}\times\vec{CP}$. If the signs of all three are the same, then point P is inside the shape.


### Dot product and cross product in matrix:

**2D reflection about y-axis:**

$$
\begin{pmatrix}
-1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}=
\begin{pmatrix}
-x \\
y
\end{pmatrix}
$$

??? normal-comment "matrix in latex"

    ```
    \begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}
    ```

    Rendered output:

    $$
    \begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}
    $$


$$
\vec{a}\cdot\vec{b}=A^T\cdot B
=\begin{pmatrix} x_a & y_a & z_a \end{pmatrix} \begin{pmatrix} x_b \\ y_b \\ z_b \end{pmatrix}
$$

$$
\vec{a}\times\vec{b}=A^*B
=\begin{pmatrix}
 0 & -z_a & y_a \\
 z_a & 0 & -x_a \\
 -y_a & x_a & 0
 \end{pmatrix}
 \begin{pmatrix}
 x_b \\ y_b \\ z_b
 \end{pmatrix}
$$

($\begin{pmatrix} 
 0 & -z_a & y_a \\
 z_a & 0 & -x_a \\
 -y_a & x_a & 0
 \end{pmatrix}$ is the dual matrix of $\vec{a}$)

# Lecture 03 / Transformation

!!! remarks "Menu of this lecture"

    - [2D transformations: rotation, scale, shear](#viewing-transformation)
    - [Homogeneous coordinates](#homogeneous-coordinates)
    - [Composing transformation](#composing-transforms)

### Viewing transformation

Viewing transformation: 3D -> 2D projection

**Scale**

$$
\begin{pmatrix}
x' \\
y'
\end{pmatrix}
=\begin{pmatrix}
s_x & 0 \\
0 & s_y
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
$$

Multiplying a matrix on the left corresponds to performing a row operation.

**Reflection**

E.g. reflection about the y-axis:

$$
\begin{pmatrix}
x' \\
y'
\end{pmatrix}
=\begin{pmatrix}
-1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
$$

**Sheer**

Illustration of sheer tranformation:  
![Sheer tranformation](../../images/sheer illustration.png){style="width:500px"}

$$
\begin{pmatrix}
x' \\
y'
\end{pmatrix}
=\begin{pmatrix}
x+ay \\
y
\end{pmatrix}
=\begin{pmatrix}
1 & a \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
$$

**Rotation**

By default, the rotation is around the origin.  
$R_{45}$ refers to rotatiing 45 degrees counterclockwose about the origin. 

$$
R_{\theta}=\begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{pmatrix}
$$

### Homogeneous Coordinates

Translation is not linear transform, so it cannot be represented in matrix form. 
But we don't want it to be a special case, so homogeneous coordinates are used to represent all transformations. 

Add a third coordinate (w-coordinate), to represent the translation characters of points or vectors.  

**Affine transformations:**  
affine map = linear map + translation map  

$$
\begin{pmatrix}
x' \\ y'
\end{pmatrix}
=\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
+\begin{pmatrix}
t_x \\ t_y
\end{pmatrix}
$$

#### 2D version

- 2D point: $\begin{pmatrix}x , y , 1 \end{pmatrix}^T$
- 2D vector:$\begin{pmatrix}x , y , 0 \end{pmatrix}^T$

When $w\neq 0$, 2D point $\begin{pmatrix}x , y , w \end{pmatrix}^T$ means $\begin{pmatrix}x/w , y/w , 1 \end{pmatrix}^T$

(The w-coordinate of vectors are 0, which means vectors are translation invariant. By comparison, w-coordinate of points are 1)

**Use homogeneous Coordinates to represent affine translations:**

$$
\begin{pmatrix}
x' \\ y' \\ w'
\end{pmatrix}
=\begin{pmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ 1
\end{pmatrix}
=\begin{pmatrix}
x+t_x \\ y+t_y \\ 1
\end{pmatrix}
$$

**Properties:**   
1. The last row must be 0 0 1.  
2. The top-left 2×2 matrix represents a linear transformation.  
3. The rightmost column represents translation.
4. Relations between points and vectors:
   - vector + vector = vector
   - point  - point  = vector
   - point  + vector = point
   - point  + point  = point


**Scale:**

$$
S(s_x, s_y)=\begin{pmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

**Rotation:**

$$
R(\alpha)=\begin{pmatrix}
\cos\alpha & -\sin\alpha & 0 \\
\sin\alpha & \cos\alpha & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

**Translation:**

$$
T(t_x, t_y)=\begin{pmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\ 
0 & 0 & 1
\end{pmatrix}
$$

**Inverse transformations:** $M^{-1}$

Esp. matrix $R_{\theta}$ for rotation is orthogonal, so $R_{-\theta}=R^{-1}=R^T$.

#### 3D version

- 3D point: $\begin{pmatrix}x , y , z, 1 \end{pmatrix}^T$
- 3D vector:$\begin{pmatrix}x , y , z, 0 \end{pmatrix}^T$

Use 4×4 matrix for affine transformations. 

### Composing Transforms

All matrices are left-multiplied to the original coordinates, and are composed in the order of transformations from right to left.

!!! examples 

    Transformations: A1 -> A2 -> ... -> An  
    Matrix: $A_n\cdots A_2A_1\begin{pmatrix}x \\ y \\ 1\end{pmatrix}$
    

# Lecture 04 Transformations Cont.

!!! remarks "Menu of this lecture"

    - [3D transformations](#3d-transformations)
    - [Viewing transformations](#viewing-transformations)

## 3D Transformations

**Scale:**

$$
S(s_x, s_y, s_z)=
\begin{pmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**Translation:**

$$
T(t_x, t_y, t_z)=
\begin{pmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

### 3D Rotations

#### Compose from $R_x, R_y, R_z$

$$
R_x(\theta)=\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos\theta & -\sin\theta & 0 \\
0 & \sin\theta & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

$$
R_y(\theta)=\begin{pmatrix}
\cos\theta & 0 & \sin\theta & 0 \\
0 & 1 & 0 & 0 \\
-\sin\theta & 0 & \cos\theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

The rotation part of $R_y(\theta)$ is different from common rotation matrix, because $\vec{y}=\vec{z}\times\vec{x}$, which is not the common sequence xyzxyz.

$$
R_z(\theta)=\begin{pmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

When rotating around x-, y-, and z- axis with angle $\alpha, \beta, \gamma$ respectively ($\alpha, \beta, \gamma$ are called Euler angles), 
$$
R_{xyz}(\alpha, \beta, \gamma)=R_x(\alpha)R_y(\beta)R_z(\gamma)
$$

#### Rodrigues' Rotation Formation

Rotation by angle $\alpha$ around axis n,
$$
R(n, \alpha)=\cos(\alpha)I+(1-\cos(\alpha))n n^T+\sin(\alpha)\begin{pmatrix}
0 & -n_z & n_y \\
n_z & 0 & -n_x \\
-n_y & n_x & 0
\end{pmatrix}
$$

If the axis of rotation does not pass through the origin, first translate the entire system so that the axis passes through the origin, perform the rotation, and then translate the entire system back to its original position.

Quaternions can be used for interpolation between rotation angles.

## Viewing transformations

*MVP Transformations:*

1. Model transformations (arrange objects and places)
2. View transformations (arrange angles)
3. Projection transformations

### Define camera

- position: $\hat{e}$ (points from the origin to the camera)
- look-at / gaze direction: $\hat{g}$ (points from the camera to the object)
- up direction: $\hat{t}$

Usually we transform the camera to the origin, up at Y, look at -Z.  
And transform the objects along with the camera.

### Transform the camera (MV transformation)

*Steps:*

1. Translate e to origin ($T_{view}$)
2. Rotate g to -Z, t to Y, (g, x, t) to x ($R_{view}$)

$T_{view}$:

$$
T_{view}=
\begin{pmatrix}
1 & 0 & 0 & -x_e \\
0 & 1 & 0 & -y_e \\
0 & 0 & 1 & -z_e \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

$R_{view}$: Consider its inverse rotation (X to (g, x, t), Y to t, Z to -g).

!!! common-comment "comment"

    Both the direction and order of rotation must be reversed.


$$
R_{view}^{-1}=\begin{pmatrix}
x_{\hat{g}\times\hat{t}} & x_t & x_{-g} & 0 \\
y_{\hat{g}\times\hat{t}} & y_t & y_{-g} & 0 \\
z_{\hat{g}\times\hat{t}} & z_t & z_{-g} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

Since $R_{view}$ is orthoganal, 
$$R_{view}=(R_{view}^{-1})^T$$

### Projection transformation

*Two 3D -> 2D types:*
1. orthographic projection
2. perspective projection

#### Orthographic projection

Consider a cuboid $[l,r]\times[b,t]\times[f,n]$, map it to the canonical cube $[-1,1]^3$, and drop Z coordinate to project.

??? common-comment "Why we just need to drop Z coordinate?"

    In the ["Define camera"](#define-camera) part, we define the camera located at the origin, up at Y, look at -Z.

\[
M_{ortho} =
\begin{pmatrix}
\frac{2}{r - l} & 0 & 0 & 0 \\
0 & \frac{2}{t - b} & 0 & 0 \\
0 & 0 & \frac{2}{n - f} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 & 0 & -\frac{r + l}{2} \\
0 & 1 & 0 & -\frac{t + b}{2} \\
0 & 0 & 1 & -\frac{n + f}{2} \\
0 & 0 & 0 & 1
\end{pmatrix}
\]

#### Perspective projection

Illustration:

![perspective illustration](../../images/perspective illustration.png){style="width:400px"}

*Steps:*
1. Squish the frustum into a cuboid, all points on the near plane remain unchanged, all points on the far plane undergo in-plane contraction, with the center point of the far plane remaining fixed.  
2. Do orthographic projection.

$$
M_{persp\to ortho}=\begin{pmatrix}
n & 0 & 0 & 0\\
0 & n & 0 & 0\\
0 & 0 & n+f & -nf\\
0 & 0 & 1 & 0
\end{pmatrix}
$$

??? common-comment "Derivation"

    Squish illustration:  
    ![squish illustration](../../images/squish illustration.png){style="width:500px"}  

    $$
    M_{persp\to ortho}\begin{pmatrix}x\\y\\z\\1\end{pmatrix}
    =\begin{pmatrix}nx/z\\ny/z\\?\\1\end{pmatrix}
    =\begin{pmatrix}nx\\ny\\?\\z\end{pmatrix}
    $$

    thus,

    $$
    M_{persp\to ortho}=\begin{pmatrix}
    n&0&0&0\\
    0&n&0&0\\
    A&B&C&D\\
    0&0&1&0
    \end{pmatrix}
    $$

    According to the properties of squishing, consider a point on the near plane and the middle point on the far plane to solve the third row.

    1. $(x,y,n,1)\to(x,y,n,1)=(nx,ny,n^2,n)$
        $n^2$ is unrelated to x and y, thus $A=B=0, Cn+D=n^2$
    2. $(0,0,f,1)\to(0,0,f,1)=(0,0,f^2,f)$
        $Cf+D=f^2$

    Solve the equations above:
    $$C=n+f, D=-nf$$

