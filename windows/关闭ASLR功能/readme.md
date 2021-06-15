# 关闭ASLR功能

ASLR功能和一个标志位有关：  
IMAGE_NT_HEADERS -> IMAGE_OPTIONAL_HEADER -> DLL Characteristics -> IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE(40)标志  

将该标志置0即可删除ASLR功能，也就是修改40为00  

可使用工具：  
1. CFF Explorer, 取消勾选"DLL can move"即可
2. XPEViewer, 取消勾选"DYNAMIC_BASE"即可

不同工具只是叫法不一样，指的是一个东西  


2019/6/19  
2021/6/15  
