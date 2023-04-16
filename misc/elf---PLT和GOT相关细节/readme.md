# elf---PLT和GOT相关细节

## 简介
PLT, Procedure Linkage Table, 过程链接表  
GOT, Global Offset Table, 全局偏移表  

简略来说就是从PLT去GOT找api真实地址。  

有一个延迟绑定的机制，默认开启，和这2个表有关。延迟绑定大概就是说我先不绑定提到的api，等你用的时候我再绑定你用的api，这样来避免启动时间浪费。有的人可能就想，我就不延迟绑定，我不在乎启动时间，我就要直接全部绑定好，用的时候不就快了吗，也可以，因为延迟绑定是可以关闭的。  

观察elf，发现有4个相关的节，分别是：  
```
.plt
.plt.got
.got
.got.plt
```
下面举个例子，看一下节的关系，代码如下（后面都用这个例子）：  
```c
// test.c x64
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```


## 默认编译
朴实无华的helloworld，先默认编译：  
```
gcc -o test test.c
```
然后用IDA看一下printf是怎么找到的（这里优化成了puts）：  
```
.text:0000000000400526 main            proc near               ; DATA XREF: _start+1D↑o
.text:0000000000400526 ; __unwind {
.text:0000000000400526                 push    rbp
.text:0000000000400527                 mov     rbp, rsp
.text:000000000040052A                 mov     edi, offset s   ; "Hello World!"
.text:000000000040052F                 call    _puts
.text:0000000000400534                 mov     eax, 0
.text:0000000000400539                 pop     rbp
.text:000000000040053A                 retn
.text:000000000040053A ; } // starts at 400526
.text:000000000040053A main            endp
```
点一下 `_puts`，来到了 .plt：  
```
.plt:0000000000400400 ; int puts(const char *s)
.plt:0000000000400400 _puts           proc near               ; CODE XREF: main+9↓p
.plt:0000000000400400                 jmp     cs:off_601018
.plt:0000000000400400 _puts           endp
```
跟过去，到了 .got.plt：  
```
.got.plt:0000000000601018 off_601018      dq offset puts          ; DATA XREF: _puts↑r
.got.plt:0000000000601020 off_601020      dq offset __libc_start_main
```


## 关闭延迟绑定的编译
加 `-z now` 选项，可以关闭延迟绑定，编译命令如下：  
```
gcc -o pre_test -z now test.c
```
然后用IDA跟踪一下：  
```
.text:0000000000400516 main            proc near               ; DATA XREF: _start+1D↑o
.text:0000000000400516 ; __unwind {
.text:0000000000400516                 push    rbp
.text:0000000000400517                 mov     rbp, rsp
.text:000000000040051A                 mov     edi, offset s   ; "Hello World!"
.text:000000000040051F                 call    puts
.text:0000000000400524                 mov     eax, 0
.text:0000000000400529                 pop     rbp
.text:000000000040052A                 retn
.text:000000000040052A ; } // starts at 400516
.text:000000000040052A main            endp
```
点一下 `puts`，来到了 .plt.got：  
```
.plt.got:0000000000400400 ; int puts(const char *s)
.plt.got:0000000000400400 puts            proc near               ; CODE XREF: main+9↓p
.plt.got:0000000000400400                 jmp     cs:puts_ptr
.plt.got:0000000000400400 puts            endp
```
跟过去，到了 .got：  
```
.got:0000000000600FE8 puts_ptr        dq offset __imp_puts    ; DATA XREF: puts↑r
.got:0000000000600FF0 __libc_start_main_ptr dq offset __imp___libc_start_main
```


## 总结
跟踪下来可以确定：  
如果开启了延迟绑定（默认情况），节跳转是：  
```
.plt -> .got.plt  
```
如果关闭了延迟绑定（-z now），节跳转是：  
```
.plt.got -> .got  
```


感谢atQ4n  


2020/12/1  
