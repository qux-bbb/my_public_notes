# deb打包

keywords: 生成deb 制作deb  

一个简单生成deb包的流程，不那么正规，先记一下  

hello.c  
```c
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```
生成hello二进制文件  
```r
gcc -o hello hello.c
```
准备这样的目录结构：  
```
the_hello
├── DEBIAN
│   └── control
└── usr
    └── bin
        └── hello
```
hello就是上面生成的hello二进制文件  
control文件内容为：  
```r
Package: hello
Version: 1.0
Section: custom
Priority: optional
Architecture: all
Essential: no
Installed-Size: 16192
Maintainer: jack
Description: Print Hello World on the screen
```

执行以下命令，即可生成 the_hello.deb包：  
```r
dpkg-deb --build the_hello
```

安装: `sudo dpkg -i the_hello.deb`, 安装之后会有 `hello` 命令  
卸载: `sudo dpkg -P hello`  


原链接: https://linuxconfig.org/easy-way-to-create-a-debian-package-and-local-package-repository  


2021/10/3  
