# visualstudio---asm

visualstudio也可以用来直接写汇编代码。  

安装AsmDude扩展提供汇编代码高亮功能。  

相加例子：  
```asm
; AddTwo.asm - adds two 32-bit integers.
; Chapter 3 example

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.code
main proc
	mov	eax,5				
	add	eax,6				

	invoke ExitProcess,0
main endp
end main
```

参考链接：http://www.asmirvine.com/gettingStartedVS2019/index.htm  


2020/11/25  
