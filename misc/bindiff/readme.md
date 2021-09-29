# bindiff

bindiff可以结合IDA Pro、Binary Ninja、Ghidra比较两个可执行程序的流程差异，可用于版本功能比较或补丁分析，2011年被google收购后转为免费工具。  

官方简介: https://www.zynamics.com/bindiff.html  
下载地址: https://www.zynamics.com/software.html  

以IDA举例，安装时将安装路径选择为IDA目录，如: `D:\sec_tools\IDA_Pro_v7.5_Portable\`  

使用步骤：  
1. 两个程序都提前用IDA打开，保存为压缩数据库，然后关闭
2. IDA打开一个压缩数据库，`Edit->Plugins->BinDiff`，首次使用可点击 `Diff Database...`，打开另一个压缩数据库
3. 在新出现的 `Matched Functions` 窗口，右键选择 `View context in call graphs`，等一段时间即可查看比较结果

查看完毕之后，在关闭时，可以根据提示保存结果，这样再次比较时，可点击 `Load Results...` 做后续操作  


参考链接: https://www.cnblogs.com/lsdb/p/10543411.html  


2021/9/29  
