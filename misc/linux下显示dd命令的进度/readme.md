# linux下显示dd命令的进度

```r
dd if=/dev/zero of=/tmp/zero.img bs=10M count=100000
```
想要查看上面的dd命令的执行进度，可以使用下面几种方法每5秒输出dd的进度：  
```r
# 方法一
watch -n 5 pkill -USR1 ^dd$
# 方法二
watch -n 5 killall -USR1 dd
# 方法三
while killall -USR1 dd; do sleep 5; done
# 方法四
while (ps auxww |grep " dd " |grep -v grep |awk '{print $2}' |while read pid; do kill -USR1 $pid; done) ; do sleep 5; done
```

上述四种方法中使用三个命令：pkill、killall、kill向dd命令发送SIGUSR1信息，dd命令进程接收到信号之后就打印出自己当前的进度。  

原链接: http://blog.csdn.net/xyz846/article/details/7367962  


2016/11/4  
