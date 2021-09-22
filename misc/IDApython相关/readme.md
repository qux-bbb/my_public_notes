# IDApython相关

按字母顺序排列的api:  
https://www.hex-rays.com/products/ida/support/idadoc/162.shtml  

idapython文档:  
https://www.hex-rays.com/wp-content/static/products/ida/support/idapython_docs/  

github地址:  
https://github.com/idapython  

一些技巧：  
1. 尽量用python风格的函数，比如: `get_byte` 函数
2. 在写脚本时，可以把脚本放在 `idaapi.py` 目录下，写起来更方便，写完可以移出来用


一个博客的简单总结:  
```
IDAPython 由三个分离的模块组成,
他们分别是 idc,idautils 和 idaapi。

idc(注意大小写,不是 IDA 中的 IDC)是一个封装了 IDA 的 IDC 的兼容性模块,
idautils 是 IDA 的高级实用功能模块,
idaapi 允许了我们访问更加底层的数据。
```
注: IDC 语言是一种类 C 语言  
https://www.cnblogs.com/whitehawk/p/10803489.html  


已经用过的函数:  
```c
// 修改内存
PatchByte(0x6cd000, 0x12)
PatchWord(0x6cd000, 0x1234)
PatchDword(0x6cd000, 0x12345678)
PatchQword(0x6cd000, 0x1234567812345678)

// 修改寄存器
SetRegValue(0x12, 'rax')

// 获取寄存器值
GetRegValue('RIP')

// 当前光标地址, 不是rip寄存器的值
here()

// 反汇编指定地址的一行数据
GetDisasm(0x478540)
```


步过自动处理信息:  
```python
# coding:utf8

from idaapi import *

while True:
    GetDebuggerEvent(WFNE_SUSP, -1) 
    rip = GetRegValue('RIP')
    print(GetDisasm(rip))
    # 步过
    step_over()
```
如果只是想看每一步执行的指令和相关寄存器变化，直接用IDA的指令追踪功能:  
Debugger->Tracing->Instruction tracing  


一个修改数据的脚本示例：  
```python
# coding:utf8

from idaapi import get_screen_ea, get_byte, patch_byte

sea = get_screen_ea()

for i in range(0x00,0x50):
    b = get_byte(sea+i)
    decoded_byte = b ^ 0x55
    patch_byte(sea+i,decoded_byte)
```


一个人总结的常用功能：  
https://github.com/inforion/idapython-cheatsheet  


2020/4/1  
