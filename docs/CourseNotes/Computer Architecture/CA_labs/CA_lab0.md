## 怎么下载到本地？

若直接使用http协议下载，需要GitLab身份验证（但浙大统一身份认证不行，不知道要填什么）。需要使用ssh key。

!!! remarks "创建SSH key步骤"

    1. 在终端运行以下指令，生成ssh key

    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```

    2. 运行后提示`Enter file in which to save the key (/home/user/.ssh/id_ed25519):`，如果之前生成过建议自己输入路径（如果回车用默认路径，下一步提示`C:\Users\xxx/.ssh/id_ed25519 already exists. Overwrite (y/n)?`，输入`n`后自动退出而不是重命名……）
    3. 提示设置密码`Enter passphrase (empty for no passphrase):`，可直接回车
    4. 查看公钥，将`id_ed25519`替换成保存的路径名

    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```

    输出类似`ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI.... your_email@example.com`

    5. 复制上述整行内容，添加到ZJU Git
    6. clone时选择git协议，如：

    ```bash
    git clone git@git.zju.edu.cn:zju-arch/sp26/stu/xxxxxxx/arch-framework-sp26.git
    ```
