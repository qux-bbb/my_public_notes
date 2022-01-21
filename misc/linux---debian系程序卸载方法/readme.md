# linux---debian系程序卸载方法

debian系比较出名的有ubuntu、kali  

主要为2种卸载方法：  
1. apt
2. dpkg


使用apt的方式有：  
```r
apt-get remove <package>
apt-get remove --purge <package>  # 删除包，包括删除配置文件等
apt-get autoremove --purge  # 自动删除包及其依赖的软件包+配置文件等
```

使用dpkg  
```r
dpkg -r <package>  # 移除一个已安装的包
dpkg -P <package>  # 完全清除一个已安装的包。和 remove 不同的是，remove 只是删掉数据和可执行文件，purge 另外还删除所有的配制文件。
```


来源: http://www.programgo.com/article/98284973120/  


2020/3/11  
