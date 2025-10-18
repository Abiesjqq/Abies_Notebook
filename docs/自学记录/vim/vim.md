# Vim 操作大全（Cheat Sheet）

> 一份完整的 **Vim 操作速查笔记**
> 适用于 Ubuntu / WSL / VSCode / Neovim 等环境。

---

## 🗂️ 基本模式（Modes）

| 模式                        | 进入方式             | 说明                             |
| --------------------------- | -------------------- | -------------------------------- |
| **普通模式 (Normal)**       | `Esc`                | 默认模式，用于移动、复制、删除等 |
| **插入模式 (Insert)**       | `i` / `a` / `o`      | 编辑文字                         |
| **可视模式 (Visual)**       | `v` / `V` / `Ctrl+v` | 选中字符、行、矩形区域           |
| **命令模式 (Command-line)** | `:`                  | 执行保存、退出、搜索等命令       |

---

## ✍️ 插入模式（Insert Mode）

| 操作         | 命令  | 说明                        |
| ------------ | ----- | --------------------------- |
| 插入光标前   | `i`   | insert before cursor        |
| 插入光标后   | `a`   | append after cursor         |
| 插入行首     | `I`   | insert at beginning of line |
| 插入行尾     | `A`   | append at end of line       |
| 在下方新建行 | `o`   | open a new line below       |
| 在上方新建行 | `O`   | open a new line above       |
| 退出插入模式 | `Esc` | 回到普通模式                |

---

## 📦 文件操作

| 操作         | 命令          | 说明                |
| ------------ | ------------- | ------------------- |
| 保存文件     | `:w`          | write               |
| 保存并退出   | `:wq` 或 `:x` | save & quit         |
| 退出不保存   | `:q!`         | quit without saving |
| 仅退出       | `:q`          | quit                |
| 另存为       | `:w filename` | save as filename    |
| 打开文件     | `:e filename` | edit file           |
| 查看打开文件 | `:ls`         | show buffer list    |
| 切换文件     | `:b1`, `:b2`  | switch buffer       |

---

## 🧭 光标移动（Normal 模式）

| 操作                    | 命令                  | 说明                        |
| ----------------------- | --------------------- | --------------------------- |
| 左 / 下 / 上 / 右       | `h` / `j` / `k` / `l` | 基本移动                    |
| 行首 / 行尾             | `0` / `$`             | move to start / end of line |
| 向前 / 向后移动一个单词 | `w` / `b`             | word forward/backward       |
| 移动到文件开头 / 结尾   | `gg` / `G`            | first / last line           |
| 跳到第 n 行             | `:n` 或 `nG`          | go to line n                |
| 屏幕移动                | `Ctrl+u` / `Ctrl+d`   | up / down half page         |
| 向上 / 向下滚动一行     | `Ctrl+y` / `Ctrl+e`   | scroll up/down one line     |
| 定位到匹配的括号        | `%`                   | match parentheses           |

---

## ✂️ 编辑操作（删除 / 复制 / 粘贴）

| 操作             | 命令           | 说明                  |
| ---------------- | -------------- | --------------------- |
| 删除一个字符     | `x`            | delete char           |
| 删除整行         | `dd`           | delete line           |
| 删除 n 行        | `ndd`          | delete n lines        |
| 删除到行尾       | `D`            | delete to end of line |
| 复制（yank）一行 | `yy`           | yank line             |
| 复制选定区域     | `y`            | in visual mode        |
| 粘贴到光标后     | `p`            | paste                 |
| 粘贴到光标前     | `P`            | paste before cursor   |
| 替换字符         | `r<char>`      | replace one character |
| 撤销 / 重做      | `u` / `Ctrl+r` | undo / redo           |

---

## 🔍 搜索与替换

| 操作             | 命令            | 说明                        |
| ---------------- | --------------- | --------------------------- |
| 搜索字符串       | `/pattern`      | forward search              |
| 向后搜索         | `?pattern`      | backward search             |
| 下一个匹配       | `n`             | next result                 |
| 上一个匹配       | `N`             | previous result             |
| 替换单个匹配     | `:s/old/new/`   | substitute once             |
| 替换整行所有匹配 | `:s/old/new/g`  | substitute globally in line |
| 替换全文件       | `:%s/old/new/g` | substitute globally in file |
| 大小写不敏感搜索 | `/pattern\c`    | case-insensitive search     |

---

## 🎯 可视模式（Visual Mode）

| 操作          | 命令      | 说明              |
| ------------- | --------- | ----------------- |
| 进入字符选择  | `v`       | visual mode       |
| 进入行选择    | `V`       | visual line mode  |
| 进入块选择    | `Ctrl+v`  | visual block mode |
| 复制          | `y`       | yank              |
| 删除          | `d`       | delete            |
| 粘贴          | `p`       | paste             |
| 缩进 / 反缩进 | `>` / `<` | indent / unindent |

---

## 🧩 多文件 / 分屏操作

| 操作         | 命令                | 说明                      |
| ------------ | ------------------- | ------------------------- |
| 水平分屏     | `:sp filename`      | split window horizontally |
| 垂直分屏     | `:vsp filename`     | split vertically          |
| 切换分屏     | `Ctrl+w` + `方向键` | move between windows      |
| 关闭当前分屏 | `:q`                | quit window               |
| 打开新标签页 | `:tabnew`           | new tab                   |
| 切换标签页   | `gt` / `gT`         | next / previous tab       |

---

## ⚡ 快捷命令组合示例

| 目的             | 命令            | 含义              |
| ---------------- | --------------- | ----------------- |
| 删除 3 行        | `3dd`           | delete 3 lines    |
| 复制 5 行        | `5yy`           | yank 5 lines      |
| 跳到第 20 行     | `20G`           | go to line 20     |
| 搜索并替换全文件 | `:%s/foo/bar/g` | replace all       |
| 保存并退出       | `:wq`           | write + quit      |
| 不保存退出       | `:q!`           | quit without save |

---

## 💡 小技巧

- 打开行号显示：`:set number`
- 打开语法高亮：`:syntax on`
- 设置缩进宽度：`:set tabstop=4 shiftwidth=4`
- 设置自动缩进：`:set autoindent`
- 查看帮助文档：`:help <command>`
  例：`:help :wq`

---

## 🚀 退出困境：当你卡在 Vim 里

```bash
# 最经典的组合：
Esc          # 回到普通模式
:q!          # 不保存退出
:wq          # 保存并退出
```

---

## 🧱 推荐配置（可放入 ~/.vimrc）

```vim
set number          " 显示行号
syntax on           " 启用语法高亮
set tabstop=4       " Tab 宽度
set shiftwidth=4    " 缩进宽度
set expandtab       " 用空格代替 Tab
set autoindent      " 自动缩进
set cursorline      " 高亮当前行
set showmatch       " 匹配括号高亮
set hlsearch        " 搜索结果高亮
set incsearch       " 增量搜索
```

---

✅ **总结：**

> - Vim 的本质是“模式编辑器”；
> - 常用组合就是：
>   `i` → 插入； `Esc` → 普通； `:wq` → 保存退出；
> - 学会 hjkl + dd + yy + p，就能在终端中高效写代码！

非常好 👍
你现在已经掌握了 Vim 的基本操作，那么接下来我们讲的就是**“如何在 Vim 里真正写代码”**——
也就是让 Vim 不只是个文本编辑器，而是一个**轻量级 IDE**（代码开发环境）。

下面内容是系统化教程，格式为 **Markdown 教学笔记**，你可以直接放到你的 MkDocs「Abies Notebook」里用。

---

# 🧠 Vim 写代码全攻略（从入门到高效）

> 教你如何在 Vim 中进行 **代码编写、运行、调试、补全、格式化与项目管理**

---

## 🗂️ 一、Vim 基础结构回顾

Vim 有三种主要模式：

| 模式             | 作用                           |
| ---------------- | ------------------------------ |
| **Normal 模式**  | 导航 / 删除 / 复制 / 粘贴      |
| **Insert 模式**  | 输入代码                       |
| **Command 模式** | 执行命令（保存、运行、设置等） |

进入插入模式：

```bash
i   # 在光标前插入
a   # 在光标后插入
o   # 在下一行插入新行
```

退出插入模式：

```bash
Esc
```

---

## ✍️ 二、创建并编写代码文件

### 1. 新建文件

```bash
vim hello.cpp
```

或在 Vim 内部：

```vim
:e hello.cpp
```

### 2. 编写代码

按 `i` 进入插入模式，输入代码，例如：

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    cout << "Hello, Vim!" << endl;
    return 0;
}
```

按 `Esc` 退出编辑模式。

### 3. 保存与退出

```bash
:w      # 保存
:wq     # 保存并退出
:q!     # 不保存退出
```

---

## ⚙️ 三、编译与运行代码（C/C++/Python 等）

### 🧩 方法 1：在 Vim 内执行 shell 命令

在普通模式下输入：

```vim
:!g++ hello.cpp -o hello && ./hello
```

输出：

```
Hello, Vim!
```

你也可以为不同语言执行：

| 语言   | 命令                               |
| ------ | ---------------------------------- |
| C      | `:!gcc main.c -o main && ./main`   |
| C++    | `:!g++ main.cpp -o main && ./main` |
| Python | `:!python3 script.py`              |
| Java   | `:!javac Main.java && java Main`   |

---

### 🧩 方法 2：配置自定义编译快捷键（推荐）

在 `~/.vimrc` 添加：

```vim
autocmd FileType c,cpp map <F5> :w<CR>:!g++ % -o %< && ./%<<CR>
autocmd FileType python map <F5> :w<CR>:!python3 %<CR>
```

这样：

- 按 `F5` 自动保存 + 编译 + 运行；
- `%` 表示当前文件名；
- `%<` 表示去掉扩展名。

---

## 🧱 四、常用代码辅助功能

### 🔹 1. 行号与高亮

```vim
:set number          " 显示行号
:syntax on           " 启用语法高亮
:set cursorline      " 高亮当前行
:set showmatch       " 括号匹配提示
```

### 🔹 2. 自动缩进

```vim
:set autoindent
:set smartindent
:set tabstop=4
:set shiftwidth=4
:set expandtab
```

### 🔹 3. 注释技巧（手动）

- C/C++：`//` 或 `/* ... */`
- Python：`#`
- Vim 插件可以自动注释（见下）。

---

## 🧩 五、提升生产力的插件（推荐）

> Vim 本身轻量，但插件系统极强，可以像 VSCode 一样增强。

### 📦 插件管理器：vim-plug

安装：

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

在 `~/.vimrc` 添加：

```vim
call plug#begin('~/.vim/plugged')

" 基础增强
Plug 'preservim/nerdtree'        " 目录树
Plug 'jiangmiao/auto-pairs'      " 自动补全括号
Plug 'tpope/vim-commentary'      " 快捷注释
Plug 'scrooloose/syntastic'      " 语法检查
Plug 'vim-airline/vim-airline'   " 状态栏美化

" 代码补全（推荐配合 clangd / coc.nvim）
Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()
```

然后在 Vim 内执行：

```vim
:PlugInstall
```

---

## 📁 六、代码目录管理

使用 `NERDTree`：

| 操作             | 命令              | 说明        |
| ---------------- | ----------------- | ----------- |
| 打开侧边文件树   | `:NERDTreeToggle` | 文件管理器  |
| 在树中创建新文件 | `m` + `a`         | add a file  |
| 删除文件         | `m` + `d`         | delete file |
| 打开文件         | `Enter`           | open file   |

---

## 🧮 七、代码补全与错误提示

安装 `coc.nvim` 后，支持智能补全（类似 VSCode）：

| 操作     | 命令           |
| -------- | -------------- |
| 自动补全 | 输入时自动提示 |
| 跳转定义 | `gd`           |
| 查看文档 | `K`            |
| 修复错误 | `<leader>qf`   |

示例配置（C/C++ 用 clangd）：

```bash
:CocInstall coc-clangd
```

---

## 🧰 八、调试与运行整合

对于复杂项目，你可以：

- 使用 `Makefile`：

  ```bash
  :!make
  ```

- 或在 `.vimrc` 定义项目级命令：

  ```vim
  map <F9> :!make run<CR>
  ```

---

## 🧪 九、Python 示例

```bash
vim test.py
```

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))
```

执行：

```vim
:!python3 %
```

输出：

```
8
```

---

## 🧱 结语

| 目的     | 操作                           |
| -------- | ------------------------------ |
| 编辑代码 | `i` → 写代码 → `Esc`           |
| 保存运行 | `:w` → `:!g++ % -o %< && ./%<` |
| 高效配置 | `.vimrc` 添加快捷键与插件      |
| 项目管理 | `NERDTree + coc.nvim`          |

---

✅ **一句话总结：**

> Vim 写代码的核心思路是：
>
> 1. 插入模式输入；
> 2. 命令模式运行；
> 3. 配置 `.vimrc` 提升效率；
> 4. 插件化打造属于自己的轻量 IDE。
