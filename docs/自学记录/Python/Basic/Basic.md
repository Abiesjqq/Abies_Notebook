# 一些关于 Python 的碎碎念

字符串格式化：

- `'Hi %s, number %d.\n' % ('Abies', 7)`：%占位
- `'Hi {0}, number {1}.\n'.format('Abies', 7)`：{}中参数编号
- `f'Hi {name}, number {num}.\n'`：{}中为变量名

字符串操作：

- 替换：`s2=s1.replace('a','A')`，原字符串不变

list 操作：

- 创建：`a=[1,2,3]`或`a=list(range(1,9))`或`l=[x*x for x in range(1, 9) if x%2 == 0]`
- 返回长度：`len(a)`
- 添加：`a.append('Aby')` 没有返回值
- 指定位置添加：`a.insert(1,'Aby')`
- 删除：`a.pop()`
- 指定位置删除：`a.pop(2)` 指定删除位置
- 修改：`a[1]='hihi'`
- 排序：`a.sort()`
- 切片：`a[0:5:2]`

tuple 操作：

- []访问、切片，不能插入、删除、修改
- 创建：`t=(1,)`
- 若 tuple 中含 list，list 的元素可变

输入：

- `in=input()` 返回值为 str

match-case 格式：

```py
match a:
    case x if x < 3:
        pass
    case 10 | 11:
        pass
    case _:  # default
        pass
```

dict 操作：

- 创建：`d={'A':1,'B':2}`
- 查找：`d['A']`
- 插入：`d['C']=3`
- 是否存在：`'A' in d`或`d.get('A')`，后者返回索引
- 修改：键必须存在
- 删除：`d.pop('B')`

set 操作：

- 创建：`s={1,2,3}`或`s=set([1,2,3])`
- 添加：`s.add(4)`
- 删除：`s.remove(4)`
- 可以&、|操作

定义函数：

- 能返回多个值作为 tuple，`return a,b`
- 没有 return 语句时，自动 return None
- 参数有默认值，则调用时可不写。默认参数在函数内不建议改变。
- 可变参数前加\*，可传入任意多个，接收为 tuple
- 关键字参数前加\*\*

循环：

- 索引-元素迭代：`for i, v in enumerate(['A', 'B', 'C']):`
- 两个元素迭代：`for i, j in [(1,1), (2,2)]:`
