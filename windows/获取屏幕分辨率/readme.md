# 获取屏幕分辨率

keywords: 屏幕宽高  

```cpp
#include <Windows.h>
#include <stdio.h>

int main()
{
	int cxScreen = GetSystemMetrics(SM_CXSCREEN);  // wide
	int cyScreen = GetSystemMetrics(SM_CYSCREEN);  // high

	printf("screen size: %dx%d", cxScreen, cyScreen);

	return 0;
}
```

原链接: https://blog.csdn.net/lsk1124981644/article/details/43818081  


2021/8/31  
