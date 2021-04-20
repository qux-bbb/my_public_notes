# pip---源

pip默认源有时候很慢，这个时候可以换源使用  

## 修改源
### 临时修改
```bash
pip install scrapy -i https://pypi.mirrors.ustc.edu.cn/simple
```

### 永久修改
linux:  
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：  
```conf
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple
```

windows:   
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下：  
```conf
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple
```

## 国内的一些源地址
```
阿里云 http://mirrors.aliyun.com/pypi/simple/ 
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
```

测试中国科技大学的比较好用  


原链接: https://blog.csdn.net/chenghuikai/article/details/55258957  


2018/7/5  
