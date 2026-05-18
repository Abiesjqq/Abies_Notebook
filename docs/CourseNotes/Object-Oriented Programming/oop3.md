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

## Containers

- Sequencial: array, vector, deque, forward_list, list
- Associative: set, map, multiset, multimap
- Unordered associative: unordered_set, unordered_map, unordered_multiset, unordered_multimap
- Adaptors: stack, queue, priority_queue

E.g., vector:

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> evens {2, 4, 6, 8};
    evens.push_back(20);
    evens.push_back(22);
    evens.insert(evens.begin() + 4, 5, 10);  // insert five 10s in index 4

    // print
    for (int i = 0; i < evens.size(); i++)
        cout << evens[i] << ' ';
    cout << '\n';

    for (vector<int>::iterator it = evens.begin(); it < evens.end(); it++)  // auto
        cout << *it << ' ';
    cout << '\n';

    for (int e : evens)
        cout << e << ' ';
    cout << '\n';
}
```

E.g., map:

```cpp
#include <iostream>
#include <map>
#include <string>
using namepace std;

int main() {
    map<string, int> price_list;
    price_list["apple"] = 3;
    price_list["orange"] = 5;
    price_list["banana"] = 1;

    string item;
    int total = 0;
    while (cin >> item) {
        if (price_list.contains(item))
            total += price_list[item];
        else
            cout << item << " is not in the fruit list.\n";
    }
    cout << total << '\n';

    for (const auto& [fruit, price] : price_list)
        cout << fruit << ": " << price << '\n';
}
```

## Algorithm

E.g.

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
#include <string>
#include <list>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4};
    reverse(v.begin(), v.end());  // local reverse

    vector<int> u;
    // copy(v.begin(), v.end(), u.begin());  // segmentation fault
    copy(v.begin(), v.end(), beck_inserter(u));
    copy(u.begin(), u.end(), ostream_iterator<int>(cout, ", "));
}
```

Attention:

- Access safety: use `push_back()` for dynamic expansion, or reallocate with `resize()`
- Silent insertion: create entrie silently
- Invalid iterator: iterator is invalid after `erase()` (`li = L.erase(li)`)

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
