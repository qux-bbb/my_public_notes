# linux---grep

grep用来搜索文件内容。  

## 通常简单用法
grep可以接管道传送的内容搜索：  
`ls -l | grep "hello"`  

也可以直接从文件查找：  
`grep "hello" a.txt`  

当前目录递归查找：  
`grep "hello" . -r`  

指定每个匹配的上下文一共输出5行:  
`grep "hello" -C 5 a.txt`  

## 搜索换行
`grep -zoP 'fingerprint": \[\n' hello.json`  

用到的选项:  
```sh
-z, --null-data           a data line ends in 0 byte, not newline
-o, --only-matching       show only the part of a line matching PATTERN
-P, --perl-regexp         PATTERN is a Perl regular expression
```


---
2019/11/8  
