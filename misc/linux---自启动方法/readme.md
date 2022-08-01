# linux---自启动方法
简单记一下linux程序自启动方法。  

## cron
cron一般用来设置周期性执行任务，把时间指定为 `@reboot` 即可实现开机自启动  
详见: [linux---cron](../linux---cron/readme.md)  

相关配置文件或文件夹：  
```r
# 文件
/etc/crontab

# 文件夹
/var/spool/cron  # centos系
/var/spool/cron/crontabs  # debian系
/etc/cron.d
/etc/cron.daily
/etc/cron.hourly
/etc/cron.monthly
/etc/cron.weekly
```
这是一个检查cron自启动相关文件的脚本: [check_cron.sh](files/check_cron.sh)  


## 自启动服务
服务一般用来做后台长时间运行的任务  
详见：  
[linux---service](../linux---service/readme.md)  
[linux---systemd](../linux---systemd/readme.md)  

相关配置文件：  
`/etc/init.d`  
`/etc/systemd`  

## gnome-session-properties
如果是gnome环境，可以找到这个程序 `gnome-session-properties`, 图形化的界面，指定要执行的命令即可，很方便  

对应配置文件目录: `~/.config/autostart/`  

参考链接: https://linuxconfig.org/how-to-autostart-applications-on-ubuntu-20-04-focal-fossa-linux  

## 不正常的启动方式
1. 持续被攻击
2. 正常命令被替换


---
2021/4/11  
