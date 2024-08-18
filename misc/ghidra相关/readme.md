# Ghidra

Ghidra是NSA开发的逆向工具，有反编译和调试功能，类似IDA。  

官网: https://www.ghidra-sre.org/  
github地址: https://github.com/NationalSecurityAgency/ghidra  
安装流程: https://github.com/NationalSecurityAgency/ghidra#install  


## 发音
发音是: `Gee-druh /ˈɡiːdrə/`, 相关链接：  
https://github.com/NationalSecurityAgency/ghidra/wiki/Frequently-asked-questions#how-do-you-pronounce-ghidra  
https://en.wikipedia.org/wiki/Ghidra  


## 含义
最初含义是日本的田中友幸幻想的怪兽(哥斯拉也由他创造)，NSA的扩展解释是：  
```r
Generic
Hexidecimal
Integrated
Decompiling
Reverse-engineering
Architecture
```
https://en.wikipedia.org/wiki/Tomoyuki_Tanaka  
https://github.com/NationalSecurityAgency/ghidra/wiki/files/blackhat2019.pdf  
https://www.youtube.com/watch?v=kx2xp7IQNSc  


## Sleigh
发音是: `slay /sleɪ/`, 原意是雪橇，在Ghidra里Sleigh是一种基于规则的语言和引擎，用于描述和解码处理器指令集。  
通过使用Sleigh，Ghidra可以支持各种不同的处理器体系结构和指令集。  


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


## 栈字符串
Ghidra现在不能很好地处理栈字符串，有2个脚本可以添加相关注释，第1个效果还可以，第2个会猜测所有匹配情况效果不好  
https://github.com/0x6d696368/ghidra_scripts/blob/master/SimpleStackStrings.md  
https://github.com/0x6d696368/ghidra_scripts/blob/master/SearchSimpleStackStrings.md  


## 中文字符串
在数据开头，鼠标右键 -> Data -> Default Settings.../Settings... -> Charset，改为"GBK"或其他合适的编码  
Default Settings 会改所有默认的设置，Settings 只改当前数据的设置  


## 字体调整
`tool options`，在下方的 filter 搜索 `font`，地方比较多，所有都改为 Consola 11  
也可以创建新的Theme，导出之后修改font相关配置并保存，再导入修改后的Theme，还是有点麻烦  


## 高亮同名变量
默认 鼠标中键 高亮同名变量，可以修改  
Edit -> Tool Options -> Listing Fields -> Cursor Text Highlight -> Mouse Button To Activate, 可以修改为鼠标的左中右键  
Edit -> Tool Options -> Listing Fields -> Selection Colors -> Highlight Color, 可以修改高亮颜色  


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
