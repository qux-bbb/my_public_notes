# docker入门

## 官方介绍
https://docs.docker.com/get-started/overview/  

Docker 是一个用于开发、发布和运行应用程序的开放平台。 Docker 使您能够将应用程序与基础架构分离，以便 您可以快速交付软件。使用 Docker，您可以管理您的基础架构 以管理应用程序的相同方式。通过利用 Docker 的 用于交付、测试和部署代码的方法，您可以 显著减少编写代码和在生产环境中运行代码之间的延迟。  

大概就是在一个相对隔离的环境快速部署应用。  


## ubuntu安装
https://docs.docker.com/engine/install/ubuntu/  

```r
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install Docker
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# run hello-world to verify
sudo docker run hello-world
```

非root用户管理docker  
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user  
```r
# Create the docker group.
sudo groupadd docker
# Add your user to the docker group.
sudo usermod -aG docker $USER
# 重启或使用该命令生效:
newgrp docker
# run hello-world to verify
docker run hello-world
```


## 一些命令
```bash
# 以可交互，模拟终端的方式从一个镜像创建一个容器
# -i        可交互
# -t        模拟终端
# --name    起的名字
docker run -it -p 4000:4000 --name testCTFd ec0 /bin/bash

# 启动一个名为forCTFd的容器（可交互方式）
docker start -i forCTFd

# 停止名为forCTFd的容器
docker stop forCTFd

# 从容器创建一个新的镜像，以保存当前配置
docker commit -a "author" -m "description" 21b hello/world:v1

# 删除容器
docker rm 21b

# 删除镜像
docker rmi 21b

# 查看正在运行的容器
docker ps

# 查看所有容器
docker ps -a

# 查看镜像
docker images

# 复制容器内文件到本机(文件夹也可以)
docker cp 03091bf3d393:/root/a.txt ./

# 交互方式进入已运行的容器
docker exec -it 24ca03d94e9f /bin/bash

# 容器重命名(a重命名为b)
docker rename a b

# 查看容器配置参数并找出ip地址
docker inspect 2b1 | grep IPAddress

# 从Dockerfile创建镜像，指定tag和Dockerfile路径
docker build -t hello:v1.1 -f /whatever/Dockerfile .
# 可以什么参数都不指定，默认读取当前目录下的Dockerfile
docker build .

# 保存一个镜像保存到文件
docker save -o <输出文件路径>.tar <镜像名称>:<标签>

# 保存多个镜像保存到文件
docker save -o multiple_images.tar image1:image1tag image2:image2tag

# 从文件加载镜像
docker load -i <文件路径>.tar
```


## image和container的关系
Image可以理解为一个系统镜像，  
Container是根据Image创建的实例。  

如果拿虚拟机作一个比喻的话，  
Image就是iso镜像文件，  
Container就是根据镜像创建的虚拟机(这个虚拟机可以被启动、停止，但没有创建快照的功能)。  


---
2017/9/2  
