**实验内容**：给定一段静态背景的目标运动视频，通过背景建模获取场景的背景图像（不包含目标），并进行图像去噪

视频由一系列连续的图像帧组成

视频写入：声明保存路径，格式，帧率，分辨率

静态视频的背景建模

**均值法**：在一段时间内取N帧视频图像序列，对于每个像素点，在这N帧图像在此点均值为该点背景图像中的灰度值

**中值法**：在一段时间内取N帧视频图像序列，对于每个像素点，在这N帧图像在此点处的N个像素值按从小到大排序，然后将排序后的中值作为该点背景图像中的灰度值

---

## 读取视频并保存帧

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

## 写入并保存视频

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

## 图像直方图

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

## 遍历像素

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

## 均值法背景建模

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

## 中值法背景建模

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