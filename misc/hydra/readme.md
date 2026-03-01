# hydra

github地址: https://github.com/vanhauser-thc/thc-hydra  

hydra - a very fast network logon cracker which supports many different services  

hydra可以用来爆破多种服务的用户名密码，以下举例  

```bash
# 破解FTP
hydra -L user.txt -P pass.txt -P ftp://127.0.0.1
# 破解SSH
hydra -L user.txt -P pass.txt -P ssh://127.0.0.1
# 破解SMB
hydra -L user.txt -P pass.txt -P smb://127.0.0.1
# 破解MSSQL，即SQL Server，默认可能因为爆破次数多导致帐户被锁定，即使有正确密码也会爆破失败
hydra -L user.txt -P pass.txt -P mssql://127.0.0.1
```
固定一个用户名或密码则选项小写，举例：  
```bash
hydra -l hello_user -P pass.txt -P ftp://127.0.0.1
```

如果登录成功，则可看到高亮显示  
有图形化界面xhydra(新版kali没有了)  


来自：白帽学院  
