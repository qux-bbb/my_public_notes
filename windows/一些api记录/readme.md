## GetSystemDirectoryA
获取系统目录  
结果举例：`C:\Windows\system32`  


## GetWindowsDirectoryA
获取windows目录  
结果举例：`C:\Windows`  


## GetTempPathA
获取临时目录  
结果举例：`C:\Users\hello\AppData\Local\Temp\`  


## CreateFile
可用于打开文件，创建文件，确认文件是否存在  
```c++
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
```c++
#define GENERIC_READ                     (0x80000000L)
#define GENERIC_WRITE                    (0x40000000L)
#define GENERIC_EXECUTE                  (0x20000000L)
#define GENERIC_ALL                      (0x10000000L)
```
也可用这样的方式 `GENERIC_READ | GENERIC_WRITE`  

dwCreationDisposition可取值如下：  
```c++
#define CREATE_NEW          1
#define CREATE_ALWAYS       2
#define OPEN_EXISTING       3
#define OPEN_ALWAYS         4
#define TRUNCATE_EXISTING   5
```


## CreateService
用于创建windows服务  
```c++
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
```c++
#define SERVICE_BOOT_START             0x00000000
#define SERVICE_SYSTEM_START           0x00000001
#define SERVICE_AUTO_START             0x00000002
#define SERVICE_DEMAND_START           0x00000003
#define SERVICE_DISABLED               0x00000004
```
