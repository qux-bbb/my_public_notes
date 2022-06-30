# apt-get和dpkg

## 0x00 扯
kali基于debian，安装软件还是挺方便的，  
dpkg、apt-get、apt傻傻搞不清楚，dpkg比较下层，apt-get比较上层，apt做了进一步的优化  


## 0x01 dpkg
dpkg: Debian package manager  
主要用来安装本地deb包和卸载包，了解几个简单的吧，够用就可以  
```r
dpkg -i aa.deb  # 安装
dpkg -r aa  # 移除软件，保留配置
dpkg -P aa  # 移除软件，不保留配置
```


## 0x02 apt-get
apt-get: Advanced Package Tool  
主要用来在线安装升级包，或者卸载什么的，可以解决大部分依赖问题  

命令例子大概是这样，比如要安装 aa，那么就是：  
`apt-get install aa`  

下面是一些常用命令选项：  
```r
update - 取回更新的软件包列表信息
upgrade - 进行一次升级
install - 安装新的软件包
remove - 卸载软件包
purge - 卸载并清除软件包的配置
autoremove - 卸载所有自动安装且不再使用的软件包
dist-upgrade - 发布版升级
clean - 删除所有已下载的包文件
autoclean - 删除已下载的旧包文件
```

如果安装一个软件出现了依赖问题，那就可以执行下面这条命令，再去安装软件，一般依赖问题就会解决了  
```r
# 自动解决依赖问题的命令
apt-get -f -y install
```

下载包和相关依赖，用于离线安装，举例：  
```r
apt-get install -d openssh-server
```
下载的包放在 `/var/cache/apt/archives` 路径下  


## 0x03 apt
apt专为交互式使用而设计，提高了可用性，一般操作把apt当成apt-get用就可以，比如：  
`apt install aa`  

日常使用更推荐apt，自带进度条，不用敲那么多  
如果在脚本或shell管道中，还是应该使用apt-get  


## 0x04 尾
我的经验，  
apt-get是用来安装那些源里有的软件，dpkg用来安装下载好的.deb安装包  
apt-get安装一般不用担心依赖问题  


## 0x05 参考链接
https://www.linuxprobe.com/aptyum-dnfpkg-diff.html  
