# linux---find

find命令可以根据各种条件搜索文件。  

命令举例：  
```r
# 默认情况下，递归列出当前目录下的所有目录、文件
find
# 搜索根目录下所有文件名包含"hello"的文件
find /* -name *hello*
# 搜索根目录下所有文件名包含"hello"的文件，不区分大小写
find /* -iname *hello*
# 找到最近7天修改的文件
find /* -type f -daystart -mtime -7 2>/dev/null
```


2016/4/23  
