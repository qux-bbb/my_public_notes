# 删除文件

## 删除其它文件
```cpp
#include <Windows.h>

int main()
{
    DeleteFile(L"hello.txt");
    return 0;
}
```

参考链接: https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-deletefile  


## 删除自身

### 使用ShellExecuteA
DeleteFile api不能删除自身，因为被占用，但用ShellExecuteA执行删除的命令可以把自身删掉。  

```cpp
#include <Windows.h>
#include <stdio.h>

int main() {

	// 获取当前程序绝对路径
	char exeFilePath[100 + 1] = { 0 };
	GetModuleFileNameA(GetModuleHandle(NULL), exeFilePath, 100);

	char commandStr[101] = { 0 };
	// sprintf不安全，所以用sprintf_s
	sprintf_s(commandStr, "/C DEL /F /Q %s >> NUL", exeFilePath);

	ShellExecuteA(NULL, "open", "cmd.exe", commandStr, NULL, SW_HIDE);

	return 0;
}
```

参考链接: https://blog.csdn.net/qq_43080331/article/details/83506474  

### 使用备用数据流
备用数据流可以通过DeleteFile把父文件删掉，很有意思。  
```cpp
#include <Windows.h>

bool IsChildProcess() {
    char exeFilePath[100 + 1] = { 0 };
    GetModuleFileNameA(GetModuleHandle(NULL), exeFilePath, 100);
    for (int i = 2; i <= 100; i++) {
        if (exeFilePath[i] == ':') {
            return true;
        }
    }
    return false;
}

void CreateChildProcess(WCHAR *fileName, WCHAR *childFileName) {
    HANDLE fp;
    unsigned char* fBuffer;
    DWORD fSize, dwSize;
    // 读父文件
    fp = CreateFile(fileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    fSize = GetFileSize(fp, 0);
    fBuffer = (unsigned char*)VirtualAlloc(NULL, fSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    ReadFile(fp, fBuffer, fSize, &dwSize, NULL);
    CloseHandle(fp);
    
    // 写子文件
    fp = CreateFile(childFileName, GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    DWORD dwBytesWritten = 0;
    BOOL bErrorFlag = WriteFile(fp, fBuffer, fSize, &dwBytesWritten, NULL);
    CloseHandle(fp);

    // 创建子进程
    STARTUPINFO si = { 0 };
    PROCESS_INFORMATION pi = { 0 };
    si.cb = sizeof(STARTUPINFO);
    CreateProcess(childFileName, NULL, NULL, NULL, TRUE, NULL, NULL, NULL, &si, &pi);
}

int main()
{
    WCHAR fileName[] = L"Test.exe";
    WCHAR childFileName[] = L"Test.exe:a";

    if (IsChildProcess()) {
        DeleteFile(fileName);
    } else {
        CreateChildProcess(fileName, childFileName);
    }

    return 0;
}
```


2021/6/3  
