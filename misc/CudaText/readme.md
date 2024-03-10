# CudaText

CudaText是一个开源跨平台的文本编辑器。使用Lazarus 2.0编写，优点是可打开超大文件。  

官网: https://cudatext.github.io/  
github地址: https://github.com/Alexey-T/CudaText  


## 修改编辑方式打开文件大小限制
如果大文件无法用编辑方式打开，可能会有如下提示，表示默认编辑方式打开文件的大小限制为500M：  
```r
File is too big to edit: (1020M, "ui_max_size_open": 500)
```

Plugins -> Options Editor Lite, 搜索"ui_max_size_open"，修改为自己期望的值，应用重启即可  
上面方法实际修改的是user.json文件  

方法来源: https://github.com/Alexey-T/CudaText/issues/5419  


---
2022/7/4  
