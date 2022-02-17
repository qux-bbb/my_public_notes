# linux---C读写文件

linux下vscode写c代码还是挺好用的  

```cpp
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
    char path[] = "test.txt";

    /*
    O_RDONLY    只读
    O_WRONLY    只写
    O_RDWR      可读可写
    O_CREAT     文件不存在则创建
    */
    char buf[] = "Hello World!";
    int fd_w = open(path, O_WRONLY|O_CREAT);
    write(fd_w, buf, sizeof(buf));
    close(fd_w);
    printf("write content: %s\n", buf);    

    char buf2[20] = {0};
    int fd_r = open(path, O_RDONLY);
    read(fd_r, buf2, 12);
    close(fd_r);
    printf("read content: %s\n", buf2);    

    return 0;
}
```

参考链接: https://blog.csdn.net/qq_43826212/article/details/106106508  

2022/2/16  
