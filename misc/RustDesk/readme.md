# RustDesk

RustDesk是一个开源的远程桌面访问软件，支持 Windows、macOS、Linux、iOS、Android、Web 等多个平台。  

官网: https://rustdesk.com/  
github地址: https://github.com/rustdesk/rustdesk

## 在ubuntu22自建服务器
官方有免费的服务器，也可以自建服务器
```bash
sudo docker image pull rustdesk/rustdesk-server
sudo docker run --name hbbs -v ./data:/root -td --net=host --restart unless-stopped rustdesk/rustdesk-server hbbs
sudo docker run --name hbbr -v ./data:/root -td --net=host --restart unless-stopped rustdesk/rustdesk-server hbbr
```

查看key：  
```bash
docker logs hbbs
```
形似 `Key: ABCDE..=` 就是key  

打开RustDesk客户端，设置->网络->解锁网络设置  
`ID 服务器` 填写ubuntu的ip  
`Key` 填写刚刚看到的key  

这样就可以连接配置了该服务器的客户端  


## 在阿里云的ubuntu22自建服务器

如果在阿里云拉取docker镜像，可能拉取的是几年前的，使用 `docker logs hbbs` 查看日志报错如下：
```log
[2023-01-30T12:32:30Z ERROR hbbs::lic] Registered email required (-m option). Please pay and register on https://rustdesk.com/server.
```
相关链接: https://github.com/rustdesk/rustdesk-server/issues/184

如果有这样的错误，建议用这样的步骤：
1. 安装干净的的ubuntu22，不要带docker
2. 装v2raya代理(注意设置强密码)，添加入方向规则：自定义TCP 2017端口，设置绕过大陆地址
3. 安装docker，配置rustserver
    ```bash
    bash <(wget -qO- https://get.docker.com)
    wget rustdesk.com/oss.yml -O compose.yml
    sudo docker compose up -d
    ```
4. 添加入方向规则：自定义TCP 21114/21119, 自定义UDP 21116/21116

由于阿里云默认只允许22、3389、ICMP，所以不需要启用ufw


---
2024/8/25  
