原文来自：[Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)

由于我们难以提取高层次、抽象的特征来表达复杂表示，因此使用机器学习。

## Tensor 的基本计算

### 初始化 Tensor

直接创建

```python
shape = (2, 3, )
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
```

从其它数据类型创建

```python
data = [[1, 2],[3, 4]]
# 直接从数据创建
x_data = torch.tensor(data)

# 从 Numpy 创建
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
```

从 Tensor 创建

```python
x_ones = torch.ones_like(x_data) # 维度相同的全 1 矩阵
x_rand = torch.rand_like(x_data, dtype=torch.float) # 改变 x_data 的数据类型，并生成同维度的随机 Tensor
```

### Tensor 的相关操作

常用 `my_tensor.shape`, `my_tensor.dtype`, `my_tensor.device` 查看其属性

改变形状 

```python
x2 = x1.view(2, 3)
x1.reshape_(2, 3)   # 用 none 或者 -1 指定自动计算的维度
```

!!! warning-box "注意"
    原地操作虽然会节省许多空间，但是由于会立刻清除历史记录所以在计算导数时可能会有问题，因此不建议使用

计算 `+ - * / @`

> 具体相关计算见 [PyTorch 文档](https://docs.pytorch.org/docs/stable/torch.html) 和 [torch.Tensor API](http://pytorch.org/docs/master/tensors.html)


## Autograd 自动求导

来看一个简单的示例，我们从torchvision加载一个预先训练好的resnet18模型，接着创建一个随机数据tensor来表示一有3个通道、高度和宽度为64的图像，其对应的标签初始化为一些随机值。

```python
import torch, torchvision
model = torchvision.models.resnet18(weights=True)
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1, 1000)

prediction = model(data) # 前向传播

loss = (prediction - labels).sum()
loss.backward() # 反向传播
```

调用.backward()会自动计算所有梯度。此张量的梯度将累积到.grad属性中。

接着，我们加载一个优化器，在本例中，SGD的学习率为0.01，momentum 为0.9。我们在优化器中注册模型的所有参数。调用`.step()`来执行梯度下降，优化器通过存储在`.grad`中的梯度来调整每个参数。

```python
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
optim.step() #梯度下降
```

=== "手动求导 (手写一个)"
    ```python
    # Training Data
    x_data = [1.0, 2.0, 3.0]
    y_data = [2.0, 4.0, 6.0]
    
    w = 1.0  # a random guess: random value
    
    # our model forward pass
    def forward(x):
        return x * w
    
    # Loss function
    def loss(x, y):
        y_pred = forward(x)
        return (y_pred - y) * (y_pred - y)
    
    # compute gradient
    def gradient(x, y):  # d_loss/d_w
        return 2 * x * (x * w - y)
    
    # Before training
    print("Prediction (before training)",  4, forward(4))
    
    # Training loop
    for epoch in range(10):
        for x_val, y_val in zip(x_data, y_data):
            # Compute derivative w.r.t to the learned weights
            # Update the weights
            # Compute the loss and print progress
            grad = gradient(x_val, y_val)
            w = w - 0.01 * grad
            print("\tgrad: ", x_val, y_val, round(grad, 2))
            l = loss(x_val, y_val)
        print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))
    
    # After training
    print("Predicted score (after training)",  "4 hours of studying: ", forward(4))
    ```

=== "自动求导"
    ```python {highlight=[23]}
    import torch
    
    x_data = torch.tensor([1.0, 2.0, 3.0])
    y_data = torch.tensor([2.0, 4.0, 6.0])
    w = torch.tensor([1.0], requires_grad=True)
    
    # our model forward pass
    def forward(x):
        return x * w
    
    # Loss function
    def loss(y_pred, y_val):
        return (y_pred - y_val) ** 2
    
    # Before training
    print("Prediction (before training)",  4, forward(4).item())
    
    # Training loop
    for epoch in range(10):
        for x_val, y_val in zip(x_data, y_data):
            y_pred = forward(x_val) # 1) Forward pass
            l = loss(y_pred, y_val) # 2) Compute loss
            l.backward() # 3) Back propagation to update weights
            print("\tgrad: ", x_val, y_val, w.grad.item())
            w.data = w.data - 0.01 * w.grad.item()
    
            # Manually zero the gradients after updating weights
            w.grad.data.zero_()
    
        print(f"Epoch: {epoch} | Loss: {l.item()}")
    
    # After training
    print("Prediction (after training)",  4, forward(4).item())
    ```