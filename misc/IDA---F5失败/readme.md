# IDA---F5失败

反编译失败的官方解决办法：  
https://www.hex-rays.com/products/decompiler/manual/failures.shtml  

下面记一些解决示例  


## `positive sp value`
错误信息：  
```r
Decompilation failure:
40103C: positive sp value has been found

Please refer to the manual to find appropriate actions
```

点该地址的上一条指令，这里是 00401039，`Alt + k`，修改为 0，F5 即可  
```r
...
.text:00401039 add     esp, 28h              ; Add
.text:0040103C mov     esp, ebp
.text:0040103E pop     ebp
...
```


## `call analysis failed`
错误信息：  
```r
Decompilation failure:
4022CB: call analysis failed
```

跳到相应地址，进入可能有问题的函数，这里是 sub_402700，F5，点击函数名，右键 `Set item type...` -> `OK`，处理之后即可做后续操作  
```r
.text:004022CB                 call    sub_402700
.text:004022D0                 call    sub_403070
```

---
2020/5/23  
