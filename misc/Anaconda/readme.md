# Anaconda

Anaconda是一个python环境管理工具，支持比较旧版本的python环境，建议安装miniconda，占用空间较小

官网: https://www.anaconda.com/  
文档地址: https://docs.conda.io/


```bash
# 创建环境
conda create -n myenv
# 指定python版本创建环境
conda create -n myenv python=3.9

# 列出环境
conda env list

# 安装依赖方法1：激活环境后进行安装
# via environment activation
conda activate myenvironment
conda install matplotlib

# 安装依赖方法2：指定环境进行安装
conda install --name myenvironment matplotlib

# 删除环境
conda env remove -n myenv
```


2025/4/19
