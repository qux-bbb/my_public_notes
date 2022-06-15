# 输出重定向-文件描述符-数字

keywords: 标准输入 标准输出 标准错误 stdin stdout stderr 0123  

Bourne shell 使用0、1、2作为输出重定向的文件描述符。  
```r
0 : stdin(standard input)
1 : stdout(standard output)
2 : stderr(standard error)
```

举例：  
ls 一个不存在的文件夹: `ls hello 2>errfile`  
即可将错误信息输出到errfile  


2018/4/6  
