# 连接远程计算机创建服务

```cpp
#include <windows.h>
#include <stdio.h>

#pragma comment(lib, "advapi32.lib")
#pragma comment(lib, "Mpr.lib")

#define SVCNAME TEXT("SvcName")

int main() {
	SC_HANDLE schSCManager;
	SC_HANDLE schService;

	NETRESOURCEA nr;

	nr.dwScope = RESOURCE_GLOBALNET;
	nr.dwType = RESOURCETYPE_ANY;
	nr.dwUsage = RESOURCEUSAGE_CONNECTABLE;
	nr.lpLocalName = LPSTR("");
	nr.lpRemoteName = LPSTR("\\\\1.2.3.4");
	nr.lpProvider = LPSTR("");

	DWORD dwTest = WNetAddConnection2A(&nr, "test", "admin", 0);

	if (dwTest != NO_ERROR) {
		printf("WNetAddConnection2 failed (%d)\n", dwTest);
		return 1;
	}

	// Get a handle to the SCM database. 
	schSCManager = OpenSCManagerA(
		"1.2.3.4",
		NULL,                    // ServicesActive database 
		SC_MANAGER_ALL_ACCESS);  // full access rights 

	if (NULL == schSCManager)
	{
		printf("OpenSCManager failed (%d)\n", GetLastError());
		return 1;
	}

	// Create the service
	schService = CreateService(
		schSCManager,              // SCM database 
		SVCNAME,                   // name of service 
		SVCNAME,                   // service name to display 
		SERVICE_ALL_ACCESS,        // desired access 
		SERVICE_WIN32_OWN_PROCESS, // service type 
		SERVICE_AUTO_START,        // start type 
		SERVICE_ERROR_NORMAL,      // error control type 
		L"test.exe",               // path to service's binary 
		NULL,                      // no load ordering group 
		NULL,                      // no tag identifier 
		NULL,                      // no dependencies 
		NULL,                      // LocalSystem account 
		NULL);                     // no password 

	if (schService == NULL)
	{
		printf("CreateService failed (%d)\n", GetLastError());
		CloseServiceHandle(schSCManager);
		return 1;
	}
	else printf("Service installed successfully\n");

	CloseServiceHandle(schService);
	CloseServiceHandle(schSCManager);

	return 0;
}
```

如果两台计算机不在一个域下，会有访问拒绝错误，需要在目标计算机创建注册表项：  
```r
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
"LocalAccountTokenFilterPolicy"=dword:00000001
```

参考链接：  
1. https://forums.codeguru.com/showthread.php?226674-OpenSCManager-on-remote-computer
2. https://stackoverflow.com/questions/8434766/remote-openscmanager-fails-with-access-denied
3. https://docs.microsoft.com/zh-CN/troubleshoot/windows-server/windows-security/user-account-control-and-remote-restriction


2022/1/17  
