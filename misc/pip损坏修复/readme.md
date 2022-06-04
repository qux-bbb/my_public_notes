# pip损坏修复

有时候pip会报这样的错:  
```r
Traceback (most recent call last):
  File "/usr/local/bin/pip", line 7, in <module>
    from pip._internal.main import main
ImportError: No module named main
```

解决方法就是重装:  
```r
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py --force-reinstall
```


原链接: https://blog.csdn.net/github_39533414/article/details/90319560  


2020/4/14  
