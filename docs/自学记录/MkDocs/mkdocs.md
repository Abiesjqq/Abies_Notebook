## grid card 的使用

### 示例

```html
<div
  class="grid cards"
  style="display: grid; grid-template-columns: 1fr;"
  markdown
>
  <!-- 这里写 markdown 内容 -->
</div>
```

调整列宽需要修改：`style="display: grid; grid-template-columns: 1fr;"`  
其中`grid-template-columns: 1fr`定义网格的列数和宽度。`1fr`表示 1 个分数单位，相当于占满整个空间。

其他示例：

- `grid-template-columns: 1fr 2fr 1fr;` — 4 列，分别占 1、2、1 列
- `grid-template-columns: repeat(3, 1fr);` — 3 列等宽
- `grid-template-columns: 100px 2fr 1fr;` — 3 列，分别是 100px 宽，2 份宽，1 份宽

#### 分两列示例

```
<div class="grid cards" markdown>

![示例](../../images/flower-dark.jpg){.img1}

- __两列测试__

    ---

    - 1
    - 2

</div>
```

效果  

<div class="grid cards" markdown>

![示例](../../images/flower-dark.jpg){.img1}

- __两列测试__

    ---

    - 1
    - 2

</div>

浏览器自动调整为两列

#### 分三列示例

```
<div class="grid cards" style="display: grid; grid-template-columns: 1fr 1fr 1fr;" markdown>
- __三列测试1__

    ---

    - 1
    - 2

- __三列测试2__

    ---

    - 1
    - 2

- __三列测试3__

    ---

    - 1
    - 2
</div>
```

效果

<div class="grid cards" style="display: grid; grid-template-columns: 1fr 1fr 1fr;" markdown>
- __三列测试1__

    ---

    - 1
    - 2

- __三列测试2__

    ---

    - 1
    - 2

- __三列测试3__

    ---

    - 1
    - 2
</div>

## 圆角图片显示

### 示例

```
![示例](images/flower-dark.jpg){.img1}
```

`img1`类定义了圆角图片，`attr_list`扩展的引入使我们可以用`.{img1}`给图片（或其他元素）添加这个类。  
其中`images/flower-dark.jpg`表示当前目录下的images文件夹中的flower-dark.jpg。  
如要回退到上一层目录，可使用`..`

另外，可以直接用URL代替相对路径。
