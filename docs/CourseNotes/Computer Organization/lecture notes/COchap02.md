
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

!!! examples "示例"

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

!!! examples "示例"

    `addi x5, x6, 20`表示`x5=x6+20`

指令在计算机中也以二进制表示（机器码）  
x0~x31 的寄存器编码成 0~31 的数  
把每个数按特定规则拆成不同部分，每个部分表示特定含义  
7bit 表示操作，5bit 表示寄存器编号

!!! examples "示例"

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

!!! examples "示例"

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

!!! examples "if 示例"

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

!!! examples "if-else 示例"

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

!!! examples "loop 示例"

    ```asm
    Loop: ...
          bne x9, x10, Loop
    ```

set on less than (slt):如果小于则置 1  
`slt x5, x19, x20`表示如果 x19 < x20 则 x5 = 1

!!! examples "slt 示例"

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

!!! examples "jalr 示例"

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
