# png图片结构

基本信息
--------
PNG：Portable Network Graphics  
png图片的结构比较简单，看一些主要的部分  

png的文件头有固定的8个字节：  
```
89 50 4E 47 0D 0A 1A 0A
```

png图片分成很多块，除了文件头，其他块都有一致的格式，如下：  
```
数据长度：4字节
块类型：4字节
数据内容：不定长度
CRC32校验：4字节
```
CRC校验的数据范围是 块类型加数据内容  

因为png图片的第1块总是数据长度固定的IHDR(Image Header)块，所以所有的png图片前16个字节都是相同的  


简单例子
--------

举个简单的例子：  
```
00000011 74455874536F66747761726500536E697061737465 5D17CEDD
 . . . .  t E X t S o f t w a r e . S n i p a s t e  . . . .
```
`00000011` 表示数据长度 0x11  
`74455874` 表示文本信息类型 tExt  
`536F66747761726500536E697061737465` 表示具体数据 S o f t w a r e . S n i p a s t e  
`5D17CEDD` CRC32校验和，即 `74455874536F66747761726500536E697061737465` 的CRC32值为 `5D17CEDD`  


参考链接：  
1. https://en.wikipedia.org/wiki/Portable_Network_Graphics  
2. https://tools.ietf.org/html/rfc2083  


2020/8/23  
