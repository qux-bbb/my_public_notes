# ClamAV

ClamAV，Clam AntiVirus，是免费开源的防毒软件。  

官网：https://www.clamav.net/  
官方文档: https://docs.clamav.net/  
github地址: https://github.com/Cisco-Talos/clamav  

提交未检测到的病毒：https://www.clamav.net/reports/malware  
提交误报文件：https://www.clamav.net/reports/fp  


## 配置
按官方文档操作: https://docs.clamav.net/manual/Usage/Configuration.html  
复制配置文件之后，将文件中的 "Example" 行添加注释即可  


## 实时检测功能
Linux平台可配置实时检测  
Windows平台本身不支持实时监测，Immunet封装了ClamAV，提供实时检测功能，不开源  


## Windows图形界面程序
官网只有命令行版本的。  

Immunet有图形界面和实时检测功能，不开源，不需要单独安装ClamAV。  
https://www.immunet.com/  

ClamWin有图形界面，没有实时检测功能，开源，不需要单独安装ClamAV。  
https://clamwin.com/  


## ClamAV中各个程序的功能介绍

### clamd
是一个多线程守护进程，它使用 libclav 扫描文件中的病毒，以监听模式工作。  

### clamdscan
是一个简单的 clamd 的客户端，和 clamscan 相比，只需要加载一次特征库。  

### clamdtop
是监视一个或多个clamd实例的工具。它有一个有颜色显示的接口，可以展示clamd队列中的作业、内存使用情况以及有关加载的特征库的信息。  

### clamscan
是ClamAV的命令行病毒扫描器。它可用于扫描文件或目录中的病毒。为了使扫描正常工作，必须将ClamAV病毒数据库文件下载到电脑上，每次都需要加载特征库。  

### clambc
是ClamAV字节码测试工具。它可以用来测试包含字节码的文件。  

### freshclam
是ClamAV的病毒数据库更新工具，它从文件freshclam.conf读取配置(可以被命令行选项覆盖)。Freshclam的默认行为是尝试通过对比下载的diff文件来更新数据库。除非另有规定，否则会更新可能损坏的数据库，并在几次尝试失败后自动完全替换数据库。  

### clamconf
是ClamAV的配置工具。用于显示在ClamAV中配置选项的值，这将显示clamd.conf的内容(或告诉你是否配置不当),freshclam.conf的内容并显示有关软件设置、数据库、平台的信息和build信息。  

### sigtool
病毒特征工具  
`sigtool -i main.cvd`  显示有关给定CVD文件的详细信息。  
`sigtool --md5 test.exe > test.hdb`  生成静态特征码文件，只限于静态病毒使用，文件放在病毒特征库中，扫描时即可生效(如kali，放在/var/lib/clamav/下)。  
`sigtool -u main.cvd` 解压CVD文件，结果是各种特征码文件，有固定格式(格式含义在github的doc文档里有介绍，但没有总结，https://blog.csdn.net/zourzh123/article/details/45719757 此文章最后有格式总结)  



---
2018/12/13  
