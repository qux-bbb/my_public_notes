# linux---图形界面卡死解决方法

keywords: 卡死 切换终端  

从百度搜的2种方法，都是切到其它终端，然后kill掉相关进程的思路  

切终端的方法：`Ctrl + Alt + F1到F6`试一下  

切成功后，方法1：  
执行命令：`top`，看哪个进程占用资源高，然后 `kill -9 pid`，这个时候再切回去（我的切回去是`Ctrl + Alt + F2`）看看  

如果不行，试试方法2：  
执行命令：`ps -ef | grep tty`，确定卡死的tty进程，也是 `kill -9 pid`  

我是把ubuntu装到了移动硬盘里，开机之后就是黑屏，`Ctrl + Alt + F3`, 然后再切回来 `Ctrl + Alt + F2`, 就能正常显示了  


原链接：https://zhidao.baidu.com/question/373386988762384604.html  


20201215  
