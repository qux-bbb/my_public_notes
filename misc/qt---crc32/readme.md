# qt---crc32

CRC, Cyclic Redundancy Check, 循环冗余校验，一种检错手段  

其中的CRC32早期也被用来做文件校验，虽然不怎么安全  

qt的QCryptographicHash库提供了md5等比较有名的hash计算方法，没有提供CRC32，这里简单整理一下从网上搜集的代码：  
[CRC32](files/main.cpp)  


参考链接：  
1. 计算crc32，计算完整的文件有点问题: https://www.programmersought.com/article/16751068617/  
   calcFileCRC函数的`crc = crc ^ calcCRC32(raw)`莫名其妙
2. 计算crc32，没什么问题，可以和上面的结合一下: https://github.com/nusov/qt-crc32  


2021/7/22  
