## Material

渲染方程中的 BRDF 决定物体的材质。Material == BRDF

### Diffuse / Lambertian Material

Light is equally reflected in each output direction.

假设各个方向进入的光强度相同，即入射光均匀。假设被照射的点既不吸收光也不发出光。

根据能力守恒，进入的能量和反射出的能量相等。进入的能量为被照射的点周围一小块区域接收的光，即当前点的 irradiance。所以入射和出射的radiance相等。

$$
\begin{align*}
L_o(\omega_o)&=\int_{H^2}f_r L_i(\omega_i)\cos\theta_i\mathrm{d}\omega_i \\
&=f_r L_i\int_{H^2}\cos\theta_i\mathrm{d}\omega_i \\
&=\pi f_r L_i
\end{align*}
$$

故常数BRDF为：

$$f_r=\frac{\rho}{\pi}$$

其中$\rho$为albedo系数，可以为常数，可以为RGB分开设置。


