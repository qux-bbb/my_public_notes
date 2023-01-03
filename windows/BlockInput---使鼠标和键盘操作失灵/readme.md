# BlockInput---使鼠标和键盘操作失灵

让鼠标和键盘在一定时间内没有反应，需要管理员权限运行才生效。  
```c
#include <windows.h>
#include <time.h>

int main() {
	int start = clock();
	while (clock()-start<=10000)
	{
		BlockInput(true);
	}
	return 0;
}
```

原链接: https://blog.csdn.net/qq_42587937/article/details/81478939  


2020/10/24  
