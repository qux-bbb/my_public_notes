# vLLM

vLLM is a fast and easy-to-use library for LLM inference and serving.

github地址: https://github.com/vllm-project/vllm  
官方文档: https://docs.vllm.ai/  

要求：
1. OS: Linux
2. Python: 3.9 – 3.12
3. 至少8G内存

对于NVIDIA GPU，可以直接使用pip安装  
**其他需要[从源码安装](#从源码安装)**


## 快速开始
安装：
```bash
pip install vllm
```

指定模型，启动一个提供OpenAI API的服务：
```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

测试api：
```bash
curl http://localhost:8000/v1/models
```

本地测试：
```bash
vllm chat
```


## 使用modelscope下载模型
如果连huggingface有问题，可以使用modelscope下载模型  
By default, vLLM downloads models from [HuggingFace](https://huggingface.co/). If you would like to use models from [ModelScope](https://www.modelscope.cn/), set the environment variable `VLLM_USE_MODELSCOPE` before initializing the engine.
```bash
pip install modelscope
export VLLM_USE_MODELSCOPE=True
```


## 认证
You can pass in the argument `--api-key` or environment variable `VLLM_API_KEY` to enable the server to check for API key in the header.

提供服务示例：
```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct --api-key SECRET
```

测试认证：
```bash
curl -H "Authorization: Bearer SECRET" http://localhost:8000/v1/models
```


## 默认模型位置
```r
/home/alice/.cache/huggingface
/home/alice/.cache/modelscope
```

## 从源码安装
使用uv创建隔离python环境并进入
```bash
# (Recommended) Create a new uv environment. Use `--seed` to install `pip` and `setuptools` in the environment.
# 如果后续构建时出现这样的错误：
# Could NOT find Python (missing: Python_INCLUDE_DIRS Interpreter Development.Module Development.SABIModule)
# 可以把3.12改为3.12.0
uv venv vllm --python 3.12 --seed
source vllm/bin/activate
```

安装编译工具
```bash
sudo apt-get update  -y
sudo apt-get install -y gcc-12 g++-12 libnuma-dev
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12
```

克隆项目
```bash
git clone https://github.com/vllm-project/vllm.git vllm_source
cd vllm_source
```

安装python依赖
```bash
pip install --upgrade pip
pip install "cmake>=3.26" wheel packaging ninja "setuptools-scm>=8" numpy
pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

构建并安装
```bash
VLLM_TARGET_DEVICE=cpu python setup.py install
```
