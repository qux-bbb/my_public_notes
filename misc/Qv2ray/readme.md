# Qv2ray

windows linux macos 代理，核心是V2ray  
2021-08-17停止维护

网站：https://qv2ray.net/  
github地址: https://github.com/Qv2ray/Qv2ray


## windows安装
1. 下载相应平台的程序
2. 下载v2ray核心，放到config/vcore文件夹里

然后就设置自己的代理吧  


## manjaro安装
首先按该链接配置manjarocn仓库: https://github.com/manjarocn/repo  

然后执行命令：  
```bash
sudo pacman -Syy qv2ray
```


## kubuntu安装
Discover商店里的版本是2.6，配置v2ray的时候会崩溃，所以就手动配置了。  

下载v2ray-core: https://github.com/v2fly/v2ray-core/releases/download/v4.31.0/v2ray-linux-64.zip  
下载qv2ray: https://github.com/Qv2ray/Qv2ray/releases/download/v2.7.0/Qv2ray-v2.7.0-linux-x64.AppImage  

1. 解压v2ray-linux-64.zip  
2. 运行Qv2ray-v2.7.0-linux-x64.AppImage  
    - 首选项->内核设置 配置"核心可执行文件路径"和"资源目录"  
    - 首选项->常规设置 勾选"登陆时启动" "记忆上次的连接"  
3. 左上 分组 配置订阅  

这样就可以正常用了  

参考链接: https://mahongfei.com/1776.html  


---
20201216  
