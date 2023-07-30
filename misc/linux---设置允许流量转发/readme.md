# linux---设置允许流量转发

临时生效：  
```r
# 方法1(必须使用root账户)
echo 1 > /proc/sys/net/ipv4/ip_forward
# 方法1变种(有sudo权限即可)
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
# 方法2
sudo sysctl -w net.ipv4.ip_forward=1
```
方法1和方法2效果一样  

永久生效：  
修改 `/etc/sysctl.conf` 文件，将 `net.ipv4.ip_forward=1` 注释去掉，重启机器或执行如下命令生效：  
```r
sudo sysctl -p
```

允许流量转发之后，可以通过iptables设置具体的转发规则，比如：  
```r
sudo iptables -t nat -A POSTROUTING -o eth0 -s 192.168.56.0/24 -j MASQUERADE
```
表示将来源为192.168.56.0/24的流量通过eth0网卡发送  


2019/2/26  
