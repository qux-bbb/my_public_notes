# 自启动才访问百度

```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <shlobj.h>

int main(int argc, char* argv[])
{
    char szStartupPath[MAX_PATH];
    if (SUCCEEDED(SHGetFolderPathA(NULL, CSIDL_STARTUP, NULL, 0, szStartupPath)))
    {
        strcat(szStartupPath, "\\Test.exe");
        if (strcmp(argv[0], szStartupPath) != 0)
        {
            // 第一次运行，设置自启动
            printf("Startup path: %s\n", szStartupPath);
            MoveFileA(argv[0], szStartupPath);
        }
        else
        {
            // 自启动后，访问百度
            system("start http://www.baidu.com");
        }
    }
    return 0;
}
```

代码来源: bing chat  


2023/5/5  
