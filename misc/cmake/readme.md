# cmake

cmake，cross platform make，主要用于构建makefile或者project文件。  
CMakeLists.txt是其默认配置文件。  


## 简单示例
这个示例演示了linux系统下构建，编译，安装程序的过程。  

hello.c  
```cpp
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```

CMakeLists.txt  
```CMakeList
cmake_minimum_required(VERSION 3.20.2)

project(hello VERSION 1.0)

add_executable(hello hello.c)

install(TARGETS hello DESTINATION /usr/bin/)
```

执行命令：  
```bash
# 创建文件夹，进入，生成MakeFile文件
mkdir build
cd build
cmake ..
# 编译
cmake --build .
# 安装
sudo cmake --install .
```
编译和安装也可以直接用make，像这样：  
```
make
make install
```


参考链接：  
1. https://zhuanlan.zhihu.com/p/374896587  
2. https://cmake.org/cmake/help/v3.20/guide/tutorial/index.html


2021/6/5  
