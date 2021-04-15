# Supervisor

## 简介
Supervisor 是一个linux进程守护工具，在进程停止时可以自动重启进程  

官方文档: http://supervisord.org/  

个人推荐pip安装: `pip install supervisor`  


## 一个例子
准备3个脚本：  
/home/hello/Desktop/hello.sh  
```bash
#!/bin/bash

set -o errexit

while true
do
    echo hello `date` >> /home/hello/Desktop/the.log
    sleep 5
done
```
/home/hello/Desktop/world.sh  
```bash
#!/bin/bash

set -o errexit

while true
do
    echo world `date` >> /home/hello/Desktop/the.log
    sleep 5
done
```
/home/hello/Desktop/good.sh  
```bash
#!/bin/bash

set -o errexit

while true
do
    echo good `date` >> /home/hello/Desktop/the.log
    sleep 5
done
```

1个配置文件:   
/home/hello/Desktop/my_supervisord.conf  
```conf
; supervisor config file

[unix_http_server]
file=/home/hello/Desktop/supervisord/supervisor.sock   ; (the path to the socket file)

[supervisord]
logfile=/home/hello/Desktop/supervisord/supervisord.log ; (main log file;default $CWD/supervisord.log)
pidfile=/home/hello/Desktop/supervisord/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
childlogdir=/home/hello/Desktop/supervisord           ; ('AUTO' child log dir, default $TEMP)
user=hello

[supervisorctl]
serverurl=unix:///home/hello/Desktop/supervisord/supervisor.sock ; use a unix:// URL  for a unix socket

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[program:hello]
command=/home/hello/Desktop/hello.sh
user=hello
stderr_logfile=/home/hello/Desktop/supervisord/hello_err.log

[program:world]
command=/home/hello/Desktop/world.sh
autostart=false ; set autostart=false, default: true
user=hello
stderr_logfile=/home/hello/Desktop/supervisord/world_err.log

[group:echo_all]
programs=hello,world

[program:good]
command=/home/hello/Desktop/good.sh
autostart=false ; set autostart=false, default: true
user=hello
stderr_logfile=/home/hello/Desktop/supervisord/good_err.log
```

启动supervisord  
```bash
supervisord -c /home/hello/Desktop/my_supervisord.conf
```
如果想前台运行观察，可加 `-n` 选项  

使用supervisorctl查看和调整  
```bash
# 查看所有状态
supervisorctl -c /home/hello/Desktop/my_supervisord.conf status all
# 启动一个组的所有程序，注意最后有":"
supervisorctl -c /home/hello/Desktop/my_supervisord.conf start echo_all:
# 启动一个组的单个程序
supervisorctl -c /home/hello/Desktop/my_supervisord.conf start echo_all:world
# 启动不在组内的单个程序，名称可以根据 `status all` 确定
supervisorctl -c /home/hello/Desktop/my_supervisord.conf start good
# 停止所有进程
supervisorctl -c /home/hello/Desktop/my_supervisord.conf stop all
# 关闭supervisord
supervisorctl -c /home/hello/Desktop/my_supervisord.conf shutdown
```


## 其它

查看进程错误信息: `supervisorctl -c /home/hello/Desktop/my_supervisord.conf tail the_process stdout`  

最好指定配置文件，否则会使用默认配置文件，可能出现奇怪的问题  

supervisor默认不会停止一个进程的子进程，如果需要停止，可以添加 `stopasgroup = true` 选项，如：  
```conf
[program:good]
...
stopasgroup = true
...
```


2021/4/6  
