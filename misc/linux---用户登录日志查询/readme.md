# linux---用户登录日志查询

1. `/var/run/utmp` 记录当前正在登录系统的用户信息，默认由who和w查看当前登录用户的信息，uptime记录系统启动时间；
2. `/var/log/wtmp` 记录当前正在登录和历史登录系统的用户信息，默认由last命令查看；
3. `/var/log/btmp` 记录失败的登录尝试信息，默认由lastb命令查看。

`last` 和 `lastb` 都可以通过 `-f` 选项指定要查看的文件，可以是上述三个文件的任意一个  

`lastlog`  
列出所有或者指定用户最近登录的信息。lastlog引用的是/var/log/lastlog文件中的信息  

`last`  
列出当前和曾经登入系统的用户信息，它默认读取的是/var/log/wtmp文件的信息  

`lastb`  
列出失败尝试的登录信息，和last命令功能完全相同，只不过它默认读取的是/var/log/btmp文件的信息，需要sudo  

`users`  
查看当前登入系统的用户名  

`who`  
查看当前登入系统的用户信息，包括终端类型和登录时间  

`w`  
查看当前登入系统的用户信息及用户当前的进程。用户登录信息来自/var/run/utmp，进程信息来自/proc/  

`utmpdump`  
utmpdump用于转储二进制日志文件到文本格式的文件以便查看，同时也可以修改二进制文件  
```r
# 导出文件信息
utmpdump /var/run/utmp > tmp_output.txt
# <使用文本编辑器修tmp_output.txt>
# 导入到源文件中
utmpdump -r tmp_output.txt > /var/run/utmp
```


原链接: https://cloud.tencent.com/developer/article/1683126  


2022/6/15  
