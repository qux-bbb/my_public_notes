# VS2019命令行编译程序

准备示例代码sample.c  
```cpp
#include <stdio.h>

int main()
{
    printf("Hello, World! This is a native C program compiled on the command line.\n");
    return 0;
}
```

搜索 `Developer Command Prompt for VS 2019` 打开，切换到sample.c所在文件夹，执行命令：  
```bat
cl.exe sample.c
```
即可生成 sample.obj 和 sample.exe  

如果想指定生成可执行文件的文件名，执行以下命令：  
```bat
cl.exe sample.c /Fe:the_name.exe
```

如果想把编译链接的过程分开，执行以下命令：  
```bat
:: /c 表示仅编译不链接
cl.exe sample.c /c
:: 根据obj文件生成可执行文件
cl.exe sample.obj
```


参考链接: https://docs.microsoft.com/en-us/cpp/build/walkthrough-compile-a-c-program-on-the-command-line?view=msvc-160  


2021/5/29  
