# MinimumStackCommitInBytes阻止程序启动

有些勒索组织会通过注册表限制程序使用的资源或设置超过系统能够提供的资源来阻止程序启动

某勒索组织通过注册表设置了`SecurityHealthService.exe`的`MinimumStackCommitInBytes`为`0x88888888`，导致其无法启动
```r
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SecurityHealthService.exe
MinimumStackCommitInBytes类型为REG_DWORD，值为0x88888888
```

之后再通过驱动杀死相应进程，这样SecurityHealthService.exe就无法启动了
