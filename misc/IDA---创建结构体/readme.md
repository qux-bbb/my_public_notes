# IDA---创建结构体

创建结构体并应用到相应数据上，可以更好理解数据含义。  

## 相关操作
在Structures窗口，在所有结构体后按 `Ins` 即可开始创建结构体，一些操作如下：  
```r
按键    : 解释
-----------------------------------------------------
Ins/Del : create/delete structure
D/A/*   : create structure member (data/ascii/array)
N       : rename structure or structure member
U       : delete structure member
```

一个简单例子：  
```r
00000000 person          struc ; (sizeof=0x11, mappedto_144)
00000000 name            xmmword ?               ; char
00000010 age             db ?                    ; base 10
00000011 person          ends
```
在 ends 后按 `D/A/*` 可以增加成员，切换数据类型，D表示数据，A表示字符串，*表示数组  
如果没有想要的数据类型，可以 Options->Setup data types 设置更多的数据类型  
在 db 右键， Field type 可以选择成员类型  
`N` 可以设置成员名称  


## 应用到数据
找到想要设置结构体的数据，不需要全部选中，只需要光标在数据开始位置即可，  
右键->Structure->结构体名称, 或者使用快捷键 `Alt+Q`, 即可将数据以结构体形式显示  


---
2022/1/16  
