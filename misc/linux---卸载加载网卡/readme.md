# linux---卸载加载网卡

查看所有网卡：  
```
ifconfig -a
```

ifconfig 不会根据配置修改ip  
```
ifconfig vboxnet0 down
ifconfig vboxnet0 up
```

ifup可以根据配置修改ip  
```
ifdown vboxnet0
ifup vboxnet0
```
