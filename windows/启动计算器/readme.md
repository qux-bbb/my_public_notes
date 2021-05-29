# 启动计算器

一个程序启动计算器  

## 基础版
```cpp
#include <Windows.h>

int main()
{
	ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
	return 0;
}
```

## 动态获取ShellExecuteA
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

## 动态使用LoadLibraryA GetProcAddress

&&&&&&& 待补充  
先用这个试试 NtCurrentTeb，然后再换成汇编  


2021/5/27  
