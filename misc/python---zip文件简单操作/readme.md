# python---zip文件简单操作

zipfile为python内置模块, 无需安装  

```python
from zipfile import ZipFile

# 读压缩包中的一个文件
with ZipFile('spam.zip') as myzip:
    with myzip.open('eggs.txt') as myfile:
        print(myfile.read())

# 把文件放入压缩包中
with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')
```

从内存读取压缩文件进行解析  
```python
import io
import zipfile

file_like_object = io.BytesIO(my_zip_data)
zipfile_ob = zipfile.ZipFile(file_like_object)
```

zipfile不支持AES加密算法，如果需要，要用pyzipper  


参考链接：  
1. https://stackoverflow.com/questions/2463770/python-in-memory-zip-library
2. https://docs.python.org/3/library/zipfile.html


2019/12/27  
