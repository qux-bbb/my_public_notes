# 输出重定向-文件描述符-数字

keywords: 标准输入 标准输出 标准错误 stdin stdout stderr 0123  

Bourne shell 使用0、1、2作为输出重定向的文件描述符。  
```r
0 : stdin(standard input)
1 : stdout(standard output)
2 : stderr(standard error)
```

`echo morning > greet.txt`  
这里的 `>` 其实是 `1>`, 表示标准输出重定向，`1` 可以省略  

`ls dont_exist 2> errfile`  
dont_exist 不存在，这里的 `2>` 表示标准错误重定向， `2` 不能省略  


参考链接: https://pwn.college/linux-luminarium/piping/  


2018/4/6  
