## 0x00 扯
kali基于debian，安装软件还是挺方便的，  
apt-get和dpkg傻傻搞不清楚，貌似dpkg比较下层，apt-get比较上层  
```
dpkg: package manager for Debian
apt-get: Advanced Package Tool
```


## 0x01  apt-get
命令例子大概是这样，比如要安装 aa，那么就是：  
`apt-get  install  aa`  

下面是一些常用命令选项：  
```
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

自动解决依赖问题的命令：  
```bash
apt-get -f -y install
```
如果安装一个软件出现了依赖问题，那就可以执行这条命令，再去安装软件，一般依赖问题就会解决了  

下载包和相关依赖，用于离线安装，举例：  
```bash
apt install -d openssh-server
```
下载的包放在 `/var/cache/apt/archives` 路径下  

apt和apt-get没什么太大区别，把apt当成apt-get用就可以，比如：  
`apt install aa`  

其实更推荐用apt，自带进度条，而且不用敲那么多呀，哈  


## 0x02 dpkg
了解几个简单的吧，够用就可以  
```bash
dpkg -i aa.deb  # 安装
dpkg -r aa  # 移除软件，保留配置
dpkg -P aa  # 移除软件，不保留配置
```


## 0x03 尾
我的经验，  
apt-get是用来安装那些源里有的软件，dpkg用来安装下载好的.deb安装包  
apt-get安装一般不用担心依赖问题  
