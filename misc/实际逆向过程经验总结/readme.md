# 实际逆向过程经验总结

总体思路是优先收集信息，再投入时间逆向调试。因为后者会花很多时间。  
如果是分析比较出名的家族之类的样本，可以先搜一下别人的分析，增长见识，减少踩坑。  
遇到自己解决不了的难点就多搜，世界这么大，你的难点可能别人已经遇到并且解决了。  

获取hash值，去 https://www.virustotal.com 查一下，有记录的话，可以观察整理一下，有个印象，然后继续  

1. 使用file命令查看文件类型
2. 使用strings命令过滤敏感字符串，比如pdb字符串等

--  

如果是PE，继续如下步骤：  
静态：  
1. 在虚拟机中改成对应的后缀，看看图标，右键看看属性
2. 使用DIE/ExeInfoPE/PEiD识别是否加壳，PEiD还可以用Krypto ANALyzer插件扫描已知加密算法特征，将检测到的信息导出为IDC脚本供IDA使用
3. 使用xpeviewer从上往下点一遍，注意导入表（可根据导入表猜测功能），节，资源，Resource Hacker可以看程序图标
4. IDA打开，再看一下IDA分析出的字符串

动态：  
1. 放虚拟机里，用火绒剑、PCHunter监控，管理员权限打开程序，看一下对应进程组的信息，读写文件，读写注册表，网络交互之类的信息
2. 收集运行过程生成的文件，留待后续分析

如果DIE/ExeInfoPE/PEiD检测到不是普通的PE，比如autoit、vb，可通过相应工具（exe2autoit、
vb decompiler）处理之后再分析  

IDA和其他动态调试器结合，定位一下动态看到的行为  

逆向没有思路的时候，一个方法是死磕汇编代码，另一个感觉更好的方法是梳理流程，注意流程中的数据形式、细节

调试技巧见 [逆向---调试技巧](../逆向---调试技巧/readme.md)  
有什么地方暂时不清楚或者发现了什么问题，用自己的符号标记，然后慢慢解决  
多记多猜多验证  


20201206  