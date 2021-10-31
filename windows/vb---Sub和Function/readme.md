# vb---Sub和Function

Sub: 子过程 无返回值  
Function: 函数过程 有返回值  

Function示例  
```vb
'最后必须给函数名赋值，才能有返回值
Function hello(a)
    Dim b
    b = a + 2
    hello = b
End Function

Msgbox cstr(hello(1))
```


2019/6/24  
