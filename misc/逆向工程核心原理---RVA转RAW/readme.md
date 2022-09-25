# 逆向工程核心原理---RVA转RAW

ImageBase, 基址, 如: 0x00400000  
VA, Virtual Address, 虚拟地址, 如: 0x00418ABC  
RVA, Relative Virtual Address, 相对虚拟地址, 如: 0x00018ABC  
RAW, 在文件中的偏移(File Offset), 如: 0x000170BC  
section.PointerToRawData, 节区起始地址在文件中的偏移, 如: 0x00011600
section.VirtualAddress, 节区起始地址在内存中的相对地址, 如: 0x00013000

公式  
```r
VA = ImageBase + RVA
RAW - section.PointerToRawData = RVA - section.VirtualAddress
```

通过VA计算RAW，也就是在IDA中看到的地址换算成在文件中的偏移  
```r
RVA = VA - ImageBase
RAW = RVA - section.VirtualAddress + section.PointerToRawData

0x00418ABC - 0x00400000 = 0x00018ABC
0x00018ABC - 0x00013000 + 0x00011600 = 0x000170BC
```


2019/1/15  
