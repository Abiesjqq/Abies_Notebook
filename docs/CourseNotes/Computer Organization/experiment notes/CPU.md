!!! warning-box "注意"

      本文部分由 AI 生成。

《Lab02—建立 CPU 调试测试环境》详细描述了浙江大学《计算机组成与设计》课程实验中搭建的**单周期 RISC-V SoC（System on Chip）架构**。下面是对该 CPU 及整体 SOC 架构的完整解析。

## 🧠 一、整体架构概览

实验目标是：

> **基于 RISC-V 单周期 CPU 核心（SCPU），使用 Vivado 集成多个外设 IP 核，建立一个可调试、可测试、可显示的简易 SoC 系统。**

其顶层模块名为 **`CSSTE.v`**（Computer System - Single-cycle processor Test Environment）。

系统由 **11 个主要模块（U1~U11）** 构成：

| 模块代号 | 模块名称       | 功能简述                                       |
| -------- | -------------- | ---------------------------------------------- |
| **U1**   | `SCPU`         | 单周期 RISC-V CPU 核心                         |
| **U2**   | `ROM_D`        | 指令存储器（I_mem）                            |
| **U3**   | `RAM_B`        | 数据存储器（D_mem）                            |
| **U4**   | `MIO_BUS`      | CPU 与外设/存储器之间的总线接口                |
| **U5**   | `Multi_8CH32`  | 8 通道 32 位数据多路选择器，用于数码管调试显示 |
| **U6**   | `Seg7_Dev`     | 七段数码管显示驱动                             |
| **U7**   | `SPIO`         | GPIO/LED 显示模块                              |
| **U8**   | `clk_div`      | 时钟分频模块（提供全速/自动单步/手动单步）     |
| **U9**   | `SAnti_jitter` | 按键/开关去抖动模块                            |
| **U10**  | `Counter_x`    | 通用三通道计数器外设                           |
| **U11**  | `VGA`          | VGA 显示模块，用于调试信号显示                 |

---

## 🧩 二、CPU 核心（U1：SCPU）

### 架构类型：

- **RISC-V RV32I 单周期处理器**
- 支持六种指令类型：R / I / S / B / U / J
  共约 **26 条基础指令**（add、sub、lw、sw、beq、jal、lui 等）

### 核心组成模块：

| 组成单元             | 功能                                             |
| -------------------- | ------------------------------------------------ |
| **PC（程序计数器）** | 保存当前指令地址                                 |
| **IFU（取指单元）**  | 从 ROM 中取出指令                                |
| **IDU（译码单元）**  | 解析操作码，生成控制信号                         |
| **ALU**              | 实现算术逻辑运算（add、and、slt 等）             |
| **Register File**    | 32 个通用寄存器（x0~x31）                        |
| **CU（控制单元）**   | 生成控制信号：MemRW、RegWrite、Branch、ALUSrc 等 |
| **中断接口**         | INT 信号输入（后续实验实现）                     |

### 外部接口：

```verilog
input  wire [31:0] inst_in,  // 指令输入
input  wire [31:0] Data_in,  // 数据输入（从RAM/IO）
output wire [31:0] PC_out,   // 程序计数器
output wire [31:0] Addr_out, // 数据访问地址
output wire [31:0] Data_out, // 写出数据
output wire Mem_RW;          // 存储器读写信号
```

---

## 💾 三、存储系统

### 1️⃣ 指令存储器 ROM（U2）

- 采用 Vivado IP “Distributed Memory Generator”
- 容量：`1024 x 32bit`
- 初始化文件：`I_mem.coe`
- **CPU 通过 PC_out[11:2]访问**，输出指令 inst[31:0]

---

### 2️⃣ 数据存储器 RAM（U3）

- 采用 Vivado IP “Block Memory Generator”
- 容量：`1024 x 32bit`
- 初始化文件：`D_mem.coe`
- 接口：

  ```verilog
  RAM_B(.clka(clk_m),
        .wea(data_ram_we),
        .addra(ram_addr),
        .dina(ram_data_in),
        .douta(ram_data_out));
  ```

---

## 🔗 四、系统总线 (U4: MIO_BUS)

负责连接 CPU、RAM 与外设的通信，是 SoC 的“枢纽”。

- 功能：

  - 地址译码：根据地址范围确定访问哪个从设备（ROM、RAM、LED、Seg7 等）
  - 数据通路：CPU 与外设、RAM 的数据交换
  - 控制信号生成：GPIOf0000000_we、GPIOe0000000_we、counter_we 等

### 地址映射：

| 地址范围                | 设备           | 模块    |
| ----------------------- | -------------- | ------- |
| 0x00000000 – 0x00000FFC | RAM 数据区     | U3      |
| 0xE0000000 – 0xEFFFFFFF | 七段数码管接口 | U5 + U6 |
| 0xF0000000 – 0xFFFFFFFF | GPIO & LED     | U7      |
| 0xFFFFFF04 – 0xFFFFFFF4 | 计数器接口     | U10     |

---

## 💡 五、外设子系统

### (1) `SPIO` —— GPIO + LED 模块（U7）

- 控制 16 个 LED 显示灯
- 地址：0xF0000000 – 0xFFFFFFFF
- 可同时输出 `counter_set` 控制信号至计数器

### (2) `Seg7_Dev` —— 七段数码管显示模块（U6）

- 地址：0xE0000000 – 0xEFFFFFFF
- 接收来自 Multi_8CH32 的数据并驱动 8 个数码管

### (3) `Multi_8CH32` —— 8 通道 32 位多路选择器（U5）

- 用于**调试显示切换**（SW[7:5]控制显示内容）
- 可显示：

  - CPU 指令字节地址（PC_out）
  - ROM 输出指令（inst）
  - ALU 结果
  - RAM 地址/数据
  - 计数器值
  - 等共 8 个通道内容

### (4) `Counter_x` —— 通用三通道计数器（U10）

- 可作定时/计时外设
- 地址：0xFFFFFF04 – 0xFFFFFFF4

### (5) `VGA` —— 调试显示（U11）

- 实时显示：PC、inst、ALU 结果、RAM 地址/数据等
- 分辨率 640x480，25MHz 点时钟

---

## 🕹️ 六、辅助模块

| 模块                | 功能                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------ |
| **U8 clk_div**      | 提供多模式 CPU 时钟：<br>• SW2, SW8 控制<br>• 全速 100MHz / 自动单步 / 手动单步(SW10 触发) |
| **U9 SAnti_jitter** | 消除按钮/拨码开关抖动，输出稳态信号 SW_OK、BTN_OK                                          |

---

## 🧭 七、系统运行机制

1. **取指阶段：**

   - CPU 输出 `PC_out` → ROM 返回 `inst_in`

2. **译码执行阶段：**

   - 控制器生成 `MemRW`、ALU 操作、寄存器控制信号

3. **访存阶段：**

   - 若访存指令（lw/sw），则通过 `MIO_BUS` 访问 RAM 或 I/O

4. **写回阶段：**

   - 结果写入寄存器或外设

5. **显示与调试：**

   - 通过 `Multi_8CH32 + Seg7_Dev` 或 `VGA` 输出状态信号

6. **人机交互：**

   - SW 控制显示通道、步进方式
   - LED 反映外设或程序状态

---

## ⚙️ 八、实验特性与运行方式

| 模式 | SW[8:2] 设置          | 功能 |
| ---- | --------------------- | ---- |
| 00   | CPU 全速运行          |      |
| 01   | 自动单步（2²⁴ 分频）  |      |
| 1X   | 手动单步（SW10 触发） |      |

| SW[7:5] | 数码管显示内容  |
| ------- | --------------- |
| 000     | CPU 程序输出    |
| 001     | PC 地址         |
| 010     | ROM 指令        |
| 011     | Counter 计数值  |
| 100     | ALU 输出地址    |
| 101     | CPU 数据输出    |
| 110     | RAM 数据输入    |
| 111     | PC 指令字节地址 |

---

## 🧩 九、架构总结图（逻辑关系）

```
         +----------------------+
         |     SCPU (U1)       |
         +---------+------------+
                   |
                   | inst_in (from ROM)
                   |
        +----------v----------+
        |    ROM_D (U2)       | ← 指令存储器
        +---------------------+
                   |
                   | Addr/Data
                   v
        +---------------------+
        |   MIO_BUS (U4)      | ← 地址译码/数据交换
        +---+---+---+---+-----+
            |   |   |   |
            |   |   |   |
      +-----v-+ |   |   +------+
      |  RAM_B | |   |   |Counter|
      |   (U3) | |   |   |  (U10)|
      +---------+ |   |   +------+
                  |   |
                  v   v
               +------+------+
               | GPIO / LED  |
               |  (U7, U5, U6)|
               +------+------+
                      |
                   +--v--+
                   | VGA |
                   +-----+
```

---

✅ **总结一句话：**

> 本实验搭建的 CPU 是基于 **RISC-V RV32I 单周期架构** 的教学 SoC，包含指令/数据存储、总线、GPIO、计数器、显示与调试模块，具备完整的输入输出与时序控制，是一个简化的教学级 **CPU + SoC 集成系统**。

---

## 实验过程注意事项

**生成 ROM 的流程：**

- IP Catalog -> 搜索 memory generator -> 选择 Distributed Memory Generator -> memory config 中设置为 ROM，设置存储单元数 Depth 为 1024、字长 Data Width 为 32 -> RST & Initialization 中选择 coe 文件 I_mem.coe -> OK ~~-> 下一个界面选择 Global~~ -> Generate
- 课件中顺序有误，memory config 中设置后不要点 OK……
- clk 引脚自动 disable，不用手动删除
- coe 文件路径不能有中文，要修改提供的文件夹名称
- 基于 lab0 的经验我选了 Global，但实际在 Synrhsis Opetions 似乎选 Out of Context per IP 更便于调试？

**生成 RAM 的流程：**

- 本实验中提供了接口定义和网表文件，不用自己创建！
- IP Catalog -> 搜索 Block Memory Generator -> Basic 中,memory type 选择 Single Port RAM -> Port A Options 中，设置 Width 为 32、Depth 为 1024，Enable Port Type 选择 Always Enabled -> 不勾选 Primitives Output Register -> OK
- 课件中提到初始化文档为 D_mem.coe，但实际上 ~~这个文档没有给~~ RAM 可不初始化，因此不用添加
- Operating Mode 决定读写在同一个地址时怎么选择，lab0 中选择 No change，但我这里选了 Read first？
- Primitives Output Register 会使输出时加寄存器，有一个时钟的延迟，这里不勾选
- RAM 中各个端口：
  - .clka(clk_m), // 存储器时钟，与 CPU 反向
  - .wea(data_ram_we), // 存储器读写，来自 MIO_BUS
  - .addra(ram_addr), // 地址线，来自 MIO_BUS
  - .dina(ram_data_in), // 输入数据线，来自 MIO_BUS
  - .douta(ram_data_out) // 输出数据线，来自 MIO_BUS
- 输入地址：wea 使能为写、输入数据，则数据写入 RAM；输入地址：wea 使能为读、输出数据。

**用.v 文件和.edf 文件设置模块：**

- Add or Create Design Sources -> Add Files -> 选择.v 文件和.edf 文件 -> Finish
- .v 文件定义接口，.edf 文件规定门级实现，两者必须一起添加，且文件名必须相同

本 lab 中已经提供的文件为：

> abies@sjqqq:/mnt/d/\_Courses/Computer Organization/Lab2_CPU_intro/OExp02-IP2SOC\$ ls
> A7.xdc IP I_mem.coe font_8x16.mem vga_debugger.mem
> abies@sjqqq:/mnt/d/\_Courses/Computer Organization/Lab2_CPU_intro/OExp02-IP2SOC$ cd IP
> abies@sjqqq:/mnt/d/\_Courses/Computer Organization/Lab2_CPU_intro/OExp02-IP2SOC/IP\$ ls
> Counter_x.edf MIO_BUS.v RAM_B.edf SAnti_jitter.v SPIO.edf VGA clk_div.edf
> Counter_x.v Multi_8CH32.edf RAM_B.v SCPU.edf SPIO.v VGA.edf clk_div.v
> MIO_BUS.edf Multi_8CH32.v SAnti_jitter.edf SCPU.v Seg7_Dev VGA.v

直接导入所有.v 文件和.edf 文件即可

**导出 IP 核：**

- Tools -> Create and Package New IP -> Package your current file -> 先新建文件夹，再设置文件夹路径 -> OK

**调用 IP 核：**

- Settings -> IP -> Repository -> 选择 IP 核路径 -> OK -> IP Catalog -> 搜索 IP 核名称 -> 选择 IP 核，勾选 Global？ -> Generate
- 本实验中 Seg7_Dev 需要调用工程文件的 IP，~~好像可以直接复制某些文件但我没搞懂 T_T~~ 直接导出 IP 核再调用完成了

**其他：**

- 上课给出的 IP/VGA/...src/new 中有 VgaDisplay.v 文件，里面固定了用于 VGA 显示的文件路径：D://vga_debugger.mem 和 D://font_8x16.mem。可能需要将这两个文件放到 D 盘下？
