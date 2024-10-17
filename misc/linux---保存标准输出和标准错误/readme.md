# linux---保存标准输出和标准错误

示例程序：  
```c
#include <stdio.h>

int main() {
    // 写入标准输出 (stdout)
    printf("This is a message to stdout.\n");

    // 写入标准错误 (stderr)
    fprintf(stderr, "This is a message to stderr.\n");

    return 0;
}

// gcc -o test test.c
```

只保存到文件，分别保存：  
```bash
./test > stdout.txt 2> stderr.txt
```

既输出到终端，也保存到文件，分别保存：  
```bash
./test 2> >(tee stderr.txt >&2) | tee stdout.txt
```

既输出到终端，也保存到文件，保存在一个文件内：  
```bash
./test 2>&1 | tee output_and_errors.txt
```


参考链接：  
https://pwn.college/linux-luminarium/piping/  
腾讯元宝  


2024/10/17  
