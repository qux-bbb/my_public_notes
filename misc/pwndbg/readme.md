# pwndbg

pwndbg（/poʊndbæg/）是一个GDB插件，它可以降低使用GDB进行调试的难度，提供硬件黑客、逆向工程师和漏洞开发人员所需的功能。  

官网: https://pwndbg.re/  
github地址: https://github.com/pwndbg/pwndbg  

安装：  
```r
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

pwndbg和peda冲突，可以在 `~/.gdbinit` 选择启用哪个，不想用哪个就把相应的行用 `#` 注释一下  

一些命令：  
```r
hexdump
以hexdump形式查看内存，可指定地址和长度，默认是$sp的64个字节，示例: `hexdump 0x62300000 0x100`

context
在查看内存等操作后，像调试时那样展示当前寄存器值、上下文指令、栈信息、线程信息
```


2022/6/26  
