# 注册表对应文件位置

```
注册表中的位置                  文件系统中的文件路径
HKEY_LOCAL_MACHINE\System       %WINDIR%\system32\config\System
HKEY_LOCAL_MACHINE\SAM          %WINDIR%\system32\config\SAM
HKEY_LOCAL_MACHINE\Security     %WINDIR%\system32\config\Security
HKEY_LOCAL_MACHINE\Software     %WINDIR%\system32\config\Software
HKEY_USERS\User SID             Windows XP 及之前版本为 Documents and Settings\User\NTUSER.dat；
                                Windows Vista 及之后版本为 User\User\NTUSER.dat
HKEY_USERS\.Default             %WINDIR%\system32\config\default
```

获取这些文件的方式：  
开机情况下是不能直接复制这些文件，管理员权限下可以使用reg命令保存文件：  
```r
reg save HKLM\System System.hiv
reg save HKU\.Default dot_Default.hiv
```

关机状态下通过其它工具获取  
1. 如果用的是vmware虚拟机，可以用WinImage打开vmdk文件提取
2. 普通情况可以在关机情况下使用PE盘启动，复制文件出来(&&&&&&& 未测试)

&&&&&&& 还没找到解析单个注册表文件的工具  


来自: 《加密与解密》  

20200621  
