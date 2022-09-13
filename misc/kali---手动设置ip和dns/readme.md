# kali---手动设置ip和dns

keywords: kali linux 设置ip 修改ip 设置dns 修改dns 直接生效  

## ip
即时生效  
```r
ifconfig eth0 192.16.1.23 netmask 255.255.255.0

route add default gw 192.168.1.1
```

重启生效  
文件位置: /etc/network/interfaces  
内容：  
```r
auto eth0
iface eth0 inet static      // 配置eth0使用默认的静态地址
address 192.168.77.133      // 设置eth0的ip地址
netmask 255.255.255.0       // 设置eth0的子网掩码
gateway 192.168.77.254      // 配置当前主机的默认网关
```
可使用下面的命令生效，无需重启：  
```r
ifconfig flush dev eth0
ifconfig eth0 up
```

## DNS
即时生效（不建议这么修改，可能被覆盖）  
文件位置：/etc/resolv.conf  
内容：  
```r
domain 
nameserver 10.10.10.10
nameserver 102.54.16.2
```

重新启动服务生效  
文件位置: /etc/network/interfaces  
内容：  
```r
dns-nameservers  8.8.8.8 114.114.114.114
```
一行可写多个地址  
重启服务：  
```r
sudo service networking restart
```


---
2017/9/2  
