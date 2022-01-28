# ubuntu---更换源

keywords: linux软件源  

ubuntu默认源在国内有时候比较慢，可以换一个快一点的源  

## 图形界面操作
settings -> About -> Software Updates -> Ubuntu Software -> Download from  
就能选各种源地址了，这里还提供了根据速度自动选的功能，很好了  

## 手动编辑文件
/etc/apt/sources.list  

http://wiki.ubuntu.org.cn/源列表  

跟版本有关系  

阿里源  
```r
deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
```

中科大源  
```r
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
```


中科大的源比较快  

20可以把 xenial 替换成 focal  


20201122  
