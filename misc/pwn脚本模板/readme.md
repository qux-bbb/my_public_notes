# pwn脚本模板

```python
# coding:utf8
# python3

'''
暂时的pwn模板，慢慢调整
'''

from pwn import *
from LibcSearcher import LibcSearcher

exe = ELF('ret2libc3')

context.binary = exe

# 可取值['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING'] 或整数
if args.D:
    context.log_level = 'DEBUG'
else:
    context.log_level = 'INFO'


# puts_plt = exe.plt['puts']  # 系统api在plt段的地址，会跳到.got.plt段的相应位置，已经调用过的api可以直接用这个地址，因为已经被填充过了
# start_symbol = exe.symbols['_start']  # 可执行文件部分函数（不属于系统api）的地址，可以直接用，symbols可以被简写为sym
# puts_got = exe.got['puts']  # 系统api在got的地址，利用时需要注意这样的api需要被调用过，此处才有值


def conn():
    if args.REMOTE:
        return remote('addr', 1337)
    else:
        return process([exe.path])


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            debug command 1
            debug command 2
        ''')

    # good luck pwning :)

    # asm('mov eax, 0')
    # disasm('\xb8\x00\x00\x00\x00')
    # asm(shellcode.sh())

    # flat(['a' * 0x70, pop_eax_ret_addr, 0xb, pop_edx_ecx_ebx_ret_addr, 0, 0, bin_sh_addr, int_addr])


    # r.recv()  # 有多少读多少
    # r.recv(5)  # 读取5个字节
    # r.recvline()
    # r.recvuntil('hello')
    # r.send('hello')
    # r.sendline('hello')
    # r.sendlineafter('hello')

    # real_puts_addr = u32(recv_content[:4])

    # libc = LibcSearcher('puts', real_puts_addr)
    # libc_base = real_puts_addr - libc.dump('puts')
    # real_system_addr = libc_base + libc.dump('system')
    # bin_sh_addr = libc_base + libc.dump('str_bin_sh')

    r.interactive()


if __name__ == '__main__':
    main()

```


2020/12/1  
