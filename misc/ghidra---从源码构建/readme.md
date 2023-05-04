# ghidra---从源码构建

从源码构建ghidra，基本按照官方提供的步骤即可  
https://github.com/NationalSecurityAgency/ghidra#build  

主要的2条命令：  
```r
# 下载依赖
gradle -I gradle/support/fetchDependencies.gradle init
# 构建开发版本
gradle buildGhidra
```

在执行第1条gradle命令时，需要从github.com、storage.googleapis.com、sourceforge.net等网站下载依赖文件，由于国内网络问题，最好设置代理再执行  
在项目下的 gradle.properties 文件中添加以下内容即可(ip和端口根据情况而定)：  
```r
systemProp.http.proxyHost=127.0.0.1
systemProp.http.proxyPort=10809
systemProp.https.proxyHost=127.0.0.1
systemProp.https.proxyPort=10809
```

构建后的压缩包在 build/dist/ 文件夹下  


2023/5/4  
