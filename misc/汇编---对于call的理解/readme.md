# 汇编---对于call的理解

使用objdump将汇编指令搞出来:  
`objdump -d wow > wow.objdump`  

查看wow.objdump文件，有一个call行如下:  
```
400807:       e8 da fe ff ff          callq  4006e6 <welcome>
```
`400807`: 该指令的地址  
`e8 da fe ff ff`: 汇编码  
`callq  4006e6 <welcome>`: 翻译出来的指令  


是如何将汇编码转成汇编指令的呢？  
e8是call指令的代码，dafeffff是小端序，转成大端序之后为fffffeda  

call的地址应该怎么算呢？  
地址 = 当前指令位置 + 该指令长度 + 相对地址  
就是上面的公式，套在该例子中就是:  
address = 0x400807 + 5 + 0xfffffeda = 0x1004006e6  
有溢出，所以最后结果是0x4006e6，该地址对应的正好是welcome函数的地址，所以objdump把指令翻译成上面的样子  

这样就可以理解一种花指令的写法:  
`e8 00 00 00 00`  
也就是执行该指令，接着执行下一条就好了  


2018/10/21  
