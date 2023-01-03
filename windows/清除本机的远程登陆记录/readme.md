# 清除本机的远程登陆记录

通过远程桌面可以登录到远程电脑上进行相应的操作，在登录过后会在本地电脑上留下登录过的IP以及登录用户名相关信息，下面介绍一下清除远程桌面历史记录的方法：  
1. 删除我的文档下的Default.rdp文件（该文件是隐藏文件，显示隐藏文件方法：打开我的电脑→工具菜单→文件夹选项→查看选项卡→勾选显示所有文件和文件夹）。
2. “开始→运行→regedit”，打开注册表，找到：HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default，将“MRU0~MRUN”中你不想要的主机地址删掉就可以了。

原链接: https://blog.csdn.net/duhai/article/details/39314891  


2020/2/14  
