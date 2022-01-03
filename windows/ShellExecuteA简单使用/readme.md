# ShellExecuteA简单使用

```r
#include <shellapi.h>
...
    HMODULE hwnd = GetModuleHandleA(NULL);
    ShellExecuteA((HWND)hwnd, "open", "C:\\windows\\system32\\cmd.exe", NULL, NULL, SW_SHOWNORMAL);
...
```

会涉及到 `HKEY_USERS\S-1-5-21-3634838001-3123217027-2557214320-1000\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap` 下的注册表项修改，没有什么影响  

https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea  
https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea#requirements  


2020/12/2  
