# IDA---F5失败

反编译失败的官方解决办法：  
https://www.hex-rays.com/products/decompiler/manual/failures.shtml  


这里简单记录一个 `positive sp value` 的问题，错误信息：  
```
Decompilation failure:
40103C: positive sp value has been found

Please refer to the manual to find appropriate actions
```

点一下这个地址的上一条指令，这里是 00401039，`Alt + k`，修改为 0，F5 就可以了  
```
...
.text:00401039 add     esp, 28h              ; Add
.text:0040103C mov     esp, ebp
.text:0040103E pop     ebp
...
```


2020/5/23  
