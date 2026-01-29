import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# 定义激活函数
def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def gelu(x):
    # 精确公式用 scipy.special.erf 也可以，但这里用近似：
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

def silu(x):
    return x / (1 + np.exp(-x))

x = np.linspace(-5, 5, 500)

y_elu = elu(x)
y_gelu = gelu(x)
y_silu = silu(x)

# 创建3个子图并排
fig = make_subplots(rows=1, cols=3, subplot_titles=("ELU", "GELU", "SiLU"))

fig.add_trace(go.Scatter(x=x, y=y_elu, name='ELU'), row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=y_gelu, name='GELU'), row=1, col=2)
fig.add_trace(go.Scatter(x=x, y=y_silu, name='SiLU'), row=1, col=3)

fig.update_layout(height=400, width=900, showlegend=False, title_text="Other Activation Functions")

# 输出成HTML文件
pio.write_html(fig, 'activation_functions.html', full_html=False, include_plotlyjs='cdn')
