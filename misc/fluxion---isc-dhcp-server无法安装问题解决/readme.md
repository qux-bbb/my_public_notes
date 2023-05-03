# fluxion---isc-dhcp-server无法安装问题解决

```
0x00
fluxion 社工破密码神器
但是在安装的时候遇到了问题，没法安装isc-dhcp-server
kali本来有这个，但是版本比较高，依赖关系不满足，在小伙伴帮助下，终于解决

0x01
先安装 aptitude，这个跟apt-get差不多，详细了解自行百度
apt-get install aptitude
会遇到依赖问题，把依赖的两个也用apt-get安装一下

0x02
然后就开始安装isc-dhcp-server了
aptitude install isc-dhcp-server
先选 n ，之后问是否降到低的版本，选 Y 即可
```


2016/6/22  
