# Ollama

官网: https://ollama.com/  
github地址: https://github.com/ollama/ollama  
官方文档: https://github.com/ollama/ollama/tree/main/docs  

下载运行大语言模型，可以离线运行。  


## Windows下安装
默认会安装到C盘，只能通过命令行自定义安装位置：  
```r
.\OllamaSetup.exe /DIR="D:\Ollama"
```

模型默认也会下载到C盘，可以通过设置用户的环境变量 OLLAMA_MODELS 来修改下载位置  
OLLAMA_MODELS: D:\Ollama\models  


## 使用
这里可以搜ollama支持的大模型：  
https://ollama.com/library  

下载运行模型
```r
# 通义千问模型
ollama run qwen2.5:7b
# llama模型
ollama run llama3.2:3b
```

可以用Cherry Studio作为图形化界面。  


## 配置认证
Ollama本身不支持认证，如果需要开放给别人使用，可以使用nginx设置代理，进行限制

```bash
sudo apt install nginx
```

创建或修改 /etc/nginx/conf.d/proxy.conf
```r
server {
    listen 11435;
    server_name _;

    # 默认拒绝所有路径
    location / {
        return 403;
    }

    # 仅允许/v1/chat/completions
    location = /v1/chat/completions {
        # 检查Bearer Token（替换your_token为实际密钥）
        if ($http_authorization != "Bearer your_token") {
            return 401;
        }

        # 代理到本地11434端口
        proxy_pass http://localhost:11434;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

重启nginx：
```bash
sudo systemctl restart nginx
```

配置后可以这样访问：
```bash
curl http://服务器IP:11435/v1/chat/completions -H "Authorization: Bearer your_token"
```

配置方式来自DeepSeek


## 在浏览器打开查看一些信息
```
http://localhost:11434/api/version
http://localhost:11434/api/tags
http://localhost:11434/api/ps
```


## 信息来源
https://www.bilibili.com/video/BV1JTSqYqErn  


---
2024/11/3  
