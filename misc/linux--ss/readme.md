# linux--ss

keywords: 占用端口 端口占用  

ss is used to dump socket statistics. It allows showing information similar to netstat.  It can display more TCP and state information than other tools.  

一些选项：  
```r
-t, --tcp
       Display TCP sockets.
-u, --udp
       Display UDP sockets.
-n, --numeric
       Do not try to resolve service names.  Show  exact  bandwidth
       values, instead of human-readable.
-l, --listening
       Display only listening sockets (these  are  omitted  by  de‐
       fault).
-p, --processes
       Show process using socket.
```

最常用的用法：  
```bash
ss -tunlp
```


2024/6/24  
