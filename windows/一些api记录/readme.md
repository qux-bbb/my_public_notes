# 一些api记录

## GetSystemDirectoryA
获取系统目录  
结果举例：`C:\Windows\system32`  


## GetWindowsDirectoryA
获取windows目录  
结果举例：`C:\Windows`  


## GetTempPathA
获取临时目录  
结果举例：`C:\Users\hello\AppData\Local\Temp\`  


## CreateFileA
可用于打开文件，创建文件，确认文件是否存在  
```cpp
HANDLE CreateFileA(
  LPCSTR                lpFileName,
  DWORD                 dwDesiredAccess,
  DWORD                 dwShareMode,
  LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  DWORD                 dwCreationDisposition,
  DWORD                 dwFlagsAndAttributes,
  HANDLE                hTemplateFile
);
```

dwDesiredAccess可取值如下：  
```cpp
#define GENERIC_READ                     (0x80000000L)
#define GENERIC_WRITE                    (0x40000000L)
#define GENERIC_EXECUTE                  (0x20000000L)
#define GENERIC_ALL                      (0x10000000L)
```
也可用这样的方式 `GENERIC_READ | GENERIC_WRITE`  

dwCreationDisposition可取值如下：  
```cpp
#define CREATE_NEW          1
#define CREATE_ALWAYS       2
#define OPEN_EXISTING       3
#define OPEN_ALWAYS         4
#define TRUNCATE_EXISTING   5
```


## CreateServiceA
用于创建windows服务  
```cpp
SC_HANDLE CreateServiceA(
  SC_HANDLE hSCManager,         // SCM database 
  LPCSTR    lpServiceName,      // name of service 
  LPCSTR    lpDisplayName,      // service name to display
  DWORD     dwDesiredAccess,    // desired access 
  DWORD     dwServiceType,      // service type 
  DWORD     dwStartType,        // start type 
  DWORD     dwErrorControl,     // error control type 
  LPCSTR    lpBinaryPathName,   // path to service's binary 
  LPCSTR    lpLoadOrderGroup,   // load ordering group 
  LPDWORD   lpdwTagId,          // tag identifier 
  LPCSTR    lpDependencies,     // dependencies 
  LPCSTR    lpServiceStartName, // user name
  LPCSTR    lpPassword          // user pass
);
```

dwStartType可取值如下：  
```cpp
#define SERVICE_BOOT_START             0x00000000
#define SERVICE_SYSTEM_START           0x00000001
#define SERVICE_AUTO_START             0x00000002
#define SERVICE_DEMAND_START           0x00000003
#define SERVICE_DISABLED               0x00000004
```


## GetDriveTypeA
用于获取磁盘驱动器的类型  
```cpp
UINT GetDriveTypeA(
  LPCSTR lpRootPathName
);
```

返回值含义  
```
Return value          Description                                                                                    
0 DRIVE_UNKNOWN       The drive type cannot be determined.                                                           
1 DRIVE_NO_ROOT_DIR   The root path is invalid; for example, there is no volume mounted at the specified path.       
2 DRIVE_REMOVABLE     The drive has removable media; for example, a floppy drive, thumb drive, or flash card reader. 
3 DRIVE_FIXED         The drive has fixed media; for example, a hard disk drive or flash drive.                      
4 DRIVE_REMOTE        The drive is a remote (network) drive.                                                         
5 DRIVE_CDROM         The drive is a CD-ROM drive.                                                                   
6 DRIVE_RAMDISK       The drive is a RAM disk.              
```

中文例子  
```
返回值                中文例子
0 DRIVE_UNKNOWN       未知
1 DRIVE_NO_ROOT_DIR   无效
2 DRIVE_REMOVABLE     软盘，U盘，闪存卡读卡器
3 DRIVE_FIXED         硬盘，闪存
4 DRIVE_REMOTE        远程（网络）盘
5 DRIVE_CDROM         光盘
6 DRIVE_RAMDISK       RAM内存盘
```


2021/6/9  
