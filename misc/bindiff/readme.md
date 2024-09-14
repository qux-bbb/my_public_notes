# BinDiff

BinDiff可以结合IDA Pro、Binary Ninja、Ghidra比较两个可执行程序的流程差异，可用于版本功能比较或补丁分析。  
2011年被google收购后转为免费工具。  
2023年在github开源。  

官方简介: https://www.zynamics.com/bindiff.html  
github地址: https://github.com/google/bindiff/  

## IDA使用方法
两个待对比的程序都提前用IDA打开，保存为压缩数据库，然后关闭  
安装BinDiff之后，打开图形化界面，配置一下IDA所在文件夹的路径  
使用BinDiff创建工作空间，加载两个数据库文件，找感兴趣的函数看就可以了  

## Ghidra使用方法
Ghidra当前需要配合BinExport使用  
https://github.com/google/binexport  

在Release页面下载 BinExport_Ghidra-Java.zip 或 ghidra_BinExport.zip  
根据BinExport的README.md安装扩展  

经过操作，可以得到".BinExport"文件，使用BinDiff加载2个".BinExport"文件即可进行比较  


---
2021/9/29  
