# snow隐写

keywords: 空白字符 tab  

snow隐写，使用空格和制表符在网页或其它文件里隐写的方法，使用了ICE加密算法，解密需要密码。  

官网: http://www.darkside.com.au/snow/  

使用示例：  
```r
# The following command will conceal the message "I am lying" in the file infile, with compression, and encrypted with the password "hello world". The resulting text will be stored in outfile.
snow -C -m "I am lying" -p "hello world" infile outfile

# To extract the message, the command would be
snow -C -p "hello world" outfile
```


2020/8/30  
