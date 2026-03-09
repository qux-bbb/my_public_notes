# llama.cpp

keywords: ollama

llama.cpp是用C/C++实现的LLM推理工具，可以对话，提供API接口

github地址: https://github.com/ggml-org/llama.cpp

github release太频繁了，所以不关注release了

Windows安装，也可以用这条命令升级
```r
winget install llama.cpp
```

从huggingface下载使用模型
```bash
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
llama-cli -hf unsloth/Qwen3.5-9B-GGUF
# https://huggingface.co/unsloth/Qwen3.5-9B-GGUF
# https://www.modelscope.cn/models/unsloth/Qwen3.5-9B-GGUF
```

设置环境变量从modelscope下载模型
```r
MODEL_ENDPOINT=https://www.modelscope.cn/
```

启动llama-server，可以在浏览器中访问 http://localhost:8080
```bash
llama-server
```

llama-server设置api-key
```bash
llama-server --api-key hello
# 多个key用逗号隔开
llama-server --api-key hello,world
```
