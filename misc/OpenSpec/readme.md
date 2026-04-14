# OpenSpec

Spec-driven development (SDD) for AI coding assistants.  
Spec, Specification, 规范。  
设定规范指导开发，确保代码质量和可维护性。

官网: https://openspec.dev/  
github地址: https://github.com/Fission-AI/OpenSpec

初始化项目
```bash
cd your-project
openspec init
```

## 切换语言
https://github.com/Fission-AI/OpenSpec/blob/main/docs/multi-language.md

修改 openspec/config.yaml, 添加内容：
```yaml
context: |
  语言：中文（简体）
  所有产出物必须用简体中文撰写。
```

## 扩展功能
OpenSpec默认是这样：
```
/opsx:propose ──► /opsx:apply ──► /opsx:archive
```

可以通过 `openspec config profile` 和 `openspec update` 扩展成这样或其他自定义的样子
```
/opsx:new ──► /opsx:ff or /opsx:continue ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive
```
