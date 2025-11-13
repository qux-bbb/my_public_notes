# python---远程MCP示例

注意这里的示例没有添加认证功能

python-sdk github地址: https://github.com/modelcontextprotocol/python-sdk

## 配置环境
```bash
uv init mcp-remote-demo
cd mcp-remote-demo
uv add "mcp[cli]" --default-index https://pypi.tuna.tsinghua.edu.cn/simple
```

## 代码
server.py
```python
# https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_config.py

from mcp.server.fastmcp import FastMCP

# Stateful server (maintains session state)
mcp = FastMCP("StatefulServer")

# Other configuration options:
# Stateless server (no session persistence)
# mcp = FastMCP("StatelessServer", stateless_http=True)

# Stateless server (no session persistence, no sse stream with supported client)
# mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)


# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"


# Run server with streamable_http transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

```

client.py
```python
# https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/streamable_basic.py

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
            result = await session.call_tool("greet", arguments={"name": "alice"})
            print(result.model_dump_json())


if __name__ == "__main__":
    asyncio.run(main())

```

## 运行
```bash
uv run server.py
# 另一个窗口
uv run client.py
```
