# Rizin相关

Rizin是一个自由开源的逆向工程框架，从radare2分叉而来，追求稳定和易用。  
Cutter是基于Rizin的图形化逆向工程框架，开箱即用。  

官网: https://rizin.re/  
官方文档: https://book.rizin.re/  

记一些常用命令：  
```r
rizin <filepath>    正常打开文件
rizin -d <filepath> 调试文件

?               查看命令使用方法

s [address]     seek，输出当前地址或切换到指定地址

ps              print string
px [size]       print hexdump, 可指定输出长度，需要seek到指定地址使用
pr [size]       print raw bytes, 可指定输出长度，需要seek到指定地址使用
pdf             print disassembled function, 需要seek到函数头地址再使用该命令

aa              Analyze all flags starting with sym. and entry
aaa             Analyze all calls, references, emulation and applies signatures
aaaa            Experimental analysis

dbl             debug breakpoint list, 列出所有断点
db              debug breakpoint, 在当前地址下断点，不能指定其它地址，要配合seek使用
dcs             debug continue until syscall, 继续调试直到遇到系统调用，可以比较方便地看到系统调用记录

q               quit
```

命令举例：  
```r
# 保存0x100字节到文件
pr 0x100 > the_key_data
# 保存0x00006c10地址处的32字节到文件 https://github.com/rizinorg/rizin/issues/2744
pr 32 @ 0x00006c10 > /tmp/bytes_here
```


2022/6/26  
