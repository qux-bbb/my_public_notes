# gcc生成可执行文件过程

gcc可以直接生成一个可执行文件，这里同时记录一下拆解过程   

hello.c   
```cpp
#include <stdio.h>

int main(){
      printf("Hello World!\n");
      return 0;
}
```

普通生成   
```bash
gcc hello.c -o hello
```

拆解   
```bash
# 预处理，生成预编译文件 hello.i
gcc hello.c -E -o hello.i
# 编译，生成汇编文件 hello.s
gcc hello.i -S -o hello.s
# 汇编，生成目标文件 hello.o
gcc hello.s -c -o hello.o
# 链接，生成可执行文件 hello
gcc hello.o -o hello
```

也可以直接从前面任意阶段生成后面任意阶段的文件，如：  
```bash
# c文件生成汇编文件
gcc hello.c -S -o hello.s
# 预编译文件生成可执行文件
gcc hello.i -o hello
```



参考链接: https://blog.csdn.net/albertsh/article/details/89309107  


2021/5/30  
