8086寄存器  
```
通用寄存器：
AX，BX，CX，DX 称作为数据寄存器：
AX (Accumulator)：累加寄存器，也称之为累加器；
BX (Base)：基地址寄存器；
CX (Count)：计数器寄存器；
DX (Data)：数据寄存器；

SP 和 BP 又称作为指针寄存器：
SP (Stack Pointer)：堆栈指针寄存器；
BP (Base Pointer)：基指针寄存器；

SI 和 DI 又称作为变址寄存器：
SI (Source Index)：源变址寄存器；
DI (Destination Index)：目的变址寄存器；


控制寄存器：
IP (Instruction Pointer)：指令指针寄存器；
FLAG：标志寄存器；


段寄存器：
CS (Code Segment)：代码段寄存器；
DS (Data Segment)：数据段寄存器；
SS (Stack Segment)：堆栈段寄存器；
ES (Extra Segment)：附加段寄存器；
```

后来的寄存器：  
```
FS：没有全称，可用于获取当前活动线程的TEB结构（线程结构）
```

寄存器位数：  
```
al = 0x11
ah = 0x22
ax = 0x2211
eax = 0x44332211
rax = 0x8877665544332211
```
0x11 8位  



参考链接：  
1. https://www.cnblogs.com/BoyXiao/archive/2010/11/20/1882716.html
2. https://www.cnblogs.com/milantgh/p/3878771.html