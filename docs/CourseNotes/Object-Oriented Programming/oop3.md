## Memory

- stack: local vars    
- heap: dynamically allocated vars
- code/data: global vars, static global vars, static local vars

Global vars are vars defined outside any function, can be shared btw .cpp files.

`extern` is a declaration says there will be such a variable somewhere in the whole program.

Static global variable/function inhubit access from outside the .cpp file.

Static local variable keeps value in between visits to the same function.

## Pointer and Reference

`string s` will initialize, but `string *ps` will not.

引用r相当于对原变量的重命名，对r操作等价于对原变量操作，r不能重新绑定为其他变量。

引用在创建时就必须绑定在某个值，而指针创建时不一定初始化。

Restrictions:

- No references to references
- No pointers to reference, but reference to pointer is ok
- No arrays of references

## Dynamically Allocated Memory

New expression: `new int(10)`, `new int[10]`
Delete expression: `delete p`, `delete[] p`

new会调用构造函数、delete会调用析构函数，但malloc/free只操作内存。

E.g.:

```cpp
#include <iostream>
using namespace std;

struct Student {
    int id;
    Student() {
        id = 0;
        cout << "Student::Student()" << '\n';
    }
    ~Student() {
        cout << "Student::~Student() id = " << id << '\n';
    }
}

int main() {
    Student *ps1 = (Student*)malloc(sizeof(Student));
    Student *ps2 = new Student;
    free(ps1);
    delete ps2;

    Student *psarr = new Student[5];
    for (int i = 0; i < 5; i++)
        psarr[i].id = i;
    delete[] psarr;
}
```

## Constant

A const in C++ defaults to internal linkage. The compilor trie to avoid creating storage for a const, holding the value in its symbol table.

```cpp
const int n = 10;
int arr[n];  // ok

const int n;
cin >> n;
int arr[n];  // error
```

```cpp
int *const p = a;  // p is const
*p = 20;            // ok
p++;                // error

const int *p = a;   // (*p) is const
*p = 20;            // error
p++;                // ok

int const* p = a;   // equals to const int *p
```