# GetTickCount

GetTickCount可获取自系统启动以来经过的毫秒数，最多 49.7 天。  

简单示例：  
```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	DWORD runningTime = GetTickCount();

	printf("runningTime: %ldms\n", runningTime);  // 毫秒
	printf("runningTime: %lds\n", runningTime/1000);  // 秒
	printf("runningTime: %ldmin\n", runningTime/1000/60);  // 分钟
	printf("runningTime: %ldh\n", runningTime/1000/60/60);  // 小时
	printf("runningTime: %ldd\n", runningTime/1000/60/60/24);  // 天

	return 0;
}
```


参考链接: https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount  


2021/9/1  
