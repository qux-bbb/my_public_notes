# win10---血战上海滩

## 安装
没找到什么太干净的源，我在`腾讯软件管理`下载的  

直接双击`shanghai.exe`没有什么反应，需要加一个`-windows`的选项，通过建快捷方式，目标的地方加参数`-windows`即可   

开始后发现是窗口模式，800x600，而且在窗口的左上角，所以需要建一个bat脚本，通过bat脚本来调用`setres.exe`设置窗口分辨率，可以连`-windows`的选项一起设置了  
下为bat脚本内容：  

```bash
@echo off
setres h800 v600
shanghai.exe -windows
setres h1366 v768
exit
```
bat脚本，setres.exe，shanghai.exe应该在一个目录下，启动游戏直接双击bat脚本即可   

注：`setres.exe`在win10系统中没有，需要自己下载，建议下载页面：http://www.softpedia.com/get/Multimedia/Video/Other-VIDEO-Tools/Ian-Sharpe-SetRes.shtml  


## 秘籍
按左上角的"~"输入，回车即可  
```
god_on 开启无敌
god_off 关闭无敌
haveallweapon 拥有所有武器
addammo 给已有的武器加满弹药
ammonolimit 已有的武器子弹无限
```


---
2018.02.04  
2018.04.18 更新  
