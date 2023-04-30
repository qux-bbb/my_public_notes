# pwn---最简单题部署

## 题目源码：  
```c
#include <stdio.h>
int main(int argc, char** argv)
{
    int modified;
    char buffer[10];
    modified = 0;
    // setvbuf(stdout, NULL, _IOLBF, 0);
    setbuf(stdout, NULL); // 取消输出缓存，这样设置，后面才能正确输出
    printf("Please input something:\n");
    gets(buffer);        // 引发缓冲区溢出
    if (modified != 0)
    {
        printf("Congratulations, you pwned it.\n");
    }
    else
    {
        printf("Please try again.\n");
    }
    return 0;
}

```

## 编译命令:  
```bash
gcc hello.c -o hello
```

## 运行:  
```bash
socat tcp-l:4444,reuseaddr,fork exec:./hello
```
reuseaddr 是防止有别的程序占用该端口，不能正常启动  

## 本地命令测试:
```
nc 127.0.0.1 4444
11111111110
```
溢出成功


---
2017/11/13  
