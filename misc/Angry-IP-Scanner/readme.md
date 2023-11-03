# Angry IP Scanner

Angry IP Scanner 是一个开源跨平台的网络扫描工具，可以在 Linux, Windows, Mac OS X 上运行，使用java编写。  

官网: https://angryip.org/  

工具默认使用ICMP ping扫描主机，可以修改  
工具->设置->扫描->Ping->Ping方法，在这里可以选择多种方法：  
```r
Windows ICMP
UDP
TCP
UDP+TCP
Java内置
ARP（仅内网）
```
此外，在正常使用时，也可以选择是否勾选"扫描未响应主机，不回复ping"  

为了提高扫描速度，可以在设置中修改"最大线程"  


2023/11/4  
