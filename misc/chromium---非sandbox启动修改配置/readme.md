# chromium---非sandbox启动修改配置

编辑`/usr/bin/chromium`
在一开始加入如下行，保存即可，不需要考虑未定义
```r
CHROMIUM_FLAGS="$CHROMIUM_FLAGS --no-sandbox" 
```


2018/10/18  
