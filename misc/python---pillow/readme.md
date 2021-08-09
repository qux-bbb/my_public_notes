# python---pillow

keywords: 图像 PIL  


Pillow是PIL的延续，后者已经很久不维护了，PIL是Python Imaging Library  

官网: https://python-pillow.org/  
官方文档: https://pillow.readthedocs.io/en/stable  

安装: `pip install Pillow`  

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
            pic[i, j] = (0, 255, 0)  # 绿色

im.save('a.jpg')
```


2021/8/9  
