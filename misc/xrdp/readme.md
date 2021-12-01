# xrdp

xrdp - an open source RDP server  

官网: http://xrdp.org  
github地址: https://github.com/neutrinolabs/xrdp  

rdp, Remote Desktop Protocol, 远程桌面协议，xrdp可以使其它机器远程连接linux机器。  


下面以ubuntu20为例：  
安装：  
```r
sudo apt install xrdp
# 查看服务是否正常
systemctl status xrdp
```

xrdp设计不允许同一用户在多个地方登录，将本机用户登出(logout)，此时可以在别的机器通过rdp客户端连接(ubuntu本地用户不登出的话，远程连接后会黑屏)  
虽然可以允许同一用户多个地方登录，但有这样那样的问题，暂不记录  

使用windows默认的"远程桌面连接"登录之后，无法使用剪贴板、复制粘贴文件，还不知道原因。  


参考链接: https://linuxconfig.org/ubuntu-20-04-remote-desktop-access-from-windows-10  


2021/12/1  
