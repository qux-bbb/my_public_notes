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

可以用Open WebUI作为图形化界面。  


---
2024/11/3  
