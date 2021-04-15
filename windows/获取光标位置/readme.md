keywords: 鼠标 位置 光标  

获取光标位置  

```c++
#include <stdio.h>
#include <Windows.h>


int main()
{
    POINT point;
    GetCursorPos(&point);
    printf("x: %d, y: %d\n", point.x, point.y);
    return 0;
}
```

参考链接: https://www.cnblogs.com/wangjixianyun/p/3426331.html  
