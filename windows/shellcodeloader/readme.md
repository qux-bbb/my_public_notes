# shellcodeloader

执行 shellcode，代码摘自《加密与解密》  
```cpp
#include "stdafx.h"
#include <Windows.h>

int main(int argc, char* argv[])
{
    HANDLE fp;
    unsigned char* fBuffer;
    DWORD fSize, dwSize;
    fp = CreateFile("Shellcode_bin.bin", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    fSize = GetFileSize(fp, 0);
    fBuffer = (unsigned char *)VirtualAlloc(NULL, fSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    ReadFile(fp, fBuffer, fSize, &dwSize, 0);
    CloseHandle(fp);

    _asm
    {
        pushad
        mov eax, fBuffer
        call eax
        popad
    }
    printf("Hello World!\n");
    return 0;
}
```

这个项目更倾向于调试 shellcode，挺好用的，可以等调试器附加上去再继续运行：  
https://github.com/OALabs/BlobRunner  


2020/09/23  
