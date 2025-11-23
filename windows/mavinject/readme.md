# mavinject

## 基本语法
```bat
mavinject <PID> /INJECTRUNNING <DLL绝对路径>
```

## 验证注入效果
创建一个简单的DLL，当被加载时会显示消息框，这样可以直观地看到注入是否成功
```cpp
// TestDll.cpp
#include "pch.h"
#include <windows.h>

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        // DLL被加载时显示消息框
        MessageBox(NULL, L"DLL注入成功！", L"注入验证", MB_OK | MB_ICONINFORMATION);
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
```

使用notepad测试注入效果
1. 编译TestDll.cpp为TestDll.dll
2. 打开notepad.exe，进程ID为1234
3. 执行以下命令注入DLL
    ```bat
    mavinject 1234 /INJECTRUNNING C:\path\to\TestDll.dll
    ```
4. notepad.exe会弹出消息框提示注入成功