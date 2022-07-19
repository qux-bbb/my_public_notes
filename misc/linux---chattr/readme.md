# linux---chattr

chattr, Change attributes of files or directories. 修改文件或文件夹的属性。  

```r
# i是immutable, 不变的，使文件或目录无法被修改或删除，常用于保护目标
chattr +i path/to/file_or_directory
# 去除不可变保护
chattr -i path/to/file_or_directory
# 使目录及内部所有文件或文件夹不可变
chattr -R +i path/to/directory
```

原链接: tldr  


2022/7/19  
