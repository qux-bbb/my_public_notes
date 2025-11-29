# Velociraptor

数字取证和事件响应工具，可以本地或远程查看基本信息、文件、注册表，执行命令

github地址: https://github.com/Velocidex/velociraptor  
官方文档: https://docs.velociraptor.app/  
快速开始: https://docs.velociraptor.app/docs/deployment/quickstart/  
故障排除: https://docs.velociraptor.app/docs/troubleshooting/

## 单机使用
```bat
velociraptor-v0.75.5-windows-amd64.exe gui
```

## 服务端和客户端
注意：生成msi客户端安装包可能需要配置代理

### 服务端
1. 服务端生成配置
```bash
./velociraptor-v0.75.5-linux-amd64 config generate -i
```
2. 修改生成的server.config.yaml中的server_urls为服务器IP
```yaml
Client:
  server_urls:
  - https://192.168.116.131:8000/
```
3. 生成安装包
```bash
sudo ./velociraptor-v0.75.5-linux-amd64 debian server --config ./server.config.yaml
```
4. 安装服务端
```bash
sudo dpkg -i velociraptor-server-0.75.5.amd64.deb
```
5. 查看服务状态
```bash
systemctl status velociraptor_server.service
# 如果出现"permission denied"错误，尝试执行以下命令
# sudo chown -R velociraptor:velociraptor /opt/velociraptor
```
6. 确认8889和8000端口提供服务
```bash
nc -vz 127.0.0.1 8889
nc -vz 127.0.0.1 8000
```
7. 登陆管理员界面
```
https://127.0.0.1:8889
```
8. 生成客户端安装包
```bash
# 方法a 界面操作
# 左侧菜单转到"Server Artifacts"
# 搜索"Server.Utils.CreateMSI"
# 一路默认最后点击"Launch"
# 任务完成后，在"Uploaded Files"中下载生成的msi文件

# 方法b 直接执行命令
sudo ./velociraptor-v0.75.5-linux-amd64 debian client --config ./server.config.yaml
```

### 客户端
获取生成的msi安装包，安装即可


## 卸载服务端
```bash
sudo apt purge velociraptor-server
```
