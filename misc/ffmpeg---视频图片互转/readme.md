# ffmpeg---视频图片互转

视频转图片：  
```r
mkdir pngs
ffmpeg -i test.mp4 pngs/frame_%06d.png
```

图片转视频：  
```r
ffmpeg -i pngs/frame_%06d.png -vcodec mpeg4 new_test.mp4
```

查看所有支持的编码格式：  
```r
ffmpeg -codecs
```


原链接: https://blog.csdn.net/u011636440/article/details/78031734  


2023/1/31  
