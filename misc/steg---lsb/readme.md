# steg---lsb

least significant bit, 最低有效位  

这里说的lsb隐写就是把字符串按位放在一张图片的红、绿、蓝图层的最低位。用stegsolve可以看到。  

这里用python实现一下lsb隐写。  

将字符串隐藏到图片中: [files/hide_msg.py](files/hide_msg.py)  
提取图片中隐藏的信息: [files/extract_msg.py](files/extract_msg.py)  

原始图片  
![原始图片](files/steg.bmp)  
隐藏信息的图片  
![隐藏信息的图片](files/steg_lsb.bmp)  

载体bmp、png可以，jpg不可以，因为jpg默认是有损压缩  


2021/8/15  
