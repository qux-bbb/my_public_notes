# 保存内存用于取证

keywords: forensic  

内存是易变性数据，这里列一些用来获取内存数据的工具，保存的内存数据可以用Volatility分析。  

## `物理机内存`

`WinPmem`  
https://github.com/Velocidex/WinPmem  
命令行工具，开源  
```r
# 使用举例，完成后会生成physmem.raw
winpmem_mini_x64.exe physmem.raw
```

`FTK Imager`  
https://www.exterro.com/ftk-imager  
图形化界面，不开源，下载需要填写表格  
File -> Capture Memory, 等待完成即可  


## `虚拟机内存`
创建快照即可，会生成vmem文件，可用于取证  


---
参考链接: https://www.varonis.com/blog/memory-forensics  


---
2022/6/27  
