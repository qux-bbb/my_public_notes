# ROPgadget

keywords: ROP pwn peda  

用于寻找 ROP 片段，构建 ROP 链  
https://github.com/JonathanSalwan/ROPgadget  

peda 里已经集成了该工具  
https://github.com/longld/peda  

简单使用：  
```r
# 找指令 pop 或 ret
ROPgadget --binary rop  --only 'pop|ret' | grep 'eax'

# 找字符串
ROPgadget --binary rop  --string '/bin/sh'
```


2020/11/27  
