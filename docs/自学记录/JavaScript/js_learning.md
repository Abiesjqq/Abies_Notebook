## 基本用法

`windows.alert()`弹出警告框

`document.write()`将内容写入 HTML

`innerHTML`写入到 HTML 元素  
通过 id 修改内容：`document.getElementById("demo").innerHTML="修改后结果";`

`console.log()`写入到控制台

对象：`容器名 = {键:值, 键:值}`  
示例：

```js
let person = {
  name: "Abies",
  age: 3,
  school: "ZJU",
};
```

访问对象属性：`person.name`或`person["name"]`  
对象中包含函数：

```js
let person = {
  name: "Abies",
  school: "ZJU",
  nameAndSchool: function () {
    return this.name + " " + this.school;
  },
};

document.getElementById("demo").innerHTML = person.nameAndSchool();
```

函数：

```js
function 函数名(参数) {
  执行代码;
}
```

示例：

```html
<html>
  <head>
    <script>
      function myAlert() {
        alert("Hello World!");
      }
    </script>
  </head>

  <body>
    <button onclick="myAlert()">A button</button>
  </body>
</html>
```

事件：`<HTML元素 事件="执行的代码">`
常见的事件：

- onchange：HTMl 元素改变
- onclick：点击元素
- onmouseover：鼠标悬停
- onmouseout：鼠标移开
- onkeydown：按下按键
- onload：页面加载完成

字符串：[字符串函数](https://www.runoob.com/js/js-strings.html)

模板字符串：用``包围，中间可用${}使用变量   
两个字符串可直接用`+`拼接  
示例：

```js
const name = "Abies";
const age = 3;
const message = `My name is ${name} and my age is ${age}.`;
```

可作为 HTML 的模板  
示例：

```js
let header = "";
let tags = ["RUNOOB", "GOOGLE", "TAOBAO"];

let html = `<h2>${header}</h2><ul>`;
for (const x of tags) {
  html += `<li>${x}</li>`;
}

html += `</ul>`;
```

选择条件：`if ... else if ... else ...`

switch 语句：

```js
switch (n) {
  case 1:
    语句;
    break;
  case 2:
    语句;
    break;
  default:
    语句;
}
```

for 循环：

```js
for (let i = 0; i < cars.length; i++) {
  document.write(cars[i] + "<br>");
}
```

或

```js
for (x in cars) {
  document.write(x + "<br>");
}
```

while 循环：

```js
while (条件) {
  语句;
}
```

`typeof`运算符检查变量类型  
类型有：string, number, boolean, object, function, bigint, undefined, date, array, null...  
`constructor`属性返回变量的构造函数  
示例（用 constructor 判断是不是数组）：

```js
function isArray(myArray) {
  return myArray.constructor.toString().indexOf("Array") > -1;
}
```

（判断是否包含某段字符串的方法：先 toString()，再检查 indexOf()）

类型转换方法：`String()`和`toString()`，`Number()`...  
字符串和数字相加，将数字变为字符串

正则表达式：
[基本的正则表达式](https://www.runoob.com/js/js-regexp.html)  
[正则表达式教程](https://www.runoob.com/regexp/regexp-tutorial.html)

错误尝试：
`try`和`catch`成对出现，try 语句尝试运行，catch 语句捕获 try 部分的错误。finally 中的语句一定会执行。

```js
try {
    if (...) throw "...";
} catch(err) {
    处理异常
} finally {
    结束处理
}
```

示例：

```js
function myFunction() {
  let message, x;
  message = document.getElementById("message");
  message.innerHTML = "";
  x = document.getElementById("demo").value;
  try {
    if (x == "") throw "空";
    if (isNaN(x)) throw "不是数字";
    x = Number(x);
    if (x < 5) throw "太小";
    if (x > 10) throw "太大";
  } catch (err) {
    message.innerHTML = "错误：" + err;
  }
}
```

调试：用`console.log()`输出到控制台

声明提升：变量的声明和函数的声明会被解释器自动提升到最顶部  
而初始化不会提升  
会提升：

```js
let x;
x = 1;
```

不会提升：

```js
let x = 1;
```

`==`葫芦数据类型，下面的代码中`x == y`为 true

```js
let x = 10;
let y = "10";
```

而`===`为严格相等，需要变量类型也相等。上面代码中`x === y`为 false

表单，HTML 代码：

```html
<form name="myForm" action="/submit" method="get">
  姓名：<input type="text" name="fname" />
  <input type="submit" value="提交" />
</form>
```

判断表单字段 fname 是否存在，如果不存在就弹出信息

```js
function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
  if (x == null || x == "") {
    alert("需要输入名字");
    return false;
  }
}
```

（解释：`document`表示整个网页的 DOM 文件，`document.forms`表示网页中所有表单的集合，`document.forms["formName"]`表示从所有表单中取出名为 formName 的表单，`document.forms["formName"]["name"]`表示从 formName 表单中取出 name 字段，`.value`表示得到实际的值。）

示例，验证输入的数字为 1~9：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
  </head>

  <body>
    <h1>JavaScript 验证输入</h1>
    <p>请输入 1 到 10 之间的数字：</p>
    <input id="numb" />
    <button type="button" onclick="myFunction()">提交</button>
    <p id="demo"></p>
    <script>
      function myFunction() {
        let x, text;
        x = document.getElementById("numb").value;
        if (isNaN(x) || x < 1 || x > 10) {
          text = "输入错误";
        } else {
          text = "输入正确";
        }
        document.getElementById("demo").innerHTML = text;
      }
    </script>
  </body>
</html>
```

在 input 块中增加`required="required"`，会在字段为空时自动阻值提交。

其他验证属性：

HTML 输入属性（最重要的部分）：

| 属性          | 用途                             | 示例                                     | 效果               |
| ------------- | -------------------------------- | ---------------------------------------- | ------------------ |
| `required`    | 必填                             | `<input required>`                       | 不填不能提交       |
| `type`        | 限定输入类型                     | `<input type="email">`                   | 必须是邮箱格式     |
| `pattern`     | 自定义格式（正则表达式）         | `<input pattern="[A-Za-z]{3}">`          | 只能输入 3 个字母  |
| `min` / `max` | 最小/最大值（数值或日期）        | `<input type="number" min="1" max="10">` | 只能输入 1\~10     |
| `disabled`    | 禁用输入框（不可编辑、不可提交） | `<input disabled>`                       | 用户无法填写这个框 |

CSS 伪类选择器（用于样式反馈）：

伪类可以用来根据验证状态改变样式，比如加红框、显示对勾等。

| 伪类        | 意思           | 用法示例                               | 效果             |
| ----------- | -------------- | -------------------------------------- | ---------------- |
| `:required` | 必填的输入框   | `input:required { border: red; }`      | 必填框加红边     |
| `:optional` | 非必填的输入框 | `input:optional { border: gray; }`     | 可选框加灰边     |
| `:valid`    | 值合法         | `input:valid { border: green; }`       | 填写正确时加绿边 |
| `:invalid`  | 值不合法       | `input:invalid { border: red; }`       | 错误时加红边     |
| `:disabled` | 不可用输入框   | `input:disabled { background: #eee; }` | 灰掉背景色       |

DOM 属性和方法（JavaScript 操作验证）：

| API                 | 说明                                         | 示例                          |
| ------------------- | -------------------------------------------- | ----------------------------- |
| `.checkValidity()`  | 返回输入框是否通过验证（true/false）         | `input.checkValidity()`       |
| `.reportValidity()` | 检查并显示提示信息（会弹窗）                 | `form.reportValidity()`       |
| `.validity`         | 返回验证结果对象（布尔属性）                 | `input.validity.valueMissing` |
| `.willValidate`     | 返回是否会被验证（比如禁用的输入框不会验证） | `input.willValidate`          |

验证 API：
`checkValidity()`返回 true/false  
`setCustomValidity()`设置 input 元素的 validationMessage 属性，用于自定义错误提示信息的方法。使用 setCustomValidity 设置了自定义提示后，validity.customError 就会变成 true，checkValidity 总是会返回 false。

示例：

```html
<input id="id1" tyoe="number" min="10" max="300" required />
<button onclick="myFunction()">验证</button>

<script>
  function myFunction() {
    let inputObj = document.getElementById("id1");
    if (inputObj.checkValidity() == false) {
      document.getElementById("demo").innerHTML = inputObj.validitionMessage;
    }
  }
</script>
```

约束验证 DOM 属性：

| 属性              | 描述                    |
| ----------------- | ----------------------- |
| validity          | true / false            |
| validationMessage | 浏览器错误提示信息      |
| willValidate      | 指定 input 是否需要验证 |

Validity 属性：[Validity 属性表格](https://www.runoob.com/js/js-validation-api.html)

this 是一个特殊关键字，它代表“当前执行环境中的对象”。  
在对象方法中使用 this，表示它所在的对象。  
单独使用 this，指向全局对象，在浏览器中指 window

JSON 英文全称 JavaScript Object Notation，是一种轻量级的数据交换格式。用于存储和传输数据的格式，服务端向网页传递数据。  
JSON 语法：数据为键：值，用逗号分隔，大括号保存对象，中括号保存数组。  
示例：

```json
"sites":[
    {"name":"Runoob", "url":"www.runoob.com"},
    {"name":"Google", "url":"www.google.com"}
]
```

函数定义：

```js
function myProduct(a, b) {
  return a * b;
}
```

函数可以存储在变量中。此时函数不需要名称，只要用变量名来调用。  
示例：

```js
let x = function (a, b) {
  return a * b;
};
```

函数声明也可以提升到顶部，所以函数可以先调用再定义。

函数可以视为一个对象，有属性和方法。`arguments.length`属性返回函数调用过程接收到的的参数个数。  
示例：

```js
function myFunction(a, b) {
  return arguments.length;
}
```

`toString()`方法可将函数作为一个字符串返回。  
示例：

```js
function myFunction(a, b) {
  return a * b;
}
var txt = myFunction.toString();
```

箭头函数：`(参数) => {函数声明}` ，适用于只有一个语句的函数。  
示例：

```js
let x = function (x, y) {
  return x * y;
};

const x = (x, y) => x * y;
```

函数可以有自带参数，当调用函数时该参数未传入或 undefined 时，就取默认值。  
示例：

```js
function myProduct(x, y = 10) {
  return x * y;
}
```

函数有个内置的 arguments 对象,arguments 对象包含了函数调用的参数数组。  
示例，求和函数：

```js
x = sumAll(1, 123, 500, 115, 44, 88);

function sumAll() {
  let i,
    sum = 0;
  for (i = 0; i < arguments.length; i++) {
    sum += arguments[i];
  }
  return sum;
}
```

任何函数都能访问全局变量和上一层的函数变量。如示例中，使用内嵌函数`plus()`可以使当前函数能访问父函数的变量。  
示例：

```js
function add() {
  let counter = 0;
  function plus() {
    counter += 1;
  }
  plus();
  return counter;
}
```

类是用于创建对象的模板。我们使用 class 关键字来创建一个类，类体在一对大括号 {} 中，我们可以在大括号 {} 中定义类成员的位置，如方法或构造函数。每个类中包含了一个特殊的方法 constructor()，它是类的构造函数，这种方法用于创建和初始化一个由 class 创建的对象。  
格式：

```js
class 类名 {
    constructor() {...}
}
```

示例：

```js
class Runoob {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
}
```

以上实例创建了一个类，名为 "Runoob"。类中初始化了两个属性： "name" 和 "url"。

使用`new`创建对象。  
示例：

```js
let site = new Runoob("菜鸟教程", "https://www.runoob.com");
```

类表达式是定义类的另一种方法。类表达式可以命名或不命名。命名类表达式的名称是该类体的局部名称。  
示例：

```js
// 未命名/匿名类
let Runoob = class {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
};
console.log(Runoob.name);
// output: "Runoob"

// 命名类
let Runoob = class Runoob2 {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
};
console.log(Runoob.name);
// 输出: "Runoob2"
```

构造方法是一种特殊的方法：构造方法名为 constructor()，在创建新对象时会自动执行，用于初始化对象属性。如果不定义构造方法，会自动添加一个空的构造方法。  
可以用`方法名() {构造指令}`创建构造方法。  
示例：

```js
class Runoob {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    let date = new Date();
    return date.getFullYear() - this.year;
  }
}

let runoob = new Runoob("菜鸟教程", 2018);
document.getElementById("demo").innerHTML =
  "菜鸟教程 " + runoob.age() + " 岁了。";
```

还可以向类的方法发送参数。  
示例：

```js
class Runoob {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age(x) {
    return x - this.year;
  }
}

let date = new Date();
let year = date.getFullYear();

let runoob = new Runoob("菜鸟教程", 2020);
document.getElementById("demo").innerHTML =
  "菜鸟教程 " + runoob.age(year) + " 岁了。";
```

类继承：`class 类B extends 类A`表示类 B 继承类 A。  
用`super()`引用父类的构造方法。  
可以向原型对象中添加新的方法，示例：

```js
类名.prototype.方法名 = function () {
  执行代码;
};
```

变量和函数的声明会提升，但类不会。因此需先定义类，再使用。

静态方法是使用 static 关键字修饰的方法，又叫类方法，属于类的，但不属于对象，在实例化对象之前可以通过 类名.方法名 调用静态方法。静态方法不能在对象上调用，只能在类中调用。

## 测试题

引用名为 “runoob.js” 的外部脚本的正确语法是？  
`<script src="runoob.js">`

外部脚本不需要包含`<script>`标签

HTML 中注释用`<!---->`，js 中注释用`//`

定义数组：`var txt = new Array("runoob", "google", "taobao")`

如何把 7.25 四舍五入为最接近的整数？  
`Math.round(7.25)`

如何求得 2 和 4 中最大的数？  
`Math.max(2,4)`

打开名为 “window2” 的新窗口的 JavaScript 语法是？  
`window.open("https://www.runoob.com","window2")`

如何在浏览器的状态栏放入一条消息？  
`window.status = "put your message here"`

如何获得客户端浏览器的名称？  
`navigator.appName`

预测输出

```html
<script type="text/javascript">
  var a = "RUNOOB-GOOGLE";
  var x = a.lastIndexOf("G");
  document.write(x);
</script>
```

10 （在字符串 a 中，从右往左找，最后一次出现字符 "G" 的位置索引）

预测输出
```html
<script type="text/javascript" language="javascript">   
var a = "RunoobGoogle"; 
var result = a.substring(4, 5); 
document.write(result);  
</script> 
```

o （`string.substring(startIndex, endIndex)`返回从startIndex 开始（包含该位置），到 endIndex 结束（不包含该位置）之间的字符。）

预测输出
```html
<script type="text/javascript" language="javascript"> 
var x=5; 
var y=6; 
var res=eval("x*y"); 
document.write(res); 
</script> 
```

30 （`eval()` 是 JavaScript 中的一个函数,它会把字符串当作 JavaScript 代码执行）

JavaScript 中用于删除字符串开头和结尾空格的方法是什么？  
`trim()`

在 JavaScript中，我们没有 integer 和 float 等数据类型。什么方法可以用来检查数字是否是整数？  
`Number.isInteger(value)`

变量重新赋值后，可改变变量类型。 

数组对象的哪个函数为数组中的每个元素调用函数？  
`forEach()`   
（forEach() 是 JavaScript 数组对象的方法，用来对数组中每个元素执行一次指定的函数，可以理解成一个更简洁的 for 循环。格式：
```js
array.forEach(function(currentValue, index, array) {
  // 针对 currentValue 执行的操作
});
```
