# python---opencv

安装：  
```r
pip install opencv-python opencv-contrib-python
```

numpy和opencv配合生成空图片：  
```python
# coding:utf8

import cv2
import numpy

img_zero = numpy.zeros((30, 20, 3))  # 高30，宽20，BGR 3通道

cv2.imwrite('zero.png', img_zero)
```

读写文件、像素：  
```python
# coding:utf8

import cv2

# 读文件
img = cv2.imread('steg.png')
# 行数(高)、列数(宽)、每个点有几个数
print(img.shape)
# 读像素
print(img[3, 4])  # 第3行第4列的像素(行列都从0算起)，即距顶端为3、距左端为4
# 写像素
img[150,200] = [100,150,200]  # 第150行第200列，BGR分别为100 150 200
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

读取图片时包含透明图层：  
opencv读取图片默认不包含透明图层，如果要包含，需要指定flags参数  
网上资料写的都是 `cv2.imread('steg.png', flags=cv2.CV_LOAD_IMAGE_UNCHANGED)`  
我的opencv版本是4.5.4.60，python3，已经没有这个属性了，需要换成 `cv2.IMREAD_UNCHANGED`  
一个像素的数值顺序为BGRA  


参考链接：  
1. https://github.com/opencv/opencv-python
2. https://www.cnblogs.com/zlel/p/9267629.html


2021/11/29  
