## Resolver

- `<class name>::<function name>`
- 有重名情况时，`::<function name>`表示全局

## Header Files

A .cpp file is a compile unit. The compilor sees only one .cpp file and generates one corresponding .obj file. The linker links all .obh files into one executable file.

The header is a contract between the author and the user of the code.

## Object Interaction

Messages are composed by the senderm interoreted by the reciever, and implemented by the methods.

Enconsulation(封装)

## Constructor and Destructor

- With the constructor (ctor), the compilor ensures its call when an object is created.
- With the destructor (dtor), the compilor ensures its call when an object is about to end its life-cycle.

```cpp
class X {
public:
    X();   // ctor
    ~X();  // dtor
};

void f() {
    X a;  // compilor do a.X()
}
```

Initialization vs. assignment:

```cpp
Student::Student(string s) : name(s) {}  // initialization
Student::Student(string s) {name = s;}  // assignment
```

## Fields and Variables

`this` is a hidden param for all member functions, eith the type of the class. `Point a; a.print()` can be regarded as `Point::print(&a);`.

## Constant objects

编译器在编译时只有代码文件和.h文件中的函数声明，而没有对类的成员函数实现的.cpp文件，因此不能知道成员函数是否改变成员变量。要对const对象调用成员函数，需要用户在成员函数中声明是否为const，相当于将隐性的`A* this`改为了`const A* this`。

如果在成员函数中声明const，但改变类内部的值，编译器报错。

成员变量为const时，构造函数中要将数值放在参数列表中。

```cpp
#include <iostream>
using namespace std;

class A {
private:
    int i;
public:
    A() : i(0) {}
    void foo() {
        i = 3;
        cout << "This is foo()\n";
    }
    void foo() const {  // overload
        int b = i * i;
        cout << "This is foo() const\n";
    }
};

int main() {
    A a;
    a.foo();  // call the first foo()
    const A b;
    b.foo();  // call the second foo()
}
```

## Overhead

An inline function os expanded in place. Expand the code size but deduces the function call overhead.

Nowadays, the keyword `inline` for functions comes to mean "multiple definitions are permitted", rather than "inlinging is preferred".

## Composition and Inheritance

```cpp
#include <iostream>
using namespace std;

struct A {
    int x, y, z;
};
struct B {  // composition
    A a;
};
struct C : public A {  // inheritance
};

int main() {
    B b;
    // access: b.a.x
    C c;
    // access: c.x
}
```

基类中的私有成员，在派生类中不能访问。`protected`中的成员函数，派生类能调用，但外界不能调用。

- 构造顺序：基类、成员、派生类
- 析构顺序：派生类、成员、基类

如果基类和派生类中定义了同名函数（且参数列表相同），则派生类中不能访问基类中的这个函数。

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    int data;
protected:
    void setdata(int i) {
        data = i;
    }
public:
    Base(int i) : data(i) {
        cout << "Base::Base()" << '\n';
    }
    ~Base() {
        cout << "Base::~Base()" << '\n';
    }
    void print() {
        cout << "Base::print(): " << data << '\n';
    }
};

class Derived : public Base {
private:
    string name;
    string address;
public:
    Derived() : name("zju"), address("hangzhou"), Base(10) {
        cout << "Derived::Derived()\n";
    };
    ~Derived() {
        cout << "Derived::~Derived()\n";
    }
    void foo() {
        setdata(30);
        print();
    }
};

int main() {
    Derived d;
    d.setdata(20);
    d.print();
}
```

不写访问控制时，class默认为private， struct默认为public。

## Friends

在类中声明某些函数/类为friend，则这些函数/类可访问该类的私有成员。

对象的地址即第一个元素的地址。如果类中第一个成员是int，可将对象的地址转为int型指针，也能通过这个指针修改对象（即使是private也能修改）。

```cpp
#include <iostream>
using namespace std;

class Base {
   public:
    int i;
    Base() : i(10) { cout << "Base::Base()\n"; }
};

class Derived : public Base {
   private:
    int j;

   public:
    Derived() : j(30) { cout << "Derived::Derived()\n"; }
    void print_data() { cout << j << '\n'; }
};

int main() {
    Base b;
    Derived d;
    int* p = (int*)&d;
    cout << p << ' ' << *p << '\n';  // 0x30905ffb4c 10
    p++;
    cout << p << ' ' << *p << '\n';  // 0x30905ffb50 30
    *p = 7;
    cout << "d.j = ";
    d.print_data();  // d.j = 7
    return 0;
}
```
