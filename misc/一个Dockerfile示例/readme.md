# 一个Dockerfile示例

官方文档: https://docs.docker.com/reference/dockerfile/  


文件名一般是 Dockerfile  

文件内容：  
```dockerfile
# MinerDetect

FROM python:2.7

WORKDIR /home/

# 添加程序代码及样本
ADD code /home/code
ADD sample /home/sample

# 安装所需软件和依赖
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y clamav && \
    pip install -r /home/code/requirements.txt

# 更新clamav病毒库
RUN freshclam

# 清理
RUN apt-get autoremove && apt-get clean

# 开一个bash
ENTRYPOINT [ "/bin/bash" ]
```


2018/5/29  
