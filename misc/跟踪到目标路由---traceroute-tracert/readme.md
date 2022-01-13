# 跟踪到目标路由---traceroute-tracert

traceroute(linux)和tracert(windows)可以用来跟踪机器到目标机器的路由，可用于诊断网络连接问题。  

traceroute工作原理：  
> Traceroute收到目的主机的IP后，首先给目的主机发送一个TTL=1的UDP数据包，而经过的第一个路由器收到这个数据包以后，就自动把TTL减1，而TTL变为0以后，路由器就把这个包给抛弃了，并同时产生 一个主机不可达的ICMP数据报给主机。主机收到这个数据报以后再发一个TTL=2的UDP数据报给目的主机，然后刺激第二个路由器给主机发ICMP数据 报。如此往复直到到达目的主机。这样，traceroute就拿到了所有的路由器ip。  


简单使用  
```r
# linux
traceroute www.baidu.com

# windows
tacert www.baidu.com
```


20201220  
