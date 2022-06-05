# word---宏-写文件

keywords: 宏 自动 写文件  

创建文档，另存为 docm 格式  

创建宏，在 Project -> ThisDocument 里写以下内容，保存即可  

```vb
Sub Document_Open()
'以输出方式打开new.txt这里有路径问题参见 "c:\new.txt"就是指输出到哪个文件
'for output是指打开方式为输出方式 此方式如果该文件存在则覆盖
'as #1 打开文件需要占用工作区的，所以以1号工作区打开该文件
Open "hello" For Output As #1
'在一号文件区打开的文件里写入abc
Print #1, "world"
'关闭一号工作区
Close #1

End Sub
```


2020/11/23  
