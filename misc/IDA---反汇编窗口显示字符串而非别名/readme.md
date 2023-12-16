# IDA---反汇编窗口显示字符串而非别名


## 显示别名原因
一些字符串不在只读区段，Hex-Rays反编译器默认只打印常量字符串，变量字符串会以别名显示  


## 选项修改及示例
操作：  
Edit -> Plugins -> Hex-Rays Decompiler -> Options -> Analysis options 1  
取消勾选"Print only constant string literals"  


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


## 修改配置全局且永久生效
相关配置文件: cfg/hexrays.cfg  
相关行：  
```cpp
#define HO_CONST_STRINGS       0x000040
HEXOPTIONS               = 0x831FF
```
HEXOPTIONS由HO_各种选项组合，0x831FF - 0x000040 = 0x831BF  
所以HEXOPTIONS改为 0x831BF 即可  


## 参考链接
https://bbs.kanxue.com/thread-264873.htm  


---
2023/7/14  
