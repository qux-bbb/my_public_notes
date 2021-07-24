# Nmap

官网: https://nmap.org/  

Nmap, Network Mapper, 扫描工具，一般用来确定网络上机器的操作系统、端口开放情况  

Zenmap是Nmap的图形化前端。  

官方给的几个命令行示例：  
```bat
nmap -v -A scanme.nmap.org
nmap -v -sn 192.168.0.0/16 10.0.0.0/8
nmap -v -iR 10000 -Pn -p 80
```
图形化前端默认的例子：  
```bat
nmap -T4 -A -v 1.2.3.4
```

选项解释：  
```
-v: Increase verbosity level (use -vv or more for greater effect)
-A: Enable OS detection, version detection, script scanning, and traceroute
-sn: Ping Scan - disable port scan
-iR <num hosts>: Choose random targets
-Pn: Treat all hosts as online -- skip host discovery
-p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
-T<0-5>: Set timing template (higher is faster)
```


2021/7/24  
