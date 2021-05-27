# 启动计算机

```cpp
#include <Windows.h>

int main()
{
	ShellExecuteA(NULL, "open", "calc.exe", NULL, NULL, SW_SHOWNORMAL);
	return 0;
}
```


2021/5/27  
