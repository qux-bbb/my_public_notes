# docker入门

官网下载地址：https://www.docker.com/community-edition#/download  
安装后，命令行执行 docker，确认安装成功  

一些命令  
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

# 将容器导出到一个tar文件
docker export 21b -o testCTFd.tar

# 从tar文件恢复一个镜像
cat testCTFd.tar | docker import - test/ubuntu

# 复制容器内文件到本机(文件夹也可以)
docker cp 03091bf3d393:/root/a.txt ./

# 交互方式进入已运行的容器
docker exec -it 24ca03d94e9f /bin/bash

# 容器重命名(a重命名为b)
docker rename a b

# 查看容器配置参数并找出ip地址
docker inspect 2b1 | grep IPAddress

# 从Dockerfile创建镜像
docker build -t hello:v1.1 -f /whatever/Dockerfile
```

## image和container的区别
Image可以理解为一个系统镜像，  
Container是Image在运行时的一个状态。  

如果拿虚拟机作一个比喻的话，  
Image就是关机状态下的磁盘文件，  
Container就是虚拟机运行时的磁盘文件，包括内存数据。  


2017/9/2  
