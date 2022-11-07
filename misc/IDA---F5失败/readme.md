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

注意：如果失败地址处的指令是调用一个函数，大概率是函数参数个数设置有问题。  


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
如果还有问题，大概率是函数参数个数设置有问题，尝试分析后手动调整参数个数(先复制一份函数声明，改错了还可以改回来)。  
参考链接: https://www.likecs.com/show-1019881.html  


---
2020/5/23  
