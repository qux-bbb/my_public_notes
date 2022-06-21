# python---pillow

keywords: 图像 PIL  


## 简介
Pillow是PIL的延续，后者已经很久不维护了，PIL是Python Imaging Library  

官网: https://python-pillow.org/  
官方文档: https://pillow.readthedocs.io/en/stable  

安装: `pip install Pillow`  


## 简单操作
新建一张20x30(宽20高30)的红色图片：  
```python
im = Image.new('RGB', (20, 30), (255,0,0))  # 通道顺序为 RGB，即 红绿蓝
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
r, g, b = im.getpixel((1, 2))  # 第1列第2行(行列都从0算起)，即距左端为1、距顶端为2
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
im2 = im.convert('RGB')  # png如果想获取RGB形式的数据，也需要这样转换
pix1 = im2.getpixel((1,1))
print(pix1)
im.close()
im2.close()
```

GIF保存所有帧：  
```python
import os
from PIL import Image

os.makedirs('frames')

im = Image.open('test.gif')

n_frames = im.n_frames
for i in range(n_frames):
    im.seek(i)
    im.save(f'frames/{i}.png')
```


数字矩阵转黑白图片：  
```python
# 注意点：
# aa[i][j] 应该放到 (j, i) 位置，(j, i)指的是距左j，距上i
from PIL import Image

aa = [
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
]

im = Image.new('RGB', (5, 5), (0,0,0))
for i in range(5):
    for j in range(5):
        if aa[i][j] == 1:
            im.putpixel((j, i), (0,0,0))  # (0,0,0) 表示黑色
        else:
            im.putpixel((j, i), (255,255,255))  # (255,255,255) 表示白色

im.save('a.jpg')
im.close()
```


比较两张图片是否相同(像素级)：  
```python
from PIL import Image
from PIL import ImageChops

image_one = Image.open(img_path1)
image_two = Image.open(img_path2)
diff = ImageChops.difference(image_one, image_two)
if diff.getbbox():
    print('diff images')
else:
    print('same images')
```


---
2021/8/9  
