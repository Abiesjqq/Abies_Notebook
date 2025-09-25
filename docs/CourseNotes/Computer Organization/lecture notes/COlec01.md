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

响应时间/执行时间：完成任务要多长时间  
吞吐率（带宽）：单位时间能完成多少任务  
流水线 CPU 没有改变每条指令的执行时间，但是提高的吞吐率。  
性能 performance = 1 / execution time  
运行时间 elapsed time：总的时间，包括响应时间，输入输出时间，空闲时间  
CPU 时间：处理工作的总的时间，是 elapsed time 的子集，包含多个任务的 shares

**怎么计算时间？**  
握手协议：在信号的上升沿或下降沿（时钟信号的边缘）通过交换信号来协调操作。  
时钟周期 clock period：一个周期的长度  
时钟周期数 clock cycles  
1ns = $1\times 10^{-9}$s, 1ps = $1\times 10^{12}$s  
1MHz = $1\times 10^{6}$Hz， 1GHz = $1\times 10^{9}$Hz  
时钟频率 clock frequency(rate)：一秒内的周期数

CPU 时间 = 总共用了几个 CPU 时钟 \* 时钟周期 = 总共用了几个 CPU 时钟 / 时钟频率

减少 CPU 时间：周期数变少，时钟频率变大

算法影响指令数 IC 和 CPI，从而影响source-level statements and the number of I/O operations

动态能耗：半导体导通和截止时产生的能耗
