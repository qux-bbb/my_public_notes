# C---main函数参数

```cpp
#include <stdio.h>

int main(int argc, const char** argv, const char** envp) {
    printf("%d\n", argc);
    printf("%s\n", argv[0]);
    return 0;
}
```
argc: 参数个数，默认1  
argv: 参数，第1个是当前程序绝对路径  
envp: 环境变量  


2021/9/28  
