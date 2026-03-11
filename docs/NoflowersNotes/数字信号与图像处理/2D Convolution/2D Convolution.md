
## 2D Convolution

### Perfect Imaging

Imaging by a impulse function.

$$
Output(x, y) = Input(x, y) \otimes \delta(x, y)
$$

### Imperfect Imaging

When $\delta(x, y)$ turns into some approx of the 2D impulse function, the output will be distorted.

The **Gaussian blur** is defined as

$$
Output(x, y) = Input(x, y) \otimes G(x, y)
$$

where $G(x, y)$ is the 2D Gaussian function.

!!! remarks "Deconvolution"

    Then how to get the input by processing the output and the gaussian kernel?

    $$
    Input(x, y) = \mathcal{F}^{-1}\left\{\frac{\mathcal{F}\{Output\}}{\mathcal{F}\{G\}}\right\}
    $$

    What if $Output = Input \otimes G + n$ where $n$ is a noise? (To be completed)