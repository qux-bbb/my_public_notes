# linux---系统调用

预先设置对应寄存器的值，再执行系统调用指令，可以进行系统调用  

虽然不太准确，但可以这么理解：  
32 位系统的系统调用指令为 `int 80`，64 位系统的系统调用指令为 `syscall`  

具体看这个文件: [linux系统调用表.xlsx](./files/linux系统调用表.xlsx)  
还有这个网站: https://syscall.sh/  


参考链接：  
1. https://stackoverflow.com/questions/12806584/what-is-better-int-0x80-or-syscall-in-32-bit-code-on-linux  
2. https://www.dazhuanlan.com/2019/12/16/5df78b6c54f05/  


2020/07/02  
