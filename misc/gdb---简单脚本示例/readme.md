# gdb---简单脚本示例

gdb脚本可批量执行命令，自动化控制调试过程  

新建文件a.gdb, 内容如下:  
```r
file a.out
start
b *0x55555555502E
b *0x555555555A5A
b *0x555555555660
b *0x555555555714
continue
```

使用方法:  
```r
gdb -x a.gdb
```


2019/11/1  
