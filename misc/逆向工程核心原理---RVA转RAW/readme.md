# 逆向工程核心原理---RVA转RAW

RVA, Relative Virtual Address, 相对虚拟地址  
RAW, 在文件中的偏移(File Offset)  

公式  
```r
RAW - PointerToRawData = RVA - VirtualAddress
RAW = RVA - VirtualAddress + PointerToRawData
```


2019/1/15  
