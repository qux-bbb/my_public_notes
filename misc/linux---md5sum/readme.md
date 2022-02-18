# linux---md5sum

md5sum，计算文件的md5  

计算一个文件的md5：  
```r
md5sum path/to/file
```

计算文件的md5，使用结果校验：  
```r
# 计算并将结果重定向
md5sum path/to/file > file.md5
# 使用file.md5校验
md5sum -c file.md5
```

参考: tldr  


2022/2/18  
