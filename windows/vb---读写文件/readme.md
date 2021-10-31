# vb---读写文件

keywords: vb 读文件 写文件  

## 读文件  
```vb
Dim ss As String, s() As String
Open "1.txt" For Binary As #1
ss = Input(LOF(1), #1)
Close #1
```


## 写文件  
```vb
Private Sub button1_Click()
'以输出方式打开new.txt这里有路径问题参见 "c:\new.txt"就是指输出到哪个文件
'for output是指打开方式为输出方式 此方式如果该文件存在则覆盖
'as #1 打开文件需要占用工作区的，所以以1号工作区打开该文件
Open "C:\NEW.TXT" For Output As #1
'在一号文件区打开的文件里写入abc
Print #1, text1.text
'关闭一号工作区
Close #1
End Sub
```


原链接: https://zhidao.baidu.com/question/53254291.html  


2020/6/1  
