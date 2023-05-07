# 自启动才访问百度

```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <windows.h>
#include <shlobj.h>

int main() {
    char szPath[MAX_PATH];
    if (SUCCEEDED(SHGetFolderPathA(NULL, CSIDL_STARTUP, NULL, 0, szPath))) {
        printf("Startup folder: %s\n", szPath);
        char szCurrentPath[MAX_PATH];
        if (GetModuleFileNameA(NULL, szCurrentPath, MAX_PATH)) {
            printf("Current path: %s\n", szCurrentPath);
            char szNewPath[MAX_PATH];
            char szFileName[MAX_PATH];
            _splitpath(szCurrentPath, NULL, NULL, szFileName, NULL);
            sprintf(szNewPath, "%s\\%s.exe", szPath, szFileName);
            printf("New path: %s\n", szNewPath);
            if (strcmp(szCurrentPath, szNewPath) != 0) {
                if (MoveFileA(szCurrentPath, szNewPath)) {
                    printf("Moved successfully!\n");
                }
                else {
                    printf("Failed to move!\n");
                }
            }
            else {
                ShellExecuteA(NULL, "open", "https://www.baidu.com", NULL, NULL, SW_SHOWNORMAL);
            }
        }
    }
    return 0;
}
```

代码来源: bing chat  


2023/5/5  
