# Dify

官方宣传：开源的 LLM 应用开发平台。提供从 Agent 构建到 AI workflow 编排、RAG 检索、模型管理等能力，轻松构建和运营生成式 AI 原生应用。比 LangChain 更易用。

Dify = Define + Modify, referring to defining and continuously improving your AI applications.

官网: https://dify.ai/  
官方文档: https://docs.dify.ai/


## 自部署
https://docs.dify.ai/getting-started/install-self-hosted/docker-compose

硬件要求：
```r
CPU >= 2 Core
RAM >= 4 GiB
```

Linux平台docker版本要求：
```r
Docker 19.03 or later
Docker Compose 1.28 or later
```

安装：
```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
```

之后访问 http://localhost/install 配置登陆即可，邮箱可以不是真实地址


---
2025/3/30
