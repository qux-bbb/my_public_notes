# linux---自启动方法
简单记一下已经实践过的linux程序自启动方法。  

## cron
cron一般用来设置周期性执行任务，把时间指定为 `@reboot` 即可实现开机自启动  

## gnome-session-properties
如果是gnome环境，可以找到这个程序 `gnome-session-properties`, 图形化的界面，指定要执行的命令即可，很方便  

对应配置文件目录: `~/.config/autostart/`  


参考链接: https://linuxconfig.org/how-to-autostart-applications-on-ubuntu-20-04-focal-fossa-linux  


2021/4/11  
