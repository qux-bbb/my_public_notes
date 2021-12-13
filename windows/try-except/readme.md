# try-except

try-except 微软自有的对c、c++的异常处理，也是SEH。    

```cpp
// exceptions_try_except_Statement.cpp
// Example of try-except statements
#include <stdio.h>
#include <windows.h> // for EXCEPTION_ACCESS_VIOLATION
#include <excpt.h>

int filter(unsigned int code, struct _EXCEPTION_POINTERS* ep)
{
    puts("in filter.");
    if (code == EXCEPTION_ACCESS_VIOLATION)
    {
        puts("caught AV as expected.");
        return EXCEPTION_EXECUTE_HANDLER;
    }
    else
    {
        puts("didn't catch AV, unexpected.");
        return EXCEPTION_CONTINUE_SEARCH;
    };
}

int main()
{
    int* p = 0x00000000;   // pointer to NULL
    puts("hello");
    __try
    {
        *p = 13;    // causes an access violation exception;
    }
    __except (filter(GetExceptionCode(), GetExceptionInformation()))
    {
        puts("in except");
    }
    puts("world");
}
```

输出：  
```r
hello
in filter.
caught AV as expected.
in except
world
```

IDA查看，和SEH相关的部分：  
```r
.text:00401045 push    offset stru_4122E8
.text:0040104A push    offset __except_handler4
.text:0040104F mov     eax, large fs:0
.text:00401055 push    eax
```
stru_4122E8结构包含了处理异常的函数地址  


原链接: https://docs.microsoft.com/en-us/cpp/cpp/try-except-statement?view=msvc-170  


2021/12/13  
