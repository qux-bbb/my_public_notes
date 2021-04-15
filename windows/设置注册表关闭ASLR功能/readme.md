设置注册表关闭ASLR功能  

设置如下注册表项并重启系统：  
```
Windows Registry Editor Version 5.00
 
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]
"MoveImages"=dword:00000000
```

原链接：https://www.52pojie.cn/thread-377450-1-1.html  
