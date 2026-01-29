## String Literals

E.g.

```cpp
int main() {
    char *s1 = "Hello, world!";
    char s2[] = "Hello, world!";
}
```

- main(): 内存中代码段区域
- "Hello, world!": 也存在代码段区域
- s1: 相当于`const char *s1`，指向代码段区域的字符串的指针，不允许修改字符串
- s2: 将字符串拷贝一份到栈，允许修改

## Class

```cpp
#include <iostream>
using namespace std;

class Point {
private:
    int x, y

public:
    void init(int ix, int iy) {
        this->x = ix;
        this->y = iy;
    }

    void print() {
        cout << "Point at [" << this->x << ", " << this->y << "]\n";
    }

    void move(int dx, int dy) {
        this->x += dx;
        this->y += dy;
    }
};

int main() {
    Point p;
    point_init(&p, 2, 3);
    point_print(&p);
    point_move(&p, 5, 5);
    point_print(&p);
    return 0;
}
```

Global vars cannot be written in .h file, but can be written in .cpp file. 

在所有编译单元中引用多次，会报错redefinition。

解决：

```cpp
#ifdef __NAME__H__
#define __NAME__H__

#endif
```

或

```cpp
#pragma once
```

