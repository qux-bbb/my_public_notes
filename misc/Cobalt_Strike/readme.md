# Cobalt Strike

官网: https://www.cobaltstrike.com/  

Cobalt Strike, 一个把渗透过程集成的工具，有作为C2的服务端，有去连接服务端的客户端，图形界面操作，整个渗透过程变得简单了。  

Cobalt Strike 运行需要安装jdk，针对Cobalt4.4，官方文档提到的openjdk-11-jdk已经不能用了，可以换成openjdk-17-jdk。  


## 简单使用

在ubuntu18下使用服务端  

运行teamserver：  
```r
sudo ./teamserver 1.2.3.4 hello
# 1.2.3.4 是本机ip，官方不建议用0.0.0.0
# hello 是登录使用的密码，自定义即可，正式使用不建议弱密码
```

使用脚本启动Cobalt Strike，连接teamserver: `./start.sh`  

登录界面  
- ip可以和上面命令一样，也可以用127.0.0.1  
- 用户名任意  
- 密码需要和上面命令对应  

登录之后，首先添加Listener: Cobalt Strike -> Listeners -> Add, 配置相应选项即可  
生成一个Windows下运行的程序: Attacks -> Packages -> Windows Executable, 选择相应的选项，生成即可  

在Windows下运行之前生成的程序，很快在服务端就可以观察到已连接的机器，选择，右键操作即可  


---
2021/11/17  
