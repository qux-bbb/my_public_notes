# ubuntu20服务器---设置静态ip

在 `/etc/netplan` 下找到类似这样的yaml文件：  
```r
/etc/netplan/99_config.yaml
```

编辑内容类似这样：  
```r
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 10.10.10.2/24
      gateway4: 10.10.10.1
      nameservers:
          addresses: [8.8.8.8]
```

使修改生效：  
```r
sudo netplan apply
```


原链接: https://ubuntu.com/server/docs/network-configuration  


2022/4/13  
