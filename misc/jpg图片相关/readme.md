# jpg图片相关

jpg, jpeg: Joint Photographic Experts Group, 联合图像专家组  
jpg是一种有损压缩的图片格式  

FFD8 开头  
FFD9 结尾  

一般前12字节有明显的特征，但不一定完全一样，举例：  
```
FF D8 FF E0 00 10 4A 46 49 46 00 01
 .  .  .  .  .  .  J  F  I  F  .  .

FFD8: enum M_ID SOIMarker
FFE0: enum M_ID marker
0010: WORD szSection
4A46494600: char App0Type[5]
01: short versionHigh
```
具体可以用010Editor看看，比较清楚  


参考链接：  
1. https://en.wikipedia.org/wiki/JPEG
2. https://en.wikipedia.org/wiki/Joint_Photographic_Experts_Group


2021/11/20  
