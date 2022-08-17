# TLS反调试

TLS, Thread Local Storage, 线程局部存储，其它线程不可访问，可实现多线程安全。利用TLS可以实现一种反调试。  

在程序一开始运行时，会创建一个主线程，而创建主线程前，会先执行TLS相关函数。  
执行顺序: TLS函数 -> 入口点 -> main函数  

反调试示例：  
```r
#include <windows.h>

#pragma comment(linker, "/INCLUDE:__tls_used")

void NTAPI TLS_CALLBACK(PVOID DllHandle, DWORD Reason, PVOID Reserved)
{
    if( IsDebuggerPresent() )
    {
        MessageBoxA(NULL, "Debugger Detected!", "TLS Callback", MB_OK);
        ExitProcess(1);
    }
}

#pragma data_seg(".CRT$XLX")
    PIMAGE_TLS_CALLBACK pTLS_CALLBACKs[] = { TLS_CALLBACK, 0 };
#pragma data_seg()

int main(void)
{
    MessageBoxA(NULL, "Hello :)", "main()", MB_OK);
}
```
TLS_CALLBACK函数会先于main函数执行，反调试比较隐蔽。  

使用vs2017生成release版程序时，需要注意禁用"全程序优化"：  
项目设置 -> C/C++ -> 优化 -> 全程序优化，设置为"否"  


参考：  
1. 逆向工程核心原理
2. https://github.com/reversecore/book/blob/master/소스코드/06_고급_리버싱/45_TLS_Callback_Function/src/HelloTls/HelloTls.cpp
3. https://github.com/reversecore/book/blob/master/실습예제/06_고급_리버싱/45_TLS_Callback_Function/bin/HelloTls.exe


2022/8/17  
