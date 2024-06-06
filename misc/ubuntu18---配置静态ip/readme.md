# ubuntu18---配置静态ip

keywords: 配置ip 设置ip  

ubuntu版本不同，ip配置方式也不太一样，这里介绍ubuntu18的网络配置方式。  

桌面版很简单，找到网络设置，修改为相应的ip，保存就好了。如果没有生效，关掉再连接一下。  

服务器版和以前的修改`/etc/network/interfaces`不同，  
现在要使用一个新的工具`netplan`，配置文件在`/etc/netplan`文件夹下，修改之前可以先做一个备份  
```bash
# 文件名可能不同
sudo cp /etc/netplan/01-network-manager-all.yaml /etc/netplan/01-network-manager-all.yaml.bak
```

然后修改`/etc/netplan/01-network-manager-all.yaml`，这里内容如下：  
```yaml
# Let NetworkManager manage all devices on this system
network:
    version: 2
    renderer: NetworkManager
    ethernets:
        ens33:
            dhcp4: no
            addresses: [192.168.110.121/24]
            gateway4: 192.168.110.1
            nameservers:
                addresses: [8.8.8.8,8.8.4.4]
```

测试并确认：`sudo netplan try`，这样会有一个确认的过程  
如果不需要确认，可以直接运行命令：`sudo netplan apply`  


参考链接: https://ywnz.com/linuxjc/3280.html  

2021/4/26  

