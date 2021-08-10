# linux---根据进程号确定路径

keywords: 进程号 进程id 绝对路径  

使用top、ps等命令可以看到进程id，相应的文件名，有些文件因为在PATH范围内，所以看不到完整路径  

可以根据进程id去`/proc`路径下查看更详细的信息，这两个比较常用：  
1. `/proc/<process_id>/exe` 是程序的链接文件，`ls -l /proc/<process_id>/exe` 即可看到程序的绝对路径  
2. `/proc/<process_id>/cmdline` 是程序启动时执行的命令  


参考链接: https://www.cnblogs.com/klvchen/p/12071834.html  


2021/8/10  
