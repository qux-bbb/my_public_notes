# linux---C读写文件

linux下vscode写c代码还是挺好用的  

```cpp
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(){
    char path[] = "test.txt";

    /*
    int open(const char *pathname, int flags);
    int open(const char *pathname, int flags, mode_t mode);

    flags:
    O_RDONLY    只读
    O_WRONLY    只写
    O_RDWR      可读可写
    O_CREAT     文件不存在则创建
    O_APPEND    追加模式，指针在文件尾

    mode:
    S_IRUSR     00400 用户有读权限
    S_IWUSR     00200 用户有写权限
    */
    char buf[] = "Hello World!";
    int fd_w = open(path, O_WRONLY|O_CREAT|O_APPEND, S_IRUSR|S_IWUSR);
    write(fd_w, buf, strlen(buf));
    close(fd_w);
    printf("write content: %s\n", buf);    

    char buf2[100] = {0};
    int fd_r = open(path, O_RDWR);
    read(fd_r, buf2, 90);
    close(fd_r);
    printf("read content: %s\n", buf2);    

    return 0;
}
```

参考链接：  
1. https://blog.csdn.net/qq_43826212/article/details/106106508
2. https://man7.org/linux/man-pages/man2/open.2.html


2022/2/16  
