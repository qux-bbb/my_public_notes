# llama.cpp

keywords: ollama

LLM inference in C/C++

github地址: https://github.com/ggml-org/llama.cpp

Windows安装
```r
winget install llama.cpp
```

从huggingface下载使用模型
```bash
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF
llama-cli -hf unsloth/Qwen3.5-9B-GGUF
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
