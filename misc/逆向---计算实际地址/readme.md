# 逆向---计算实际地址

keywords: 真实地址  

使用场景：  
需要根据静态地址找到运行程序的实际地址，但遇到以下2种情况：  
1. 不能关闭ASLR的正常可执行程序
2. 动态库如dll、so程序

原理：  
对于一个段，实际地址和静态地址的偏移是固定的  

例子：  
```r
# .text段静态起始地址
text_static_start_addr = 0x140001000
# .text段实际起始地址
text_real_start_addr = 0x00007FF636051000
# 要下断点的静态地址
bp_static_addr = 0x140001017
# 要下断点的实际地址
bp_real_addr = text_real_start_addr - text_static_start_addr + bp_static_addr
print(hex(bp_real_addr))
# 0x7ff636051017
```


2025/2/20  
