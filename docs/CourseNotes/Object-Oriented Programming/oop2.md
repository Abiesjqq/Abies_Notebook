## Compile Unit

编译器每次只看到一个.cpp文件（及其包含的头文件），每个.cpp文件被编译成一个.obj（或.o）目标文件。然后由链接器将所有.obj文件链接成一个可执行文件。

_什么是预编译？_ 预编译执行纯文本操作，包括头文件展开、宏展开、条件编译、删除注释等。

_为什么需要头文件？_ 提供跨文件的信息共享，告诉编译器其他编译单元中存在的函数和类。头文件=接口（interface）

为防止多个.cpp文件中引用同一个头文件，导致重复编译，头文件需加：

```cpp
#ifndef HEADER_FILE
#define HEADER_FILE
// ...
#endif

// or
#pragma once
```

引用头文件有几种方式：

- `#include "xx.h"`：引用用户自定义的头文件，搜索顺序为当前目录-->编译器制定的其他目录
- `#include <xx.h>`：引用系统头文件，只搜索编译器指定的系统目录
- `#include <xx>`：等价于上一种

## Makefile

随着程序复杂度增加，需要分成多个文件。Makefile 是一种脚本文件，包含：

1. 项目结构：有哪些文件，它们之间的依赖关系
2. 创建指令：如何从源文件生成目标文件

make执行时，先将项目文件间的依赖关系构建成DAG（Directed Acyclic Graph），路径为.exe --> .o --> .c/.h。确定第一个目标，向下遍历，检查哪些需要重新创建；再从最底层的目标开始，逐层向上重建。

语法格式：

```makefile
target: dependent files
    command # 命令前必须用Tab缩进
```

!!! examples "makefile示例"

    要求：main.c和sum.h编译成main.o，sum.c和sum.h编译成sum.o，再链接成sum。

    ```makefile
    sum: main.o	sum.o  # 目标为可执行文件sum，依赖main.o和sum.o
        gcc –o sum main.o sum.o  # 命令为链接两个.o文件

    # .o默认包含.c文件，因此下面两条依赖文件中的.c文件可不写
    main.o: main.c sum.h
        gcc –c main.c  # -c表示只编译不链接

    sum.o: sum.c sum.h
        gcc –c sum.c
    ```

    ---

    自动变量：

    - `$@`：当前规则的目标
    - `$*`：当前规则的目标中，去掉后缀的部分
    - `$<`：第一个依赖文件
    - `$^`：所有依赖文件

    可以简化为：

    ```makefile
    sum: main.o sum.o
        gcc -o $@ main.o sum.o

    %.o: %.c sum.h
        gcc -c $< -o $@

    ```

    ---

    可用clear目标清理中间文件：

    ```makefile
    clean:
        rm -f *.o sum
    ```

    ---

    可以通过命令行中传入参数，在makefile中用`$(VAR_NAME)`接收，用条件判断语句确定编译哪些文件。e.g.

    ```makefile
    sum: main.o sum.o
        gcc –o sum main.o sum.o

    main.o: main.c sum.h
        gcc –c main.c

    #deciding which file to compile to create sum.o 
    ifeq ($(USE_SUM), 1)
    sum.o: sum1.c sum.h
        gcc –c sum1.c –o $@
    else
    sum.o: sum2.c sum.h
        gcc –c sum2.c –o $@
    endif
    ```

