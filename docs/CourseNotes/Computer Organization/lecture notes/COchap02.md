## 指令集介绍

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

Memory 以 byte 为单位进行索引！  
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

### R、I、S 型指令

**R-format**

操作：寄存器-寄存器运算（纯寄存器操作）

| funct7 | rs2    | rs1    | funct3 | rd     | opcode |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 7 bits | 5 bits | 5 bits | 3 bits | 5 bits | 7 bits |

通过 funct 可以区分 lw, ld, lh 等。

- `opcode`：决定指令的大类（R/I/S/B/U/J）。
- `funct3`：在同一类中进一步区分子操作（如加、与、或、移位）。
- `funct7`：在子操作中再区分特殊情况（如加/减、逻辑右移/算术右移）。

**I-format**

操作：寄存器-立即数运算、加载（load）、跳转到寄存器

| immediate | rs1    | funct3 | rd     | opcode |
| --------- | ------ | ------ | ------ | ------ |
| 12 bits   | 5 bits | 3 bits | 5 bits | 7 bits |

immediate 表示立即数或偏移量，用 12 位表示，所以范围是 $\pm 2^{11}$。

**S-format**

操作：存储指令（Store）

| imm[11:5] | rs2    | rs1    | funct3 | imm[4:0] | opcode |
| --------- | ------ | ------ | ------ | -------- | ------ |
| 7 bits    | 5 bits | 5 bits | 3 bits | 5 bits   | 7 bits |

S 型指令没有目标寄存器，因为 store 是将寄存器的数据存到基址+偏移量的地址，不是存到寄存器。

imm[11:5] 和 imm[4:0] 合并后得到立即数 imm[11:0]，存储地址偏移量（有符号数）。

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

### 逻辑操作

左移 slli，右移 srli，与 and，andi，或 or，ori，异或 xor，xori  
逻辑移位和算术移位：逻辑移位时空位补零，算术右移时空位补符号位  
只有算术逻辑右移，没有算术逻辑左移

为什么左移右移都是立即数？64 位立即数也能全部移完，立即数能覆盖

左右移的格式（I 型，将 12 位的立即数拆成两部分）：

| funct6 | immed  | rs1    | funct3 | rd     | opcode |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 6 bits | 6 bits | 5 bits | 3 bits | 5 bits | 7 bits |

- 左移：`sll x5, x6, x7`表示`x5=x6<<x7`
- 左移立即数：`slli x5, x6, 3`表示`x5=x6<<3`
- 右移：`srl x5, x6, x7`表示`x5=x6>>x7`
- 按位与：`and x9, x10, x11`表示`x9 = x10 & x11`
- 按位或：`or x9, x10, x11`表示`x9 = x10 | x11`
- 按位异或：`xor x9, x10, x11`表示`x9 = x10 ~ x11`
- 取反：通过异或实现，`xori  x9, x10, -1`

RISC-V 中没有 nor 运算，x86 中有。

### 决策指令

#### 条件跳转

**比较相等：**

- 相等跳转：`beq`（branch if equal），`beq reg1, reg2, L1`表示如果 reg1==reg2 则跳转到 L1
- 不相等跳转：`bne`（branch if not equal），`bne reg1, reg2, L1`表示如果 reg1！=reg2 则跳转到 L1

b 表示 branch

!!! examples "示例 if 跳转"

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

    由于指令顺序执行，`sub x19, x19, x22`始终会被执行
    可用`beq x0, x0, EXIT`结束

!!! examples "示例 if-else"

    C code:
    ```c
    if (i == j)
        f = g + h;
    else
        f = g - h;
    ```

    RISC-V code:
    ```asm
          bne x22, x23, Else    # 测试条件一般用bne（有利于分支预测），效率更高
          add x19, x20, x21
          beq x0, x0, Exit      # goto Exit
    Else: sub x19, x20, x21
    Exit: ...
    ```

**循环语句：**

!!! examples "示例 loop"

    ```asm
    Loop: ...
          bne x22, x21, Loop
    ```

!!! examples "示例 while 循环"

    C code:
    ```c
    while (a[i] == k)
        i += 1;
    ```

    RISCV code:（用变量名代替寄存器）
    ```asm
    Loop:
        slli  addr, offset, 3
        add   addr, addr, base
        ld    saved1, 0(addr)   # saved1=a[i]
        bne   saved1, k, Exit
        addi  i, i, 1
        beq   x0, x0, Loop
    Exit:
        ...
    ```

**比较运算：**

set on less than (slt):如果小于则置 1  
`slt x5, x19, x20`表示如果 x19 < x20 则 x5 = 1

!!! examples "示例 slt"

    C code:
    ```c
    if (a < b) goto Less;
    ```

    RISC-V code:
    ```asm
    slt  x5, x8, x9
    bne  x5, zero, Less
    ```

- 小于则跳转：`blt rs1, rs2, L1`如果 rs1 < rs2，则跳转到 L1
- 大于等于则跳转：`bge rs1, rs2, L1`如果 rs1 >= rs2，则跳转到 L1

区分有符号数和无符号数，blt 和 bge 表示有符号，无符号数后加 u  
没有“addu”指令，所有加法都按有符号数处理

#### 无条件跳转

jump register：switch-case 语句

`jalr x1, 100(x6)`把当前地址放到 x1（x1=PC+4, 之后能回来），跳到 x6+100（不需要做判断）

switch(k)时，不同 k 的值的地方存储指令的地址，指向各个指令  
x6 表示当前跳转表的地址，x6 和 k 左移 3（字的地址）后的值相加得到 x7（表示当前地址），load 到 x7（之前的 x7 里存的是另一个地址，这一步从 x7 指向的内存位置，加载一个 64 位值，存到 x7，这样 x7 表示真正的目标代码的地址），jalr 时以 x7 中地址跳转

!!! examples "示例 jalr"

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
    blt   x25, x0, Exit     # k<0, 超出范围
    bge   x25, x5, Exit     # k>=4, 超出范围
    slli  x7, x25, 3        # 偏移量存到x7
    add   x7, x7, x6        # 当前地址
    ld    x7, 0(x7)         # 加载目标地址
    jalr  x1, 0(x7)         # 当前地址存放到x1，按x7跳转
    ```

    具体分支中用 `jalr x0, 0(x1)` 跳回来，因为上一步 jalr 中 x1 已经存储下一步指令。

### U 型指令

U 型指令表示大立即数指令。  
I 型指令中只有 12 位表示立即数（还有符号位），无法表示大立即数。U 型指令中可用 32 位立即数。

如果存储 32 位的数？  
lui 指令 (load upper immediate)：U-type，用于存储立即数  
指令中高 20 位表示立即数，直接放在 64 位 rd 寄存器低 32 位中的高位；指令中低 12 位表示 rd 和指令，放到寄存器低 32 位的低位时全部置零。寄存器的高 32 位全部置零。  
此时寄存器中存储的数实际为低 32 位的高 20 位的数乘 2e12（因为后面都是 0）。  
要低位不全是零：用 addi 指令补上剩余部分。

高位通过右移得到，低位通过与运算得到。

**U-format**

操作：加载高位立即数（如 `lui`）或与 `jalr` 配合构成完整地址（如 `auipc`）（Upper Immediate Format）。

| imm[31:12] | rd     | opcode |
| ---------- | ------ | ------ |
| 20 bits    | 5 bits | 7 bits |

- 立即数解释：
  - 直接作为高 20 位，低 12 位补 0。
  - 即：`imm[31:12] << 12`，形成 32 位有符号立即数（但仅高 20 位可设）。
- 典型指令：
  - `lui rd, imm`：将 `imm[31:12]` 加载到 `rd` 的高 20 位，低 12 位为 0。
  - `auipc rd, imm`：将 `PC + (imm[31:12] << 12)` 写入 `rd`，用于 PC 相对寻址。

U 格式不涉及 rs1/rs2，仅提供高位立即数。

!!! examples "示例 存储 32 位数 976\*16^3+2304"

    RISC-V code：

    ```asm
    lui   s3, 976       # 低32位的高20位：lui放置
    addi  s3, s3, 2304  # 低32位的低12位：加法放置
    ```

    如果低 12 位第一位为 1，而addi指令中将最高位理解为符号位，表示负数。
    需要在低 12 位的上一位再加一，抵消负数。
    即正确情况应该为：

    ```asm
    lui   s3, 977       # 低32位的高20位：lui放置
    addi  s3, s3, 2304  # 低32位的低12位：加法放置
    ```

### SB 型指令

SB 型指令表示分支寻址。

Branch Addressing：  
SB-type 中立即数没有第 0 位，默认为 0。  
跳转地址 = PC + 偏移值 = PC + 立即数\*2  
RISC-V 代码中的数值为实际跳转量，指令封装时的数值为省略末尾 0 的结果。

**SB-format**

操作：条件分支指令（如 `beq`, `bne`, `blt` 等）。

| imm[12 / 10:5] | rs2    | rs1    | funct3 | imm[4:1 / 11] | opcode |
| -------------- | ------ | ------ | ------ | ------------- | ------ |
| 7 bits         | 5 bits | 5 bits | 3 bits | 5 bits        | 7 bits |

立即数拼接方式（12 位有符号偏移，按 2 字节对齐，实际范围 ±4KB）：

`imm[12]（符号位） | imm[10:5] | imm[4:1] | imm[11]`


最终形成：`imm[12:1]`，最低位 `imm[0]` 隐含为 0（因为指令地址总是 2 字节对齐）。
跳转目标地址 = PC + sign_extend(imm[12:0])

给定 C 代码，SB 指令和 UJ 指令不唯一，因为是相对于当前 PC 的跳转。

如果 branch 中需要跳转到 L1，但跳转的范围超过 bne 的范围，可以先跳转到 L2，再用 jal 跳转到 L1。

### UJ 型指令

UJ 型指令表示无条件跳转（如 `jal`）。

Jump Addressing：  
UJ-type，二十位立即数，跳转可以很远。第 0 位也默认为 0。

对更长的跳转：先用 lui 将地址存到临时寄存器，再用 jalr 加上基址并跳转。

**UJ-format**

| imm[20 / 10:1 / 11 / 19:12] | rd     | opcode |
| --------------------------- | ------ | ------ |
| 20 bits                     | 5 bits | 7 bits |

立即数拼接方式（20 位有符号偏移，按 2 字节对齐，实际范围 ±1MB）：

`imm[20] | imm[10:1] | imm[11] | imm[19:12]`

最终形成：`imm[20:1]`，`imm[0]` 隐含为 0。
跳转目标地址 = PC + sign_extend(imm[20:0])
跳转后的返回地址（PC + 4）写入 `rd`（通常为 `x1`，即 `ra`）

## 指令的执行

### 程序的调用

Bacis Block（基本块）：不包含任何跳转，一定是顺序执行  
编译器会识别基本块，对其做加速  
没有调用其他函数，称为 leaf procedure

Procedure/Function：程序的调用  
调用存储的子进程，利用传入的参数实现特定的功能  
步骤：

1. 将参数放在函数能访问到的位置（可能是存储器或寄存器）
2. 通过 jump 指令将控制权传给 procedure
3. 取出需要的存储资源
4. 执行任务
5. 将返回结果放在调用者（主程序）能访问到的位置
6. 将控制权换给主程序

调用者称为 caller，用 jal（jump and link）调用  
`jal x1, ProcedureAddress` 将 ProcedureAddress+4 放在 x1（因为 ProcedureAddress 是要跳转到的指令，回来时回到下一条，即 +4 的位置），然后跳转到 ProcedureAddress。  
ProcedureAddress 可以放偏移值或 label。

被调用者称为 callee，用 jalr（jump and link register）返回  
`jalr x0, 0(x1)` 跳转到 x1 的位置。  
为什么用 x0？此时执行到最后一条，但如果要跳转进入这个函数必须从头进入，所以当前位置肯定不需要存储。x0 不会改变，所以用 x0。

!!! normal-comment "jalr 和 jal 能不能互换使用？"

    caller 能不能用 jalr？可以，只要把要跳转的地址换为绝对寻址。
    callee 能不能用 jal？不可以，因为调用时跳转地址固定，但返回时地址不固定。

### 堆栈

a0~a7 (寄存器 x10~x17) 是 8 个用于存储参数和返回值的寄存器；  
ra (寄存器 x1) 用于存储跳转后返回的地址

压栈时从高地址向低地址压，栈顶在高地址，压栈后栈顶指针（sp）下移  
压栈：先下移栈顶、再 store，以 8 为单位，如果一次压多个则移动 8 的倍数  
出栈：先 load、再上移栈顶，以 8 为单位，如果一次出多个则移动 8 的倍数  
pop 的最后一步一定是跳转回 x1

!!! examples "示例 push 和 pop"

    Push： sp = sp - 8

    ```asm
    addi sp, sp, -8
    sd   ..., 0(sp)
    ```

    存储多个寄存器：

    ```asm
    addi  sp, sp, -24
    sd    x5, 16(sp)
    sd    x6, 8(sp)
    sd    x20, 0(sp)
    ```

    Pop: sp = sp + 8

    ```asm
    ld   ..., 0(sp)
    addi sp, sp, 8
    ```

    弹出多个寄存器：

    ```asm
    ld    x20, 0(sp)
    ld    x6, 8(sp)
    ld    x5, 0(sp)
    addi  sp, sp, 24
    ```

leaf procedure 不管外部的程序，只管内部改变了哪些寄存器，保存这些值并执行后返回。  
但部分寄存器没有被调用者用到，这些寄存器的压栈和弹栈是不必要的，有很多额外的保存操作。  
为了提高效率，约定两类寄存器：  
t0~t6: 7 temporary registers，调用的函数中不保存  
s1~s11: 12 saved registers，调用的函数中会保存

caller 将 t 或 s 寄存器压栈；callee 将 ra 和 a 寄存器压栈。

| Name            | Register no. | Usage                         | Preserved on call |
| --------------- | ------------ | ----------------------------- | ----------------- |
| x0(zero)        | 0            | The constant value 0          | n.a.              |
| x1(ra)          | 1            | Return address(link register) | yes               |
| x2(sp)          | 2            | Stack pointer                 | yes               |
| x3(gp)          | 3            | Global pointer                | yes               |
| x4(tp)          | 4            | Thread pointer                | yes               |
| x5-x7(t0-t2)    | 5-7          | Temporaries                   | no                |
| x8(s0/fp)       | 8            | Saved/frame point             | Yes               |
| x9(s1)          | 9            | Saved                         | Yes               |
| x10-x17(a0-a7)  | 10-17        | Arguments/results             | no                |
| x18-x27(s2-s11) | 18-27        | Saved                         | yes               |
| x28-x31(t3-t6)  | 28-31        | Temporaries                   | No                |
| PC              | -            | Program counter               | Yes               |

!!! examples "示例 嵌套过程"

    C Code for n!:

    ```c
    int fact(int n) {
        if (n < 1)
            return 1;
        else
            return (n * fact(n - 1));
    }
    ```

    RISC-V code

    ```asm
    fact:
        addi  sp, sp, -16   # 分配两个寄存器的占空间
        sd    ra, 8(sp)     # ra 保存返回地址
        sd    a0, 0(sp)     # a0 保存参数 n
        addi  t0, a0, -1    # t0=n-1
        bge   t0, zero, L1  # 若 t0=n-1>= 0，即 n>=1，跳到 L1
        addi  a0, zero, 1   # 否则返回 1（阶乘终止条件）
        addi  sp, sp, 16    # 回收栈空间
        jalr  zero, 0(ra)   # 返回调用者

    L1:
        addi  a0, a0, -1    # n=n-1
        jal   ra, fact      # 调用 fact(n-1)
        add   t1, a0, zero  # t1=fact(n-1)
        ld    a0, 0(sp)     # 取回原来的 n
        ld    ra, 8(sp)     # 取回返回地址
        add   sp, sp, 16    # 回收栈帧
        mul   a0, a0, t1    # a0=n*fact(n-1)
        jalr  zero, 0(ra)   # 返回
    ```

    为什么 fact 中 ra 要保存？因为这一次由其他函数调用 fact，要返回调用者的位置；但 fact 会递归调用，内部 ra 会覆盖外部调用者的 ra。因此在刚进入函数时要保存外部的 ra。同理，外部调用者和当前函数都会改变 a0，因此也要在开头保存 a0。
    为什么要区分保存和不保存的寄存器？提高执行效率。

父函数保证子函数能随便使用临时寄存器，返回给父函数时可以被改变；  
子函数保证返回给父函数保存的寄存器存储计算的值。

当程序调用一个函数时，系统会在栈上为这个函数开辟一小块区域，专门用来保存参数、返回地址、局部变量、临时寄存器保存区、前一个函数的帧指针。
这整一块区域就叫做一个栈帧（stack frame），也称调用帧（call frame）。

- sp（栈指针）：指向当前栈顶，每当程序在栈上分配或释放局部变量、保存寄存器、压入参数时，sp 都会相应地移动。
- 在大多数体系结构（包括 RISC-V、ARM、x86）中，栈是向低地址增长的：栈向下长，每压入一个值，sp 递减。
- fp（帧指针，基址指针）：指向当前函数的栈帧的固定基准位置，用于访问局部变量、参数、保存寄存器等。
- sp 在函数执行过程中可能多次变化（push/pop），所以编译器会额外用 fp 记录该函数栈帧的起始参考点，这样变量访问有固定偏移。在进程调用时 sp 往后移，但 fp 不变。

### 内存分布

- Text：程序代码
- Static data：全局变量、常数数组、常数字符串
- Dynamic data：堆（heap）
- Stack：自动分配的内存

堆和栈的区别：

| 对比项目     | 栈（Stack）                                          | 堆（Heap）                                              |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------- |
| **管理方式** | 由编译器 / CPU 自动管理（函数调用自动分配/释放）     | 由程序员或运行库手动管理（`malloc/new`，`free/delete`） |
| **存储内容** | 函数调用信息：局部变量、参数、返回地址、保存寄存器等 | 动态分配的内存（如数组、对象、链表节点等）              |
| **分配时机** | 编译期确定大小，运行时快速分配                       | 运行时动态决定大小                                      |
| **分配速度** | 非常快（CPU 直接改 `sp`）                            | 较慢（需要系统调用 / 管理空闲块）                       |
| **生命周期** | 随函数调用自动创建、结束时自动释放                   | 程序员控制（或由垃圾回收机制控制）                      |
| **空间大小** | 较小（如几 MB）                                      | 较大（可占整个剩余内存）                                |
| **增长方向** | 高地址向低地址                                       | 低地址向高地址                                          |
| **典型错误** | 栈溢出（stack overflow）                             | 内存泄漏（memory leak）                                 |

以内存从低地址到高地址为例（以 Linux / RISC-V / x86_64 为例）：

```
高地址 ↑
────────────────────────────
|   栈 Stack (局部变量、返回地址)    | ← 向下增长（从高地址往低地址）
|------------------------------------|
|             ↓                      |
|            ↑                       |
|   堆 Heap (malloc/new分配区)        | ← 向上增长（从低地址往高地址）
|------------------------------------|
|   全局/静态数据区 (.bss, .data)     |
|------------------------------------|
|   代码区 (.text)                    |
────────────────────────────
低地址 ↓
```

!!! normal-comment "gp 和 tp"

    - gp (global pointer，全局指针)：是编译器自动管理的一个指针，指向全局静态数据区的中间位置，用于快速访问全局变量 / 静态变量。
    - tp (thread pointer，线程指针)：指向当前线程的线程控制块或线程局部存储区域。

!!! normal-comment "指令中 lw 和 lwu"

    读入 32 位但寄存器 64 位，需要把读入的 32 位扩展为 64 位寄存器。
    lwu 指令：高 32 位自动补零；lw 指令：高 32 位自动补符号位。

!!! normal-comment "相对寻址和绝对寻址"

    相对寻址为相对于当前的 PC 偏移。如 jal 指令 `jal x1,100`，跳转到当前 PC+100；
    绝对寻址为给定寄存器和偏移值。如 jalr 指令 `jalr x1,100(x5)`，跳转到 x5+100。

示例：字符串拷贝

```asm
strcpy: addi  sp, sp, 8
        sd    s3, 0(sp)         # 寄存器保存i
        add   s3, zero, zero    # i初始化为零
    L1: add   t0, s3, a1        # t0=i+rs
        lbu   t1, 0(t0)         # t1取t0的字节
        add   t2, s3, a0        # t2=i+rd
        sb    t1, 0(t2)         # t1存储到目标寄存器
        beq   t1, zero, L2      # 到末尾则退出循环
        addi  s3, s3, 1         # i++
        jal   zero, L1          # 循环
    L2: ld    s3, 0(sp)         # 弹栈
        addi  sp, sp, 8
        jalr  zero, 0(x1)
```

在 leaf procedure 中没有条件跳转，编译器会先将所有临时寄存器都用完，再用保存的寄存器。

寻址方式：

- 立即数寻址：addi
- 寄存器寻址：add，从寄存器中取数
- 基址寻址：ld、sd，寄存器基址加上立即数，从内存中取数
- PC 相对寻址：beq， PC 加立即数，从内存中取数

### 几个示例

!!! examples "示例 swap"

    C code:

    ```c
    void swap(long long v[], size_t k) {
        long long temp;
        temp = v[k];
        v[k] = v[k + 1];
        v[k + 1] = temp;
    }
    ```

    步骤：

    1. 给函数变量赋寄存器
    2. 编写 body 部分代码
    3. 如有需要，恢复寄存器

    RISC-V code:

    ```asm
    swap:   slli  x6, x11, 3    # x6=k*8
            add   x6, x10, x6   # x6=&v[k]
            ld    x5, 0(x6)     # x5=v[k]
            ld    x7, 8(x6)     # x7=v[k+1]
            sd    x7, 0(x6)     # v[k]=x7=v[k+1]
            sd    x5, 8(x6)     # v[k+1]=x5=v[k]
            jalr  x0, 0(x1)     # return to calling routine
    ```

!!! examples "示例 冒泡排序"

    C code:

    ```c
    void sort(long long v[], size_t n) {
        size_t i, j;
        for (i = 0; i < n; i++) {
            for (j = i - 1; j >= 0 && v[j] > v[j + 1]; j -= 1) {
                swap(v, j);
            }
        }
    }
    ```

    外循环：

    `for (i = 0; i < n; i++)`

    ```asm
                lui   x19, 0            # i(x19)=0
    for1tst:    bge   x19, x11, exit1   # if i>=n(x11),exit
                (body of inner for-loop)
                addi  x19, x19, 1       # i++
                jal   x0, for1tst
    exit1:

    ```

    内循环：

    ```c
    for (j = i - 1; j >= 0 && v[j] > v[j + 1]; j -= 1) {
        swap(v, j);
    }
    ```

    ```asm
                addi  x20, x19, -1      # j(x20)=i-1
    for2tst:    blt   x20, x0, exit2    # if j<0,exit
                slli  x5, x20, 3        # x5=j*8
                add   x5, x10, x5       # x5=&v[j]
                ld    x6, 0(x5)         # x6=v[j]
                ld    x7, 8(x5)         # x7=v[j+1]
                ble   x6, x7, exit2     # if v[j]<=v[j+1],exit
                addi  x21, x10, 0       # store x10 in x21
                addi  x22, x11, 0       # store x11 in x22
                addi  x10, x21, 0       # first swap parameter is v
                addi  x11, x20, 0       # second swap parameter is j
                jal   x1, swap          # call swap
                addi  x20, x20, -1      # j-=1
                jal   x0, for2tst
    exit2:

    ```

    分配寄存器：

    ```asm
    sort:    addi  sp, sp, -40
                sd    x1, 32(sp)
                sd    x22, 24(sp)
                sd    x21, 16(sp)
                sd    x20, 8(sp)
                sd    x19, 0(sp)
    ```

    恢复寄存器：

    ```asm
    exit1:    ld    x19, 0(sp)
                ld    x20, 8(sp)
                ld    x21, 16(sp)
                ld    x22, 24(sp)
                ld    x1, 21(sp)
                addi  sp, sp, 40
    ```

## 了解内容

**同步一致性：**

现在用多核计算机，当两个核同时处理一个地址时可能出现读写不同步，会发生数据竞争/数据冒险（data race）。

Load reserved 指令：`lr.d rd, (rs1)`  
先读 rs1 中的值并放到 rd 中，在读取的内存地址上进行保护

Store conditional 指令：`sc.d rd, (rs1), rs2`  
将 rs2 中的值存到 rs1 的地址中，rd 表示 status。  
如果 lr.d 期间地址没有改变，则保存成功，rd 返回 0；否则如果地址改变，存储失败，rd 返回非零值。

!!! examples "示例 原子操作的交换"

    目标：将 x23 和 x20 中的值交换。

    ```asm
    again:  lr.d  x10, (x20)
            sc.d  x11, (x20), x23
            bne   x11, x0, again   # 如果失败则重试
            addi  x23, x10, 0
    ```

**程序的执行：**

compiler, assembler, linker, loader

动态链接：初始化时调用所有库，使用时只加载要用到的库。  
静态链接：每次使用时都加载所有库

**数组和指针：**

数组中取值：先将索引乘每个元素的大小，再加到基址上

```c
clear1(int array[], int size) {
    int i;
    for (int i = 0; i < size; i++) {
        array[i] = 0;
    }
}
```

```c
clear2(int *array, int size) {
    int *p;
    for (p = &array[0]; p < &array[size]; p += 1) {
        *p = 0;
    }
}
```

数组形式下，每次需要移位、加到地址上；而指针能直接指向地址，不用每次移位相加。

**MIPS、x86 和其他 RISC-V 指令：**

MIPS 和 RISC-V 相同：都有 32 位指令，32 个寄存器，0 号寄存器表示零，通过 load 和 store 访问内存

略。

基本整型指令：RV61I  
32 位指令（当寄存器为 32 位时用）：RV32I

标准扩展：M, A, F, D, C（略）

更高级的语言不一定带来更高的性能。  
汇编代码也不一定性能更高。

顺序的单词（或连续的字）并未存储在连续的地址上（每次 +4 而不是 +1）。  
在函数返回后仍保留指向自动变量的指针。

设计原则：

1. Simplicity favors regularity.
2. Smaller is faster.
3. Good design demands good compromises.
