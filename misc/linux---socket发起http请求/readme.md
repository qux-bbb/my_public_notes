# linux---socket发起http请求

keywords: 网络请求 访问百度  

如果把发送的内容改成单纯的数据，那就是tcp了  
如果再把 SOCK_STREAM 换成 SOCK_DGRAM，那就是udp了  

域名和ip的处理方式不太一样  
域名版本: [socket_http_domain.c](./files/socket_http_domain.c)  
ip版本: [socket_http_ip.c](./files/socket_http_ip.c)  


参考链接：  
1. https://www.geeksforgeeks.org/socket-programming-cc
2. https://www.kernel.org/doc/man-pages


2022/2/20  
