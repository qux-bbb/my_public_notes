## radare2
A free/libre toolchain for easing several low level tasks like forensics, software reverse engineering, exploiting, debugging, ...  

It is composed by a bunch of libraries (which are extended with plugins) and programs that can be automated with almost any programming language.  

简而言之，逆向工具集合  


## r2pipe
The simplest and most effective way to script radare2, which consists in 1 method API that takes a string representing the r2 command to run and returns the output as a string.  

简而言之，用脚本控制 radare2 的方法  


## Cutter
Cutter is the official UI for radare2 for Linux, macOS and Windows, it's written in C++ and uses the Qt.  

简而言之，radare2 的 UI  
感觉反编译还不错，可以用r2dec和Ghidra，各有特色  
可以通过拖拽窗口自定义视图，很好  
可以通过x64dbgcutter插件和x64dbg符号转换：https://github.com/yossizap/x64dbgcutter  