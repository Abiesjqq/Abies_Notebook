## 参考

可能由于官方教程是几年前编写的，下载得到的头文件在命名、使用等方面和教程以及网上的笔记有小小的出入。

学习参考：

- [官方 wiki](https://github.com/ssloy/tinyrenderer/wiki)
- [官方 v2](https://haqr.eu/tinyrenderer/)
- [知乎 Shawoxo 的笔记](https://zhuanlan.zhihu.com/p/399056546)

~~以及 g 老师和 d 老师的倾情相助，帮我解决了大部分问题~~

## 编译

只要 tgaimage.h, tgaimage.cpp 等，编译时链接起来即可.

编译运行示例：

```bash
g++ name.cpp tgaimage.cpp model.cpp -o name
name
```

编译不要加`-O2`的优化，会产生未知错误导致文件无法读取。~~我也不知道为什么~~

不需要用 CMake。

## 模块简介

??? normal-comment "Model 简介"

    `Model model = new Model("name.obj");`用`model`表示 name.obj 对应的模型。

    `model->nverts()`得到点数，`model->nfaces()`得到面数。

    所有顶点按顺序依次存在`facet_vrt`中，顶点的法向量依次存在`facet_nrm`中，第 i 个面第 j 个顶点的索引为`i*3+j`。但这两个 vector 是私有属性。

    `model->vert(i,j)`得到第 i 个面第 j 个顶点的位置，返回类型为 vec3。

    `model->normal(i,j)`得到第 i 个面第 j 个顶点的法向量，返回类型为 vec3。

    `model->index(i,j)`得到第 i 个面第 j 个顶点的编号，返回类型为 int。

    `model->uv(i,j)`得到第 i 个面第 j 个顶点纹理信息，即这个顶点在纹理图案中的坐标，返回类型为 vec2。

    `model->diffuse()`得到对应贴图的图像，返回类型为 TGAImage。`model->diffuse().get(x,y)`获得贴图上坐标(x,y)处的像素颜色。

??? normal-comment "vec 简介"

    用`vec<n>`可以创建任意维度的向量，元素类型为 double。`vec<2>`可简写为`vec2`，`vec<3>`可简写为`vec3`。

    用`v[i]`可以访问向量 v 的第 i 个元素。特别地，可用 `.x`, `.y` 访问`vec2`，用 `.x`, `.y`, `.z` 访问`vec3`。对于`vec4`，`.xy()`返回前两位，`.xyz()`返回前三位。

    运算符`*`表示向量点乘，返回类型为 double。运算符`+-`表示向量的加减法。`向量*常数`，`常数*向量`，`向量/常数`均可行。

    `norm(v)`表示向量的模长，返回类型为 double。

    `normalized(v)`返回单位化的向量。

    `cross(a,b)`表示三维向量的叉积（仅对 vec3 定义），返回类型为`vec3`。

    额外定义`vec2i`，元素类型为 int。

??? normal-comment "mat 简介"

    `mat<nrows,ncols> m`用于创建 nrows\*ncols 的矩阵 m，元素类型为 double。用`m[i][j]`访问第 i 行第 j 列的元素。

    `m.n_rows()`返回矩阵的行数，`m.n_cols()`返回矩阵的列数，返回类型均为 int。

    `transpose(m)`求矩阵 m 的转置。

    `invert(m)`求矩阵 m 的逆。

    `det(m)`求矩阵 m 的行列式。

    矩阵乘法运算符为`*`，支持矩阵和大小对应的向量相乘。矩阵加减法运算符为`+-`。

    `矩阵*标量`，`矩阵/标量`可行，矩阵中每个元素乘除相应值。

    `identity<n>()`生成 n\*n 的单位矩阵。
