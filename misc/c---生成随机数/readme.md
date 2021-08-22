# c---生成随机数

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    int a;
    srand((unsigned)time(NULL));
    a = rand();
    printf("%d\n", a);
    return 0;
}
```


原链接: http://c.biancheng.net/view/2043.html  


2021/8/22  
