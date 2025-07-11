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
