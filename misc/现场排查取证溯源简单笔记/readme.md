# 现场排查取证溯源简单笔记

自己找资料看的，不确定有没有用  
首先和客户确定排查范围、方案和方法，不确定的话，可能违法  
对于主机的入侵痕迹排查，主要从网络连接、进程信息、后门账号、计划任务、登录日志、自启动项、文件等方面进行排查。  

尽量断网排查，避免受攻击者干扰，也避免攻击者删除痕迹跑路。  

一些技巧：  
1. 把隐藏文件设置显示，已知后缀设置显示
2. `netstat -ano` 查看网络连接是否有异常，如有异常，用 `wmic process where processid=<PID> get executablepath` 查找对应程序路径
3. 借助外部工具确定网络信息和可疑文件（vt，微步）
4. 用火绒剑看看，进程（可以设置看已退出进程）、启动项（很重要，各种不同启动方式）、服务、网络等
5. windows的 事件查看器（暂时不知道重点看什么）
6. Autoruns查看自启动项很专业

他的总结：思路需要清晰，操作要细致，跟客户要保持沟通，切记不能闷着擅自操作！  

部分工具使用感受：  
1. Process Hacker 2 和任务管理器差不多，感觉没用
2. 火绒剑，看进程做的关键操作，很好用
3. Autoruns，看自启动项，很好用
4. SysInspector，类似火绒剑，可以按风险等级过滤，还可以
5. OTL（OldTimer ListIt），扫描计算机获取各种信息，完全不好用

如果怀疑可能是客户自己不小心操作的，可以排查以下项：  
1. 浏览器下载记录
2. 一般下载文件夹: %USERPROFILE%\Downloads
3. 微信下载文件夹: %USERPROFILE%\Documents\WeChat Files

参考链接：  
Windows主机入侵痕迹排查办法：https://www.freebuf.com/articles/system/255107.html  
中毒应急处置流程1.0：https://bbs.pediy.com/thread-259725.htm  


其他资料：  
应急响应实战笔记 https://bypass007.github.io/Emergency-Response-Notes/  
应急响应之Linux入侵排查 https://www.freebuf.com/vuls/255852.html  
应急响应之Windows入侵排查 https://www.freebuf.com/vuls/255600.html  


---
2020/12/9  
