# vs---修改系统时间

```cpp
#include <stdio.h>
#include <Windows.h>


int ChangeYear(int addedYear) {
	SYSTEMTIME theSystemTime;
	GetLocalTime(&theSystemTime);

	theSystemTime.wYear += addedYear;
	SetLocalTime(&theSystemTime);
	return 0;
}

int main() {
	ChangeYear(1);
	return 0;
}
```

参考链接：  
1. C++SYSTEMTIME修改系统日期时间（非批处理）: https://blog.csdn.net/TweeChalice/article/details/96624308  
2. GetLocalTime function (sysinfoapi.h): https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime  


20201211  
