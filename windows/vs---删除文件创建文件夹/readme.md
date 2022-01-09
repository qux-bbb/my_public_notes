# vs---删除文件创建文件夹

```cpp
#include <Windows.h>

LPCWSTR svchostComPath = L"C:\\Windows\\svchost.com";

int main(){
    DeleteFile(svchostComPath);
    CreateDirectory(svchostComPath, NULL);
    return 0;
}
```

删除文件：`RemoveDirectory(svchostComPath);`  

参考链接：https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectorya  


2020/12/11  
