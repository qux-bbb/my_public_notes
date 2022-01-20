# bss段相关实验

名称来源 Block Started by Symbol  
属于静态内存分配，程序运行时的地址不变，用来存放程序中未初始化的全局变量  

看这段代码：  
```c
#include <stdio.h>

int theValue;

int main() {
	theValue = 1;
	printf("theValue: %d\n", theValue);
	return 0;
}
```

visual studio不产生bss段，theValue放在.data段中  
ubuntu下使用`gcc -o test test.c`生成程序，theValue放在.bss段中  
随便一个delphi exe程序都会生成BSS段  


20201206  
