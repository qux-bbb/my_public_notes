# masscan

MASSCAN: Mass IP port scanner, TCP端口扫描器，异步发送SYN数据包，在5分钟内扫描整个互联网。  
mass, /mæs/ 是大量、大批的意思  

github地址: https://github.com/robertdavidgraham/masscan  

使用示例：  
```r
# 扫描指定网段的指定端口
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112
# 扫描整个网络
masscan 0.0.0.0/0 -p0-65535
# 可以指定结果格式和导出位置，导出文件格式默认是xml，list比较好
masscan 0.0.0.0/0 --ports 0-65535 -output-format binary|grepable|json|list|xml --output-filename path/to/file
```

参考: tldr  


2023/2/2  
