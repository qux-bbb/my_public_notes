# 启动计算器

一个程序启动计算器，隐藏使用api  
测试使用IDE: VS2019  

## 基础版
```cpp
#include <Windows.h>

int main() {
	ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
	return 0;
}
```

## 导入表隐藏ShellExecuteA
```cpp
#include <Windows.h>

//      返回类型  函数调用约定 函数类型        各参数类型
typedef HINSTANCE(WINAPI* ShellExecuteATYPE) (HWND, LPCSTR, LPCSTR, LPCSTR, LPCSTR, INT);

int main() {
	HINSTANCE Shell32Dll = LoadLibraryA("Shell32.dll");
	ShellExecuteATYPE ShellExecuteA = (ShellExecuteATYPE)GetProcAddress(Shell32Dll, "ShellExecuteA");
	ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
	FreeLibrary(Shell32Dll);

	return 0;
}
```

参考链接：  
https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress  
https://docs.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking  

## 导入表隐藏LoadLibraryA GetProcAddress

&&&&&&& 待补充  
```cpp
#include <Windows.h>

typedef FARPROC(WINAPI* GetProcAddressTYPE) (HMODULE, LPCSTR);

int main() {

	// 获取kernel32.dll的基地址
	HINSTANCE Kernel32Dll = NULL;
	__asm {
		pushad
		mov eax, fs : [30h] ; 获取PEB所在地址
		mov eax, [eax + 0ch]; 获取PEB_LDR_DATA 结构指针
		mov esi, [eax + 1ch]; 获取InInitializationOrderModuleList 链表头
							; 第一个LDR_MODULE节点InInitializationOrderModuleList成员的指针
		lodsd				; 获取双向链表当前节点后继的指针
		mov eax, [eax + 8]	; 获取kernel32.dll的基地址
		mov Kernel32Dll, eax
		popad
	}

	char GetProcAddressStr[] = "GetProcAddress";
	GetProcAddressTYPE GetProcAddress;

	&&&&&&& 获取GetProcAddress，然后就能用GetProcAddress获取其它api了
	return 0;
}
```

参考链接：  
https://www.cnblogs.com/xuanyuan/p/4031751.html  
WindowsPE权威指南 11.3  
《Windows PE权威指南》随书资源包 https://bbs.pediy.com/thread-141538.htm  

2021/5/27  
