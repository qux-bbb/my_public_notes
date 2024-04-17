# linux---sudo

keywords: root sudo 时间  

## 简介
sudo, superuser do, 以系统管理者 root 的身份执行指令  

举例，重启ftp服务：  
```bash
sudo systemctl restart vsftpd
```

## 修改默认超时时间
使用sudo时，默认超时时间是15分钟，表示输过一次密码之后，15分钟之内使用sudo不再需要密码  
时间太短，可以通过 visudo 调整一下  

```bash
sudo visudo
```
内容增加一行：  
```r
Defaults timestamp_timeout=1440
```
这样输过一次密码之后，1440分钟(24小时)之内使用sudo不再需要密码  

来源：  
1. https://zhuanlan.zhihu.com/p/672320308
2. chatgpt


---
2020/6/30  
