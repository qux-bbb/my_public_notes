# RustDesk

RustDesk是一个开源的远程桌面访问软件，支持 Windows、macOS、Linux、iOS、Android、Web 等多个平台。  

官网: https://rustdesk.com/  

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


---
2024/8/25  
