# nginx

keywords: 反向代理

nginx ("engine x") is an HTTP web server, reverse proxy, content cache, load balancer, TCP/UDP proxy server, and mail proxy server.

官网: https://nginx.org/

nginx.conf配置文件示例部分：
```conf
...
    # 增加bucket大小
    map_hash_bucket_size 128;  # 或更大，如256

    # 定义授权令牌
    map $http_authorization $auth_status {
        default 0;
        "Bearer your-secret-token-here" 1;
    }

    # 定义允许的路径
    map $request_uri $allowed_path {
        default 0;
        "/" 1;
        "/v1/chat/completions" 1;
        "/api/version" 1;
        "/api/tags" 1;
        "/api/ps" 1;
    }

    server {
        listen 11435;

        location / {
            if ($auth_status = 0) {
                return 401 "Unauthorized";
            }

            if ($allowed_path = 0) {
                return 403 "Forbidden - Path not allowed";
            }

            proxy_pass http://localhost:11434;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_buffering off;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
...
```
