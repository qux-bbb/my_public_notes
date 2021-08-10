# 占用端口相应信息
查看占用端口进程相应的进程id和程序名称  

## linux
用root执行可以看到比较详细的内容  
```bash
# 法1
lsof -i:端口号

# 法2
netstat -tunlp | grep 端口号
```

netstat选项解释  
```
  <Socket>={-t|--tcp} {-u|--udp}
  -n, --numeric            don't resolve names
  -l, --listening          display listening server sockets
  -p, --programs           display PID/Program name for sockets
```


## windows
管理员权限执行

如果有grep命令，就这样：  
```cmd
netstat -abno | grep 端口号 -A 2
```
如果没有grep命令：  
```cmd
netstat -abno > netstat_result.txt
```
然后在netstat_result.txt里搜端口号，之所以不用findstr，是因为程序名在下一行  


netstat选项解释
```
  -a            显示所有连接和侦听端口。
  -b            显示在创建每个连接或侦听端口时涉及的
                可执行文件。在某些情况下，已知可执行文件托管
                多个独立的组件，此时会
                显示创建连接或侦听端口时
                涉及的组件序列。在此情况下，可执行文件的
                名称位于底部 [] 中，它调用的组件位于顶部，
                直至达到 TCP/IP。注意，此选项
                可能很耗时，并且可能因为你没有足够的
                权限而失败。
  -n            以数字形式显示地址和端口号。
  -o            显示拥有的与每个连接关联的进程 ID。
```

grep选项解释  
```
  -A, --after-context=NUM   print NUM lines of trailing context
```
