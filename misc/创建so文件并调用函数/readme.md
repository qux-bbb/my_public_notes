# 创建so文件并调用函数

keywords: 创建共享库 shared object  

## 准备文件
mylib.c  
```c
#include <stdio.h>

void print_hello() {
    printf("Hello from the shared mylib!\n");
}
```

main.c  
```c
extern void print_hello();

int main() {
    print_hello();
    return 0;
}
```

## 编译
```bash
# -fPIC, position-independent-code, 位置无关代码
# libmylib.so 名字需要以lib开头，.so结尾
gcc -shared -fPIC -o libmylib.so mylib.c
# -lmylib 这里的"mylib"，gcc会在前面添加"lib"在后面添加".so"去找相应文件
gcc -o main main.c -L. -lmylib
```

## 运行
```bash
# 使main能找到相应的.so文件
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
./main
```


参考资料：  
1. https://blog.csdn.net/gaoxiang__/article/details/38094525
2. chatgpt


2023/4/23  
