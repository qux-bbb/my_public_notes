keywords: 无限循环 死循环  

无限循环(死循环)指令（适用于Intel指令集）  

EB FE  
跳转到当前位置  

举例：  
```
00401824 EB FE      JMP SHORT 00401824
```

原理：  
Intel手册相关内容  
```
Opcode      Instruction     Description
EB cb       JMP rel8        Jump short, RIP = RIP + 8-bit displacement sign extended to 64-bits
```
从IA-32用户手册上可知，操作码0xEB是近距离（Short Distance）JMP指令，带有1个字节大小的值，该值为Signed Value（有符号数），指的是“与Next EIP的相对距离”，计算时有如下公式：  
``` 
    Jump Address=Next EIP(401826)+0xFE(-2)=401824  
```


来自《逆向工程核心原理》  
