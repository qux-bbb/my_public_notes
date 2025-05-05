# Ghidra和x64dbg的地址配合

keywords: 断点 真实地址

有时候不方便关ASLR，可以用Ghidra和x64dbg的功能配合确定调试的实际地址。  

Ghidra  
右键 选择 Copy Special... -> Imagebase Offset，这样得到的是Relative Virtual Address, 相对虚拟地址  
假设结果是 6e2e0  

x64dbg  
x64dbg的跳转支持这样的格式 `:$RVA`  
所以Ctrl + G, 输入 `:$6e2e0` 回车即可跳转到实际地址  


2024/10/8  
