# docker---配置域名解析

以ubuntu22.04作为基础镜像，build新的镜像，在执行 `apt-get update` 命令时，出现以下错误：  
```r
167.4 Err:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
167.4   Temporary failure resolving 'security.ubuntu.com'
```

搜索错误信息，发现是域名解析问题，可以通过配置永久解决该问题  

编辑配置文件
```r
sudo vim /etc/docker/daemon.json
```

添加以下内容：  
```json
{
    "dns": ["8.8.8.8"]
}
```

重启生效：  
```r
sudo systemctl restart docker
```


参考链接: https://medium.com/@faithfulanere/solved-docker-build-could-not-resolve-archive-ubuntu-com-apt-get-fails-to-install-anything-9ea4dfdcdcf2  


2024/4/18  
