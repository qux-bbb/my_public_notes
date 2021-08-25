# strlen和wcslen

strlen: 获取字符串的长度  
wcslen: 获取宽字符串的长度  

示例：  
```cpp
#include <Windows.h>
#include <string.h>
#include <stdio.h>

int main() {
    char hello1[] = "hello";
    WCHAR hello2[] = L"hello";

    int len1 = strlen(hello1);
    int len2 = wcslen(hello2);

    printf("%d\n", len1);
    printf("%d\n", len2);

    return 0;
}
```
结果都是5  


参考链接: https://docs.microsoft.com/en-us/previous-versions/windows/embedded/ms860442(v=msdn.10)  


2021/8/25  
