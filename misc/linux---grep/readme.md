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

# 将错误输出如"Permission denied"使用重定向丢弃(2>/dev/null)
grep -r helloworld / 2>/dev/null

# 排除proc文件夹，只能是文件夹名字，不能是文件夹路径
# https://unix.stackexchange.com/questions/589347/grep-exclude-dir-that-contains-some-text-in-the-name
grep -r --exclude-dir "proc" "hello" /
```


---
2019/11/8  
