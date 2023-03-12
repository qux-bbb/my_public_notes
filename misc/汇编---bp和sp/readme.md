# 汇编---bp和sp

```r
bp为基址寄存器，一般在函数中用来保存进入函数时的sp的栈顶基址
sp是栈顶指针，它每次指向栈顶。
每次子函数调用时，系统在开始时都会保存这个两个指针并在函数结束时恢复sp和bp的值。像下面这样：
在函数进入时：
push bp  //保存bp指针
mov bp,sp //将sp指针传给bp，此时bp指向sp的基地址。这个时候，如果该函数有参数，则[bp+4]则是该子函数的第一个参数，[bp+6]则是该子函数的第二个参数，以此类推，有多少个参数则[bp+4+2^n]。
.....
.....
函数结束时：
mov sp,bp //将原sp指针传回给sp
pop bp  //恢复原bp的值。
```

简洁版  
```r
bp  base pointer    基址指针，保存进入函数时sp的值
sp  stack pointer   栈指针，栈的偏移地址
ss  stack segment   栈段，栈的起始地址

进入函数时
push bp
mov bp,sp

退出函数时
mov sp,bp
pop bp


地址
栈    由高到低增长
堆    由低到高增长
```


原链接: http://blog.chinaunix.net/uid-391792-id-2410253.html  


2017/3/19  
