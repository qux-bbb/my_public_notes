# ctf---checksec

一个脚本，可以用来检测程序是否开启了部分保护  
https://github.com/slimm609/checksec.sh  
输出的信息有以下几行：  
```r
Arch:       i386-32-little      # 架构: 32位程序
RELRO:      Partial RELRO       # RELocation Read-Only 重定向只读
Stack:      No canary found     # 栈: canary是一个用来检测栈是否溢出的标志
NX:         NX disabled         # No eXecute 某些区域 不可执行
PIE:        No PIE (0x8048000)  # Position-Independent Executables 位置独立的可执行域
RWX:        Has RWX segments    # 读写执行段
```
**Arch**  
这个不用多说，就是程序运行在什么平台，位数是多少，数据格式是大端还是小端，本例中为i386平台，32位，小端    

**RELRO**  
重定向只读，本例中为`Partial RELRO`，部分开启，这样就表示GOT(Global Offset Table)是可写的，如果值为`Full RELRO`，GOT就是只读了  

**Stack**  
关于栈的canary保护，canary是一个用来检测栈是否溢出的标志，如果该值被更改，就说明栈上的数据被恶意修改了，在使用gcc编译时可以通过以下选项打开该保护  
`gcc -o hello -fstack-protector-all hello.c`  

**NX**  
某些区域不可执行，一般指的是堆栈/数据段区域，对应windows下的DEP(Data Execute Protect 数据执行保护)，如果该项的值为`NX enabled`，则堆栈，数据段的数据都不能作为指令执行  

**PIE**  
如果该项开启，那代码段在内存中的位置是不固定的  

参考链接：http://yunnigu.dropsec.xyz/2016/10/08/checksec%E5%8F%8A%E5%85%B6%E5%8C%85%E5%90%AB%E7%9A%84%E4%BF%9D%E6%8A%A4%E6%9C%BA%E5%88%B6/  


2020/11/30  
