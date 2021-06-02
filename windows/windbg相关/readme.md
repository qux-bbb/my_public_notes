# windbg相关

WinDbg 是包含在 Windows 调试工具中的内核模式和用户模式调试器。  

- - - -
## 手册
debugger.chm  
windbg.chm  
用everthing搜一下就好了  
也可以打开windbg，F1 或者点帮助  
  
手册一开始的 `Getting Started with Windows Debugging` 真的很好  

- - - -
## 简单的快捷键
F5: Go  
F11 or F8: Step Into  
F10: Step Over  
Ctrl+F10 or F7: Run to Cursor  

- - - -
## WinDbg基本指令(来源: 逆向工程)

| 指 令 | 说 明             | 应 用                                          |
| ----- | ----------------- | ---------------------------------------------- |
| u     | Unassemble        | u: 显示下一条指令                              |
|       |                   | u address: 显示指定地址的指令                  |
|       |                   | u L10: 显示10行指令(L和数字之间没有空格)       |
|       |                   | u address L10: 显示指定地址的10行指令          |
|       |                   | ub: 显示上一条指令                             |
| t     | Trace(F11)        | Step Into                                      |
| p     | Pass(F10)         | Step Over                                      |
| g     | Go(Run)           | g: 运行                                        |
|       |                   | g address: 运行到指定的地址                    |
| d     | Dump              | d address: 显示地址内容(可用L指定显示行数)     |
|       |                   | db address: byte                               |
|       |                   | dd address: dword                              |
|       |                   | dq address: qword                              |
| r     | Register          | r: 显示寄存器                                  |
|       |                   | r register: 仅显示指定寄存器                   |
| bp    | Break Point       | bp: 设置断点                                   |
|       |                   | bl: 显示断点列表                               |
|       |                   | bc: BP Clear (删除断点)                        |
| lm    | Loaded Module     | lm: 显示被调试进程中加载的模块 (库)            |
| dt    | Display Type      | dt struct name: 显示结构体成员                 |
|       |                   | dt struct name address: 映射地址到结构体并显示 |
| !dh   | Display PE Header | !dh loaded address:                            |
|       |                   | !dh module name: 显示进程PE文件头              |


以'!'开头的命令为扩展命令  

- - - -
## 实践
```
# 输出ecx指向地址处的ascii字符串
da ecx

# 输出ecx指向地址处的unicode字符串
du ecx

# 给某个函数下断点，不区分大小写  
bp KERNELBASE!CreateProcessW

# 给某个函数下未加载模块断点，也不区分大小写  
bu Shell32!ShellexecuteA

# 触发断点时执行"du eax"命令
bp kernelbase!CreateFileW "du ecx"

# 达到一定次数才停下来
bp kernelbase!CreateFileW ".if(@$t0<42f){.printf \"hits=%d\",@$t0;r @$t0=@$t0+1;gc;};.else{}"

# 内存断点，比硬件断点更强大
# e 执行时断下 1 内存大小 0xdeadbeef 地址
ba e 1 0xdeadbeef

# 列出当前断点
bl

# 删除编号为1的断点
bc 1

# 显示peb结构体
!peb

# 修改内存将BeingDebugged标志位置为0
# peb起始位置为eb8000，BeingDebugged为+0x2
ed eb8002 0

# 堆栈回溯，显示传递给堆栈跟踪中每个函数的前三个参数
kb

# 堆栈回溯，显示帧指针省略（FPO）信息。在基于x86的处理器上，显示还包括调用约定信息
kv

# 查看入口点地址(EP)，也可以通过查看进程PE文件头的`address of entry point`的值来获取EP
# $exentry 是一个伪寄存器，总是等于EP
r $exentry

# 直接到达入口点
g @$exentry

# 显示进程PE文件头
!dh WOW64Test_x64

# 执行到RVA(相对地址)
g WOW64Test_x64 + 142C

# 显示TEB结构体成员
dt _TEB

# 详细列出请求地址的页堆信息，包括此地址与整页堆块的关系的完整详细信息，例如，此地址是否为页堆的一部分，其在块中的偏移量，以及块是否被分配或释放。只要可用，就包括堆栈跟踪
!heap -p -a eax

# 线程相关
# 当前线程
~.
# 所有线程
~*
# 造成异常的线程
~#
# 切换到1线程
~1s

# 清屏
.cls
```
- - - -
## 搜索内存举例
```
# 下面3个都是搜索 "Hello"
0:000> s 0012ff40 L20 'H' 'e' 'l' 'l' 'o' 
0:000> s 0012ff40 L20 48 65 6c 6c 6f 
0:000> s -a 0012ff40 L20 "Hello" 
```
从 0012ff40 开始，搜索 20 行，搜的目标是 ascii 形式的 "Hello"  

- - - -
## 设置symbol file path
File-->Settings-->Debugging settings-->Symbol path  
```sh
C:\Symbols;SRV*C:\Symbols*http://msdl.microsoft.com/downloads/symbols
```
不行的话，可以试试 https  
如果不想让windbg去网站获取pdb文件，直接把path设成本地的文件夹就好了（因为有时候太卡了，）  

- - - -
## 找不到依赖的文件
可以在打开程序时设置 `Start directory`  

- - - -
## 官方学习资料
https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg  

- - - -
2018/9/29  
2021/6/2  
