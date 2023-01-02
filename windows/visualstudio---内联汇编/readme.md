# visualstudio---内联汇编

keywords: vs visual studio asm 汇编  

直接操作寄存器  
```c
#include <stdio.h>

int main() {
	printf("Hello World!\n");
	int a = 1, b = 2;
	unsigned c;
	__asm {
		pushad
		mov eax, a
		mov ebx, b
		add eax, ebx
		mov c, eax
		popad
	}
	printf("%d + %d = %d\n", a, b, c);
	return 0;
}
```

汇编调用c函数  
```c
// InlineAssembler_Calling_C_Functions_in_Inline_Assembly.cpp
// processor: x86
#include <stdio.h>

char format[] = "%s %s\n";
char hello[] = "Hello";
char world[] = "world";
int main()
{
    __asm
    {
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
    }
    return 0;
}
```

花指令可以用 `emit` 实现  
```c
__asm
{
    _emit 0xAA  // _emit 在当前位置放一个指定的字节，没有实际作用，干扰分析
}
```


参考链接：  
https://docs.microsoft.com/en-us/cpp/assembler/inline/calling-c-functions-in-inline-assembly?view=msvc-160  


2020/11/24  
