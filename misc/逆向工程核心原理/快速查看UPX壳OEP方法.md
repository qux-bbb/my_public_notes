# 快速查看UPX壳OEP方法

UPX压缩器的特征之一是，其EP代码被包含在PUSHAD/POPAD指令之间。并且，跳转到OEP代码的JMP指令紧接着出现在POPAD指令之后。只要在JMP指令处设置好断点，运行后就能找到OEP。  

执行完 PUSHAD 后，查看ESP值，右键Follow in dump，  
设置硬件断点，右键 Breakpoint→Hardware，onaccess→Byte  
F9运行，其下方不远处就是跳转到OEP的JMP指令  

硬件断点  
访问相应的地址，就会触发的断点，最多可以设置4个  


2019/1/9  
