
## Von Neumann Model

![alt text](image-1.png)

### Memory

For a $2^k \times m$ array of memory bits,

**Address** unique ($k$-bit) identifier of location  
**Contents** $m$-bit value stored in location

Basic operations: **LOAD** and **STORE**

Here we have **MDR** (Memory Address Register) and **MAR** (Memory Data Register)

To LOAD a location (A):  
1. Write the address (A) into the MAR.  
2. Send a “read” signal to the memory.  
3. Read the data from MDR.

To STORE a value (X) to a location (A):  
1. Write the data (X) to the MDR.  
2. Write the address (A) into the MAR.  
3. Send a “write” signal to the memory.

### Processing Unit

ALU and Temp.

**ALU** (Arithmetic and Logic Unit), LC-3 performs *ADD*, *AND* and *NOT*

**Registers** (Temp) Operands and results of functional units, LC-3 has eight registers (R0, …, R7), each 16 bits wide.

**Word Size** number of bits normally processed by ALU in one instruction, and it is also the width of registers.  
LC-3 is 16 bits.

### Input and Output

LC-3 supports keyboard (input) and monitor (output).

Keyboard has data register (**KBDR**) and status register (**KBSR**)  
Monitor has data register (**DDR**) and status register (**DSR**)

### Control Unit

Orchestrates execution of the program

**Instruction Register** (IR) contains the current instruction  
**Program Counter** (PC) contains the *address* of the next instruction to be executed.  
**Control Unit** reads an instruction from the memory, interprets the instruction and generates signals that tell the other components what to do  

### Instruction

One instruction specifies two things:  
**opcode** operation to be performed  
**operands** data/locations to be used for operation

An instruction is encoded as a sequence of bits. They are often encoded in a fixed length, such as 16 or 32 bits.

A computer’s instructions and their formats is known as its **Instruction Set Architecture** (**ISA**).

