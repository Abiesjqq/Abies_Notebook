## 编译

~~在Github主页上给出的代码为:~~

```bash
git clone https://github.com/ssloy/tinyrenderer.git &&
cd tinyrenderer &&
cmake -Bbuild &&
cmake --build build -j &&
build/tinyrenderer obj/diablo3_pose/diablo3_pose.obj obj/floor.obj
```

~~但是可能会碰到连接不稳定无法下载的情况，可以直接在GitHub里download zip~~

~~解压后要cd到类似于`<name>\tinyrenderer-master\tinyrenderer-master`文件夹执行build指令~~

~~`tinyrenderer.exe`文件在`build\Debug`里,最后一条指令可改用`.\build\Debug\tinyrenderer.exe obj\diablo3_pose\diablo3_pose.obj obj\floor.obj`~~

只要tgaimage.h, tgaimage.cpp等，编译时链接起来即可

编译运行示例：

```bash
g++ temp.cpp tgaimage.cpp -o temp
temp
```

## geometry.h 简介

### 向量 vec

用`vec<n>`可以创建任意维度的向量，元素类型为 double。`vec<2>`可简写为`vec2`，`vec<3>`可简写为`vec3`。

用`v[i]`可以访问向量 v 的第 i 个元素。特别地，可用 `.x`, `.y` 访问`vec2`，用 `.x`, `.y`, `.z` 访问`vec3`。对于`vec4`，`.xy()`返回前两位，`.xyz()`返回前三位。

运算符`*`表示向量点乘，返回类型为 double。运算符`+-`表示向量的加减法。`向量*常数`，`常数*向量`，`向量/常数`均可行。

`norm(v)`表示向量的模长，返回类型为 double。

`cross(a,b)`表示三维向量的叉积（仅对 vec3 定义），返回类型为`vec3`。

额外定义`vec2i`，元素类型为 int。

## 矩阵 mat

`mat<nrows,ncols> m`用于创建 nrows*ncols 的矩阵 m，元素类型为 double。用`m[i][j]`访问第 i 行第 j 列的元素。

`m.n_rows()`返回矩阵的行数，`m.n_cols()`返回矩阵的列数，返回类型均为int。

`transpose(m)`求矩阵 m 的转置。

`invert(m)`求矩阵 m 的逆。

`det(m)`求矩阵 m 的行列式。

矩阵乘法运算符为`*`，支持矩阵和大小对应的向量相乘。矩阵加减法运算符为`+-`。

`矩阵*标量`，`矩阵/标量`可行，矩阵中每个元素乘除相应值。
