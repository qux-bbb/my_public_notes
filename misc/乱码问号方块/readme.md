# 乱码问号方块

有时候乱码会出现一些问号方块，这是一些编辑器将无法识别的部分替换为对应编码方案中表示乱码的字符了。  
常见编码方案替换如下：  
```r
HTML Entity:        &#65533;
                    &#xFFFD;
UTF-8 Encoding:     0xEF 0xBF 0xBD
UTF-16 Encoding:    0xFFFD
UTF-32 Encoding:    0x0000FFFD
```

参考链接：  
1. https://www.bilibili.com/video/BV1xP4y1J7CS
2. https://www.compart.com/en/unicode/U+FFFD


2022/8/1  
