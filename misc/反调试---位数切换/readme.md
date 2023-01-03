# 反调试---位数切换

```r
在x64系统下的进程是有32位和64位两种工作模式，这两种工作模式的区别在于CS寄存器。32位模式时，CS = 0x23；64位模式时，CS = 0x33。;

这两种工作模式是可以进行切换的，一般会通过retf指令，一条retf指令等效于以下2条汇编指令

pop ip
pop cs

如果此时栈中有0x33，则会将0x33弹出到CS寄存器中，实现32位程序切换到64位代码的过程。所以retf是识别32位程序调用64位代码的重要标志。
```
原链接：https://www.sohu.com/a/297638567_750628  

```cpp
// 这里反调试相关的代码有个 32位 -> 64位 -> 32位 的过程
fn()
{
    __asm
    {
        ; 32bit code
        ; ...
     
        ; 32 -> 64
        push    33h
        call    $+5
        add     dword ptr [esp], 5
        retf
 
        ; 64bit code
        ; ...
         
        ; 64 -> 32
        call    $+5
        mov     dword ptr [rsp+4], 23h
        add     dword ptr [rsp], 0Dh
        retf
         
        ; 32bit code
        ; ...
     
    }
}
```
自己还没有实现成功  

原链接：https://bbs.pediy.com/thread-263644.htm  


2020/11/24  
