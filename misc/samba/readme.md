# samba

samba 可以用于局域网文件共享  
Server Messages Block  

## ubuntu安装配置samba
安装: `sudo apt install samba`  
创建共享目录: `mkdir /home/<username>/sambashare/`  
编辑配置文件: /etc/samba/smb.conf, 在结尾添加：  
```r
[sambashare]
    comment = Samba on Ubuntu
    path = /home/username/sambashare
    read only = no
    browsable = yes
```
重启Samba: `sudo service smbd restart`  
允许samba流量通过防火墙: `sudo ufw allow samba`  
设置已存在用户的samba密码: `sudo smbpasswd -a username`  

ubuntu文件管理器访问: `smb://ip-address/sambashare`  
windows文件管理器访问: `\\ip-address\sambashare`  

原链接: https://ubuntu.com/tutorials/install-and-configure-samba  


## samba修改密码后windows无法登录
windows下打开命令行，执行: `net use`，  
如果看到和samba服务器ip一样的行，使用该命令删除连接: `net use \\1.2.3.4\sambashare /del /y`  
`\\1.2.3.4\sambashare`是"远程"下的项，根据实际看到的调整  

原链接: https://www.cnblogs.com/linuxws/p/11138335.html  


---
2021/10/27  
