# 获取电脑内存

```cpp
#include <Windows.h>
#include <stdio.h>


int main()
{
	MEMORYSTATUSEX memoryStatusEx;
	// 必须设置dwLength，否则结果错误
	memoryStatusEx.dwLength = sizeof(memoryStatusEx);
	// 官方说GlobalMemoryStatus函数有问题，所以用GlobalMemoryStatusEx函数
	GlobalMemoryStatusEx(&memoryStatusEx);

	// 单位 byte
	printf("ullTotalPhys: %I64d\n", memoryStatusEx.ullTotalPhys);
	
	return 0;
}
```

参考链接：  
1. https://duck1998.github.io/2019/07/03/OS-homework-3.html
2. https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-globalmemorystatus
3. https://docs.microsoft.com/en-us/windows/win32/api/winbase/ns-winbase-memorystatus
4. https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex
5. https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/ns-sysinfoapi-memorystatusex


2021/9/1  
