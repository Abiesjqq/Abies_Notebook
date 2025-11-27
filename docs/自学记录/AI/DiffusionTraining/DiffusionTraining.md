
扩散模型的训练 (SVD 和 SV4D 的训练 (training) 流程)

这里使用的库是 [generative-models](https://github.com/Stability-AI/generative-models)

## 先看懂 `main.py`  (一个示例)

### 数据流: Lightning 流程

#### 1. 从构建好的 DataModule / Dataset 读取文件

组成字典，例如 

```python
batch = {
  "image":    [B, 3, H, W]      # 当前要预测的目标帧
  "context":  [B, T_ctx, 3, H, W]  # 输入视角视频（未来做条件）
  "camera":   [B, ..., 3]       # 相机外参编码
  ...
}
```

#### 读取模型

这里从 cfg 文件中读取模型

```python
model = instantiate_from_config(config.model)   # DiffusionEngine
```

这里使用 `DiffusionEngine` 库 (`/sgm/models/diffusion.py`). 改库继承自 `pytorch_lightning.LightningModule`: (注意看这里的返回值)

```python
class DiffusionEngine(pl.LightningModule):

    def __init__(...):

        super().__init__()
        ...
        self.optimizer_config = default(
            optimizer_config, {"target": "torch.optim.AdamW"}
        )   # 优化器配置
        model = instantiate_from_config(network_config)
        self.model = get_obj_from_str(default(network_wrapper, OPENAIUNETWRAPPER))(
            model, compile_model=compile_model
        )   # 加载初始化 model
        # 去噪器
        self.denoiser = instantiate_from_config(denoiser_config)
        self.sampler = (
            instantiate_from_config(sampler_config)
            if sampler_config is not None
            else None
        )
        ...     # 等等训练相关参数

    def training_step(self, batch, batch_idx):
        loss, loss_dict = self.shared_step(batch)
        self.log_dict(loss_dict, ...)  # 给 logger
        return loss

    def shared_step(self, batch):
        x = self.get_input(batch)      # 从 batch 里取输入
        loss, loss_dict = self(x, batch)
        return loss, loss_dict

    def forward(self, x, batch=None):
        loss = self.loss_fn(self.model, self.denoiser, self.conditioner, x, batch)
        return loss
```

`self.model`：真正的 UNet / VideoUNet，不过外面套了一层 `OPENAIUNETWRAPPER`（比如统一 forward 接口、可选 compile）。  
`self.denoiser`：EDM 风格的封装（负责根据 $\sigma$ 做 scaling、skip 连接）。  
`self.conditioner`：把 batch 里的条件（文本、camera、context……）封装成统一结构。  
`self.first_stage_model`：在 _init_first_stage 里构造，是 VAE/AE 或 Identity，用来在 latent 空间工作。  
`self.loss_fn`：真正定义「怎么采样噪声 $\sigma$，怎么算 target，怎么加权」的 loss 函数（例如 StandardDiffusionLoss 的某个版本）。  
`self.sampler`：采样时（推理）用的时间步调度器（ODE/SDE solver）。  
`self.input_key`：决定从 batch 的哪个 key 取“图像数据”（默认 "jpg"，你现在改成了 "image" / "video"）。

数据从上面进入模型内部

#### 模型内数据流动

```python
def shared_step(self, batch: Dict) -> Any:
    # batch 可能能有不同的 key 用来取数据。这里返回指定的 key 对应的数据
    # 返回的一般还是 [B, C, H, W] 或 [B, C, T, H, W] (视频)
    x = self.get_input(batch)
    # 把数据 x 变成 latent space
    # 返回一个乘以 scale_factor 的 latent space
    x = self.encode_first_stage(x)
    batch["global_step"] = self.global_step
    # 调用 forward
    loss, loss_dict = self(x, batch)
    return loss, loss_dict
```

```python
def forward(self, x, batch):
    loss = self.loss_fn(self.model, self.denoiser, self.conditioner, x, batch)
    loss_mean = loss.mean()
    loss_dict = {"loss": loss_mean}
    # 返回 loss
    return loss_mean, loss_dict
```

具体在 `self.loss_fn` 中，  
从 `batch` 和 `conditioner` 中拿到条件 cond  
--> 采样 $\sigma$ 和噪声 $\varepsilon$  
--> 构造 noisy latent `z_noisy`    
--> 用 `denoiser(self.model, z_noisy, σ, cond, ...)` 得到预测；  
--> 和 target 做 MSE / weighted MSE

`training_step(self, batch, batch_idx)`: 把 loss 交给 Lightning + 记录日志 (待研究，听说这里是用的 wandb，不是 tensorboard)

#### 超参

**EMA（指数滑动平均权重）** 在 `on_train_batch_end` 中，每个 batch 后更新一次 EMA 权重 (没怎么看懂，到要用了看)

```python
if self.use_ema:
    self.model_ema(self.model)
```

**Optimizer + Scheduler** 典中典，

```python
def configure_optimizers(self):
    lr = self.learning_rate
    params = list(self.model.parameters())
    for embedder in self.conditioner.embedders:
        if embedder.is_trainable:
            params = params + list(embedder.parameters())
    opt = self.instantiate_optimizer_from_config(params, lr, self.optimizer_config)
    if self.scheduler_config is not None:
        scheduler = instantiate_from_config(self.scheduler_config)
        scheduler = [{"scheduler": LambdaLR(opt, lr_lambda=scheduler.schedule),
                      "interval": "step", "frequency": 1}]
        return [opt], scheduler
    return opt
```

可以调包括 U-Net、Conditioner、Embedder 在内的参数

**采样 `sample()`**

```python
@torch.no_grad()
def sample(self, cond, uc=None, batch_size=16, shape=None, **kwargs):
    # 采样高斯 randn
    randn = torch.randn(batch_size, *shape).to(self.device)

    # 用 denoiser 和 sampler 去噪
    denoiser = lambda input, sigma, c: self.denoiser(
        self.model, input, sigma, c, **kwargs
    )
    samples = self.sampler(denoiser, randn, cond, uc=uc)
    return samples
```

**`log_images` 可视化** 看结果用，不仔细看了

### 具体细节

#### VAE / AE: 编码到 latent

```python
# 预训练模型, no_grad
@torch.no_grad()
def encode_first_stage(self, x):
    # 分批次防止 OOM
    n_samples = default(self.en_and_decode_n_samples_a_time, x.shape[0])
    n_rounds = math.ceil(x.shape[0] / n_samples)
    all_out = []
    # autocast: 打开 AMP（自动混合精度）允许部分计算用 float16/bfloat16
    with torch.autocast("cuda", enabled=not self.disable_first_stage_autocast):
        # 调用 VAE 编码器
        for n in range(n_rounds):
            out = self.first_stage_model.encode(
                x[n * n_samples : (n + 1) * n_samples]
            )
            all_out.append(out)
    z = torch.cat(all_out, dim=0)
    z = self.scale_factor * z
    return z
```

#### `forward / loss_fn / denoiser`

显然 `loss_fn` 执行调用 `denoiser` 然后计算 loss.

```python
class Denoiser(nn.Module)
```

具体不做介绍