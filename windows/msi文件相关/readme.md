# msi文件相关

msi, microsoft installer，windows使用的一种安装包文件  

这是官方文档: https://docs.microsoft.com/en-us/windows/win32/msi/windows-installer-portal  
虽然目录看起来很好，但其实并没有一个完整的示例  


## 创建msi安装包

大概流程：  
1. 在Visual Studio 扩展商店搜索安装 `Microsoft Visual Studio Installer Projects` 扩展(关键字搜 `Setup` 就好了)
2. 创建 `Setup Project`
3. 添加要安装的文件或文件夹，要设置的快捷方式

然后生成解决方案就好了  

在项目上 右键->View->自定义操作，Install和Commit阶段均可添加自动运行的程序，可以是exe、dll、vbs、js  
&&&&&&& 不知道怎么运行到一半故意失败  


## 运行
普通的运行直接双击按提示操作就好了。  

命令行静默安装：  
```bat
msiexec /i Setup1.msi /qn /norestart

:: /i 后跟msi路径，可以是url
:: /qn 表示quiet、无用户界面
:: /norestart 表示安装完成后不重新启动
```


## 提取msi安装包中的文件
lessmsi: http://lessmsi.activescott.com/  


参考链接：  
1. https://baike.baidu.com/item/.msi/4900284  
2. https://www.youtube.com/watch?v=0lXA4RSYUGQ  
3. https://www.52pojie.cn/thread-751608-1-1.html  


2021/10/6  
