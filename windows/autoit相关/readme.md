# autoit相关

## 0x0 简介
https://www.autoitscript.com/  

自动执行一些动作的工具，主要被用来做安装程序过程自动化。  

创建一个 hello.au3 文件，然后右键编辑，点 Help，看教程就可以了  
Tutorials 很好  

## 0x1 示例
最简单的 hello world 弹窗  
```r
#include <MsgBoxConstants.au3>

MsgBox($MB_OK, "Tutorial", "Hello World!")
```

英文环境下的notepad操作  
```r
Run("notepad.exe")
WinWaitActive("Untitled - Notepad")
Send("This is some text.")
WinClose("Untitled - Notepad")
WinWaitActive("Notepad", "Save")
;WinWaitActive("Notepad", "Do you want to save") ; When running under Windows XP
Send("!n") 
```
这里的 `!n` 指的是不保存的选项  


AutoIt Window Info 用于获取窗口信息，和 spy++ 类似  


自动化装 winzip  
```r
; Run the winzip installer
Run("winzip90.exe")

; Initial Setup Screen
WinWaitActive("WinZip� 9.0 SR-1 Setup", "&Setup")
Send("!s")

; Install location
WinWaitActive("WinZip Setup", "into the following folder")
Send("{ENTER}")

; Features overview
WinWaitActive("WinZip Setup", "WinZip features include")
Send("!n")

; License agreement
WinWaitActive("License Agreement")
Send("!y")

; Quick start
WinWaitActive("WinZip Setup", "Quick Start Guide")
Send("!n")

; Choose interface
WinWaitActive("WinZip Setup", "switch between the two interfaces")
Send("!c")
Send("!n")

; Installation type (custom/express)
WinWaitActive("WinZip Setup", "&Express setup (recommended)")
Send("!e")
Send("!n")

; Select file associations
WinWaitActive("WinZip Setup", "WinZip needs to associate itself with your archives")
Send("!n")

; Completed installation screen
WinWaitActive("WinZip Setup", "Thank you for installing this evaluation version")
Send("{ENTER}")

; Wait for winzip to load then close it
WinWaitActive("WinZip (Evaluation Version)")
WinClose("WinZip (Evaluation Version)")

```

核心就是 Alt+首字母，或者 {ENTER}  

## 0x2 调试相关
autoit没有断点这样的概念，没法中途停下来查看变量，只能自己插入相关调试信息，可以用弹窗来暂停，Return来停止  

简单示例  
```r
#include <MsgBoxConstants.au3>
#include <Debug.au3>

_DebugSetup("Check Excel")
For $i = 1 To 4
   WinActivate("Microsoft Excel")
   ; interact with Excel
   Send("{Down}")
   _DebugOut($i)
   _DebugReportVar("i value", $i)
   If $i == 3 Then
	  Return
   EndIf
   MsgBox($MB_OK, "Tutorial", "Hello World!")
   _DebugOut("Moved Mouse Down")
Next

```


## 0x3 反编译相关
autoit编译生成的exe可以恢复到autoit源码，使用如下工具：  
https://github.com/JacobPimental/exe2aut/  


---
2020/7/15  
