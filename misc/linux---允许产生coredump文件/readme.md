# linux---允许产生coredump文件

在linux下调试程序，在程序出错时产生coredump文件，默认是关闭的，如果需要打开，使用以下命令：  
```r
ulimit -c unlimited
```
这样在程序出错后就会生成一个不限制大小的core文件  

gdb加载此core文件包含信息：  
```r
gdb ./test core
```


2018/1/1  
