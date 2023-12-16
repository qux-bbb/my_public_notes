# gdb---简单脚本示例

gdb脚本可批量执行命令，自动化控制调试过程  

新建文件a.gdb(后缀不重要), 内容如下:  
```r
# This is a comment.
file a.out
start
break *0x55555555502E
break *0x555555555A5A
break *0x555555555660
break *0x555555555714
continue
delete *
```

使用方法:  
```r
gdb -x a.gdb
```

相关链接: https://sourceware.org/gdb/current/onlinedocs/gdb.html/File-Options.html#File-Options  


2019/11/1  
