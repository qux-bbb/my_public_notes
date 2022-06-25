# gdb---dump进程内存

keywords: 保存内存  

全部命令都可以在gdb里运行，dump必须在gdb中进行  

```r
# 查找进程id  
ps -elf | grep my_process

# 查看相应进程的内存映射  
cat /proc/my_process_id/maps

# gdb附加相应进程  
gdb attach my_process_id

# dump想要的内存
# dump memory <dst_path> <start_addr> <end_addr>
dump memory /root/memory.dump 0xc81fff0000 0xc820200000
```

参考链接：  
1. https://blog.csdn.net/caiqiiqi/article/details/72807952
2. https://colin.guru/index.php?title=Dumping_Ram_From_Running_Linux_Processes
3. https://blog.csdn.net/ztguang/article/details/51015758


2019/4/7  
