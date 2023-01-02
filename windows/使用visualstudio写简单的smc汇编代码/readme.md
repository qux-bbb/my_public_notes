# 使用visualstudio写简单的smc汇编代码

## 简单介绍
Self-Modifying Code，自修改代码  

可以提高静态分析的难度，这里简单写一个示例  


## 生成基本的exe
Visual Studio创建一个空项目，在"源文件"文件夹里新建一个 test.c，粘贴内容如下：  
```c
// InlineAssembler_Calling_C_Functions_in_Inline_Assembly.cpp
// processor: x86
#include <stdio.h>

char format[] = "%s %s\n";
char hello[] = "Hello";
char world[] = "World";

int main()
{
    __asm
    {
        mov eax, start
        mov ecx, end
        sub ecx, eax
        the_loop:
            mov ebx, [eax]
            xor ebx, 0x23
            mov [eax], ebx
            inc eax
            loop the_loop
        start:
            pushad
            mov  eax, offset world
            push eax
            mov  eax, offset hello
            push eax
            mov  eax, offset format
            push eax
            call printf
            //clean up the stack so that main can exit cleanly
            //use the unused register ebx to do the cleanup
            pop  ebx
            pop  ebx
            pop  ebx
            popad
        end: 
    }
    return 0;
}
```

代码比较简单，大概说一下  
the_loop上面的3行汇编代码是获取要异或的区域，开始地址存在eax，长度存在ecx；  
the_loop到start是异或的逻辑，这里用0x23异或；  
start到end是输出"Hello World"的逻辑  

然后编译x86版本的exe，注意这个时候的exe是不能正常输出"Hello World"的，因为还没有对start到end的部分做异或处理，另外还有两个默认的PE机制问题，后面再说。  


## 使用IDA对部分代码做异或
IDA打开上一步生成的exe，找到我们要处理的部分，如下：  
```
.text:00411894 60                                pusha
.text:00411895 B8 10 A0 41 00                    mov     eax, offset aWorld ; "world"
.text:0041189A 50                                push    eax
.text:0041189B B8 08 A0 41 00                    mov     eax, offset aHello ; "Hello"
.text:004118A0 50                                push    eax
.text:004118A1 B8 00 A0 41 00                    mov     eax, offset aSS ; "%s %s\n"
.text:004118A6 50                                push    eax
.text:004118A7 E8 21 F8 FF FF                    call    sub_4110CD
.text:004118AC 5B                                pop     ebx
.text:004118AD 5B                                pop     ebx
.text:004118AE 5B                                pop     ebx
.text:004118AF 61                                popa
```
记下开始地址和结束地址，这里是0x00411894和0x004118AF，  
然后在IDA里，File -> Script file...，运行如下python脚本：  
```python
# coding:utf8

from ida_bytes import get_byte, patch_byte

def range_xor(start_addr, end_addr, xor_num):
    for the_addr in range(start_addr, end_addr+1):
        the_byte = get_byte(the_addr)
        patch_byte(the_addr, the_byte ^ xor_num)

range_xor(0x00411894, 0x004118AF, 0x23)
```
之后 Edit -> Patch program -> Apply patches to input file...，这样保存之后，我们就得到异或处理之后的exe了，但现在还是不能正常运行。  


## 处理PE机制造成的问题
上面提到PE的两个机制，导致程序还不能正常运行。  
一个是代码段默认不可写，另一个是动态基址，我们使用xpeviewer来修改相应的位置。  

禁用动态基址：  
先把右上角的"只读"取消勾选  
IMAGE_NT_HEADERS -> IMAGE_OPTIONAL_HEADER -> DllCharacteristics 取消勾选"DYNAMIC_BASE"  

设置代码段可写：  
区块 -> .text -> 右键编辑 -> 取消右上角的"只读"勾选，Characteristics 点击勾选 "MEM_WRITE"  

这样之后，就能实现一个最简单的smc例子了。  


## 最后
这个过程只是自己的想法，如果有不合适的地方，请各位大神指正。  


---
2020/11/25  
