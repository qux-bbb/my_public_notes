在vb中可以用GetSpecialFolder获取特定文件夹路径，有以下3种参数可用：  
```
0 windows文件夹，举例：C:\Windows
1 system文件夹，举例：C:\Windows\System32
2 temp文件夹，举例：C:\Users\hello\AppData\Local\Temp
```

下面是获取temp文件夹路径的示例：  
```vb
Set FSO = CreateObject("Scripting.FileSystemObject")
TempPath = FSO.GetSpecialFolder(2)
MsgBox TempPath
```


参考链接：https://blog.csdn.net/limlimlim/article/details/8132447  