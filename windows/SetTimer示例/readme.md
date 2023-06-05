# SetTimer示例

```c
#include <stdio.h>
#include <windows.h>

void CALLBACK f(HWND hwnd, UINT uMsg, UINT timerId, DWORD dwTime)
{
	printf("Hello\n");
}

int main()
{
	MSG msg;

	SetTimer(NULL, 0, 1000 * 3, (TIMERPROC)& f);
	while (GetMessage(&msg, NULL, 0, 0)) {
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return 0;
}
```


2019/11/19  
