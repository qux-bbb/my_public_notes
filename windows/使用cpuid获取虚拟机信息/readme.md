使用cpuid获取虚拟机信息  

```c++
#include <stdio.h>
#include <Windows.h>


int main()
{
    unsigned int ueax = 0;
    unsigned int uebx = 0;
    unsigned int uecx = 0;
    unsigned int uedx = 0;
    __asm {
        mov eax, 0x40000000
        cpuid
        mov ueax, eax
        mov uebx, ebx
        mov uecx, ecx
        mov uedx, edx
    }
    printf("%08X-%08X-%08X-%08X\n", ueax, uebx, uecx, uedx);
    // ebx, ecx, edx 存储12字节的信息
    if (uebx && uecx && uedx) {
        printf("Vm info: %4.4s%4.4s%4.4s\n", &uebx, &uecx, &uedx);
    }
    else {
        printf("Not vm.\n");
    }
        
    return 0;
}
```


参考链接: https://www.cnblogs.com/oloroso/p/6182669.html  
