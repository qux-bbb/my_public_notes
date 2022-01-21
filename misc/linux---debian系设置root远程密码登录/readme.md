# linux---debian系设置root远程密码登录

**相关文件：**  
/etc/ssh/sshd_config  

**修改选项：**  
PasswordAuthentication yes  
PermitRootLogin yes  

**保存并重启ssh服务：**  
```bash
service ssh restart
```

**让ssh服务开机自启:**  
执行命令：  
```bash
update-rc.d ssh enable
```
这个命令其实相当于修改`/etc/rc3.d/`下的`K01ssh`为`S03ssh`  


2019/10/02  
