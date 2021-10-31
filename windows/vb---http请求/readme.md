# vb---http请求

```vb
Option Explicit
 
Private Sub Form_Load()
    Dim bytData() As Byte
    Dim objHTTP As Object
     
    Set objHTTP = CreateObject("MSXML2.XMLHTTP")
    objHTTP.open "GET", "https://www.baidu.com", False
    objHTTP.send
    If objHTTP.Status = 200 Then
        bytData = objHTTP.responseBody
        Debug.Print StrConv(bytData, vbUnicode)
    End If
    Set objHTTP = Nothing
End Sub
```

原链接: https://bbs.csdn.net/topics/340031850?list=669793  


2020/3/11  
