# kali---安装搜狗输入法

先安装fcitx：  
```r
apt install fcitx
```
从 https://pinyin.sogou.com/linux/ 下载相应版本的deb，举例为 `sogoupinyin_2.2.0.0108_amd64.deb`，安装：  
```r
dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
```

重启即可  

切换输入法为 `Ctrl+Space`  

更新之后如果输入法弹不出来，在命令行输 `im-config` 重新选一下，重启就好了  


20180609  
