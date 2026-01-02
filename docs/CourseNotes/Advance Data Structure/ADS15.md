# External Sorting

## Introduction

When query on a disk, need to find the track, sector, element and transmit sequentially. This process is slower than in internal memory and device-dependent.

- Tape: store data on tapes (can only be accessed sequentially). At least 3 tapes are used;
- Run: a sorted sequence in tape;
- Pass: one process of mergesort.

### Merge

!!! examples "2-way merge"

    Assume $M=3$ (#records stored in memory), $B=1$ (#records in each I/O).

    > Input (T1): 81 94 11 | 96 12 35 | 17 99 28 | 58 41 75 | 15

    Run generation: read 3 elements from T1, sort in memory, and write back to disk, which generate a run. Finally the original tape is seperated into multiple sorted runs.

    Assume runs are written on T2, T3:

    > T2: 11 81 94 | 17 28 99 | 15
    > T3: 12 35 96 | 41 58 75

    2-way merge: merge two runs into a larger run.

    After the first merge:

    > T1: 11 12 35 81 94 96 | 15
    > T4: 17 28 41 58 75 99

    After the second merge:

    > T2: 11 12 17 28 35 41 58 75 81 94 96 99
    > T3: 15

    After the third merge:

    > 11 12 15 17 28 35 41 58 75 81 94 96 99

    ---

    In $k$-way merge, use min-heap to sort.

!!! remarks "k-way merge"

    Time concerned: Time to read or write one block of records, to internally sort $M$ records, to merge $N$ records from input buffers to the output buffer.

    To reduce #passes, use $k$-way merge where $k$ is #tapes/2.

    !!! normal-comment "Why #tapes/2?"

        $k$ tapes used for input, and $k$ tapes used for output.

        In a single pass, only 1 tape is needed for output. But in the whole process, the output serves as the input of the next pass, thus need other tapes to output the new run.

    In general, assume number of data is $N$, length of each run is $M$, #tapes is $k+1$. The initial #runs is $N/M$. In $k$-way merge, each pass decrease #runs into $1/k$, thus #passes is $\lceil \log_k(N/M)\rceil$. The total #runs is

    $$1+\lceil \log_k(N/M)\rceil.$$

!!! remarks "Polyphase Merge"

    _Can we use 3 tapes for a 2-way merge?_

    A naive approach evenly distributes runs across two input tapes, but this causes one input tape to become empty early, forcing extra copy passes and wasting I/O.

    A smarter solution is polyphase merge, which distributes runs unevenly across tapes so that at every stage two tapes contain input runs and the third serves as output.This avoids copying and allows continuous merging, even with the minimum number of tapes.

    Claim: If the number of runs is a Fibonacci number $F_N$, then the best way to distribute them is to split them into $F_{N–1}$ and $F_{N–2}$.

    With this method, only $k+1$ tapes are needed for $k$-way merge.

### Buffer Handling

Buffer is a block-sized region in internal memory used to temporarily hold data read from or written to disk.

For normal operations, each I/O has at least 1 buffer; but for parallel operation, each I/O has at least 2 buffers.

!!! examples "E.g."

    Sort a file containing 3250 records, using a computer with an internal memory capable of sorting at most 750 records. The input file has a block length of 250 records. 

    1 block has 250 records, thus 1 buffer can hold 250 records. Memory / (size of buffer) = 3 buffers. 3 - 1 = 2. Can only do 2-way merge.

### Replacement Selection

_Can we generate a longer run with the same memory?_

It maintains a priority queue (typically a min-heap) of size $M$ in memory. At each step, the smallest element is output to the current run and replaced by a new input element. If the new element is smaller than the last output, it is frozen and deferred to the next run. This process continues until all elements in memory are frozen, at which point a new run begins.

??? examples "E.g."

    Input:

    > 81 94 11 96 12 35 17 99 28 58 41 75 15

    Output:

    > 12 17 28 35 41 58 75 99
    > 11 81 94 96
    > 15

The average length of run in replacement selection is $2M$.

(Each new input element has roughly a 50% chance of being greater than or equal to the last output element. Such elements can continue the current run, while the remaining elements are frozen for the next run. As a result, on average only half of the $M$ elements in memory become unavailable at any time, allowing the current run to extend to about twice the memory size, i.e., an average run length of approximately $2M$.
)