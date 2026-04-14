# AGENTS.md

在项目根目录写AGENTS.md文件，约束大模型的行为。

官网: https://agents.md/  
github地址: https://github.com/agentsmd/agents.md

示例：
```md
# AGENTS.md

1. 用中文写文档和代码注释
2. 判断操作系统，确保只执行对应操作系统下的命令(如windows下执行powershell、cmd命令，不要执行bash命令)
3. 如果涉及到删除.git文件夹，必须由用户确认
```