# linux---C执行命令

system函数执行命令：  
```cpp
#include <stdlib.h>

int main(){
    char command[] = "ls -l";
    system(command);

    return 0;
}
```

popen函数执行命令获取结果：  
```cpp
#include <stdio.h>

int main(){
    char command[] = "ls -l";
    char buf[1024];
    FILE *ptr;
    if((ptr=popen(command, "r"))!=NULL){
        while (fgets(buf, 1024, ptr)!=NULL)
        {
            printf("%s", buf);
        }
        pclose(ptr);
        ptr = NULL;        
    }else{
        printf("popen %s error\n", command);
    }

    return 0;
}
```

参考链接：  
1. https://www.cnblogs.com/FlyAway2013/p/3625107.html
2. https://blog.csdn.net/qianbo042311/article/details/119251541
3. man命令

2022/2/16  
