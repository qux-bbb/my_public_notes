# 获取父进程路径

获取父进程路径，可用于反沙箱  

```cpp
#include <Windows.h>
#include <tlhelp32.h>
#include <stdio.h>

DWORD GetParentPID(DWORD pid)
{
	DWORD ppid = 0;
	PROCESSENTRY32W processEntry = { 0 };
	processEntry.dwSize = sizeof(PROCESSENTRY32W);
	HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (Process32FirstW(hSnapshot, &processEntry))
	{
		do
		{
			if (processEntry.th32ProcessID == pid)
			{
				ppid = processEntry.th32ParentProcessID;
				break;
			}
		} while (Process32NextW(hSnapshot, &processEntry));
	}
	CloseHandle(hSnapshot);
	return ppid;
}

int main() {
	DWORD parentPid = GetParentPID(GetCurrentProcessId());
	WCHAR parentName[MAX_PATH + 1];
	DWORD dwParentName = MAX_PATH;
	HANDLE hParent = OpenProcess(PROCESS_QUERY_INFORMATION, FALSE, parentPid);
	QueryFullProcessImageNameW(hParent, 0, parentName, &dwParentName); // another way to get process name is to use 'Toolhelp32Snapshot'
	//CharUpperW(parentName);
	wprintf(L"parentName: %ls\n", parentName);
	if (!wcsstr(parentName, L"explorer.exe")) {
		wprintf_s(L"Do nothing.\n");
		//return;
	} else
		wprintf_s(L"Now hacking...\n");

	getchar();
	return 0;
}
```


原链接: https://0xpat.github.io/Malware_development_part_2/  


2021/4/20  
