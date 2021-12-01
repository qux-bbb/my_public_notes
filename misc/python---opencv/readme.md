# python---opencv

安装：  
```r
pip install opencv-python opencv-contrib-python
```

读写文件、像素：  
```python
# coding:utf8

import cv2

# 读文件
img = cv2.imread('steg.png')
# 行数、列数、每个点有几个数
print(img.shape)
# 读像素
print(img[3, 4])
# 写像素
img[150,200] = [1,1,1]
# 写文件
cv2.imwrite('new.png', img)
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
