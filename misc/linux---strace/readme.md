# linux---strace

strace, the linux syscall tracer.  

官网: https://strace.io/  

可以用来查看和修改程序使用的系统调用，可以是进程号、程序。  
strace的操作是由被称为ptrace的内核特性实现的。  

官网一些示例：  
```r
# 附加进程
strace -p 26380

# 执行程序
strace cat /dev/null
```


2022/7/21  
