# 搭建域名服务器

keywords: 自建dns服务器  

服务器版本ubuntu22，使用软件bind9  

## 安装
```r
sudo apt install bind9 bind9utils bind9-doc
```

## 配置
/etc/bind/named.conf.local 添加如下内容：  
```r
zone "example.com"      { type master; file "/etc/bind/db.example.com"; };
```

`sudo cp /etc/bind/db.local /etc/bind/db.example.com`  
修改 /etc/bind/db.example.com 内容如下：  
```r
;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     ns.example.com. root.ns.example.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@               IN      NS      ns.example.com.
example.com.    IN      A       192.168.1.1
ns              IN      A       192.168.1.10

;also list other computers
box             IN      A       192.168.1.21
```
表示：  
```r
example.com -> 192.168.1.1
ns.example.com -> 192.168.1.10
box.example.com -> 192.168.1.21
```

## 生效
重启服务生效：  
```r
sudo systemctl restart bind9
```

## 参考链接
1. https://help.ubuntu.com/community/BIND9ServerHowto
2. https://www.cnblogs.com/doherasyang/p/14464999.html
3. https://www.isc.org/bind/
4. https://blog.csdn.net/qq_19655405/article/details/117125744


---
2022/7/20  
