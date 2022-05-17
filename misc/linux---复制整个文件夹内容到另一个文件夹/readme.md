# linux---复制整个文件夹内容到另一个文件夹

错误命令，`*` 并不是全部，不会复制隐藏文件：  
```r
cp /home/test/* /home/test2/
```

一种正确的命令：  
```r
cp -r /home/test/ /home/test2/
```


2020/6/25  
