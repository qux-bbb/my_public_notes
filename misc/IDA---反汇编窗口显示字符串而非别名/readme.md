# IDA---反汇编窗口显示字符串而非别名

操作：  
Edit -> Plugins -> Hex-Rays Decompiler -> Options -> Analysis options 1  
取消勾选"Print only constant string literals"  

原因：  
一些字符串不在只读区段，Hex-Rays反编译器默认只打印常量字符串，变量字符串会以别名显示  

示例：  
```c
#include <stdio.h>

char global_str[] = "hello";

int main() {
	char local_str[] = "world";

	printf("global_str: %s\n", global_str);
	printf("local_str: %s\n", local_str);
	
	return 0;
}
```

字符串所在区段如下：  
```r
.rdata:00417A8C aWorld          db 'world',0            ; DATA XREF: _main+10↑r
...
.data:004198B0 aHello          db 'hello',0            ; DATA XREF: _main+23↑o

```

默认反编译结果：  
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[8]; // [esp+0h] [ebp-Ch] BYREF

  strcpy(v4, "world");
  sub_401040("global_str: %s\n", aHello);
  sub_401040("local_str: %s\n", v4);
  return 0;
}
```

取消勾选"Print only constant string literals"后的反编译结果：  
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[8]; // [esp+0h] [ebp-Ch] BYREF

  strcpy(v4, "world");
  sub_401040("global_str: %s\n", "hello");
  sub_401040("local_str: %s\n", v4);
  return 0;
}
```


参考链接: https://bbs.kanxue.com/thread-264873.htm  


2023/7/14  
