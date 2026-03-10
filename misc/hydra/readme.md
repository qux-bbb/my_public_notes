# hydra

hydra - a very fast network logon cracker which supports many different services  
可以用来爆破多种服务的用户名密码

github地址: https://github.com/vanhauser-thc/thc-hydra

示例如下：
```bash
# 爆破FTP
hydra -L user.txt -P pass.txt ftp://127.0.0.1
# 爆破SSH
hydra -L user.txt -P pass.txt ssh://127.0.0.1
# 爆破SMB
hydra -L user.txt -P pass.txt smb://127.0.0.1
# 爆破MSSQL，即SQL Server，默认可能因为爆破次数多导致帐户被锁定，即使有正确密码也会爆破失败
hydra -L user.txt -P pass.txt mssql://127.0.0.1
```
固定一个用户名或密码则选项小写，举例：  
```bash
hydra -l hello_user -P pass.txt ftp://127.0.0.1
```

如果登录成功，则可看到高亮显示  


来自：白帽学院  
