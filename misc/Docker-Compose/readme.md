# Docker Compose

## 官方介绍
https://docs.docker.com/compose/  

Compose是一个用于定义和运行多容器Docker应用程序的工具。使用Compose，您可以使用YAML文件来配置应用程序的服务。然后，只需一个命令，就可以从配置中创建并启动所有服务。  


## ubuntu安装
Docker的Compose插件和单独的Compose除了执行方式应该没有其它区别  

安装Docker的Compose插件：  
```r
sudo apt-get update
sudo apt-get install docker-compose-plugin

# 查看版本
docker compose version
```

安装单独的Compose：  
```r
sudo curl -SL https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 查看版本
docker-compose version
```


## 一些命令
```r
# 根据配置文件拉取相关镜像
docker compose pull
# 创建并启动容器
docker compose up
# 停止相关容器
docker compose stop
# 启动相关容器
docker compose start
# 停止并删除相关容器
docker compose down
```


---
2023/12/22  
