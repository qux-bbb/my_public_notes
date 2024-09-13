# virtualbox

VirtualBox是一个开源的虚拟机，功能和VMWare类似。  

官网: https://www.virtualbox.org  


可以在论坛查看或发起一些讨论，需要先搜索是不是已经有过讨论，发起新的讨论需要选择合适的位置  
https://forums.virtualbox.org  
比如: https://forums.virtualbox.org/viewtopic.php?t=109563  

如果想要报告bug或者提出建议，可以在Bugtracker发起新的流程，同样注意发起前先搜索  
https://www.virtualbox.org/wiki/Bugtracker  

如果想要看代码，可以在下载页面获取打包好的源代码  
https://www.virtualbox.org/wiki/Downloads  
也可以用svn获取最新的代码，看历史修改更方便  
svn co https://www.virtualbox.org/svn/vbox/trunk vbox  


注意: 管理->全局设定->代理，在这里设置的代理仅用于VirtualBox下载增强功能包、检查更新，和虚拟机的网络没有关系。  

从6.0开始有了 `file manager`, 可以比较方便地在虚机和主机之间传文件。  
从7.1.0开始有了 `Clipboard File Transfers`, 启用就可以在虚机和主机之间复制粘贴文件了。  

ubuntu查看增强功能版本：  
```bash
/usr/bin/VBoxClient --version
```


2022/1/29  
