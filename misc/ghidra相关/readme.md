# Ghidra

Ghidra是NSA开发的逆向平台，有反编译和调试功能，类似IDA。  
发音大概是: `[giˈdræ]`, 只是前半部分不太确定，相关链接: https://bbs.pediy.com/thread-249900.htm  

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


---
20190925
