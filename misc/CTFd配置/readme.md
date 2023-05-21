# CTFd配置

创建一个虚拟python环境：  
`virtualenv env4CTFd (名字自己随便写)`

进入虚拟环境：  
`source env4CTFd/bin/activate`

把CTFd clone下来：  
`git clone https://github.com/CTFd/CTFd.git`

配置所需环境：  
`./prepare.sh`

修改serve.py:  
debug改成False  
host改成 0.0.0.0  

后台启动：  
`nohup python serve.py &`

复制主题位置：  
`CTFd\CTFd\themes`

退出虚拟环境：  
`deactivate`

结束后台进程：  
`ps -aux | grep serve.py   # 找到对应的进程号`  
`kill 进程号`  



config.py可以自己修改  


2017/10/23  
