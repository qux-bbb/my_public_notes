# linux---关机

poweroff, shutdown, halt, reboot 都可以用来关机或重启。  
这4个命令都是systemctl的符号链接。  

常用方法：  
```r
# 直接关机
poweroff

# 重启
reboot

# 指定10分钟后关机，不加参数默认1分钟后关机
shutdown +10

# 指定22:00关机，只能是这种格式，不能精确到秒
shutdown 22:00

# 立刻关机，使用"+0"可以达到同样效果
shutdown now

# 指定10分钟后重启
shutdown -r +10

# 取消shutdown操作
shutdown -c
```

参考链接: https://zhuanlan.zhihu.com/p/580590984  


2022/11/6  
