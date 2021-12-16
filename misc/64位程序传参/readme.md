# 64位程序传参

keywords: 函数调用  

## windows
前4个参数：rcx, rdx, r8, r9  
后面的参数用栈传递  

## linux
前6个参数: rdi, rsi, rdx, rcx, r8, r9
后面的参数用栈传递  

rax寄存器保存的是对应调用号  


2020/11/21  
