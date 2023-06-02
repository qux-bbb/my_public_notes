# misc---盲水印

keywords: 隐写  

特征  
两张图像相同，文件大小不同的图片  

工具  
https://github.com/chishaxie/BlindWaterMark  
  
用python3的pip安装  

解密命令  
```sh
# raw.png 原图片
# with_info.png 携带信息的图片
# decoded.png 将要存放解密信息的图片
py -3 .\bwmforpy3.py decode raw.png with_info.png decoded.png
```


2020/8/30  
