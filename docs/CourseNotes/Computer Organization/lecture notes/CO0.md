## 十进制小数转浮点数

**单、双精度的格式：**

| 浮点数类型 | 符号位 | 指数 | 尾数 | bias |
| ---------- | ------ | ---- | ---- | ---- |
| 单精度     | 1      | 8    | 23   | 127  |
| 双精度     | 1      | 11   | 52   | 1023 |

特殊情况：

| 类型       | 符号位 | 指数      | 尾数 | 说明                                            |
| ---------- | ------ | --------- | ---- | ----------------------------------------------- |
| 0          | x      | 0         | 0    | 符号位决定是+0 还是-0                           |
| 非规格化数 | x      | 0         | 非 0 | 此时隐含的前导位是 0 而非 1                     |
| 无穷大     | x      | 1111_1111 | 0    | 符号位决定是 $+\infty$ 还是 $-\infty$           |
| NaN        | x      | 1111_1111 | 非 0 | NaN 包括 0.0/0.0，$\sqrt{-1}$，$\infty -\infty$ |

**十进制小数转浮点数的过程：**

判断符号位 --> 整数部分、小数部分转为二进制 --> 移动小数点至 1.xx --> 移动小数点的数值 + bias 得到指数 --> 指数前补 0、尾数后补 0，补到相应位数 --> 组合成浮点数

整数转二进制：除 2 取余，从下到上排序  
小数转二进制：乘 2 取整，从上到下排序

**十进制小数加法：**

分别转为二进制 --> 指数对齐，统一化为更大的指数 --> 尾数相加 --> 规范化为 1.xx 格式 --> 去点隐含 1，判断舍入误差 --> 判断溢出和特殊值 --> IEEE 754 表示

指数对齐时，指数小的数的尾数需右移，用 guard, round, sticky 三个位保留，其中 G 和 R 为直接右移得到，S 为后面所有位的或。

判断舍入：GRS 位表示的数大于等于 0.5 则加一，小于 0.5 则不加一。（示例为 0.5\*ulp，其中 ulp 为保留的浮点数最后一位表示的数值。）

| 情况                  | 条件                          | 处理方式                |
| :-------------------- | :---------------------------- | :---------------------- |
| 指数上溢（overflow）  | 规格化后指数 > 254            | 结果置为 ±∞             |
| 指数下溢（underflow） | 规格化后指数 < 1              | 结果置为 ±0 或 次正规数 |
| 结果为 0              | 符号相反、尾数相等 → 完全抵消 | 结果 ±0                 |
| 无穷参与运算          | ±∞ ± 有限数 / ±∞ ± ±∞         | 视情况得 ±∞ 或 NaN      |
| NaN（非数）参与运算   | 操作数有 NaN 或 ∞–∞           | 结果为 NaN              |

指数下溢情况：

若 E 仍在 [–22, 0] 范围：尾数右移（产生次正规数 subnormal）：`E'=0, M'=原尾数右移(1–E)位`，保持符号不变。  
若 E<0 太多：尾数右移到全 0，结果为 ±0

无穷大情况：

| 操作                  | 结果 |
| :-------------------- | :--- |
| `(+∞) + (有限数)`     | +∞   |
| `(–∞) + (有限数)`     | –∞   |
| `(+∞) + (–∞)`         | NaN  |
| `(±∞) + (±∞)`（同号） | ±∞   |

## 本地编译和转化

C 代码转 RISCV：

```bash
riscv64-unknown-elf-gcc -O1 -c -march=rv64gc -mabi=lp64d ex.c -o ex.o && riscv64-unknown-elf-objdump -d ex.o
```

十进制小数转单精度浮点数：

```bash
python3 -q

import struct
x=-20.796875
bits=struct.unpack('>I', struct.pack('>f', x))[0]
print(f"res:{bits:032b}")

exit()
```

十进制小数转双精度浮点数：

```bash
python3 -q

import struct
x=-20.796875
bits=struct.unpack('>Q', struct.pack('>d', x))[0]
print(f"res:{bits:064b}")

exit()
```

## 不同数据类型的字节

| 指令  | 全称                   | 加载宽度 | 扩展方式           | 适用数据类型（C 语言示例）                       | 典型用途                              | 是否需地址对齐   |
| ----- | ---------------------- | -------- | ------------------ | ------------------------------------------------ | ------------------------------------- | ---------------- |
| `lb`  | Load Byte              | 1 字节   | 符号扩展           | `signed char`, `int8_t`                          | 读取有符号小整数（如 -5 存为 `char`） | 否（任意地址）   |
| `lbu` | Load Byte Unsigned     | 1 字节   | 零扩展             | `char`（文本/ASCII）, `unsigned char`, `uint8_t` | 字符串、字节流、像素值、二进制数据    | 否（任意地址）   |
| `lh`  | Load Halfword          | 2 字节   | 符号扩展           | `short`, `int16_t`                               | 读取有符号 16 位整数                  | 是（2 字节对齐） |
| `lhu` | Load Halfword Unsigned | 2 字节   | 零扩展             | `unsigned short`, `uint16_t`                     | 无符号 16 位整数（如端口号）          | 是（2 字节对齐） |
| `lw`  | Load Word              | 4 字节   | 无扩展（直接加载） | `int`, `float`, 指针（RV32）                     | 通用 32 位整数或单精度浮点数          | 是（4 字节对齐） |
| `ld`  | Load Doubleword        | 8 字节   | 无扩展（直接加载） | `long`（RV64）, `double`, 指针（RV64）           | 64 位整数或双精度浮点数（仅 RV64）    | 是（8 字节对齐） |

## 指令执行的延迟

!!! examples "题目"

    4.7 本练习中的问题假设用于实现处理器数据通路的逻辑模块具有以下延迟：

    | I-Mem / D-Mem | Register File | Mux   | ALU    | Adder  | Single gate | Register Read | Register Setup | Sign extend | Control |
    | ------------- | ------------- | ----- | ------ | ------ | ----------- | ------------- | -------------- | ----------- | ------- |
    | 250 ps        | 150 ps        | 25 ps | 200 ps | 150 ps | 5 ps        | 30 ps         | 20 ps          | 50 ps       | 50 ps   |

    “Register read”是指在时钟上升沿之后，新寄存器值出现在输出端所需的时间。此值仅适用于 PC（程序计数器）。“Register setup”是指寄存器的数据输入必须在时钟上升沿之前保持稳定的最短时间。该值同时适用于 PC 和寄存器文件。

    4.7.1 [5] <§4.4> R 型指令的延迟是多少？（即：为确保该指令正确执行，时钟周期至少需要多长？）

    4.7.2 [10] <§4.4> `ld` 指令的延迟是多少？

    4.7.3 [10] <§4.4> `sd` 指令的延迟是多少？

    4.7.4 [5] <§4.4> `beq` 指令的延迟是多少？

    4.7.5 [5] <§4.4> I 型指令的延迟是多少？

    4.7.6 [5] <§4.4> 此 CPU 所需的最小时钟周期是多少？

- I-Mem：取指时间
- D-Mem：内存读写时间
- Register File：寄存器文件读取时间
- Mux：多选器时间
- ALU
- Adder
- Single Gate：（1）控制信号，branch && zero （2）跳转地址，立即数左移
- Register Read：PC 读取（寄存器文件是异步读、同步写，这里只对 PC 读取有延迟）
- Register Setup：寄存器写的时间，对 PC 和寄存器文件都有延迟（因为都是同步写）
- Sign extend：Imm Gen 模块，将 32 位立即数扩展为 64 位所需的时间
- Control：控制信号生成时间（同步进行）

R 型指令的延迟是多少？

$$
\begin{align*}
Time=\,&RegRead + IMem + RegFile \\
&+ MUX(\text{decide the second input of ALU}) \\
&+ ALU + MUX(\text{decide the destination of ALU result}) + RegSetup\\
\end{align*}
$$

`ld` 指令的延迟是多少？

$$
\begin{align*}
Time=\,&RegRead + IMem +
\begin{cases}RegFile \\ SignExtend\end{cases}\\
&+ MUX(\text{input of ALU})\\
&+ ALU + DMem(\text{read from mem})\\
&+ MUX(\text{destination of mem data}) + RegSetup\\
&=950ps\end{align*}
$$

`sd` 指令的延迟是多少？

$$
\begin{align*}
Time=\,&RegRead + IMem +
\begin{cases}RegFile \\ SignExtend\end{cases}\\
&+ MUX + ALU + MUX\end{align*}
$$

sd 中存储到 MEM 后没有输出 data，后面不用加 MUX

`beq` 指令的延迟是多少？

$$
\begin{align*}
Time=\,&RegRead + IMem +
\begin{cases}RegFile \\ SignExtend\end{cases}\\
&+ \begin{cases}SingleGate+Adder(\text{new PC}) \\ MUX+ALU(\text{compare rs1 and rs2})+SingleGate(\text{shift\,left\,1})\end{cases}\\
&+ MUX+Setup\end{align*}
$$

I 型指令的延迟是多少？

略。

此 CPU 所需的最小时钟周期是多少？

最小时钟周期 = 最大的指令执行时间（单周期 CPU）

950ps
