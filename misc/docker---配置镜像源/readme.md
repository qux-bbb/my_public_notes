# docker---配置镜像源

docker拉取镜像比较慢，可以自己配置镜像源，虽然也不会多快，可以尝试一下。  

编辑配置文件
```r
sudo vim /etc/docker/daemon.json
```

添加以下内容：  
```json
{
  "registry-mirrors": [
    "https://dockerproxy.com",
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com",
    "https://ccr.ccs.tencentyun.com"
  ]
}
```

重启生效：  
```r
sudo systemctl restart docker
```

查看当前生效信息：  
```r
docker info
```

可能因为docker拉取镜像流量太大，这些源都不太好用，docker官网也找不到第三方源的信息  
测试发现只有 https://ccr.ccs.tencentyun.com 可以用  

如果镜像源效果也不好，暂时能想到的就是挂代理了  


参考链接: https://zhuanlan.zhihu.com/p/670743587  


2023/12/28  
