# kali---安装网易云音乐

```
在官网选择deepin版本下载，然后安装：
dpkg -i netease-cloud-music_1.0.0-2_amd64_deepin15.deb  
安装之后打不开，找到 /usr/share/applications/netease-cloud-music.desktop
右键属性 ，修改命令为  netease-cloud-music %U --no-sandbox
即可正常使用
```


2017/9/3  
