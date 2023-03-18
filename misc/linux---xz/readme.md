# linux---xz

xz是一种压缩率极高的压缩工具。  

```r
# 压缩
xz hello.txt
# 解压缩
xz -d hello.txt.xz
```

一些选项：  
```r
-k  保留文件
-0  使用最小的字典(256 KiB)，字典越大，压缩率越高，但处理时间可能越长，-9 可以使用最大的字典(64 MiB)
```

参考链接: https://blog.csdn.net/u014057054/article/details/52329938  


2016/10/15  
