## Memory Hierarchy Introduction

Programs may access any address space at any time.

Locality:

- Temporal locality: Items accessed recently are likely to be accessed again soon (e.g., loop).
- Spatial locality: Items near those accessed recently are likely to be accessed soon (e.g., sequential instruction access).

Taking advantage of locality:

- Copy recently accessed and nearby items from disk to smaller DRAM (main memory);
- Copy more recently accessed and nearby items from DRAM to smaller SRAM (cache, which is inside CPU).

More closer to CPU, faster, smaller, and more expensive.

## Cache

### Terminology

- Block (aka. line): unit of copying, may be multiple words.
- Hit: accessed data is present in upper level.
- Hit time: the time to access the upper level of memory.
- Hit ratio: hits/accesses.
- Miss: not hit, need to copy block from lower level.
- Miss penalty: time taken to copy block (replace+deliver).
- Miss ratio: misses/accesses.

### How to find?

**1. Locate the line in cache!**

There are three methods to locate a block in cache: fully associative, set associative, direct mapped.

- **Direct mapped**: block can only go in one place in the cache. Memory address is modulo #(cache blocks).
- **Fully associative**: block can go anywhere in cache. Cache has no index bits.
- **Set associative**: block can go in one set of places in cache. A set is a group of adjacent blocks in cache. Index equals to block address mod(#sets). If each set has n blocks, the cache is said to be n-way set associative.

**2. Check the particular block!**

_Multiple blocks share location, so how do we know which particular block is stored?_

**Tag**: Store memory address as well as its data. Since lower bits is the cache address, only need to store higher bits as memory address, called tag.

**Valid bit**: 1 if present, 0 if empty. Initialized as 0.

Components of three addresses:

- **Physics address (main memory address): tag / index / byte offset.** Byte offset is determined by size of block. Index is the cache address, i.e. lower bits of memory block address. Tag is the higher bits of block address. Tag and index are concatenated to form block address.
- **block address: tag / index** (main memory address deprived of offset).
- **Cache line: (index,) valid bit / tag / data.**

### How to read?

After the cache lookup, there are two possible outcomes: a read hit or a read miss.

**Read hit** is what we want. Read the cache line (block) containing the requested address from cache. The offset is then used to select the specific word within the cache block, and that word is returned to the processor.

**Read misses** has two cases, instrunction cache miss and data cache miss:

- **Instrunction cache miss**: stall the CPU, fetch block from memory, deliver to cache, restart CPU.  
- **Data cache miss**:


### How to write?


### Exercises



## Virture Memory

### Terminology

### How to find?

### How to read?

### How to write?

