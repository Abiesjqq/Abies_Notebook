**实验内容**：给定一段静态背景的目标运动视频，通过背景建模获取场景的背景图像（不包含目标），并进行图像去噪

视频由一系列连续的图像帧组成

视频写入：声明保存路径，格式，帧率，分辨率

静态视频的背景建模

**均值法**：在一段时间内取N帧视频图像序列，对于每个像素点，在这N帧图像在此点均值为该点背景图像中的灰度值

**中值法**：在一段时间内取N帧视频图像序列，对于每个像素点，在这N帧图像在此点处的N个像素值按从小到大排序，然后将排序后的中值作为该点背景图像中的灰度值

--- 

## 基础操作

### 读取视频并保存帧

要捕获视频，你需要创建一个 VideoCapture 对象。以下是一个读取视频并将每一帧保存到 frame 文件夹的示例：

在这个示例中，我们通过传递视频文件的路径创建了一个 VideoCapture 对象。然后，我们使用 while 循环通过 read() 方法读取视频的每一帧。如果帧读取成功，我们使用 imwrite() 方法保存该帧。最后，我们释放 VideoCapture 对象。

```py
import cv2
import os

folder=os.path.exists('frame')

# 检查‘frame’文件夹是否存在
# 如果不存在，则创建文件夹
if not folder:
    os.makedirs('frame')
    print('new folder...')
    print('OK')
else:
    print('There is this folder!')

# 帧编号
number=0

# 创建VideoCapture对象
cap=cv2.VideoCapture('video.mp4')

while True:
    # 从视频中读取一帧
    ret,frame=cap.read()

    # 帧编号增加
    number=number+1
    if ret:
        # 保存帧
        cv2.imwrite(f"./frame/save{number}.jpg",frame)

    # 退出循环
    else:
        break

print('Saved in the frame folder.')

print('Success!')

# 释放VideoCapture对象
cap.release()
```

### 写入并保存视频

要写入并保存视频，你需要创建一个 VideoWriter 对象。以下是一个如何写入并保存视频的示例：

在这个示例中，我们通过传递视频文件的路径创建了一个 VideoCapture 对象。然后，我们使用 get() 方法获取视频帧的尺寸和帧率。接下来，我们通过传递输出文件名、fourcc 编码、帧率和帧尺寸创建了一个 VideoWriter 对象。fourcc 编码是一个四字节编码，用于指定视频编解码器。在这个示例中，我们使用了 XVID 编解码器。

然后，我们使用 while 循环通过 read() 方法读取视频的每一帧。如果帧读取成功，我们对其进行处理（例如，应用滤镜），并使用 VideoWriter 对象的 write() 方法将其写入输出视频。最后，我们释放 VideoCapture 和 VideoWriter 对象。

```py
import cv2

# 创建一个 VideoCapture 对象
cap = cv2.VideoCapture('video.mp4')

# 获取视频帧的尺寸和帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 创建一个 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

while True:
    # 从视频中读取一帧
    ret, frame = cap.read()

    if ret:
        # 处理帧
        # ...
        # 将处理后的帧写入输出视频
        out.write(frame)

    else:
        break

print('Succeed in saving!')

# 释放 VideoCapture 和 VideoWriter 对象
cap.release()
out.release()
```

### 图像直方图

在这个示例中，我们通过 cv2.imread() 以灰度格式读取图像文件。然后，使用 cv2.calcHist() 或 numpy.histogram() 计算直方图。最后，使用 matplotlib 绘制直方图并通过 savefig() 保存。

```py
import cv2
import matplotlib.pyplot as plt

# 读取图像，灰度格式
image_path = 'test.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 计算直方图
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# 可视化直方图
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.plot(hist, color='black')
plt.xlim([0, 256])

# 保存绘图
save_path = 'histogram.png'
plt.savefig(save_path)

print(f'Saved as: {save_path}')
```

`calcHist`参数：


* 第1个参数 `[img]`：图像数据，放在列表里，因为可以一次处理多张图像。

  * 这里是单张图，所以写 `[img]`。

* 第2个参数 `[0]`：要计算的通道索引。

  * 灰度图只有一个通道（索引 0）。
  * 彩色图：0=B，1=G，2=R。

* 第3个参数 `None`：掩模（mask），如果不想对整幅图像计算直方图，而是选定部分区域，就在这里传入掩模。

  * `None` 表示使用整张图像。

* 第4个参数 `[256]`：直方图的 bins（柱子数），即灰度值划分的区间个数。

  * 256 表示 0\~255 共 256 个灰度级。

* 第5个参数 `[0, 256]`：灰度值范围。

  * 通常是 `[0, 256]`，因为 OpenCV 直方图上限是非包含型（不包含 256）。

### 遍历像素

1. 使用 cv2.VideoCapture() 读取视频。  
2. 通过 cap.read() 逐帧读取视频。  
3. 对每一帧（本质是 NumPy 数组）用双重或三重循环（灰度图用双重，彩色图用三重）遍历像素。

```py
import cv2

# 打开视频文件
cap = cv2.VideoCapture('video.mp4')

# 判断是否打开成功
if not cap.isOpened():
    print('Failed to open the video.')
    exit()

# 帧数
frame_count = 0

# 逐帧读取
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    print(f"Processing frame {frame_count}.")

    # 每一帧的大小(H,W,C)
    height, width, channel = frame.shape

    for y in range(height):
        for x in range(width):
            # 获取RGB三个通道值
            b, g, r = frame[y, x]
            # 处理像素
            # ...
            pass

# 释放视频对象
cap.release()
print('Finished!')

```

### 均值法背景建模

1. 读取视频：用 cv2.VideoCapture() 打开视频文件。  
2. 选择 N 帧：可以选择视频的前 N 帧，或者每隔若干帧采样。  
3. 累加像素值：对每一帧，将每个像素的颜色值累加到一个累加数组中。   
4. 求均值：累加完成后，将累加值除以帧数 N，得到每个像素的平均值，即背景颜色值。

```py
import cv2
import numpy as np

# 视频路径
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

# 设置帧数
N = 50 # 总处理帧数
count = 0 # 已处理帧数

# 读取第一帧获取尺寸
ret, frame = cap.read()
if not ret:
    print('Cannot read the video!')
    exit()

# 每一帧的参数(H,W,C)
height, width, channels = frame.shape

# 初始化累加数组（浮点型）
accumulate = np.zeros((height, width, channels), dtype=np.float32)

# 将第一帧加入累加
accumulate += frame
count += 1

while count < N:
    ret, frame = cap.read()
    if not ret:
        break

    accumulate += frame
    count += 1

# 求均值
background = (accumulate / count).astype(np.uint8)

# 高斯滤波平滑背景，消除鬼影
background_smooth = cv2.GaussianBlur(background, (7, 7), 0)

# 左边是原始均值背景，右边是平滑后的背景
combined = np.hstack((background, background_smooth))

# 保存背景图像
cv2.imwrite('background_comparison.png', combined)
print('Comparison image saved!')

cap.release()

```

### 中值法背景建模

1. 读取视频，选择 N 帧。  
2. 将 N 帧存入数组（每帧为 (H, W, C)）。  
3. 对每个像素点沿时间轴取 N 个像素值，计算中值（np.median）。  
4. 得到背景图像。

```py
import cv2
import numpy as np

# 视频路径
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

# 设置使用的帧数
N = 50
count = 0
frames = []

# 读取前N帧
while count < N:
    ret, frame = cap.read()
    if not ret:
        break
    
    frames.append(frame.astype(np.float32)) # 转浮点，避免溢出
    count += 1

cap.release()

if len(frames) == 0:
    print('Failed to read any frames.')
    exit()

# 将帧堆叠为(N,H,W,C)
stacked_frames = np.stack(frames, axis=0)

# 沿时间轴计算中值
background = np.median(stacked_frames, axis=0).astype(np.uint8)

# 保存背景图像
cv2.imwrite('background_median_color.png', background)
print('Background saved!')

```

---

## 前景提取和识别


### 任务 2 · 基于**背景差分**的前景建模与运动检测

**目标**：利用任务 1 的背景图或在线更新的背景，提取前景大鼠机器人，完成目标检测与可视化。  
**输出**：检测可视化视频 `outputs/detect_vis.mp4`，以及关键帧可视化与简单指标。

> 评分：
>
> - 1.1 图像处理基础
> - 1.2 静态背景差分
> - 1.3 轮廓筛选 + 最小外接矩形（minAreaRect）实现目标检测和跟踪
> - 1.4 扩展任务（+分）：对比 OpenCV 背景建模器

```py
# %pip install opencv-python numpy matplotlib ipywidgets -q
import cv2, numpy as np, math, time
from pathlib import Path
import matplotlib.pyplot as plt
from IPython.display import Video, display

from matplotlib import pyplot as plt
from matplotlib import font_manager, rcParams
# 在 Windows 上常见的中文字体优先级列表
_candidate_fonts = [
    "SimHei",            # 黑体
    "Microsoft YaHei",   # 微软雅黑
    "SimSun",            # 宋体
    "KaiTi",             # 楷体
]
rcParams['font.sans-serif'] = _candidate_fonts
rcParams['axes.unicode_minus'] = False  # 使坐标轴等能正常显示负号
print("Matplotlib 中文字体设置完成：", rcParams['font.sans-serif'])

DATA = Path("data")
OUT = Path("outputs")
DATA.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)

video_path = str(DATA/"demo.mp4")
bg_path = str(DATA/"bg_estimated.jpg")
print("视频：", video_path)
print("背景：", bg_path)
```

### 图像处理基础 

本节将给出任务2中“背景差分→阈值化→形态学处理”的核心步骤涉及到的知识点：**概念、数学定义/直觉、典型参数、常见坑、示例代码**。  
建议课堂：每位同学先单独运行每个知识点的例子，再把它们按“差分→阈值→开/闭”的顺序组合起来完成检测。


> 演示默认使用 `data/room.mp4` 和 `outputs/bg_estimated.jpg`；如未生成，请先完成任务1。

#### 知识点 1：`cv2.absdiff` —— 像素级**绝对差分**（背景差分/帧间差分）
**作用**：衡量两张图对应像素的强度差异，用于把“变化/运动”的区域凸显出来。  
**数学**：对每个像素 $(x,y)$ 和通道 $c$，$D(x,y,c) = |I_1(x,y,c) - I_2(x,y,c)|$。  
**两种常见用法**：  
1) **背景差分**：`absdiff(当前帧, 背景)` → 适合**静态背景**。  

2) **帧间差分**：`absdiff(当前帧, 上一帧)` → 适合**慢变化光照**但会对低速物体不敏感。

**要点 & 坑**：  
- 先做**灰度化**可减少噪声和通道差异；彩色差分有时会放大颜色抖动。  
- 差分前可做**轻微平滑（高斯/均值）**抑制传感器噪声。  
- 输入类型通常是 `uint8`，`absdiff` 已处理了溢出/符号问题。

下面代码展示**背景差分**与**帧间差分**的可视化：

```py
# 准备单帧示例
cap = cv2.VideoCapture(str(Path("data")/"demo.mp4"))
ok, f1 = cap.read()
ok2, f2 = cap.read()  # 下一帧（用于帧间差分）
cap.release()

bg = cv2.imread(str(Path("data")/"bg_estimated.jpg"), cv2.IMREAD_COLOR)
assert f1 is not None and bg is not None, "请先完成任务1并确保存在 data/room.mp4 与 outputs/bg_estimated.jpg"

# 预处理：转灰度 & 轻微模糊（可调）
g1 = cv2.GaussianBlur(cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY), (5,5), 0)
g2 = cv2.GaussianBlur(cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY), (5,5), 0)
gbg = cv2.GaussianBlur(cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY), (5,5), 0)

# TODO：可以自己实现一个absdiff函数
diff_bg = cv2.absdiff(g1, gbg)  # 背景差分
diff_fr = cv2.absdiff(g2, g1)   # 帧间差分

fig, ax = plt.subplots(1,3, figsize=(12,4))
ax[0].imshow(cv2.cvtColor(f1, cv2.COLOR_BGR2RGB)); ax[0].set_title("原始帧")
ax[1].imshow(diff_bg, cmap="gray"); ax[1].set_title("背景差分 absdiff(frame, bg)")
ax[2].imshow(diff_fr, cmap="gray"); ax[2].set_title("帧间差分 absdiff(frame_t, frame_t-1)")
for a in ax: a.axis("off")
plt.show()
```

#### 知识点 2：`cv2.threshold` —— **阈值化**把差分图转为二值前景
**作用**：将灰度差分图转换为二值掩码（前景=1/背景=0）。  
**基本形式**：`_, mask = cv2.threshold(diff, T, 255, cv2.THRESH_BINARY)`  
其中$T$是阈值。

**选择阈值的三种思路**：  
1) **固定阈值**（课堂推荐起点）：如 $T \in [25,35]$。  

2) **OTSU 自动阈值**：`cv2.THRESH_BINARY+cv2.THRESH_OTSU`，对双峰直方图有效。  

3) **自适应阈值**：适合光照不均（本任务先不强制）。

**常见坑**：阈值过小 → 噪声；过大 → 目标断裂/漏检。建议配合直方图观察。

示例：固定阈值 vs OTSU：

Opencv官方文档：https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

```py
# 复用上一节的 diff_bg
diff = diff_bg.copy()

# 固定阈值
T = 28
_, m_fixed = cv2.threshold(diff, T, 255, cv2.THRESH_BINARY)

# OTSU（会忽略手动阈值，返回自动T）
_, m_otsu = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

fig, ax = plt.subplots(1,4, figsize=(12,4))
ax[0].hist(diff.ravel(), bins=50); ax[0].set_title("差分直方图")
ax[1].imshow(diff, cmap="gray"); ax[1].set_title("差分图")
ax[2].imshow(m_fixed, cmap="gray"); ax[2].set_title(f"固定阈值 T={T}")
ax[3].imshow(m_otsu, cmap="gray"); ax[3].set_title("OTSU 自动阈值")
for a in ax: a.axis("off")
plt.show()
```


#### 知识点 3：形态学操作及连通域

图像的**形态学操作**常用于二值图像的处理，基于**结构元素 (structuring element, kernel)**，  
可实现噪声去除、孔洞填补、边界提取等。

---

**（1）基本操作**

- <details>
  <summary><b>腐蚀 Erode（📘 点击展开）</b></summary>

  - **定义**：前景区域收缩，去除细小噪点。  
  - **核心思想**：结构元素内 **所有像素都是前景** 时，中心才保留为前景。  

  **数学表达式**：  

  $$
  A \ominus B = \{ z \mid B_z \subseteq A \}
  $$  

  其中 $A$ 是原图，$B$ 是结构元素。  

  → 结果：边缘收缩，细节变细，孤立点消失。  

  </details>

- <details>
  <summary><b>膨胀 Dilate（📘 点击展开）</b></summary>

  - **定义**：前景区域膨大，填补小孔洞。  
  - **核心思想**：结构元素内 **只要有一个前景**，中心就变为前景。  

  **数学表达式**：  

  $$
  A \oplus B = \{ z \mid (B^s)_z \cap A \neq \emptyset \}
  $$  

  其中 $B^s$ 是 $B$ 的对称。  

  → 结果：边缘扩张，孔洞被填补。  

  </details>

- <details>
  <summary><b>开运算 Open（📘 点击展开）</b></summary>

  - **定义**：先腐蚀后膨胀。  
  - **公式**：  

  $$
  A \circ B = (A \ominus B) \oplus B
  $$  

  → 功能：去除小噪点，保留主要轮廓。  

  </details>

- <details>
  <summary><b>闭运算 Close（📘 点击展开）</b></summary>

  - **定义**：先膨胀后腐蚀。  
  - **公式**：  

  $$
  A \bullet B = (A \oplus B) \ominus B
  $$  

  → 功能：填补小孔，连接断裂区域。  

  </details>

- <details>
  <summary><b>形态学梯度 Gradient（📘 点击展开）</b></summary>

  - **定义**：膨胀 − 腐蚀，突出边界。  
  - **公式**：  

  $$
  \text{Grad}(A) = (A \oplus B) - (A \ominus B)
  $$  

  → 功能：勾勒物体边界。  

  </details>


---

**（2）连通域与轮廓（📘 点击展开）**

- **connectedComponents**：按 4/8 邻域为前景打标签，得到**区域数、标签图**  
- **findContours**：提取外轮廓/层级结构，可用于统计**面积、周长、外接矩形**等  
- 可将标签图**随机上色**直观展示实例分割效果

```py
import cv2, numpy as np, matplotlib.pyplot as plt

# 先用固定阈值得到一个粗掩码
T = 28
_, mask0 = cv2.threshold(diff_bg, T, 255, cv2.THRESH_BINARY)


# 结构元素（核）
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# 腐蚀（瘦身）
erode_3_1 = cv2.erode(mask0, kernel3, iterations=1)
erode_5_1 = cv2.erode(mask0, kernel5, iterations=1)
erode_5_2 = cv2.erode(mask0, kernel5, iterations=2)

# 膨胀（增粗）
dilate_3_1 = cv2.dilate(mask0, kernel3, iterations=1)
dilate_5_1 = cv2.dilate(mask0, kernel5, iterations=1)
dilate_5_2 = cv2.dilate(mask0, kernel5, iterations=2)

# 直接输出（不保存文件）
fig, ax = plt.subplots(2, 4, figsize=(12,6))
ax[0,0].imshow(mask0, cmap="gray"); ax[0,0].set_title("原始二值 mask0")
ax[0,1].imshow(erode_3_1, cmap="gray"); ax[0,1].set_title("Erode 3x3×1")
ax[0,2].imshow(erode_5_1, cmap="gray"); ax[0,2].set_title("Erode 5x5×1")
ax[0,3].imshow(erode_5_2, cmap="gray"); ax[0,3].set_title("Erode 5x5×2")

ax[1,0].imshow(mask0, cmap="gray"); ax[1,0].set_title("原始二值 mask0")
ax[1,1].imshow(dilate_3_1, cmap="gray"); ax[1,1].set_title("Dilate 3x3×1")
ax[1,2].imshow(dilate_5_1, cmap="gray"); ax[1,2].set_title("Dilate 5x5×1")
ax[1,3].imshow(dilate_5_2, cmap="gray"); ax[1,3].set_title("Dilate 5x5×2")

for a in ax.ravel(): a.axis("off")
plt.tight_layout(); plt.show()
```

##### `cv2.morphologyEx` 的 **开运算**（Open）——去小噪点
**定义**：开运算 = 先腐蚀（erode）后膨胀（dilate）。  
**直觉**：清理“盐粒”样的小白点，保留较大前景结构。  
**接口**：`cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)`

**关键参数**：
- `kernel`（结构元素）形状与尺寸极其重要：椭圆/矩形/十字；尺寸 3×3, 5×5, 7×7…  
- 尺寸越大，越容易抹掉细小结构，也可能削弱目标边缘。

示例：不同核尺寸对比：


```py
# 开运算示例

# 先用固定阈值得到一个粗掩码
T = 28
_, mask0 = cv2.threshold(diff_bg, T, 255, cv2.THRESH_BINARY)

ks = [3,5,7]
outs = []
for k in ks:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k,k))
    # 开运算示例
    m_open = cv2.morphologyEx(mask0, cv2.MORPH_OPEN, kernel)
    outs.append((k, m_open))

fig, ax = plt.subplots(1, len(outs)+1, figsize=(14,4))
ax[0].imshow(mask0, cmap="gray"); ax[0].set_title("原始二值")
for i,(k,m) in enumerate(outs, start=1):
    ax[i].imshow(m, cmap="gray"); ax[i].set_title(f"Open {k}x{k}")
for a in ax: a.axis("off")
plt.show()
```

##### `cv2.morphologyEx` 的 **闭运算**（Close）——填孔与连接
**定义**：闭运算 = 先膨胀（dilate）后腐蚀（erode）。  
**直觉**：弥合前景中的小黑洞或窄缝，使目标更连贯。  
**接口**：`cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)`

**开 vs 闭 的顺序**：常见管线是 **开后闭**（先去噪，再填孔）；也可视场景尝试闭后开。

示例：
1、闭运算示例
2、在开运算结果上继续做闭运算：


```py
# 闭运算示例：

# 先用固定阈值得到一个粗掩码
T = 28
_, mask0 = cv2.threshold(diff_bg, T, 255, cv2.THRESH_BINARY)

ks = [3, 5, 7]
outs = []
for k in ks:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    # 闭运算（Close）= 先膨胀后腐蚀：填小孔、连通细缝
    m_close = cv2.morphologyEx(mask0, cv2.MORPH_CLOSE, kernel)
    outs.append((k, m_close))

# 直接输出，不保存
fig, ax = plt.subplots(1, len(outs) + 1, figsize=(14, 4))
ax[0].imshow(mask0, cmap="gray"); ax[0].set_title("原始二值")
for i, (k, m) in enumerate(outs, start=1):
    ax[i].imshow(m, cmap="gray"); ax[i].set_title(f"Close {k}x{k}")
for a in ax: a.axis("off")
plt.show()
```

```py
kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# 开运算（去噪）
_, mask0 = cv2.threshold(diff_bg, 28, 255, cv2.THRESH_BINARY)
mask_open = cv2.morphologyEx(mask0, cv2.MORPH_OPEN, kernel5)

# 闭运算（填孔/连通）
mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel5)

fig, ax = plt.subplots(1,3, figsize=(12,4))
ax[0].imshow(mask0, cmap="gray"); ax[0].set_title("阈值后")
ax[1].imshow(mask_open, cmap="gray"); ax[1].set_title("开运算 → 去噪")
ax[2].imshow(mask_close, cmap="gray"); ax[2].set_title("闭运算 → 连通")
for a in ax: a.axis("off")
plt.show()
```

#### **结构元素（kernel）与参数调优**（实践经验）
**为什么重要**：形态学效果 80% 取决于 kernel 的**形状**与**尺寸**。

- **形状选择**：
  - 椭圆（ELLIPSE）：对“圆滑/椭圆形目标”更自然，常用默认。
  - 矩形（RECT）：更“强硬”，对横竖细节影响更大。
  - 十字（CROSS）：对十字方向更敏感。
- **尺寸经验**：
  - 3×3：轻微去噪或细微连通；
  - 5×5：课堂默认，适中；
  - 7×7+：强力去噪/连通，但可能过度平滑目标边界。

**顺序建议**：先 **Open** 去噪，再 **Close** 连通；如目标内部孔洞较多，可加大闭运算核。

下面网格化比较不同核与顺序：

```py
# 对差异背景图像进行二值化处理
# 参数说明：
# diff_bg: 输入的差异背景图像
# 28: 阈值，像素值超过此值会被处理
# 255: 最大值，超过阈值的像素会被设置为此值
# cv2.THRESH_BINARY: 二值化类型，超过阈值为255，否则为0
# 返回值：第一个为阈值（通常不用，用_接收），第二个为处理后的二值图像base
_, base = cv2.threshold(diff_bg, 28, 255, cv2.THRESH_BINARY)

# 定义不同类型和大小的形态学操作结构元素（卷积核）
# 用于后续的开运算和闭运算，比较不同结构元素的处理效果
kernels = {
    "ELLIPSE-3": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),  # 3x3椭圆形结构元素
    "ELLIPSE-5": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)),  # 5x5椭圆形结构元素
    "RECT-5":    cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)),     # 5x5矩形结构元素
    "CROSS-5":   cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5)),    # 5x5十字形结构元素
}

# 存储不同结构元素处理后的结果
rows = []
# 遍历所有结构元素，分别进行两种顺序的形态学操作
for name,k in kernels.items():
    # 先进行开运算（去除噪点）再进行闭运算（填充孔洞）
    open_then_close = cv2.morphologyEx(cv2.morphologyEx(base, cv2.MORPH_OPEN, k), cv2.MORPH_CLOSE, k)
    # 先进行闭运算（填充孔洞）再进行开运算（去除噪点）
    close_then_open = cv2.morphologyEx(cv2.morphologyEx(base, cv2.MORPH_CLOSE, k), cv2.MORPH_OPEN, k)
    # 将结构元素名称和两种处理结果存入列表
    rows.append((name, open_then_close, close_then_open))

# 可视化所有结果，便于对比
# 创建子图：行数为结构元素数量+1（多一行放原始图），列数为3
# figsize设置图像整体大小
fig, ax = plt.subplots(len(rows)+1, 3, figsize=(10, 3*(len(rows)+1)))

# 第一行显示原始二值图像
ax[0,0].imshow(base, cmap="gray"); ax[0,0].set_title("原始二值")
# 第一行后两列不显示内容，关闭坐标轴
ax[0,1].axis("off"); ax[0,2].axis("off")

# 遍历处理结果，逐行显示
for i, (name, o_c, c_o) in enumerate(rows, start=1):
    # 第一列显示结构元素名称
    ax[i,0].text(0.0, 0.5, name, fontsize=12); ax[i,0].axis("off")
    # 第二列显示先开后闭的处理结果
    ax[i,1].imshow(o_c, cmap="gray"); ax[i,1].set_title("Open→Close")
    # 第三列显示先闭后开的处理结果
    ax[i,2].imshow(c_o, cmap="gray"); ax[i,2].set_title("Close→Open")

# 关闭所有子图的坐标轴，使图像更整洁
for a in ax.ravel():
    if hasattr(a, "set_axis_off"): a.set_axis_off()

# 自动调整子图间距
plt.tight_layout()
# 显示图像
plt.show()
```

```py
def prepare_demo():
    """准备演示用的视频帧和前景掩码，用于展示背景差分与形态学处理效果"""
    # 读取视频文件（路径为data目录下的demo.mp4）
    # 使用Path处理路径，增强跨平台兼容性
    cap = cv2.VideoCapture(str(Path("data")/"demo.mp4"))
    
    # 读取视频的一帧画面，并释放视频捕获资源（仅需一帧用于演示）
    # ok为布尔值，表示是否成功读取帧；frame为读取到的视频帧
    ok, frame = cap.read(); cap.release()
    
    # 读取预估计的背景图像（路径为data目录下的bg_estimated.jpg）
    bg = cv2.imread(str(Path("data")/"bg_estimated.jpg"))
    
    # 断言检查：确保帧和背景图像都成功读取，否则提示错误信息
    # 防止后续处理因数据缺失而报错
    assert ok and bg is not None, "请先完成任务1，或放置 data/room.mp4 与 data/bg_estimated.jpg"
    
    # 对视频帧进行预处理：
    # 1. 从BGR格式转为灰度图（减少计算量，简化处理）
    # 2. 应用5x5的高斯模糊（平滑图像，减少高频噪声干扰）
    g1  = cv2.GaussianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (5,5), 0)
    
    # 对背景图像进行同样的预处理（保持处理方式一致，确保差分有效性）
    gbg = cv2.GaussianBlur(cv2.cvtColor(bg,     cv2.COLOR_BGR2GRAY), (5,5), 0)
    
    # 计算视频帧与背景图像的灰度差分（获取两图的差异区域）
    # 绝对差分能有效突出前景目标（与背景不同的区域）
    diff = cv2.absdiff(g1, gbg)
    
    # 对差分结果进行二值化处理：
    # - 阈值设为28，像素值超过28的区域视为前景（设为255，白色）
    # - 低于等于28的区域视为背景（设为0，黑色）
    # 得到初始掩码mask0
    _, mask0 = cv2.threshold(diff, 28, 255, cv2.THRESH_BINARY)
    
    # 定义形态学操作的结构元素：5x5的椭圆形核
    # 椭圆形核在处理曲线边缘时效果更自然，适合大多数场景
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    
    # 对初始掩码进行形态学优化：
    # 1. 先开运算（MORPH_OPEN）：去除小面积噪点（如孤立的亮点）
    # 2. 再闭运算（MORPH_CLOSE）：填充前景区域内的小空洞，使掩码更完整
    mask = cv2.morphologyEx(cv2.morphologyEx(mask0, cv2.MORPH_OPEN, kernel), cv2.MORPH_CLOSE, kernel)
    
    # 返回处理后的视频帧和优化后的前景掩码
    return frame, mask

# 调用函数准备演示数据
frame_demo, mask_demo = prepare_demo()
# 提示用户数据准备完成
print("演示帧与掩码就绪。")
```


### 任务 2：**静态背景差分**
- 读取 `bg_estimated.jpg` 与视频逐帧做差，二值化获得前景掩码；
- 保存 5 张关键帧（含原图、差分、掩码、叠加预览）。

```py
def diff_mask(frame, bg, thr=30, kernel_size=5):
    """
    计算视频帧与背景图像的差异，并生成优化后的前景掩码
    参数:
        frame: 输入的视频帧（BGR格式）
        bg: 背景图像（BGR格式）
        thr: 二值化阈值，默认30，用于区分前景和背景
        kernel_size: 形态学操作的结构元素大小，默认5
    返回:
        m: 优化后的前景掩码（二值图像，255表示前景，0表示背景）
    """
    # 将输入帧和背景图从BGR格式转为灰度图
    # 目的：减少通道数，降低计算复杂度，简化后续差异计算
    g1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    
    # 计算灰度图的绝对差分
    # 作用：突出两图中像素值差异明显的区域（即可能的前景目标）
    d = cv2.absdiff(g1, g2)
    
    # 对差分结果进行二值化处理
    # 参数说明：thr为阈值，超过该值的像素设为255（前景），否则设为0（背景）
    # 目的：将连续的差异值转换为离散的二值掩码，明确区分前景和背景
    _, m = cv2.threshold(d, thr, 255, cv2.THRESH_BINARY)
    
    # 创建椭圆形结构元素，用于后续形态学操作
    # 椭圆形核在处理边缘时更平滑，适合大多数自然场景的前景提取
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    
    # 先进行开运算（去除小面积噪点），再进行闭运算（填充前景中的小空洞）
    # 开运算：消除孤立的小亮点，减少噪声干扰
    # 闭运算：填充前景区域内的小孔洞，使前景目标更完整
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, kernel)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, kernel)
    
    # 返回优化后的前景掩码
    return m
```

```py
# 创建视频捕获对象，从指定路径读取视频文件
cap = cv2.VideoCapture(video_path)

# 获取视频帧的高度(H)和宽度(W)，用于后续图像处理和保存
H, W = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# 用于计数成功保存的可视化图像数量
sampled = 0

# 生成5个均匀分布的帧索引（从0到视频总帧数-1），用于采样关键帧
# np.linspace确保帧在视频中均匀分布，dtype=int转换为整数索引
for i in np.linspace(0, max(0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1), 5, dtype=int):
    # 设置视频捕获对象的当前帧位置为索引i，定位到要采样的帧
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(i))
    
    # 读取当前帧，ok为是否读取成功的标志，f为读取到的帧数据
    ok, f = cap.read()
    if not ok:  # 如果读取失败，跳过当前帧
        continue
    
    # 调用diff_mask函数生成前景掩码：基于当前帧与背景的差异，应用阈值和形态学处理
    m = diff_mask(f, bg, thr=28, kernel_size=5)
    
    # 创建原始帧的副本作为覆盖层，用于标记前景区域
    overlay = f.copy()
    # 将掩码中不为0的区域（前景）标记为绿色(0,255,0)，便于可视化前景
    overlay[m>0] = (0,255,0)
    
    # 构建可视化网格：水平拼接4个图像
    # 1. 原始帧(f)
    # 2. 灰度差分图（转换为BGR格式以保持与其他图像通道一致）
    # 3. 前景掩码（转换为BGR格式）
    # 4. 标记了前景的覆盖层
    grid = np.hstack([
        f, 
        cv2.cvtColor(cv2.absdiff(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), 
                                cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)), 
                   cv2.COLOR_GRAY2BGR),  # 差分图转BGR
        cv2.cvtColor(m, cv2.COLOR_GRAY2BGR),  # 掩码转BGR
        overlay
    ])
    
    # 保存拼接后的网格图像到OUT目录，文件名包含采样计数
    cv2.imwrite(str(OUT/f"diff_vis_{sampled}.jpg"), grid)
    sampled += 1  # 递增采样计数

# 释放视频捕获资源，避免内存占用
cap.release()

# 打印成功保存的可视化图像数量
print("已保存关键帧可视化：", sampled, "张")
```


### 子任务 3：**轮廓筛选 + 最小外接矩形（minAreaRect）**实现目标检测和跟踪
- 在每帧掩码上找外部轮廓，取**最大面积**轮廓；
- 使用 `cv2.minAreaRect` 得到矩形、中心、宽高、旋转角；
- 在视频上绘制轮廓、矩形、中心点并导出 `outputs/detect_vis.mp4`。


```py
# 定义视频编码器，使用mp4v格式（支持MP4文件输出）
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# 创建视频捕获对象，读取输入视频
cap = cv2.VideoCapture(video_path)

# 获取视频的帧率(FPS)，若获取失败则默认使用20.0
fps = cap.get(cv2.CAP_PROP_FPS) or 20.0

# 创建视频写入对象，用于保存处理后的可视化视频
# 参数：输出路径、编码器、帧率、视频宽高(W,H)
out = cv2.VideoWriter(str(OUT/"detect_vis.mp4"), fourcc, fps, (W,H))

# 初始化列表，用于存储目标跟踪信息
centers = []    # 存储目标中心坐标 (cx, cy)
rect_wh = []    # 存储目标外接矩形的宽高 (w, h)
angles = []     # 存储目标外接矩形的旋转角度 theta

# 循环读取视频帧，直到所有帧处理完毕
while True:
    # 读取一帧视频，ok为读取成功标志，frame为帧数据
    ok, frame = cap.read()
    if not ok:  # 若读取失败（如到达视频末尾），退出循环
        break
    
    # 调用diff_mask函数生成前景掩码，提取视频帧与背景的差异区域
    m = diff_mask(frame, bg, thr=28, kernel_size=5)
    
    # 从掩码中查找轮廓（目标边界）
    # cv2.RETR_EXTERNAL：只保留最外层轮廓；cv2.CHAIN_APPROX_SIMPLE：简化轮廓点
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 若未检测到轮廓，直接将原始帧写入输出视频并继续下一帧
    if len(cnts) == 0:
        out.write(frame)
        continue
    
    # 选择面积最大的轮廓（假设最大轮廓为目标）
    cnt = max(cnts, key=cv2.contourArea)
    
    # 计算轮廓的最小外接矩形（旋转矩形）
    # 返回值格式：((中心x, 中心y), (宽w, 高h), 旋转角度theta)
    rect = cv2.minAreaRect(cnt)
    
    # 计算矩形的四个顶点坐标（转换为整数用于绘制）
    box = cv2.boxPoints(rect).astype(int)
    
    # 提取矩形中心坐标（转换为整数）
    cx, cy = int(rect[0][0]), int(rect[0][1])
    # 提取矩形宽高和旋转角度
    w, h = rect[1]
    theta = rect[2]
    
    # 将目标信息存入对应列表，用于后续分析
    centers.append((cx, cy))
    rect_wh.append((w, h))
    angles.append(theta)
    
    # 创建原始帧的副本，用于绘制可视化元素（避免修改原图）
    vis = frame.copy()
    
    # 绘制最小外接矩形（绿色，线宽2）
    cv2.drawContours(vis, [box], 0, (0, 255, 0), 2)
    # 绘制目标中心（蓝色圆点，半径3，填充）
    cv2.circle(vis, (cx, cy), 3, (255, 0, 0), -1)
    # 绘制目标轮廓（红色，线宽1）
    cv2.drawContours(vis, [cnt], -1, (0, 0, 255), 1)
    # 在帧上添加文本信息：中心坐标、宽高、旋转角度
    cv2.putText(vis, 
                f"center=({cx},{cy}) w={w:.1f} h={h:.1f} ang={theta:.1f}", 
                (10, 20),                  # 文本位置（左上角）
                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                0.5,                       # 字体大小
                (0, 0, 0),                 # 文本颜色（黑色）
                1)                         # 线宽
    
    # 将绘制了目标信息的可视化帧写入输出视频
    out.write(vis)

# 释放视频捕获资源和视频写入资源，避免内存泄漏
cap.release()
out.release()

# 显示生成的检测视频（嵌入模式）
display(Video(str(OUT/"detect_vis.mp4"), embed=True))

# 提示视频导出完成
print("检测视频已导出。")
```


### 扩展任务：**对比 OpenCV 背景建模器**
- 分别使用 `cv2.createBackgroundSubtractorMOG2()` 与 `KNN()`进行背景建模；
- 与静态背景差分的结果对比，给出定量（覆盖率、连通域数）和定性（可视化）评估。
