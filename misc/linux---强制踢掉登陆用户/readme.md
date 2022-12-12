# linux---强制踢掉登陆用户

keywords: linux user 用户 在线 下线 踢出 登出 已登陆  

只有root才能踢用户  

查看当前登陆用户  
```r
w
```

可能结果为  
```r
 19:36:32 up 491 days,  5:23,  6 users,  load average: 3.47, 3.35, 3.37
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
hellowor tty1                      14Feb19 248days  1.95s  1.91s -bash
worldgoo pts/0    11.222.3.114     19:36    0.00s  0.00s  0.00s w
goodmorn pts/4    55.222.111.99    13Mar20 27:37m  0.09s  0.09s -bash
```

踢掉`worldgoo`用户  
```r
pkill -kill -t pts/0
```

tty和pts的区别  
tty就是本地或者串口线开的shell  
pts就是远程连接开的shell  

tty: Teletypewriter  
pts: pseudo terminal slave  


参考链接:  
1. https://blog.csdn.net/chengest/article/details/4360584  
2. https://www.cnblogs.com/hust-yao/p/9742337.html  
3. https://www.question-defense.com/2009/09/11/what-do-pts-and-tty-mean-on-linux-what-is-the-difference-between-the-two-terminal-types  


2020/3/20  
