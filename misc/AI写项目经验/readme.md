# AI写项目经验

```bash
cd my_project
openspec init
# 选择OpenCode

修改 openspec/config.yaml, 添加内容：
context: |
  语言：中文（简体）
  所有产出物必须用简体中文撰写。

openspec config profile
选择：
opsx:new
opsx:continue
opsx:apply
opsx:verify
opsx:archive

openspec update

创建AGENTS.md文件，添加内容:
1. 用中文写文档和代码注释
2. 判断操作系统，确保只执行对应操作系统下的命令(如windows下执行powershell、cmd命令，不要执行bash命令)
3. 如果涉及到删除.git文件夹，必须由用户确认

OpenCode打开项目

切换为Plan模式聊需求

OpenSpec建提案，改文档，编码，验证，归档记录
opsx:new <需求名称>
opsx:continue
# 调整生成的openspec相关文件
opsx:apply
opsx:verify
opsx:archive
```
