# python---opencv

安装：  
```r
pip install opencv-python opencv-contrib-python
```

将彩色图片转为灰白图片：  
```python
# coding:utf8

import cv2

img_path = 'the_img.png'

img = cv2.imread(img_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray_img)
```


参考链接：  
1. https://github.com/opencv/opencv-python
2. https://www.cnblogs.com/zlel/p/9267629.html


2021/11/29  
