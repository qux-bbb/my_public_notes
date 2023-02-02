# masscan

MASSCAN: Mass IP port scanner, TCP端口扫描器，异步发送SYN数据包，在5分钟内扫描整个互联网。  

github地址: https://github.com/robertdavidgraham/masscan  

使用示例：  
```r
# 扫描指定网段的指定端口
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112
# 扫描整个网络
masscan 0.0.0.0/0 -p0-65535
```


2023/2/2  
