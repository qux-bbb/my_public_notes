## 简介
提供网络虚假回应或转发功能  


## 原始版本
fakenet  
https://practicalmalwareanalysis.com/fakenet/  


## 升级版本
flare-fakenet-ng  

https://github.com/fireeye/flare-fakenet-ng  

### windows使用
直接在release页面下载zip文件，解压使用即可  

需要管理员权限打开命令行窗口，然后运行  

保存日志：  
```
fakenet.exe -l net.log
```

在win10会闪退，win7看着还可以  

### ubuntu使用
安装python2.7和相应的pip，然后按如下步骤安装：  
```bash
# 安装依赖
sudo apt install python-dev libssl-dev libffi-dev libnetfilter-queue-dev
# 使用pip安装fakenet
pip install https://github.com/fireeye/flare-fakenet-ng/zipball/master
```

最简单使用: `sudo fakenet`  
要网络正常才能用，现在只能看到dns查询记录，可能自己的配置不正确  
默认配置文件为：  
`/usr/local/lib/python2.7/dist-packages/fakenet/configs/default.ini`  

可能遇到53端口占用，提示"Address already in use" 错误，停止并禁用相关服务即可：  
```bash
systemctl stop systemd-resolved.service
systemctl disable systemd-resolved.service
```

参考链接: https://www.cnblogs.com/DragonStart/p/8193391.html  
