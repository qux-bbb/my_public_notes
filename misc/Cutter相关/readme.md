## 简介
Cutter is the official UI for radare2 for Linux, macOS and Windows, it's written in C++ and uses the Qt.  

官网: https://cutter.re/  
github地址: https://github.com/rizinorg/cutter/  

简而言之，radare2 的 UI  
感觉反编译还不错，可以用r2dec和Ghidra，各有特色  
调试体验不太好  
可以通过拖拽窗口自定义视图，很好  
可以通过x64dbgcutter插件和x64dbg符号转换  

支持多平台: Windows/Linux/macOS  


## x64dbgcutter
https://github.com/yossizap/x64dbgcutter  
可以在cutter里导入导出x64dbg符号文件，效果，还行吧，能用  

这是我知道的Cutter的第一个插件，安装方法：  
1. Edit -> Preferences -> Plugins，然后可以在窗口上方看到插件路径，点击进入  
2. 下载 x64dbgcutter.py，放到插件路径下的python目录下

使用方法：  
Windows -> Plugins，选择插件执行即可  


20201210  