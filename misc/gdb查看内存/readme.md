# gdb查看内存

x, Examine memory, gdb查看内存的命令。  

官方文档: https://sourceware.org/gdb/current/onlinedocs/gdb.html/Memory.html#Memory  

gdb里 `help x` 结果：  
```r
Examine memory: x/FMT ADDRESS.
ADDRESS is an expression for the memory address to examine.
FMT is a repeat count followed by a format letter and a size letter.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char), s(string)
  and z(hex, zero padded on the left).
Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).
The specified number of objects of the specified size are printed
according to the format.  If a negative number is specified, memory is
examined backward from the address.

Defaults for format and size letters are those previously used.
Default count is 1.  Default address is following last thing printed
with this command or "print".
```

一些示例：  
```r
# 查看0x400c90到向后0x400c90+24的内容  
x/24 0x400c90

# 显示0x400c90到0x400c90+24的内容，显示的格式为整数d，这个命令常用于检查输出数组的内容  
x/24d 0x400c90

# 显示3组数据，hex形式，每组为一个word(4个字节)
x/3xw 0x400c90
```

gdb本身不提供hexdump功能，可以安装pwndbg插件使用hexdump功能。  


参考链接：https://www.cnblogs.com/adamwong/p/10538019.html  


2020/12/1  
