# 获取用户名和计算机名

```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	char username[50] = { 0 };
	char computername[50] = { 0 };

	DWORD bufCharCount = 50;

	GetUserNameA(username, &bufCharCount);
	printf("username: %s\n", username);

	bufCharCount = 50;
	GetComputerNameA(computername, &bufCharCount);
	printf("computername: %s\n", computername);

	return 0;
}
```

需要注意的是，bufCharCount既作为输入参数，也作为输出参数。  
作为输入参数，表明缓冲区大小；作为输出参数，表明结果长度。  


参考链接: https://docs.microsoft.com/en-us/windows/win32/sysinfo/getting-system-information  


2021/9/1  
