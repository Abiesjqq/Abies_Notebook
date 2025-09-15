~~我要用 tmux 代替 screen!~~

## 基本概念

- `session`: 会话 (任务)
- `windows`: 窗口
- `pane`: 窗格

关系： $\mathrm{pane} \in \mathrm{window} \in \mathrm{session}$

## Session 操作

### 启动

默认 `tmux` 启动一个 id 为 0 的 session

```bash
tmux new -s session-name
```

### 分离

当前 session 与当前窗口分离，session 转到后台运行.

```bash
tmux detach
```

### 绑定

```bash
tmux attach -t session-name
```

### 切换

```bash
tmux switch -t session-name
```

### 退出

```bash
tmux kill-session -t session-name
```

### 重命名

```bash
tmux rename-session -t old-session new-session
```

## Window 操作

### 新建

```bash
tmux new-window -n your-window-name
```

### 切换窗口

- ctrl+b c: 创建一个新窗口（状态栏会显示多个窗口的信息）
- ctrl+b p: 切换到上一个窗口（按照状态栏的顺序）
- ctrl+b n: 切换到下一个窗口
- ctrl+b w: 从列表中选择窗口（这个最好用）

### 重命名

```bash
tmux rename-window -t old_name new_name
```

## Pane 操作

### 划分窗格

```bash
# 划分为上下两个窗格
tmux split-window

# 划分左右两个窗格
tmux split-window -h
```

- 左右划分：ctrl+b %
- 上下划分：ctrl+b "

### 关闭窗格

- ctrl + d, 如果只有一个窗格就是关闭 window 了.

## 查看

```bash
# 列出所有快捷键，及其对应的 Tmux 命令
tmux list-keys

# 列出所有 Tmux 命令及其参数
tmux list-commands

# 列出当前所有 Tmux 会话的信息
tmux info
```