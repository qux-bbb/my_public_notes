windows，执行命令获取结果  

```c++
#include <stdio.h>
#include <Windows.h>

#define BUFFER_LEN 1024 * 4


int main()
{
    TCHAR szCmdLineW[] = L"cmd.exe /c whoami";     //保存命令行信息   
    char buffer[BUFFER_LEN] = { 0 };                         //保存命令行输出   
    DWORD bytesRead = 0;

    SECURITY_ATTRIBUTES sa = { 0 };
    HANDLE hRead = NULL, hWrite = NULL;                         //设置管道读写句柄   
    sa.nLength = sizeof(SECURITY_ATTRIBUTES);
    sa.lpSecurityDescriptor = NULL;
    sa.bInheritHandle = TRUE;
    if (!CreatePipe(&hRead, &hWrite, &sa, 0))                    //创建管道   
    {
        return false;
    }
    STARTUPINFO si = { 0 };
    PROCESS_INFORMATION pi = { 0 };
    si.cb = sizeof(STARTUPINFO);
    GetStartupInfo(&si);
    si.hStdError = hWrite;
    si.hStdOutput = hWrite;
    si.wShowWindow = SW_HIDE;
    si.dwFlags = STARTF_USESHOWWINDOW | STARTF_USESTDHANDLES;
    if (!CreateProcess(NULL, szCmdLineW, NULL, NULL, TRUE, NULL, NULL, NULL, &si, &pi))
    {
        CloseHandle(hWrite);
        CloseHandle(hRead);
        return false;
    }
    WaitForSingleObject(pi.hProcess, 3000);                  //等待新进程结束   
    // Close process and thread handles.       
    CloseHandle(pi.hProcess);                                   //关闭新进程的主线程   
    CloseHandle(pi.hThread);                                    //关闭新进程   
    CloseHandle(hWrite);                                        //关闭管道的写句柄   
    ReadFile(hRead, buffer, BUFFER_LEN, &bytesRead, NULL); //从管道中读取新进程的运行结果   
    CloseHandle(hRead);                                         //关闭管道的读句柄   
    printf("%s\n", buffer);
    return 0;
}
```

参考链接: http://www.linuxidc.com/Linux/2011-04/34092.htm  
