# python---pillow

keywords: 图像 PIL  


## 简介
Pillow是PIL的延续，后者已经很久不维护了，PIL是Python Imaging Library  

官网: https://python-pillow.org/  
官方文档: https://pillow.readthedocs.io/en/stable  

安装: `pip install Pillow`  


## 简单操作
新建一张256x256的红色图片：  
```python
im = Image.new('RGB', (256, 256), (255,0,0))
im.save('a.jpg')
im.close()
```

打开一张图片：  
```python
im = Image.open('a.jpg')
```

读写像素方法1：  
```python
im = Image.open('a.jpg')
# 读像素
r, g, b = im.getpixel((1, 2))
# 写像素
im.putpixel((1, 2), (r, g, 255))
im.save('new.jpg')
im.close()
```

读写像素方法2：  
```python
im = Image.open('a.jpg')
pic = im.load()
# 读像素
r, g, b = pic[1, 2]
# 写像素
pic[1, 2] = (r, g, 255)
im.save('new2.jpg')
im.close()
```

简单的例子：  
```python
# coding:utf8
# python3

from PIL import Image

im = Image.new('RGB', (256, 256), (255,0,0))  # 红色
pic = im.load()
for i in range(256):
    for j in range(256):
        if abs(i-j) < 100:
            # 写像素
            pic[i, j] = (0, 255, 0)  # 绿色

im.save('a.jpg')
```

GIF读取像素示例：  
```python
# 注意点：
# seek是选择第几帧，从0开始
# 需要转成RGB模式才能读取像素
from PIL import Image

im = Image.open('test.gif')
im.seek(0)
im2 = im.convert('RGB')
pix1 = im2.getpixel((1,1))
print(pix1)
im.close()
im2.close()
```


2021/8/9  
