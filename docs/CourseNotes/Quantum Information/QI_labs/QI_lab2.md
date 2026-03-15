## 描述量子态

首先`import qutip`或`from qutip import basis`

### 定义标准基矢、内积

`basis(n,i)`表示n维空间中第i个标准基矢，默认为 $|i\rangle$（第i个值为1、其余为0的单位向量）。二维量子态的基矢定义为：

```py
H = basis(2,0)  # |0>，水平方向
V = basis(2,1)  # |1>，竖直方向
P45 = 1 / np.sqrt(2) * (H + V)  # +45度偏振
M45 = 1 / np.sqrt(2) * (H - V)  # -45度偏振
L = 1 / np.sqrt(2) * (H - 1.j * V)  # 圆偏振基，左旋
R = 1 / np.sqrt(2) * (H + 1.j * V)  # 圆偏振基，右旋
```

!!! normal-comment "为什么圆偏振基能表示旋转？"

    光是横波，假设光传播方向为z，则光的电场在xy平面，可分解为 (Ex,Ey)。

    实际中电场振动为正余弦函数。为方便计算，用复数 $e^{i\omega t}$ 表示，再取实部得到正余弦，其中的 $\omega t$ 表示相位。而 $i=e^{i\pi/2}$，因此乘i等价于相位加 $\pi/2$。

    当电场方向旋转时，Ex和Ey分别为sin和cos，即相位相差90度。圆偏振基（右旋为例：$|R\rangle=\frac{1}{\sqrt{2}} (|H\rangle+i|V\rangle)$）满足这一特点，表示电场方向随时间匀速旋转。


对两个ket A和B，用`A.dag()*B`（dag表达dagger，厄米共轭，将ket转为bra）或`A.overlap(B)`（内积表示B在A方向上分量的大小，其平方为测量B得到结果A的概率，因此表示两个量子态的重叠程度）表示内积。

投影算符为ket和对应bra的内积，可用dag()表示：`Pa=A*A.dag()`。

### 测量量子态

```py
# 态s2在态s1方向的振幅，返回结果的平方为概率
def probability_amplitude(s1, s2):
    return s1.unit().overlap(s2.unit())

# 测量s2、得到结果为s1的概率
def measurement_probability(s1, s2):
    return abs(probability_amplitude(s1.unit(), s2.unit()))**2

```

### 量子类与实例

```py
class Photon:
    def __init__(self, state):
        self._state = state  # 设定状态
        
    # 以m_basis为基测量，返回测量结果为第几个基态
    def measure(self, m_basis):   
        if np.random.rand() < measurement_probability(self._state, m_basis[0]):  # 用随机数模拟概率
            self._state = m_basis[0]  # 量子态坍缩
            return 0  # 返回测量值
        else:
            self._state = m_basis[1]
            return 1
    
    def __repr__(self):
        return("{}, {}".format(self._state[0], self._state[1]))

```

创建实例测试：

```py
basisHV = [H, V]
p = Photon(P45)
print(p.measure(basisHV))  # 出现0和1的概率分别为50%
```


## 量子密钥

### 量子密钥分发原理

最经典的协议为BB84 protocol。设Alice要将信号发送给Bob，用光子偏振代表0和1，有H/V、P/M两组基。Bob随机选择一组基测量，如果选对则测量正确、选错则有50%概率正确。发送完后，两人通过普通通信信道（可以被窃听）核对每个光子的基，Bob只保留基相同的位。由此得到双方都知道、但其他人不知道的密钥（一组0/1值）。

_为什么能避免窃听？_ 假设Eve想要窃听，需要在中间测量光子、再重新发送给Bob。Eve只能随机选择基，如果选错，则有50%可能性重发错误。但如果Bob对重发的光子选择正确的基，则测量结果与Alice发送的不同。后续两个抽查一部分比特时，会发现错误率升高（约25%），即说明有人窃听。

### 简要实现

```py
# 准备两组基
basisHV = [H, V]
basisPM45 = [P45, M45]
modes = [basisHV, basisPM45]

# 定义函数：随机生成nb位比特
def bit_generate(nb = 1):
    return np.random.randint(0,2,nb)

# Alice随机生成1000位密钥
nbits = 1000
Alice_bits = bit_generate(nbits)

# 定义函数：随机选择测量的基
def mode_select():
    return np.random.randint(0,2)

# Alice随机选择基并发送
Alice_modes = []
Alice_prepared = []
for i in range(len(Alice_bits)):
    mode = mode_select()
    Alice_modes.append(mode)
    Alice_prepared.append(Photon(modes[mode][Alice_bits[i]]))

# Bob接收Alice的信息
Bob_received = Alice_prepared.copy()
Alice_prepared.clear()

# Bob随机选择基并测量
Bob_modes = []
Bob_bits = []
for p in Bob_received:
    mode = mode_select()
    Bob_modes.append(mode)
    Bob_bits.append(p.measure(modes[mode]))

# Alice和Bob核对选择的基，保留基相同的位
keys = []
for am, bm, ab, bb in zip(Alice_modes, Bob_modes, Alice_bits, Bob_bits):
    if (am == bm):
        assert ab == bb
        keys.append(ab)

# 打印得到的密钥
print ('Sifted keys:', len(keys))
print(keys)
```

