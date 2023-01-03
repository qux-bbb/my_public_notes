# openssl头文件未找到解决方法

错误如下：  
```r
Error: Could not find header file for OPENSSL
  No file openssl/evp.h in /usr/local/include
  No file openssl/evp.h in /usr/includ
```

安装一个开发包即可  
```r
sudo apt-get install libssl-dev
```

原链接: https://stackoverflow.com/questions/13024481/fatal-error-openssl-evp-h-no-such-file-or-directory  


2020/11/22  
