# 谷歌浏览器---本地js访问资源失效

有一个js写的小游戏，需要访问本地资源，google浏览器就给禁了，问题如下：  
```r
Cross origin requests are only supported for protocol schemes
```

解决方法：  
新建一个快捷方式，目标 填写类似下面的内容：  
```
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files
```

可能需要把google浏览器的位置改一下  


2016/12/30  
