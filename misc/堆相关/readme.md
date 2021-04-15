# 堆相关

先写一个用堆的例子：  
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int len = 1000;
    
    char *the_memory = (char*)malloc(len*sizeof(char));

    strcpy(the_memory, "Hello World!\n");
    printf("%s", the_memory);

    free(the_memory);
    
    return 0;
}
```

malloc函数不是真正与系统交互的函数，分配小内存用brk函数，大内存用mmap函数  

以后慢慢补充  


参考链接: 
1. https://blog.csdn.net/weixin_39662462/article/details/111269792
2. https://ctf-wiki.org/pwn/linux/glibc-heap/heap_overview/


20210403  
