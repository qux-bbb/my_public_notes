# linux---杀死进程

```r
# 通过进程id 123
kill -9 123
# 通过进程名
pkill -9 "python"
# 通过命令(进程名或者参数，只要有匹配的就可以), "--full"可简写为"-f"
pkill --full "hello.py"
```


2022/12/12  
