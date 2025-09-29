### Introduction

- 图灵机：图灵提出的一种 理想化的计算模型
- 图灵测试：图灵提出的检验人工智能的方法，如果一个机器在对话中能让人类分不清自己面对的是机器还是真人，就通过了图灵测试。
- 图灵完备性（图灵完全）：如果一个系统能模拟任意图灵机的运算，就称它是图灵完备的，通常需要有条件分支、循环（或递归）、可修改的数据存储。

电子管（真空管），可编程 -> 晶体管，体积减小 -> 集成电路 -> 微处理器

冯诺依曼架构：计算和存储分离，数据和指令保存在同一个存储器，按照程序顺序执行  
现代：计算和存储统一（CPU 运算速度增长得越来越快，但内存访问速度提升远远跟不上，“内存墙”）  
功耗墙：随着处理器频率的不断提高，功耗也随之增加，导致散热问题越来越严重。当功耗达到一定的上限时，进一步提高频率或增加功能的设计变得不可行，因为过高的功耗会导致硬件损坏或热量过高而影响稳定性。

RISC：指令执行用尽量少的时钟周期，指令编码长度定长，提高 CPU 与编译效率

Moore's Law： 单芯片上所集成的晶体管资源每 18 至 24 个月翻一倍

什么是计算机？电子化，有指令集，可执行指令，可存储指令与数据，计算能力上是图灵完全

### Computer Organization

硬件：CPU（控制单元，数据线），内存，I/O 接口

Memory：  
Main memory: volatile, hold programs while they are running  
Second memory: nonvolatile, store programs and data between runs

Volatile（易失性）：DRAM, SRAM（读写快，用于缓存）  
Nonvolatile（非易失性）：固态硬盘 or 闪存，硬盘

软件：应用软件 + 系统软件

操作系统：处理基本输入输出操作，管理存储和内存，决策不同程序计算能力的分配

### Computer Design

响应时间/执行时间（response time）：多久完成任务  
吞吐率（throughput）：单位时间内能完成的工作量  
流水线 CPU 没有改变每条指令的执行时间，但是提高的吞吐率。  
对每个操作响应时间短，吞吐率大；吞吐率大不一定对每个的响应时间都短  
增加处理器，响应时间不一定提高（考虑单处理器），但吞吐率提高  
性能 performance=1/执行时间  
performance 必须基于同一个程序  
运行时间 elapsed time：总的时间，包括响应时间，输入输出时间，空闲时间  
CPU 时间：处理工作的总的时间，是 elapsed time 的子集，包含多个任务的 shares

真正的执行时间不只有 CPU 时间，还有 IO 等系统时间（这里先只考虑 CPU）

同步逻辑：同一个时钟驱动  
CPU 是同步逻辑

**怎么计算 CPU 执行时间？**  
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
算法影响指令数 IC 和 CPI，从而影响 source-level statements and the number of I/O operations
计算平均 CPI  
频率很难提高：功耗限制 -> 多核  
功耗 = 负载 \* 电压^2 \* 频率  
工艺越先进，电压越低，功耗越小（电压降低使频率增长没有导致功耗同等增长）  
动态能耗：半导体导通和截止时产生的能耗  
Instruction set architecture 指令集

握手协议：在信号的上升沿或下降沿（时钟信号的边缘）通过交换信号来协调操作。  
时钟周期 clock period：一个周期的长度  
时钟周期数 clock cycles  
1ns = $1\times 10^{-9}$s, 1ps = $1\times 10^{12}$s  
1MHz = $1\times 10^{6}$Hz， 1GHz = $1\times 10^{9}$Hz  
时钟频率 clock frequency(rate)：一秒内的周期数

芯片制造：芯片设计，掩膜，硅切片成晶圆，光刻，测试，晶圆切片，封装  
？nm：两条线之间的最小距离

$$ \text{cost per die}=\frac{\text{cost per wafer}}{\text{dies per wafer}\times\text{yield}},\quad\text{dies per wafer}\approx\text{wafer area}/\text{die area}$$

$$\text{yield}=\frac{1}{(1+(\text{defects per area}\times\text{die area}/2))^2}$$

芯片面积越大，良率越低。

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
2. use abstraction to simplify design：封装，TCP/IP，ISA
3. make the common case fast：如将 0 存储在特定寄存器 x0
4. performance via parallelism：同时进行同一件事
5. performance via pipelining：前后步骤重叠进行（洗衣服）
6. performance via prediction：预测要做什么事，在得到明确答案之前计算不同可能的结果，条件是试错成本不大
7. hierarchy of memory：越便宜、越慢、越大，越放在底层（少用）
8. dependability via redundancy：通过冗余提升程序的可靠性，如多个处理器同时处理同一过程

新的摩尔定律：每 1.5~2 年，智能体的数量翻一倍

??? examples "8个思想的示例"

    汽车生产：流水线
    吊桥：冗余  
    飞机考虑风向：预测  
    电梯：common case fast  
    图书馆放书的书桌：hierarchy    
    CMOS中，门区域大：并行  
    技术发展：摩尔定律  
    自驾系统分类：封装
