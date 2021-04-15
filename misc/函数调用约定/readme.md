# 函数调用约定
主要根据两个方面分：  
1. 参数怎么传（寄存器，栈，或者两者结合）
2. 由谁负责处理栈

以下是具体的分类。  

## cdecl
C Declaration（声明）  
主要在C语言中使用的方式，调用者负责处理栈  
好处：向被调用函数传递长度可变的参数  


## stdcall
常用于Win32 API，由被调用者清理栈  
好处：代码尺寸小，兼容性更好  


## fastcall
前两个参数使用寄存器传递（ECX，EDX）  
好处：由于使用寄存器，所以较快，但是如果ECX、EDX中有重要数据，需要备份，增加了额外的系统开销  


## 补充
还有别的调用方法  
**thiscall**  
仅仅应用于"C++"成员函数。this指针存放于CX寄存器，参数从右到左压。thiscall不是关键词，因此不能被程序员指定  
**nakecall**  
一个很少见的调用约定，一般程序设计者建议不要使用。编译器不会给这种函数增加初始化和清理代码，更特殊的是，不能用return返回返回值，只能用插入汇编返回结果。  
**pascal**  
参数从左向右压栈，被调用者负责清理栈(&&&&&&& 这个不知道是什么东西)  
**delphi**  
将前三个参数依次放入eax,edx,ecx，其他参数压栈，返回值是eax  

补充参考的链接：  
https://www.cnblogs.com/kwinwei/p/11527081.html  
https://www.cnblogs.com/john-h/p/6276828.html  
https://www.cnblogs.com/wucg/p/4260147.html  
