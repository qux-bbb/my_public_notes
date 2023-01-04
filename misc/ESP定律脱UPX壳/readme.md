# ESP定律脱UPX壳

Esp定律  
在编写加壳软件时，必须遵守栈平衡原理。  
将整个外壳作为一个函数或子程序来理解，执行前后遵守栈平衡原理，当其跳转到OEP时，esp的值不会变，这就是esp定律。可利用这一特性找到OEP。  

```r
用OD载入
0040E8C0 >  60              pushad 按F8下
0040E8C1    BE 15B04000     mov     esi, 0040B015 到这里你会看到右边数据寄存器窗口esp的值是跟第一个不一样并且是发光的状态。。我们右键那个值去按到“数据窗口跟随。。”
会看到一大堆难懂的数据。。。（本人觉得堆栈区在破解。。相当有作用）
你会看到
0012FFA4  38 07 91 7C FF FF FF FF F0 FF 12 00 C4 FF 12 00  
在第一行的前4个数值上右键－》断点－》硬件访问－》－》word
按F9直接运行到
0040EA0F  - E9 B826FFFF     jmp     004010CC //直接按F8跳。。。
0040EA14    0000            add     byte ptr [eax], al
0040EA16    0000            add     byte ptr [eax], al
0040EA18    0000            add     byte ptr [eax], al
跳到OEP。。
004010CC    55              push    ebp
004010CD    8BEC            mov     ebp, esp
004010CF    83EC 44         sub     esp, 44
004010D2    56              push    esi
004010D3    FF15 E4634000   call    dword ptr [4063E4]               ; kernel32.GetCommandLineA
又可以脱壳啦。。并且比第一种有效率。。
记得破解后记得清除断点。。不然会出错ERROR － －ll
```

 

原链接: http://www.52pojie.cn/thread-16381-1-1.html  


2016/5/21  
