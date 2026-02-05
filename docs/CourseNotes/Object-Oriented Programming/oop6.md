## Polymorphism

由于向上造型，派生类中的同名函数会被替换为基类中的函数。但如果基类中有`virtual`关键字，会派生对象会调用派生类中定义的函数。在派生类中加`override`关键字，可使复写关系更明确。

若派生类的对象放在用基类定义的结构中，则析构时调用基类的析构函数。E.g.，假设基类为`Shape`类，派生类为`Circle`类。main中定义`Shape*`的vector、`Circle c`，并将`&c`加入vector，则后续delete vector时调用`Shape`的析构函数而非`Circle`的析构函数。

不加`virtual`是静态绑定，加`virtual`是动态绑定

virtual的实现：在类的前8个字节vptr预留指针，指向虚函数代码区。

将派生类对象直接赋值给基类对象：共有成员，派生类对象的值覆盖原先的值；派生类中多余成员，直接舍弃；vptr不改变，赋值后调用重载的函数仍为基类中定义的函数。

但如果派生类对象的指针直接赋值给基类对象的指针，调用为派生类中定义的函数。指针和引用均为动态绑定。

如果在派生类的重载函数中仍要调用基类的函数，可加基类限定符调用。

重载函数的返回值不一定相同。返回为引用或指针时，派生类中函数的返回值可以是基类中返回值的子类。

抽象类（abstract class）指含有纯虚函数`virtual int func(...) = 0`成员函数的类，必须override。

接口类（interface class）指除了析构函数，其他均为纯虚函数的类。

## Copying

构造对象时，等号和括号等价，即`O=p`等价于`O(p)`。

用对象赋值时，触发拷贝构造函数（参数为同类型类的构造函数`T::T(const T&)`），而不是默认构造函数。但析构函数是统一的。

编译器自动生成的拷贝构造函数中，原生类型拷贝值，嵌套的类调用类的拷贝构造函数。当成员中有指针时，值拷贝后两个对象的成员指针指向同一个区域，析构时delete多次，程序报错。因此类型中有指针时，需注意ctor、dtor、拷贝构造函数。

函数返回对象赋值时也有拷贝构造。编译器会优化去除一些不必要的拷贝构造。

vector每次扩容成两倍时，将原先的值全部copy一次。可先用`.reserve()`预留空间，`.push_back`换成`.emplace_back`避免copy。

static类型的对象，在整个程序结束时才析构，在创建时才构造。如果类中有static成员，则该成员的生存期和存储位置独立于对象，对象构造时不将static成员一起构造，需要在全局额外定义static成员；且由于static变量在全局，若该类有不同对象，则共用一个static变量。

## Operator Overloading

运算符重载不能创造新的运算符，不改变参数和优先级。

单目运算符怎么区分前缀/后缀？定义时不带参数的为前缀，带参数的为后缀。

可利用不同运算符间的逻辑关系简化。E.g.

```cpp
bool Interger::operator< (const Integer& rhs) const {
    return i < ths.i;
}

bool Interger::operator>= (const Integer& rhs) const {
    return !(*this < rhs);
}
```

`operator[]`必须为成员函数，返回值为元素的引用。

编译器自动生成`operator=`。当类中有指针时同样存在share的问题，需自己写`operator=`。注意copy assignment时对象原先已有定义，拷贝时要先delete原先拷贝构造是的指针。E.g.

```cpp
#include <iostream>
using namespace std;

class A {
private:
    char* p;
public:
    A& operator= (const A &rhs) {
        if (this != &rhs) {  // 避免a=a报错
            delete[] p;  // 删除原先的指针
            p = new char[strlen(rhs) + 1];
            strcpy(p, rhs.p);
            return *this;
        }
    }
};
```

```cpp
T a = b;  // copy constructor

T a, b;
a = b;    // copy assignment
```

`operator()`相当于将对象当作函数使用。E.g.

```cpp
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

void transform(vector<int>& v, function<int(int)> f) {
    for (int& x : v)
        x = f(x)
}

class mul_by {  // 匿名函数即编译器生成一个类
private:
    int a;
public:
    mul_by(int a) : a(a) {}
    int operator() (int x) {
        return x * a;
    }
}

int main() {
    vector<int> v = {1, 2, 3, 4, 5};
    int a = 5;
    transform(v, [a](int x) { return x * a; });
    for (int& x : v)
        cout << x << ' ';
    cout << '\n';
}
```

隐式转换：类B有参数为A对象的构造函数，则如果某函数期望的参数是B对象、实际有A对象，会将A对象隐式转换为B对象作为参数。若B中对应ctor前加`explicit`关键字，则需手动将A对象转为B对象。