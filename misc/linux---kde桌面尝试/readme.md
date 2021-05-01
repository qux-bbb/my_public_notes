# linux---kde桌面尝试

记一些使用kde桌面的linux发行版，好看呀。  


## arch
官网: https://archlinux.org/  

安装有点复杂，现在有一个`archinstall`可以自己配一些安装选项然后自动安装，不过虚拟机还不能用。  
暂时不体验了。  


## manjaro
官网: https://manjaro.org/  

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


## opensuse
官网: https://www.opensuse.org/  

使用kde桌面，默认的界面比manjaro要好看一些。  

安装很顺利，没有什么问题。  


2021/5/1  
