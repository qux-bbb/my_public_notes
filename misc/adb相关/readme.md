# adb相关

adb, Android Debug Bridge, 用于调试管理Android设备  

## 安装
根据链接下载相应压缩包解压使用即可，可以把路径加到path里  
https://www.xda-developers.com/install-adb-windows-macos-linux/  

## 简单使用命令
```r
# 上传文件，从PC复制文件到设备
adb push <PC文件> </tmp/...>
# 下载文件，从设备复制文件到PC
adb pull </tmp/...> <PC文件>
# 安装程序
adb install <*.apk>
# 卸载程序
adb uninstall <*.apk>
# 找到所有的设备
adb devices
# 安装程序到指定设备
adb -s 要安装到的设备 install aa.apk
# 不使用USB线连接，在同一局域网下连接开启了相关服务的设备
adb connect 192.168.1.4:5555
# 使用设备shell，也可使用-s指定设备
# -s emulator-1234
# -s 192.168.1.4:5555
adb shell
```


## 参考链接
https://developer.android.google.cn/studio/command-line/adb  
