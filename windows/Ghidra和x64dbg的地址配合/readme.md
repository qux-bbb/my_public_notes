# Ghidra和x64dbg的地址配合

有时候不方便关ASLR，可以用Ghidra和x64dbg的功能配合确定调试的实际地址。  

Ghidra  
右键 选择 Copy Special... -> Imagebase Offset, 假设结果是 6e2e0  

x64dbg  
Ctrl + G, 输入 `:$6e2e0` 回车即可跳转到实际地址。    


2024/10/8  
