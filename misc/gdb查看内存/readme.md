# gdb查看内存

x, Examine memory, gdb查看内存的命令  

首先使用`gdb [YourFileName].c`进入gdb界面  

使用`examine`命令，字母缩写为`x`查看内存地址的值。`x`命令语法  
```r
x/[number][format] <addr>
```
其中number,format和u都是可选参数, addr为查看变量的内存地址  

number: 一个正整数，表示从当前地址向后显示几个地址的内容。如  
```r
x/24 0x400c90
```
表示查看0x400c90到向后0x400c90+24的内容  

format：显示的格式不是查看的格式。和c语言中的格式缩写一样，如  
```r
d:整数integer
s:字符串string
c:字符char
u:无符号整数 unsigned integer
o:八进制格式显示变量
x:十六进制格式
f: 浮点数格式float
......
```
```r
x/24d 0x400c90
```
显示0x400c90到0x400c90+24的内容，显示的格式为整数d，这个命令常用于检查输出数组的内容  


原链接：https://www.cnblogs.com/adamwong/p/10538019.html  


2020/12/1  
