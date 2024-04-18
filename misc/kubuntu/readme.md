# kubuntu

官网: https://kubuntu.org/  

kubuntu 是 ubuntu 官方维护的 KDE 桌面版本，挺好的。  

## 一些点

### 安装注意
虚拟机安装的时候，断网、删掉额外加的两个设置项、安装时不下载其它东西，这样安装会快一点。  

### 图形界面修改源
Discover -> 左下角 设置 -> 右边 Software Sources  
然后选源就好了  

### vmware安装之后不能全屏
执行命令: `sudo apt install open-vm-tools-desktop`  

### 安装软件没有中文  
首先确认系统的 设置->区域设置->语言，"简体中文"在顶部。  

然后以krita为例，安装之后无法切换为中文。  
在命令行先搜索相关包: `sudo apt search krita`  
发现一个相关的包：  
```
krita-l10n/impish,impish 1:4.4.8+dfsg-1ubuntu1 all
  translations for Krita painting program
```
执行命令安装: `sudo apt install krita-l10n`  
这样再打开krita就是中文界面了  

### 登陆界面不是中文
查看locale配置文件: `cat /etc/default/locale`, 发现LANG是英文配置  
修改LANG项为 `LANG=zh_CN.UTF-8` 重启即可  
locale命令显示的和 /etc/default/locale 不一定一样，还不知道为什么，但改文件肯定是正确的  

### 安装中文拼音输入法
在Discover里搜索"Pinyin"安装即可(就是ibus-pinyin)，重启或重新登陆生效  
默认只启用了英语，可以在设置里添加拼音  
默认的输入法切换快捷键是"Super+空格"(Windows上的Super是"田"字键)，之后可以用Shift键切换中英文  


---
2021/5/15  
