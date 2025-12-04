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

- Block (aka. line): unit of copying, maybe multiple words.
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

Each access contains: tag, index, byte offset. (Byte offset is determined by size of block. Index is the cache address, i.e. lower bits of memory block address. Tag is the higher bits of block address. Tag and index are concatenated to form block address.)

Each line in cache contains: index, valid bit, tag, data.

??? examples "E.g.1 cache access"

    8-blocks, 1 word/block, direct mapped. Access Sequence: 10110, 11010, 10110, 10010.

    ---

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
    #block \* (data size + tag size + valid size)
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

!!! remarks "Q1 Block placement"

    _Where can a block be placed in the upper level?_

    Fully Associative, Set Associative, Direct Mapped.

    - Direct mapped: block can only go in one place in the cache.
    - Fully associative: block can go anywhere in cache.
    - Set associative: block can go in one set of places in cache.

    In fully associative, cache has no index bits.

    Details on set associatice: A set is a group of adjacent blocks in cache. Index equals to block address mod(#sets). If each set has n blocks, the cache is said to be n-way set associative.

!!! remarks "Q2 Block identification"

    _How is a block found if it is in the upper level?_

    Tag/Block.

!!! remarks "Q3 Block replacement"

    _Which block should be replaced on a miss?_

    Random, LRU, FIFO.

!!! remarks "Q4 Write strategy"

    _What happens on a write?_

    Write Back or Write Through (with Write Buffer).
