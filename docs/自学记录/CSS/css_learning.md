## 语法

CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明。
选择器通常是需要改变样式的 HTML 元素,每条声明由一个属性和一个值组成。属性（property）是希望设置的样式属性（style attribute）。每个属性有一个值。属性和值被冒号分开。  
CSS 声明总是以分号 ; 结束，声明总以大括号 {} 括起来。  
样式：`选择器 {属性:值; 属性:值;}`  
示例：`h1 {color:blue; font-size:12px;}`

## id 和 class

设置 CSS 样式需要在元素中设置"id" 和 "class"选择器。

在 HTML 和 CSS 中可以使用 id 选择器来给特定的 HTML 元素设置样式。HTML 里用 `id="..."` 来标记一个元素；而在 CSS 里，用 `#id` 名的方式来给这个元素设置样式。  
示例：

```css
#para1 {
  text-align: center;
  color: red;
}
```

class 选择器用来给一组 HTML 元素统一设置样式的。和 id 不同，同一个 class 可以用在多个元素上。class 选择器在 HTML 中以 class 属性表示, 在 CSS 中，类选择器以一个点 . 号显示。  
示例：`.center{text-align:center;}`

也可以指定特定的 HTML 元素使用 class。  
示例（所有的 p 元素使用 class="center" 让该元素的文本居中）：`p.center{text-align:center;}`

## 创建

| 类型                       | 写在哪里？                      | 示例                            |
| -------------------------- | ------------------------------- | ------------------------------- |
| **行内样式（Inline）**     | 写在 HTML 标签内部              | `<p style="color:red">内容</p>` |
| **内部样式表（Internal）** | 写在 HTML 文件 `<style>` 标签中 | 放在 `<head>` 里                |
| **外部样式表（External）** | 写在一个独立的 `.css` 文件里    | 用 `<link>` 引入                |

### 外部样式表

当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 <link> 标签链接到样式表。 <link> 标签在（文档的）头部。  
示例：

```html
<head>
  <link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>
```

其中`rel`表示这个链接的是一个“样式表”文件（stylesheet），`type`表示这个文件是 CSS 类型（可以省略，不强制），`herf`指定要加载的 CSS 文件路径，比如 mystyle.css 是同目录下的文件。  
样式表文件的示例：

```
hr {color:sienna;}
p {margin-left:20px;}
body {background-image:url;}
```

### 内部样式表

当单个文档需要特殊的样式时，就应该使用内部样式表。你可以使用 <style> 标签在文档头部定义内部样式表。  
示例：

```html
<head>
  <style>
    hr {
      color: sienna;
    }
    p {
      margin-left: 20px;
    }
    body {
      background-image: url;
    }
  </style>
</head>
```

### 内联样式

在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性。  
示例：`<p style="color:sienna;margin-left:20px">这是一个段落。</p>`

### 多重样式

优先级：内联样式 > 内部样式 > 外部样式。

## 背景

### 背景颜色

background-color 属性定义了元素的背景颜色。页面的背景颜色使用在 body 的选择器中。  
示例：`body {background-color:#b0c4de;}`

颜色值定义：

- 十六进制，如`#ff0000`
- rgb，如`rgb(255,0,0)`
- 颜色名称，如`"red"`

### 背景图像

background-image 属性描述了元素的背景图像。默认情况下，背景图像进行平铺重复显示，以覆盖整个元素实体。  
示例：`body {background-image:url('paper.gif');}`

默认情况下 background-image 属性会在页面的水平或者垂直方向平铺。  
background-repeat 可以设置平铺的方向（参数为 repeat-x，repeat-y 和 no-repeat）。  
示例：

```css
body {
  background-image: url;
  background-repeat: repeat-x;
}
```

background-position 属性可以改变图像在背景中的位置。参数：left center right；top bottom；和两者的组合。  
示例：`...background-position:right top;...`

### 背景属性简写

为了简化这些属性的代码，我们可以将这些属性合并在同一个属性中。背景颜色的简写属性为 "background"。  
属性值顺序：

1. background-color
2. background-image
3. background-repeat
4. background-attachment
5. background-position

示例：`body {background:#ffffff url('img_tree.png') no-repeat right top;}`

## 文本

| **属性**          | **作用**                                | **常用取值/参数**                                                                                  |
| ----------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `color`           | 设置文本颜色                            | 颜色名（`red`）、十六进制（`#ff0000`）、RGB（`rgb(255,0,0)`）等                                    |
| `direction`       | 设置文本方向（从左到右或从右到左）      | `ltr`（从左到右）、`rtl`（从右到左）                                                               |
| `letter-spacing`  | 设置字符之间的间距                      | 正数增加间距：`2px`，负数减少间距：`-1px`，`normal`（默认）                                        |
| `line-height`     | 设置文本的行高                          | 比例值：`1.5`，长度：`20px`，百分比：`150%`，`normal`（默认）                                      |
| `text-align`      | 设置文本的水平对齐                      | `left`、`right`、`center`、`justify`（两端对齐）                                                   |
| `text-decoration` | 添加文本修饰线（如下划线、删除线）      | `none`、`underline`（下划线）、`line-through`（删除线）、`overline`（上划线）                      |
| `text-indent`     | 设置首行缩进                            | 像素（`20px`）、百分比（`5%`）                                                                     |
| `text-shadow`     | 设置文本阴影                            | 例：`2px 2px 5px gray`（右下方向，模糊 5px，灰色）                                                 |
| `text-transform`  | 控制字母大小写                          | `none`（无变化）、`capitalize`（每个单词首字母大写）、`uppercase`（全大写）、`lowercase`（全小写） |
| `unicode-bidi`    | 控制双向文本（与 `direction` 配合使用） | `normal`、`embed`、`bidi-override`                                                                 |
| `vertical-align`  | 设置元素的垂直对齐                      | `baseline`、`middle`、`top`、`bottom`、`sub`、`super`、`px` 值等                                   |
| `white-space`     | 设置空白字符（空格、换行）的处理方式    | `normal`（默认）、`nowrap`、`pre`、`pre-wrap`、`pre-line`                                          |
| `word-spacing`    | 设置单词之间的间距                      | 像素：`10px`，`normal`（默认）                                                                     |

```css
p {
  color: #333;
  text-align: justify;
  line-height: 1.6;
  text-indent: 2em;
  letter-spacing: 1px;
  word-spacing: 3px;
  text-shadow: 1px 1px 2px gray;
}
```

## 字体

| **属性**       | **作用说明**                                                                   | **常用取值示例 / 说明**                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `font-family`  | 设置字体系列                                                                   | `"Times New Roman"`、`Arial`、`"宋体"`，多个用逗号分隔，最后常加 `serif`（衬线字体）、`sans-serif`（无衬线）、`monospace`（等宽）作为回退字体 |
| `font-style`   | 控制字体是否为斜体                                                             | `normal`（正常）、`italic`（斜体）、`oblique`（倾斜，兼容性较差）                                                                             |
| `font-size`    | 设置字体大小                                                                   | `15px`、`1.2em`、`120%`、`1rem` 等；百分比或 `em` 通常相对于父元素字体大小                                                                    |
| `font-weight`  | 设置字体粗细                                                                   | `normal`、`bold`、`lighter`、`bolder`，或具体数字如 `400`、`700`                                                                              |
| `font-variant` | 控制小型大写字母（small-caps）显示                                             | `normal`、`small-caps`                                                                                                                        |
| `line-height`  | 设置行高                                                                       | `normal`、具体数值：`1.5`、`20px`、`150%`                                                                                                     |
| `font`（简写） | 简写所有字体属性（顺序：style → variant → weight → size/line-height → family） | 例如：`font: italic small-caps bold 16px/1.5 Arial, sans-serif;`                                                                              |

## 链接

链接状态：

- a:link：正常，未访问过的链接
- a:visited：用户已访问过的链接
- a:hover：当用户鼠标放在链接上时
- a:active：链接被点击的那一刻

示例：

```css
a:link {
  color: #000000;
}
a:visited {
  color: #00ff00;
}
a:hover {
  color: #ff00ff;
}
a:active {
  color: #0000ff;
}
```

顺序规则：

- a:hover 必须跟在 a:link 和 a:visited 后
- a:active 必须跟在 a:hover 后

`background-color`指定链接的背景色  
示例：`a:link {background-color:#B2FF99;}`

## 列表

html 中的列表：

1. 无序列表`ul`
2. 有序列表`ol`

`list-style-type`属性指定列表项标记的类型。  
示例：

```css
ul.a {
  list-style-type: circle;
}
ol.d {
  list-style-type: lower-alpha;
}
```

具体参数：

- 无序列表的 list-style-type：dics（实心圆），circle（空心圆），square（实心方块），none（无标记）。
- 有序列表的 list-style-type：decimal（1，2……），demical-leading-zero（01，02……），lower-alpha，upper-alpha，lower-roman，upper-roman，none。
- 图像：直接用 url。
- margin：设置内边距
- padding：设置外边距

示例：

```css
ul {
  list-style-type: none;
  padding: 0px;
  margin: 0px;
}
ul li {
  background-image: url(sqpurple.gif);
  background-repeat: no-repeat;
  background-position: 0px 5px;
  padding-left: 14px;
}
```

## 表格

- table：表格的外层容器
- tr：Table Row 表格行
- th：Table Header 表格单元头
- td：Table Data 数据单元格

`border`设置边框。  
示例：`table, th, td {border:1px solid black;}`

`border-collapse`设置边框是否被折叠成一条线。  
示例：`table {border-collapse:collapse;}`

`width`和`height`设置表格的宽度和高度。  
示例（表格宽度 100%，表头高度 50 像素）：

```css
table {
  width: 100%;
}
th {
  height: 50px;
}
```

`text-align`设置水平对齐方式（left，right，center，justfy），`vertical-align`设置垂直对齐方式（top，middle，bottom……）。  
示例：

```css
td {
  text-align: left;
  vertical-align: bottom;
}
```

设置颜色：  
边框颜色在 border 的第三个参数设置，文本文字在 color 设置，背景颜色在 background-color 设置。

## 盒子模型

从外到内：margin -> border -> padding -> content  
总元素的宽度=宽度+左填充+右填充+左边框+右边框+左边距+右边距  
总元素的高度=高度+顶部填充+底部填充+上边框+下边框+上边距+下边距

示例：

```css
div {
  width: 220px;
  padding: 10px;
  border: 5px solid gray;
  margin: 0;
}
```

## 边框

`border-style`用于指定要显示的边框类型。

| **取值** | **含义**    | **说明**                             |
| -------- | ----------- | ------------------------------------ |
| `none`   | 无边框      | 默认，无边框显示                     |
| `hidden` | 隐藏边框    | 与 `none` 类似，主要用于冲突处理     |
| `dotted` | 点状边框    | 由点组成的边框                       |
| `dashed` | 虚线边框    | 由短线段组成的边框                   |
| `solid`  | 实线边框    | 连续的实线                           |
| `double` | 双线边框    | 两条实线，宽度与 `border-width` 相同 |
| `groove` | 3D 沟槽边框 | 根据 `border-color` 显示沟槽效果     |
| `ridge`  | 3D 脊状边框 | 根据 `border-color` 显示脊状效果     |
| `inset`  | 3D 嵌入边框 | 根据 `border-color` 显示嵌入效果     |
| `outset` | 3D 突出边框 | 根据 `border-color` 显示突出效果     |

`border-width`设置边框宽度。  
参数：thick，medium，thin，或用 px 设置。  
示例：

```css
p.one {
  border-style: solid;
  border-width: 5px;
}
```

`border-color`设置边框颜色。  
border-color 单独使用是不起作用的，必须得先使用 border-style 来设置边框样式。  
颜色可设置为 transparent。  
示例：

```css
p.one {
  border-style: solid;
  border-color: red;
}
```

border-top-style，border-right-style，border-bottom-style，border-left-style 可以给不同侧面设置不同边框。  
示例：

```css
p {
  border-top-style: dotted;
  border-right-style: solid;
  border-bottom-style: dotted;
  border-left-style: solid;
}
```

上面四个可以合并成 border-style 一个属性。

- 4 个参数：上，右，下，左
- 3 个参数：上，左右，下
- 2 个参数：上下，左右
- 1 个参数：四周

`border`是 border-width，border-style，border-color 的简写

## 轮廓

| 属性名          | 说明                         | 常用值（示例）                                                                                 | CSS 版本 |
| --------------- | ---------------------------- | ---------------------------------------------------------------------------------------------- | -------- |
| `outline`       | 在一条声明中设置所有轮廓属性 | 组合 `outline-color`、`outline-style`、`outline-width` 等                                      | CSS2     |
| `outline-color` | 设置轮廓颜色                 | 颜色名称（`red`）、十六进制（`#ff0000`）、RGB（`rgb(255,0,0)`）、`invert`、`inherit`           | CSS2     |
| `outline-style` | 设置轮廓样式                 | `none`、`dotted`、`dashed`、`solid`、`double`、`groove`、`ridge`、`inset`、`outset`、`inherit` | CSS2     |
| `outline-width` | 设置轮廓宽度                 | 关键词：`thin`、`medium`、`thick`；长度单位（如 `2px`）；`inherit`                             | CSS2     |

## 外边距

| **属性**        | **说明**                             | **取值/示例**                                   |
| --------------- | ------------------------------------ | ----------------------------------------------- |
| `margin`        | 简写属性，一次性设置四个方向的外边距 | `margin: 25px 50px 75px 100px;` （上 右 下 左） |
| `margin-top`    | 设置元素的上外边距                   | `100px`, `2em`, `10%`, `auto`                   |
| `margin-right`  | 设置元素的右外边距                   | 同上                                            |
| `margin-bottom` | 设置元素的下外边距                   | 同上                                            |
| `margin-left`   | 设置元素的左外边距                   | 同上                                            |

| **取值**           | **说明**                                    |
| ------------------ | ------------------------------------------- |
| `auto`             | 由浏览器决定边距大小，常用于水平居中        |
| `<length>`         | 固定长度，如像素（px）、点（pt）、em、cm 等 |
| `%`                | 百分比值，相对于包含块宽度                  |
| 负值（如 `-10px`） | 允许使用负值，实现内容重叠                  |

简写属性 `margin` 的用法示例：

| 写法                            | 含义描述                            |
| ------------------------------- | ----------------------------------- |
| `margin: 25px;`                 | 上、右、下、左边距均为 25px         |
| `margin: 25px 50px;`            | 上下 25px，左右 50px                |
| `margin: 25px 50px 75px;`       | 上 25px，左右 50px，下 75px         |
| `margin: 25px 50px 75px 100px;` | 上 25px，右 50px，下 75px，左 100px |

## 填充

| 属性名           | 说明                           | 示例                           |
| ---------------- | ------------------------------ | ------------------------------ |
| `padding`        | 简写属性，设置四个方向的内边距 | `padding: 10px 20px 30px 40px` |
| `padding-top`    | 设置元素顶部的内边距           | `padding-top: 10px`            |
| `padding-right`  | 设置元素右侧的内边距           | `padding-right: 20px`          |
| `padding-bottom` | 设置元素底部的内边距           | `padding-bottom: 30px`         |
| `padding-left`   | 设置元素左侧的内边距           | `padding-left: 40px`           |

| 写法示例                        | 含义说明                                    |
| ------------------------------- | ------------------------------------------- |
| `padding: 25px`                 | 四个方向全部为 25px                         |
| `padding: 25px 50px`            | 上下为 25px，左右为 50px                    |
| `padding: 25px 50px 75px`       | 上为 25px，左右为 50px，下为 75px           |
| `padding: 25px 50px 75px 100px` | 上为 25px，右为 50px，下为 75px，左为 100px |

`padding` 支持的单位：

| 单位  | 示例            | 说明                   |
| ----- | --------------- | ---------------------- |
| `px`  | `padding: 20px` | 像素                   |
| `em`  | `padding: 2em`  | 相对于当前字体大小     |
| `%`   | `padding: 10%`  | 相对于父元素的宽度     |
| `rem` | `padding: 1rem` | 相对于根元素的字体大小 |
| `pt`  | `padding: 10pt` | 点（在网页中较少用）   |

`padding` 特性：

- `padding` **不影响内容大小**，但会增大**元素总尺寸**（除非使用 `box-sizing: border-box`）。
- `padding` 填充的区域**会被背景颜色覆盖**。
- `padding` 是内边距，**不同于 `margin`（外边距）**。

## 分组和嵌套选择器

分组选择器：将多个选择器合并在一起，用逗号分隔。  
示例：
```css
h1, h2, p {
  color:green;
}
```

嵌套选择器：适用于选择器内部的选择器的样式。  
在下面的例子设置了四个样式：  
- `p{ }`: 为所有 p 元素指定一个样式。
- `.marked{ }`: 为所有 class="marked" 的元素指定一个样式。
- `.marked p{ }`: 为所有 class="marked" 元素内的 p 元素指定一个样式。
- `p.marked{ }`: 为所有 class="marked" 的 p 元素指定一个样式。