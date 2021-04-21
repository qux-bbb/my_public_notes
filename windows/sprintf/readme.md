# sprintf

sprintf，字符串格式化函数。  

VS2017示例如下：  
```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	char msg[100] = { 0 };
	// sprintf不安全，所以用sprintf_s
	sprintf_s(msg, "%s: %08x", "Sorry", GetLastError());
	MessageBoxA(NULL, msg, "msg", MB_OK);

	WCHAR wMsg[100] = { 0 };
	wsprintf(wMsg, L"%s: %08x", L"Sorry", GetLastError());
	MessageBox(NULL, wMsg, TEXT("wMsg"), MB_OK);

	return 0;
}
```


2021/4/21  
