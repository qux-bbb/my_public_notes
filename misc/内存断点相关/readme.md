# 内存断点相关

内存断点原理：设置内存的PAGE_GUARD，发生异常后判断是否为断点地址。  
如果程序调用了VirtualProtect，可能会使内存断点失效。  

OD: 仅可设置读写内存断点  
x64dbg: 可设置读写执行内存断点，但不能指定内存范围  
windbg: 全能  

给windbg举个例子：  
```r
# ba Access Size Address
ba e 1 0xdeadbeef
```
e e (execute)，还可以设置r (read/write)，w (write)，i (i/o)  
1 范围  
0xdeadbeef 地址  