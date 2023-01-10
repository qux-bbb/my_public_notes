# 确定服务器ip地址

情景：一台服务器，没有登录权限，可以网线直连，怎么知道服务器ip地址？  

方法：把windows笔记本和服务器用网线直连，在笔记本上打开wireshark，如果服务器设置了ip地址，就可以看到ARP包，也就知道服务器ip了。  
如果服务器有多个网口，可以一个一个试，直到wireshark看到ARP包。  

确定服务器ip地址后，就可以把笔记本相应的网卡设置同网段(一般是24位掩码)的ip，和服务器三层(网络层)互通了。  

参考链接: https://superuser.com/questions/1005693/getting-ip-address-of-a-direct-connected-computer  


2023/1/10  
