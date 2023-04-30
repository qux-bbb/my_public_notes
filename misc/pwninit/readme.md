# pwninit

https://github.com/io12/pwninit  

A tool for automating starting binary exploit challenges  
会把一些通用步骤和exploit的架子写好  

简单命令:  
```sh
# 最基础
./pwninit --bin hello

# 使用自定义模板
./pwninit --bin hello --template-path template_my.py
```


我的模板`template_my.py`:  
```python
#!/usr/bin/env python3


from pwn import *

{bindings}

context.binary = {bin_name}


def conn():
    if args.LOCAL:
        return process({proc_args})
    else:
        return remote("addr", 1337)


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            debug command 1
            debug command 2
        ''')

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
```

生成的`solve.py`:  
```python
# coding:utf8
# python3

from pwn import *

exe = ELF('ymjr')

context.binary = exe 


def conn():
    if args.LOCAL:
        return process([exe.path])
    else:
        return remote('addr', 1337)


def main():
    r = conn()

    if args.G:
        gdb.attach(r, ''' 
            debug command 1
            debug command 2
        ''')

    # good luck pwning :)

    r.interactive()


if __name__ == '__main__':
    main()

```


2020/11/28  
