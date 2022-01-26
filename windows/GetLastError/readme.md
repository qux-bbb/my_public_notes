# GetLastError

GetLastError 用于获取当前最后一个错误值，所有错误值含义可以在 winerror.h 找到。  

```cpp
#include <Windows.h>
#include<stdio.h>

int main() {
	if (CreateDirectory(L"C:\\Windows", NULL) == 0)  // If the function fails, the return value is zero.
	{
		DWORD errCode = GetLastError();
		if (errCode == ERROR_ALREADY_EXISTS)
		{
			printf("ERROR_ALREADY_EXISTS(%d)\n", errCode);
		}
		else
		{
			printf("other error(%d)\n", errCode);
		}
	}

	getchar();
	return 0;
}
```

复制上面代码到VisualStudio，Ctrl+鼠标左键点击 ERROR_ALREADY_EXISTS, 可查看所有错误值。  


2022/1/26  
