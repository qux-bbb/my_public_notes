# Ghidra

Ghidra是NSA开发的逆向工具，有反编译和调试功能，类似IDA。  
发音是: `Gee-druh /ˈɡiːdrə/`, 相关链接：  
https://github.com/NationalSecurityAgency/ghidra/wiki/Frequently-asked-questions#how-do-you-pronounce-ghidra  
https://en.wikipedia.org/wiki/Ghidra  

官网: https://www.ghidra-sre.org/  
github地址: https://github.com/NationalSecurityAgency/ghidra  
安装文档: https://www.ghidra-sre.org/InstallationGuide.html  


## 调试相关
Ghidra10.0版本增加了调试器  
GADP: Ghidra Asynchronous Debug Protocol, Ghidra异步调试协议  

据文档介绍IN-VM模式直接调用调试器，会快一点，GADP模式通过协议连接调试器，比IN-VM模式慢，但不会导致数据丢失  

官方说明的一个bug：调试功能现在必须启动之后下断点才能生效，启动之前下的断点断不下来  


## 重置窗口
Ghidra的窗口布局是由CodeBrowser工具控制的。  
如果搞乱了窗口布局，可以删除重新导入：  
1. Tools -> Delete Tool -> CodeBrowser (或者在首页的 `Tool Chest` 下，将CodeBrowser工具(龙图标)右键删除)
2. Tools -> Import Default Tools...，勾选 `defaultTools/CodeBrowser.tool`，点击`OK`

Ghidra的汇编指令窗口是`Listing:<文件名>`  


## 入口函数
IDA有一个入口函数叫 start，Ghidra的入口函数叫 entry  


## 数据类型转换
```
b   Byte -> Word -> DoubleWord -> QuadWord -> Byte
'   Ascii -> String -> Unicode -> Ascii
f   Float -> Double -> Float
c   清除数据类型
```

## 字体调整
`tool options`，在下方的 filter 搜索 `font`，地方比较多，所有都改为 Consola 11  


## 高亮同名变量
默认 鼠标中键 高亮同名变量，可以修改  

## 设置快捷键
方法1：  
Edit -> Tool Options... -> Key Bindings  
然后可以搜索功能设置快捷键  

方法2(简单快捷)：  
光标放在相应功能上，按 F4，此时可以在弹出的窗口内设置相应快捷键  
举例：光标放在一个函数上，右键 -> References -> Find References to xxx，按 F4，设置快捷键为"x"  


## 不同格式复制数据
选择部分数据，右键 -> Copy Special... 然后可以选择不同格式  


## 官方CheatSheet
https://ghidra-sre.org/CheatSheet.html  


---
20190925
