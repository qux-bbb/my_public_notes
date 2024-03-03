# gdb基本使用方法

keywords: gdb相关  

gdb, GNU Debugger, linux下调试程序  

官网: https://www.sourceware.org/gdb/  
官方文档: https://www.sourceware.org/gdb/documentation/  

```r
gdb             # 进入gdb
gdb 程序名      # 直接加载程序

进入gdb之后
file 程序名     # 加载程序
disas main      # 显示main函数的汇编代码，其他函数类似 全 disassemble
disas $rip      # 显示当前地址附近的汇编代码
disas 0x012345  # 显示某个地址处的汇编代码

b *0x08048bee   # 对某个地址下断点，退出之后所有断点消失 全 break
b 函数名        # 对某个函数下断点
i b	            # 查看所有断点 全 info breakpoints
d 4             # 删除标号为4的断点 全 delete
d               # 删除所有断点
disable 4       # 禁用断点

start           # 启动被调试的程序，在主过程开始时暂停
r               # 运行被调试的程序 全 run
c               # 继续执行被调试的程序 全 continue
s               # 步入，源代码级别 全 step
si              # 步入，指令级别 全 stepi (step instruction)
n               # 步过，源代码级别 全 next
ni              # 步过，指令级别 全 nexti
finish          # 执行完当前函数并返回

set args 1122   # 设置可执行文件需要的参数
set args "`cat a.txt`"  # 设置可执行文件需要的参数，适用于有时参数不能显示的情况
set $eip = 0x401008       # 设置eip寄存器的值
set *((char*)($ebp-0xc)) = 1    # 修改某内存的值
x /x $ebp-0xc           # 查看某内存位置的值 (Examine memory)
x /3xw 0xffffd25c       # 16进制方式按word查看3个word长度的内容
x /s 0xffffd25c         # 以字符串方式查看指定地址的内容
x /4i 0xffffd3fc        # 查看4条指令
i func                  # 显示所有函数名，可以加正则表达式 全 info function
i r                     # 查看所有寄存器的值 全 info registers	
p $eip                  # 输出寄存器值 全 print
p *0x400123@12          # 输出长度12的某个地址处的数组

bt                      # 栈回溯 全 backtrace
i threads               # 查看所有线程 全 info threads
thread 2                # 切换到线程2
thread apply 2 bt       # 对线程2执行bt命令
thread apply 2 3 bt       # 对线程2、3执行bt命令
thread apply all bt     # 对所有线程执行bt命令

q   # 退出调试 全 quit

set follow-fork-mode parent # 设置有fork进程时也调试父进程
```

参考链接：  
1. GDB十分钟教程 http://blog.csdn.net/liigo/article/details/582231/
2. GDB查看、修改内存 http://jiangyingji1.blog.163.com/blog/static/171630340201122283017414/
3. chatgpt

&&&&&&& 有时候修改eflags不生效，比较奇怪  


2016/11/9  
2021/3/2  
