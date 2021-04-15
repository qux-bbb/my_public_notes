# linux---cron
linux用于实现定时任务，精确级最小为分钟，适用于24小时运行的机器，关机则不能按预期执行，大概和windows的 `任务计划` 类似  

cron，词源：chronological， 按时间顺序的  
是linux的一个守护进程，会解析指定文件的cron指令并按时执行  


## crontab和配置文件
crontab，用于编辑管理包含cron指令的文件  
```bash
# 创建并编辑
crontab -e
# 列出当前用户的cron配置
crontab -l
# 删除当前用户的cron配置
crontab -r
```

`crontab -e` 的初始内容  
```conf
# Edit this file to introduce tasks to be run by cron.                                                                                                                      
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
```


在线生成 cron 设置: https://crontab.guru/  


用户创建的cron文件都在这个目录下，以用户名作为文件名  
`/var/spool/cron/crontabs`  

系统默认的cron文件为: `/etc/crontab`, 默认内容为：  
```conf
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

```


## 举例
最简单而且无聊的例子  
```conf
# 每分钟将当前时间写入date.txt中
* * * * * date > /tmp/date.txt
```

另一个时间设定  
```conf
# 每周二三四五六 早上八点
0 8 * * 2,3,4,5,6 <the command>
```

重启执行一次(实际可以理解为开机自启动)  
```conf
@reboot <the command>
```


## 其它
看这篇文章说还有图形界面的  
https://www.xmodulo.com/add-cron-job-linux.html  
gnome-schedule 和 kcron 都没装上，以后试一下  


参考：https://www.cnblogs.com/zhoul/p/9931664.html  
