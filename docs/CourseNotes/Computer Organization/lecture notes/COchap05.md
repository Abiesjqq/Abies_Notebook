## Memory Hierarchy Introduction

Programs may access any address space at any time.

Locality:

- Temporal locality: Items accessed recently are likely to be accessed again soon (e.g., loop).
- Spatial locality: Items near those accessed recently are likely to be accessed soon (e.g., sequential instruction access).

Taking advantage of locality:

- Copy recently accessed and nearby items from disk to smaller DRAM (main memory);
- Copy more recently accessed and nearby items from DRAM to smaller SRAM (cache, which is inside CPU).

More closer to CPU, faster, smaller, and more expensive.

### Terminology

- Block (aka. line): unit of copying, may be multiple words.
- Hit: accessed data is present in upper level.
- Hit time: the time to access the upper level of memory.
- Hit ratio: hits/accesses.
- Miss: not hit, need to copy block from lower level.
- Miss penalty: time taken to copy block (replace+deliver).
- Miss ratio: misses/accesses.

## Cache

Simple implementations: Each item of data at the lower level has exactly one location in the cache. Lots of items at the lower level shares locations in the upper level.

_Two issues: How do we know if a data item is in the cache? If it is, how do we find it?_

### Locate the data item!

**Direct-mapping algorithm**: memory address is modulo #(cache blocks).

Usually cache has $2^n$ blocks, so the cache index equals to the lowest $n$ bits of memory index.

### Check its presence!

_Multiple blocks share location, so how do we know which particular block is stored?_

**Tag**: Store memory address as well as its data. Since lower bits is the cache address, only need to store higher bits as memory address, called tag.

**Valid bit**: 1 if present, 0 if empty. Initialized as 0.

Components of three addresses:

- **Physics address (main memory address): tag / index / byte offset.** Byte offset is determined by size of block. Index is the cache address, i.e. lower bits of memory block address. Tag is the higher bits of block address. Tag and index are concatenated to form block address.
- **block address: tag / index** (main memory address deprived of offset).
- **Cache line: (index,) valid bit / tag / data.**

??? examples "E.g.1 cache access"

    8-blocks, 1 word/block, direct mapped. Access Sequence: 10110, 11010, 10110, 10010.

    ---

    The access sequence here refers to block address. index has 3 bits, thus tag has 2 bits.

    10110 --> valid=0 --> miss --> copy to cache (time locality) --> cache[110].valid=1, cache[110].tag=10, cache[110].data=Mem[10110] --> return data.

    11010 --> valid=0 --> miss --> copy to cache --> omitted.

    10110 --> valid=1, tag is the same --> hit --> return data.

    10010 --> valid=1, but tag is not the same --> miss --> replace --> cache[010].valid=1, cache[010].tag=10, cache[010].data=Mem[10010] --> return data.

??? examples "E.g.2 caceh size"

    64-bits addresses, directed mapped, $2^n$ blocks, $2^m$ words/block. Bits needed for each part? Total number of bits in cache?

    ---

    - Byte offset: $2^m$ words = $2^{m+2}$ bytes --> m+2 bits.
    - Cache index: $2^n$ blocks --> n bits.
    - Tag: all remaining bits --> 64-(n+m+2) bits.
    - Total size of cache:
    = #block \* (data size + tag size + valid size)
    = #block \* (#(words/block)\*32 + #(tag bits) + 1)
    = $2^n\times (2^m\times 32+63-n-m)$.

??? examples "E.g.3 cache size"

    How many total bits are required for a direct-mapped cache 16KB of data and 4-word blocks, assuming a 32-bit address?

    ---

    Total data size id 16KB = $2^{12}$ words, while each block contains $2^2$ words. So #blocks is $2^{10}$.

    In a block:

    - index: 10 bits
    - byte offset: s\*2=4 bits
    - tag: 32-10-4=18 bits
    - valid: 1 bit
    - data: 4\*32=128 bits

    Size of cache: $2^{10}\times (128+18+1)=147 Kbits$.

??? examples "E.g.4 cache size"

    Consider a cache with 64 blocks and a block size of 16 bytes. What block number does byte address 1200 map to?

    ---

    Block address = byte address / bytes per block = $\lfloor\frac{1200}{16}\rfloor$ =75.

    Index = block address modulo #(cache blocks) = 75 mod(64) = 11.

### Handle hits and misses?

**Read hits** is what we want.

**Read misses** has two cases: instrunction cache miss and data cache miss.

When instrction miss occurs: stall the CPU, fetch block from memory, deliver to cache, restart CPU.

**Write hits** lead to different strategies:

- write-back: only write into cache, and write back to memory later. Faster, but cause inconsistency (need dirty bit to mark eviction).
- write-through: write into both cache and memory. Slower (add write buffer to mitigate), but ensure consistency.

**Write misses**: read the entire block into the cache, then write the word. (See in Q4.)

### Q&As on Memory Hierarchy

**Q1 (Block placement): _Where can a block be placed in the upper level?_**

Fully Associative, Set Associative, Direct Mapped.

- Direct mapped: block can only go in one place in the cache.
- **Fully associative**: block can go anywhere in cache.
- **Set associative**: block can go in one set of places in cache.

In fully associative, cache has no index bits.

Details on set associatice: A set is a group of adjacent blocks in cache. Index equals to block address mod(#sets). If each set has n blocks, the cache is said to be n-way set associative.

**Q2 (Block identification): _How is a block found if it is in the upper level?_**

Use tag and valid bit.

Tag comparation: For fully-associative caches, compare the requested tag with every block's tag in the cache to determine hit or miss. For set-associative caches, compare with every block's tag in the set.

Index of puysical address: for set-associative caches, index has $\log_2(\#\text{sets})$ bits; for directed-mapped caches, index has $\log_2(\#\text{blocks})$ bits; for fully-associated caches, there are no index foeld.

**Q3 (Block replacement): _Which block should be replaced on a miss?_**

Random, LRU, FIFO.

In set-associative caches and fully-associative caches, there exists the replacement issue.

- **Random replacement**: randomly pick any block. Easy to implement, allocate uniformly, but may evict a block that is about to be accessed.
- **Least-recently used (LRU)**: pick the block in the set which was least recently accessed. Require extra bits to keep track of accesses.
- **First in, first out (FIFO)**: pick a block from the set which was first came into the cache.

**Q4 (Write strategy): _What happens on a write?_**

**Write hit**:

- **Write-through**: can always discard cached data, maintaining most up-to-date data in the memory.
- **Write-back**: can't just discard cached data cause may have to write it back to memory. Add dirty bits to cache control.

Advantages:

- write-through: read misses don't result in writes, memory hierarchy is consistent and it's simply to implement.
- write-back: write occur at speed of cache and main memory bandwidth is smaller when multiple writes occur to the same block.

**Write stall**: CPU wait for writes to complete during write-through.

**Write buffer**: A small cache that can hold a few values waiting to go to main memory. To avoid stalling on writes, many CPUs use a write buffer.

Write buffer does not entirely eliminate stalls.

**Write miss**:

- **Write allocate**: the block is loaded into the cache on a miss before anything else occurs.
- **Write around**: the block is only written to main memory, not stored in cache.

In general, write-back caches use write-allocate, and write-through caches use write-around.

!!! normal-comments "Write through + no write allocate"

    - Write through: when write hit, always write to both cache and the next layer (main memory or the next cache).
    - No write allocate: when write miss, write directly to memory, but not copy the block to cache.

    _Why use no write allocate?_

    Write through + no write allocate acts better in streamint write, where the written data will not be read again. In this case, write allocate will result in meaningless copy.

!!! normal-comments "Write back + write allocate"

    - Write back: when write hit, only write to cache, and the dirty bit of this block becomes 1. The block is write to memory until being evicted.
    - Write allocate: when write miss, first allocate the block from memory to cache, then write to the cache.

    _Why use write allocate?_

    Write back + write allocate acts better in write-and-read case. In this case, no write allocate will result read miss when reading the same block, thus increasing time.

??? examples "E.g.5 compare three mapping strategy"

    Three small caches, four one-word blocks per cache. One cache is direct-mapped, the second is two-way set associative, and the third is fully associative.

    Access sequence: 0, 8, 0, 6, 8.

    ---

    Direct-mapped: 5 misses, because 0 and 8 share the same position in cache.

    Two-way associative: all data stored in set 0, but each set has 2 blocks. 4 misses and 1 hit.

    Fully associative: 3 misses and 2 hits.

??? examples "E.g.6 cache size"

    Assume cache size is 4K Block, block size is 4 words, physical address is 32bits. Find the total number of tag bits for 4-way associativity.

    ---

    - number of cache sets: $2^{12}$/4 = $2^{10}$
    - Index: 10 bits
    - Offset: 4 bits
    - Tag: 32-10-4 = 18 bits
    - Total bits for tag: 18\*4K = 72 Kbits

### Measure Cache Performance!

- Average_memory_access_time = hit_time + miss_time  
  = hit_rate \* cache_time + miss_rate \* memory_time

Use CPU time to measure cache performance.

- CPU_time = (CPU_execution_clock_cycle + Memory_stall_clock_cycles) \* Clock_cycle_time.

In which:

- CPU_execution_clock_cycle = CI \* CPI \* Clock_cycle_time.

- Memory_stall_clock_cycles = #instrctions \* miss_ratio \* miss_penalty  
  = Read_stall_cycles + Write_stall_cycles.

For read stall:

- Read_stall_cycles = Read_per_program \* Read_miss_rate \* Read_miss_panelty.

For a write-through plus write buffer scheme:

- Write_stall_cycles = (Write_per_program \* Write_miss_rate \* Write_miss_panelty) + Write_buffer_stalls.

In most write-through cache organizations, the read and write miss penalties are the same.

??? examples "E.g.7 calculate cache performance"

    Assume:

    - instruction cache miss rate: 2%
    - data cache miss rate: 4%
    - CPI without any memory stalls: 2
    - miss penalty: 100 cycles
    - The frequency of all loads and stores in gcc: 36%

    How faster a processor would run with a perfect cache?

    ---

    - Instruction miss cycles: 2%\*CI\*100 = 2CI
    - Data miss cycles: 4%\*(CI\*36%)\*100 = 1.44CI
    - Total memory-stall cycles: 3.44CI

    CPI with stall: CPI with perfect cache + total memory-stalls = 5.44CI

    ---

    When CPU is faster, total memory-stall cycles increases, thus the increase in computer performance is less than proportional to the increase in CPU frequency.

### Improve Cache Performance!

!!! remarks "Sol.1 More flexible placement of blocks to reduce cache misses"

    See in Q1.

!!! remarks "Sol.2 Choosing which block to replace"

    See in Q2.

!!! remarks "Sol.3 Choosing different block size"

    Larger blocks should reduce miss rate, but fewer blocks means more competition and may increase miss rate as well.

    Larger blocks exploit spatial locality. In practice, use split caches because there is more spatial locality in code.

!!! remarks "Sol.4 Designing the memory system to support cache"

    Bandwidth: transferred words / time panelty

    **Performance in wider main memory**: When width of main memory increases, transfer times decrease and bandwidth increases.

    **Performance in four-way interleaved memory**: parallel access to four memory banks.

!!! remarks "Sol.5 Reducing miss penalty with multilevel caches"

    Add a second level cache: often primary cache is on the same chip as the processor. Use SRAMs to add another cache above primary memory (DRAM). Miss penalty goes down if data is in 2nd level cache.

    ??? examples "E.g. multilevel caches miss panelty"

        CPI of 1.0 on a 5GHz machine with a 2% miss rate, 100ns DRAM access. Adding 2nd level cache with 5ns access time decreases miss rate to 0.5%. Calculate the decreasement of CPI.

        ---

        - Clock cycle time: 0.2ns.
        - Miss panelty to main memory: 100ns/0.2ns = 500 cycles.

        CPI equals execution cycles plus stall cycles:

        - Total CPI with one level cache: 1.0+2%\*500 = 11 cycles.
        - Miss panelty to the 2nd cache: 5ns/0.2ns = 25 cycles.
        - Total CPI with two levels cache: 1.0+2%\*25+0.5%\*500 = 4 cycles.

        The processor is faster by: 11/4 = 2.8.

!!! remarks "Sol.6 Software optimization blocking"

    Interact with software. Misses depend on memory patterns.

## Virtual Memory

Virtual memory acts like a cache between disk and main memory (DRAM). There's also a TLB (SRAM) to accelerate the searching.

Terminology:

- VA: virtual address, generated by CPU;
- VPN: virtual page number, stemming from VA;
- PPN: physical page number, map from VPN by pagetable;
- PA: physical address, comtaining PPN.

Core idea:

CPU generate VA from instruction --> get VPN from VA --> map VPN to PPN using page table --> combine PPN and offset to get PA --> read page in main memory.

### Process

!!! normal-comments "VA to VPN?"

    VA is composed by: **VPN (higher bits) | page offset (lower bits)**.

    The key is to determine the bits for VPN and offset.

    - Offset bits is decide by page size. If one page has $2^k$ bytes, then offset has $k$ bits.
    - VPN bits is total VA bits minus offset bits.

    VPN is used to find the corresponding PPN by pagetable, and offset keeps the same in transfer process, which is used to pinpoint the specific byte in a page.

!!! normal-comment "VPN to PPN?"

    - Page table: a table to record mapping from VPN to PPN;
    - Entry: one line in page table;
    - Page: an area to store data, e.g., virtual page and physical page.

    VPN directly serves as index of page table. Each entry contains PPN, valid bit, dirty bit, etc. (Compared with cache, page table uses "direct mapping" strategy.)

    Page fault occurs when the page table entry is invalid (page not in memory) or when access violates permissions (e.g., not readable). On a page fault, the CPU traps to the OS; the OS pauses the process, brings the page from disk into memory if needed, updates the page table, and then resumes the instruction.

    Virtual pages are more than physical pages. Page faults cause huge miss panelty, thus pages are faily large (e.g., 4KB). We can handle the faults in software instead of hardware. Using write-through is too expensive, so we use write back.

!!! normal-comment "TLB?"

    TLB (Translation Lookaside Buffer) is a small and fast cache for page table, usually SRAM.

    Each TLB entry contains VPN, PPN, valid bit, etc. TLB can be fully associative, set associative or directed-mapped. Divide VPN into tag and index to do the search.

    - TLB hit (read): get PPN, skip to the next step.
    - TLB miss: search in page table. If the set in TLB is full, replace using LRU (last recently used), MRU (most recently used), FIFO (first in first out), or Random rule.

    With TLB, page fault will only occur if both TLB and page table miss.

!!! normal-comment "PPN to PA?"

    Offset remains the same during mapping. Combine PPN and offset (generated by VA) and get PA.

!!! normal-comment "PA to cache?"

Divide PA into `tag | index | offset`, search in cache.

![Memory hierarchy](../resources/5-1.png)

![TLB and cache](../resources/5-2.png)

### Remarks

_What about writes?_

Must use write-back strategy. The dirty bit is set when a page is first written. If dirty bit is 1, the page must be written back to disk before being replaced.

Trends:

- Synchronous SDRAMs (provide a burst of data)
- Redesign DRAM chips to provide higher bandwidth or processing
- Restructure code to increase locality
- Use prefetching (make cache visible to ISA)

!!! remarks "Calculation"

    Cache:

    1. Size of DRAM = #(blocks in DRAM) x block size.
    2. Physical address bits = $\log_2 size\, of\, DRAM$.
    3. Offset bits = $\log_2 block\, size$.
    4. Index bits = $\log_2 #blocks$.
    5. Tag bits = physical address bits - offset bits - index bits.
    6. Number of blocks = data size / size of data in each block.
    7. Cache size = #blocks x ((valid bit + )tag bits + data bits).


    Virtual memory:

    1. Number of entries: $2^{VPN\, bits}$.
    2. Size of page table = #entries x entry bits.
    3. Offset bits = $\log_2 page\, size$.
    4. Size of virtual memory: $2^{VA\, bits}\text{ bytes}$.
    5. Number of virtual pages: size of virtual memory / page size.

!!! remarks "Five techniques to reduce page table size"

    1. Multi-level Paging
    2. Inverted Page Table
    3. Larger Page Size
    4. Page Table Entry Compression / Sharing
    5. egmented Paging（分段分页）

??? examples "E.g.8 page table size"

    Assume virtual page number is 32 bits, page size is 4KB, and each entry is 4 bytes. Calculate the number of page table entries and the size of page table.

    - Number of entries: $2^{32}$
    - Size of page table: 4\*#entry = $2^{34}$ bytes

    ---

    Assume virtual address is 32 bits, page size is 4KB, and each entry is 4 bytes. Calculate the number of page table entries and the size of page table.

    - Page size: $2^{12}$ bytes
    - Page offset: 12 bits
    - Virtual page number: virtual_address-page_offset=32-12 = 20 bits
    - Number of entries: $2^{20}$
    - Size of page table: $2^{22}$ bytes

??? examples "E.g.9 size of page table"

    Consider a virtual memory system with the following properties: 36-bit virtual address, 4KB pages, 32-bit physical address.

    What is the total size of the page table for each process on this processor, assuming that the valid bit and dirty bit are in use? ( assuming that disk addresses are not stored in the page table).

    ---

    - Page offset: 12 bits
    - Virtual page number: 36-12 = 24 bits
    - Number of entries: $2^{24}$
    - Entry size: 1+1+20 = 22 bits
    - Size of page table: 22\*$2^{24}$ bits
