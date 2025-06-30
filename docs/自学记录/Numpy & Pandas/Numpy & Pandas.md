# Numpy

## List 的复杂度分析

Python 的 `list` 是用 一块连续的内存空间 存储元素的：

- 内部实际是一个 指针数组（即 `PyObject**` 指针数组），每个元素指向一个 Python 对象。
- 所以列表本身存的是对象的引用，不是对象本身。
- 所以 Python 的 list 可以包含不同类型的数据（因为存的是指针）。

## 小技巧

### 逆置

```python
a -> a[:: -1]
```

### IO

```python
# 保存到 outfile.npy 文件上
np.save('outfile.npy', a) 
 
# 保存到 outfile2.npy 文件上
np.save('outfile2', a)

# c 使用了关键字参数 sin_array
np.savez("runoob.npz", a, b, sin_array = c)
r = np.load("runoob.npz")  
```

# Pandas

NaN 占位符: `np.nan`

## Series

初始化 `s = pd.Series(data, index=index)` （相当于一列 ）

上述代码中，data 支持以下数据类型 （一维）：

 - Python 字典
 - 多维数组
 - 标量值（如，5）

## DataFrame

DataFrame 支持多种类型的输入数据：

 - 一维 ndarray、列表、字典、Series 字典
 - 二维 numpy.ndarray
 - 结构多维数组或记录多维数组
 - Series
 - DataFrame

![img.png](img.png)

### 索引

`df[xxx]` 返回 xxx **列**构成的 Series

### IO

