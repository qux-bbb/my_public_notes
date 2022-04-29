# 计算PE文件实际大小

部分PE文件会在文件尾附加额外数据  
可以通过PE节区数据计算原PE文件大小: 最后一个节区的PointerToRawData + SizeOfRawData  
后面还有数据就是额外的了  

原链接: https://stackoverflow.com/a/33278940/7164926  


2022/4/29  
