# 调试器---镜像劫持

如果 A 程序 启动了 B 程序，而且设定了一些东西，这个时候想调试 B 程序，可以用镜像劫持  

打开注册表编辑器并转到：  
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options
```

在该项下新建项，名字写成想要调试的程序，比如 `powershell.exe`，  
在新建的项下新建字符串类型的项，名称设置为 `Debugger`，值设置为调试器的绝对路径  

这样设置之后，当 powershell.exe 被调用时，调试器就会自动附加并断下  
举个例子: powershell.reg  
```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\powershell.exe]
"Debugger"="C:\\Users\\q\\Desktop\\x64dbg\\release\\x32\\x32dbg.exe"
```


注：服务程序这样设置不会生效，会弹窗提示无法启动服务，现在只能想到把对应位置改成无限循环，然后windbg去附加的方法（不是内核调试器的好像都不行）  


参考链接：https://www.mobibrw.com/2015/2722  

感谢 yg  


2020/6/2  
