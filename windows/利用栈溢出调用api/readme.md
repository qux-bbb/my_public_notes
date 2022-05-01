# 利用栈溢出调用api

仅适用32位程序，可能用于免杀、反分析。  

```cpp
#include <Windows.h>
#include <stdio.h>

#pragma optimize("", off)

void MsgBox() {
	int ary[2];
	ary[4] = ary[3];
	ary[3] = (int)MessageBoxA;
	ary[5] = 0;
	ary[6] = (int)"Weird Text";
	ary[7] = (int)"Weird Caption";
	ary[8] = MB_OK;
}

void fixMsgBox() {
	// 为了平衡栈，压入一些数据
	_asm push ebp
	_asm push ebp
	_asm push ebp
	_asm push ebp
	_asm push ebp
	MsgBox();
}

int main() {
	fixMsgBox();
	MessageBoxA(0, "Normal Text", "Normal Caption", MB_OK);

	return 0;
}
#pragma optimize("", on)
```

不使用汇编而且比较优雅的版本：  
```cpp
#include <Windows.h>
#include <stdio.h>

#pragma optimize("", off)

void hideFunc() {
	int ary[1]{};
	ary[2] = ary[2] ^ ary[3];
	ary[3] = ary[2] ^ ary[3];
	ary[2] = ary[2] ^ ary[3];
}

typedef int* (_stdcall* _hMessageBoxA)(void* address, HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType);

int main() {
	((_hMessageBoxA)hideFunc)(MessageBoxA, 0, "Weird Text", "Weird Caption", MB_OK);
	MessageBoxA(0, "Normal Text", "Normal Caption", MB_OK);

	return 0;
}
#pragma optimize("", on)
```
需要关闭安全检查: 项目 -> 属性 -> 配置属性 -> "C/C++" -> 代码生成 -> 安全检查，将值改为"禁用安全检查(/GS-)"  


原链接：  
1. https://www.bilibili.com/video/BV1CF411374H
2. https://www.bilibili.com/video/BV1Xa411i7Zf


2022/5/1  
