# Lec 07 Interactive Segmentation & Graph-Cut

目标：根据用户提供的粗糙边框提取物体

用二维网格表示图像，每个像素是网格的顶点，和周围若干个相邻的像素相连。  
将图像分割视为二分割的问题，根据用户边框分为前景和背景

## 1-NN 分类

将每个像素转换为 RGB 空间中三维的点，分别计算和 foreground 和 background 的最近的距离，判断哪个更近。  
或聚类分析，找最近的类。

**优化 1**：定义函数，使得 cost 最小时将图像上所有点划分为 foreground 和 background  
用 F 表示用户标注出的 foreground，B 表示用户标注的 background，cost 为 0 时为 foreground

**优化 2**：Markov Random Field (MRF)，考虑相邻像素的连续性。

## MRF

### MRF 定义

像素作为 MRF Nodes，节点间有 MRF edges 相连。每个节点分别计算到 foreground 和 background 的 cost（data cost）。因为要使全局 cost 最小，像素的两个 cost 中哪个小选哪个。

在边上也定义 cost function（smooth cost），表示相邻节点的相似程度。总的 cost 为两种 cost 相加。

Smooth cost:

$$E_2(x_i,x_j)=|x_i-x_j|\cdot g(C_{ij})$$

其中 x 为 0 或 1（前景或背景），C 表示 color：

$$g(\xi)=\frac{1}{\xi +1}\, ,\, C_{ij}=||C(i)-C_(j)||^2$$

转化为图的问题：部分节点标注为 0 或 1，剩余点有 0、1 两种状态。找到全局状态 X，使总 cost 最小。

### Min-cut 和 Max-flow

#### Max-flow

最大流问题，本质上是线性规划问题  
simplex 算法求解：从一个可行解出发，每次选一个管道增大流量、直到打破某条约束。重复操作。具体方法回忆 fds。  
对图的某些切分，切割边上的流量和等于最大流量。min-cut = max-flow.

#### 图像分割原理

在图像中，将边视为管道，边的容量为连接的两个像素的相似程度，越不相似则容量越小、越有可能被切开。  
引入两个额外的节点，FG 作为 source，BG 作为 sink，和每个节点相连。这些边的容量和对应的 cost 负相关。  
找到一个 min-cut 将图像一分为二，和 source 相连的为 FG。

这里用 max-flow 能得到全局最优解。

**cost 计算：**

在 RGB 空间，对 FG 和 BG 分别拟合高斯分布，对每个高斯分布的中心计算距离。

**优化：**

图像分成不规则的 super-pixel，每个 super-pixel 作为一个节点

### 非二进制标签

如果标签 x 不一定是 0、1，令标签为 1-n

**Alpha-expansion**：对每个像素，判断是否需要切换为第 alpha 个标签。是、否转化为二进制问题。  
从初始值开始迭代，alpha 值轮流取 1-n。
