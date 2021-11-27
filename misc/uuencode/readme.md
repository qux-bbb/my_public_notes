# uuencode

uuencode和base64类似，特征为`begin`开头，`end`结尾。  


## ubuntu安装使用
安装：  
```r
sudo apt install sharutils
```

使用
```r
# 编码 hello.txt为原文件 the_hello为解码之后要用的文件名 result.txt为经过编码的文件名
uuencode hello.txt the_hello > result.txt
# 解码 执行命令后会生成the_hello文件
uudecode result.txt
```

原内容为: `hello world`  
编码之后内容为：  
```r
begin 664 the_hello
,:&5L;&\@=V]R;&0*
`
end
```


## python使用
python3  
```python
# coding:utf8

import codecs

the_str = b'hello world'

result = codecs.encode(the_str, 'uu')
print(result)
raw_str = codecs.decode(result, 'uu')
print(raw_str)

'''
b'begin 666 <data>\n+:&5L;&\\@=V]R;&0 \n \nend\n'
b'hello world'
'''
```


---
参考：  
1. tldr
2. https://en.wikipedia.org/wiki/Uuencoding


2021/11/27  
