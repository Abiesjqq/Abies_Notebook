
## Assembly Language

Each line of the command is:  
- an instruction  
- an assembler directive
- a comment

A instruction has the following format:

```asm
LABEL OPCODE OPERANDS ; COMMENTS 
```

**Opcodes** are reserved symbols that correspond to LC-3 instructions. eg `ADD`, `LDR`

**Operands**  
- _registers_ are specified by `Rn`, where `n` is the register number.  
- _numbers_ are indicated by `#(decimal)` or `x(hex)`  
- _label_ is symbolic name of memory location (optional)

operands are separated by by comma (`,`)

```asm
LOOP ADD R1,R1,#-1
     BRp LOOP
```

**Pseudo-operations** are used by assembler, and they start with dot.

| Opcode   | Operand                  | Meaning                                                  |
|----------|--------------------------|----------------------------------------------------------|
| `.ORIG`    | address                  | starting address of program                              |
| `.END`     | —                        | end of program                                           |
| `.BLKW`    | n                        | allocate n words of storage (array)                              |
| `.FILL`    | n                        | allocate one word, initialize with value n               |
| `.STRINGZ` | n-character string       | allocate n+1 locations, initialize with characters and null terminator |

Chap Code

| Code | Equivalent  | Description                                                                 |
|------|------------|-----------------------------------------------------------------------------|
| `HALT` | `TRAP x25`   | Halt execution and print message to console.                                |
| `IN`   | `TRAP x23`   | Print prompt on console, read (and echo) one character from keyboard. Character stored in `R0[7:0]`. |
| `OUT`  | `TRAP x21`   | Write one character (in `R0[7:0]`) to console.                                |
| `GETC` | `TRAP x20`   | Read one character from keyboard. Character stored in `R0[7:0]`.              |
| `PUTS` | `TRAP x22`   | Write null-terminated string to console. Address of string is in R0.        |