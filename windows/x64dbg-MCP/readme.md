# x64dbg MCP

x64dbg-automate支持MCP调用x64dbg

安装文档: https://dariushoule.github.io/x64dbg-automate-pyclient/installation/  
MCP说明: https://dariushoule.github.io/x64dbg-automate-pyclient/mcp-server/

opencode.json 内容
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "x64dbg-mcp-server": {
      "type": "local",
      // Or ["bun", "x", "my-mcp-command"]
      "command": ["x64dbg-automate-mcp"],
      "environment": {
        "X64DBG_PATH": "C:\\Users\\the_user\\Desktop\\snapshot_2024-08-05_13-47\\release\\x96dbg.exe"
      }
    }
  }
}
```
建议放在用户级别的配置文件里：  
%USERPROFILE%\.config\opencode\opencode.json


可以操作，但不太智能，还不如手动操作  
而且，ClaudeCode、OpenCode必须联网，如果调试恶意程序，风险挺高的


信息来源: https://mp.weixin.qq.com/s/iDP_WgGfxvDF4s_K9lak3Q
