## MLP (多层神经网络) 的 PyTorch 实现

```python
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.l1 = nn.Linear(784, 520)
        self.l2 = nn.Linear(520, 320)
        self.l3 = nn.Linear(320, 240)
        self.l4 = nn.Linear(240, 120)
        self.l5 = nn.Linear(120, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)
```

## CNN (卷积神经网络)

在PyTorch中，卷积层有 Conv1d、Conv2d、Conv3d， 这三个分别对应着一维卷积、二维卷积、三维卷积，然后它们的输入数据的格式分别是  
- Conv1d的输入数据为 (minibatch, in_chanels, iW)
- Conv2d的输入数据为 (minibatch, in_chanels, iH, iW)
- Conv3d的输入数据为 (minibatch, in_chanels, iT, iH, iW)

=== "直接构建卷积"
    ```python
    # 使用PyTorch的函数来进行卷积操作
    
    x = Variable(torch.Tensor(range(9)))
    x=x.view(1,1,3,3)
    weights = Variable(torch.Tensor([0,1,2,3]))
    weights = weights.view(1,1,2,2)
    bias = Variable(torch.Tensor([1]))
    
    y=F.conv2d(x, weights,bias, padding=0)
    ```

=== "用 `nn` 构建卷积模型"
    ```python
    x = Variable(torch.Tensor(range(9)))
    x = x.view(1,1,3,3)
    
    weights = torch.Tensor([0,1,2,3]).view(1,1,2,2)
    weights = torch.nn.Parameter(weights)
    bias = torch.nn.Parameter(torch.Tensor([1]))
    
    # model
    model = torch.nn.Conv2d(in_channels=x.data.size()[1], out_channels=x.data.size()[1], kernel_size=(2,2), stride=1 )
    
    # 设置该卷积层过滤器形状 (out_channels, in_channels, kernel_size[0], kernel_size[1]) 和 权重数值
    model.weight = weights
    model.bias = bias
    
    # 求解X
    y = m(x)
    ```

模型构建：

```python
#%%
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 3x3 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 6 * 6, 120)  # 6*6 from image dimension 
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
```

该模型为 

```
Net(
  (conv1): Conv2d(1, 6, kernel_size=(3, 3), stride=(1, 1))
  (conv2): Conv2d(6, 16, kernel_size=(3, 3), stride=(1, 1))
  (fc1): Linear(in_features=576, out_features=120, bias=True)
  (fc2): Linear(in_features=120, out_features=84, bias=True)
  (fc3): Linear(in_features=84, out_features=10, bias=True)
)
```

!!! remarks "注意"
    `torch.nn`只支持小批量输入,整个torch.nn包都只支持小批量样本,而不支持单个样本
例如,`nn.Conv2d`将接受一个4维的张量,每一维分别是$nSamples\times nChannels\times Height\times Width$(样本数*通道数*高*宽).
如果你有单个样本,只需使用`input.unsqueeze(0)`来添加其它的维数.

## Pooling (池化)

不做介绍

## 应用：AlexNet 的构建

```python
class AlexNet(nn.Module):

    def __init__(self, num_classes: int = 1000) -> None:
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
```