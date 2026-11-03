# DeepSeek Harness

DeepSeek官方的类似Codex、ZCode的智能体工具

官网: https://www.deepseek.com/harness/

没有ask模式，但是可以把权限改为“仅可查看”

密钥存储位置
```r
$DSH_HOME/.credentials.yaml
# Windows下通常对应
%USERPROFILE%\.dsh\.credentials.yaml
```

思考过程机器翻译 是DSH内置试验性插件，挺好用的

dsh-mnemon是一个DSH插件，提供记忆功能  
https://github.com/omdsh-dev/dsh-mnemon/blob/main/README.zh-CN.md


想要的功能：
1. 打开远端linux机器的目录、本地wsl的目录作为工作区
2. 连接MCP
4. 侧边对话
