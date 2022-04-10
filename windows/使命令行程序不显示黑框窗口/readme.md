# 使命令行程序不显示黑框窗口


```cpp
#include <Windows.h>

#pragma comment(linker, "/subsystem:\"windows\" /entry:\"mainCRTStartup\"")  // 不显示窗口

int main()
{
    MessageBoxA(NULL, "Hello World!", "caption", MB_OK);
    return 0;
}
```

还不知道原理  


原链接: https://www.bilibili.com/video/BV1CF411374H  


2022/4/10  
