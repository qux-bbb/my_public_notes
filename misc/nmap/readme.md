# Nmap

官网: https://nmap.org/  

Nmap, Network Mapper, 扫描工具，一般用来确定网络上机器的操作系统、端口开放情况  

Zenmap是Nmap的图形化前端。  

官方给的几个命令行示例：  
```r
nmap -v -A scanme.nmap.org
nmap -v -sn 192.168.0.0/16 10.0.0.0/8
nmap -v -iR 10000 -Pn -p 80
```
图形化前端默认的例子：  
```r
nmap -T4 -A -v 1.2.3.4
```

选项解释：  
```r
-v: Increase verbosity level (use -vv or more for greater effect)
-A: Enable OS detection, version detection, script scanning, and traceroute
-sn: Ping Scan - disable port scan
-iR <num hosts>: Choose random targets
-Pn: Treat all hosts as online -- skip host discovery
-p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
-T<0-5>: Set timing template (higher is faster)
```

自己会用的一些例子：  
```r
nmap 192.168.0.1/24 -sn -n
# 扫描192.168.0.1/24网段存活的主机，速度非常快
# -sn 表示不扫描端口
# -n 表示不进行DNS解析
# 当目标在局域网时，nmap默认会进行ARP扫描，如果需要明确使用ARP扫描，可以使用"-PR"选项
# https://nmap.org/man/zh/man-host-discovery.html
```


2021/7/24  
