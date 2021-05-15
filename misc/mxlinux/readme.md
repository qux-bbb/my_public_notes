# mxlinux

## 简介
官网: https://mxlinux.org/  

mxlinux 基于 Debian，可以选择不同桌面版本，我当然选 KDE 了，挺好看的，而且自己对 debian 系的用法比较熟悉。  

安装的时候用美国区域和英语，用中文的话，在 home 下生成的文件夹名字还需要自己改成英文的，有点不方便。  


## 配置软件源  
打开 Muon 软件包管理器，Settings -> Configure Software Sources，修改 Download From 的内容即可。  


## 语言时区输入法设置  
1. 左下角 System Settings -> Regional Settings，  
    设置 Language: Add Language，选择"简体中文"后，拖到最上方，点击右下角 Apply  
    设置 Formats: Region，拖到最下面，选择"中国-简体中文(zh_CN)"，点击右下角 Apply  
2. 设置 Date & Time: Time Zone，搜索"Shanghai"，选中，点击右下角 Apply  
3. 左下角 点击最左边图标 -> MX Tools -> System Locales，第一次点击"继续"，第二次选择"zh_CN.UTF-8"，接着点击"继续"，生成新的配置  
4. 左下角 点击最左边图标 -> MX Tools -> MX Package Installer，搜索"Chinese"，选中安装一些中文包和中文输入法  
5. 重启  

注意不同输入法的切换快捷键不同。  


2021/5/15  
