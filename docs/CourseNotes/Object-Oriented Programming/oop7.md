## Streams

Turn off sunchronization: `std::ios::sync_with_stdio(false)`

- insertor: `<<`
- extractor: `>>`

Extractor的重载：

```cpp
istream& operator>> (istream* is, T& obj) {
    return is;  // 返回istream用于构建流（类似链表）
}
```

```cpp
#include <iostream>
using namespace std;

class Point {
   private:
    int x, y;

   public:
    Point(int px = 0, int py = 0) : x(px), y(py) {}
    friend ostream& operator<<(ostream&, const Point&);
    friend istream& operator>>(istream&, Point&);
};

ostream& operator<<(ostream& os, const Point& p) {
    return os << '(' << p.x << ", " << p.y << ")";
}

istream& operator>>(istream& is, Point& p) {
    is >> p.x >> p.y;
    return is;
}

int main() {
    Point a(1, 2);
    cout << a << '\n';
}
```

## Templates

函数重载的前提是函数名相同、参数列表不同。如果调用时参数类型不同但能隐式转换，则编译器自动完成转换；但如果有多个重载函数均能隐式转换，编译报错。

默认参数（default argument）必须从右到左写。默认参数在头文件和.cpp文件中不能重复写。调用时，如果默认参数位置未传参，则用默认值；如果传参，则用传入的参数。

Templates包括function template和class template。如stack, queue都为class templates，其中的成员函数也写成template。

函数模板中，template可表示参数、主体中变量和返回类型，也可以有多个模板参数。E.g., swap function templates。匹配时顺序：普通函数 --> 模板函数 --> 普通函数的隐式转换。

```cpp
template <class T>
void swap(T& x, T& y) {
    T tmp = x;
    x = y;
    y = tmp;
}
```

调用可用`swap<int>(x, y)`指定用int实例化。如果函数参数列表中无template类型，调用时必须用`<>`指定实例化类型。

类模板，e.g.

```cpp
template <class T>
class Vector {
   public:
    Vector(int);
    ~Vector();
    Vector(const Vector&);
    Vector& operator=(const Vector&);
    T& operator[](int);

   private:
    T* m_elements;
    int m_size;
};
```

Member template：当成员函数的参数类型和类模板不一致。E.g.

```cpp
#include <iostream>
using namespace std;

template <class T>
struct complex {
    T real, imag;
    complex(T real, T imag) : real(real), imag(imag) {};

    template <typename U>  // 允许不同类型的complex转换
    complex(const complex<U>& other) : real(other.real), imag(other.imag){};
};

template <typename T>
ostream& operator<<(ostream& out, const complex<T>& c) {
    return out << "(" << c.real << ", " << c.imag << ")";
}

int main() {
    complex<double> a(3.14, -1.57);
    cout << a << '\n';
    complex<int> b = a;
    cout << b << '\n';  // (3, -1)
}
```


