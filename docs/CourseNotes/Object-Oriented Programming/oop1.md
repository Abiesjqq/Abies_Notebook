## Introduction

Bjarne Stroustrup.

## String

String类的用法：

- Assignment: `string str1 = "aaa"`
- Assign: `str.assign('ahgie')`
- Concatenation: `str3 = str1 + str2`, `str1 += str2`
- Constructors: `string(const string& s2, int pos, int len)`, `string(const char *cp, int len)`
- Sub-string: `substr(int pos, int len)`
- Modification: `assign()`, `insert(int pos, const string& s)`, `erase()`, `append()`, `replace(int pos, int len, const string& s)`
- Search: `find(const string& s)`

!!! normal-comments "string长度说明"

    string末尾没有`\0`，`string.length()`返回可见字符的长度。

## File I/O

```cpp
#include <fstream>

ofstream File1("out.txt");
File1 << "Hello world" << std::endl;

ifstream File2("in.txt");
std::string str;
File2 >> str;
```

Notice: ifstream will terminate in white spaces (space, tab, enter, etc.). Readline will get the whole line.

## Memory Model

内存存储分为几类：

- 全局/静态存储区：存储全局变量、静态全局变量、静态局部变量
- 栈区：存储局部变量、函数参数、返回值
- 堆区：存储动态分配的变量（new/malloc分配）
- 常量存储区：存储字符串常量、const常量
- 代码区：存储程序的机器指令

!!! normal-comment "局部变量和静态局部变量的区别？"

    相同点：两者都只在块内可见，块外无法访问。

    不同点：

    - 普通局部变量每次进入作用域时创建、离开作用域时销毁；静态局部变量只在第一次进入作用域时创建一次，之后多次调用并“记住上次的值”。
    - 普通局部变量存储在栈中，编译器自动管理；静态局部变量存储在静态存储区（数据段/BSS）。

!!! normal-comment "全局变量和静态全局变量的区别？"

    相同点：

    - 本文件中全局可访问
    - 都存储在静态存储区（数据段/BSS）

    不同点：全局变量可跨文件用`extern`引用；静态全局变量（加`static`）不能，只在当前.cpp文件可见

动态分配内存：

1. 分配指针：`int* p = new int()` --> `delete p`
   - `new int`表示分配但不初始化
   - `new int()`表示分配且初始化为0
   - `new int(5)`表示分配且初始化为5
2. 分配数组：`int* arr = new int[10]` --> `delete[] arr`
   - `new int[10]`表示分配但不初始化
   - `new int[10]()`表示分配且初始化为0
   - `new int[10]{1,2,3}`表示分配且前三个初始化、其余为0

new的原理：在堆上分配对应的内存，返回一个栈上的指针，指针中存储这块内存的起始地址、指向堆内存。

## Pointer to Objects

同C，用`*`表示指针，`&`表示取地址，`->`表示指针内函数调用。

注意：用一个指针给另一个指针，两者指向同一个对象

## Reference

引用相当于对变量的别名，作用与同一变量。可用于函数传参时代替指针。

几点注意：

- 指针可以改变指向的值，但引用不能改变，也不能为空
- 引用的对象必须有内存位置，不能引用临时变量
- 没有引用的引用，没有数组的引用，没有引用的指针

## Const

几点注意：

- 常量也是变量，遵循作用域规则，只是不能修改值
- 默认内部链接，即只在当前cpp文件中可见；如果加extern关键字，则能在其他文件中使用
- 编译器会尝试不分配存储空间，而是记录在符号表中，直接替换所有使用常量的地方。当extern或变量过大时，需要分配存储空间
- 常量在编译时就已经确定值，必须初始化（除非使用extern声明）
- 常量分为编译时常量和运行时常量，后者不能用于设定数组大小
- 指针和常量组合：const修饰左边最近的类型，如果左边没有则修饰右边最近的

```cpp
const int* p = &x;  // 能修改p指向的对象，但不能通过p修改x（const修饰int）
int const* p = &x;  // 和上一行等价（const修饰int）

int* const p = &x;  // 不能修改p指向的对象，但能通过p修改x（const修饰int*）

const int* const p = &x;  // 不能修改p指向的对象，也不能通过p修改x（第一个const修饰int，第二个const修饰int*）
int const* const p = &x;  // 和上一行等价（第一个const修饰int，第二个const修饰int*）
```
