# windows---x64---函数调用约定

64位系统中使用变形的fastcall，最多把函数的4个参数通过寄存器传递，若超过4个，与栈并用  


| 参数 | 整数型 | 实数型 |
| ---- | ------ | ------ |
| 1st  | RCX    | XMM0   |
| 2nd  | RDX    | XMM1   |
| 3rd  | R8     | XMM2   |
| 4th  | R9     | XMM3   |


函数的前4个参数虽然使用寄存器传递，但栈中仍为这4个参数预留了空间(32个字节)  

相关文档: https://docs.microsoft.com/en-us/cpp/build/x64-calling-convention?view=vs-2019  


2019/6/12  
