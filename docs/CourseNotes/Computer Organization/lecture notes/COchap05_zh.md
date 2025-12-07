## 内存介绍

对内存的希望：size 和 speed

内存的基本要素：speed, cost per bit, volatility, endurance cycles  
机械硬盘、固态硬盘

集成电路工艺的发展，使芯片晶体管密度增加，功能更欠打，存储容量更大，成本更低

SRAM（静态存储）：将数值存储在反相器中，速度快，但相比 DRAM 所占空间更大。  
对任意位置的数据，访问时间固定，和 CPU 的时钟周期接近。

DRAM（动态存储）：将数值存储在电容中，需要不断刷新电路。  
体积小、密度高，但访问速度比 SRAM 更慢。

flash（闪存）：非易失性存储  
flash 分为 NOR flash（嵌入式系统）、NAND flash（USB、多媒体存储）  
Flash bits wears out after 1000's of accesses

Disk storage（机械硬盘）：非易失性，靠机械硬盘的旋转读取数据  
数据存储在轨道（track）的扇区（sector）中。每个扇区中包括 sector ID、数据、ECC（Error correcting code）  
从扇区中读取数据：（寻道）将磁头定位在正确的磁道上方 --> 旋转磁盘将要读的扇区转到磁头下方 --> 将数据 transfer 出来  
要会计算机械硬盘读取的时间！

## 层次存储技术

程序在任意时间都可能访问一小部分内存

局部性理论  
时间局部性：最近被访问的 item 很可能再次被访问（如循环中操作的变量、循环条件的变量）  
空间局部性：最近被访问的附近的 item 很可能再次被访问

将所有数据存储在硬盘上（disk memory），将最近访问的数据和附近的数据放在小的 DRAM 上（主存 main memory），将更近访问的和附近的数据放在更小的 SRAM 上（缓存 cache memory）  
越往上存储空间越小、价格越贵，但访问速度越快

层间搬运数据的最小单位为 block（或 line），可以是一个 word 也可以是多个 word。  
命中（hit）：从最上层存储器开始访问。如果访问的数据正好在上层存储中，则称为命中  
hit radio：命中次数/访问次数  
失效（miss）：访问数据不在上层存储中，则称为 miss  
miss 后，先将数据从下层存储 copy 到上层存储，再访问。  
miss penalty：额外花费的时间，搬运数据的时间 + 访问并传输数据的时间

高速缓存解决 speed 问题，虚拟存储解决 size 问题。

### Cache

Cache 解决了 CPU 和主存速度不匹配的矛盾。

对底层存储中的每一项，都在上层存储中有相应位置。  
e.g., lots of items at the lower level share locations in the upper level  
问题：怎么判断数据是否早 cache 内？如果在 cache 中，怎么找到数据？

cache 对空间局部性：从主存中取回待访问数据时，会同时取回与其位置相邻的主存单元的数据  
cache 对时间局部性：保存近期频繁被访问的主存单元的数据

Cache 地址映射机制：主存地址分为块地址和块偏移量，块地址分为标签（Tag）和索引（Index）。其中 Tag 判断数据是否在 cache，Index 决定在 cache 的哪一行读取数据。  
cache 的每行包含四部分：标签（Tag）、数据（Data）、一位 Valid、一位 Dirty。其中 Valid 表示是否有效，Dirty 表示是否是最近更新。  
映射方式：直接映射、组相连、全相连

直接映射：  
以下两种映射方法找到对应的数据块，两者等价：

1. <块地址> mod < cache 中的数据块的数量 >
2. 若 cache 中有 $2^n$ 个数据块，则索引为主存块地址的最低 n 位

下层很多元素在上层中共享同一个位置。  
通过索引字段找到 cache 的行，用 cache 行中的 tag 和主存中的 tag 匹配，检查 valid 和 dirty 是否是 1（1 表示有效），若全部匹配且有效则读取数据。

怎么将主存地址分为三部分？  
假设 cache 中有 $2^n$ 个 block，则 index 为 n 位。如果每个 block 中有 $2^m$ 个 word（$2^{m+2}$ 个 byte），则字节偏移量为 m+2。剩余的高位全部表示 tag。

cache 的一行中出现冲突？选择一个淘汰。

cache 的总大小包含 data、tag、valid 和 dirty 的位数。题目中所说的 cache 大小一般只表示数据的总位数。  
计算 cache 大小的题目必考！

!!! examples "Ex. Direct mapping in cache"

    Consider a cache with 64 blocks and a block size of 16 bytes. What block number dies byte address 1200 map to?

    ---

    First, get block address:

    $$\lfloor\frac{\text{Byte address}}{\text{Bytes per block}}\rfloor=75$$

    Second, get index:

    $$75\,\text{modulo}\,64=11$$

如果数据不在 cache 中，在主存中找。先直接送到 CPU，再将附近的 block 全部搬到 cache。

Read misses：分为 instruction cache miss 和 data cache miss  
指令失效：CPU stall，从主存中找到 block，搬到 cache，CPU restart。

cache 访问过程：

1. 写穿策略
2. 写回策略：可能导致 cache 和主存中存储数据不一致

直接映射的缺点：多个块在 cache 中共享位置，容易冲突，利用率低

cache 的利用率和块容量也有关系，容量更大的块可以通过挖掘空间局部性来降低失效率。但块容量大到一定程度，失效率也会升高（cache 中能放的块减少，块中各个字之间的空间局部性降低）。

!!! remarks "cache 映射"

    1. 直接映射：每个块只可能放到一个位置，用地址对块数取模得到位置。
    2. 全相连：块可能放到任意位置。
    3. 组相连：块可以放到一组位置，地址对组数取模得到位置。如果每组有 n 个块，则称为 n-路相连。

    若 cache 中有 m 组，则直接映射相当于 1 路相连，全相连相当于 m 路相连。

全相连中没有索引字段。

偏移量策略：

1. 随机：硬件上容易实现；可能替换即将使用的块。
2. Least-recently used (LRU)：替换最近最少使用的；需要额外的位来记录使用。
3. First in, first out (FIFO)：替换最先进入的块。

!!! remarks "写策略"

    1. 写穿策略：将数据写到主存
    2. 写回策略：只写到cache，不写到主存。替换cache时不能直接丢弃，可能还要写到主存中。

!!! remarks "写停止"

    CPU 可能需要等待写操作。

    做法：CPU 中插入 write buffer。但如果写的数据量超过 buffer 的量，不能完全消除写停止。

!!! remarks "写失效"

    如果要写的块是 not present，有两种方式：

    1. 写分配 (write allocate)：先将数据从主存加载到 cache 中
    2. 写不分配 (write around)：只将内容写到主存中，不写到 cache。

### Measuring and Improving Cache Performance

Measurement of cache performance:

$$\text{Average memory access time} = \text{hit time}+\text{write time}$$

$$\text{CPU time}=(\text{CPU exucetion clock cycles} + \text{Memory-stall clock cycles})\times \text{Clock cycle time}$$

$$\text{Memory-stall clock cycles}=\text{\# of instructions}\times\text{miss ratio}\times\text{miss panalty}$$

直接映射的缺点：如果冲突的块间隔访问，失效率很大。

??? examples "E.g.5"

    Three small caches, four one-word blocks per cache. One cache is direct-mapped, the second is two-way set associative, and the third is fully associative.

    Access sequence: 0, 8, 0, 6. 8.

    ---

    Direct-mapped: 5 misses, because 0 and 8 share the same position in cache.

    Two-way associative: all data stored in set 0, but each set has 2 blocks. 4 misses and 1 hit.

    Fully associative: 3 misses and 2 hits.

??? examples "E.g.6"

    Assume cache size is 4K Block, block size is 4 words, physical address is 32bits. Find the total number of set and total number of tag bits for n-way associativity.

    ---

    To be supplemented.


## 虚拟内存

虚拟内存中的拷贝单位称为页，转换失效称为页失效。