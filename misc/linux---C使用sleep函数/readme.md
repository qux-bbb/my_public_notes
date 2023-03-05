# linux---C使用sleep函数

linux下用C调用sleep函数  

```cpp
#include <stdio.h>
#include <unistd.h>

int main(){
    for(int i=0;;i++){
        // unsigned int sleep(unsigned int seconds);
        sleep(1);
        printf("%d\n", i);
    }
    return 0;
}
```

参考链接: https://man7.org/linux/man-pages/man3/sleep.3.html  


2023/3/5  
