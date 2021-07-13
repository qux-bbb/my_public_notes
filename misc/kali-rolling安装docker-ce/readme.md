# kali rolling安装docker ce

docker官方的debian系安装方法：  
https://docs.docker.com/engine/installation/linux/docker-ce/debian/  

kali rolling 的 debian 版本为 jessie，部分命令显示的结果也不同，整个过程安装命令如下：    

```bash
# 更新包列表
apt update

# 安装一些包，允许 apt 使用基于 https 的站点
apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common

# 添加 docker 官方 GPG key，可用 apt-key fingerprint 0EBFCD88 看是否添加成功
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

# 在 /etc/apt/sources.list 中添加一行源，出错可以手动添加
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian jessie stable"

# 更新包列表
apt update

# 安装docker-ce
apt install docker-ce
```

其实直接下载安装包通过dpkg来安装也可以，但是找不到安装包...，如果找到安装包会更新这里，安装命令：  
```bash
dpkg -i 安装包
```


2018/1/2  
