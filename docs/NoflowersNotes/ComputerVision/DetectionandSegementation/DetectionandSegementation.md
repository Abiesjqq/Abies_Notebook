## Semantic Segmentation

Detect which region a pixel belongs to.

At training time, each pixel is labeled with a semantic category. And at test time,classify each pixel of a new image.

### Fully Convolutional

Design network as a bunch of convolutional layers, with downsampling and upsampling inside the network.

![img.png](img.png)

#### Upsampling

##### Unpooling

Sampling --> Pooling

e.g. Max Unpooling: Set others to zero, and put it back to the original position.

![img_1.png](img_1.png)

##### Transposed Convolution

The inverse of convolution.

$$
Y[m, n] = \sum_{i=0}^{H-1} \sum_{j=0}^{W-1} X[i, j] \cdot K[m - i \cdot s, n - j \cdot s]
$$

> $X$: input figure  
> $K$: conv kernel  
> $Y$: larger output  

