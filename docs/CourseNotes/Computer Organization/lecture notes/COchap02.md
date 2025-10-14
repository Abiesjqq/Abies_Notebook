## 指令集介绍

（目录：指令的表示，逻辑操作，决策指令，计算机对过程的支持，指令的寻址）

指令集将软件和硬件联系  
GCC 高级编程语言 -（编译器）-> 汇编语言 -（汇编器）-> 机器语言，二进制  
这里学习的指令集将汇编和机器语言对应起来

Instruction set：定义语法结构（syntax）

一条指令由 op（operators）和 oprand（操作对象）组成  
RISC: Reduced Insruction Set Computer

**现代计算机的两条原理**：

- 指令以数字形式表示。
- 程序可以存储在内存中，像数字一样被读取或写入。

**计算机硬件的操作**：

- 任何指令集必须支持算术运算
- RISC-V 中每一条指令只支持一种操作，其他的如 x86 中有乘加（为什么？_Simplicity favors regularity_）

## 操作和操作数

### 操作格式

格式：`操作符 结果 操作数1 操作数2`

!!! examples "示例 RISC-V 中加减法"

    示例：f=(g+h)-(i+j)
    RISC-V：

    ```asm
    # 示例，实际中g，h不能出现
    add t0, g, h    # 临时变量t0
    add t1, i, j    # 临时变量t1
    sub f, t0, t1   # f=t0-t1
    ```

    用寄存器表示（标准的汇编）：

    ```asm
    add x5, x20, x21
    add x6, x22, x23
    sub x19, x5, x6
    ```

    Arithmetic 类型中，三个寄存器中，第一个为目标寄存器，后两个为源寄存器。

### 寄存器操作数

算术逻辑操作只能用 register，不能用 memory。  
RISC-V 中有 32 个 64 位寄存器，一个寄存器是一个整体。  
经常用的数据放在寄存器中，32 位数据叫做 word，一个寄存器中 64 位数据叫做 doubleword。

32 个寄存器分别叫做 x0~x31，有特殊含义。  
为什么是 32 个？_Smaller is fast_，通过 benchmark 对不同数量测试

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

### 内存操作数

两类指令将数据从 memory 拿到寄存器：`load` 和 `store`。load 从 memory 到 register，store 从 register 到 memory。
因此 RISC-V 被称为 load-store 架构。

Memory 以 byte 为单位进行索引  
相邻指令加四：指令是 32 位，而内存中以 byte（8 位）为最小单位，每个指令是 4 个 byte。
word 的地址从 4、8…… 开始

align：每个 word 的第 0 个 byte 放在第 0 个还是第 3 个 byte，决定是 little endian（小端序）还是 big endian（大端序）  
RISC-V 中采用小端序。

- 小端序：低地址放在低位
- 大端序：低地址放在高位

!!! examples "示例 小端序和大端序"

    (1) 十六进制数 0x（高）12 34 56 78（低），内存中从左到右为低地址到高地址。

    - 大端序：（低）12 34 56 78（高）
    - 小端序：（低）78 56 34 12（高）

    (2) 计算示例

    - big end, Byte1: 01; Byte2: 02 -> 0x0201, 513
    - little end, Byte1: 01; Byte2: 02 -> 0x0102, 258

RISC-V does not require word to be aligned，可以放在边界上（但是不好的方式，避免）  
e.g. 内存对齐，一次只能读出 4 字节内存中的一行，有些布局的 double 不能一次性读出（不 align 的结果）

!!! examples "示例"

    C Code：`A[12]=h+A[8]`, h in x21, A 的基址（base address）放在 x22。

    从 A[0] 到 A[8] 需要 64 个字节的偏移量。因为每个 doubleword 为 8 字节，索引为 8，总共 8\*8=64 字节。
    字节的偏移用 `偏移量(基址)` 表示。

    `ld`表示 load doubleword，`lw`表示 load word, `lh`表示 load halfword. `s`开头表示 store。

    RISC-V：

    ```asm
    ld x9, 64(x22)  # x9 <- x22+64
    add x9, x21, x9
    sd x9, 96(x22)  # x9 -> x22+96
    ```

**Register vs Memory**：

寄存器直接集成在 CPU 内部，由硬件电路直接控制，访问几乎无延迟。而内存（RAM）在 CPU 外部，通过总线通信，每次读写都需要几十到上百个 CPU 时钟周期。减少内存的访问能提升性能。
因此尽量少使用 memory。对 memory 中数据进行操作，必须 load 和 store。  
编译器决定什么时候放回去，用得多的放在寄存器，用得少的才放回内存。

**对常数的优化**：

_Make common case fast_，增加 constant operand，不用将常数取出、放到寄存器、再相加。  
增加 `addi` 指令：立即数相加。如 `addi x5, x6, 20` 表示 `x5=x6+20`。
立即数直接包含在指令内部，字段有限，不能特别大

## 指令的表示

指令在计算机中也以二进制表示（机器码），长度为 32 位。

x0~x31 的寄存器编码成 0~31 的数。

把每个指令按特定规则拆成不同部分，每个部分表示特定含义。7bit 表示操作，5bit 表示寄存器编号

!!! examples "示例"

    指令：`add x9, x20, x21`
    十进制表示机器码：0 21 20 0 9 51
    0 源操作数 源操作数 0 目标操作数 指令编号

**十六进制与二进制**：

| 十六进制 | 二进制 | 十六进制 | 二进制 |
| -------- | ------ | -------- | ------ |
| 0        | 0000   | 8        | 1000   |
| 1        | 0001   | 9        | 1001   |
| 2        | 0010   | A        | 1010   |
| 3        | 0011   | B        | 1011   |
| 4        | 0100   | C        | 1100   |
| 5        | 0101   | D        | 1101   |
| 6        | 0110   | E        | 1110   |
| 7        | 0111   | F        | 1111   |

### R-format

操作：寄存器-寄存器运算（纯寄存器操作）

| funct7 辅助 | rs2 源寄存器 2 | rs1 源寄存器 1 | funct3 辅助 | rd 目标寄存器 | opcode 操作 |
| ----------- | -------------- | -------------- | ----------- | ------------- | ----------- |
| 7 bits      | 5 bits         | 5 bits         | 3 bits      | 5 bits        | 7 bits      |

通过 funct 可以区分 lw, ld, lh 等。

- `opcode`：决定指令的大类（R/I/S/B/U/J）。
- `funct3`：在同一类中进一步区分子操作（如加、与、或、移位）。
- `funct7`：在子操作中再区分特殊情况（如加/减、逻辑右移/算术右移）。

### I-format

操作：寄存器-立即数运算、加载、跳转到寄存器

| immediate 立即数 | rs1 源寄存器 | funct3 辅助 | rd 目标寄存器 | opcode 操作码 |
| ---------------- | ------------ | ----------- | ------------- | ------------- |
| 12 bits          | 5 bits       | 3 bits      | 5 bits        | 7 bits        |

立即数用 12 位表示，所以范围是 $\pm 2^{11}$。

### S-format

操作：存储指令（Store）

| imm[11:5]立即数的高 7 位 | rs2 源寄存器 2 | rs1 存储寄存器 1 | funct3 辅助 | imm[4:0]立即数的低 5 位 | opcode 操作码 |
| ------------------------ | -------------- | ---------------- | ----------- | ----------------------- | ------------- |
| 7 bits                   | 5 bits         | 5 bits           | 3 bits      | 5 bits                  | 7 bits        |

imm[11:5] 和 imm[4:0] 合并后得到立即数 imm[11:0]，存储地址偏移量（有符号数）。

SB-format：条件跳转的指令  
UJ-format：无条件跳转

!!! normal-comment "RISC-V 指令格式汇总"

    RISC-V 指令格式（RV32I）

    | 类型  | 名称            |            31–25             |  24–20  |  19–15  |   14–12    |       11–7       |    6–0     |
    | :---: | :-------------- | :--------------------------: | :-----: | :-----: | :--------: | :--------------: | :--------: |
    | **R** | Register        |          **funct7**          | **rs2** | **rs1** | **funct3** |      **rd**      | **opcode** |
    | **I** | Immediate       |   **imm[11:0]** (12 bits)    |    —    | **rs1** | **funct3** |      **rd**      | **opcode** |
    | **S** | Store           |        **imm[11:5]**         | **rs2** | **rs1** | **funct3** |   **imm[4:0]**   | **opcode** |
    | **B** | Branch          |      **imm[12\|10:5]**       | **rs2** | **rs1** | **funct3** | **imm[4:1\|11]** | **opcode** |
    | **U** | Upper Immediate |   **imm[31:12]** (20 bits)   |    —    |    —    |     —      |      **rd**      | **opcode** |
    | **J** | Jump            | **imm[20\|10:1\|11\|19:12]** |    —    |    —    |     —      |      **rd**      | **opcode** |



    ??? normal-comment "说明"

        字段说明

        | 字段         | 含义                                  |
        | ------------ | ------------------------------------- |
        | `opcode`     | 操作码（7 位），决定指令基本类型      |
        | `rd`         | 目标寄存器（5 位，`x0`–`x31`）        |
        | `rs1`, `rs2` | 源寄存器 1 和 2（各 5 位）            |
        | `funct3`     | 功能码（3 位），用于区分同类指令      |
        | `funct7`     | 扩展功能码（7 位），主要用于 R 型指令 |
        | `imm[...]`   | 立即数字段，不同格式拼接方式不同      |

        立即数（Immediate）拼接规则

        | 类型  | 立即数拼接方式（高位 → 低位）                   | 最终形式               |
        | ----- | ----------------------------------------------- | ---------------------- |
        | **I** | `[11:0]`                                        | `sext(imm[11:0])`      |
        | **S** | `[11:5] + [4:0]` → `[11:0]`                     | `sext(imm[11:0])`      |
        | **B** | `[12] + [10:5] + [4:1] + [11]` → `[12:1] + 0`   | `sext(imm[12:1] << 1)` |
        | **U** | `[31:12]`                                       | `imm[31:12] << 12`     |
        | **J** | `[20] + [10:1] + [11] + [19:12]` → `[20:1] + 0` | `sext(imm[20:1] << 1)` |

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
