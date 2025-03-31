# linux---ip命令

```r
# 查看网卡ip地址，不用"-brief"显示太多，全写和简写
sudo ip -brief address
sudo ip -br a

# 查看网卡mac地址
sudo ip -brief link
sudo ip -br l

# 查看指定网卡的具体信息
sudo ip address show dev ens160

# 清空某个网卡的ip地址
sudo ip address flush dev eth0

# 添加指定的ipv4地址
sudo ip address add 192.168.1.100/24 dev eth0

# 删除指定的ipv4地址
sudo ip address del 192.168.1.100/24 dev eth0

# 卸载加载网卡(! up时不会自动加载配置)
sudo ip link set eth0 down
sudo ip link set eth0 up

# 查看路由
sudo ip route
sudo ip r
```


2022/5/16  
