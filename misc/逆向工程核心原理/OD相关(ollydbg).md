# OD相关(ollydbg)

基本指令（适用于代码窗口）  
```r
Ctrl + F2   重新开始调试
F7          步入
F8          步过
Ctrl + F9   执行到Return
Alt + F9    回到应用程序领空
空格        编写汇编代码
            创建文本副本，鼠标右键菜单 --> Copy to executable file
Ctrl + G    移动到指定地址，用来查看代码或内存，运行时不可用
F4          执行到光标位置，即直接转到要调试的地址
;           添加注释
            搜索注释，鼠标右键菜单-->Search for --> User-defined comment
:           添加标签(给指定地址添加特定名称)
            搜索标签，鼠标右键菜单-->Search for --> User-defined label
F2          设置或取消断点
F9          运行（若设置了断点，则执行至断点处）
F12         程序死循环时可使程序暂停
*           显示当前EIP（命令指针）位置
-           显示上一个光标的位置
Enter       若光标处有CALL/JMP等指令，则跟踪并显示相关地址（运行时不可用，简单查看函数内容时非常有用）
Ctrl + A    重新分析代码
```

跟踪命令  
```r
Ctrl + F7   反复执行步入(画面显示)
Ctrl + F8   反复执行步过(画面显示)
Ctrl + F11  反复执行步入(画面不显示)
Ctrl + F12  反复执行步过(画面不显示)
F7          停止跟踪
```

字符串检索  
```r
鼠标右键 --> Search for --> All  referenced text strings
```

查看调用的API函数名(可用来下断点)  
```r
鼠标右键 --> Search for  -->  All  intermodular  calls
```

数据窗口编辑快捷键  
```r
Ctrl + E
```

要跳转的地址显示为红色  
```r
打开 Options→Debugging options→CPU
勾选 
Show jump path
Show grayed path if jump is not taken
Show jumps to selected command
```

设置新的EIP  
```r
光标选中地址，右键选择"New origin here"
```

已知API函数名，下断点  
```r
在进入该函数后断下
OD最下面可以执行命令，  `bp API函数名`
在调用该函数时断下
查找模块间调用，下相应的断点(相应的命令：bpx API函数名)
```

条件断点  
```r
Shift + F2
举例:
bp  401476  eax==040000
bp  CreateFileA  [STRING [esp+4]]=="c:\1212.txt"
bp  CreateFileW  [UNICODE [esp+4]]=="c:\1212.txt"
```


2019/1/9  
