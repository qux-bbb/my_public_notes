# linux---ip命令

```r
# 查看网卡ip地址，不用"-brief"显示太多，全写和简写
ip -brief address
ip -br a

# 查看网卡mac地址
ip -brief link
ip -br l

# 查看指定网卡的具体信息
ip addr show dev ens160

# 清空某个网卡的ip地址
ip addr flush dev eth0

# 卸载加载网卡(! up时不会自动加载配置)
ip link set eth0 down
ip link set eth0 up

# 查看路由
ip route
ip r
```


2022/5/16  
