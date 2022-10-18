# 查看互斥量

keywords: mutex  

SysinternalsSuite的几个工具可以用来查看互斥量。  

可以用Process Explorer查看一个进程的互斥量，显示Lower Pane即可，Type是Mutant的就是互斥量。  

可以用WinObj查看所有互斥量，分布在不同位置，如: \Sessions\6\BaseNamedObjects\SSO_APP_EXIST_MUTEX_ID_1  

可以用handle在命令行过滤出互斥量(管理员权限执行可显示更多):  
```r
# 列出所有互斥量
# -a         Dump all handle information.
# /C:string  Uses specified string as a literal search string. 第2个/C会排除掉指定的字符串
#    这里findstr会过滤出包含"Mutant"但不包含"pid:"的行
handle -a | findstr /C:Mutant /C:pid:

# 指定进程，列出互斥量
# -p         Dump handles belonging to process (partial name accepted). 既可以是进程号，也可以是程序名
handle -a -p qq.exe | findstr /C:Mutant /C:pid:
```


参考链接: https://stackoverflow.com/questions/1389868/get-a-list-of-mutex  


2022/10/18  
