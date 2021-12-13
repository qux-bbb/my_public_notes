# 2种异常处理

SEH: Structured Exception Handling 结构化异常处理  
VEH: Vectored Exception Handling 向量化异常处理  

2个用来添加异常处理的api：  
SetUnHandledExceptionFilter  
AddVectoredExceptionHandler  

SEH安装:  
```r
assume fs:nothing
    push    offset SEHandler
    push    fs:[0]
    mov     fs:[0],esp
```

SEH卸载:  
```r
mov     esp,dword ptr fs:[0]
pop     dword ptr fs:[0]
```


来源：《加密与解密》  

2020/9/14  
