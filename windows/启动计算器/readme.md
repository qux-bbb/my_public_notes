# 隐藏使用api-启动计算器

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

```cpp
#include <Windows.h>

typedef FARPROC(WINAPI* GetProcAddressTYPE) (HMODULE, LPCSTR);
typedef HMODULE(WINAPI* LoadLibraryATYPE) (LPCSTR);
typedef BOOL(WINAPI* FreeLibraryTYPE) (HMODULE);

typedef HINSTANCE(WINAPI* ShellExecuteATYPE) (HWND, LPCSTR, LPCSTR, LPCSTR, LPCSTR, INT);

int main() {

	// 获取kernel32.dll的基地址
	HINSTANCE Kernel32Dll = NULL;
	__asm {
		pushad
		mov eax, fs : [30h] ; 获取PEB所在地址
		mov eax, [eax + 0ch]; 获取PEB_LDR_DATA 结构指针
		mov esi, [eax + 1ch]; 获取InInitializationOrderModuleList 链表头
		; 第一个LDR_MODULE节点InInitializationOrderModuleList成员的指针
		lodsd; 获取双向链表当前节点后继的指针
		mov eax, [eax + 8]; 获取kernel32.dll的基地址
		mov Kernel32Dll, eax
		popad
	}

	// 找到GetProcAddress
	PIMAGE_DOS_HEADER ImageDosHeader = (PIMAGE_DOS_HEADER)Kernel32Dll;
	PIMAGE_NT_HEADERS ImageNtHeaders = (PIMAGE_NT_HEADERS)((PBYTE)ImageDosHeader + ImageDosHeader->e_lfanew);
	PIMAGE_EXPORT_DIRECTORY ImageExportDirectory = (PIMAGE_EXPORT_DIRECTORY)((ULONG)Kernel32Dll + ImageNtHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress);

	DWORD Index = 0;
	WORD FunctionIndex = 0;
	CHAR* FunctionName = NULL;
    while (true)
    {
        FunctionName = (CHAR*)((ULONG)Kernel32Dll + (((PULONG)((ULONG)Kernel32Dll + ImageExportDirectory->AddressOfNames))[Index++]));
        if (strncmp(FunctionName, "GetProcAddress", 14) == 0)
            break;
    }
    FunctionIndex = ((PWORD)((ULONG)Kernel32Dll + ImageExportDirectory->AddressOfNameOrdinals))[Index - 1];
	GetProcAddressTYPE GetProcAddress = (GetProcAddressTYPE)((ULONG)Kernel32Dll + (((PULONG)((ULONG)Kernel32Dll + ImageExportDirectory->AddressOfFunctions))[FunctionIndex]));

	// 加载 LoadLibraryA
	LoadLibraryATYPE LoadLibraryA = (LoadLibraryATYPE)GetProcAddress(Kernel32Dll, "LoadLibraryA");
	// 加载 FreeLibrary
	FreeLibraryTYPE FreeLibrary = (FreeLibraryTYPE)GetProcAddress(Kernel32Dll, "FreeLibrary");

	// 加载 ShellExecuteA
	HINSTANCE Shell32Dll = LoadLibraryA("Shell32.dll");
	ShellExecuteATYPE ShellExecuteA = (ShellExecuteATYPE)GetProcAddress(Shell32Dll, "ShellExecuteA");

	// 启动 calc.exe
	ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
	
	// 释放库
	FreeLibrary(Shell32Dll);

	return 0;
}
```

还能做的事情就是把字符串加密，使用的时候再解密，使用完之后清除，这样的逻辑了。  

参考链接：  
1. https://www.cnblogs.com/xuanyuan/p/4031751.html  
2. WindowsPE权威指南 11.3  
3. 《Windows PE权威指南》随书资源包 https://bbs.pediy.com/thread-141538.htm  

2021/5/27  
