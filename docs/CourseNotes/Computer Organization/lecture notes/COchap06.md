## Disks

Two major types of magnetic disks:

- Floppy disks: small capacity (not used);
- Hard disks: larger, higher density, higher data rate, more than one platter.

### Hard Disks

**The organization of hard disk:**

- Platters: disk consists of a collection of platters, each of which has two recordable disk surfaces;
- Tracks: each disk surface is divided into concentric circles (tracks);
- Sectors: each track is in turn divided into sectors, which is the smallest unit that can be read or written.

**Process to access data of disk:**

Seek the right track --> waits for the desired sector to rotate under the head --> transfer data from disk to memory --> notifies the processor upon completion.

Disk access time = seek time + rotation latency + transfer time + controller time.

### Measure Disk Performance

Manufacturers quote average seek time, but locality and OS scheduling lead to smaller actual average seek times.

Smart disk controller allocate physical sectors on disk (Logical sector abstraction).

Disk drives include caches: Prefetch sectors in anticipation of access; avoid seek and rotational delay.

- Dependability: overall trustworthiness of a system to deliver correct, safe, and secure service.
- Reliability: ability to operate correctly over time without failure (e.g., failure-free operation).
- Availability: proportion of time the system is up and able to provide service when needed.

Three measurements:

- MTTF: Mean Time to Failure;
- MTTR: Mean Time to Repair;
- MTRF: Mean Time Between Failures. MTRF + MTTF + MTTR.

### RAID Techneques

Redundant Arrays of Inexpensive Disks (RAID) is used to combine multiple drives into one logical unit to improve performance, increase capacity, and/or provide redundancy so data remains available if a disk fails (depending on the RAID level).

!!! remarks "RAID 0: No Redundancy"

    Data is striped across a disk array but there is no redundancy to tolerate disk failure. It also improves performance for large accesses, since many disks can operate at once.

!!! remarks "RAID 1: disk mirroring"

    Each disk is fully duplicated onto its "mirror". Can achieve very high availability.

    Cons: need two physical writes.

    RAID 2 is inefficient, therefore is not introduced here.

!!! remarks "RAID 3: Bit-Interleaved Parity Disk"

    A separate parity disk P contains sum of other disks per stripe mod 2 ("parity") If one disk fails, its data can be recovered using the remaining data disks and the parity disk.

    Cons: small read / small write. (Need to update every disk and the parity result in P.)

!!! remarks "RAID 4: Block-Interleaved Parity"

    Compare to RAID 3, parity by block instead of by bit.

    - Read: good
    - Large write: write both disks and the parity disk, good.
    - Small write: read old disk --> read old P --> update P --> write disk --> write P. Especially bad in parallel write. The parity disk becomes a performance bottleneck.

!!! remarks "RAID 5: High I/O Rate Interleaved Parity"

    Compared with RAID 4, parity information in RAID 5 is distributed across all disks, not stored on a single disk.

    - Good read performance due to parallel access to data disks.
    - Better write performance than RAID 4, since parity updates are spread across disks.

!!! remarks "RAID 6: P+Q Redundancy"

    RAID 6 extends RAID 5 by using two independent parity blocks, allowing the system to tolerate the failure of any two disks at the cost of additional storage overhead and write complexity.

## Buses

**Bus:** Shared communication link (one or more wires)

A bus contains two types of lines:

- Control lines: signal requests and acknowledgments, and to indicate what types of information is on the data lines
- Data lines: carry information between the source and the destination.

Bus transaction include two operations: input (device --> memory) and output (memory --> device).

!!! normal-comments "Output and Input"

    **Output:**

    1. Control lines signal a read request to memory, while the data lines contain the address;
    2. Memory access the data;
    3. Memory transfers data and signal data is available. The device stores data as it appears on the bus.

    **Input:**

    4. Control lines indicate a write request for memory, while the data lines contain the address;
    5. When the memory is ready, it signals the device, which then transfers the data. The memory will store the data as it receives it . The device need not wait for the store to be completed.

Type of buses:

- processor-memory: short high speed, custom design
- backplane: high speed, often standardized, e.g., PCI
- I/O: lengthy, different devices, standardized, e.g., SCSI

Common structure: A separate bus is used for processor-memory traffic. A small number of backplane buses tap into the processor-memory bus.

### Synchronous vs. Asynchronous

- Synchronous bus: use a clock and a fixed protocol, fast and small but every device must operate at same rate and clock skew requires the bus to be short.
- Asynchronous bus: don’t use a clock and instead use handshaking.

!!! normal-comments "Handshaking protocol"

    ![6_1](../resources/6_1.png)

    ![6_2](../resources/6_2.png)

!!! examples "Performance Analysis"

    Assume: The synchronous bus has a clock cycle time of 50 ns, and each bus transmission takes 1 clock cycle.The asynchronous bus requires 40 ns per handshake. The data portion of both buses is 32 bits wide.

    Question: Find the bandwidth for each bus when reading one word from a 200-ns memory.

    ---

    **Synchronous:** All pperations obey the clock, cannot overlap.

    - Send address (50ns) --> read memory (200ns) --> return data (50ns). Total time is 300ns.
    - Bandwidth = data size / time = 13.3MB/s.

    **Asynchronous:** Use request/acknowledge (handshaking), can overlap.

    - Send address (40ns) --> overlap with memory reading (200ns) --> three handshakes (3*40=120ns). Total time is 360ns.
    - Bandwidth = 11.1MB/s.

### Bus Arbitration

Bus masters initiate and control all bus requests.

1. First, the device generates a bus request to indicate to the processor that it wants to use the bus.
2. The processor responds and generates appropriate bus control signals.
3. The processor also notifies the device that its bus request is being processed as a result, the device knows it can use the bus and places the address for the request on the bus.

Two factors in choosing which device to grant the bus: bus priority and fairness.

## I/O Devices

Two methods used to address the device

- memory-mapped I/O: portions of the memory address space are assigned to I/O devices,and lw and sw instructions can be used to access the I/O port.
- special I/O instructions. exp: in al,port out port,al.

### Communication with Processor

- Polling: The processor periodically checks status bit to see if it is time for the next I/O operation.
- Interrupt: When an I/O device wants to notify processor that it has completed some operation or needs attentions, it causes processor to be interrupted.
- DMA (direct memory access): the device controller transfer data directly to or from memory without involving processor.

!!! remarks "DMA transfer"

    A DMA transfer need three steps:

    - The processor sets up the DMA by supplying some information, including the identity of the device, the operation, the memory address that is the source or destination of the data to be transferred, and the number of bytes to transfer.
    - The DMA starts the operation on the device and arbitrates for the bus. If the request requires more than one transferon the bus, the DMA unit generates the next memory address and initiates the next transfer.
    - Once the DMA transfer is complete, the controller interrupts the processor, which then examines whether errors occur.

!!! normal-comments "Comparison"

    Compare polling, interrupts, DMA:

    - The disadvantage of polling is that it wastes a lot of processor time. When the CPU polls the I/O devices periodically, the I/O devices maybe have no request or have not get ready.
    - If the I/O operations is interrupt driven, the OS can work on other tasks while data is being read from or written to the device.
    - Because DMA doesn’t need the control of processor, it will not consume much of processor time.

### I/O Performance Measures

- Supercomputer I/O Benchmarks
- Transaction Processing I/O Benchmarks: I/O rate (the number of disk access per second)
- File System I/O Benchmarks: MakeDir, Copy, ScanDir, ReadAll, Make, etc.

### Designing an I/O system

The general approaches to designing I/O system:

1. Find the weakest link in the I/O system, which is the component in the I/O path that will constrain the design.
2. Configure this component to sustain the required bandwidth.
3. Determine the requirements for the rest of the system and configure them to support this bandwidth.
