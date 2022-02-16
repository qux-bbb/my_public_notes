# linux---man

man, manuals, 用来查看命令、api的用法  
对应网址: https://man7.org/linux/man-pages/index.html  

查看命令例子：  
```sh
# 查看kill命令手册
man kill

# 查看kill命令手册第2节(kill(2))
man 2 kill
```

查看api例子：  
```sh
# 查看execve api
man execve
```
结果的一部分：  
```r
#include <unistd.h>

int execve(const char *pathname, char *const argv[],
            char *const envp[]);
```

2020/2/7  
