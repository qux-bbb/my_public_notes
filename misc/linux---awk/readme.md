# linux---awk

awk, 一种处理文件的通用编程语言  
名字来源于3位作者: Al Aho, Peter Weinberger, Brian Kernighan  

github地址: https://github.com/onetrueawk/awk  

一些使用举例：  
```r
# hello.txt以空格分列，输出第5列
awk '{print $5}' hello.txt

# hello.txt以","分列，输出最后一列
awk -F ',' '{print $NF}' hello.txt

# 匹配rob-list中包含"220"的行，并输出符合条件行的第5和第9列
awk '/220/ {print $5 " " $9}' rob-list.txt
```

参考: tldr  


2017/11/16  
