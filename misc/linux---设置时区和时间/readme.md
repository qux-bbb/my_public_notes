# linux---设置时区和时间

设置时区：  
```r
timedatectl list-timezones
sudo timedatectl set-timezone Asia/Shanghai
```

设置时间：  
```r
sudo timedatectl set-ntp false
sudo timedatectl set-time '2015-11-23 08:10:40'
```

参考链接：  
1. https://linuxize.com/post/how-to-set-or-change-timezone-on-centos-7/
2. https://askubuntu.com/questions/683067/how-to-stop-automatic-time-update-via-terminal
3. https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/


2022/9/19  
