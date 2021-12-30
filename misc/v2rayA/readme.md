# v2rayA

Qv2ray不维护了，发现了v2rayA。  
一个易用而强大的，专注于 Linux 的 V2Ray 客户端。  

https://v2raya.org/  

## kubuntu安装
安装V2Ray：  
```r
# v2rayA 提供的镜像脚本
curl -Ls https://mirrors.v2raya.org/go.sh | sudo bash
# 安装后可以关掉服务，因为 v2rayA 不依赖于该 systemd 服务。
sudo systemctl disable v2ray --now ### Xray 需要替换服务为 xray
```

安装 v2rayA：  
```r
# 获取并添加公钥
curl -s https://apt.v2raya.mzz.pub/key/public-key.asc | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/v2raya.gpg --import
# 修改所有者
sudo chown _apt /etc/apt/trusted.gpg.d/v2raya.gpg

# 添加 V2RayA 软件源
echo "deb https://apt.v2raya.mzz.pub/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list
sudo apt update
# 安装 V2RayA
sudo apt install v2raya
```

启动 v2rayA / 设置 v2rayA 自动启动  
```r
# 启动 v2rayA
sudo systemctl start v2raya.service
# 设置开机自动启动
sudo systemctl enable v2raya.service
```

然后可以访问: http://localhost:2017  
创建账号、导入节点、启动服务，开始使用  


参考链接：  
1. https://v2raya.org/docs/prologue/installation/debian/
2. https://stackoverflow.com/questions/68992799/warning-apt-key-is-deprecated-manage-keyring-files-in-trusted-gpg-d-instead


---
2021/12/30  
