# linux---ssh
使用ssh可远程登陆服务器  

最基础方式，默认端口是 22  
```
ssh hello@192.168.1.2
```

指定端口  
```
ssh hello@192.168.1.2 -p 233
```

配置文件  
```bash
# 客户端配置文件，一般不改
/etc/ssh/ssh_config
# 服务端配置文件，可以设置禁止远程密码登录
/etc/ssh/sshd_config
```
