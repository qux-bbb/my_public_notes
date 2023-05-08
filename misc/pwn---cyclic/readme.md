# pwn---cyclic

keywords: 随机字符串  

生成可用于定位信息的字符串，pwntools和pwndbg都有的功能。  
配合gdb使用，gdb的输出信息为hex/str，用于确定栈溢出偏移、异常位置等信息。  

生成指定长度字符串  
```bash
cyclic 100
```
执行后确定异常位置  
```bash
cyclic -l hex/str
```

默认是linux/i386，其他系统需要使用 -c 指定  


2019/10/27  
