## Iterators

迭代器（iterator）提供了顺序访问数据结构内部元素的接口，使算法能适配于不同的容器。

```cpp
auto it = find(s.begin(), s.end(), val);  // it为迭代器
cout << *it << '\n';
```

不同容器的迭代器可执行的操作不同。如vector的迭代器能执行`+=`，但list的迭代器不行（因为vector在内存中为连续区域，可以随机访问；而list底层为双向链表，不能直接跳到第n个节点，只能执行`++`和`--`）。

set底层为红黑树，遍历时为红黑树的中序遍历，内部顺序为从小到大。

```cpp
template <class T>
struct myIter {
    typedef T value_type;  // 用value_type表示指向的值的类型
    /* ... */
    T* ptr;
    myIter(T *p = 0) : ptr(p) {}
    T& operator*() {
        return *ptr;
    }
};
```

```cpp
template <class I>
typename I::value_type func (I iter) {
    return *iter;
}
```

### Template specialization

Primary template:

```cpp
template <class T1, class T2, int I>
class A {
    /* ... */
}
```

模板特化后，在特定输入下直接用特化的模板，而不是主模板。

Explicit (full) template specialization:

```cpp
template <>
class A<int, double, 5> {
    /* ... */
}
```

Partial template specialization:

```cpp
template <class T2>
class A<int, T2, 5> {
    /* ... */
}
```

```cpp
template <class T>
class A<T*> {  // 对指针类型的特化
    /* ... */
}
```

### Iterator category

