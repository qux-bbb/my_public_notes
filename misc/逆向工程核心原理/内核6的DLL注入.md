# 内核6的DLL注入

内核6(Vista/7/8)的创建远程进程发生变化，导致不能按原来的方式进行dll注入  


**Windows XP**  
Kernel32!CreateRemoteThhread()  
 -> ntdll!ZwCreateThread()  
 
**Windows 7**  
Kernel32!CreateRemoteThhread()  
 -> kernelbase!CreateRemoteThreadEx()  
 -> ntdll!ZwCreateThreadEx()  

win7 中的 ntdll!ZwCreateThreadEx() 会根据传入的参数判断创建进程的会话id，如果是0，则不创建。可以修改参数，直接使用该函数来创建进程  


InjectDll_new.cpp  
```c

#include "windows.h"
#include "stdio.h"
#include "tchar.h"

BOOL SetPrivilege(LPCTSTR lpszPrivilege, BOOL bEnablePrivilege) 
{
    TOKEN_PRIVILEGES tp;
    HANDLE hToken;
    LUID luid;

    if( !OpenProcessToken(GetCurrentProcess(),
                          TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, 
			              &hToken) )
    {
        _tprintf(L"OpenProcessToken error: %u\n", GetLastError());
        return FALSE;
    }

    if( !LookupPrivilegeValue(NULL,             // lookup privilege on local system
                              lpszPrivilege,    // privilege to lookup 
                              &luid) )          // receives LUID of privilege
    {
        _tprintf(L"LookupPrivilegeValue error: %u\n", GetLastError() ); 
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
        _tprintf(L"AdjustTokenPrivileges error: %u\n", GetLastError() ); 
        return FALSE; 
    } 

    if( GetLastError() == ERROR_NOT_ALL_ASSIGNED )
    {
        _tprintf(L"The token does not have the specified privilege. \n");
        return FALSE;
    } 

    return TRUE;
}

typedef DWORD (WINAPI *PFNTCREATETHREADEX)
( 
    PHANDLE                 ThreadHandle,	
    ACCESS_MASK             DesiredAccess,	
    LPVOID                  ObjectAttributes,	
    HANDLE                  ProcessHandle,	
    LPTHREAD_START_ROUTINE  lpStartAddress,	
    LPVOID                  lpParameter,	
    BOOL	                CreateSuspended,	
    DWORD                   dwStackSize,	
    DWORD                   dw1, 
    DWORD                   dw2, 
    LPVOID                  Unknown 
); 

BOOL IsVistaOrLater()
{
    OSVERSIONINFO osvi;

    ZeroMemory(&osvi, sizeof(OSVERSIONINFO));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);

    GetVersionEx(&osvi);

    if( osvi.dwMajorVersion >= 6 )
        return TRUE;

    return FALSE;
}

BOOL MyCreateRemoteThread(HANDLE hProcess, LPTHREAD_START_ROUTINE pThreadProc, LPVOID pRemoteBuf)
{
    HANDLE      hThread = NULL;
    FARPROC     pFunc = NULL;

    if( IsVistaOrLater() )    // Vista, 7, Server2008
    {
        pFunc = GetProcAddress(GetModuleHandle(L"ntdll.dll"), "NtCreateThreadEx");
        if( pFunc == NULL )
        {
            printf("MyCreateRemoteThread() : GetProcAddress(\"NtCreateThreadEx\") failed!!! [%d]\n",
                   GetLastError());
            return FALSE;
        }

        ((PFNTCREATETHREADEX)pFunc)(&hThread,
                                    0x1FFFFF,
                                    NULL,
                                    hProcess,
                                    pThreadProc,
                                    pRemoteBuf,
                                    FALSE,
                                    NULL,
                                    NULL,
                                    NULL,
                                    NULL);
        if( hThread == NULL )
        {
            printf("MyCreateRemoteThread() : NtCreateThreadEx() failed!!! [%d]\n", GetLastError());
            return FALSE;
        }
    }
    else                    // 2000, XP, Server2003
    {
        hThread = CreateRemoteThread(hProcess, 
                                     NULL, 
                                     0, 
                                     pThreadProc, 
                                     pRemoteBuf, 
                                     0, 
                                     NULL);
        if( hThread == NULL )
        {
            printf("MyCreateRemoteThread() : CreateRemoteThread() failed!!! [%d]\n", GetLastError());
            return FALSE;
        }
    }

	if( WAIT_FAILED == WaitForSingleObject(hThread, INFINITE) )
    {
        printf("MyCreateRemoteThread() : WaitForSingleObject() failed!!! [%d]\n", GetLastError());
        return FALSE;
    }

    return TRUE;
}

BOOL InjectDll(DWORD dwPID, char *szDllName)
{
    HANDLE hProcess = NULL;
    LPVOID pRemoteBuf = NULL;
    FARPROC pThreadProc = NULL;
    DWORD dwBufSize = strlen(szDllName)+1;

    if ( !(hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPID)) )
    {
        printf("[ERROR] OpenProcess(%d) failed!!! [%d]\n", 
        dwPID, GetLastError());
        return FALSE;
    }

    pRemoteBuf = VirtualAllocEx(hProcess, NULL, dwBufSize, 
                                MEM_COMMIT, PAGE_READWRITE);

    WriteProcessMemory(hProcess, pRemoteBuf, (LPVOID)szDllName, 
                       dwBufSize, NULL);

    pThreadProc = GetProcAddress(GetModuleHandle(L"kernel32.dll"), 
                                 "LoadLibraryA");

    if( !MyCreateRemoteThread(hProcess, (LPTHREAD_START_ROUTINE)pThreadProc, pRemoteBuf) )
    {
        printf("[ERROR] MyCreateRemoteThread() failed!!!\n");
        return FALSE;
    }

    VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE);

    CloseHandle(hProcess);

    return TRUE;
}

int main(int argc, char *argv[])
{
	// adjust privilege
    SetPrivilege(SE_DEBUG_NAME, TRUE);

    // InjectDll.exe <PID> <dll_path>
    if( argc != 3 )
    {
        printf("usage : %s <PID> <dll_path>\n", argv[0]);
        return 1;
    }

    if( !InjectDll((DWORD)atoi(argv[1]), argv[2]) )
    {
        printf("InjectDll() failed!!!\n");
        return 1;
    }

    printf("InjectDll() succeeded!!!\n");

    return 0;
}


```


dummy.cpp  
```c

#include "windows.h"
#include "tchar.h"

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    TCHAR   szPath[MAX_PATH]    = {0,};
    TCHAR   szMsg[1024]         = {0,};
    TCHAR   *p                  = NULL;

    switch( fdwReason )
    {
        case DLL_PROCESS_ATTACH : 
            GetModuleFileName(NULL, szPath, MAX_PATH);
            p = _tcsrchr(szPath, L'\\');
            if( p != NULL )
            {
                _stprintf_s(szMsg, 1024 - sizeof(TCHAR), 
                            L"Injected in %s(%d)", 
                            p + 1,                          // Process Name
                            GetCurrentProcessId());         // PID
                OutputDebugString(szMsg);
            }
            
            break;
    }

    return TRUE;
}

```


2019/6/23  
