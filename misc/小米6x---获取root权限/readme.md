# 小米6x---获取root权限

效果：稳定版获取root权限  

1. 解锁BL  
https://www.miui.com/unlock/index.html  
2. 刷TWRP（实测TWRP官网不行）  
https://pan.baidu.com/s/1K0VuCxwwKT9OI3yCouV3Gg  
刷完之后，进"高级"，执行2项操作：Root系统，签名boot  
3. 安装面具  
https://github.com/topjohnwu/Magisk/releases  
下载Magisk-v21.zip，用adb push到手机  
TWRP选择zip包安装  

重启手机，即可获取root权限，成功安装magisk  

参考链接：http://www.romleyuan.com/lec/read?id=137  

2020/10/12  


使用这个命令时卡住了：  
```r
fastboot flash recovery twrp.img
< waiting for any device >
```
据说是驱动的问题，但不知道怎么解决  

2022/2/27  


取消解锁  
切记操作前保存数据  
1. 升级到最新官方系统或刷入官方MIUI
2. 手机关机
3. 手机按"音量减 + 电源键"进入fastboot（BootLoader）
4. USB线连接手机
5. 在解锁工具目录下执行命令: fastboot oem lock (没有反应可以试试运行MiUsbDriver.exe安装驱动)

这样手机会上锁并重置系统，需要重新配置  

参考链接: https://zhidao.baidu.com/question/139095658331101245.html  

2023/10/14  
