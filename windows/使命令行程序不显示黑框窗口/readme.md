# 使命令行程序不显示黑框窗口

原理：  
命令行程序的subsystem默认是"console"，subsystem改成"windows"但入口点保持不变，就可以实现不显示黑框窗口了。  
```r
Function name                               Default for
mainCRTStartup (or wmainCRTStartup)         An application that uses /SUBSYSTEM:CONSOLE; calls main (or wmain)
WinMainCRTStartup (or wWinMainCRTStartup)   An application that uses /SUBSYSTEM:WINDOWS; calls WinMain (or wWinMain), which must be defined to use __stdcall
_DllMainCRTStartup                          A DLL; calls DllMain if it exists, which must be defined to use __stdcall
```

示例：  
```cpp
#include <Windows.h>

#pragma comment(linker, "/subsystem:\"windows\" /entry:\"mainCRTStartup\"")  // 不显示窗口

int main()
{
    MessageBoxA(NULL, "Hello World!", "caption", MB_OK);
    return 0;
}
```


参考链接：  
1. https://www.bilibili.com/video/BV1CF411374H
2. https://docs.microsoft.com/en-us/cpp/build/reference/entry-entry-point-symbol?view=msvc-170


2022/4/10  
