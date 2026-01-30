# sftp

sftp, SSH File Transfer Protocol, SSH 文件传输协议，和FTPS完全不同，FTPS 是在 FTP 协议基础上添加了 SSL/TLS 加密，而 sftp 是在 SSH 协议基础上添加了文件传输功能。

感觉sftp适合交互式使用

常用命令
```bash
# 连接服务器
sftp username@hostname
# 或指定端口
sftp -P 2222 username@hostname

# 连接后可以使用类似 FTP 的命令：
put local_file.txt        # 上传文件
get remote_file.txt       # 下载文件
ls                        # 列出远程目录文件
lls                       # 列出本地目录文件
cd path                   # 切换远程目录
lcd path                  # 切换本地目录
```
