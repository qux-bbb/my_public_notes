# windows---C-判断路径是否为文件夹

```c
#pragma comment (lib, "shlwapi.lib")

#include <stdio.h>
#include <windows.h>
#include <shlwapi.h>

int main() {
	if (PathIsDirectory(L"D:\\tmp"))
		printf("Right!\n");
	else
		printf("Wrong!\n");
	return 0;
}
```

参考链接：  
1. https://docs.microsoft.com/zh-cn/windows/win32/api/shlwapi/nf-shlwapi-pathisdirectorya  
2. https://forums.codeguru.com/showthread.php?198910-PathIsDirectory()-question  
3. https://forums.codeguru.com/showthread.php?510606-PathIsDirectory  


2020/12/4  
