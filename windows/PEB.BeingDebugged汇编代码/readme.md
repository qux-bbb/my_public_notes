# PEB.BeingDebugged汇编代码

```r
mov eax, dword ptr fs:[30]
cmp byte ptr ds:[eax+2],1
```
如果等于1，就是处于调试状态  


来自: 逆向工程核心原理  


2019/6/29  
