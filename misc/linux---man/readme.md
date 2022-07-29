# linux---man

## 命令
man, manuals, 手册、说明书, 用来查看命令、api的用法  
对应网址: https://man7.org/linux/man-pages/index.html  

查看命令例子：  
```sh
# 查看kill命令手册，用 `man 1 kill` 更准确
man kill

# 查看kill命令手册第2节(kill(2))
man 2 kill
```

查看api例子：  
```sh
# 查看execve api, 用 `man 2 execve` 更准确
man execve
```
结果的一部分：  
```r
#include <unistd.h>

int execve(const char *pathname, char *const argv[],
            char *const envp[]);
```

## 网站
man7.org  
估计是网站所有者叫Michael Kerrisk，都是7位，所以申请了这样的域名  

这里是man-pages主页：  
https://man7.org/linux/man-pages/index.html  

在linux下使用命令`man ls`可以看到ls的详细用法，这是man7网站对应的内容：  
https://man7.org/linux/man-pages/man1/ls.1.html  

这里有各章节提供内容描述，可以根据分类查找相关内容，进入具体章节会跳转到 man7.org：  
https://www.kernel.org/doc/man-pages/  
```r
1, user commands, 用户命令，如 ls
2, system calls, linux内核提供的系统调用，如 fork
3, library functions, 标准C库函数，如 fprintf
4, special files(devices), 各种特殊设备，如 zero
5, file formats and filesystems, 文件格式和文件系统，如 shadow
6, games, 游戏，好像没内容
7, overview and miscellany section, 概述和杂项部分，如 uri
8, administration and privileged commands, 管理和特权命令，如 ip
```


---
2020/2/7  
