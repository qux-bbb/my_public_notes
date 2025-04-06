# Open WebUI

官网: https://openwebui.com/  
github地址: https://github.com/open-webui/open-webui  

Open WebUI是一个可扩展、功能丰富、用户友好的自托管AI界面，完全离线操作。它支持各种LLM运行程序，包括Ollama和OpenAI兼容的API。  

可使用pip安装，注意使用Python 3.11以避免兼容性问题：  
```r
pip install open-webui
```

运行：  
```r
open-webui serve
```

默认会监听 0.0.0.0, 如果不想让其他人使用，可以指定host：  
```r
open-webui serve --host 127.0.0.1
```

第一次运行有些依赖要下载，可能会报 `sentence-transformers/all-MiniLM-L6-v2` 相关的错，要挂代理运行一次，之后把代理关了就好了。  
使用语音输入需要下载 WhisperModel, 也是挂代理运行一次就好了。  

删除所有对话记录：  
设置 -> 对话 -> 删除所有对话记录  


2024/11/3  
