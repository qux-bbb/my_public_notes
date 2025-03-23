# linux---strace

keywords: linux监控api  

strace, the linux syscall tracer.  

官网: https://strace.io/  

可以用来查看和修改程序使用的系统调用，可以是进程号、程序。  
strace的操作是由被称为ptrace(process trace)的内核特性实现的。  

官网一些示例：  
```r
# 附加进程
strace -p 26380

# 执行程序
strace cat /dev/null

# 日志保存到文件
strace -o output.txt cat /dev/null

# 日志既输出到终端也保存到文件
strace cat /dev/null 2>&1 | tee output_and_errors.txt

# 跟随子进程
#   -f, --follow-forks
#                  follow forks
#   -ff, --follow-forks --output-separately
#                  follow forks with output into separate files
strace -ff cat /dev/null
```


2022/7/21  
