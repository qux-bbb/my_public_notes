# stegdetect

stegdetect 用于检测图片隐写方式  

## 资源
github的版本只能在linux下编译使用，按官方建议在ubuntu18下编译即可  
https://github.com/abeluck/stegdetect  

这里可以看到原始版本的介绍：  
https://web.archive.org/web/20150415213536/http://www.outguess.org/detection.php  

这里可以下载源码和windows版本：  
https://web.archive.org/web/20150415220609/http://www.outguess.org/download.php  
windows版本下载地址：https://web.archive.org/web/20150415220609/http://www.outguess.org/stegdetect-0.4.zip  


## linux版本编译和使用
编译：  
```sh
sudo apt install autoconf g++ make
linux32 ./configure
linux32 make
```

简单使用方法  
官网示例：  
```
$ stegdetect *.jpg
cold_dvd.jpg : outguess(old)(***) jphide(*)
dscf0001.jpg : negative
dscf0002.jpg : jsteg(***)
dscf0003.jpg : jphide(***)
[...]
$ stegbreak -tj dscf0002.jpg
Loaded 1 files...
dscf0002.jpg : jsteg(wonderland)
Processed 1 files, found 1 embeddings.
Time: 36 seconds: Cracks: 324123,   8915 c/s
```

# windows版本的简单使用方法  
检测加密方式：  
```bat
stegdetect.exe -tjopi -s 10.0 hide.jpg
```
爆破密码：  
```bat
stegbreak.exe -r rules.ini -f password.txt -t p hide.jpg
```


参考链接：  
https://blog.csdn.net/weixin_43921596/article/details/86654754  


2020/8/23  
