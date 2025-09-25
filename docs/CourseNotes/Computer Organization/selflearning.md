!!! warning-box "注意"

    仅自学用。

    但上课的ppt和md的一样。经实践，这里作为笔记的主要部分。

## Chap 01

Instruction set architecture 指令集

芯片制造：芯片设计，掩膜，硅切片成晶圆，光刻，测试，晶圆切片，封装  
？nm：两条线之间的最小距离

$$ \text{cost per die}=\frac{\text{cost per wafer}}{\text{dies per wafer}\times\text{yield}},\quad\text{dies per wafer}\approx\text{wafer area}/\text{die area}$$

$$\text{yield}=\frac{1}{(1+(\text{defects per area}\times\text{die area}/2))^2}$$

芯片面积越大，良率越低。

响应时间/执行时间（response time）：多久完成任务  
吞吐率（throughput）：单位时间内能完成的工作量  
对每个操作响应时间短，吞吐率大；吞吐率大不一定对每个的响应时间都短  
增加处理器，响应时间不一定提高（考虑单处理器），但吞吐率提高  
性能 performance=1/执行时间  
performance 必须基于同一个程序

真正的执行时间不只有 CPU 时间，还有 IO 等系统时间（这里先只考虑 CPU）

同步逻辑：同一个时钟驱动  
CPU 是同步逻辑

怎么计算 CPU 执行时间？  
CPU 有时钟周期，上升沿驱动。频率是时钟周期的倒数  
clock frequency = 1 / clock period  
CPU 时间 = 总共用了几个 CPU 时钟 \* 时钟周期 = 总共用了几个 CPU 时钟/时钟频率  
性能提高：减少时钟，提高频率，硬件设计时在 clock rate 和 cycle count 中 trade-off  
clock cycle = 指令数目 \* 每条时间多少个时钟数（CPI）  
指令数 IC（Instruction Count）  
CPU time = clock cycle \* clock cycle time = instruction count \* CPI / clock rate  
影响指令数：减少指令数，指令集（ISA），编译器  
CPI 由 CPU 决定，和指令的组成方式有关  
真正的 clock cycle = 每一种 CPI \*这种 CPI 的指令数 求和  
计算平均 CPI  
频率很难提高：功耗限制 -> 多核  
功耗 = 负载 \* 电压^2 \* 频率  
工艺越先进，电压越低，功耗越小（电压降低使频率增长没有导致功耗同等增长）

单核：指令集并行  
多核：并行编程，load balance，核与核的交互

性能评估：SPEC CPU benchmark:跑分，测试性能的程序  
参考机跑出来的结果为 1，各部分的得分为标准机的时间/实际时间  
跑分标准：将不同部分的得分相乘、开 n 次方根（几何平均）

功耗评估：ssj_ops，表示单位时间的性能  
不同负载下，记录性能（ssj_ops）和功耗（W），综合指标 ssj_ops/Watt = 性能求和 / 功耗求和  
Amdahl's law：能提高的那部分性能，由不可改变的那部分的占比决定  
改进的时间=（可以改变的/改进系数）+ 不能改变的时间  
要优化 common case  
负载少不一定功耗低，尽量使 CPU 负载多  
MIPS：millions of instruction per second，MIPS = clock rate / CPI\*10^6  
MIPS 高，性能不一定越好，和指令集 ISA 有关  
MIPS 和指令数无关，同一个计算机只有一个 MIPS（哪怕是不同程序），因此不全面

eight great ideas:

1. design for moore law：每两年单位面积的晶体管数翻倍
2. use abstraction to simplify design：TCP/IP，ISA
3. make the common case fast
4. performance via parallelism
5. performance via pipelining：前后步骤重叠进行
6. performance via prediction：及早判断要做什么事
7. hierarchy of memory
8. dependability via redundancy：冗余，如多个处理器同时处理同一过程

## Chap 03

word 由计算机的位宽决定，课上按 32bit  
指令也是用 word 形式表示

有符号数：

1. sign magnitude：第一位符号位，后面绝对值（0）有两个
2. two's complement：2 的补码，第一位-2^n
   一般表示补码

判断 overflow（有符号数）：次高位向高位进位，记为 c2；高位向再上一位进位，记为 c1。如果 c1 和 c2 异或为 1，则有进位。  
溢出处理：忽略，报给 OS，程序自己处理  
ALU 检测溢出（异常，中断）：把当前指令的地址存储，跳到 OS 中处理异常的部分（或其他处理）

构建 ALU：从一位扩展到多位  
单位：与，或，加，减，比较，检测零  
全加器：sum=A 异或 B 异或 cin，cout=B cin+A cin+ AB  
减法：B 按位取反，cin 一定是 1  
parallel redundant select：提前并行计算处出 cin 是 0 和 1 的两种可能结果，再选择。加快速度  
slt rd rs rt:set less than,rd 存储结果，对 rs 和 rt 比较。当 rs < rt 时 rd 为 1，否则为 0。先判断是不是同号，因为异号相减会溢出。  
most significant bit：最高位（符号位），叫做 set 信号。  
扩展：依次计算每一位，进位串联  
ALU 输出：是不是 0，计算结果，有没有溢出

Verilog 代码：

```v
module alu(A, B, ALU_operation, res, zero, overflow);
    input [31:0] A, B;
    input [2:0] ALU_operation;
    output [31:0] res;
    output zero, overflow;
    wire [31:0] res_and, res_or, res_add, res_sub, res_nor, res_slt;
    reg [31:0] res;
    parameter one = 32'h0000_0001, zero_0 = 32'h0000_0000;

    assign res_and = A & B;
    assign res_or = A | B;
    assign res_add = A + B;
    assign res_sub = A - B;
    assign res_slt = (A < B) ? one : zero_0;
    always@ (A or B or ALU_operation)
        case (ALU_operation)
            3'b000: res = res_and;
            3'b001: res = res_or;
            3'b010: res = res_add;
            3'b110: res = res_sub;
            3'b100: res = ~(A | B);
            3'b111: res = res_slt;
            default: res = 32'hx;
        endcase
    assign zero = (res == 0) ? 1 : 0;

endmodule

```

always@后面是敏感列表，出现再等式右边或导致结果变化的所有值，都要放在敏感列表中。  
中间值存储：redundant select，如果直接将计算式代入 case 中，则可以执行时优化

fast adder:

1. carry lookahead adder (CLA)：每个进位的式子展开成输入的表达式。十六位：四个一组，相同表示（两级加法器） 。

??? normal-comment "carry lookahead"

    `G`（Generate，生成）和 `P`（Propagate，传递）是进位先算（carry lookahead）加法器的核心概念。

    * **Generate g**：表示本位一定会产生进位，不依赖输入进位。

    $$
    g_i = a_i \land b_i
    $$

    * **Propagate p**：表示本位会把输入进位传给高一位。

    $$
    p_i = a_i \oplus b_i
    $$

    逐位情况：

    |  a |  b |  g |  p | 含义          |
    | -: | -: | -: | -: | ----------- |
    |  0 |  0 |  0 |  0 | 不产生进位，不传播进位 |
    |  0 |  1 |  0 |  1 | 不产生，但会传递进位  |
    |  1 |  0 |  0 |  1 | 不产生，但会传递进位  |
    |  1 |  1 |  1 |  0 | 一定会产生进位     |

    因此进位公式为：

    $$
    c_{i+1} = g_i \lor (p_i \land c_i)
    $$

    当把多位分为一组时，定义组信号：

    * **组传递 P**（整个组会把输入进位传到组末尾）

    $$
    P = p_{k-1} \land p_{k-2} \land \cdots \land p_0
    $$

    * **组生成 G**（整个组本身一定会在内部产生进位）

    $$
    G = g_{k-1} \lor (p_{k-1} g_{k-2}) \lor (p_{k-1} p_{k-2} g_{k-3}) \lor \cdots \lor (p_{k-1} \cdots p_1 g_0)
    $$

    于是组间进位可以写成：

    $$
    c_{out} = G \lor (P \land c_{in})
    $$

    举例，4 位组，a=\[1,0,1,1]，b=\[0,1,1,0]：

    * bit0: g0=0, p0=1
    * bit1: g1=0, p1=1
    * bit2: g2=1, p2=0
    * bit3: g3=0, p3=1

    组传递 P = 1·0·1·1 = 0
    组生成 G = g3 ∨ (p3 g2) ∨ … = 0 ∨ (1·1) = 1
    所以无论输入进位是多少，组的输出进位必然为 1。

    直观理解：

    * g=1 → “我自己一定能产出进位”
    * p=1 → “我会把外来的进位传下去”
    * 组 G/P 是把这逻辑串联起来的结果，可以并行计算出组间进位，从而避免逐位 ripple 传递，加快加法器速度。

    在 16 位两级进位先算加法器里，16 位被划分成 4 个小组，每组 4 位。每个小组先计算自己的组生成信号 G 和组传递信号 P（不依赖 c0）。这两个信号可以并行得到，因为它们只依赖本组的输入位，而不依赖外来的进位。

    有了各组的 G 和 P，组间进位（c4、c8、c12、c16）可以直接通过逻辑展开式并行算出来，例如：

    $$
    c4 = G_0 \lor (P_0 \land c0)
    $$

    $$
    c8 = G_1 \lor (P_1 \land G_0) \lor (P_1 P_0 c0)
    $$

    $$
    c12 = G_2 \lor (P_2 G_1) \lor (P_2 P_1 G_0) \lor (P_2 P_1 P_0 c0)
    $$

    这些公式都是组合逻辑，可以同时计算，不需要等低位的进位逐级传递。

    而组内的进位（c1、c2、c3，或者 c5、c6、c7 等）必须依赖于该组的输入进位。例如 c1 的公式里就包含 c0，c5 的公式里包含 c4。如果不知道本组的入口进位，就无法算组内的逐位进位。因此必须等组间进位先确定下来，才能往下展开计算。

    所以顺序是：先并行产生组间进位 c4、c8、c12、c16，然后再用这些结果去算每个组内部的 c1、c2、c3 等。这样既保证了速度，又减少了关键路径延迟。

2. carry select adder (CSA): 将进位是 0 和 1 都计算出来，用 c4 选择结果。

乘法：加法器、寄存器  
64bit 相乘，结果可能 128bit  
检验乘数的最后一位，如果是 1，结果加被乘数，如果是 0 跳过。被乘数左移一位，乘数右移一位。（太大！）  
加法只是 64 位，最低位后面不变。对积移位，每次将积右移。  
积用 128 位寄存器存储，初始时的后 64 位没有用到，全部在右移时移走。因为右移和乘数的移动相同，把乘数放在这个位置。  
乘法不能用补码计算。绝对值相乘，再判断符号位是不是一样。  
Booth 法：（从低位开始） 第一个出现的 1，减；连续出现的 1，移位（符号位不变）；最后出现的 1，加

??? normal-comment "Booth's Algorithm"

    Booth 算法是一种对二进制数进行有符号乘法运算的优化方法，主要目的是减少实际需要的加法或减法次数，从而提高运算效率。它适用于二进制补码表示的数。

    在普通的乘法器中，逐位扫描乘数的每一位，如果该位为 1，就加上被乘数对应的移位版本，如果该位为 0，就跳过。这种方法在乘数里有很多连续的 1 时，就会产生很多次重复的加法操作。Booth 算法通过对乘数的位模式进行编码，能把一串连续的 1 替换为一次加法和一次减法，从而减少计算次数。

    Booth 算法的基本思想是：观察乘数的相邻两位（包括最低位和额外添加的一位 0，记作 Q\[-1]）。根据这两位的组合，决定当前步骤是否需要对部分积加上或减去被乘数。规则如下：

    * 如果当前位 Q\[i] = 0，上一位 Q\[i-1] = 0 → 不操作（部分积不变）。
    * 如果当前位 Q\[i] = 1，上一位 Q\[i-1] = 0 → 部分积减去被乘数。
    * 如果当前位 Q\[i] = 0，上一位 Q\[i-1] = 1 → 部分积加上被乘数。
    * 如果当前位 Q\[i] = 1，上一位 Q\[i-1] = 1 → 不操作。

    在每一步之后，对整个寄存器（部分积 + 乘数 + Q\[-1]）做一次算术右移，这样逐步生成最终结果。

    举个例子，用 4 位 Booth 算法计算 `(-3) × (5)`：

    * 被乘数 M = -3，用 4 位补码表示是 1101。
    * 乘数 Q = 5，用 4 位补码表示是 0101。
    * 初始部分积 A = 0000，扩展为 8 位来计算，Q\[-1] = 0。

    步骤如下：

    1. 检查 Q\[0]=1, Q\[-1]=0 → 部分积 = 部分积 - M。
    然后算术右移。
    2. 检查新 Q\[0], Q\[-1] → 决定是否加减。
    每次操作后再算术右移。
    3. 重复 4 次（因为是 4 位数）。

    最终结果得到 11111111 1011（二进制补码），即十进制的 -15。这个与 -3 × 5 的正确结果一致。

    Booth 算法的优势在于，它能快速处理乘数中包含连续 1 的情况。比如普通乘法器在遇到 1111 时会执行 4 次加法，而 Booth 算法只需要 1 次加法和 1 次减法。这样在硬件实现上可以减少部分积累加次数，提高乘法效率。

![booth](../resources/booth.png){style="width:500px"}

unroll the loop：计算所有位的乘法结果，以树状的形式两两相加。  
RISC-V 中：mul, mulh, mulhu, mulhsu

除法：从高位开始减  
将除数从左边开始放，每次减除数，如果结果小于零表示多减了，再把除数加回来。将除数往右移。  
优化：除数开始时放在右边，每次被除数左移。  
为什么除数（64 位）从 remainder（128 位）的最左边开始匹配，而不是直接对齐？这是通用除法器，不确定除数有几位，不能直接对齐。

![division](../resources/division.png){style="width:500px"}

一正一负相除：商的符号和被除数相同  
指令：div,rem; divu,remu  
当除数是 0 时，产生 overflow，要自己处理  
除法不能展开，因为不知道什么时候结束

浮点数：  
浮点是数据结构，sign（符号），significand（fraction，尾数，归一化），exponent（指数位，乘 2 的几次）
符号位 0 表示正数，1 表示负数  
单精度：8 位指数，23 位尾数；  
双精度：11 位指数，52 位尾数（尾数越多，精度越高）  
存储顺序：符号、指数、尾数  
默认尾数的小数点前为 1，节省一个 bit  
指数默认加 bias，实际的指数为 exponent - bias，这样 exponent 的存储值始终是正的  
单精度的 bias 是 127，双精度的 bias 是 1023  
exponent=0 表示非规范化数或 0，所以单精度的范围最小是$1\times 2^{-126}$，最小精度是$2^{-23}$

$$(-1)^{sign}\cdot(1+significand)\cdot 2^{exponent-bias}$$

exponent=111..., fraction=000...表示无穷  
exponent=111..., fraction!=000...表示 nan  
普通数的指数不能全 1

浮点计算：对齐（化成指数相同），对应数相加，归一化，rounding（进位），归一化  
对齐时小的向大的靠近，因为计算后超过位数需要丢掉几位，这样丢掉的是权值低的位  
不同计算机有不同的进位方法

![float algorithm](./resources/float%20algorithm.png){style="width:500px"}

浮点乘法：尾数相乘，指数相加  
指数相加时 bias 加了两次，一定要减一个 bias  
浮点除法：小数相除，指数相减  
指数减完要把 bias 加回去

实际计算中，为了计算准确（对齐右移时有些被丢掉），额外加一些位  
guard 位（后面放一位用于保护），round 位（guard 位的下一位），sticky 位（round 位的下一位，指数差很多，丢掉余下的数中，只要非零则 sticky 位为 1，否则为 0）  
sticky 位有些地方没有  
ulp（units in the last place）：四舍五入，最大的损失是最小精度的一半

## Chap 02

指令集将软件和硬件联系  
GCC 高级编程语言 -（编译器）-> 汇编语言 -（汇编器）-> 机器语言，二进制  
这里学习的指令集将汇编和机器语言对应起来
Instruction set：定义语法结构 syntax  
一条指令由 op（operators）和 oprand（操作对象）组成

Operation：  
任何指令集必须支持算术运算  
RISC-V 中一条指令只支持一种操作，其他的如 x86 中有乘加  
格式：`操作符 结果 操作数1 操作数2`

示例：f=(g+h)-(i+j)  
RISC-V：

```asm
# 示例，实际中g，h不能出现
add t0, g, h    # 临时变量t0
add t1, i, j
sub f, t0, t1   # f=t0-t1
```

Operands：  
算术逻辑操作，只能用 register，不能用 memory  
RISC-V 中有 32 个 64 位寄存器，一个寄存器是一个整体  
经常用的数据放在寄存器中，一个寄存器叫做一个 doubleword  
32 个寄存器分别叫做 x0~x31，有特殊含义  
为什么是 32 个？Smaller is fast

| Name    | Register name | Usage                                           | Preserved On call? |
| ------- | ------------- | ----------------------------------------------- | ------------------ |
| x0      | 0             | The constant value 0（只存放 0）                | n.a.               |
| x1(ra)  | 1             | Return address(link register)（函数返回的地址） | yes                |
| x2(sp)  | 2             | Stack pointer（堆栈指针）                       | yes                |
| x3(gp)  | 3             | Global pointer                                  | yes                |
| x4(tp)  | 4             | Thread pointer                                  | yes                |
| x5-x7   | 5-7           | Temporaries （临时寄存器）                      | no                 |
| x8-x9   | 8-9           | Saved （saved 寄存器）                          | yes                |
| x10-x17 | 10-17         | Arguments/results （函数传参）                  | no                 |
| x18-x27 | 18-27         | Saved                                           | yes                |
| x28-x31 | 28-31         | Temporaries                                     | no                 |

示例：

```asm
# 标准汇编
add x5, x20, x21
add x6, x22, x23
sub x19, x5, x6
```

Memory Oprands：  
两类指令将数据从 memory 拿到寄存器：load 和 store  
load 从 memory 到 register，store 从 register 到 memory  
RISC-V 被称为 load-store 架构  
Memory 以 byte 为单位进行索引  
最开始 word 的地址：4、8……（一个 word 四字节）  
（align：）每个 word 的第 0 个 byte 放在第 0 个还是第 3 个 byte，决定是 little endian（小端序）还是 big endian（大端序）  
低地址放在低位：小端序  
RISC-V does not require word to be aligned，可以放在边界上（但是不好的方式，避免）  
e.g. 内存对齐，一次只能读出 4 字节内存中的一行，有些布局的 double 不能一次性读出（不 align 的结果）  
e.g.

- big end, Byte1: 01; Byte2: 02 -> 0x0201, 513
- little end, Byte1: 01; Byte2: 02 -> 0x0102, 258

!!! normal-comment "示例"

    C Code：`A[12]=h+A[8]`, h in x21, base address of A in x22
    Index 8 requires offset of 64 （按 64 位，doubleword 每个 8 字节，索引 8 \* 每个元素 8 字节）
    `ld`表示 load doubleword，`lw`表示 load word, `lh`表示 load halfword. `s`开头表示 store
    ```asm
    ld x9, 64(x22)  # 偏移量(基址)，从x22+64取值放到x9中
    add x9, x21, x9
    sd x9, 96(x22)  # 将x9的值放到x22+96的值
    ```

Register vs Memory
寄存器比内存更快  
对 memory 中数据进行操作，必须 load 和 store  
编译器决定什么时候放回去，用得多的放在寄存器，用得少的才放回内存

make common case fast，不用将常数取出、放到寄存器、再相加  
增加`addi`指令：立即数相加  
立即数直接包含在指令内部，字段有限，不能特别大

!!! normal-comment "示例"

    `addi x5, x6, 20`表示`x5=x6+20`

指令在计算机中也以二进制表示（机器码）  
x0~x31 的寄存器编码成 0~31 的数  
把每个数按特定规则拆成不同部分，每个部分表示特定含义  
7bit 表示操作，5bit 表示寄存器编号

!!! normal-comment "示例"

    指令：`add x9, x20, x21`
    十进制表示机器码：0 21 20 0 9 51
    0 源操作数 源操作数 0 目标操作数 指令编号

一般用十六进制表示

| 十六进制 | 二进制 | 十六进制 | 二进制 |
| -------- | ------ | -------- | ------ |
| 0        | 0000   | 4        | 0100   |
| 1        | 0001   | 5        | 0101   |
| 2        | 0010   | 6        | 0110   |
| 3        | 0011   | 7        | 0111   |
| 8        | 1000   | C        | 1100   |
| 9        | 1001   | D        | 1101   |
| A        | 1010   | E        | 1110   |
| B        | 1011   | F        | 1111   |

R-format 格式（普通操作）：

| funct7 辅助 | rs2 源寄存器 2 | rs1 源寄存器 1 | funct3 辅助 | rd 目标寄存器 | opcode 操作 |
| ----------- | -------------- | -------------- | ----------- | ------------- | ----------- |
| 7 bits      | 5 bits         | 5 bits         | 3 bits      | 5 bits        | 7 bits      |

通过 funct 可以区分 lw, ld, lh 等

I-format 格式（立即数）：

| immediate 立即数 | rs1 源寄存器 | funct3 辅助 | rd 目标寄存器 | opcode 操作码 |
| ---------------- | ------------ | ----------- | ------------- | ------------- |
| 12 bits          | 5 bits       | 3 bits      | 5 bits        | 7 bits        |

立即数用 12 位表示，所以范围是$\pm 2^{11}$

S-format 格式（Store）：

| imm[11:5]立即数的高 7 位 | rs2 源寄存器 2 | rs1 存储寄存器 1 | funct3 辅助 | imm[4:0]立即数的低 5 位 | opcode 操作码 |
| ------------------------ | -------------- | ---------------- | ----------- | ----------------------- | ------------- |
| 7 bits                   | 5 bits         | 5 bits           | 3 bits      | 5 bits                  | 7 bits        |

imm[11:5]用来表示偏移

!!! normal-comment "示例"

    `sd x9, 64(x22)`
    22: rs1
    9: rs2
    64: imm[11:5]

SB-format：条件跳转的指令  
UJ-format：无条件跳转

逻辑操作：  
左移 slli，右移 srli，与 and，andi，或 or，ori，异或 xor，xori  
为什么左移右移都是立即数？64 位立即数也能全部移完，立即数能覆盖

左右移的格式：

| funct6 | immed  | rs1    | funct3 | rd     | opcode |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 6 bits | 6 bits | 5 bits | 3 bits | 5 bits | 7 bits |

I 型，将 12 位的立即数拆成两部分

与门：`and x9, x10, x11`表示`x9 = x10 & x11`  
或门：`or x9, x10, x11`表示`x9 = x10 | x11`  
异或门：`xor x9, x10, x11`表示`x9 = x10 ~ x11`  
取反操作通过异或实现

条件跳转：

```asm
beq reg1, reg2, L1  # 如果reg1==reg2则跳转到L1
bne reg1, reg2, L1  # 如果reg1！=reg2则跳转到L1
```

b 表示 branch

!!! normal-comment "if 示例"

    C code:
    ```c
    if (i == j) goto L1;
    f = g + h;
    L1: f = f - i;
    ```

    RISC-V assembly code:
    ```asm
        beq x21, x22, L1
        add x19, x20, x21
    L1: sub x19, x19, x22
    ```

!!! normal-comment "if-else 示例"

    C code:
    ```c
    if (i == j) f = g + h;
    else f = g - h;
    ```

    RISC-V code:
    ```asm
        bne x22, x23, Else
        add x19, x20, x21
        beq x0, x0, Exit  # goto Exit
    Else: sub x19, x20, x21
    Exit: ...
    ```

!!! normal-comment "loop 示例"

    ```asm
    Loop: ...
          bne x9, x10, Loop
    ```

set on less than (slt):如果小于则置 1  
`slt x5, x19, x20`表示如果 x19 < x20 则 x5 = 1

!!! normal-comment "slt 示例"

    C code:
    ```c
    if (a < b) goto Less;
    ```

    RISC-V code:
    ```asm
    slt x5, x8, x9
    bne x5, zero, Less
    ```

`blt rs1, rs2, L1`如果 rs1 < rs2，则跳转到 L1  
`bge rs1, rs2, L1`如果 rs1 >= rs2，则跳转到 L1  
区分有符号数和无符号数，blt 和 bge 表示有符号，无符号数后加 u

jump register：switch-case 语句  
`jalr x1, 100(x6)`把当前地址放到 x1（之后能回来），跳到 x6+100  
switch(k)时，不同 k 的值的地方存储指令的地址，指向各个指令  
x6 表示当前跳转表的地址，x6 和 k 左移 3（字的地址）后的值相加得到 x7（表示当前地址），load 到 x7（之前的 x7 里存的是另一个地址，这一步从 x7 指向的内存位置，加载一个 64 位值，存到 x7，这样 x7 表示真正的目标代码的地址），jalr 时以 x7 中地址跳转

!!! normal-comment "jalr 示例"

    C code:
    ```c
    switch (k) {
        case 0: f = i + j; break;
        case 1: f = g + h; break;
        case 2: f = g - h; break;
        case 3: f = i - j; break;
    }
    ```

    RISC-V:
    ```asm
    blt x25, x0, Exit  # k<0, 超出范围
    bge x25, x5, Exit  # k>=4, 超出范围
    slli x7, x25, 3    # 偏移量存到x7
    add x7, x7, x6     # 当前地址
    ld x7, 0(x7)       # 加载目标地址
    jalr x1, 0(x7)     # 当前地址存放到x1，按x7跳转
    ```
