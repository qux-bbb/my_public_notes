用xpreviewer可以看到ImageBase、BaseOfCode、代码段的PointerToRawData，然后代码地址和文件偏移是下面的关系：  

`the_code_addr = the_file_offset - PointerToRawData + ImageBase + BaseOfCode`  
hex(0x10710-0x400+0x400000+0x1000) = 0x411310  
`the_file_offset = the_code_addr – ImageBase – BaseOfCode + PointerToRawData`  
hex(0x411310-0x400000-0x1000+0x400) = 0x10710  
