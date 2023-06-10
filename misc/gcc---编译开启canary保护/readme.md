# gcc---编译开启canary保护

使用这样的编译方式可以开启canary保护  
`gcc -o hello -fstack-protector-all hello.c`  

canary在一个程序里只有一个值，fs:28h处取得，每次运行都会重新生成，对于64位程序，长度为64位，可以理解成压入返回地址和rbp后就会压入canary值(实际上是压入rbp后将rsp的值减小然后将参数和canary的值填入)  

该段代码为main函数刚开始的栈操作，将参数放入栈中，设置canary  
```asm
.text:0000000000400794 push    rbp
.text:0000000000400795 mov     rbp, rsp
.text:0000000000400798 sub     rsp, 40h
.text:000000000040079C mov     [rbp+var_34], edi
.text:000000000040079F mov     [rbp+var_40], rsi
.text:00000000004007A3 mov     rax, fs:28h
.text:00000000004007AC mov     [rbp+var_8], rax
```
该段代码为main函数快结束时对canary的检查  
```asm
.text:0000000000400AA6 mov     rdx, [rbp-8]
.text:0000000000400AAA xor     rdx, fs:28h
.text:0000000000400AB3 jz      short locret_400ABA
.text:0000000000400AB5 call    sub_400590
.text:0000000000400ABA
.text:0000000000400ABA locret_400ABA:                          ; CODE XREF: .text:0000000000400AB3↑j
.text:0000000000400ABA leave
.text:0000000000400ABB retn
```


2018/10/23  
