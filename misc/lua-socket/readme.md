# lua-socket

安装
```bash
sudo apt install lua5.4
sudo apt install lua-socket
```

命令示例
```bash
lua -e 'local socket=require("socket"); local tcp=socket.tcp(); tcp:settimeout(3); local ok, err = tcp:connect("baidu.com", 80); print(ok and "网络连通正常" or "连接失败: "..err); tcp:close()'
```


2025/8/21
