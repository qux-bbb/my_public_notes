# 反调试---NtSetInformationThread

```r
六、NtSetInformationThread方法
 
这个也是使用Windows的一个未公开函数的方法，你可以在当前线程里调用NtSetInformationThread，调用这个函数时，如果在第二个参数里指定0x11这个值（意思是ThreadHideFromDebugger），等于告诉操作系统，将所有附加的调试器统统取消掉。示例代码:
 
// 声明一个函数指针。
typedef NTSTATUS (*NtSetInformationThreadPtr)(HANDLE threadHandle,
       THREADINFOCLASS threadInformationClass,
       PVOID threadInformation,
       ULONG threadInformationLength);
 
void NtSetInformationThreadApproach()
{
      HMODULE hModule = LoadLibrary(TEXT("ntdll.dll"));
      NtSetInformationThreadPtr NtSetInformationThread = (NtSetInformationThreadPtr)GetProcAddress(hModule, "NtSetInformationThread");
    
      NtSetInformationThread(GetCurrentThread(), (THREADINFOCLASS)0x11, 0, 0);
}
```

关键点: NtSetInformationThread, 第2个参数的值是0x11  

效果是调试器显示程序一直在运行, 但就是不结束  

原链接: https://www.cnblogs.com/this-543273659/archive/2013/03/04/2943380.html  

---
2020/4/25  
