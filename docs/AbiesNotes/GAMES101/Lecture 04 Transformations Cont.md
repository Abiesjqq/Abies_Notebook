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

!!! normal-comment "comment"

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

??? normal-comment "Why we just need to drop Z coordinate?"

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

![perspective illustration](../../images/perspective illustration.png){style="width:300px"}

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

??? normal-comment "Derivation"

    Squish illustration:  
    ![squish illustration](../../images/squish illustration.png){style="width:300px"}  

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

