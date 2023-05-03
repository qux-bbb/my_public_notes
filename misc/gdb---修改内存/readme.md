# gdb---修改内存

keywords: 写内存 字符串  

命令格式：  
```r
set {<data_type>} <address> = <value>
```

命令示例：  
```r
# 这里注意必须显式指定字符串长度(加了最后一位空字节)，否则会报错，地址也可以是寄存器，如: $rax
set {char[6]} 0x12345678 = "Hello"
```

参考来源: bing chat  


2023/5/3  
