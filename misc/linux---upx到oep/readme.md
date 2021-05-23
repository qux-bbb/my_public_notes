# linux---upx到oep
linux的upx壳和windows不一样，运行到oep，要结合指令特征操作。  


## 32位程序
可以用esp定律，但断点会被多次触发，所以要注意观察。  
开始执行几条指令后会执行 `pusha`，  
到oep前会执行 `popa` `retn`, 这2条指令是动态填充的，所以不能提前下断点  

使用IDA远程调试，  
在执行 `pusha` 之后，复制esp寄存器的值，跳转到该值对应的地址后，右键设置断点：硬件读写断点  
F9运行，会断下多次，观察到断点所处位置的指令是 `popa` `retn` 时，F8执行完 `retn`，即可到达oep  

## 64位程序
这个好像不能用esp定律  

同样使用IDA远程调试，  
中间调试的时候如果遇到比较复杂的跳转，往下翻，找到接近return的位置，F4直接运行到那个位置，然后继续调试  
最后会通过syscall的方式调用 sys_mmap sys_close sys_munmap 函数，然后return到oep即可  


2021/4/13  
