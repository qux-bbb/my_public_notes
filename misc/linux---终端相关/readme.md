# linux---终端相关

keywords: 默认shell 当前shell 修改shell 修改终端  

查看当前终端：  
```r
echo $0
```

查看默认终端：  
```r
echo $SHELL
```

查看所有可用终端：  
```r
cat /etc/shells
```

设置默认终端，重启生效：  
```r
chsh -s /bin/zsh
# 修改指定用户的默认终端
chsh -s /bin/zsh username
```

参考链接: https://zhuanlan.zhihu.com/p/672097191  


2020/12/1  
