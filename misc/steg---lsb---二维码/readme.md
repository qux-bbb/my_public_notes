# steg---lsb---二维码

把一个二维码图片或者任意一张图片隐藏到另一张图片中。  

实现该功能的网址: https://incoherency.co.uk/image-steganography/  

自己写个脚本，把二维码隐藏到指定图层的最低位: [files/hide_qrcode.py](files/hide_qrcode.py)  

二维码(在这里生成的: https://cli.im/)  
![二维码](files/qrcode.png)  
原始图片  
![原始图片](files/raw.png)  
隐藏二维码的图片  
![隐藏二维码的图片](files/dst.png)  

隐藏二维码的图片可以用stegsolve打开，点下面的箭头切换图层，切到红色图层0位，就看到二维码了  

载体bmp、png可以，jpg不可以，因为jpg默认是有损压缩  


2021/8/16  
