# python3---编码问题

文本字符和二进制数据区分得更清晰，分别用 str 和 bytes 表示。  
文本字符全部用 str 类型表示，str 能表示 Unicode 字符集中所有字符，  
而二进制字节数据用一种全新的数据类型，用 bytes 来表示。  

bytes: Python3 中，在字符引号前加‘b’，明确表示这是一个 bytes 类型的对象，实际上它就是一组二进制字节序列组成的数据，bytes 类型可以是 ASCII范围内的字符和其它十六进制形式的字符数据，但不能用中文等非ASCII字符表示。  

str 与 bytes 类型的数据不能执行 + 操作，尽管在py2中是可行的  

str 与 bytes 之间的转换可以用 encode 和从decode 方法  
```r
# python3.x
+-----+                       +-------+
|     | +-----decode--------> |       |
| str |    ascii,utf-8,gbk... | bytes |
|     | <-----encode--------+ |       |
+-----+                       +-------+
```

encode 负责字符到字节的编码转换。默认使用 UTF-8 编码准换。  
```r
>>> s = "Python之禅"
>>> s.encode()
b'Python\xe4\xb9\x8b\xe7\xa6\x85'
>>> s.encode("gbk")
b'Python\xd6\xae\xec\xf8'
```
decode 负责字节到字符的解码转换，通用使用 UTF-8 编码格式进行转换。  
```r
>>> b'Python\xe4\xb9\x8b\xe7\xa6\x85'.decode()
'Python之禅'
>>> b'Python\xd6\xae\xec\xf8'.decode("gbk")
'Python之禅'
```

原链接: https://www.cnblogs.com/mzc1997/p/7755135.html  


2019/12/1  
