# c---printf特殊符号

keywords: 格式化字符串  

## %lx
长整型数(long int)以16进制输出，长度最多为8位，值举例: fe7e7403  

## %n
之前输出字符的个数，示例如下:  
```c
#include <stdio.h>

int main()
{
    int val;

    printf("blah %n blah\n", &val);

    printf("val = %d\n", val);
    return 0;
}
```

## $
在C11中定义  
```c
#include <stdio.h>
int main() {
    int a = 3, b = 2;
    printf("%2$d %1$d", a, b);
    return 0;
}
```
结果为 2 3  

原链接 https://stackoverflow.com/questions/19327441/gcc-dollar-sign-in-printf-format-string

## %.48363x
.number的形式指定了后面要输出的长度，超过按后面的实际长度输出，不足就在前面补0  

## $hn
```c
printf("%1024c%23$hn\n");
//带有攻击性的做法，第01个参数对用%c，
//具体是什么不关心，目标是是把第23个参数
//指向的内存的前2个字节赋值为1024。
```
%hn 把前面打印的字符数（0x1024）输出到buff指向的2个字节  
%ln 把前面打印的字符数（0x1024）输出到buff指向的4个字节  
%n 把前面打印的字符数（0x1024）输出到buff指向的4个字节  


参考: http://www.cplusplus.com/reference/cstdio/printf/  
https://blog.csdn.net/u010517901/article/details/46486341  


---
2018/10/29  
