## Introduction

Bjarne Stroustrup.

## Using Objects

**String:**

- Assignment: `string str1 = "aaa"`
- Assign: `str.assign('ahgie')`
- Concatenation: `str3 = str1 + str2`, `str1 += str2`
- Constructors: `string(const string& s2, int pos, int len)`, `string(const char *cp, int len)`
- Sub-string: `substr(int pos, int len)`
- Modification: `assign()`, `insert(int pos, const string& s)`, `erase()`, `append()`, `replace(int pos, int len, const string& s)`
- Search: `find(const string& s)`

!!! normal-comments "string长度说明"

    string末尾没有`\0`，`string.length()`返回可见字符的长度。

!!! remarks "局部变量，静态局部变量，全局变量，静态全局变量，临时分配变量"

    所有局部变量（定义在`{}`中）都只在块内可见，块外无法访问。不同点在于，普通局部变量每次进入作用域时创建、离开作用域时销毁，而静态局部变量只在第一次进入作用域时创建一次，之后多次调用并“记住上次的值”。

    普通全局变量课跨文件用`extern`引用，但静态全局变量（加`static`）不能，只在当前.cpp文件可见。

    普通局部变量存储在栈中，编译器自动管理。静态局部变量、全局变量、静态全局变量都存储在静态存储区（数据段/BSS）。临时分配变量存储在堆中，程序员管理。

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

## Template

In order to support multiple data structures.

```cpp
template<typename T>
void print_array(T arr[], int n) {
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << ' ';
    std::cout << '\n';
}
```

```cpp
template<typename T>
void swap(T& a, T& b) {
    T tmp = a;
    a = b;
    b = tmp;
}
```

## Operator

```cpp
struct Student {
    int id;
    std::string name;

    bool operator<(const Student& s) {
        return id < s.id;
    }
}
```

or:

```cpp
struct Student {
    int id;
    std:string name;
}

bool operator<(const Student& s1, const Student& s2) {
    retrun s1.id < s2.id;
}

std::ostream& operator<<(std::ostream out, const Student& s) {
    return out << "(" << s.id << "," << s.name << ")\n";
}
```

## Class

```cpp
class Rectangle {
private:
    double w, h;
    double area, perimeter;

public:
    Rectangle(double w, double h): w(w), h(h) {}
    void calc_area() {
        area = w * h;
    }
    void calc_perimeter() {
        perimeter = 2 * (w + h);
    }
};

// Omitted

int main() {
    Rectangle arr[] = {Rectangle(2, 3), Rectangle(5, 5)};
    int n = sizeof(arr) / sizeof (arr[0]);

    for (Rectangle& r : arr) {
        r.calc_area();
        r.calc_perimeter();
    }
}
```

Add class `Shape`:

```cpp
class Shape {
protected:
    double area, perimeter;
public:
    virtual ~Shape() {}
    virtual void calc_area() = 0;  // virtual means the function will be override
    virtual void calc_perimeter() = 0;
    virtual std::string name() const = 0;   // const means name() will not change Shape&
    friend std::ostream& operator<<(std::ostream& out, const Shape& s);  // friend enables the function to access protected variables
    double get_area() const {return area;}
    double get_perimeter() const {return perimeter;}
}

std::ostream& operator<<(std::ostream& out, const Shape& s) {
    // function name() is override in child class (has the risk to change protected variables), thus father class need to add const to ensure it does not change inner values
    return out << "(" << s.name() << ": " << s.area << ", " << s.perimeter << ")\n";
}

template<typename T>
void print_array(T* arr, int n) {
    for (int i = 0; i < n; i++)
        std::cout << *arr[i] << ' ';
    std::cout << '\n';
}

bool less_shape_area(Shape* s1, Shape* s2) {
    return s1->get_area() < s2->get_area()
}

bool less_shape_perimeter(Shape* s1, Shape* s2) {
    return s1->get_perimeter() < s2->get_perimeter()
}

template<typename T, typename Compare>
int min_element(T arr[], int begin, int end, Compare cmp) {
    int min_idx = begin;
    for (int i = begin + 1; i < end; i++) {
        if (cmp(arr[i], arr[min_idx]))
            min_idx = i;
    }
    return min_idx;
}

template<typename T>
void swap(T& a, T& b) {
    T tmp = a;
    a = b;
    b = tmp;
}

template<typename T, typename Compare>
void selection_sort(T arr[], int n, Compare cmp) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = min_element(arr, i, n, cmp);
        if (min_idx != i)
            swap(arr[min_idx], arr[i]);
    }
}

class Rectangle : public Shape {
private:
    double w, h;
public:
    Rectangle(double w, double h): w(w), h(h) {}
    void calc_area() override {
        area = w * h;
    }
    void calc_perimeter() override {
        perimeter = 2 * (w + h);
    }
    std::string name() const override {
        return "Rectangle"
    }
}

int main() {
    Shape* arr[] = {new Rectangle(2, 3), new Rectangle (5, 5), new Circle(3), new Triangle(2, 5, 4)};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (Shape* s : arr) {
        s -> calc_area();
        s -> calc_perimeter();
    }

    for (Shape* s : arr)
        delete s;
}
```
