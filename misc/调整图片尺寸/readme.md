# 调整图片尺寸

可以使用ImageMagick调整图片尺寸。  

```sh
# 将原图片调整为32x32大小的图片(单位是像素)，32x32是宽x高，magick默认会保持纵横比，这会导致部分情况下只有宽的像素是准确的
magick xhash.png -resize 32x32 xhash_32.png
# 将原图片调整为32x32大小的图片，不保持纵横比
magick xhash.png -resize 32x32\! xhash_32.png
```

参考链接: https://imagemagick.org/Usage/resize/  


2024/5/29  
