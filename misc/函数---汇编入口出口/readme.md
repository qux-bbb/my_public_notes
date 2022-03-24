# 函数---汇编入口出口

典型的函数入口出口汇编指令特征  

函数入口:  
```r
.text:00401BD0 push    ebp
.text:00401BD1 mov     ebp, esp
```

函数出口:  
```r
.text:00401DD9 mov     esp, ebp
.text:00401DDB pop     ebp
```


2020/3/12  
