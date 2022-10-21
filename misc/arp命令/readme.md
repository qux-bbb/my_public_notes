# arp命令

arp, Address Resolution Protocol, 地址解析协议  

arp命令可以用来看本地缓存中ip对应的mac地址。  

```r
# 查看所有缓存(ip和mac对应关系)
arp -a
# 查看指定ip地址对应的mac地址
arp -a 192.168.0.2

# 清除所有缓存
arp -d *
# 清除指定地址缓存
arp -d 192.168.0.2
```


2017/1/1  
