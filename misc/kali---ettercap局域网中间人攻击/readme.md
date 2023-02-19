# kali---ettercap局域网中间人攻击

可以直接搜索ettercap打开图形化界面，也可以终端通过命令: `ettercap -G` 打开  

Sniffer -> Unified Sniffing, 选择 eth0 即可  

Hosts -> Hosts List  
Hosts -> Scan for hosts  
View -> Resolve IP address  
选择要攻击的ip 添加到Tartget1，选择 gateway 添加到 tartget2  


MitM -> Arp Poisoning, 勾选 `Sniff remote connections`  
Start -> Start sniffing  

然后理论上就能在那个被监控的人登陆的时候捕捉到东西了，  
但只是理论而已，我试了一下午都没用，，  


2017/9/2  
