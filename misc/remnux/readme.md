# remnux

官网: https://remnux.org  

REMnux 是用于逆向工程和分析恶意软件的Linux工具包。  
REMnux提供了由社区创建的精选免费工具集合。分析人员可以使用它来分析恶意软件，而无需查找，安装和配置工具。  

好吧，就是预装了一些工具的Ubuntu，装的工具还不少，可以试试，不需要自己配置了  

Username: remnux Password: malware  

桌面环境网卡显示"Wired Unmanaged"  
修改/etc/netplan/01-netcfg.yaml, 将renderer由networkd改为NetworkManager(大小写敏感)  
然后应用更改: `sudo netplan apply`  
参考链接: https://blog.csdn.net/qq_30727593/article/details/122855277  


2020/12/16  
