# linux---kde桌面尝试

记一些使用kde桌面的linux发行版，好看呀。  


## arch
官网: https://archlinux.org/  

手动安装有点复杂，现在有一个`archinstall`可以自己配置一些安装选项然后自动安装。  
执行archinstall命令后，关键的选项如下：  
```r
Profile: Desktop Kde
Audio: Pipewire
Network configuration: Use NetworkManager
```

VirtualBox装完arch之后需要设置以解决登陆后黑屏问题：  
设置 -> 显示 -> 屏幕 -> 显卡控制器 -> 扩展特性，勾选"启用3D加速"  
也可以把显卡控制器切换成"VBoxSVGA"  
https://bbs.archlinux.org/viewtopic.php?id=293824  


## kubuntu
官网: https://kubuntu.org/  

基于ubuntu，由ubuntu团队维护，因为要保持稳定性，不会用最新的kde版本。  


## KDE neon
官网: https://neon.kde.org/  

基于ubuntu长期支持版，但会安装最新的kde桌面和软件。  
Discover没有配置源的地方，官方源太慢了，没有其它镜像源。  


## manjaro
官网: https://manjaro.org/  

Manjaro 读音 /mənˈdʒɑːroʊ/ (汉语谐音：满家柔)  

有多种桌面版本，使用kde桌面的manjaro很漂亮，基于arch，安装过程对用户更友好。  

### 安装问题
vmware安装遇到问题，卡死在这儿了：  
`A start job is running for LiveMedia MHWD Script (7min 54s / no limit)`  
时间一直在增加  

在启动的时候按一下上下方向键，停在`Boot with open source dirvers`选项，按`E`进入编辑模式，将`driver=free`改成`driver=intel`，看下面的提示按`Ctrl-c`或`F10`，就可以进入安装界面了  

参考链接: https://blog.csdn.net/Umbrella2B/article/details/84258951  

### 分辨率问题
修改了分辨率，闪一下就变成原来的了，难受  

在硬件设定中安装或重新安装video-virtualmachine，这个时候再去修改分辨率就没问题了  

参考链接: https://blog.csdn.net/qq_44874759/article/details/115256777  

### 安装中文输入法
如果有fcitx先删除fcitx: `sudo pacman -Rsc fcitx`  
安装fcitx5: `sudo pacman -S fcitx5-im fcitx5-chinese-addons`  
配置环境变量，编辑~/.pam_environment，如果没有文件自己创建一个：  
```
GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=\@im=fcitx
SDL_IM_MODULE DEFAULT=fcitx
```
注销重新登入即可生效  

原链接: https://linuxacme.cn/336/  

### 登录界面非全中文
搜 SDDM，换一个登录屏幕  

感谢 QQ 的 Manjaro 群  


## opensuse
官网: https://www.opensuse.org/  

使用kde桌面，默认的界面比manjaro要好看一些。  

安装很顺利，没有什么问题。  

比manjaro稳定，但软件比manjaro少一点。  
opensuse好像受美国出口管制，manjaro没有。  
opensuse的默认界面更好看一些，不过只是不同的风格，manjaro切换一下就好了。  


2021/5/1  
