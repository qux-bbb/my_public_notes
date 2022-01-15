# 获取和设置光标位置

keywords: 鼠标 位置 光标  
  
```c++
#include <stdio.h>
#include <Windows.h>

int main()
{
	POINT point;

	// 获取光标坐标
	GetCursorPos(&point);
	printf("x: %d, y: %d\n", point.x, point.y);

	// 设置光标坐标
	SetCursorPos(point.x + 200, point.y + 100);

	return 0;
}
```

参考链接：  
1. https://www.cnblogs.com/wangjixianyun/p/3426331.html
2. https://blog.csdn.net/everlasting_20141622/article/details/60779518
