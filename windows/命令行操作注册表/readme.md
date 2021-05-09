# 命令行操作注册表

查询
```
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\open\command
```

添加或修改  
```
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\open\command /d "\"%1\" %*" /f
```
`/v` 可以执行键的名字，没有这个参数的话，就是`(默认)`或`(Default)`  


20201208  
