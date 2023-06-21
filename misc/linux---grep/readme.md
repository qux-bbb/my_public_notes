# linux---grep

grep用来搜索文件内容。  

用法：  
```r
grep [OPTION...] PATTERNS [FILE...]
```

简单示例：  
```bash
# grep可以接管道传送的内容搜索
ls -l | grep "hello"

# 也可以直接从文件查找
grep "hello" a.txt

# 不区分大小写
grep -i "hello" .
# --ignore-case

# 当前目录递归查找
grep -r "hello" .
# --recursive

# 指定每个匹配的上下文一共输出5行
grep -C 5 "hello" a.txt
# --context=NUM

# 搜索换行
grep -zoP 'fingerprint": \[\n' hello.json
# -z, --null-data           a data line ends in 0 byte, not newline
# -o, --only-matching       show only the part of a line matching PATTERN
# -P, --perl-regexp         PATTERN is a Perl regular expression
```


---
2019/11/8  
