## Monte Carlo Integration

**Why:** we want to solve an integral, but it can be too difficult to solve $\int_a^b f(x)dx$ analytically.

**What & how:** estimate the integral of a function by averaging random samples of the function's value.

**Monte Carlo estimator:**

$$X_i\sim p(x)\quad\int_a^b f(x)dx $$

$$\int f(x)dx=\frac{1}{N}\sum_{i=1}^N\frac{f(X_i)}{p(X_i)}$$

- The more samples, the less variance.
- Sample on X, integration on X.

## Path Tracing

**Problems of Whitted-Style:**

- Glossy texure (Utah teapot)
- Color bleeding (Cornell box)

**A simple example: direct illumination**

$$
L_o(\mathrm{p},\omega_o)=\int_{\Omega^+}L_i(\mathrm{p},\omega_i)f_r(\mathrm{p},\omega_i,\omega_o)(n\cdot\omega_i)\mathrm{d}\omega_i
$$

- $f(x)$: $L_i(\mathrm{p},\omega_i)f_r(\mathrm{p},\omega_i,\omega_o)(n\cdot\omega_i)$
- $pdf(\omega)$: $1/2\pi$

Monte Carlo integration:

$$
L_o(\mathrm{p},\omega_o)\approx\frac{1}{N}\sum_{i=1}^N\frac{L_i(\mathrm{p},\omega_i)f_r(\mathrm{p},\omega_i,\omega_o)(n\cdot\omega_i)}{pdf(\omega_i)}
$$

Code:

```
shade (p, wo)
    Randomly choose N directions wi~pdf
    Lo = 0.0
    For each wi
        Trace a ray r(p, wi)
        If ray r hit the light
            Lo += (1 / N) * L_i * f_r * cosine / pdf(wi)
    Return Lo
```

**Introduce global illumination:**

The light reflect from Q to P, equals to the direct illumination ar Q observed at P.

```
shade (p, wo)
    Randomly choose N directions wi~pdf
    Lo = 0.0
    For each wi
        Trace a ray r(p, wi)
        If ray r hit the light
            Lo += (1 / N) * L_i * f_r * cosine / pdf(wi)
        Else If ray r hit an object at q
            Lo += (1 / N) * shade(q, -wi) * f_r * cosine / pdf(wi)
    Return Lo
```

**Problems 1:** Explosion of rays as bounces go up  
Rays will not explode iff N = 1.

This is "path tracing".

Code:

```
shade (p, wo)
    Randomly choose ONE directions wi~pdf(w)
    Lo = 0.0
    For each wi
        Trace a ray r(p, wi)
        If ray r hit the light
            Return L_i * f_r * cosine / pdf(wi)
        Else If ray r hit an object at q
            Return shade(q, -wi) * f_r * cosine / pdf(wi)
```

## Ray Generation

```
ray_genaration(camPos, pixel)
    Uniformly choose N sample positions within the pixel
    pixel_radiance = 0.0
    For each sample in the pixel
        Shoot a ray t(camPos, cam_to_sample)
        If ray r hit the scene at p
            pixel_radiance += 1 / N * shade(p, sample_to_cam)
    Return pixel_radiance
```

**Problem 1:** The recursion won't stop.  
**Solution:** Russian Roulette (RR)

Suppose we manually set a probability P (0<P<1).  
With probability P, shoot a ray and return the shading result divided by P is Lo / P.  
With probability 1-P, don't shoot a ray adn you'll get 0.

In this way, you can still expect to get Lo:  
E = P _ (Lo / P) + (1 - P) _ 0 = Lo

Code:

```
(Add)
    Manually specify a probability P_RR
    Randomly select ksi in a uniform dist. in [0, 1]
    If (ksi > P_RR) retunr 0.0

    Return ... / P_RR
```

**Problem 2:** Inefficient. When SPP (samplees per pixel) is low, get noisy results

Only a few rays hit the light, so a lot of rays are "wasted".

**Solution:** sample on the light

Assume pdf = 1 / A. But the rendering equation intefrates on the solid angle.

To sample on the light and integrate on the light, need the relationship between $d\omega$ and $dA$.

![sample the light](../resources/sample%20the%20light.png){style="width:400px"}

$$d\omega=\frac{dA\cos\theta'}{|| x'-x ||^2}$$

Rewrite the rendering equation:

$$
\begin{align*}
L_o(\mathrm{p},\omega_o)&=\int_{\Omega^+}L_i(\mathrm{p},\omega_i)f_r(\mathrm{p},\omega_i,\omega_o)\cos\theta\,\mathrm{d}\omega_i \\
&=\int_A L_i(\mathrm{p},\omega_i)f_r(\mathrm{p},\omega_i,\omega_o)\frac{\cos\theta\cos\theta'}{|| x'-x ||^2}\mathrm{d}A
\end{align*}
$$

Code:

```
shade(p, wo)
    # Contribution from the light source.
    Uniformlu sanple the light at x' (pdf_light = 1 / A)
    L_dir = L_i * f_r * cos theta * cos theta' / |x' - p|^2 / pdf_light

    # Contribution from other reflectors
    L_indir = 0.0
    Test Russian Roulette with probability P_RR
    Uniformly sample the hemisphere toward wi (pdf_hemi = 1 / 2pi)
    Trace a ray r(p, wi)
    If ray r hir a non-emitting object ar q
        L_indir = shade(q, -wi) * f_r * cos theta / pdf_hemi / P_RR

    Return L_dir + L_indir
```

**Final problem:** need to test if the ray os not blocked in the middle.

Hard to handle point light source.

Things haven't covered:

- Uniformly sampling the hemisphere  
  - How? And in gengral. how to sample any function?   

- Monte Carlo intefration allows arbitatry pdfs  
  - What's the best choice? (importance sampling)   

- Do random numbers matter?  
  - Yes (low discrepancy sequences)  

- Sample the hemimsphere and the light  
  - Can I combine them? Yes (multipe immp. sampling) 
 
- The radiance of a pixel is the average of radiance on all paths passing through it  
  - Why? (pixel reconstruction filter)  

- Is the radiance of a pixel the color of a pixel?  
  - No. (gamma correction, curves, color space)