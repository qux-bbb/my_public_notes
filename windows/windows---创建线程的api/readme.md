# windows---创建线程的api

现在就知道3个：  
CreateThread  
NtCreateThreadEx  
CreateRemoteThread  

具体的函数定义：  
```cpp
HANDLE CreateThread(
  LPSECURITY_ATTRIBUTES   lpThreadAttributes,
  SIZE_T                  dwStackSize,
  LPTHREAD_START_ROUTINE  lpStartAddress,
  __drv_aliasesMem LPVOID lpParameter,
  DWORD                   dwCreationFlags,
  LPDWORD                 lpThreadId
);
```

```cpp
// 在其他进程里创建线程
HANDLE CreateRemoteThread(
  HANDLE                 hProcess,
  LPSECURITY_ATTRIBUTES  lpThreadAttributes,
  SIZE_T                 dwStackSize,
  LPTHREAD_START_ROUTINE lpStartAddress,
  LPVOID                 lpParameter,
  DWORD                  dwCreationFlags,
  LPDWORD                lpThreadId
);
```

NtCreateThreadEx 未公开，有一个别人分析的  
```cpp
NTSTATUS NtCreateThreadEx(
    OUT PHANDLE ThreadHandle,
    IN ACCESS_MASK DesiredAccess,
    IN POBJECT_ATTRIBUTES ObjectAttributes OPTIONAL,
    IN HANDLE ProcessHandle,
    IN PTHREAD_START_ROUTINE StartRoutine,
    IN PVOID StartContext,
    IN ULONG CreateThreadFlags,
    IN ULONG ZeroBits OPTIONAL,
    IN ULONG StackSize OPTIONAL,
    IN ULONG MaximumStackSize OPTIONAL,
    IN PNT_PROC_THREAD_ATTRIBUTE_LIST AttributeList
);
```

参考链接：  
https://docs.microsoft.com/zh-cn/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread  
https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread  
https://www.cnblogs.com/Acg-Check/p/4283626.html  


2020/11/29  
