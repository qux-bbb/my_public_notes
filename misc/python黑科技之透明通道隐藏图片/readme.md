# python黑科技之透明通道隐藏图片

```r
透明通道的使用
putalpha(alpha)
这个方法是一个神奇的方法，你可以将一个图片(与原图尺寸相同)写入到原图片的透明通道中，而不影响原图片的正常显示，可以用于信息隐藏哦。当然，前提是原
始图片有透明通道。不过就算不是也没有多大关系，因为有PIL提供的convert功能，可以把一个图片先转换成RGBA模式，然后把要隐藏的信息文件转成“L”或者“1”模
式，最后使用这个putalpha将其叠加。而在图片的使用方，只需要简单的抽取其中的透明通道就可以看到隐藏信息了，哈哈。
```

Python代码  
```python
def hideInfoInImage(img, info):  
if img.mode != "RGBA":  
        img = img.convert("RGBA")  
if info.mode != "L"and info.mode != "1":  
        info = info.convert("L")  
    img.putalpha(info)  
return img  
```

测试之，Python代码  
```python
if __name__ == "__main__":  
    img = Image.open("green.png")  
    band = Image.open("antelope_inhalf.jpg")  
    img = hideInfoInImage(img, band)  
    img.show()#可以看到，原图片没有显式变化
    img.split()[3].show()#抽取出透明通道中的图片并显示
```


原链接: http://blog.csdn.net/sheldon761642718/article/details/52209817  


2016/9/11  
