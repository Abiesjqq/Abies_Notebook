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