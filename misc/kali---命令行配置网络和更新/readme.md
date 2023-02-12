# kali---命令行配置网络和更新

## 配置dns服务器
编辑 `/etc/resolv.conf` 内容如下：  
```r
domain
nameserver 10.10.10.10
nameserver 102.54.16.2
```

## 配置网卡静态ip地址
编辑 `/etc/network/interfaces` 内容如下：  
```r
auto eth0
iface eth0 inet static
address 192.168.0.1
netmask 255.255.255.0
gateway 192.168.0.254
dns-nameservers 192.168.1.1 192.168.1.2
up route add -net 172.16.5.0/24 gw 192.168.10.100 eth1
down route del-net 172.24.0.0/24
```

## 更新相关
```r
# 更新软件列表
apt-get update
# 更新异常索引文件
apt-get update --fix-missing
# 更新软件
apt-get upgrade
# 更新系统版本
apt-get dist-upgrade
```


2016/6/2  
