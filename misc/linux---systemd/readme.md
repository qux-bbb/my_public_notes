# linux---systemd
systemd代替旧的service，主要用来管理服务程序，据说比service简单好用。  

官网: https://systemd.io/  

## 简单的例子  
### 1 一个待执行脚本
/home/hello/Desktop/test.sh  
```bash
#!/bin/bash

set -o errexit

while true
do
    date >> /home/hello/Desktop/the.log
    sleep 5
done
```
记得设置可执行权限: `chmod 764 test.sh`  

### 2 对应的配置文件
/etc/systemd/system/test.service  
```conf
[Unit]
Description=Test Service

[Service]
ExecStart=/home/hello/Desktop/test.sh

[Install]
WantedBy=multi-user.target
```
本来想放在 `/etc/systemd/user` 下，但是不生效  

### 3 简单的操作
创建的服务默认不启动，需要自己操作。  

简单操作示例如下：  
```bash
# 查看test服务状态
systemctl status test
# 启动test服务
systemctl start test
# 停止test服务
systemctl stop test
# 设置test服务自启动
systemctl enable test
# 禁止test服务自启动
systemctl disable test
```


## 参考链接
1. https://askubuntu.com/questions/919054/how-do-i-run-a-single-command-at-startup-using-systemd  
2. https://www.cnblogs.com/lanbosm/articles/13828784.html  


2021/4/11  
