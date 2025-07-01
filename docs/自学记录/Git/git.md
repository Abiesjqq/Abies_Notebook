## 简化版本：上传 MyProject 项目

1. 在本地创建项目并初始化 Git 仓库
```bash
mkdir MyProject          # 创建项目文件夹
cd MyProject             # 进入目录
git init                 # 初始化 Git 仓库
```
2. 创建文件并提交
```bash
git add .                # 添加所有文件到暂存区
git commit -m "<comment>"
```
3. 在 GitHub 上新建一个空仓库
4. 将本地仓库连接到 GitHub 仓库
```bash
git remote add origin <URL>
```
5. 推送本地内容到 GitHub
```bash
git branch -M main             # 确保分支叫 main（GitHub 默认主分支）
git push -u origin main        # 推送到 GitHub 并绑定远程主分支
```

??? info "注意"
    如果本地和远程同时对某个文件更改，可能因为error: Your local changes to the following files would be overwritten by merge导致无法拉取。  
    可以按以下方法执行：  
    1. `git stash` 保存本地改动  
    2. `git pull origin main` 拉取远程代码  
    3. `git stash pop` 恢复本地修改，可能需要手动选择保留哪部分修改  

## 提交

- `git commit` 创建提交

## 分支

- `git branch <BranchName>` 创建分支
- `git branch A C` 在提交 C 的位置上创建分支 A
- `git checkout <BranchName>` 切换分支
- `git checkout -b <BranchName>` 创建分支并切换到新分支
- `git checkout -b A C` 在提交 C 的位置上创建分支 A，并切换到分支 A

- `git merge <BranchName>` 将 BranchName 合并到 main（当前 checkout 的分支），此时 main 有多个 parent，包含了两个分支的提交记录
- `git checkout A; git merge main` 将 main 合并到 A
- `git rebase <BranchName>` 将当前 checkout 的分支的提交搬运到 BranchName

> 将 A 合并到 main:  
>
> ```  
> git checkout A  
> git rebase main  
> ```  

## 移动

HEAD 总是指向当前分支上最近一次提交记录。分离的 HEAD 就是让其指向了某个具体的提交记录而不是分支名。

- `git checkout <Name>` 使 HEAD 指向 Name（可以是某个提交，基于哈希值指定提交记录）

相对引用：
使用`^`向上移动 1 个提交记录
使用`~<num>`向上移动多个提交记录，如`~3`

- `git checkout HEAD^` 使 HEAD 指向当前 HEAD（一般是最近的提交记录）的 parent
- `git checkout HEAD~3` 使 HEAD 后退 3 步

- `git branch -f A` 强制将分支 A 指向当前 HEAD
- `git branch -f A B` 强制让分支 A 指向提交 B 所在的位置
- `git branch -f main HEAD~3` 将 main 分支强制指向 HEAD 的第 3 级 parent 提交

- `git cherry-pick <CommitName>` 将其他分支上的提交 CommitName 复制到当前分支
- `git cherry-pick c2 c4` 将 c2，c4 依次复制到当前分支

- `git rebase -i <CommitName>` 从 CommitName 的下一个提交开始（不包括它），列出直到当前分支 HEAD 的所有提交，供你在交互式界面（interactive）中编辑、合并、重排、改写等

## 撤销

- `git reset HEAD~2` 回退 2 个提交记录，但对远程分支无效
- `git revert HEAD` 创建更改的提交

## 远程操作

远程分支命名：`远程仓库名/分支名`，远程仓库名默认为`origin`。切换到远程分支时，自动进入分离 HEAD 状态。

- `git clone` 复制整个远程仓库，创建一个本地分支，并跟踪远程的同名分支。
- `git fetch` 从远程仓库下载本地仓库中缺失的提交记录，并更新远程分支指针（实际上将本地仓库中的远程分支更新成了远程仓库相应分支最新的状态，但不会改变本地仓库的状态）
- `git pull` 等价于先`git fetch`再`git merge`
- `git push` 将变更上传到指定的远程仓库，并在远程仓库上合并新提交记录
- `git push origin A` 把本地的分支 A 推送到远程仓库 origin（默认），在远程也创建一个同名分支 A

当远程仓库更新后，直接`git push`会由于历史偏移而失败。
解决方法：先使工作基于最新的远程分支

- `git fetch; git rebase o/main; git push` 用`git fetch`更新了本地仓库中的远程分支，然后用 `rebase` 将我们的工作移动到最新的提交记录下，最后再用 - `git push` 推送到远程仓库
- `git fetch; git merge o/main; git push` 用 `git fetch` 更新了本地仓库中的远程分支，然后合并了新变更到我们的本地分支（为了包含远程仓库的变更），最后我们用 `git push` 把工作推送到远程仓库
- `git pull --rebase` 等价于`git fetch`和`git rebase o/main`
- `git pull` 等价于`git fetch`和`git merge o/main`
