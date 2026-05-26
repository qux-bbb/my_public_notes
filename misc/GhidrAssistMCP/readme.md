# GhidrAssistMCP

An native MCP server extension for Ghidra

https://github.com/symgraph/GhidrAssistMCP

opencode.json 内容
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "ghidrassist": {
      "type": "remote",
      "url": "http://localhost:8080/mcp",
      "enabled": true
    }
  }
}
```
建议放在用户级别的配置文件里：  
%USERPROFILE%\.config\opencode\opencode.json
